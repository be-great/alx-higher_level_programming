#include <stdio.h>
#include <Python.h>

/**
* print_python_bytes - Prints bytes object information
*
* @bytes_obj: Python bytes object
* Return: No return
*/
void print_python_bytes(PyObject *bytes_obj)
{
	char *byte_string;

	long int size, i, limit;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(bytes_obj))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_GET_SIZE(bytes_obj);
	byte_string = PyBytes_AS_STRING(bytes_obj);
	limit = (size >= 10) ? 10 : size + 1;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", byte_string);
	printf("  first %ld bytes:", limit);

	for (i = 0; i < limit; i++)
		printf(" %02x", (unsigned char)byte_string[i]);

	printf("\n");
}

/**
* print_python_list - Prints list information
*
* @list_obj: Python list object
* Return: No return
*/
void print_python_list(PyObject *list_obj)
{
	long int size, i;
	PyListObject *list;
	PyObject *list_item;

	size = Py_SIZE(list_obj);
	list = (PyListObject *)list_obj;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		list_item = PyList_GetItem(list_obj, i);
		printf("Element %ld: %s\n", i, Py_TYPE(list_item)->tp_name);
		if (PyBytes_Check(list_item))
			print_python_bytes(list_item);
	}
}
