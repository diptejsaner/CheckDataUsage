import urllib.request
import sys
import lxml.html
import datetime

def getTotalUsage(usage_matrix):
	days = 0
	usage = 0
	for row in usage_matrix:
		usage += float(row[6])
		date = row[2].split('/')
		days += 1

		if(date[0] == '07'):
			return usage, days

#url1 = "http://mqr.hathway.com/mqsweb/reports/serviceusagereport_selfcare.asp"

url = "http://mqr.hathway.com/mqsweb/reports/UsageDetails.asp"

current_month = datetime.date.today().month
prev_month = current_month - 1

CSD = '01/{0}/2016'.format(current_month)
PSD = '01/{0}/2016'.format(prev_month)
PED = '30/{0}/2016'.format(prev_month)

values = {"AN":"1351265",		# account number
		  "FU":"0",				# fair usage
		  "RP":"3149",			# rate plan id
		  "PP":"Y",				# prepaid
		  "CSD":CSD,			# current start date
		  "PSD":PSD,			# prev start date
		  "PED":PED}			# prev end date

#values = {"username" : "diptej123"}

data = urllib.parse.urlencode(values)
data = data.encode("utf-8")

req = urllib.request.Request(url, data)

try:
	print("Requesting data from server...")
	resp = urllib.request.urlopen(req, timeout=10)

	respData = resp.read()

	print("Data recieved. Writing the data to file...")
	with open("DataUsage.txt", "w") as dfile:
		dfile.write(str(respData))

except Exception as e:
	print("Error : {0}\nScript will retry in the next interval.".format(str(e)))
	sys.exit(0)

print("Parsing the data...")
root = lxml.html.fromstring(str(respData))
usage_raw_table = root.xpath('//table//tr[2]//table//tr//td/text()')

usage_matrix = [usage_raw_table[x:x+8] for x in range(0, len(usage_raw_table), 8)]
print("Data parsing complete.")

for row in usage_matrix:
	print(row)

t = getTotalUsage(usage_matrix)
print("Total usage : {0} MB in {1} days.".format(t[0], t[1]))


