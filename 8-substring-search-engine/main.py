#Implement a substring search engine that indicates the first and last position where a given word appears.
word = 'Implement a substring search substring that indicates the substring and substring substring where a given substring appears'

def searchFOR(s,w): return f'"{w}" in "{s.find(w)}" and "{s.rfind(w)}"', s.find(w), s.rfind(w)

result, first, last = searchFOR(word,"substring")
print(result)
print(first)
print(last)
print(word[0:first], word[0:last])