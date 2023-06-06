#include "lists.h"
/**
 * check_cycle -> check if a single linked list has a cycle
 * @list: single linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	size_t i = 0;
	listint_t *tmp, *prev;

	tmp = malloc(sizeof(listint_t));
	if(tmp == NULL)
		return (0);
	prev = malloc(sizeof(listint_t));
	if(prev == NULL)
		return (0);
	tmp = (list->next)->next;
	prev = list;
	while (tmp != NULL || tmp->next != prev)
	{
		if (tmp->next == NULL)
		{
			free(tmp);
			free(prev);
			return (0);
		}
		prev = tmp;
		tmp = tmp->next;
		i++;
	}
	free(tmp);
	free(prev);
	return (1);
}
