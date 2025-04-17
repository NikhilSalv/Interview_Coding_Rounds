"""
Given an array of integers, find the most occuring kth element

arr = [1,2,3,4,4,5,2,1,3,45,3,4,5,4,4,4,4]
k = 3 

output = 
"""
from collections import Counter

class Node:
    def __init__(self,root, left= None, right= None):
        self.root = root
        self.left = left
        self.right = right
    
def insert(arr, head):
    temp = head
    
    for i in range(1, len(arr)):
        print("root head is : ", temp.root)
        if arr[i] < temp.root:
            temp.left = Node(arr[i])
            temp = temp.left
        else:
            temp.right = Node(arr[i])
            temp = temp.right
    return head

def preorder(head,result):
    if head:
        result.append(head.root)
        print(result)
        preorder(head.left, result)
        preorder(head.right, result)
    return result

def kth_occuring(arr, k):
    pass


if __name__ == "__main__":
    arr = [1,2,3,4,5,4,4,4,4]
    print(Counter(arr))
    head = Node(arr[0])
    head = insert(arr, head)
    print(head.right.root)
    result = []
    result_list = preorder(head, result)
    print(result_list)
