
class next_perm:
    
    def __init__(self):
        """
        Creates a next_perm object
        """
        pass

    def next_perm(self, pre_perm):
        """
        takes in a list and outputs a list containing the
        next permutation of the given input list
        """
        
        for idx in range(len(pre_perm)-1, 0, -1):
            
            if pre_perm[idx] > pre_perm[idx-1]:
                
                for jdx in range (len(pre_perm)-1, idx-1, -1):
                    
                    if jdx > idx-1:
                        pre_perm[idx-1], pre_perm[jdx] = pre_perm[jdx], pre_perm[idx-1]
                        return self.reverse(pre_perm, idx)
                    
                return self.reverse(pre_perm, idx)
            
        return pre_perm[::-1]
                
    def reverse(self, r_list, fdx):
        """
        Takes in a list and an index position to reverse the list after inclusive
        returns the list contianing the reversed section
        """
            
        r_list = r_list[:fdx] + r_list[:fdx-1:-1]
        return(r_list)

def main():
    """
    contains test cases from leet code
    """
    test = next_perm()
    
    print (test.next_perm([1,2,3]))
    print (test.next_perm([3,2,1]))
    print (test.next_perm([1,1,5]))


if __name__ == '__main__':
    main()