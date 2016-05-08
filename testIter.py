from lxml import etree
import lxml.html
import re

#with open("DataUsage.txt", "r") as dfile:
#	content = dfile.read()

content1 = """<table>
			 	<tr>
			 		<td class="labeltext" align='center' nowrap>1351265</td>								
					<td class="labeltext" align='center' nowrap>HD 2 STREAM 50MB Qtrly U</td>
					<td class="labeltext" align='center'>08/05/2016</td>			
					<td class="labeltext" align='right'>1279116</td>			
					<td class="labeltext" align='right'>5585572</td>	
					<td class="labeltext" align='right'>6864688</td>			
					<td class="labeltext" align='right'>6.547</td>					
					<td class="labeltext" align='right'>0</td>
			 	</tr>
			 </table>"""

content2 = """sfasfasdfasf
			<table>
  			 <tr>	<th>Event</th>	<th>Start Date</th>	<th>End Date</th>	</tr>
  			 <tr>	<td>a</td>	<td>b</td>	<td>c</td>	</tr>
  			 <tr>	<td>d</td>	<td>e</td>	<td>f</td>	</tr>
  			 <tr>	<td>g</td>	<td>h</td>	<td>i</td>	</tr>
			</table>
		"""
with open("DataUsage.txt", "r") as dfile:
	content = dfile.read()

content_table = re.findall(r'<table border=1.*?</table>', content)

root = lxml.html.fromstring(content)
usage_raw = root.xpath('//table//tr[2]//table//tr//td/text()')
print(root.xpath('//table//tr[2]//table//tr//td/text()'))

'''
parser = etree.HTMLParser()
tree = etree.parse(content_table[0], parser)

result = etree.tostring(tree.getroot(), pretty_print=True, method="html")

print(result)

'''

'''
table = etree.XML(content_table[0])
#print(table)
rows = iter(table)

headers = [col.text for col in next(rows)]
print(headers)
for row in rows:
    values = [col.text for col in row]
    print(dict(zip(headers, values)))
'''

usage_matrix = []
usage_matrix = [usage_raw[x:x+8] for x in range(0, len(usage_raw), 8)]

for list in usage_matrix:
	print(list)