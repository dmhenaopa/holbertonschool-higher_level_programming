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
	int i;
	struct listint_s *pointer[1024];

	pointer[0] = list->next;
	list = list->next;

	while (list != NULL)
	{
		i = 0;
		for (; pointer[i] != NULL; i++)
		{
			if (pointer[i] == list->next)
			{
				return (1);
			}
		}
		pointer[i] = list->next;
		list = list->next;
	}
	return (0);
}
