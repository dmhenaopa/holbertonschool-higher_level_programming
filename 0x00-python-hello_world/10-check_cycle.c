#include "lists.h"

/**
* check_cycle - Linked list cycle
* @list: Linked list
*
* Description: A function that checks
* if a singly linked list has a cycle in it.
* Return: 0 if there is no cycle. 1 otherwise.
*/
int check_cycle(listint_t *list)
{
	struct listint_s *pointer;

	/* Obtain the first node memory address*/
	pointer = list->next;
	/* Move to the next node*/
	list = list->next;
	while (list != NULL)
	{
		/* Compare the address of first node and others nodes */
		if (pointer == list->next)
		{
			return (1);
		}
		list = list->next;
	}
	return (0);
}
