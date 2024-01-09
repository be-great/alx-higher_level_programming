#include <Python.h>
#include <listobject.h>
#include <object.h>

void print_python_list_info(PyObject *p)
{
	long int len;
	int i;
	PyListObject *obj;

	thesize = PyList_Size(p);
	pyobj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", len);
	printf("[*] Allocated = %li\n", pyobj->allocated);
	for (i = 0; i < len; i++)
	{
		printf("Element %i: %s\n", i, Py_TYPE(pyobj->ob_item[i])->tp_name);
	}
}
