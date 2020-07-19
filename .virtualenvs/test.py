#import CVEdescriptionAndSolutionsGetter

results = {u'CVE-2006-4925': {u'bulletinFamily': u'NVD', u'description': u'packet.c in ssh in OpenSSH allows remote attackers to cause a denial of service (crash) by sending an invalid protocol sequence with USERAUTH_SUCCESS before NEWKEYS, which causes newkeys[mode] to be NULL.', u'title': u'CVE-2006-4925', u'modified': u'2018-10-17T21:40:00', u'cvss': {u'vector': u'AV:N/AC:L/Au:N/C:N/I:N/A:P', u'score': 5.0}, u'href': u'https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2006-4925', u'lastseen': u'2019-05-29T18:08:34', u'enchantments': {u'vulnersScore': u'PENDING'}, u'published': u'2006-09-29T00:07:00', u'type': u'cve', u'id': u'CVE-2006-4925'}, u'CVE-2000-0999': {u'bulletinFamily': u'NVD', u'description': u'Format string vulnerabilities in OpenBSD ssh program (and possibly other BSD-based operating systems) allow attackers to gain root privileges.', u'title': u'CVE-2000-0999', u'modified': u'2008-09-05T20:22:00', u'cvss': {u'vector': u'AV:N/AC:L/Au:N/C:C/I:C/A:C', u'score': 10.0}, u'href': u'https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2000-0999', u'lastseen': u'2019-05-29T18:07:37', u'enchantments': {u'vulnersScore': u'PENDING'}, u'published': u'2000-12-11T05:00:00', u'type': u'cve', u'id': u'CVE-2000-0999'}, u'CVE-1999-1010': {u'bulletinFamily': u'NVD', u'description': u'An SSH 1.2.27 server allows a client to use the "none" cipher, even if it is not allowed by the server policy.', u'title': u'CVE-1999-1010', u'modified': u'2016-10-18T02:00:00', u'cvss': {u'vector': u'AV:L/AC:L/Au:N/C:P/I:N/A:N', u'score': 2.1}, u'href': u'https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-1999-1010', u'lastseen': u'2019-05-29T18:07:36', u'enchantments': {u'vulnersScore': u'PENDING'}, u'published': u'1999-12-14T05:00:00', u'type': u'cve', u'id': u'CVE-1999-1010'}}
data = {}


CVEs = []
CVE_Number = {}
CVE_Description = {}
CVE_Solution = {}


with open('testCVEnums.txt') as my_file:
    CVEs = my_file.readlines()
    CVEs = [x.strip() for x in CVEs] 
    


for index, x in enumerate(CVEs):
    CVE_Number[index] = x
    CVE_Description[index] = results.get(x).get("description")
    CVE_Solution[index] = results.get(x).get("href")

data["CVE Number"] = CVE_Number
data["Description"] = CVE_Description
data["Solution"] = CVE_Solution

print(data)

