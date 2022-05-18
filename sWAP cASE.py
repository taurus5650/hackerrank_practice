def swap_case(s):
    change_words =[]
    
    for i in range (len(s)) :
        if (s[i].isupper()) == True :
            change_words.append (s[i].lower())
            #upper to lower
        elif (s[i].islower()) == True :
            change_words.append (s[i].upper())
            #lower to upper
        else :
            change_words.append (s[i])
            #others words, like symbols
    
        strings = ''
    
    return strings.join (change_words)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
