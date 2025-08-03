#include <stdio.h>
#include <stdlib.h>

struct ListNode
{
    int val;
    struct ListNode *next;
};

void printLL(struct ListNode *head)
{
    struct ListNode *currNode = head;
    while (currNode != NULL)
    {
        printf("%d ", currNode->val);
        currNode = currNode->next;
    };
    printf("\n");
}

struct ListNode *reverseKGroup(struct ListNode *head, int k)
{
    struct ListNode *currNode = head;
    struct ListNode *prevNode = NULL;
    struct ListNode *newHead = NULL;
    struct ListNode *tailNode = head;
    struct ListNode *prevTailNode = NULL;
    int counter = 0;
    while (currNode != NULL)
    {
        if (counter == (k - 1))
        {
            newHead = currNode;
        }
        if (counter % k == 0)
        {
            prevNode = currNode;
            struct ListNode *tmp = tailNode;
            while (tailNode != currNode)
            {
                struct ListNode *placeholder = tailNode->next;
                tailNode->next = prevNode;
                prevNode = tailNode;
                prevTailNode->next = tailNode;
                tailNode = placeholder;
            }
            prevTailNode = tmp;
        }
        currNode = currNode->next;
        counter++;
    };
    return newHead;
}

struct ListNode *convert(int arr[], int size)
{
    struct ListNode *head = NULL;
    for (int i = 0; i < size; i++)
    {
        struct ListNode *node = (struct ListNode *)malloc(sizeof(struct ListNode));
        node->val = arr[i];
        node->next = head;
        head = node;
    };
    return head;
}

int main()
{
    int size = 15;
    int myNumbers[] = {14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0};
    struct ListNode *head = convert(myNumbers, size);
    printLL(head);
    struct ListNode *h = reverseKGroup(head, 4);
    printLL(h);

    return 0;
}
