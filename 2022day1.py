
with open("2022day1.txt", "r") as input:
    data = input.read()

list = data.split("\n")


sums = []
sum = 0
for num in list:
    if num == "":
        sums.append(sum)
        sum = 0
    else:
        sum += int(num)


largest = sums[0]
for sum in sums:
    if sum > largest:
        largest = sum

print(f"First Part Answer: {largest}")


sums.remove(largest)
second = sums[0]
for sum in sums:
    if sum > second:
        second = sum

sums.remove(second)
third = sums[0]
for sum in sums:
    if sum > third:
        third = sum

print(f"Second Part Answer: {largest + second + third}")
