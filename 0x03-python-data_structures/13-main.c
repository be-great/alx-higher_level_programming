#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * main - check the code for
 *
 * Return: Always 0.
 */
int main(void)
{
    listint_t *head, *head0,*head1,*head2,*head3,*head4;

    head = NULL;
    head0 = NULL; /*empty = NULL*/
    head1 = NULL; /* one element*/
    head2 = NULL; /* two element*/
    head3 = NULL; /* three element*/
    head4 = NULL; /* four element*/
    
    printf("##########empty############");
    print_listint(head0);
    printf("##########one element#############");
    add_nodeint_end(&head1, 1);
    print_listint(head1);
    printf("###########two element############");
    add_nodeint_end(&head2, 5);
    add_nodeint_end(&head2, 5);
    print_listint(head2);
    printf("#############three##########");
    add_nodeint_end(&head3, 17);
    add_nodeint_end(&head3, 2);
    add_nodeint_end(&head3, 16);
    print_listint(head3);
    printf("############four###########");
    add_nodeint_end(&head4, 17);
    add_nodeint_end(&head4, 1);
    add_nodeint_end(&head4, 1);
    add_nodeint_end(&head4, 17);
    print_listint(head4);    
    printf("###########long one############");
    /*long*/
    add_nodeint_end(&head, 1);
    add_nodeint_end(&head, 17);
    add_nodeint_end(&head, 972);
    add_nodeint_end(&head, 50);
    add_nodeint_end(&head, 98);
    add_nodeint_end(&head, 88);
    add_nodeint_end(&head, 50);
    add_nodeint_end(&head, 972);
    add_nodeint_end(&head, 17);
    add_nodeint_end(&head, 1);
    print_listint(head);
    is_palindrome(&head);

    if (is_palindrome(&head) == 1)
        printf("defult- Linked list is a palindrome\n");
    else
        printf("defult- Linked list is not a palindrome\n");

    if (is_palindrome(&head0) == 1)
        printf("0- Linked list is a palindrome\n");
    else
        printf("0- Linked list is not a palindrome\n");
    if (is_palindrome(&head1) == 1)
        printf("1- Linked list is a palindrome\n");
    else
        printf("1- Linked list is not a palindrome\n");
    if (is_palindrome(&head2) == 1)
        printf("2- Linked list is a palindrome\n");
    else
        printf("2- Linked list is not a palindrome\n");
    if (is_palindrome(&head3) == 1)
        printf("3- Linked list is a palindrome\n");
    else
        printf("3- Linked list is not a palindrome\n");
    if (is_palindrome(&head4) == 1)
        printf("4- Linked list is a palindrome\n");
    else
        printf("4- Linked list is not a palindrome\n");

    free_listint(head);
    free_listint(head0);
    free_listint(head1);
    free_listint(head2);
    free_listint(head3);
    free_listint(head4);
    
    return (0);
}