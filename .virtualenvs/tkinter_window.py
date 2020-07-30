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

root = tk.Tk() #creates the actual window

frame = Frame(root, background ="#03021a") #creates frame and makes it dark blue 
frame.pack(fill='both', expand=True)
frame.pack()

root.title("TKINTER > KIVY")

root.geometry("1200x800") #sets the size of the GUI box 
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

        content = tk.StringVar()
        entry_ip = tk.Entry(frame, textvariable=content)
        entry_ip.place(relx=0.50, rely=0.10, relwidth=0.40, relheight=0.08, anchor='n')
        
        scan_button = tk.Button(frame, text="Scan", bg="#1e92eb", fg='white', command= lambda:press_scan())
        scan_button.place(relx =0.85, rely=0.10, relwidth=0.10, relheight=0.07, anchor='n')

        def press_scan():
            ip_address = content.get()
            try:
                print(ip_address)

                # https://github.com/scipag/vulscan
                Vulscan.scan(ip_address)
                print("work")

            except:
                print("error")

            try: 
                CVEnumbersExtractor.vulnScanExtract()
                print ("VulnScanner running")
            except:
                print("Anthony Can't Code")

            try: 
                CVEdescriptionAndSolutionsGetter.getCveDescription()
                print ("CVE Descirption Works")
            except:
                print("Anthony Can't Code2")



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
        block_ip = tk.Entry(frame, textvariable=block_ip_content)
        block_ip.place(relx=0.50, rely=0.10, relwidth=0.40, relheight=0.08, anchor='n')
  

        block_button = tk.Button(frame, text="Block IP", bg="#1e92eb", fg='white', command= lambda:press_block())
        block_button.place(relx =0.85, rely=0.10, relwidth=0.10, relheight=0.07, anchor='n')

        unblock_ip_content = tk.StringVar()
        unblock_ip = tk.Entry(frame, textvariable=unblock_ip_content)
        unblock_ip.place(relx=0.50, rely=0.50, relwidth=0.40, relheight=0.08, anchor='n')
        
        unblock_button = tk.Button(frame, text="UnBlock IP", bg="#1e92eb", fg='white', command= lambda:press_remove())
        unblock_button.place(relx =0.85, rely=0.50, relwidth=0.10, relheight=0.07, anchor='n')

        def press_block():
            ip_address = block_ip_content.get()

            try:
                print(ip_address)
                # https://github.com/scipag/vulscan
                windows_7.add_rule("Blocked IP From Console", ip_address)
                print("success")
            except:
                print("YOu FAIL")

        def press_remove():
            ip_address = unblock_ip_content.get()

            try:
                print(ip_address)
                # https://github.com/scipag/vulscan
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
