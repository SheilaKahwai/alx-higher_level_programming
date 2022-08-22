#include "lists.h"

/**
 * check_cycle - checks if a linked lists contains a cycle
 * @list: pointer to head of list
 * Return: 0 if there is no cycle, 1 if there is
 */

int check_cycle(listint_t *list)
{
  int *slow = list;
  int *fast = list;

  if (!head)
    return (0);  ;
  while (slow && fast && fast->next)
    {
      slow = slow->next;
      fast = fast->next->next;
      if (slow == fast)
	return (1);
    }
  return (0);
}
