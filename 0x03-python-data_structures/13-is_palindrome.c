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

    return prev;
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to the head of the linked list.
 * Return: 1 if it's true, 0 if it's false.
 */
int is_palindrome(listint_t **head)
{
    if (*head == NULL || (*head)->next == NULL)
        return 1;

    listint_t *slow = *head, *fast = *head, *second_head = NULL, *temp;

    while (fast != NULL && fast->next != NULL)
    {
        slow = slow->next;
        fast = fast->next->next;
    }

    temp = slow;
    while (temp != NULL)
    {
        listint_t *new_node = malloc(sizeof(listint_t));
        if (new_node == NULL)
            exit(-1);

        new_node->n = temp->n;
        new_node->next = second_head;
        second_head = new_node;

        temp = temp->next;
    }

    temp = *head;
    while (second_head != NULL)
    {
        if (temp->n != second_head->n)
            return 0;

        temp = temp->next;
        second_head = second_head->next;
    }

    return 1;
}
