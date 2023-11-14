# http://www.pythonchallenge.com/pc/def/peak.html

# Deserialize data
import pickle as pkl
file = open("05.txt",'rb')
object_file = pkl.load(file)
file.close()

# Prepare formatting
output = ""
for line in object_file:
    for char, count in line:
        output += char * count
    output += "\n"

print(output)

# Answer http://www.pythonchallenge.com/pc/def/channel.html
