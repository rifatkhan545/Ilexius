def index_middle(middle):
    for x in middle:
        if min(middle) < x < max(middle):
            return middle.index(x)


print(index_middle([1, 4, 3]))