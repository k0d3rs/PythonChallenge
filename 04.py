# http://www.pythonchallenge.com/pc/def/linkedlist.html

import urllib.request
import re
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
urlParam = "12345"
pattern = re.compile("the next nothing is (?P<next>.[0-9]+)")
while True:
    response = urllib.request.urlopen(url+urlParam)
    html = response.read().decode()
    print(html)
    match = pattern.search(html)
    if match:
        urlParam = match.group('next')
    else:
        if html == "Yes. Divide by two and keep going.":
            urlParam = str(int(urlParam) / 2)
        else:
            break

# Answer http://www.pythonchallenge.com/pc/def/peak.html