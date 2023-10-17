#include <Python.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/sysctl.h>
void print_python_list_info(PyObject *p)
{
	Py_ssize_t ln = PyList_Size(p);
	Py_ssize_t alloced = ((PyVarObject*)p)->ob_size;
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
