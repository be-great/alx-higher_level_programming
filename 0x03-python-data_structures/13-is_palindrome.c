#include "lists.h"

/**
* reverse_listint - Reverses a linked list.
* @head: Pointer to the head of the linked list.
* Return: Pointer to the new head of the reversed list.
*/
listint_t *reverse_listint(listint_t *head)
{
	listint_t *prev = NULL, *current = head, *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}

/**
* compare_lists - Compares two linked lists for equality.
* @list1: Pointer to the first linked list.
* @list2: Pointer to the second linked list.
* Return: 1 if lists are equal, 0 otherwise.
*/
int compare_lists(listint_t *list1, listint_t *list2)
{
	while (list1 != NULL && list2 != NULL)
	{
		if (list1->n != list2->n)
			return (0);

		list1 = list1->next;
		list2 = list2->next;
	}

	return (1);
}

/**
* is_palindrome - Checks if a singly linked list is a palindrome.
* @head: Pointer to the head of the linked list.
* Return: 1 if it's true, 0 if it's false.
*/
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	listint_t *slow = *head, *fast = *head, *second_head;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	second_head = reverse_listint(slow);

	if (!compare_lists(*head, second_head))
		return (0);

	return (1);
}
