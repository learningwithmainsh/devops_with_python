import re

text = "The quick green fox"
pattern = r"green"

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")
