
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    results = []
    # X + Y + Z != n
    #find all the possibility ways 

    for i in range(x+1) :
        for j in range(y+1) :
            for k in range(z+1) :
                if i + j + k != n :
                    #results.append(("[{}, {}, {}]".format(i,j,k)))
                    #not work cuz of ' that appear in the print when i try with Sting
                    results.append([i,j,k])

    print(results)