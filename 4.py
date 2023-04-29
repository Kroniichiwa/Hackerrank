if __name__ == '__main__':
    super_set_str = input()
    super_set = [int(x) for x in super_set_str.split()]
    set_super = set(super_set)
    n = int(input())
    i=0
    while i < n :
        nums = []
        set_A = {}
        y = 0
        #get input of subset
        nums_str = input()
        nums = [int(y) for y in nums_str.split()]

        set_A = set(nums)

        set_count = len(set_A.intersection(set_super))
        
        if set_count != len(set_A) :
            print("False")
            break
        if i+1 == n :
            print("True")
        i+=1
