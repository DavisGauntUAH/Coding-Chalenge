

def next_perm(pre_perm):
    for idx in range(len(pre_perm)-1, 0, -1):
        
        if pre_perm[idx] > pre_perm[idx-1]:
            
            for jdx in range (len(pre_perm)-1, idx-1, -1):
                if jdx > idx-1:
                    pre_perm[idx-1], pre_perm[jdx] = pre_perm[jdx], pre_perm[idx-1]
                    return reverse(pre_perm, idx)
            return reverse(pre_perm, idx)
    return pre_perm[::-1]
            
def reverse(r_list, fdx):
    r_list = r_list[:fdx] + r_list[:fdx-1:-1]
    return(r_list)

def main():
    print (f"{next_perm([1,2,3])}")
    print (next_perm([3,2,1]))
    print (next_perm([1,1,5]))


if __name__ == '__main__':
    main()