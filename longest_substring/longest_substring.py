

def main():
    print(length_of_longest_substring("abcabcbb"))

def length_of_longest_substring(in_str):
    
    last_seen = {}
    max_len = 0
    
    window_start = 0
    
    for s_idx in range(0, len(in_str)):
        
        if in_str[s_idx] in last_seen:
            window_start = max(window_start, last_seen[in_str[s_idx]] + 1)
        
        max_len = max(max_len, s_idx - window_start + 1)
        
        last_seen[in_str[s_idx]] = s_idx
    
    return max_len
    

if __name__ == '__main__':
    main()