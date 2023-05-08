if __name__ == '__main__':
    n = int(input())
    i=0
    while i < n :
        #get input of A
        index_of_a = int(input())
        a_nums_str = input()
        nums_a = [int(x) for x in a_nums_str.split()]

        #get input of B
        index_of_b = int(input())
        b_nums_str = input()
        nums_b = [int(y) for y in b_nums_str.split()]

        set_A = set(nums_a)
        set_B = set(nums_b)

        #intersection will make the new set that contain only the common number on the set 
        subset_count = len(set_A.intersection(set_B))
        
        if subset_count == len(set_A) :
            print("True")
        else :
            print("False")

        i+=1
