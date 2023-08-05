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
  TBF Reader
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
		unsigned int frameCountWord;
	};
	unsigned int secondsCount;
	signed short int firstChan;
	signed short int unassigned;
} TBFHeader;


typedef struct {
	signed long long timeTag;
	unsigned char bytes[6144];
} TBFPayload;


typedef struct {
	TBFHeader header;
	TBFPayload data;
} TBFFrame;
#pragma pack(pop)


PyObject *tbf_method = NULL;
PyObject *tbf_size   = NULL;


PyObject *readTBF(PyObject *self, PyObject *args) {
	PyObject *ph, *buffer, *output, *frame, *fHeader, *fData, *temp;
	PyArrayObject *data;
	int i;
	TBFFrame cFrame;
	
	if(!PyArg_ParseTuple(args, "OO", &ph, &frame)) {
		PyErr_Format(PyExc_RuntimeError, "Invalid parameters");
		return NULL;
	}
	
	// Create the output data array
	npy_intp dims[3];
	// 4+4-bit Data -> 6144 samples in the data section as 12 channels, 256 stands, and 2 pols.
	dims[0] = (npy_intp) 12;
	dims[1] = (npy_intp) 256;
	dims[2] = (npy_intp) 2;
	data = (PyArrayObject*) PyArray_ZEROS(3, dims, NPY_COMPLEX64, 0);
	if(data == NULL) {
		PyErr_Format(PyExc_MemoryError, "Cannot create output array");
		Py_XDECREF(data);
		return NULL;
	}

	// Read from the file
	if( tbf_method == NULL ) {
		tbf_method = Py_BuildValue("s", "read");
		tbf_size = Py_BuildValue("i", sizeof(cFrame));
	}
	buffer = PyObject_CallMethodObjArgs(ph, tbf_method, tbf_size, NULL);
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
	cFrame.header.firstChan = __bswap_16(cFrame.header.firstChan);
	cFrame.data.timeTag = __bswap_64(cFrame.data.timeTag);
	
	// Fill the data array
	const float *fp;
	float complex *a;
	a = (float complex *) PyArray_DATA(data);
	for(i=0; i<6144; i++) {
		fp = tbfLUT[ cFrame.data.bytes[i] ];
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
	// 1.  Header
	fHeader = PyObject_GetAttrString(frame, "header");
	
	temp = Py_BuildValue("B", cFrame.header.id);
	PyObject_SetAttrString(fHeader, "id", temp);
	Py_XDECREF(temp);
	
	temp = PyLong_FromUnsignedLong(cFrame.header.frameCount);
	PyObject_SetAttrString(fHeader, "frameCount", temp);
	Py_XDECREF(temp);
	
	temp = PyLong_FromUnsignedLong(cFrame.header.secondsCount);
	PyObject_SetAttrString(fHeader, "secondsCount", temp);
	Py_XDECREF(temp);
	
	temp = Py_BuildValue("h", cFrame.header.firstChan);
	PyObject_SetAttrString(fHeader, "firstChan", temp);
	Py_XDECREF(temp);
	
	// 2. Data
	fData = PyObject_GetAttrString(frame, "data");
	
	temp = PyLong_FromLongLong(cFrame.data.timeTag);
	PyObject_SetAttrString(fData, "timeTag", temp);
	Py_XDECREF(temp);
	
	PyObject_SetAttrString(fData, "fDomain", PyArray_Return(data));
	
	// 3. Frame
	PyObject_SetAttrString(frame, "header", fHeader);
	PyObject_SetAttrString(frame, "data", fData);
	output = Py_BuildValue("O", frame);
	
	Py_XDECREF(fHeader);
	Py_XDECREF(fData);
	Py_XDECREF(data);
	
	return output;
}

char readTBF_doc[] = PyDoc_STR(\
"Function to read in a single TBW frame (header+data) and store the contents\n\
as a Frame object.\n\
\n\
.. versionadded:: 1.2.0\n\
");
