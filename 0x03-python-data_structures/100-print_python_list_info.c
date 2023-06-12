#include <Python.h>
#include <stdio.h>
void print_python_list_info(PyObject *p)
{
	Py_ssize_t ln = PyList_Size(p);
	Py_ssize_t alloced = PyList_GET_SIZE(p);
	Py_ssize_t i;
	PyTypeObject *itemType;

	printf("[*] Size of the Python List = %zd\n", ln);
	printf("[*] Allocated = %zd\n", alloced);
	for (i = 0 ; i < ln ; i++)
	{
		itemType = Py_TYPE(PyList_GetItem(p, i));
		printf("Element %zd: %s", i, itemType->tp_name);
		printf("\n");
	}
}	
