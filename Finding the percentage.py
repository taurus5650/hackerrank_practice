if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        #*line : single line ; split () : all value split  ; Malika (name) 52 56 60 (single line)
        scores = list(map(float, line))
        #line into float type
        student_marks[name] = scores
        #parsing name as key ; Malika : [52.0, 56.0, 60.0]
    query_name = input()
    marks = student_marks[query_name]
    #student_marks pass to query_name
    print (format(sum(marks)/3, '.2f'))
    #questions mention "legth of marks arrays 3"

        
        
        
        
"""
name, *line = input().split()
print (name)
print (line)
-------------
//input :
Shene 50 79.5 90
//print :
Shene
['50', '79.5', '90']
"""
