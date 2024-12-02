import sys
instructions = [y.split() for y in sys.stdin.read().splitlines()]
tails = []
for i in range(10):
    tails.append((0, 0, i))
positions = set()
for instruction in instructions:
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    dx, dy = directions[["R", "L", "U", "D"].index(instruction[0])]
    times = int(instruction[1])
    for _ in range(times):
        tails[0] = (tails[0][0] + dx, tails[0][1] + dy, 0)
        #print("Head: ", tails[0])
        #print("Tail: ", tails[1])
        for i in range(1, len(tails)):
            #print("Tail: {}".format(tails[i]))
            ## move tail to head if tail is not adjacent to head
            if abs(tails[i-1][0] - tails[i][0]) > 1 or abs(tails[i-1][1] - tails[i][1]) > 1:
                #print(tails[i], tails[i-1])
                #print((1 if tails[i][1] - tails[i-1][1] < 0 else -1))
                tails[i] = (
                        tails[i][0] + 
                        (1 if tails[i][0] - tails[i-1][0] < 0 else (
                            -1 if tails[i][0] - tails[i-1][0] > 0 else 0)),
                        tails[i][1] + 
                        (1 if tails[i][1] - tails[i-1][1] < 0 else (
                            -1 if tails[i][1] - tails[i-1][1] > 0 else 0)), tails[i][2])
            if tails[i][2] == 9:
                positions.add(tails[i])
#print(positions)
print(len(positions))
