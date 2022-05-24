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
        
            
        



def main():
    sl1 = Llist()
    sl2 = Llist()
    l1 = [9,9,9,9,9,9,9]
    l2 = [0]
    sl1.insert_list(l1)
    sl2.insert_list(l2)
    
    slretun = addTwoNumbers(sl1, sl2)
            
    return
    


def addTwoNumbers(sl1, sl2):
    num1 = 0
    num2 = 0
    ret_list = Llist()
    
    num1 = lList_to_int(sl1)
    num2 = lList_to_int(sl2)
    if(num1 == -1 or num2 == -1):
        print("invalid input!")
        return -1
    ans = num1+num2
    
    if (ans != 0):
        while (ans != 0):
            ret_list.insert(ans%10)
            ans = int(ans/10)
        return ret_list
    else:
        ret_list.insert(0)
        return ret_list
    
    
    
def lList_to_int(l_list):
    num = 0
    count = 0
    if(l_list.head):
        active = l_list.head
        while(active.next_node):
            num = num + (active.value * 10 ** count)
            count += 1
            active = active.next_node
        num = num + (active.value * 10 ** count)
        return num
    else:
        return -1
        

if __name__ == '__main__':
    
    main()

