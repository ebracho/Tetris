def get_tetromino(shape, orientation): # :: int shape, int orientaiton

    if orientation not in range(4): 
        raise ValueError("%d is not a valid orientation" % orientation)

    # points: (y,x)
    if shape == 'i': # color: cyan
        if orientation in [0,2]: return [(0,0), (1,0), (2,0), (3,0)] 
        if orientation in [1,3]: return [(0,0), (0,1), (0,2), (0,3)]

    if shape == 'o': return [(0,0), (0,1), (1,0), (1,1)] # color: yellow

    if shape == 't': # color: purple
        if orientation == 0: return [(0,1), (1,0), (1,1), (1,2)]
        if orientation == 1: return [(0,0), (1,0), (1,1), (2,0)]
        if orientation == 2: return [(0,0), (0,1), (0,2), (1,1)]
        if orientation == 3: return [(0,1), (1,0), (1,1), (2,1)]

    if shape == 'j': # color: blue
        if orientation == 0: return [(0,1), (1,1), (2,0), (2,1)]
        if orientation == 1: return [(0,0), (1,0), (1,1), (1,2)]
        if orientation == 2: return [(0,0), (0,1), (1,0), (2,0)]
        if orientation == 3: return [(0,0), (0,1), (0,2), (1,2)]

    if shape == 'l': # color: orange
        if orientation == 0: return [(0,0), (1,0), (2,0), (2,1)]
        if orientation == 1: return [(0,0), (0,1), (0,2), (1,0)]
        if orientation == 2: return [(0,0), (0,1), (1,1), (2,1)]
        if orientation == 3: return [(0,2), (1,0), (1,1), (1,2)]

    if shape == 's': # color: green
        if orientation in [0,2]: return [(0,1), (0,2), (1,0), (1,1)]
        if orientation in [1,3]: return [(0,0), (1,0), (1,1), (2,1)]

    if shape == 'z': # color: red
        if orientation in [0,2]: return [(0,0), (0,1), (1,1), (1,2)]
        if orientation in [1,3]: return [(0,1), (1,0), (1,1), (2,0)]
