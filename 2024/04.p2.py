
import sys
lines = sys.stdin.read().splitlines()

g = [list(l) for l in lines]

ans=0

w=len(g[0])
h=len(g)

def check(x,y):
    return x >= 0 and x < w and y >= 0 and y < h

t=set()
for sx in range(w):
    for sy in range(h):
        for dx in [-1,0,1]:
            for dy in [-1,0,1]:
                c=g[sy][sx]
                cx=sx
                cy=sy
                i=1
                while check(cx,cy) and i < 3:
                    cx+=dx
                    cy+=dy
                    if not check(cx,cy) and i < 4:break
                    c+=g[cy][cx]
                    i+=1
                if c[:3] == 'MAS': t.add((sx,sy,cx,cy))

for sx,sy,cx,cy in list(t):
    if (sx,sy+2,cx,cy-2) in t: ans += 1
    if (sx+2,sy,cx-2,cy) in t: ans += 1

print(ans)