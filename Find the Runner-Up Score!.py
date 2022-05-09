if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    arr_list = list(arr)[:n] 
    #Convert the type from arr to list type ; [:n] : when "n = int(input())" input 5 then only got 5 numbers
    
    max_number = max(arr_list)
    #Findout the max_number = 6
    
    while (max_number in arr_list) :
        arr_list.remove (max_number)
    #While max_number = 6 then removed, remaining [2,3,5,2,3]
        
    runner_up = max(arr_list)
    #max_number again, then got number "5"
    print(runner_up)
    # print 5
