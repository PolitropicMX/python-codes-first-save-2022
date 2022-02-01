x = [5,1,7,0,3,4,5,3,2,6,7,3,6]
get_indexes = lambda x, xs: [i for (y, i) in zip(xs, range(len(xs))) if x == y]
print(get_indexes(7,x))
