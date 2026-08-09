#Implement the rotation of a list to the left or right by N positions.
myList1 = [0,1,2,3,4,5,6,7,8,9]
def rotate(l,Orindex,Npos,Direction = "Right"):
    match Direction:
        case "right":
            valuer = l[(Orindex + Npos)%len(l)]
            l[(Orindex + Npos)%len(l)] = l[Orindex]
            l[Orindex] = valuer
        case "left":
            for i in range(1, Npos%len(l) + 1):
                ogVal = l[Orindex - i + 1]
                postVal = l[Orindex - i]
                l[Orindex - i] =  ogVal
                l[Orindex - i + 1] =  postVal
    return l

print(rotate(myList1,2,6, "left"))