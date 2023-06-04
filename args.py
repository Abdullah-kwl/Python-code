# in this file we will learn how to pass command line arguments

import sys

# we will just make a simple calculator which accept two arguments and perform different calculations

# print(sys.argv) #first defalt argument is file name sys.argv[0]

# In default argument accepted as string so we convert them into intigers
n1=int(sys.argv[1])
n2=int(sys.argv[2])


# in terminal we pass arguments by writing "python args.py 12 4"
print("Addition       :", n1+n2  )
print("Multiplication :", n1*n2  )
print("Division       :", n1/n2  )