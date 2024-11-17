import sys
i = int(sys.argv[1])
l = int(sys.argv[2])

v = 0
switchs = 0

while switchs < l:
        O = (10**(switchs+1))
        v *= 10
        o = v + i
        v += O - (o%O)
        switchs += 1

print(f'...{v} + {i} = 0')

