#include "lists.h"

/**
 * reverse_listint - Reverses a linked list.
 * @head: Double pointer to the head of the linked list.
 * Description: This function reverses a linked list and updates the head.
 */
void reverse_listint(listint_t **head)
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
 * compare_lists - Compares two linked lists for equality.
 * @list1: Pointer to the first linked list.
 * @list2: Pointer to the second linked list.
 * Return: 1 if lists are equal, 0 otherwise.
 * Description: This function compares two linked lists node by node.
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
 * @head: Double pointer to the head of the linked list.
 * Return: 1 if it's true, 0 if it's false.
 * Description: This function checks if a linked list is a palindrome.
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

	second_head = slow->next;

	reverse_listint(&second_head);

	if (!compare_lists(*head, second_head))
	{
		reverse_listint(&second_head); /* Re-reverse the second half */
		return (0);
	}

	reverse_listint(&second_head); /* Re-reverse the second half */
	return (1);
}
