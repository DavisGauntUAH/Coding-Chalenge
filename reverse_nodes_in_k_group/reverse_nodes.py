
from requests import head


class Node:
    def __init__(self, val = 0, next = None):
        self.value = val
        self.next_node = None
        
class Llist:
    def __init__(self):
        self.head = None

    def insert(self, val):
        temp_node = Node(val)
        
        if(self.head):
            active = self.head
            while(active.next_node):
                active = active.next_node
            active.next_node = temp_node
        else:
            self.head = temp_node
            
    def insert_list(self, val_list):
        for val in val_list:
            self.insert(val)
            
            
    def in_swap(self,pre_node, s_node, gap):
        h_hold = pre_node.next_node
        s_hold = s_node.next_node
        temp = s_node
        temp.next_node = h_hold.next_node
        pre_node.next_node = temp
        h_hold.next_node = s_hold
        hold = pre_node
        for idx in range(0, gap):
            hold = hold.next_node
        hold.next_node = h_hold
    
    def swap(self, s_node, gap):
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
        
        active = self.head
        for l_idx in range(0,idx-1):
            if active.next_node:
                active = active.next_node
        
        return active


def main():
    
    sl1 = Llist()
    l1 = [1,2,3,4,5]
    
    sl1.insert_list(l1)
    
    swap(sl1, 3)
    
    l_print(sl1)
    
    return

def swap(list, interval):
    active = list.head
    for idx in range(0, interval-1):
        active = active.next_node
    list.swap(active, interval-2)
    
    active = list.get(interval)
    pre_swap = active
    idx = interval
    
    while active.next_node:
        
        idx+=1
        active = active.next_node
        
        if idx%interval == 0:
            list.in_swap(pre_swap, active, interval-1)
            active = list.get(idx)
            pre_swap = active
            
def l_print(list):
    active = list.head
    while active.next_node:
        print(f'{active.value}')
        active = active.next_node
    print(f'{active.value}')
            

if __name__ == '__main__':
    main()