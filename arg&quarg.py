

def fun(*args,**kwargs):
    
    sum=0

    for item in args:
        sum = sum+item
        print(item)
        
    print(f"Your sum is : {sum}")

    print(kwargs)

li=[5,6,4]

fun(*li,l=5,w=8)
