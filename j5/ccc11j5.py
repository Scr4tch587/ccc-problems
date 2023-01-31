#CCC '11 J5 - Unfriend
#AC
n = int(input())

friends = [int(input()) for i in range(n-1)]

def ways(friend):
    count = 1

    for i in range(0, n-1):
        if (friends[i] == friend):
            count *= 1 + ways(i + 1)

    
    return count

print(ways(n))
