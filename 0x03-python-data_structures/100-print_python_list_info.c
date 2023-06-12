#include <Python.h>
#include <stdio.h>
void print_python_list_info(PyObject *p)
{
	Py_ssize_t ln = PyList_Size(p);
	Py_ssize_t alloced = PyList_GET_SIZE(p);
	Py_ssize_t i;
	PyObject *item;

	printf("[*] Size of the Python List = %zd\n", ln);
	printf("[*] Allocated = %zd\n", alloced);
	for (i = 0 ; i < ln ; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %zd: \n", i);
		PyObject_Print(item, stdout, Py_PRINT_RAW);
		printf("\n");
	}
}	
