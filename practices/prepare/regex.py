import re


# s = 'GeeksforGeeks:portal A computer science portal for geeks'
# match = re.search(r'portal', s)
# print(type(match))

# print('Start Index:', match.start())
# print('End Index:', match.end())

# print(re.findall('portal',s))

# p = re.compile('[a-e]')
# print(p)


p = re.compile('[a-zA-Z*_. ]')
print(p.findall(r"He said * in some_lang."))

p = re.compile('\w+')
print(p.findall("I went to him at 11 A.M., he \
said *** in some_language."))

# p = re.compile('\W')
# print(p.findall("he said *** in some_language."))

text = "He said * in some_lang."
list_of_words = list(text)
print(list_of_words)

p = re.compile('\W')
print(p.findall("he said *** in some_language."))