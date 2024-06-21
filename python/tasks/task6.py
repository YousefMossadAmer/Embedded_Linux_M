#program to find largest item from a given list using loop

i=0
ls=[1,5,8,9,63,2,1,4,5]

def largest_item(ls):
    max=ls[1]
    for i in ls :
        if i>max:
            max=i
    return max

print('largest number=',largest_item(ls))
