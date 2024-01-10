#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <Python.h>

/**
* print_python_list - Print information about Python lists
* @p: PyObject pointer to a Python list
*/
void print_python_list(PyObject *p)
{
	Py_ssize_t i, size;
	PyListObject *list;

	if (!PyList_Check(p))
	{
		fprintf(stderr, "[*] Python list info\n");
		fprintf(stderr, "  [ERROR] Invalid List Object\n");
		return;
	}

	list = (PyListObject *)p;
	size = Py_SIZE(list);

	fprintf(stderr, "[*] Python list info\n");
	fprintf(stderr, "[*] Size of the Python List = %ld\n", size);
	fprintf(stderr, "[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; ++i)
	{
		fprintf(stderr, "Element %ld: %s\n", i,
				Py_TYPE(PyList_GetItem(p, i))->tp_name);
		if (PyBytes_Check(PyList_GetItem(p, i)))
			print_python_bytes(PyList_GetItem(p, i));
	}
}

/**
* print_python_bytes - Print information about Python bytes objects
* @p: PyObject pointer to a Python bytes object
*/
void print_python_bytes(PyObject *p)
{
	Py_ssize_t i, size;
	PyBytesObject *bytes;

	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "[.] bytes object info\n");
		fprintf(stderr, "  [ERROR] Invalid Bytes Object\n");
		return;
	}

	bytes = (PyBytesObject *)p;
	size = Py_SIZE(bytes);

	fprintf(stderr, "[.] bytes object info\n");
	fprintf(stderr, "  size: %ld\n", size);
	fprintf(stderr, "  trying string: %s\n", PyBytes_AS_STRING(p));

	fprintf(stderr, "  first 10 bytes: ");
	for (i = 0; i < size && i < 10; ++i)
	{
		fprintf(stderr, "%02x", (unsigned char)PyBytes_AS_STRING(p)[i]);

		if (i < 9 && i < size - 1)
			fprintf(stderr, " ");
	}
	fprintf(stderr, "\n");
}

