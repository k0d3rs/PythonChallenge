# http://www.pythonchallenge.com/pc/def/ocr.html

inputText = open("02.txt", "r").read()
outputText = "".join(filter(lambda x: x.isalpha(), inputText))
print(outputText)

# Answer http://www.pythonchallenge.com/pc/def/equality.html
