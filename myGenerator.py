def myGenerator():
    yield'first'
    yield'second'
    yield'third'

for word in myGenerator():
    print(word)
    
