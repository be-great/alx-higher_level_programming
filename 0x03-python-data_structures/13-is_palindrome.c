#include "lists.h"

/**
* find_second_head - Finds the second half of the linked list.
* @head: Pointer to the head of the linked list.
* Return: Pointer to the second half of the list.
*/
listint_t *find_second_head(listint_t *head)
{
	listint_t *slow = head, *fast = head;

	while (1)
	{
		fast = fast->next->next;
		if (!fast)
			return (slow->next);
		if (!fast->next)
			return (slow->next->next);
		slow = slow->next;
	}
}

/**
* reverse_list - Reverses a linked list.
* @head: Double pointer to the head of the linked list.
* Description: This function reverses a linked list and updates the head.
*/
void reverse_list(listint_t **head)
{
	listint_t *prev = NULL, *current = *head, *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
* is_palindrome - Checks if a singly linked list is a palindrome.
* @head: Double pointer to the head of the linked list.
* Return: 1 if it's true, 0 if it's false.
* Description: This function checks if a linked list is a palindrome.
*/
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	listint_t *second_head = find_second_head(*head);

	reverse_list(&second_head);

	while (second_head && *head)
	{
		if ((*head)->n == second_head->n)
		{
			second_head = second_head->next;
			*head = (*head)->next;
		}
		else
			return (0);
	}

	if (!second_head)
		return (1);

	return (0);
}
