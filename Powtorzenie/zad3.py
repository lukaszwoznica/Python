import re
import urllib.request as urllib

response = urllib.urlopen("https://www.google.com/")
text = response.read().decode('utf-8')
pattern = re.compile(r'gmail', re.IGNORECASE)
wordList = re.findall(pattern, text)
print(len(wordList))

