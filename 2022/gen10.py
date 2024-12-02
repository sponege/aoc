#!/bin/python3
sponege=0

#image_data = [(x**2)%100 < 50 for x in range(40*6)]
image_data = """## #  #  #  #  #  #  #  #  #  #  #  #  #
  #  #  #  #  #  #  #  #  #  #  #  #  # 
 #  #  #  #  #  #  #  #  #  #  #  #  #  
#  #  #  #  #  #  #  #  #  #  #  #  #  #
  #  #  #  #  #  #  #  #  #  #  #  #  # 
 #  #  #  #  #  #  #  #  #  #  #  #  #  """
image_data = """
####   ##  ##  #### ###   ##  #    #  # 
#       # #  # #    #  # #  # #    #  # 
###     # ###  ###  #  # #    #    #### 
#       # #    #    ###  # ## #    #  # 
#    #  # #  # #    #    #  # #    #  # 
####  ##   ##  #    #     ### #### #  # 
"""[1:-1]
image_data = """
   #             # #                    
   #                                    
 ###   ##  # ##  # #                    
#  #  #  #  #  # # #                    
#  #  #  #  #  # # #                    
 ## #  ## # #  # # #                    
"""[1:-1]
if sponege: image_data = """
                                        
 ##                  ##   ##   ##      
#     ##            #  # #  # #  #      
 ##  #  # ### # ##  ###   ##  ###      
   # ###  # #  #  # #       # #         
 ##  #    ###  #  #  ##   ##   ##      
"""[1:-1]
#image_data = image_data.strip().splitlines()
image_data = image_data.splitlines()
truthy = lambda c: c == '#' or c == '█'
#for row in image_data:
    #print(len(row))
#    print(row)
#image_data = [truthy(c) for line in image_data for c in line]
danii_data = [[truthy(c) for c in line] for line in image_data]
image_data = [(x/2)%3 == 0 for x in range(40*6)]
len_signature = 20
if sponege: len_signature = 34
for pos, row in enumerate(danii_data):
    image_data[pos*40+(40-len_signature)-2:pos*40+(40-len_signature)-1] = [0]
    image_data[pos*40+(40-len_signature-1):(pos+1)*40] = row[:len_signature+1]
X = 0
cycle = 0
output = ""

def addx(val):
    global X, output, cycle
    X += val
    output += f"addx {val}\n"
    cycle += 2
    cycle %= 40

def noop():
    global output, cycle
    output += "noop\n"
    cycle += 1
    cycle %= 40

for pos, bit in enumerate(image_data):
    sprite_on_scanline = cycle>=X and cycle<X+3
    #print(bit, pos)
    if pos % 40 != cycle:
        continue

    #if bit == 1 and not sprite_on_scanline:
        # we can't turn on the sprite here, it's too late!
        #continue
    if pos + 2 < len(image_data):
        ## its not too late for the third and fourth bit though!
        add = ((cycle+2)%40)-X - 3 + max(
                (1 * (image_data[pos + 2])),
                (2 * (pos + 3 < len(image_data) and image_data[pos + 3])),
                #(3 * (pos + 4 < len(image_data) and image_data[pos + 4]))
            )
        if not image_data[pos + 2] and (pos + 3 < len(image_data) and image_data[pos + 3]):
            add += 2
        addx(add)
        #if add == 0:
        #    noop()
        #else:
        #    addx(add)
    else:
        noop()
    
print(output[:-1])

exit()
for pos, bit in e(image_data):
    if bit == 1:
        print('#', end='')
    else:
        print(' ', end='')
    if pos % 40 == 39:
        print()
