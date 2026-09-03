#some operations

#finding the length 

def count_nodes(head):
    cont = 0 
    curr = head

    while curr is not None:
        count += 1 
        curr = count.next #move pointer to next node 

    return count 

#searching

def search_key(head, key):
    curr = head

    while curr is not None:
        if curr.data == key:
            return True 
        
        curr.next
    return False 



