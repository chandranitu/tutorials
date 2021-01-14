import re


pattern = r"Cookie"
sequence = "Cookie"
if re.match(pattern, sequence):
  print("Match!")
else: print("Not a match!")


---------------

x = 'blue,red,green'
x.split(",")

a,b,c = x.split(",")

#result = re.sub(pattern, repl, string, count=0, flags=0)

input=('abcdefpqr') 
result = re.sub('abc',  '',input)           # Delete pattern abc
result = re.sub('abc',  'def', input)           # Replace pattern abc -> def
result = re.sub(r'\s+', ' ',   input)           # Eliminate duplicate whitespaces
result = re.sub('abc(def)ghi', r'\1', input)    # Replace a string with a part of itself



#result = re.subn(pattern, replacement, input)
print ('Result: ', result[0])
print ('Replacements: ', result[1])

----------------

re.split('\W+', 'Words, words, words.')

re.split('(\W+)', 'Words, words, words.')

re.split('\W+', 'Words, words, words.', 1)

>>> re.split('[a-f]+', '0a3B9', flags=re.IGNORECASE)


------

m = re.search('(?<=abc)def', 'abcdef')
m.group(0)


-------
print all([not re.match("a", "cat"),re.search("a", "cat"),not re.search("c", "dog"),3 == len(re.split("[ab]", "carbs")),"R-D-" == re.sub("[0-9]", "-", "R2D2")])
