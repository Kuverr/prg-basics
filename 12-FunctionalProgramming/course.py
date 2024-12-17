scores = [37,51,44,23,78,92,39,84,83,51]

def min_pts(minimum):
    return list(filter(lambda x : x > minimum, scores))

print (min_pts(70))
print (min_pts(40))
print (min_pts(30))