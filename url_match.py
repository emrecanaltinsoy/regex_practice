import re

pattern = re.compile("http(s)?://(www.)[a-z]+\.(com|net|org)")

url = """
https://www.google.com
https://www.google.net
https://www.google.org
https://www.gOOgle.org
https://www.google.io
"""

matches = re.finditer(pattern,url)

[print(m) for m in matches]
