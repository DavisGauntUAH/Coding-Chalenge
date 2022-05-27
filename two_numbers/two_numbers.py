from functools import cache


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
    
    l1 = []
    l2 = [5,6,4]
    l3 = [0]
    l4 = [0]
    l5 = [9,9,9,9,9,9,9]
    l6 = [9,9,9,9]
    
    test1 = two_numbers(l1, l2)
    test2 = two_numbers(l3, l4)
    test3 = two_numbers(l5, l6)
   
    ans1 = test1.addTwoNumbers()
    ans2 = test2.addTwoNumbers()
    ans3 = test3.addTwoNumbers()
    
    print(test1.l_list_to_arr(ans1))
    print(test2.l_list_to_arr(ans2))
    print(test3.l_list_to_arr(ans3))



def lList_to_int(l_list):
    """
    Takes in a linked list of ints reverses it converts it 
    and converts the reversed list to an int
    """
    num = 0
    count = 0
    if(l_list.head):
        active = l_list.head
        while(active):
            if(not type(active.value) is int or active.value < 0 or active.value > 9):
                raise Exception(f"{active.value} is not an int between 0 and 9")
            
            num = num + (active.value * 10 ** count)
            count += 1
            active = active.next_node
        return num
    else:
        raise TypeError(f"{type(l_list)} is not a valid type: Llist expected")
        

class two_numbers:
    def __init__(self, num1=[2,4,3], num2=[5,6,4]):
        """
        creates a two numbers argument and sets num1&2 to default
        values if none are given
        """
        
        self.sl1 = Llist()
        self.sl2 = Llist()
        
        self.sl1.insert_list(num1)
        self.sl2.insert_list(num2)
        
    
    def set_num1(self, num):
        """
        sets num1 to the given new value
        """
        
        self.sl1.head = None
        self.sl1.insert_list(num)
    
    
    def set_num2(self, num):
        """
        sets num2 to the given new value
        """
        self.sl2.head = None
        self.sl2.insert_list(num)
    

    def addTwoNumbers(self):
        """
        Takes in two linked list containg ints reverses them and adds them as
        if they where ints and returns the awnser reversed as a linked list
        """
       
        
        num1 = 0
        num2 = 0
        ret_list = Llist()
        
        try:
            num1 = lList_to_int(self.sl1)
            num2 = lList_to_int(self.sl2)
        except Exception as err:
            print(f"Error: {err}")
            exit()
            
            
            
        if(num1 <= -1 or num2 <= -1):
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
        

    def l_list_to_arr(self, l_list):
        """
        Takes in a linked list and converts it to an array and return
        the array
        """
        arr = []
        active = l_list.head
        while active:
            arr.append(active.value)
            active = active.next_node
            
        return arr

    

if __name__ == '__main__':
    
    main()