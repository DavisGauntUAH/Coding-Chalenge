
from pickle import FALSE


class Zig_Zag:
    """
    Implements the leet code
    Zig Zag problem
    """
    
    def __init__(self, in_str, zig_len):
        """
        Takes in a string and the lenght of the pattern
        and creates a zig zag patern out of the string then reforms the string
        bassed on the patern and prints both the patern and results
        """
        
        self.zig_zag_arr = [['']]
        self.zig_len = zig_len
        
        """
        0 = down
        1 = up and across
        """
        traverse_flag = False 
        idx = 0
        
        while idx < len(in_str):
            
            if traverse_flag == False:
                t_funct = self.t_down
            else:
                t_funct = self.diagonal
                
            for jdx in range(traverse_flag, self.zig_len - traverse_flag):
                
                if idx < len(in_str):
                    t_funct(jdx, in_str[idx])
                    idx += 1
                    
            traverse_flag = not traverse_flag
                
                
        new_str = ''
        for arr in self.zig_zag_arr:
            
            patern = ''
            for char in arr:
                
                patern = patern + char
                if char != ' ': new_str = new_str + char
            print (patern)
        
        print(f"Solution = {new_str}")
        
        
    def t_down(self,idx, in_char):
        """
        Takes in the position in the string and the original string and creates the down
        protion of the zig zag patern
        """
        
        if self.zig_zag_arr[0][0] == '':
            self.zig_zag_arr[0][0] = in_char
            
        elif(len(self.zig_zag_arr) >= self.zig_len):
            self.zig_zag_arr[idx%self.zig_len].append(in_char)
            
        else:
            self.zig_zag_arr.append([in_char])
        
    
    def diagonal(self, idx, in_char):
        """
        Takes in the position in the string and the original string and creates the
        diagonal portion of the zig zag patern
        """
        
        cnt = 0
        for l_idx in range(self.zig_len-1, -1, -1):
            
            if idx%self.zig_len == cnt:
                self.zig_zag_arr[l_idx].append(in_char)
                cnt+=1
            else:
                self.zig_zag_arr[l_idx].append(' ')
                cnt+=1


def main():
    """
    tests the zig zag class
    """
    Zig_Zag("PAYPALISHIRING", 3)
    Zig_Zag("PAYPALISHIRING", 4)
    Zig_Zag("A", 1)


if __name__ == '__main__':
    main()