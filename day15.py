class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

        def display(self,head):
        current = head
        while current:
            print current.data,
            current = current.next

class Solution:

    def display(self,head):
        current = head
        while current:
            print current.data,
            current = current.next	


    def insert(self,head,data): 
	    #Complete this method
	    current = head

	    if not current:
	    	return Node(data)

	    while current:
	    	if not current.next:
	    		current.next = Node(data)
	    		break

	    	else:
	        	current = current.next

	    return head






