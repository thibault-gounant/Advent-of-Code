with open('input.txt', 'r') as file:
    data = file.read()

left = []
right = {}

for line in data.splitlines():
    l, r = map(int, line.split())
    left.append(l)
    if r not in right:
        right[r] = 0
    right[r] += 1

score = sum(l * right[l] for l in left if l in right)

print(score)
