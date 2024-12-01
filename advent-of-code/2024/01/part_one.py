with open('input.txt', 'r') as file:
    data = file.read()

left = []
right = []

for line in data.splitlines():
    l, r = map(int, line.split())
    left.append(l)
    right.append(r)

left.sort()
right.sort()

distance = sum(abs(l - r) for l, r in zip(left, right))

print(distance)
