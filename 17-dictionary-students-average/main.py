#Given a dictionary of students with lists of grades, calculate each student's average and determine the highest one.
students = {'Pea Pearson':[13,17,11,12],'Appaul Appleston':[11,5,20,20],'Pin Appler':[20,20,20,19]}

def mostAVG(d):
    student = (sorted(d.items(),key=lambda x:sum(x[1]) / len(x[1]),reverse=True))
    return f'{student[0][0]} got an average of {sum(student[0][1]) / len(student[0][1])}'

print(mostAVG(students))