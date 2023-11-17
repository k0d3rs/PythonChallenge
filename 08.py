
import bz2
import re

un = b"BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084"
pw = b"BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08"


decodedUn = bz2.decompress(un)
print("Decoded Username ", decodedUn)
decodedPwd = bz2.decompress(pw)
print("Decoded Username ", decodedPwd)

# Next level: http://www.pythonchallenge.com/pc/return/good.html
# Username: huge
# Password: file



# pattern2 = re.compile("(?P<comment>.[A-z]+)?.*Next nothing is (?P<next>.[0-9]+)")
# pattern = re.compile("(?P<hexChar>.?"-\x".[0-f]{2}?)")


# pattern = re.compile(r'\\x[0-9a-f]{2}?')
# matches = pattern.findall(un)
#
# decodedUn = un
# print("Match:")
# for x in matches:
#     print(x)
#     hexChar = x.replace(r"\x", "")
#     print(hexChar)
#     decodedUn = decodedUn.replace(x, chr(int(hexChar, 16)))
# print("Decoded Username ", decodedUn)
# print("Decoded Password ", pw)