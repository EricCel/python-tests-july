#Given a long text, create a word frequency counter using a dictionary.
text = 'Given a long text text text, create a word frequency counter using a dictionary.'
def WordFreq(s): return dict({(i,s.count(i)) for i in s.replace(","," ").replace("."," ").split()})
print(WordFreq(text))