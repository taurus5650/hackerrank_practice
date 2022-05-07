if __name__ == '__main__':
    n = int(input())
    
    for i in range (1, n+1) :
        # 1 : initial value as 1
        # n+1 : if only n, just print out 1,2 but expected result should be 1,2,3, so n+1
        print (i, end = "")
        # end : removed new line default
