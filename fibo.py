def fibo(n):
    c=2
    b=1
    a=c
    lst=[0,1,1,2]
    #it requires few thing to be fixed 
    
    while len(lst)<n:
        a=c
        c=c+b
        lst.append(c)
        b=a
        
    return lst
        
