#Write a program that receives a list of numbers and removes duplicate elements while maintaining the original order.
list1 = [6,9,1,1,6,6,2,2,4,3,4,5,6]

def orderNotRep(l):
    for item in reversed(range(len(l))):
        for i in reversed(range(item + 1,len(l))):
            if l[item] == l[i]:
                l.pop(i)
    return l

print(orderNotRep(list1))