#include <Python.h>
#include <stdio.h>
void print_python_list_info(PyObject *p)
{
	Py_ssize_t ln = PyList_Size(p);
	Py_ssize_t alloced = ((PyObject *)p)->alloced;
	Py_ssize_t *tp;
	int i;

	printf("[*] Size of the Python List = %d\n", ln);
	print("[*] Allocated = %d\n");
	for (i = 0 ; i <= ln ; i++)
	{
		printf("Element %d: %d\n", i, PyList_GetItem(p, i));
	}
}	
