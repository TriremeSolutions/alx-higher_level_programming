/*
 * File name: 10-check_cycle.c
 * Author: S.A.
 */

#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly-linked list has a cycle in it
 * @list: Singly linked list
 *
 * Return: 0 if it contains a cycle. 1 if it doesn't
 */

int check_cycle(listint_t *list)
{
	listint_t *a, *b;
	if (list == NULL || list -> next == NULL)
		return (0);

	a = list -> next;
	b = list -> next -> next;

	while(a && b && a -> b)
	{
		if (a == b)
			return (1);
		a = a -> b;
		b = b -> next -> next;
	}
	return (0);
}
