
from pydoc import resolve


class Node:
    """
    contains the structure of the node of a linked list
    """
    def __init__(self, val = 0, next = None):
        self.value = val
        self.next_node = None
        
class Llist:
    """
    linked list data type made of a head containing a node
    """
    def __init__(self):
        """
        creates an empty head
        """
        self.head = None

    def insert(self, val):
        """
        takes in a value to append to the end of the linked list
        """
        temp_node = Node(val)
        
        if(self.head):
            active = self.head
            while(active.next_node):
                active = active.next_node
            active.next_node = temp_node
        else:
            self.head = temp_node
            
    def insert_list(self, val_list):
        """
        takes in a list and appends the whole list to the end of 
        the linked list
        """
        for val in val_list:
            self.insert(val)
            
            
    def in_swap(self,pre_node, pre_s_node, gap):
        """
        swaps interior nodes
        takes in the node befor the first node to be swap, the last node
        to be swaped, and the gap between the nodes and swaps the nodes
        """
        s_node = pre_s_node.next_node
        h_hold = pre_node.next_node
        
        pre_node.next_node = s_node
        pre_s_node.next_node = h_hold
        
        temp = h_hold.next_node
        h_hold.next_node = s_node.next_node
        s_node.next_node = temp
        
    
    def swap(self, s_node, gap):
        """
        swapes the first node and a later node
        takes in node to be swaped with and the gap between it and the first
        node and swaps the nodes
        """
        s_remain = s_node.next_node
        h_remain = self.head
        self.head = s_node
        self.head.next_node = h_remain.next_node
        h_remain.next_node = s_remain
        hold = self.head
        for idx in range(0, gap):
            hold = hold.next_node
        hold.next_node = h_remain
        
    def get(self, idx):
        """
        gets the node at the given index
        """
        
        active = self.head
        for l_idx in range(0,idx-1):
            if active.next_node:
                active = active.next_node
        
        return active


    

class reverse_nodes:
    """
    Object to reverse the nodes at a given increment of
    a linked list
    """
    
    def __init__ (self, lst):
        """
        creates a reverse node object
        """
        
        self.l_lst = Llist()
        self.l_lst.insert_list(lst)

    def swap(self, interval, list=None):
        """
        Takes in a linked list and an int containing the
        interval between in which to swap items in the linked list
        """
        if(interval <= 1): return
        
        if list == None: list = self.l_lst
        
        active = list.head
        for idx in range(0, interval-1):
            active = active.next_node
        list.swap(active, interval-2)
        
        active = list.get(interval)
        pre_swap = active
        idx = interval
        
        while active:
            
            idx+=1
            
            
            if idx%interval == 0:
                if(active.next_node): list.in_swap(pre_swap, active, interval-1)
                active = list.get(idx)
                pre_swap = active.next_node
                
            active = active.next_node

                
                
    def l_print(self, list=None):
        """
        takes in a linked list and prints out the contents
        """
        if list == None: list = self.l_lst
        resolved = []
        
        active = list.head
        while active:
            print(f'{active.value}')
            resolved.append(active.value)
            active = active.next_node

        return resolved
        
            
def main():
    """
    creates test case4s and test swap then prints results
    """
    
    
    l1 = [1,2,3,4,5]*50000
    l2 = [1,2,3,4,5,6]
    expectedl3 = [3,2,1,6,5,4]
    
    sl1 = reverse_nodes(l1)
    sl2 = reverse_nodes(l2)
    
    sl1.swap(2)
    sl2.swap(3)
   
    #sl1.l_print()
    print("\n")
    assert(expectedl3 == sl2.l_print())
    

if __name__ == '__main__':
    main()