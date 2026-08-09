#Ask the user for a phrase and generate its initials in uppercase, separated by periods.
initials = lambda s:".".join(i[0] for i in [i.capitalize() for i in s.split()])

demoSTR1 = 'Ask the user for a phrase and generate its initials in uppercase, separated by periods.'
print(initials(demoSTR1))

phrase = input()
print(initials(phrase))