text_map = [
        'WWWWWWWWWW',
        'W........W',
        'W.W.....WW',
        'W.W.......W',
        'W....WW..W',
        'W........W',
        'WWWWWWWWWW'
        ]
TILE = 60
world_map = set()
print(world_map)
for j, row in enumerate(text_map):
    print(' for 1 : j = '+ str(j) + ' row = '+ str(row))
    for i, char in enumerate(row):
        print(' for 2 : i = '+ str(i) + ' char = '+ char)
        if char == 'W':
            print('yes')
            world_map.add((i * TILE, j * TILE))
print(world_map)

A = [1,2,3,4,5,6,7]
# for count,value in enumerate(A):
#   print(count,value)
