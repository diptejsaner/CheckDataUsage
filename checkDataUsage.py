import urllib.request
import sys
from lxml import etree
# script might not work on Sundays

url1 = "http://mqr.hathway.com/mqsweb/reports/serviceusagereport_selfcare.asp"
url = "http://mqr.hathway.com/mqsweb/reports/UsageDetails.asp"

values = {"AN":"1351265",		# account number
		  "FU":"0",				# fair usage
		  "RP":"3149",			# rate plan id
		  "PP":"Y",				# prepaid
		  "CSD":"01/05/2016",	# current start date
		  "PSD":"01/04/2016",	# prev start date
		  "PED":"30/04/2016"}	# prev end date

#values = {"username" : "diptej123"}

data = urllib.parse.urlencode(values)
data = data.encode("utf-8")

req = urllib.request.Request(url, data)

try:
	print("Requesting data from server...")
	resp = urllib.request.urlopen(req, timeout=10)

	respData = resp.read()

	print("Data recieved. Writing the data to file...")
	with open("DataUsage.txt", "r") as dfile:
		dfile.write(str(respData))

except Exception as e:
	print("Error : {0}\nScript will retry in the next interval.".format(str(e)))
	sys.exit(0)


'''
table = etree.XML(respData)
rows = iter(table)
headers = [col.text for col in next(rows)]
for row in rows:
    values = [col.text for col in row]
    print(dict(zip(headers, values)))
'''

print("Parsing the data...")
root = lxml.html.fromstring(str(respData))
usage_raw_table = root.xpath('//table//tr[2]//table//tr//td/text()')

usage_matrix = [usage_raw_table[x:x+8] for x in range(0, len(usage_raw_table), 8)]
print("Data parsing complete.")

for list in usage_matrix:
	print(list)