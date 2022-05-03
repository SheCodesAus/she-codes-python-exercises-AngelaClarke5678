# chilli_wishlist = ['igloo', 'chicken','donut toy', 'cardboard box' ]
# # print(chilli_wishlist)


# # print(chilli_wishlist[-1])
# # print(chilli_wishlist[3])
# # print(chilli_wishlist[1:3])
# # chilli_wishlist[1] = 'carrot'
# # print(chilli_wishlist)

# # #print the subjlist of items 2 to 3
# # print(chilli_wishlist[2:4])
# # #print the items in the -3 position
# # print(chilli_wishlist[-3])

# #chilli_wishlist.append('dig mat')
# # print(chilli_wishlist.extend(['kong', 'tennis ball', 'crocodile toy']))
# chilli_wishlist.append(['kong', 'tennis ball', 'crocodile toy'])
# print(chilli_wishlist)

# chilli_wishlist[2]

characters = ['a', 'b', 'c']
print(characters)
if 'd' in characters:
    print('good')
else:
    characters.append('d')
print(characters)

chilli_wishlist = ['igloo', 'chicken','donut toy', 'cardboard box' ]
if 'tennsi balls' in chilli_wishlist:
    print("play fetch")
else:
    print('no ball')

print(len(chilli_wishlist))

if len(chilli_wishlist) > 8:
    print("Chilli wants a lot of stuff")
else:
    print("chilli needs more stuff")

if 'blueberries' in chilli_wishlist:
    print('blue')
else: chilli_wishlist.append('blueberries')
print(chilli_wishlist)

#multiple lists
asli = [[3,5], ['blue','pink']]
print(asli[0])
print(asli[1])
print(asli[1][1])