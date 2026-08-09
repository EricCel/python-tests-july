#Take two lists with duplicates, convert them to sets, and find the elements that are in both, as well as those exclusive to each list
list1 = ["Robert","Robert","Larefd","Arlc","Terep","Terep","Souil"]
list2 = ["Checima","Larefd","Larefd","Arlc","Kiooccn","Kiooccn","Souil",'y']
list3 = ["MrLinux","Robert","Larefd","Franklin","Terep","Terep","Kmi"]

def searchEXUN(*t):
    common, unique = [], []

    for i in t:
        i = list(set(i))

    for i in range(len(t)):
        for j in t[i]:
            if j in t[i - 1]:
                common.append(j) 
            else:
                unique.append(j)

    return list(set(common)), list(set(unique))

common, unique = searchEXUN(list1,list2, list3)
print(common, unique)
