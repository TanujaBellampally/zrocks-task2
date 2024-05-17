def err(n):
    try:
        return n/0
    except:
        return "n can not be divided by zero"
    
    
    
    
n=int(input())
print(err(n))