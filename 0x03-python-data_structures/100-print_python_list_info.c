#include <Python.h>
#include <listobject.h>
#include <object.h>

void print_python_list_info(PyObject *p)
{
    long int len;
    int i;
    PyObject *item;
    const char *str;

    len = PyList_Size(p);
    printf("[*] Size of the Python List = %li\n", len);
    printf("[*] Allocated = %li\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < len; i++)
    {
        item = PyList_GET_ITEM(p, i);
        str = Py_TYPE(item)->tp_name;
        printf("Element %i: %s\n", i, str);
    }
}

