for i in range(1, 11):
    if i % 2 == 1:
        print(i)
    else:
        continue

print("----------------------")


x = 1
while x < 11:
    if x % 2 == 1:
        print(x)
    x += 1


for letter in "john.smith@pythonistitute.org":
    if letter == "@":
        break
    print(letter, end="")


for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")