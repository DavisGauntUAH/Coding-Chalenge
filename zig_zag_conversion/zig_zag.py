
class Zig_Zag:
    def __init__(self, in_str, zig_len):
        self.zig_zag_arr = [['']]
        self.zig_len = zig_len
        
        """
        0 = down
        1 = up and across
        """
        traverse_flag = 0 
        idx = 0
        
        while idx < len(in_str):
            
            if traverse_flag == 0:
                for jdx in range(0, self.zig_len):
                    if idx < len(in_str):
                        self.t_down(jdx, in_str[idx])
                        idx += 1
                traverse_flag = 1
                
            elif traverse_flag == 1:
                for jdx in range(1, self.zig_len-1):
                    if idx < len(in_str):
                        self.diagonal(jdx, in_str[idx])
                        idx += 1
                traverse_flag = 0
                
        for arr in self.zig_zag_arr:
            temp = ''
            for char in arr:
                temp = temp + char
            print (temp)
        
    def t_down(self,idx, in_char):
        if self.zig_zag_arr[0][0] == '':
            self.zig_zag_arr[0][0] = in_char
            
        elif(len(self.zig_zag_arr) >= self.zig_len):
            self.zig_zag_arr[idx%self.zig_len].append(in_char)
            
        else:
            self.zig_zag_arr.append([in_char])
        
    
    def diagonal(self, idx, in_char):
        cnt = 0
        for l_idx in range(self.zig_len-1, -1, -1):
            if idx%self.zig_len == cnt:
                self.zig_zag_arr[l_idx].append(in_char)
                cnt+=1
            else:
                self.zig_zag_arr[l_idx].append(' ')
                cnt+=1


def main():
    Zig_Zag("PAYPALISHIRING", 3)



if __name__ == '__main__':
    main()