# a = [1, 11, 21, 1211, 111221,
# len(a[30])?



sequence = "1"
for i in range(30):
    print(sequence)
    newStr = ""
    lastChar = sequence[0]
    count = 0
    for char in sequence:
        if char == lastChar:
            count += 1
        else:
            newStr += str(count) + lastChar
            lastChar = char
            count = 1
    newStr += str(count) + lastChar
    sequence = newStr

print(len(sequence))

# solution: 5808
# http://www.pythonchallenge.com/pc/return/5808.html