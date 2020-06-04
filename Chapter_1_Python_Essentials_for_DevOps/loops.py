# Notes and little tests

print('"for" loops')
for i in range(10):
    x = i * 2
    print(x)

print("\ncontinue skips a step in a loop and jumps to the next item in the sequence")
for i in range(6):
    if i == 3:
        continue
    print(i)

print('\n"while" loops repeat a block as long as a condition evaluates to True')
count = 0
while count < 3:
    print(f"The count is {count}")
    count += 1

print(
    '\n"break" statements can also be used to break out of a while loop with a nested conditional'
)
count = 0
while True:
    print(f"The count is {count}")
    if count > 5:
        break
    count += 1
