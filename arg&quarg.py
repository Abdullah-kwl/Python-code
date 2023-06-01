

def adding(*args):
    
    sum=0

    for item in args:
        sum = sum+item
        print(item)
        
    print(f"Your sum is : {sum}")


li=[5,6,4]

adding(*li)
