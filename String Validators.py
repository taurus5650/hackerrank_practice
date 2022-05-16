def func1 (s) :
    for i in range (len(s)) :
        if (s[i].isalnum ()) :
            return True;
            break;
    return False;
        
def func2 (s) :
    for i in range (len(s)) :
        if (s[i].isalpha ()) :
            return True;
            break;
    return False;
        
def func3 (s) :
    for i in range (len(s)) :
        if (s[i].isdigit ()) :
            return True;
            break;
    return False;
        
def func4 (s) :
    for i in range (len(s)) :
        if (s[i].islower ()) :
            return True;
            break;
    return False;
        
def func5 (s) :
    for i in range (len(s)) :
        if (s[i].isupper ()) :
            return True;
            break;
    return False;
                    
        


if __name__ == '__main__':
    s = input()
    result_isalnum = func1(s)
    print (result_isalnum)
    result_isalpha = func2 (s)
    print (result_isalpha)
    result_isdigit = func3 (s)
    print (result_isdigit)
    result_islower = func4 (s)
    print (result_islower)
    result_isupper = func5 (s)
    print (result_isupper)
