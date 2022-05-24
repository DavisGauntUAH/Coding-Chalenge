

def next_perm(pre_perm):
    for idx in range(len(pre_perm)-1, 0, -1):
        if pre_perm[idx] < pre_perm[idx-1]:
            for ldx in range (idx+1, len(pre_perm)):
                if pre_perm[idx] >= pre_perm[ldx]:
                    pass  # TODO make swap function
                elif ldx == len(pre_perm):
                    pass # reverse everything abovce idx TODO implement reverse
                    #return
                pass
            
            
                

def main():
    pass


if __name__ == '__main__':
    main()