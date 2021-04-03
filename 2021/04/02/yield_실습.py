def yield_silseup():
    for j in range(3):
        yield 'b'

    for k in range(3):
        yield 'c'

print(yield_silseup())
for l in yield_silseup():
    print(l)
