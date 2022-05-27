

class longest_substring:
    """
    object that will find the length of the longest
    substring in a given string
    """
    
    def __init__(self, in_str=None):
        """
        creates new instance of longest_substring
        and sets self.str = to in_str assuming it is a string type
        if not it throws an error
        """
        
        pass


    def length_of_longest_substring(self, in_str=None):
        """
        takes in a string and identifies the
        length of the longest string withough any repeats
        """
        
        
        if type(in_str) == str:
            self.str = in_str
        else: 
            raise TypeError(f"Invalid type: {type(in_str)} != String")
        
        last_seen = {}
        max_len = 0
        
        window_start = 0
        
        for s_idx in range(0, len(in_str)):
            
            if in_str[s_idx] in last_seen:
                window_start = max(window_start, last_seen[in_str[s_idx]] + 1)
            
            max_len = max(max_len, s_idx - window_start + 1)
            
            last_seen[in_str[s_idx]] = s_idx
        
        return max_len
    
def main():
    """
    prints test case
    """
    test = longest_substring()
    
    try:
        print(test.length_of_longest_substring("abcabcbb"*500000))
        print(test.length_of_longest_substring(""))
        print(test.length_of_longest_substring("pwwkew"))
    except TypeError as err:
        print(f"Error: {err}")

if __name__ == '__main__':
    main()