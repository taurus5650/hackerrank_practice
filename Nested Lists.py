if __name__ == '__main__':
    
    record_list = []
    score_list = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        record_list.append ([name,score])
        # To record "name, score" two dimensional lists (array)
        score_list.append (score)
        # Only recoding "score" value, to sorting the value
    
    score_value = sorted(set(score_list)) [1]
    # Sorting the value ; Set : To remove the dupicated value ; [1] : Get the second lowest grade (index : 0,1,2, ...)
        
    for name, score in (sorted (record_list, key = lambda x:x[0])) :
    #name, score : As item (append [name, score]) ; record_list lambda : For sorting, sorting rule started from x[0]
        if score_value == score :
            print (name)
          
          
"""
Ref :
https://hackmd.io/@brad84622/mumi/%2F64JIEMPPRAyB9olR0eDp0Q
"""
