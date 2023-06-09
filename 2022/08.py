trees = []

while True:
    try:
        line = input()
    except EOFError:
        break
    trees.append(line)

w = len(trees[0])
h = len(trees)
print("Width: {}\nHeight: {}".format(w, h))

def is_tree_visible(x, y):
    scenic_score = 1
    visible_fr = False
    for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        local_scenic_score = 0
        visible = True # true until proven false
        tree_height = trees[y][x]
        cx, cy = x + dx, y + dy
        while cx >= 0 and cx < w and cy >= 0 and cy < h:
            local_scenic_score += 1
            if trees[cy][cx] >= tree_height:
                visible = False
                break
            cx += dx
            cy += dy
        if visible:
            visible_fr = True
        scenic_score *= local_scenic_score
        #if x == 0 and y == 2:
        #    print(local_scenic_score, scenic_score)
    #if visible_fr and x != 0 and x != w-1 and y != 0 and y != h-1:
        #print("Tree at ({}, {}) is visible with height {} and scenic score {}".format(x, y, tree_height, scenic_score))
    return visible_fr, scenic_score


visible_trees = 0
scenic_scores = []
for y in range(h):
    for x in range(w):
        # print(trees[y][x], end="")
        visible, scenic_score = is_tree_visible(x, y)
        visible_trees += visible
        scenic_scores.append((scenic_score, x, y, trees[y][x]))
    # print()
print("Visible trees: {}".format(visible_trees))
print("Max scenic score: {}".format(max(scenic_scores)[0]))
