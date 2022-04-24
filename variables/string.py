singleQuote = '"python" with single quotes written with single quotes'
doubleQuote = "python's with single quotes written with double quotes"
tripleQuote = '''
[multiline string]
well you can use this triple quotes
to write like letter or email or for like this
    "python" & python's
'''

print(doubleQuote[0]) #python strore to array with indexing
print(doubleQuote[-1]) #from the last one
print(doubleQuote[-2]) #from the last two one
print(doubleQuote[0:3]) #I think you should understand this is not to difficult to understand
# and its same with [:3] and what happen with [:] it's mean return all character you can clone array with this
# the rules [exclude:include] when you do like this [0:] then python will show all but when you give out [1:] then python will exclude the first one
# then what happen when you do like this [1:-1] the it will have the opposite rules it's become [include:exclude]
# e.g 'Jennifer' t
# hen it will return 'ennife' if u do  [0:-1] then python will read like this include [from 0 to end: but exclude the last one(-1)]
# default rules is [exclude(-numeric):include (+numeric)]

## formatted string
first = 'Jhon'
last = 'Smith'
# user f mean formatted
msg = f'{first} [{last}] is a coder'
print(msg)

## string methods
