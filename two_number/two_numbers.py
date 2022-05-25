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


def main():
    """
    runs leet code test and prints results
    """
    sl1 = Llist()
    sl2 = Llist()
    sl3 = Llist()
    sl4 = Llist()
    sl5 = Llist()
    sl6 = Llist()
    
    l1 = [2,4,3]
    l2 = [5,6,4]
    l3 = [0]
    l4 = [0]
    l5 = [9,9,9,9,9,9,9]
    l6 = [9,9,9,9]
    
    sl1.insert_list(l1)
    sl2.insert_list(l2)
    sl3.insert_list(l3)
    sl4.insert_list(l4)
    sl5.insert_list(l5)
    sl6.insert_list(l6)
    
    ans1 = addTwoNumbers(sl1, sl2)
    ans2 = addTwoNumbers(sl3, sl4)
    ans3 = addTwoNumbers(sl5, sl6)
    
    print(l_list_to_arr(ans1))
    print(l_list_to_arr(ans2))
    print(l_list_to_arr(ans3))
    

def l_list_to_arr(l_list):
    """
    Takes in a linked list and converts it to an array and return
    the array
    """
    arr = []
    active = l_list.head
    arr.append(active.value)
    while active.next_node:
        active = active.next_node
        arr.append(active.value)
    return arr



def addTwoNumbers(sl1, sl2):
    """
    Takes in two linked list containg ints reverses them and adds them as
    if they where ints and returns the awnser reversed as a linked list
    """
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
    """
    Takes in a linked list of ints reverses it converts it 
    and converts the reversed list to an int
    """
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