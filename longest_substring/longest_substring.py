

class longest_substring:
    def __init__(self, in_str=None):
        
        if type(in_str) == str or in_str  == None:
            self.str = in_str
        else: 
            raise TypeError(f"Invalid type: {type(in_str)} != String")
    
    def setStr(self, in_str):
        
        if type(in_str) == str:
            self.str = in_str
        else: 
            raise TypeError(f"Invalid type: {type(in_str)} != String")
        


    def length_of_longest_substring(self, in_str):
        """
        takes in a string and identifies the
        length of the longest string withough any repeats
        """
        
        last_seen = {}
        max_len = 0
        
        window_start = 0
        
        for s_idx in range(0, len(in_str)):
            
            if in_str[s_idx] in last_seen:
                window_start = max(window_start, last_seen[in_str[s_idx]] + 1)
            
            max_len = max(max_len, s_idx - window_start + 1)
            
            last_seen[in_str[s_idx]] = s_idx
        
        return max_len
    
#def main():
#    """
#    prints test case
#    """
#    print(length_of_longest_substring("abcabcbb"))
#    print(length_of_longest_substring("bbbb"))
#    print(length_of_longest_substring("pwwkew"))

#if __name__ == '__main__':
#    main()