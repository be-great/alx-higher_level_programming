#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - Inserts a number into a sorted singly linked list
 * @head: Pointer to the head of the list
 * @number: Integer to insert
 *
 * Return: The address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *new_node;

	/* Allocate memory for the new node */
	new_node = malloc(sizeof(listint_t));
	if (!new_node)
	{
		free(new_node);
		return (NULL);
	}

	/* Initialize the new node */
	new_node->n = number;
	new_node->next = NULL;

	/* Check if the list is empty or insertion at the beginning */
	if (*head == NULL || number < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		/* Locate the correct position in the sorted list */
		current = *head;

		while (current->next != NULL && current->next->n < number)
		{
			current = current->next;
		}

		/* Insert the new node at the correct position */
		new_node->next = current->next;
		current->next = new_node;
	}

	return (*head); /* Return the address of the new node */
}
