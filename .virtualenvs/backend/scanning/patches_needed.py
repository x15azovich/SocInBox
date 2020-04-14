#!/usr/bin/python

import vulners

#scandatafile = open("../CVEdetails.txt","r+")

#for x in scandatafile:
#cve=scandatafile.readline()
vulners_api = vulners.Vulners(api_key="LKTS0IPVW1HU9XA3EENOEDDJEKOS6VACTQ6YLSPR9L3L2TI065XWRUBP5DQLYJHO")
CVE_DATA = vulners_api.documentList(["CVE-2017-14174"])

print(CVE_DATA.get("CVE-2017-14174").get("description"))

    

