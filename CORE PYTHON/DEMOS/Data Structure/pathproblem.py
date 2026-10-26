# finding the shortest path .
# using the chapital letter only (EWNS).

def path():
    path = input("Enter the path in the from of EWNS = ")

    x = 0
    y = 0

    for pos in path:
        if pos == "N":
            y+=1

        elif pos == "S":
            y-=1

        elif pos == "E":
            x+=1

        elif pos == "W":
            x-=1
        
        else:
            ("Invalid path.")
            break
    else:    
        dist = ((x**2)+(y**2))**0.5
    return dist
res = path()

print(f"Shortest Distance of youer path = {res}")
    