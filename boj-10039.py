average = 0

for i in range(5):
    a = int(input())
    if a < 40:
        a = 40
    average += a

average = int(average / 5)
print(average)