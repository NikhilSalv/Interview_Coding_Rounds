"""
[1,2,3,5,6] > [6,1,2,3,5] end = 2 > [5,6,1,2,3] end = 1 > 

 5,6] 1,2,3,


[5,6,1,2,3]

arr[0] * n

counter = 0

in a while loop, when counter = n
start appending the arr, 

reset to head and run loop from (0,n) to append the array from 0 to n. 

head = node
node.next = node
node.next.next = node

Optimal approach :

Count the lenghth,
Make the linked list cirucular

end = lenght - k
while loop over end in reverse
end = 5 - 2 = 3

"""

class Node:
    def __init__(self,data, next_node=None):
        self.data = data
        self.next_node = next_node

def rotateRight(head, k):
    if head == None or head.next_node == None or k == 0:
        return head
    # calculating length
    temp = head
    length = 1
    while temp.next_node != None:
        length += 1
        temp = temp.next_node
    # link last node to first node
    print("lenght is : ", length)
    temp.next_node = head
    # print(temp.data)
    # print(temp.next_node.data)
    k = k % length  # when k is more than length of list
    end = length - k  # to get end of the list
    print("This is K  :", k)
    print("This is end :", end)

    while end:
        print("IN while loop before", temp.data)
        temp = temp.next_node
        print("IN while loop", temp.data)
        
        end -= 1
    # breaking last node link and pointing to NULL
    head = temp.next_node
    print("out while loop", temp.data)
    temp.next_node = None


    return head

def printList(head):
    while head.next_node != None:
        print(head.data, end='->')
        head = head.next_node
    print(head.data)
    return


if __name__ == "__main__":
    head = Node(1)
    head.next_node = Node(2)
    head.next_node.next_node = Node(3)
    head.next_node.next_node.next_node = Node(4)
    head.next_node.next_node.next_node.next_node = Node(5)
    head.next_node.next_node.next_node.next_node.next_node = Node(6)
    # print(head.next_node.next_node.next_node.data)

    print("Before")
    printList(head)
    new_head = rotateRight(head, 2)
    print("After")
    printList(new_head)




