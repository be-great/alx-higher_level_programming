#include <stdio.h>
#include <Python.h>

/**
* print_python_bytes - functions that print some basic info about
* python bytes object
* discription: check if python object is type sbytes (string in python)
* varaible : lable name of the object , value (object value)
* @p: Python bytes object
*/
void print_python_bytes(PyObject *p)
{
	char *byte_string;
	long int size, i;
	long int limit;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	byte_string = PyBytes_AsString(p);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", byte_string);

	limit = (size >= 10) ? 10 : size + 1;

	printf("  first %ld bytes:", limit);

	for (i = 0; i < limit; i++)
		printf(" %02x", (unsigned char)byte_string[i]);

	printf("\n");
}

/**
* print_python_list - functions that print some basic info about
* python list object
* @p: Python list object
* Return: No return
*/
void print_python_list(PyObject *p)
{
	long int size, i;

	PyListObject *list;
	PyObject *list_item;

	size = PyList_Size(p);
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		list_item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(list_item)->tp_name);

		if (PyBytes_Check(list_item))
			print_python_bytes(list_item);
	}
}
