proverbs = '''All's well that ends well.
Bad news travels fast.
Well begun is half done.
Birds of a feather flock together.'''


table = dict()

for word in proverbs.split():
    if word not in table:
        table[word] = 1
    else:
        table[word] += 1

print(table)
