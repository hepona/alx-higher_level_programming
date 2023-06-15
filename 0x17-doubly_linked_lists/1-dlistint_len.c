#include "lists.h"

/**
 * dlistint_len -> return nm of elemnt in a list
 * @h: list
 * Return: num of element in a list
 */
size_t dlistint_len(const dlistint_t *h)
{
	int c;

	for (c = 0; h != NULL ; c++)
	{
		h = h->next;
	}
	return (c);
}
