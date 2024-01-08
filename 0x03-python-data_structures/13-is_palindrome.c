#include "lists.h"

/**
* get_nodeint_at_index - Function that returns
* the nth node of a listint_t linked list.
* @head: The header of the link list
* @index: The index to check
*
* Return: The node or NULL if not found
*/
listint_t *get_nodeint_at_index(listint_t *head, unsigned int index)
{
	listint_t *tempnode;
	size_t size = 0;

	tempnode = head;
	while (size != index && tempnode != NULL)
	{
		tempnode = tempnode->next;
		size++;
	}
	return (tempnode);
}



/**
* listint_len - Function that returns the number
* of elements in a linked listint_t list.
* @h: The header
*
* Return: Number of elements in the list
*/
int listint_len(const listint_t *h)
{
	int size = 0;

	while (h != NULL)
	{
		h = h->next;
		size++;
	}
	return (size);
}

/**
* is_palindrome - Function in C that checks if
* a singly linked list is a palindrome.
* @head: The head of the linked list
*
* Return: 1 if it's true, 0 if it's false
* Empty list is palindrome
*/
int is_palindrome(listint_t **head)
{
	int start_indx, end_indx, linkend_length;
	listint_t *current_s, *current_e;

	/* Case the node is empty */
	if (*head == NULL)
		return (1);

	linkend_length = listint_len(*head);
	start_indx = 0;
	end_indx = linkend_length - 1;

	/* 1 element case */
	if (linkend_length == 1)
	{
		return (1);
	}

	/* Other cases */

	current_s = *head;
	current_e = get_nodeint_at_index(*head, end_indx);

	while (start_indx < end_indx)
	{
		if (current_s->n != current_e->n)
		{
			return (0);
		}
		start_indx++, end_indx--;
		current_s = current_s->next;
		current_e = get_nodeint_at_index(*head, end_indx);
	}
	return (1);
}
