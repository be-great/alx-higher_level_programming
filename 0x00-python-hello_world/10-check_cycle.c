#include "lists.h"

/**
 * check_cycle - function that checks if a singly linked list has a cycle
 * @list: pointer to the head of the linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, /* Tortoise pointer */
	*fast = list; /* Hare pointer */

	/* Traverse the list */
	while (slow && fast && fast->next)
	{
		slow = slow->next;        /* Move one step at a time */
		fast = fast->next->next;  /* Move two steps at a time */

		/* If the pointers meet, a cycle is detected */
		if (slow == fast)
			return (1);  /* Cycle detected */
	}

	return (0);  /* No cycle detected */
}
