#include "list.h"

/**
 * insert_node -> insert a nood 
 * @head: list
 * @number: num to insert
 * Return: adress of new node, NULL otherwise
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nv;
	int i;

	nv->n = number;
	if (*head == NULL)
	{
		*head = nv;
		return (nv);
	}
	else if (*head->next == NULL)
	{
	       	if (number < *head->n)
		{
			nv->next = *head;
			*head = nv;
			return (nv);
		}
		else
		{
			*head->next = nv;
			*head = nv;
			return (nv);
		}
	}
	else
	{
		for (i = 0 ; *head != NULL ; i++)
		{

}	
