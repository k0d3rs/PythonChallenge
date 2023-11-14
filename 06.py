# http://www.pythonchallenge.com/pc/def/channel.html

import re, zipfile

file = zipfile.ZipFile("06.zip")
num = '90052'
pattern = re.compile("Next nothing is (?P<next>.[0-9]+)")

while True:
    content = file.read(num + ".txt").decode("utf-8")
    print(content)
    match = pattern.search(content)
    if match:
        num = match.group('next')
    else:
        break

# At runtime we discover the last instruction is "Collect the comments."
# Zipfiles support comments, so we can extract them
# So, we need to iterate (again) through the files and collect the comments in order

num = '90052'
comments = ""
while True:
    content = file.read(num + ".txt").decode("utf-8")
    comments += file.getinfo(num + ".txt").comment.decode("utf-8")
    print(content)
    match = pattern.search(content)
    if match:
        num = match.group('next')
    else:
        break

print(comments)

# Answer http://www.pythonchallenge.com/pc/def/hockey.html



# import re, zipfile
# import os
# filename = "90052"
# filepath = "06/"
# pattern = re.compile("(?P<comment>.[A-z]+)?.*Next nothing is (?P<next>.[0-9]+)")
# numFiles = 0
# fileset = set()
# comments = ""
#
# while True:
#     file = open(filepath+filename+".txt",'rb')
#     text = file.read().decode()
#     print(text)
#     match = pattern.search(text)
#     fileset.add(filename)
#     numFiles += 1
#     if match:
#         filename = match.group('next')
#         # print("FileName: " + filename)
#         comment = match.group('comment')
#         if comment:
#             comments += comment
#             print("Comments: " + comments)
#     else:
#         break
#
# print("Finished searching. NumLinkFiles: " + str(numFiles))
# print("Comments:" + comments)
#
# answer =
# There are 909 files with references to other files (including the final one - 46145,txt), but 910 files in total.
# The missing one is readme.txt
# comments = ""
# numFiles = 0
# # Iterate directory
# pattern = re.compile("(?P<fileNumber>.[0-9]+).txt")
# for file in os.listdir(filepath):
#     # check if current file is a file
#     match = pattern.search(file)
#     if match:
#         fileNumber = match.group('fileNumber')
#         if os.path.isfile(os.path.join(filepath, file)) and fileset.isdisjoint({fileNumber}):
#             print(file)
#             currentFile = open(filepath+filename+".txt",'rb')
#             comments += currentFile.read().decode() + "\n"
#             numFiles += 1
#     else:
#         print("No match for file: " + file)
#
# print(comments)
# print("NumCommentFiles:" + str(numFiles))