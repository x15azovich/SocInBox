import vulners

def getCveDescription():
	f = open("CVEresults.txt", "w+")
	CVEs = []
	#Getting CVEs based on api key
	vulners_api = vulners.Vulners(api_key="LKTS0IPVW1HU9XA3EENOEDDJEKOS6VACTQ6YLSPR9L3L2TI065XWRUBP5DQLYJHO")

	with open('CVEnumbers.txt') as my_file:
		CVEs = my_file.readlines()
		CVEs = [x.strip() for x in CVEs] 

	CVE_DATA = vulners_api.documentList(CVEs)
	print (CVE_DATA)

	for x in CVEs:
		f.write("CVE Number: "+ x + "\n")
		f.write("CVE Description: " + CVE_DATA.get(x).get("description")+"\n")
		f.write("CVE Solutions: " + CVE_DATA.get(x).get("href")+"\n\r")

getCveDescription()