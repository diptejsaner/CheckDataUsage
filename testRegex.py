import re
import lxml

with open("DataUsage.txt", "r") as dfile:
	content = dfile.read()

#print(content)

fwords = re.findall(r'<table border=1.*?</table>', content)

print(fwords)