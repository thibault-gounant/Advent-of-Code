with open('input.txt', 'r') as file:
    data = file.read()


def is_safe(report):
    differences = [report[i] - report[i - 1] for i in range(1, len(report))]
    increasing = all(d > 0 for d in differences)
    decreasing = all(d < 0 for d in differences)
    valid = all(1 <= abs(d) <= 3 for d in differences)
    return (increasing or decreasing) and valid


safe = sum(is_safe(list(map(int, line.split(' ')))) for line in data.splitlines())

print(safe)
