#!/usr/bin/python

import vulners

scandatafile = open("CVEnumbers.txt","r+")
f = open("CVEdescriptions.txt", "w+")

vulners_api = vulners.Vulners(api_key="LKTS0IPVW1HU9XA3EENOEDDJEKOS6VACTQ6YLSPR9L3L2TI065XWRUBP5DQLYJHO")

for x in scandatafile:
	cve=scandatafile.readline().strip('\n\r')
	CVE_DATA = vulners_api.documentList([cve])
	f.write("CVE Number: "+ cve + "\n")
	f.write("CVE Description: " + CVE_DATA.get(cve).get("description")+"\n")
	f.write("CVE Solutions: " + CVE_DATA.get(cve).get("href")+"\n\r")
 
f.close()

    

