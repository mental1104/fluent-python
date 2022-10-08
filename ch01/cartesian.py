colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]

print(tshirts)

# equivalent:
for color in colors: 
    for size in sizes:
        print((color, size))

# size first: 
tshirts = [(color, size) for size in sizes 
                         for color in colors]

print(tshirts)



