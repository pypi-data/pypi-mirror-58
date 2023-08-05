#include "Python.h"
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <complex.h>

#if defined(__linux__)
/* Linux */
#include <byteswap.h>
#elif defined(__APPLE__) && defined(__MACH__)
/* OSX */
#include <libkern/OSByteOrder.h>
#define __bswap_16 OSSwapInt16
#define __bswap_32 OSSwapInt32
#define __bswap_64 OSSwapInt64
#endif

#define NO_IMPORT_ARRAY
#define PY_ARRAY_UNIQUE_SYMBOL gofast_ARRAY_API
#include "numpy/arrayobject.h"

#include "readers.h"

/*
  DRX Reader
*/

#pragma pack(push)
#pragma pack(1)
typedef struct {
	unsigned int syncWord;
	union {
		struct {
			unsigned int frameCount:24;
			unsigned char id:8;
		};
		/* Also: 
			struct {
				unsigned int frameCount:24;
				unsigned char beam:3;
				unsigned char tune:3;
				unsigned char reserved:1;
				unsigned char pol:1;
			};
		*/
		unsigned int frameCountWord;
	};
	unsigned int secondsCount;
	unsigned short int decimation;
	unsigned short int timeOffset;
} DRXHeader;


typedef struct {
	unsigned long long timeTag;
	unsigned int tuningWord;
	unsigned int flags;
	unsigned char bytes[4096];
} DRXPayload;


typedef struct {
	DRXHeader header;
	DRXPayload data;
} DRXFrame;
#pragma pack(pop)


PyObject *drx_method = NULL;
PyObject *drx_size   = NULL;


