#include "list.h"

/**
 * is_palindrome -> check if a list is palindrome
 * @head: list
 * Return: 0 if it's not palindrome, 1 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *s, *f;
	int i;
	s = *head;
	f = *head;
	for (i = 0; f != NULL && f->next != NULL; i++)
	{
		f = f->next->next;
		s = s->next;
	}

