#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	long int len, x;
	PyListObject *pyobj; 
	pyobj = (PyListObject *)p;
	const char *str;
	
	len = PyList_Size(p);
	printf("[*] Size of the Python List = %li\n", len);
	printf("[*] Allocated = %li\n", pyobj->allocated);
	for (x = 0; x < len; x++)
	{
		str = Py_TYPE(pyobj->ob_item[x])->tp_name;
		printf("Element %i: %s\n", x, str);
	}
}
