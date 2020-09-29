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

root = tk.Tk() #creates the actual window


frame = Frame(root, background ="#03021a") #creates frame and makes it dark blue 
frame.pack(fill='both', expand=True)
frame.pack()

root.title("TKINTER > KIVY")

root.geometry("1920x1080") #sets the size of the GUI box 
#root.state("zoomed") #makes window full screen
def switch_tab(tab_name):

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

        ip_content = tk.StringVar()
        entry_ip = tk.Entry(frame, font = "Calibri 15", textvariable=ip_content)
        entry_ip.place(relx=0.50, rely=0.10, relwidth=0.40, relheight=0.065, anchor='n')
        
        scan_button = tk.Button(frame, text="Scan", bg="#1e92eb", fg='white', command= lambda:press_scan())
        scan_button.place(relx =0.85, rely=0.10, relwidth=0.10, relheight=0.065, anchor='n')

        def press_scan():
            ip_address = ip_content.get()
            #54.209.137.253
            
            print(ip_address)
            try:
                print("running scan")
                # https://github.com/scipag/vulscan
                Vulscan.scan(ip_address) # dumps results into 'portscandata.txt'
                print("work")

            except:
                print("error")

            try: 
                CVEnumbersExtractor.vulnScanExtract() #opens portscandata.txt and writes into cvenumbers.txt
                print ("VulnScanner running")
            except:
                print("Anthony Can't Code")

            try: 
                CVEdescriptionAndSolutionsGetter.getCveDescription()
                print ("CVE Descirption Works")
            except:
                print("Anthony Can't Code2")

            #creates frame 
            table_frame = Frame(frame)
            table_frame.place(relx =0.50, rely=0.20, relwidth= 0.85, relheight=0.75, anchor='n')

            #creates treeview table within the "table_frame"
            tree = ttk.Treeview(table_frame, selectmode="extended", columns=("IP Address", "Vulnerability" ,"Description")) 

            #treeview config
            style = ttk.Style(root)
            style.configure("Treeview", rowheight=80)
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
            tree.column("Description", minwidth=0, width=1000,stretch=NO)

            results = CVEdescriptionAndSolutionsGetter.getCveDescription()
            if len(results) == 0:
                entry_ip.delete(0, tk.END)
                entry_ip.insert(0, 'Error: No data dound for ' + ip_address + "!" )
            count = 0 
            for i in results:
                count +=1 

                description = results.get(i).get('description')
                
                #import textwarp for support 
                if len(description) >= 175:
                    description = textwrap.fill(description, 175)

                tree.insert("", 'end', text ="", values =(ip_address, i , description)) 

            



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
        directory_path = tk.StringVar()
        directory_field= tk.Entry(frame, font = "Calibri 15", textvariable=directory_path)
        directory_field.place(relx=0.50, rely=0.10, relwidth=0.40, relheight=0.065, anchor='n')
  

        scan_file_button = tk.Button(frame, text="Scan Directory", bg="#1e92eb", fg='white', command= lambda:press_block())
        scan_file_button.place(relx =0.85, rely=0.10, relwidth=0.10, relheight=0.065, anchor='n')

        quarantine_file_button = tk.Button(frame, text="Show Quarantined Files", bg="#1e92eb", fg='white', command= lambda:press_block())
        quarantine_file_button.place(relx =0.85, rely=0.2, relwidth=0.10, relheight=0.065, anchor='n')

        release_button = tk.Button(frame, text="Show Released Files", bg="#1e92eb", fg='white', command= lambda:press_remove())
        release_button.place(relx =.85, rely=0.3, relwidth=0.10, relheight=0.065, anchor='n')



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
