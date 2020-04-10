#!/usr/bin/python

import vulners

scandatafile = open("../CVEdetails.txt","r+")

for x in scandatafile:
	cve=scandatafile.readline()
	vulners_api = vulners.Vulners(api_key="YOUR_API_KEY_HERE")
	CVE_DATA = vulners_api.documentList(["CVE-2017-14174", "CVE-2016-1175"])
	references = vulners_api.references("CVE-2014-0160")
