#CCC '00 S2 - Babbling Brooks
#AC
streams = []
num = int(input())
for i in range(num):
    stream = int(input())
    streams.append(stream)
while True:
    reading = int(input())
    if reading == 99:
        index = int(input())
        index -= 1
        percent =  int(input())
        current = streams[index]
        streams[index] = current * (100-percent)/100
        streams.insert(index, current * percent/100)
    elif reading == 88:
        index = int(input())
        index -= 1
        streams[index] = streams[index] + streams[index+1]
        streams.pop(index+1)
    elif reading == 77:
        break

output = ""
for stream in streams:
    rounded = round(stream)
    output += str(rounded)
    output += " "
print(output)
