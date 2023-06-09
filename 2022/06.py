packet = input()
markerPos = 0

for i in range(4, len(packet)-4+1):
    marker = packet[i:i+4]
    # check if all characters in marker are all different
    if len(set(marker)) == 4:
        print(marker)
        markerPos = i + 4
        break
print("Start of packet marker:", markerPos)

for i in range(markerPos, len(packet)-14+1):
    marker = packet[i:i+14]
    # check if all characters in marker are all different
    if len(set(marker)) == 14:
        print(marker)
        markerPos = i + 14
        break
print("Start of message marker:", markerPos)
