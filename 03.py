# http://www.pythonchallenge.com/pc/def/equality.html
import re
inputText = open("03.txt", "r").read()
pattern = re.compile("[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]")
output = "".join(pattern.findall(inputText))
print(output)
# Answer http://www.pythonchallenge.com/pc/def/linkedlist.html
