import tkinter as tk
from tkinter import *

from tkinter import ttk
from tkinter import font as tkFont

import os, re
import sys
#sys.path.insert(1, '.virtualenvs/backend/scanning/nampVulScanner.py')
import Vulscan
import CVEnumbersExtractor
import CVEdescriptionAndSolutionsGetter
import windows_7
import textwrap

from tkinter import filedialog
import csv 
import operator
root = tk.Tk() #creates the actual window


frame = Frame(root, background ="#03021a") #creates frame and makes it dark blue 
frame.pack(fill='both', expand=True)
frame.pack()

root.title("TKINTER > KIVY")

root.geometry("1920x1080") #sets the size of the GUI box 
#root.state("zoomed") #makes window full 


csvfile = r'C:\Users\Jeff\Desktop\SocInBox\.virtualenvs\database.csv'


def switch_tab(tab_name):

    def sort_csv(csv_input_file):
        reader = csv.reader(open(csv_input_file), delimiter=",")
        sortedlist = sorted(reader, key=operator.itemgetter(1), reverse=True)

        with open(csv_input_file, "w", newline='') as f:
            fileWriter = csv.writer(f)
            for row in sortedlist:
                print(row)
                fileWriter.writerow(row)


        print("CSV sorted!")

    def create_table():
        #creates frame 
        table_frame = Frame(frame)
        table_frame.place(relx =0.50, rely=0.20, relwidth= 0.85, relheight=0.75, anchor='n')
        #creates treeview table within the "table_frame"
        tree = ttk.Treeview(table_frame, selectmode="extended", columns=("IP Address", "Vulnerability" ,"Description")) 
        #treeview config
        style = ttk.Style(root)
        style.configure("Treeview", rowheight=90)
        tree.configure(style="Treeview")
        #Anchors the text to be aligned in the center 
        tree.column("IP Address",  anchor ='c')
        tree.column("Vulnerability",  anchor ='c') 
        #tree.column("Description",  anchor ='c') 
        # Defining header column
        tree['show'] = 'headings'
        tree.pack(expand=YES, fill=BOTH)
        tree.heading("IP Address", text="IP Address")
        tree.column("IP Address", minwidth=0, width=200,stretch=NO)
        tree.heading("Vulnerability", text="Vulnerability")
        tree.column("Vulnerability", minwidth=0, width=200,stretch=NO) 
        tree.heading("Description", text="Description")
        tree.column("Description", minwidth=0, width=1250,stretch=NO)

        return tree

    for widget in frame.winfo_children(): #deletes any objects in the frame. if you were in "scanning" tab, this function will delete any objects from previous tabs
        widget.destroy()
     

    if tab_name =="home":
        # show home button_tab
        home_button_tab = tk.Button(root, text="Home", bg="#03021a", fg='white', command= lambda:switch_tab("home")) #when pressed (lambda), executes command. without "lambda" the command will run on launch of code regardless if it was pressed or not  
        home_button_tab.place(relx =0.10, rely=0.00, relwidth=0.20, relheight=0.07, anchor='n') #relx = x position, rely = y position, relwidth = width of entity, relheight = height of entity

        # show scanning button
        scanning_button_tab = tk.Button(root, text="Scanning", bg="#1e92eb", fg='white', command= lambda:switch_tab("scanning"))
        scanning_button_tab.place(relx =0.30, rely=0.00, relwidth=0.20, relheight=0.07, anchor='n')

        # show patching button
        patching_button_tab = tk.Button(text="Patching", bg="#0b6eba", fg='white', command= lambda:switch_tab("patching"))
        patching_button_tab.place(relx=0.50, rely=0.00, relwidth=0.20, relheight=0.07, anchor='n')

        # show network button_tab
        network_button_tab = tk.Button(root, text="Network", bg="#085b9c", fg='white', command= lambda:switch_tab("network"))
        network_button_tab.place(relx =0.70, rely=0.00, relwidth=0.20, relheight=0.07, anchor='n')

        # show hostbase button_tab
        hostbase_button_tab = tk.Button(text="Hostbase", bg="#054a80", fg='white', command= lambda:switch_tab("hostbase"))
        hostbase_button_tab.place(relx=0.90, rely=0.00, relwidth=0.20, relheight=0.07, anchor='n')

    if tab_name =="scanning":

        # need to create and sort database of all scans to pass into patching using either CSV.
        # sort data by newest csv

        ip_content = tk.StringVar()
        entry_ip = tk.Entry(frame, font = "Calibri 15", textvariable=ip_content)
        entry_ip.place(relx=0.50, rely=0.10, relwidth=0.40, relheight=0.065, anchor='n')
        
        scan_button = tk.Button(frame, text="Scan", bg="#1e92eb", fg='white', command= lambda:press_scan())
        scan_button.place(relx =0.85, rely=0.10, relwidth=0.10, relheight=0.065, anchor='n')

        def press_scan():
            '''
            This function is executed when user pressed "scan", then takes in the ip address from user input and is scanned upon for vulnerabilities. 
            If there are vulnerabilities, then said vulnerabilities will be displayed on a table in tkinter 
            and appended to a CSV database as long as the data isn't already within the CSV file. 
            '''
            ip_address = ip_content.get()
            ip_address = "hackthissite.org"
            
            # print(ip_address)
            # try:
            #     print("running scan")
            #     # https://github.com/scipag/vulscan
            #     Vulscan.scan(ip_address) # dumps results into 'portscandata.txt'
            #     print("work")

            # except:
            #     print("error")

            # try: 
            #     CVEnumbersExtractor.vulnScanExtract() #opens portscandata.txt and writes into cvenumbers.txt
            #     print ("VulnScanner running")
            # except:
            #     print("Anthony Can't Code")

            # try: 
            #     CVEdescriptionAndSolutionsGetter.getCveDescription()
            #     print ("CVE Descirption Works")
            # except:
            #     print("Anthony Can't Code2")

            #results = CVEdescriptionAndSolutionsGetter.getCveDescription() #calls API and gets CVE Description  
            results = {'CVE-2011-4451': {'lastseen': '2019-05-29T18:11:25', 'bulletinFamily': 'NVD', 'description': '** DISPUTED ** libs/Wakka.class.php in WikkaWiki 1.3.1 and 1.3.2, when the spam_logging option is enabled, allows remote attackers to write arbitrary PHP code to the spamlog_path file via the User-Agent HTTP header in an addcomment request.  NOTE: the vendor disputes this issue because the rendering of the spamlog_path file never uses the PHP interpreter.', 'modified': '2012-09-06T13:05:00', 'id': 'CVE-2011-4451', 'published': '2012-09-05T20:55:00', 'href': 'https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2011-4451', 'title': 'CVE-2011-4451', 'type': 'cve', 'cvss': {'score': 4.3, 'vector': 'AV:N/AC:M/Au:N/C:N/I:P/A:N'}, 'enchantments': {'vulnersScore': 'PENDING'}}, 'CVE-2011-4449': {'lastseen': '2019-05-29T18:11:25', 'bulletinFamily': 'NVD', 'description': 'actions/files/files.php in WikkaWiki 1.3.1 and 1.3.2, when INTRANET_MODE is enabled, supports file uploads for file extensions that are typically absent from an Apache HTTP Server TypesConfig file, which makes it easier for remote attackers to execute arbitrary PHP code by placing this code in a file whose name has multiple extensions, as demonstrated by a (1) .mm or (2) .vpp file.', 'modified': '2012-09-07T04:24:00', 'id': 'CVE-2011-4449', 'published': '2012-09-05T20:55:00', 'href': 'https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2011-4449', 'title': 'CVE-2011-4449', 'type': 'cve', 'cvss': {'score': 6.8, 'vector': 'AV:N/AC:M/Au:N/C:P/I:P/A:P'}, 'enchantments': {'vulnersScore': 'PENDING'}}, 'CVE-2011-4140': {'lastseen': '2019-05-29T18:11:24', 'bulletinFamily': 'NVD', 'description': 'The CSRF protection mechanism in Django through 1.2.7 and 1.3.x through 1.3.1 does not properly handle web-server configurations supporting arbitrary HTTP Host headers, which allows remote attackers to trigger unauthenticated forged requests via vectors involving a DNS CNAME record and a web page containing JavaScript code.', 'modified': '2018-01-18T02:29:00', 'id': 'CVE-2011-4140', 'published': '2011-10-19T10:55:00', 'href': 'https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2011-4140', 'title': 'CVE-2011-4140', 'type': 'cve', 'cvss': {'score': 6.8, 'vector': 'AV:N/AC:M/Au:N/C:P/I:P/A:P'}, 'enchantments': {'vulnersScore': 'PENDING'}}, 'CVE-2011-4139': {'lastseen': '2019-05-29T18:11:24', 'bulletinFamily': 'NVD', 'description': "Django before 1.2.7 and 1.3.x before 1.3.1 uses a request's HTTP Host header to construct a full URL in certain circumstances, which allows remote attackers to conduct cache poisoning attacks via a crafted request.", 'modified': '2018-01-18T02:29:00', 'id': 'CVE-2011-4139', 'published': '2011-10-19T10:55:00', 'href': 'https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2011-4139', 'title': 'CVE-2011-4139', 'type': 'cve', 'cvss': {'score': 5.0, 'vector': 'AV:N/AC:L/Au:N/C:N/I:P/A:N'}, 'enchantments': {'vulnersScore': 'PENDING'}}, 'CVE-2009-4492': {'lastseen': '2019-05-29T18:10:01', 'bulletinFamily': 'NVD', 'description': 'WEBrick 1.3.1 in Ruby 1.8.6 through patchlevel 383, 1.8.7 through patchlevel 248, 1.8.8dev, 1.9.1 through patchlevel 376, and 1.9.2dev writes data to a log file without sanitizing non-printable characters, which might allow remote attackers to modify a window\'s title, or possibly execute arbitrary commands or overwrite files, via an HTTP request containing an escape sequence for a terminal emulator.\nPer:  http://www.ruby-lang.org/en/news/2010/01/10/webrick-escape-sequence-injection\r\n\r\n\r\n"Affected versions\r\n\r\n    * Ruby 1.8.6 patchlevel 383 and all prior versions\r\n    * Ruby 1.8.7 patchlevel 248 and all prior versions\r\n    * Development versions of Ruby 1.8 (1.8.8dev)\r\n    * Ruby 1.9.1 patchlevel 376 and all prior versions\r\n    * Development versions of Ruby 1.9 (1.9.2dev)"', 'modified': '2018-10-10T19:49:00', 'id': 'CVE-2009-4492', 'published': '2010-01-13T20:30:00', 'href': 'https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2009-4492', 'title': 'CVE-2009-4492', 'type': 'cve', 'cvss': {'score': 5.0, 'vector': 'AV:N/AC:L/Au:N/C:P/I:N/A:N'}, 'enchantments': {'vulnersScore': 'PENDING'}}, 'CVE-2008-1385': {'lastseen': '2019-05-29T18:09:25', 'bulletinFamily': 'NVD', 'description': 'Cross-site scripting (XSS) vulnerability in the Top Referrers (aka referrer) plugin in Serendipity (S9Y) before 1.3.1 allows remote attackers to inject arbitrary web script or HTML via the Referer HTTP header.', 'modified': '2018-10-11T20:33:00', 'id': 'CVE-2008-1385', 'published': '2008-04-23T13:05:00', 'href': 'https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2008-1385', 'title': 'CVE-2008-1385', 'type': 'cve', 'cvss': {'score': 4.3, 'vector': 'AV:N/AC:M/Au:N/C:N/I:P/A:N'}, 'enchantments': {'vulnersScore': 'PENDING'}}, 'CVE-2007-5273': {'lastseen': '2019-05-29T18:09:01', 'bulletinFamily': 'NVD', 'description': "Sun Java Runtime Environment (JRE) in JDK and JRE 6 Update 2 and earlier, JDK and JRE 5.0 Update 12 and earlier, SDK and JRE 1.4.2_15 and earlier, and SDK and JRE 1.3.1_20 and earlier, when an HTTP proxy server is used, allows remote attackers to violate the security model for an applet's outbound connections via a multi-pin DNS rebinding attack in which the applet download relies on DNS resolution on the proxy server, but the applet's socket operations rely on DNS resolution on the local machine, a different issue than CVE-2007-5274. NOTE: this is similar to CVE-2007-5232.", 'modified': '2018-10-30T16:26:00', 'id': 'CVE-2007-5273', 'published': '2007-10-08T23:17:00', 'href': 'https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2007-5273', 'title': 'CVE-2007-5273', 'type': 'cve', 'cvss': {'score': 2.6, 'vector': 'AV:N/AC:H/Au:N/C:N/I:P/A:N'}, 'enchantments': {'vulnersScore': 'PENDING'}}, 'CVE-2007-5274': {'lastseen': '2019-05-29T18:09:01', 'bulletinFamily': 'NVD', 'description': 'Sun Java Runtime Environment (JRE) in JDK and JRE 6 Update 2 and earlier, JDK and JRE 5.0 Update 12 and earlier, SDK and JRE 1.4.2_15 and earlier, and SDK and JRE 1.3.1_20 and earlier, when Firefox or Opera is used, allows remote attackers to violate the security model for JavaScript outbound connections via a multi-pin DNS rebinding attack dependent on the LiveConnect API, in which JavaScript download relies on DNS resolution by the browser, but JavaScript socket operations rely on separate DNS resolution by a Java Virtual Machine (JVM), a different issue than CVE-2007-5273.  NOTE: this is similar to CVE-2007-5232.', 'modified': '2018-10-30T16:26:00', 'id': 'CVE-2007-5274', 'published': '2007-10-08T23:17:00', 'href': 'https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2007-5274', 'title': 'CVE-2007-5274', 'type': 'cve', 'cvss': {'score': 2.6, 'vector': 'AV:N/AC:H/Au:N/C:N/I:P/A:N'}, 'enchantments': {'vulnersScore': 'PENDING'}}, 'CVE-2007-5232': {'lastseen': '2019-05-29T18:09:01', 'bulletinFamily': 'NVD', 'description': "Sun Java Runtime Environment (JRE) in JDK and JRE 6 Update 2 and earlier, JDK and JRE 5.0 Update 12 and earlier, SDK and JRE 1.4.2_15 and earlier, and SDK and JRE 1.3.1_20 and earlier, when applet caching is enabled, allows remote attackers to violate the security model for an applet's outbound connections via a DNS rebinding attack.", 'modified': '2018-10-30T16:26:00', 'id': 'CVE-2007-5232', 'published': '2007-10-05T23:17:00', 'href': 'https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2007-5232', 'title': 'CVE-2007-5232', 'type': 'cve', 'cvss': {'score': 4.0, 'vector': 'AV:N/AC:H/Au:N/C:P/I:P/A:N'}, 'enchantments': {'vulnersScore': 'PENDING'}}, 'CVE-2007-0760': {'lastseen': '2019-05-29T18:08:58', 'bulletinFamily': 'NVD', 'description': 'EQdkp 1.3.1 and earlier authenticates administrative requests by verifying that the HTTP Referer header specifies an admin/ URL, which allows remote attackers to read or modify account names and passwords via a spoofed Referer.', 'modified': '2017-10-19T01:30:00', 'id': 'CVE-2007-0760', 'published': '2007-02-06T02:28:00', 'href': 'https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2007-0760', 'title': 'CVE-2007-0760', 'type': 'cve', 'cvss': {'score': 7.5, 'vector': 'AV:N/AC:L/Au:N/C:P/I:P/A:P'}, 'enchantments': {'vulnersScore': 'PENDING'}}, 'CVE-2004-2124': {'lastseen': '2019-05-29T18:08:04', 'bulletinFamily': 'NVD', 'description': 'The register_globals simulation capability in Gallery 1.3.1 through 1.4.1 allows remote attackers to modify the HTTP_POST_VARS variable and conduct a PHP remote file inclusion attack via the GALLERY_BASEDIR parameter, a different vulnerability than CVE-2002-1412.', 'modified': '2017-07-11T01:31:00', 'id': 'CVE-2004-2124', 'published': '2004-12-31T05:00:00', 'href': 'https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2004-2124', 'title': 'CVE-2004-2124', 'type': 'cve', 'cvss': {'score': 5.0, 'vector': 'AV:N/AC:L/Au:N/C:N/I:P/A:N'}, 'enchantments': {'vulnersScore': 'PENDING'}}, 'CVE-2002-1412': {'lastseen': '2019-05-29T18:07:39', 'bulletinFamily': 'NVD', 'description': 'Gallery photo album package before 1.3.1 allows local and possibly remote attackers to execute arbitrary code via a modified GALLERY_BASEDIR variable that points to a directory or URL that contains a Trojan horse init.php script.', 'modified': '2017-10-10T01:30:00', 'id': 'CVE-2002-1412', 'published': '2003-04-11T04:00:00', 'href': 'https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2002-1412', 'title': 'CVE-2002-1412', 'type': 'cve', 'cvss': {'score': 7.5, 'vector': 'AV:N/AC:L/Au:N/C:P/I:P/A:P'}, 'enchantments': {'vulnersScore': 'PENDING'}}, 'CVE-2001-0399': {'lastseen': '2019-05-29T18:07:37', 'bulletinFamily': 'NVD', 'description': 'Caucho Resin 1.3b1 and earlier allows remote attackers to read source code for Javabean files by inserting a .jsp before the WEB-INF specifier in an HTTP request.', 'modified': '2016-10-18T02:10:00', 'id': 'CVE-2001-0399', 'published': '2001-06-18T04:00:00', 'href': 'https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2001-0399', 'title': 'CVE-2001-0399', 'type': 'cve', 'cvss': {'score': 5.0, 'vector': 'AV:N/AC:L/Au:N/C:P/I:N/A:N'}, 'enchantments': {'vulnersScore': 'PENDING'}}, 'CVE-2013-2070': {'lastseen': '2019-05-29T18:13:02', 'bulletinFamily': 'NVD', 'description': 'http/modules/ngx_http_proxy_module.c in nginx 1.1.4 through 1.2.8 and 1.3.0 through 1.4.0, when proxy_pass is used with untrusted HTTP servers, allows remote attackers to cause a denial of service (crash) and obtain sensitive information from worker process memory via a crafted proxy response, a similar vulnerability to CVE-2013-2028.', 'modified': '2018-10-30T16:26:00', 'id': 'CVE-2013-2070', 'published': '2013-07-20T03:37:00', 'href': 'https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2013-2070', 'title': 'CVE-2013-2070', 'type': 'cve', 'cvss': {'score': 5.8, 'vector': 'AV:N/AC:M/Au:N/C:P/I:N/A:P'}, 'enchantments': {'vulnersScore': 'PENDING'}}, 'CVE-2013-2028': {'lastseen': '2019-05-29T18:13:02', 'bulletinFamily': 'NVD', 'description': 'The ngx_http_parse_chunked function in http/ngx_http_parse.c in nginx 1.3.9 through 1.4.0 allows remote attackers to cause a denial of service (crash) and execute arbitrary code via a chunked Transfer-Encoding request with a large chunk size, which triggers an integer signedness error and a stack-based buffer overflow.', 'modified': '2018-10-30T16:26:00', 'id': 'CVE-2013-2028', 'published': '2013-07-20T03:37:00', 'href': 'https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2013-2028', 'title': 'CVE-2013-2028', 'type': 'cve', 'cvss': {'score': 7.5, 'vector': 'AV:N/AC:L/Au:N/C:P/I:P/A:P'}, 'enchantments': {'vulnersScore': 'PENDING'}}, 'CVE-2011-4317': {'lastseen': '2020-04-04T00:01:33', 'bulletinFamily': 'NVD', 'description': 'The mod_proxy module in the Apache HTTP Server 1.3.x through 1.3.42, 2.0.x through 2.0.64, and 2.2.x through 2.2.21, when the Revision 1179239 patch is in place, does not properly interact with use of (1) RewriteRule and (2) ProxyPassMatch pattern matches for configuration of a reverse proxy, which allows remote attackers to send requests to intranet servers via a malformed URI containing an @ (at sign) character and a : (colon) character in invalid positions.  NOTE: this vulnerability exists because of an incomplete fix for CVE-2011-3368.', 'modified': '2018-01-09T02:29:00', 'id': 'CVE-2011-4317', 'published': '2011-11-30T04:05:00', 'href': 'https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2011-4317', 'title': 'CVE-2011-4317', 'type': 'cve', 'cvss': {'score': 4.3, 'vector': 'AV:N/AC:M/Au:N/C:N/I:P/A:N'}, 'enchantments': {'vulnersScore': 'PENDING'}}, 'CVE-2011-3368': {'lastseen': '2020-04-04T00:01:27', 'bulletinFamily': 'NVD', 'description': 'The mod_proxy module in the Apache HTTP Server 1.3.x through 1.3.42, 2.0.x through 2.0.64, and 2.2.x through 2.2.21 does not properly interact with use of (1) RewriteRule and (2) ProxyPassMatch pattern matches for configuration of a reverse proxy, which allows remote attackers to send requests to intranet servers via a malformed URI containing an initial @ (at sign) character.', 'modified': '2018-01-09T02:29:00', 'id': 'CVE-2011-3368', 'published': '2011-10-05T22:55:00', 'href': 'https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2011-3368', 'title': 'CVE-2011-3368', 'type': 'cve', 'cvss': {'score': 5.0, 'vector': 'AV:N/AC:L/Au:N/C:P/I:N/A:N'}, 'enchantments': {'vulnersScore': 'PENDING'}}, 'CVE-2010-3574': {'lastseen': '2019-05-29T18:10:30', 'bulletinFamily': 'NVD', 'description': "Unspecified vulnerability in the Networking component in Oracle Java SE and Java for Business 6 Update 21, 5.0 Update 25, 1.4.2_27, and 1.3.1_28 allows remote attackers to affect confidentiality, integrity, and availability via unknown vectors.  NOTE: the previous information was obtained from the October 2010 CPU.  Oracle has not commented on claims from a reliable downstream vendor that HttpURLConnection does not properly check for the allowHttpTrace permission, which allows untrusted code to perform HTTP TRACE requests.\nPer: http://www.oracle.com/technetwork/topics/security/cpujan2011-194091.html\r\n'Oracle released a Java Critical Patch Update in October 2010 to address multiple vulnerabilities affecting the Java Runtime Environment. Oracle CVE-2010-3574 refers to the advisories that were applicable to JRockit from the Java Critical Patch Update. The CVSS score of this vulnerability CVE# reflects the highest among those fixed in JRockit. The complete list of all advisories addressed in JRockit under CVE-2010-3574 is as follows: CVE-2010-1321, CVE-2010-3541, CVE-2010-3548, CVE-2010-3549, CVE-2010-3551 CVE-2010-3553, CVE-2010-3554, CVE-2010-3555, CVE-2010-3556, CVE-2010-3557, CVE-2010-3559, CVE-2010-3561, CVE-2010-3562, CVE-2010-3565, CVE-2010-3566, CVE-2010-3567, CVE-2010-3568, CVE-2010-3569, CVE-2010-3571, CVE-2010-3572, CVE-2010-3573 and CVE-2010-3574.'", 'modified': '2018-10-30T16:26:00', 'id': 'CVE-2010-3574', 'published': '2010-10-19T22:00:00', 'href': 'https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2010-3574', 'title': 'CVE-2010-3574', 'type': 'cve', 'cvss': {'score': 10.0, 'vector': 'AV:N/AC:L/Au:N/C:C/I:C/A:C'}, 'enchantments': {'vulnersScore': 'PENDING'}}, 'CVE-2010-3553': {'lastseen': '2019-05-29T18:10:30', 'bulletinFamily': 'NVD', 'description': "Unspecified vulnerability in the Swing component in Oracle Java SE and Java for Business 6 Update 21, 5.0 Update 25, 1.4.2_27, and 1.3.1_28 allows remote attackers to affect confidentiality, integrity, and availability via unknown vectors.  NOTE: the previous information was obtained from the October 2010 CPU.  Oracle has not commented on claims from a reliable downstream vendor that this is related to unsafe reflection involving the UIDefault.ProxyLazyValue class.\nPer: http://www.oracle.com/technetwork/topics/security/javacpuoct2010-176258.html\r\n\r\n'May be vulnerable only through untrusted Java Web Start applications and Java applets.'", 'modified': '2018-10-30T16:26:00', 'id': 'CVE-2010-3553', 'published': '2010-10-19T22:00:00', 'href': 'https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2010-3553', 'title': 'CVE-2010-3553', 'type': 'cve', 'cvss': {'score': 10.0, 'vector': 'AV:N/AC:L/Au:N/C:C/I:C/A:C'}, 'enchantments': {'vulnersScore': 'PENDING'}}, 'CVE-2010-3549': {'lastseen': '2019-05-29T18:10:30', 'bulletinFamily': 'NVD', 'description': "Unspecified vulnerability in the Networking component in Oracle Java SE and Java for Business 6 Update 21, 5.0 Update 25, 1.4.2_27, and 1.3.1_28 allows remote attackers to affect confidentiality, integrity, and availability via unknown vectors.  NOTE: the previous information was obtained from the October 2010 CPU.  Oracle has not commented on claims from a reliable downstream vendor that this is an HTTP request splitting vulnerability involving the handling of the chunked transfer encoding method by the HttpURLConnection class.\nPer: http://www.oracle.com/technetwork/topics/security/javacpuoct2010-176258.html\r\n\r\n\r\n'May be vulnerable only through untrusted Java Web Start applications and Java applets.'", 'modified': '2018-10-30T16:26:00', 'id': 'CVE-2010-3549', 'published': '2010-10-19T22:00:00', 'href': 'https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2010-3549', 'title': 'CVE-2010-3549', 'type': 'cve', 'cvss': {'score': 6.8, 'vector': 'AV:N/AC:M/Au:N/C:P/I:P/A:P'}, 'enchantments': {'vulnersScore': 'PENDING'}}, 'CVE-2010-3541': {'lastseen': '2019-05-29T18:10:30', 'bulletinFamily': 'NVD', 'description': "Unspecified vulnerability in the Networking component in Oracle Java SE and Java for Business 6 Update 21, 5.0 Update 25, 1.4.2_27, and 1.3.1_28 allows remote attackers to affect confidentiality, integrity, and availability via unknown vectors.  NOTE: the previous information was obtained from the October 2010 CPU.  Oracle has not commented on claims from a reliable downstream vendor that this is related to missing validation of request headers in the HttpURLConnection class when they are set by applets, which allows remote attackers to bypass the intended security policy.\nPer: http://www.oracle.com/technetwork/topics/security/javacpuoct2010-176258.html\r\n\r\n'May be vulnerable only through untrusted Java Web Start applications and Java applets.'", 'modified': '2018-10-30T16:26:00', 'id': 'CVE-2010-3541', 'published': '2010-10-19T22:00:00', 'href': 'https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2010-3541', 'title': 'CVE-2010-3541', 'type': 'cve', 'cvss': {'score': 5.1, 'vector': 'AV:N/AC:H/Au:N/C:P/I:P/A:P'}, 'enchantments': {'vulnersScore': 'PENDING'}}, 'CVE-2010-1623': {'lastseen': '2020-04-10T12:25:50', 'bulletinFamily': 'NVD', 'description': 'Memory leak in the apr_brigade_split_line function in buckets/apr_brigade.c in the Apache Portable Runtime Utility library (aka APR-util) before 1.3.10, as used in the mod_reqtimeout module in the Apache HTTP Server and other software, allows remote attackers to cause a denial of service (memory consumption) via unspecified vectors related to the destruction of an APR bucket.', 'modified': '2017-09-19T01:30:00', 'id': 'CVE-2010-1623', 'published': '2010-10-04T21:00:00', 'href': 'https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2010-1623', 'title': 'CVE-2010-1623', 'type': 'cve', 'cvss': {'score': 5.0, 'vector': 'AV:N/AC:L/Au:N/C:N/I:N/A:P'}, 'enchantments': {'vulnersScore': 'PENDING'}}, 'CVE-2010-0010': {'lastseen': '2019-05-29T18:10:25', 'bulletinFamily': 'NVD', 'description': 'Integer overflow in the ap_proxy_send_fb function in proxy/proxy_util.c in mod_proxy in the Apache HTTP Server before 1.3.42 on 64-bit platforms allows remote origin servers to cause a denial of service (daemon crash) or possibly execute arbitrary code via a large chunk size that triggers a heap-based buffer overflow.', 'modified': '2018-10-10T19:49:00', 'id': 'CVE-2010-0010', 'published': '2010-02-02T16:30:00', 'href': 'https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2010-0010', 'title': 'CVE-2010-0010', 'type': 'cve', 'cvss': {'score': 6.8, 'vector': 'AV:N/AC:M/Au:N/C:P/I:P/A:P'}, 'enchantments': {'vulnersScore': 'PENDING'}}, 'CVE-2009-3877': {'lastseen': '2019-12-18T13:57:57', 'bulletinFamily': 'NVD', 'description': 'Unspecified vulnerability in Sun Java SE in JDK and JRE 5.0 before Update 22, JDK and JRE 6 before Update 17, SDK and JRE 1.3.x before 1.3.1_27, and SDK and JRE 1.4.x before 1.4.2_24 allows remote attackers to cause a denial of service (memory consumption) via crafted HTTP headers, which are not properly parsed by the ASN.1 DER input stream parser, aka Bug Id 6864911.', 'modified': '2018-10-30T16:26:00', 'id': 'CVE-2009-3877', 'published': '2009-11-05T16:30:00', 'href': 'https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2009-3877', 'title': 'CVE-2009-3877', 'type': 'cve', 'cvss': {'score': 5.0, 'vector': 'AV:N/AC:L/Au:N/C:N/I:N/A:P'}, 'enchantments': {'vulnersScore': 'PENDING'}}, 'CVE-2009-0164': {'lastseen': '2019-05-29T18:09:56', 'bulletinFamily': 'NVD', 'description': 'The web interface for CUPS before 1.3.10 does not validate the HTTP Host header in a client request, which makes it easier for remote attackers to conduct DNS rebinding attacks.', 'modified': '2018-10-11T21:00:00', 'id': 'CVE-2009-0164', 'published': '2009-04-24T15:30:00', 'href': 'https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2009-0164', 'title': 'CVE-2009-0164', 'type': 'cve', 'cvss': {'score': 6.4, 'vector': 'AV:N/AC:L/Au:N/C:N/I:P/A:P'}, 'enchantments': {'vulnersScore': 'PENDING'}}, 'CVE-2005-2088': {'lastseen': '2020-04-03T23:44:41', 'bulletinFamily': 'NVD', 'description': 'The Apache HTTP server before 1.3.34, and 2.0.x before 2.0.55, when acting as an HTTP proxy, allows remote attackers to poison the web cache, bypass web application firewall protection, and conduct XSS attacks via an HTTP request with both a "Transfer-Encoding: chunked" header and a Content-Length header, which causes Apache to incorrectly handle and forward the body of the request in a way that causes the receiving server to process it as a separate HTTP request, aka "HTTP Request Smuggling."', 'modified': '2018-10-19T15:32:00', 'id': 'CVE-2005-2088', 'published': '2005-07-05T04:00:00', 'href': 'https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2005-2088', 'title': 'CVE-2005-2088', 'type': 'cve', 'cvss': {'score': 4.3, 'vector': 'AV:N/AC:M/Au:N/C:N/I:P/A:N'}, 'enchantments': {'vulnersScore': 'PENDING'}}, 'CVE-2005-1760': {'lastseen': '2019-05-29T18:08:14', 'bulletinFamily': 'NVD', 'description': 'sysreport 1.3.15 and earlier includes contents of the up2date file in a report, which leaks the password for a proxy server in plaintext and allows local users to gain privileges.', 'modified': '2017-10-11T01:30:00', 'id': 'CVE-2005-1760', 'published': '2005-06-13T04:00:00', 'href': 'https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2005-1760', 'title': 'CVE-2005-1760', 'type': 'cve', 'cvss': {'score': 7.5, 'vector': 'AV:N/AC:L/Au:N/C:P/I:P/A:P'}, 'enchantments': {'vulnersScore': 'PENDING'}}, 'CVE-2004-2762': {'lastseen': '2019-05-29T18:08:04', 'bulletinFamily': 'NVD', 'description': 'The server in IBM Tivoli Storage Manager (TSM) 4.2.x on MVS, 5.1.9.x before 5.1.9.1, 5.1.x before 5.1.10, 5.2.2.x before 5.2.2.3, 5.2.x before 5.2.3, 5.3.x before 5.3.0, and 6.x before 6.1, when the HTTP communication method is enabled, allows remote attackers to cause a denial of service (daemon crash or hang) via unspecified HTTP traffic, as demonstrated by the IBM port scanner 1.3.1.', 'modified': '2017-08-17T01:29:00', 'id': 'CVE-2004-2762', 'published': '2009-03-31T18:24:00', 'href': 'https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2004-2762', 'title': 'CVE-2004-2762', 'type': 'cve', 'cvss': {'score': 4.3, 'vector': 'AV:N/AC:M/Au:N/C:N/I:N/A:P'}, 'enchantments': {'vulnersScore': 'PENDING'}}, 'CVE-2004-0700': {'lastseen': '2019-05-29T18:08:03', 'bulletinFamily': 'NVD', 'description': 'Format string vulnerability in the mod_proxy hook functions function in ssl_engine_log.c in mod_ssl before 2.8.19 for Apache before 1.3.31 may allow remote attackers to execute arbitrary messages via format string specifiers in certain log messages for HTTPS that are handled by the ssl_log function.', 'modified': '2017-07-11T01:30:00', 'id': 'CVE-2004-0700', 'published': '2004-07-27T04:00:00', 'href': 'https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2004-0700', 'title': 'CVE-2004-0700', 'type': 'cve', 'cvss': {'score': 7.5, 'vector': 'AV:N/AC:L/Au:N/C:P/I:P/A:P'}, 'enchantments': {'vulnersScore': 'PENDING'}}, 'CVE-2004-0492': {'lastseen': '2019-05-29T18:08:02', 'bulletinFamily': 'NVD', 'description': 'Heap-based buffer overflow in proxy_util.c for mod_proxy in Apache 1.3.25 to 1.3.31 allows remote attackers to cause a denial of service (process crash) and possibly execute arbitrary code via a negative Content-Length HTTP header field, which causes a large amount of data to be copied.', 'modified': '2017-10-11T01:29:00', 'id': 'CVE-2004-0492', 'published': '2004-08-06T04:00:00', 'href': 'https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2004-0492', 'title': 'CVE-2004-0492', 'type': 'cve', 'cvss': {'score': 10.0, 'vector': 'AV:N/AC:L/Au:N/C:C/I:C/A:C'}, 'enchantments': {'vulnersScore': 'PENDING'}}, 'CVE-2003-1580': {'lastseen': '2019-05-29T18:07:57', 'bulletinFamily': 'NVD', 'description': 'The Apache HTTP Server 2.0.44, when DNS resolution is enabled for client IP addresses, uses a logging format that does not identify whether a dotted quad represents an unresolved IP address, which allows remote attackers to spoof IP addresses via crafted DNS responses containing numerical top-level domains, as demonstrated by a forged 123.123.123.123 domain name, related to an "Inverse Lookup Log Corruption (ILLC)" issue.', 'modified': '2010-02-08T05:00:00', 'id': 'CVE-2003-1580', 'published': '2010-02-05T22:30:00', 'href': 'https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2003-1580', 'title': 'CVE-2003-1580', 'type': 'cve', 'cvss': {'score': 4.3, 'vector': 'AV:N/AC:M/Au:N/C:N/I:P/A:N'}, 'enchantments': {'vulnersScore': 'PENDING'}}, 'CVE-2002-2012': {'lastseen': '2019-05-29T18:07:39', 'bulletinFamily': 'NVD', 'description': 'Unknown vulnerability in Apache 1.3.19 running on HP Secure OS for Linux 1.0 allows remote attackers to cause "unexpected results" via an HTTP request.', 'modified': '2008-09-05T20:32:00', 'id': 'CVE-2002-2012', 'published': '2002-12-31T05:00:00', 'href': 'https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2002-2012', 'title': 'CVE-2002-2012', 'type': 'cve', 'cvss': {'score': 5.0, 'vector': 'AV:N/AC:L/Au:N/C:N/I:N/A:P'}, 'enchantments': {'vulnersScore': 'PENDING'}}, 'CVE-2002-0177': {'lastseen': '2019-05-29T18:07:38', 'bulletinFamily': 'NVD', 'description': 'Buffer overflows in icecast 1.3.11 and earlier allows remote attackers to execute arbitrary code via a long HTTP GET request from an MP3 client.', 'modified': '2016-10-18T02:16:00', 'id': 'CVE-2002-0177', 'published': '2002-04-22T04:00:00', 'href': 'https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2002-0177', 'title': 'CVE-2002-0177', 'type': 'cve', 'cvss': {'score': 7.5, 'vector': 'AV:N/AC:L/Au:N/C:P/I:P/A:P'}, 'enchantments': {'vulnersScore': 'PENDING'}}, 'CVE-2001-1083': {'lastseen': '2019-05-29T18:07:38', 'bulletinFamily': 'NVD', 'description': 'Icecast 1.3.7, and other versions before 1.3.11 with HTTP server file streaming support enabled allows remote attackers to cause a denial of service (crash) via a URL that ends in . (dot), / (forward slash), or \\ (backward slash).', 'modified': '2017-10-10T01:29:00', 'id': 'CVE-2001-1083', 'published': '2001-06-26T04:00:00', 'href': 'https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2001-1083', 'title': 'CVE-2001-1083', 'type': 'cve', 'cvss': {'score': 5.0, 'vector': 'AV:N/AC:L/Au:N/C:N/I:N/A:P'}, 'enchantments': {'vulnersScore': 'PENDING'}}, 'CVE-2001-0925': {'lastseen': '2019-05-29T18:07:38', 'bulletinFamily': 'NVD', 'description': 'The default installation of Apache before 1.3.19 allows remote attackers to list directories instead of the multiview index.html file via an HTTP request for a path that contains many / (slash) characters, which causes the path to be mishandled by (1) mod_negotiation, (2) mod_dir, or (3) mod_autoindex.', 'modified': '2017-12-19T02:29:00', 'id': 'CVE-2001-0925', 'published': '2001-03-12T05:00:00', 'href': 'https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2001-0925', 'title': 'CVE-2001-0925', 'type': 'cve', 'cvss': {'score': 5.0, 'vector': 'AV:N/AC:L/Au:N/C:P/I:N/A:N'}, 'enchantments': {'vulnersScore': 'PENDING'}}, 'CVE-2001-0129': {'lastseen': '2019-05-29T18:07:37', 'bulletinFamily': 'NVD', 'description': 'Buffer overflow in Tinyproxy HTTP proxy 1.3.3 and earlier allows remote attackers to cause a denial of service and possibly execute arbitrary commands via a long connect request.', 'modified': '2018-05-03T01:29:00', 'id': 'CVE-2001-0129', 'published': '2001-03-12T05:00:00', 'href': 'https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2001-0129', 'title': 'CVE-2001-0129', 'type': 'cve', 'cvss': {'score': 10.0, 'vector': 'AV:N/AC:L/Au:N/C:C/I:C/A:C'}, 'enchantments': {'vulnersScore': 'PENDING'}}, 'CVE-2000-1206': {'lastseen': '2019-05-29T18:07:37', 'bulletinFamily': 'NVD', 'description': 'Vulnerability in Apache httpd before 1.3.11, when configured for mass virtual hosting using mod_rewrite, or mod_vhost_alias in Apache 1.3.9, allows remote attackers to retrieve arbitrary files.', 'modified': '2008-09-10T19:06:00', 'id': 'CVE-2000-1206', 'published': '1999-08-20T04:00:00', 'href': 'https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2000-1206', 'title': 'CVE-2000-1206', 'type': 'cve', 'cvss': {'score': 5.0, 'vector': 'AV:N/AC:L/Au:N/C:P/I:N/A:N'}, 'enchantments': {'vulnersScore': 'PENDING'}}, 'CVE-2000-0869': {'lastseen': '2019-05-29T18:07:37', 'bulletinFamily': 'NVD', 'description': 'The default configuration of Apache 1.3.12 in SuSE Linux 6.4 enables WebDAV, which allows remote attackers to list arbitrary directories via the PROPFIND HTTP request method.', 'modified': '2017-10-10T01:29:00', 'id': 'CVE-2000-0869', 'published': '2000-11-14T05:00:00', 'href': 'https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2000-0869', 'title': 'CVE-2000-0869', 'type': 'cve', 'cvss': {'score': 5.0, 'vector': 'AV:N/AC:L/Au:N/C:P/I:N/A:N'}, 'enchantments': {'vulnersScore': 'PENDING'}}}
            
            if len(results) == 0: #If there's no CVE's then display an Error message 
                entry_ip.delete(0, tk.END)
                entry_ip.insert(0, 'Error: No data dound for ' + ip_address + "!" )

            else:
                tree = create_table()
 
                print("Appending Data")

                with open(csvfile, mode='a+', newline="") as csv_file:
                    csv_file.seek(0)
                    reader = csv.reader(csv_file)
                    data = list(reader) 
                    fieldnames = ['IP Address', 'Vulnerability', 'Description']
                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames) 

                    if fieldnames not in data: #writes header if not in the file, usually runs once if the CSV file doesnt exist 
                        writer.writeheader()

                    for i in results:
                        description = results.get(i).get('description')        
                        og_description = description
                        #import textwarp for support 
                        if len(description) >= 210: 

                            description = textwrap.fill(description, 210) #creates newline at the end of a word of index 175
                        
                        tree.insert("", 'end', text ="", values =(ip_address, i , description)) #writes to table to display in tkinter
                        line = [ip_address, i, og_description]

                        #print(line)
                        if line not in data:
                            #print("write to csv\n")
                            writer.writerow({'IP Address': ip_address, 'Vulnerability': i, 'Description': og_description}) #writes to csv file
                        else:
                            print("throw away\n")
             

            sort_csv(csvfile)


        
        # show home button_tab
        home_button_tab = tk.Button(root, text="Home", bg="#6db8f2", fg='white', command= lambda:switch_tab("home")) #when pressed (lambda), executes command. without "lambda" the command will run on launch of code regardless if it was pressed or not  
        home_button_tab.place(relx =0.10, rely=0.00, relwidth=0.20, relheight=0.07, anchor='n') #relx = x position, rely = y position, relwidth = width of entity, relheight = height of entity

        # show scanning button_tab
        scanning_button_tab = tk.Button(root, text="Scanning", bg="#03021a", fg='white', command= lambda:switch_tab("scanning"))
        scanning_button_tab.place(relx =0.30, rely=0.00, relwidth=0.20, relheight=0.07, anchor='n')

        # show patching button_tab
        patching_button_tab = tk.Button(text="Patching", bg="#0b6eba", fg='white', command= lambda:switch_tab("patching"))
        patching_button_tab.place(relx=0.50, rely=0.00, relwidth=0.20, relheight=0.07, anchor='n')

        # show network button_tab
        network_button_tab = tk.Button(root, text="Network", bg="#085b9c", fg='white', command= lambda:switch_tab("network"))
        network_button_tab.place(relx =0.70, rely=0.00, relwidth=0.20, relheight=0.07, anchor='n')

        # show hostbase button_tab
        hostbase_button_tab = tk.Button(text="Hostbase", bg="#054a80", fg='white', command= lambda:switch_tab("hostbase"))
        hostbase_button_tab.place(relx=0.90, rely=0.00, relwidth=0.20, relheight=0.07, anchor='n')

    if tab_name =="patching":

        # take in CSV database and post results in table format. once "patched" ip/host then remove from CSV database.
        # 1. open up csv
        # 2. create data table
        # 3. display csv on data table
        # 4. have a "patch" button to remove from data table and remove from csv 
        # 5. refresh and show data table again 
        tree = create_table()

        with open(csvfile, mode='r', newline="") as csv_file:
            reader = csv.reader(csv_file)
            data = list(reader) 

            for row in (data[1:]):
                #print(row)
                ip_address = row[0]
                cve = row[1]
                description = row[2]


                if len(description) >= 210: 
                    description = textwrap.fill(description, 210) #creates newline at the end of a word of index 175
                
                tree.insert("", 'end', text ="", values =(ip_address, cve , description)) #writes to table to display in tkinter


        # show home button_tab
        home_button_tab = tk.Button(root, text="Home", bg="#6db8f2", fg='white', command= lambda:switch_tab("home")) #when pressed (lambda), executes command. without "lambda" the command will run on launch of code regardless if it was pressed or not  
        home_button_tab.place(relx =0.10, rely=0.00, relwidth=0.20, relheight=0.07, anchor='n') #relx = x position, rely = y position, relwidth = width of entity, relheight = height of entity

        # show scanning button_tab
        scanning_button_tab = tk.Button(root, text="Scanning", bg="#1e92eb", fg='white', command= lambda:switch_tab("scanning"))
        scanning_button_tab.place(relx =0.30, rely=0.00, relwidth=0.20, relheight=0.07, anchor='n')

        # show patching button_tab
        patching_button_tab = tk.Button(text="Patching", bg="#03021a", fg='white', command= lambda:switch_tab("patching"))
        patching_button_tab.place(relx=0.50, rely=0.00, relwidth=0.20, relheight=0.07, anchor='n')

        # show network button_tab
        network_button_tab = tk.Button(root, text="Network", bg="#085b9c", fg='white', command= lambda:switch_tab("network"))
        network_button_tab.place(relx =0.70, rely=0.00, relwidth=0.20, relheight=0.07, anchor='n')

        # show hostbase button_tab
        hostbase_button_tab = tk.Button(text="Hostbase", bg="#054a80", fg='white', command= lambda:switch_tab("hostbase"))
        hostbase_button_tab.place(relx=0.90, rely=0.00, relwidth=0.20, relheight=0.07, anchor='n')

    if tab_name =="network":

        block_ip_content = tk.StringVar()
        block_ip = tk.Entry(frame, font = "Calibri 15", textvariable=block_ip_content)
        block_ip.place(relx=0.50, rely=0.10, relwidth=0.40, relheight=0.065, anchor='n')
  

        block_button = tk.Button(frame, text="Block IP", bg="#1e92eb", fg='white', command= lambda:press_block())
        block_button.place(relx =0.85, rely=0.10, relwidth=0.10, relheight=0.065, anchor='n')

        unblock_ip_content = tk.StringVar()
        unblock_ip = tk.Entry(frame, textvariable=unblock_ip_content)
        unblock_ip.place(relx=0.50, rely=0.20, relwidth=0.40, relheight=0.065, anchor='n')
        
        unblock_button = tk.Button(frame, text="Unblock IP", bg="#1e92eb", fg='white', command= lambda:press_remove())
        unblock_button.place(relx =0.85, rely=0.2, relwidth=0.10, relheight=0.065, anchor='n')

        def press_block():
            ip_address = block_ip_content.get()

            try:
                #print(ip_address)
                # https://github.com/scipag/vulscan
                #windows_7.check_admin("Blocked IP From Console", ip_address)
                windows_7.check_admin()
                windows_7.add_rule("Blocked IP From Console", ip_address)
                print("success")
            except:
                print("YOu FAIL")

        def press_remove():
            ip_address = unblock_ip_content.get()

            try:
                print(ip_address)
                # https://github.com/scipag/vulscan
                windows_7.check_admin()
                windows_7.delete_rule("Remove Blocked IP From Console", ip_address)
                print("success")
            except:
                print("YOu FAIL")

        # show home button_tab
        home_button_tab = tk.Button(root, text="Home", bg="#6db8f2", fg='white', command= lambda:switch_tab("home")) #when pressed (lambda), executes command. without "lambda" the command will run on launch of code regardless if it was pressed or not  
        home_button_tab.place(relx =0.10, rely=0.00, relwidth=0.20, relheight=0.07, anchor='n') #relx = x position, rely = y position, relwidth = width of entity, relheight = height of entity

        # show scanning button_tab
        scanning_button_tab = tk.Button(root, text="Scanning", bg="#1e92eb", fg='white', command= lambda:switch_tab("scanning"))
        scanning_button_tab.place(relx =0.30, rely=0.00, relwidth=0.20, relheight=0.07, anchor='n')

        # show patching button_tab
        patching_button_tab = tk.Button(text="Patching", bg="#0b6eba", fg='white', command= lambda:switch_tab("patching"))
        patching_button_tab.place(relx=0.50, rely=0.00, relwidth=0.20, relheight=0.07, anchor='n')

        # show network button_tab
        network_button_tab = tk.Button(root, text="Network", bg="#03021a", fg='white', command= lambda:switch_tab("network"))
        network_button_tab.place(relx =0.70, rely=0.00, relwidth=0.20, relheight=0.07, anchor='n')

        # show hostbase button_tab
        hostbase_button_tab = tk.Button(text="Hostbase", bg="#054a80", fg='white', command= lambda:switch_tab("hostbase"))
        hostbase_button_tab.place(relx=0.90, rely=0.00, relwidth=0.20, relheight=0.07, anchor='n')

    if tab_name =="hostbase":
        ip_content = tk.StringVar()
        entry_ip = tk.Entry(frame, font = "Calibri 15", textvariable=ip_content)
        entry_ip.place(relx=0.50, rely=0.10, relwidth=0.40, relheight=0.065, anchor='n')

        def scanFiles(): 
            filename = filedialog.askdirectory(initialdir = "/", 
                                            title = "Select a Directory")
            filename = "Scanning: " + filename
            entry_ip = tk.Entry(frame, font = "Calibri 15", textvariable=filename)
            entry_ip.place(relx=0.50, rely=0.10, relwidth=0.40, relheight=0.065, anchor='n')
            entry_ip.insert(tk.END,filename)
    

        scan_file_button = tk.Button(frame, text="Scan Directory", bg="#1e92eb", fg='white', command= scanFiles)
        scan_file_button.place(relx =0.85, rely=0.10, relwidth=0.10, relheight=0.065, anchor='n')

        quarantine_file_button = tk.Button(frame, text="Show Quarantined Files", bg="#1e92eb", fg='white', command= lambda:press_block())
        quarantine_file_button.place(relx =0.85, rely=0.2, relwidth=0.10, relheight=0.065, anchor='n')

        release_button = tk.Button(frame, text="Show Released Files", bg="#1e92eb", fg='white', command= lambda:press_remove())
        release_button.place(relx =.85, rely=0.3, relwidth=0.10, relheight=0.065, anchor='n')

       
    
       
    # Change label contents 

       

        # Create a File Explorer label 
        
        # Grid method is chosen for placing 
        # the widgets at respective positions  
        # in a table like structure by 
        # specifying rows and columns 
        
        #button_file_button_tab.grid(column = 1, row = 2) 

        #button_exit.grid(column = 1,row = 3) 



        '''
        Jeffs Please Helps Good Sirire

        def result_box_display(text, num = 0):
        '''
        #This function will display success/failure/update messages in the bottom corner for users 
        '''
        resultbox.delete(0, tk.END)
        resultbox.insert(tk.END, text)
        if num == 1:
            resultbox.insert(tk.END, "Please add new rule in the Confluence documents!")

        def clear_placeholder(event):
        '''
        #If a user clicks on the comment entry box, then this function will delete the placeholder within the comment box
        '''
        entry.delete(0, tk.END)

        def add_placeholder(self):
        '''
        #If the user clicks out of the comment box and inputs no text, then this function will add in the placeholder text again
        '''
        if not entry.get():
            entry.insert(0, 'Please enter comment here:')

        def resize_image(event):
        '''
        #This function will resize the background image to match/expand to the window size
        '''
        new_width = event.width
        new_height = event.height
        image = copy_of_image.resize((new_width, new_height))
        photo = ImageTk.PhotoImage(image)
        label.config(image = photo)
        label.image = photo #avoid garbage collection

        #Image and properties to resize image to window size
        image = Image.open("C:\\elastalert\\scripts\\landscape.png")
        copy_of_image = image.copy()
        photo = ImageTk.PhotoImage(image)
        label = ttk.Label(root, image = photo)
        label.bind('<Configure>', resize_image)
        label.pack(fill='both', expand = 'yes')



        tk.Label(root, text='Field',font='Helvetica 12 bold').place(relx =0.150, rely=0.025, relwidth=0.095, relheight=0.025, anchor='n')
        tk.Label(root, text='Value',font='Helvetica 12 bold').place(relx =0.30, rely=0.025, relwidth=0.095, relheight=0.025, anchor='n')
        tk.Label(root, text='Select Annotation Stage',font='Helvetica 12 bold').place(relx =0.26, rely=0.885, relwidth=0.16, relheight=0.025, anchor='n')

        # Comment Entry
        content = tk.StringVar()
        entry= tk.Entry(root, textvariable=content)
        entry.insert(0, 'Please enter comment here:')
        entry.place(relx=0.10, rely=0.95, relwidth=0.50, relheight=0.025)

        entry.bind("<FocusIn>", clear_placeholder)
        #entry.bind("<FocusOut>", add_placeholder) 


        '''


        



        # show home button_tab
        home_button_tab = tk.Button(root, text="Home", bg="#6db8f2", fg='white', command= lambda:switch_tab("home")) #when pressed (lambda), executes command. without "lambda" the command will run on launch of code regardless if it was pressed or not  
        home_button_tab.place(relx =0.10, rely=0.00, relwidth=0.20, relheight=0.07, anchor='n') #relx = x position, rely = y position, relwidth = width of entity, relheight = height of entity

        # show scanning button_tab
        scanning_button_tab = tk.Button(root, text="Scanning", bg="#1e92eb", fg='white', command= lambda:switch_tab("scanning"))
        scanning_button_tab.place(relx =0.30, rely=0.00, relwidth=0.20, relheight=0.07, anchor='n')

        # show patching button_tab
        patching_button_tab = tk.Button(text="Patching", bg="#0b6eba", fg='white', command= lambda:switch_tab("patching"))
        patching_button_tab.place(relx=0.50, rely=0.00, relwidth=0.20, relheight=0.07, anchor='n')

        # show network button_tab
        network_button_tab = tk.Button(root, text="Network", bg="#085b9c", fg='white', command= lambda:switch_tab("network"))
        network_button_tab.place(relx =0.70, rely=0.00, relwidth=0.20, relheight=0.07, anchor='n')

        # show hostbase button_tab
        hostbase_button_tab = tk.Button(text="Hostbase", bg="#03021a", fg='white', command= lambda:switch_tab("hostbase"))
        hostbase_button_tab.place(relx=0.90, rely=0.00, relwidth=0.20, relheight=0.07, anchor='n')


if __name__ == "__main__":
    switch_tab("home") #start in home tab
    root.mainloop()