PyObject *readDRX(PyObject *self, PyObject *args) {
	PyObject *ph, *buffer, *output, *frame, *fHeader, *fData, *temp;
	PyArrayObject *data;
	int i;
	DRXFrame cFrame;
	
	if(!PyArg_ParseTuple(args, "OO", &ph, &frame)) {
		PyErr_Format(PyExc_RuntimeError, "Invalid parameters");
		return NULL;
	}
	
	// Create the output data array
	npy_intp dims[1];
	dims[0] = (npy_intp) 4096;
	data = (PyArrayObject*) PyArray_ZEROS(1, dims, NPY_COMPLEX64, 0);
	if(data == NULL) {
		PyErr_Format(PyExc_MemoryError, "Cannot create output array");
		Py_XDECREF(data);
		return NULL;
	}
	
	// Read from the file
	if( drx_method == NULL ) {
		drx_method = Py_BuildValue("s", "read");
		drx_size = Py_BuildValue("i", sizeof(cFrame));
	}
	buffer = PyObject_CallMethodObjArgs(ph, drx_method, drx_size, NULL);
	if( buffer == NULL ) {
		if( PyObject_HasAttrString(ph, "read") ) {
			PyErr_Format(PyExc_IOError, "An error occured while reading from the file");
		} else {
			PyErr_Format(PyExc_AttributeError, "Object does not have a read() method");
		}
		Py_XDECREF(data);
		return NULL;
	} else if( PyString_GET_SIZE(buffer) != sizeof(cFrame) ) {
		PyErr_Format(eofError, "End of file encountered during filehandle read");
		Py_XDECREF(data);
		Py_XDECREF(buffer);
		return NULL;
	}
	memcpy(&cFrame, PyString_AS_STRING(buffer), sizeof(cFrame));
	Py_XDECREF(buffer);
	
	Py_BEGIN_ALLOW_THREADS
	
	// Swap the bits around
	cFrame.header.frameCountWord = __bswap_32(cFrame.header.frameCountWord);
	cFrame.header.secondsCount = __bswap_32(cFrame.header.secondsCount);
	cFrame.header.decimation = __bswap_16(cFrame.header.decimation);
	cFrame.header.timeOffset = __bswap_16(cFrame.header.timeOffset);
	cFrame.data.timeTag = __bswap_64(cFrame.data.timeTag);
	cFrame.data.tuningWord = __bswap_32(cFrame.data.tuningWord);
	cFrame.data.flags = __bswap_32(cFrame.data.flags);
	
	// Fill the data array
	const float *fp;
	float complex *a;
	a = (float complex *) PyArray_DATA(data);
	for(i=0; i<4096; i++) {
		fp = drxLUT[ cFrame.data.bytes[i] ];
		*(a + i) = fp[0] + _Complex_I * fp[1];
	}
	
	Py_END_ALLOW_THREADS
	
	// Validate
	if( !validSync5C(cFrame.header.syncWord) ) {
		PyErr_Format(syncError, "Mark 5C sync word differs from expected");
		Py_XDECREF(data);
		return NULL;
	}
	
	// Save the data to the frame object
	// 1. Header
	fHeader = PyObject_GetAttrString(frame, "header");
	
	temp = PyLong_FromUnsignedLong(cFrame.header.frameCount);
	PyObject_SetAttrString(fHeader, "frameCount", temp);
	Py_XDECREF(temp);
	
	temp = Py_BuildValue("B", cFrame.header.id);
	PyObject_SetAttrString(fHeader, "drxID", temp);
	Py_XDECREF(temp);
	
	temp = PyLong_FromUnsignedLong(cFrame.header.secondsCount);
	PyObject_SetAttrString(fHeader, "secondsCount", temp);
	Py_XDECREF(temp);
	
	temp = Py_BuildValue("H", cFrame.header.decimation);
	PyObject_SetAttrString(fHeader, "decimation", temp);
	Py_XDECREF(temp);
	
	temp = Py_BuildValue("H", cFrame.header.timeOffset);
	PyObject_SetAttrString(fHeader, "timeOffset", temp);
	Py_XDECREF(temp);
	
	// 2. Data
	fData = PyObject_GetAttrString(frame, "data");
	
	temp = PyLong_FromUnsignedLongLong(cFrame.data.timeTag);
	PyObject_SetAttrString(fData, "timeTag", temp);
	Py_XDECREF(temp);
	
	temp = PyLong_FromUnsignedLong(cFrame.data.tuningWord);
	PyObject_SetAttrString(fData, "tuningWord", temp);
	Py_XDECREF(temp);
	
	temp = PyLong_FromUnsignedLong(cFrame.data.flags);
	PyObject_SetAttrString(fData, "flags", temp);
	Py_XDECREF(temp);
	
	PyObject_SetAttrString(fData, "iq", PyArray_Return(data));
	
	// 3. Frame
	PyObject_SetAttrString(frame, "header", fHeader);
	PyObject_SetAttrString(frame, "data", fData);
	output = Py_BuildValue("O", frame);
	
	Py_XDECREF(fHeader);
	Py_XDECREF(fData);
	Py_XDECREF(data);
	
	return output;
}

char readDRX_doc[] = PyDoc_STR(\
"Function to read in a single DRX frame (header+data) and store the contents\n\
as a Frame object.  This function serves as a replacement for the pure python\n\
reader lsl.reader.drx.readFrame.\n\
\n\
In order to use this reader in place of lsl.reader.drx.readFrame change:\n\
\n\
\t>>> import lsl.reader.tbn as drx\n\
\t>>> fh = open('some-drx-file.dat', 'rb')\n\
\t>>> frame = drx.readFrame(fh)\n\
\n\
to:\n\
\n\
\t>>> import lsl.reader.drx as drx\n\
\t>>> from lsl.reader._gofast import ReadDRX, syncError, eofError\n\
\t>>> fh = open('some-drx-file.dat', 'rb')\n\
\t>>> frame = readDRX(fh, tbn.Frame())\n\
\n\
In addition, the exceptions checked for in the try...except blocks wrapping the\n\
frame reader need to be changed to 'IOError' since syncError and eofError are\n\
are sub-classes of IOError.\n\
\n\
.. versionchanged:: 0.4.0\n\
\tThe Go Fast! readers are the default readers used by the :mod:`lsl.reader.drx`\n\
\tmodule.\n\
");
