from lxml import etree
import lxml.html
import re
import datetime

#with open("DataUsage.txt", "r") as dfile:
#	content = dfile.read()

with open("DataUsage.txt", "r") as dfile:
	content = dfile.read()

content_table = re.findall(r'<table border=1.*?</table>', content)

root = lxml.html.fromstring(content)
usage_raw = root.xpath('//table//tr[2]//table//tr//td/text()')

usage_matrix = []
usage_matrix = [usage_raw[x:x+8] for x in range(0, len(usage_raw), 8)]
dates = []

for list in usage_matrix:
	print(list)
	dates.append(datetime.datetime.strptime(list[2], '%d/%m/20%y').date())

date1 = datetime.datetime.strptime('10/05/2016', '%d/%m/20%y').date()
date2 = datetime.datetime.strptime('12/05/2016', '%d/%m/20%y').date()

print(date1)
print(date2)

if(date2 > date1):
	print(date2 - date1)

i = 0
index = 0
upload = 0
download = 0
'''for row in usage_matrix:
	usage += float(row[6])
	day = row[2].split('/')
	if(day[0] == '07'):
		index = i
		break
	i += 1	
'''
days = 0
usage = 0
for row in usage_matrix:
	upload 		+= float(row[3])/1000000
	download 	+= float(row[4])/1000000
	usage += float(row[6])
	date = row[2].split('/')
	days += 1

	if(date[0] == '07'):
		break
print("total : {0}".format(usage))
print("Upload = {0} Download = {1} Total usage : {2} MB in {3} days.".format(upload, download, (upload+download), days))