
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
            
                jdx = self.get_next_biggest(pre_perm, idx-1)
                    
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
    
    def get_next_biggest(self, list, target_idx):
        
        low = target_idx+1
        high = len(list)-1
        mid = 0
        
        while low < high:
            
            mid = (high +low) // 2
            
            if ord(list[target_idx])+1 == ord(list[mid]):
                for idx in range(mid, len(list)):
                    if list[idx] <= list[target_idx]: return idx -1
                    
            elif list[target_idx] == list[mid]:
                for idx in range(mid-1, target_idx, -1):
                    if list[idx] > list[target_idx]: return idx
            
            elif list[mid] > list[target_idx] and low+1 != high:
                low = mid
            
            elif list[mid] < list[target_idx]: high = mid-1
            
            else:
                if(list[high] > list[target_idx]): return high
                return low
        
        return high
        
        
    

def main():
    """
    contains test cases from leet code
    """
    test = next_perm()
    
    print (test.next_perm(['h','e','f','g']*500000))
    print (test.next_perm(['d','h','c','k']))
    print (test.next_perm(['d','k','h','c']))
    #print (test.next_perm([1,5,8,4,7,6,5,3,1]))


if __name__ == '__main__':
    main()