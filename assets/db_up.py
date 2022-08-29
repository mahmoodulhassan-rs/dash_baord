#!/bin/python3
import codecs
import re
import csv
from sqlite3 import TimestampFromTicks
from sre_constants import BRANCH
import sys
import glob
import pandas as pd
import numpy as np
import os 
import itertools
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import shutil
import pathlib
from itertools import islice
from collections import Counter
from dash import dcc
from dash import html
# from openpyl import *
# from openpyxl.styles import *
# from openpyxl.worksheet.dimensions import ColumnDimension, DimensionHolder
import matplotlib.pyplot as plt
from pathlib import Path
import time
import ntpath
import dash, dash_table
from dash.dependencies import Input, Output
#############################################################################
##############################################################################
def get_test_name (log_file):
    global row_no
    global test_name
    test_name= (log_file.split("/")[-1]).replace(".log","")
    # test_name=ntpath.basename(path)
    # print(test_name)
    if test_name in test_collection.keys():
        
        row_no = test_collection [test_name]
    else:
        row_no = row_no + 1
        test_collection[test_name] = row_no
        # print("xxxxxxxxxxxxxxxxxxxxxx",test_collection)
   # print("Test_Name is",test_name)
    return [test_name,row_no]

def I2C (planned_tests,test_passed,test_failed):
    global i2c_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_I2C +"/*.log"
    # get_design_row = i2c_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate I2C log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        df.loc[test_name[1],"Hierarchy"]= "SoC"
        df.loc[test_name[1],["IP"]]="I2C"
        with open (log_file,'r') as read:
           lines = read.readlines()
           for line in lines:
                   if  (re.search (r"UVM_FATAL \[",line)) or (re.search(r"UVM_FATAL @ 0:",line)) or (re.search (r"UVM_ERROR \[",line))  :
                       temp=line
                   elif  re.search(r"TEST PASSED",line):
                       df.loc[test_name[1],"Status"]="Passed"
                       test_passed=test_passed+1
                       break
                   elif (re.search(r"TEST FAILED",line)) or (re.search(r"\b^UVM_ERROR :    [1-9]*$\b",line)) or (re.search(r"\b^UVM_FATAL :    1\b",line)) :
                    #    print(line)
                       df.loc[test_name[1],"Status"]="Failed"
                       df.loc[test_name[1],"Remarks"]=temp
                       test_failed=test_failed+1
                       break
    planned_tests=pld_tests+planned_tests
    # print("Test_planned:",planned_tests)
    return planned_tests,test_passed,test_failed
    # df["IP"]="I2C"    
    # test_collection
def UART0 (planned_tests,test_passed,test_failed):
    # global i2c_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_UART0+"/*.log"
    # get_design_row = i2c_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate UART0 log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        df.loc[test_name[1],"Hierarchy"]= "SoC"
        df.loc[test_name[1],["IP"]]="UART0"
        with open (log_file,'r') as read:
           lines = read.readlines()
           for line in lines:
                   if  (re.search (r"UVM_FATAL \[",line)) or (re.search(r"UVM_FATAL @ 0:",line)) or (re.search (r"UVM_ERROR \[",line))  :
                       temp=line
                   elif  re.search(r"TEST PASSED",line):
                       df.loc[test_name[1],"Status"]="Passed"
                       test_passed=test_passed+1
                       break
                   elif (re.search(r"TEST FAILED",line)) or (re.search(r"\b^UVM_ERROR :    [1-9]*$\b",line)) or (re.search(r"\b^UVM_FATAL :    1\b",line)) :
                    #    print(line)
                       df.loc[test_name[1],"Status"]="Failed"
                       df.loc[test_name[1],"Remarks"]=temp
                       test_failed=test_failed+1
                       break
    planned_tests=pld_tests+planned_tests
    # print("Test_planned:",planned_tests)
    return planned_tests,test_passed,test_failed

def UART1 (planned_tests,test_passed,test_failed):
    # global i2c_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_UART1+"/*.log"
    # get_design_row = i2c_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate UART1 log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        df.loc[test_name[1],"Hierarchy"]= "SoC"
        df.loc[test_name[1],["IP"]]="UART1"
        with open (log_file,'r') as read:
           lines = read.readlines()
           for line in lines:
                   if  (re.search (r"UVM_FATAL \[",line)) or (re.search(r"UVM_FATAL @ 0:",line)) or (re.search (r"UVM_ERROR \[",line))  :
                       temp=line
                   elif  re.search(r"TEST PASSED",line):
                       df.loc[test_name[1],"Status"]="Passed"
                       test_passed=test_passed+1
                       break
                   elif (re.search(r"TEST FAILED",line)) or (re.search(r"\b^UVM_ERROR :    [1-9]*$\b",line)) or (re.search(r"\b^UVM_FATAL :    1\b",line)) :
                    #    print(line)
                       df.loc[test_name[1],"Status"]="Failed"
                       df.loc[test_name[1],"Remarks"]=temp
                       test_failed=test_failed+1
                       break
    planned_tests=pld_tests+planned_tests
    # print("Test_planned:",planned_tests)
    return planned_tests,test_passed,test_failed

def BOOT (planned_tests,test_passed,test_failed):
    # global i2c_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_BOOT+"/*.log"
    # get_design_row = i2c_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate BOOT log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        df.loc[test_name[1],"Hierarchy"]= "SoC"
        df.loc[test_name[1],["IP"]]="BOOT"
        with open (log_file,'r') as read:
           lines = read.readlines()
           for line in lines:
                   if  (re.search (r"UVM_FATAL \[",line)) or (re.search(r"UVM_FATAL @ 0:",line)) or (re.search (r"UVM_ERROR \[",line))  :
                       temp=line
                   elif  re.search(r"TEST PASSED",line):
                       df.loc[test_name[1],"Status"]="Passed"
                       test_passed=test_passed+1
                       break
                   elif (re.search(r"TEST FAILED",line)) or (re.search(r"\b^UVM_ERROR :    [1-9]*$\b",line)) or (re.search(r"\b^UVM_FATAL :    1\b",line)) :
                    #    print(line)
                       df.loc[test_name[1],"Status"]="Failed"
                       df.loc[test_name[1],"Remarks"]=temp
                       test_failed=test_failed+1
                       break
    planned_tests=pld_tests+planned_tests
    # print("Test_planned:",planned_tests)
    return planned_tests,test_passed,test_failed

def DMA (planned_tests,test_passed,test_failed):
    # global i2c_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_DMA+"/*.log"
    # get_design_row = i2c_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate DMA log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        df.loc[test_name[1],"Hierarchy"]= "SoC"
        df.loc[test_name[1],["IP"]]="DMA"
        with open (log_file,'r') as read:
           lines = read.readlines()
           for line in lines:
                   if  (re.search (r"UVM_FATAL \[",line)) or (re.search(r"UVM_FATAL @ 0:",line)) or (re.search (r"UVM_ERROR \[",line))  :
                       temp=line
                   elif  re.search(r"TEST PASSED",line):
                       df.loc[test_name[1],"Status"]="Passed"
                       test_passed=test_passed+1
                       break
                   elif (re.search(r"TEST FAILED",line)) or (re.search(r"\b^UVM_ERROR :    [1-9]*$\b",line)) or (re.search(r"\b^UVM_FATAL :    1\b",line)) :
                    #    print(line)
                       df.loc[test_name[1],"Status"]="Failed"
                       df.loc[test_name[1],"Remarks"]=temp
                       test_failed=test_failed+1
                       break
    planned_tests=pld_tests+planned_tests
    # print("Test_planned:",planned_tests)
    return planned_tests,test_passed,test_failed
def GPIO (planned_tests,test_passed,test_failed):
    # global i2c_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_GPIO+"/*.log"
    # get_design_row = i2c_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate GPIO log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        df.loc[test_name[1],"Hierarchy"]= "SoC"
        df.loc[test_name[1],["IP"]]="GPIO"
        with open (log_file,'r') as read:
           lines = read.readlines()
           for line in lines:
                   if  (re.search (r"UVM_FATAL \[",line)) or (re.search(r"UVM_FATAL @ 0:",line)) or (re.search (r"UVM_ERROR \[",line))  :
                       temp=line
                   elif  re.search(r"TEST PASSED",line):
                       df.loc[test_name[1],"Status"]="Passed"
                       test_passed=test_passed+1
                       break
                   elif (re.search(r"TEST FAILED",line)) or (re.search(r"\b^UVM_ERROR :    [1-9]*$\b",line)) or (re.search(r"\b^UVM_FATAL :    1\b",line)) :
                    #    print(line)
                       df.loc[test_name[1],"Status"]="Failed"
                       df.loc[test_name[1],"Remarks"]=temp
                       test_failed=test_failed+1
                       break
    planned_tests=pld_tests+planned_tests
    # print("Test_planned:",planned_tests)
    return planned_tests,test_passed,test_failed
def GPT (planned_tests,test_passed,test_failed):
    # global i2c_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_GPT+"/*.log"
    # get_design_row = i2c_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate GPT log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        df.loc[test_name[1],"Hierarchy"]= "SoC"
        df.loc[test_name[1],["IP"]]="GPT"
        with open (log_file,'r') as read:
           lines = read.readlines()
           for line in lines:
                   if  (re.search (r"UVM_FATAL \[",line)) or (re.search(r"UVM_FATAL @ 0:",line)) or (re.search (r"UVM_ERROR \[",line))  :
                       temp=line
                   elif  re.search(r"TEST PASSED",line):
                       df.loc[test_name[1],"Status"]="Passed"
                       test_passed=test_passed+1
                       break
                   elif (re.search(r"TEST FAILED",line)) or (re.search(r"\b^UVM_ERROR :    [1-9]*$\b",line)) or (re.search(r"\b^UVM_FATAL :    1\b",line)) :
                    #    print(line)
                       df.loc[test_name[1],"Status"]="Failed"
                       df.loc[test_name[1],"Remarks"]=temp
                       test_failed=test_failed+1
                       break
    planned_tests=pld_tests+planned_tests
    # print("Test_planned:",planned_tests)
    return planned_tests,test_passed,test_failed
def SPI (planned_tests,test_passed,test_failed):
    # global i2c_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_SPI+"/*.log"
    # get_design_row = i2c_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate SPI log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        df.loc[test_name[1],"Hierarchy"]= "SoC"
        df.loc[test_name[1],["IP"]]="SPI"
        with open (log_file,'r') as read:
           lines = read.readlines()
           for line in lines:
                   if  (re.search (r"UVM_FATAL \[",line)) or (re.search(r"UVM_FATAL @ 0:",line)) or (re.search (r"UVM_ERROR \[",line))  :
                       temp=line
                   elif  re.search(r"TEST PASSED",line):
                       df.loc[test_name[1],"Status"]="Passed"
                       test_passed=test_passed+1
                       break
                   elif (re.search(r"TEST FAILED",line)) or (re.search(r"\b^UVM_ERROR :    [1-9]*$\b",line)) or (re.search(r"\b^UVM_FATAL :    1\b",line)) :
                    #    print(line)
                       df.loc[test_name[1],"Status"]="Failed"
                       df.loc[test_name[1],"Remarks"]=temp
                       test_failed=test_failed+1
                       break
    planned_tests=pld_tests+planned_tests
    # print("Test_planned:",planned_tests)
    return planned_tests,test_passed,test_failed

def SRAM (planned_tests,test_passed,test_failed):
    # global i2c_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_SRAM+"/*.log"
    # get_design_row = i2c_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate SRAM log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        
        # print("*************dasd************",planned_tests)
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        df.loc[test_name[1],"Hierarchy"]= "SoC"
        df.loc[test_name[1],["IP"]]="SRAM"
        with open (log_file,'r') as read:
           lines = read.readlines()
           for line in lines:
                   if  (re.search (r"UVM_FATAL \[",line)) or (re.search(r"UVM_FATAL @ 0:",line)) or (re.search (r"UVM_ERROR \[",line))  :
                       temp=line
                   elif  re.search(r"TEST PASSED",line):
                       df.loc[test_name[1],"Status"]="Passed"
                       test_passed=test_passed+1
                       break
                   elif (re.search(r"TEST FAILED",line)) or (re.search(r"\b^UVM_ERROR :    [1-9]*$\b",line)) or (re.search(r"\b^UVM_FATAL :    1\b",line)) :
                    #    print(line)
                       df.loc[test_name[1],"Status"]="Failed"
                       df.loc[test_name[1],"Remarks"]=temp
                       test_failed=test_failed+1
                       break
    planned_tests=pld_tests+planned_tests
    print("Test_planned:",planned_tests)
    return planned_tests,test_passed,test_failed
def WDT (planned_tests,test_passed,test_failed):
    # global i2c_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_WDT+"/*.log"
    # get_design_row = i2c_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate WDT log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        df.loc[test_name[1],"Hierarchy"]= "SoC"
        df.loc[test_name[1],["IP"]]="WDT"
        with open (log_file,'r') as read:
           lines = read.readlines()
           for line in lines:
                   if  (re.search (r"UVM_FATAL \[",line)) or (re.search(r"UVM_FATAL @ 0:",line)) or (re.search (r"UVM_ERROR \[",line))  :
                       temp=line
                   elif  re.search(r"TEST PASSED",line):
                       df.loc[test_name[1],"Status"]="Passed"
                       test_passed=test_passed+1
                       break
                   elif (re.search(r"TEST FAILED",line)) or (re.search(r"\b^UVM_ERROR :    [1-9]*$\b",line)) or (re.search(r"\b^UVM_FATAL :    1\b",line)) :
                    #    print(line)
                       df.loc[test_name[1],"Status"]="Failed"
                       df.loc[test_name[1],"Remarks"]=temp
                       test_failed=test_failed+1
                       break
    planned_tests=pld_tests+planned_tests
    print("Test_planned:",planned_tests)
    return planned_tests,test_passed,test_failed

#def CLK (planned_tests,test_passed,test_failed):
    # global i2c_ip
#    temp='NaN'
#    log_no=0
#    log_count=0
#    log_files= ip_CLK+"/*.log"
    # get_design_row = i2c_ip   
    # print (get_design_row)
##    log_files_glb = glob.glob(log_files)
#    if log_files_glb:
        #  print (log_files_glb)
#         pass
#    else:
#         print("Error: glob failed to locate CLK log files")
#    log_count=len(log_files_glb)
#   for log_file in log_files_glb:
#        # print(count)
#        log_no=log_no+1
#       pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
#        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
 #       test_name=get_test_name (log_file)
#        df.loc[test_name[1],"Test_Name"]= test_name[0]
# df.loc[test_name[1],"Hierarchy"]= "SoC"
#        df.loc[test_name[1],["IP"]]="CLK"
#        with open (log_file,'r') as read:
#           lines = read.readlines()
#           for line in lines:
#                   if  (re.search (r"UVM_FATAL \[",line)) or (re.search(r"UVM_FATAL @ 0:",line)) or (re.search (r"UVM_ERROR \[",line))  :
#                       temp=line
#                   elif  re.search(r"TEST PASSED",line):
#                       df.loc[test_name[1],"Status"]="Passed"
#                       test_passed=test_passed+1
#                       break
#                   elif (re.search(r"TEST FAILED",line)) or (re.search(r"\b^UVM_ERROR :    [1-9]*$\b",line)) or (re.search(r"\b^UVM_FATAL :    1\b",line)) :
#                    #    print(line)
#                       df.loc[test_name[1],"Status"]="Failed"
#                       df.loc[test_name[1],"Remarks"]=temp
#                       test_failed=test_failed+1
#                       break
#    planned_tests=pld_tests+planned_tests
#    print("Test_planned:",planned_tests)
#    return planned_tests,test_passed,test_failed

#def GATING (planned_tests,test_passed,test_failed):
#    # global i2c_ip
#    temp='NaN'
#    log_no=0
#    log_count=0
#    log_files= ip_GATING+"/*.log"
#    # get_design_row = i2c_ip   
#    # print (get_design_row)
#    log_files_glb = glob.glob(log_files)
#    if log_files_glb:
#        #  print (log_files_glb)
#         pass
#    else:
#         print("Error: glob failed to locate GATING log files")
#    log_count=len(log_files_glb)
#    for log_file in log_files_glb:
#        # print(count)
#        log_no=log_no+1
#        pld_tests=log_no
#        # planned_tests=pld_tests+planned_tests
#        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
#        test_name=get_test_name (log_file)
#        df.loc[test_name[1],"Test_Name"]= test_name[0]
# df.loc[test_name[1],"Hierarchy"]= "SoC"
#        df.loc[test_name[1],["IP"]]="GATING"
#        with open (log_file,'r') as read:
#           lines = read.readlines()
#           for line in lines:
#                   if  (re.search (r"UVM_FATAL \[",line)) or (re.search(r"UVM_FATAL @ 0:",line)) or (re.search (r"UVM_ERROR \[",line))  :
#                       temp=line
#                   elif  re.search(r"TEST PASSED",line):
#                       df.loc[test_name[1],"Status"]="Passed"
#                       test_passed=test_passed+1
#                       break
#                   elif (re.search(r"TEST FAILED",line)) or (re.search(r"\b^UVM_ERROR :    [1-9]*$\b",line)) or (re.search(r"\b^UVM_FATAL :    1\b",line)) :
#                    #    print(line)
#                       df.loc[test_name[1],"Status"]="Failed"
#                       df.loc[test_name[1],"Remarks"]=temp
#                       test_failed=test_failed+1
#                       break
#    planned_tests=pld_tests+planned_tests
#    print("Test_planned:",planned_tests)
#    return planned_tests,test_passed,test_failed
#
def SCU (planned_tests,test_passed,test_failed):
    # global i2c_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_SCU+"/*.log"
    # get_design_row = i2c_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate SCU log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        df.loc[test_name[1],"Hierarchy"]= "SoC"
        df.loc[test_name[1],["IP"]]="SCU"
        with open (log_file,'r') as read:
           lines = read.readlines()
           for line in lines:
                   if  (re.search (r"UVM_FATAL \[",line)) or (re.search(r"UVM_FATAL @ 0:",line)) or (re.search (r"UVM_ERROR \[",line))  :
                       temp=line
                   elif  re.search(r"TEST PASSED",line):
                       df.loc[test_name[1],"Status"]="Passed"
                       test_passed=test_passed+1
                       break
                   elif (re.search(r"TEST FAILED",line)) or (re.search(r"\b^UVM_ERROR :    [1-9]*$\b",line)) or (re.search(r"\b^UVM_FATAL :    1\b",line)) :
                    #    print(line)
                       df.loc[test_name[1],"Status"]="Failed"
                       df.loc[test_name[1],"Remarks"]=temp
                       test_failed=test_failed+1
                       break
    planned_tests=pld_tests+planned_tests
    print("Test_planned:",planned_tests)
    return planned_tests,test_passed,test_failed

def DDR3 (planned_tests,test_passed,test_failed):
    # global i2c_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_DDR3+"/*.log"
    # get_design_row = i2c_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Skipping DDR3")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        df.loc[test_name[1],"Hierarchy"]= "SoC"
        df.loc[test_name[1],["IP"]]="DDR3"
        with open (log_file,'r') as read:
           lines = read.readlines()
           for line in lines:
                   if  (re.search (r"UVM_FATAL \[",line)) or (re.search(r"UVM_FATAL @ 0:",line)) or (re.search (r"UVM_ERROR \[",line))  :
                       temp=line
                   elif  re.search(r"TEST PASSED",line):
                       df.loc[test_name[1],"Status"]="Passed"
                       test_passed=test_passed+1
                       break
                   elif (re.search(r"TEST FAILED",line)) or (re.search(r"\b^UVM_ERROR :    [1-9]*$\b",line)) or (re.search(r"\b^UVM_FATAL :    1\b",line)) :
                    #    print(line)
                       df.loc[test_name[1],"Status"]="Failed"
                       df.loc[test_name[1],"Remarks"]=temp
                       test_failed=test_failed+1
                       break
    planned_tests=pld_tests+planned_tests
    print("Test_planned:",planned_tests)
    return planned_tests,test_passed,test_failed
# 
def FCB (planned_tests,test_passed,test_failed):
    # global i2c_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_FCB+"/*.log"
    # get_design_row = i2c_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate FCB log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        df.loc[test_name[1],"Hierarchy"]= "SoC"
        df.loc[test_name[1],["IP"]]="FCB"
        with open (log_file,'r') as read:
           lines = read.readlines()
           for line in lines:
                   if  (re.search (r"UVM_FATAL \[",line)) or (re.search(r"UVM_FATAL @ 0:",line)) or (re.search (r"UVM_ERROR \[",line))  :
                       temp=line
                   elif  re.search(r"TEST PASSED",line):
                       df.loc[test_name[1],"Status"]="Passed"
                       test_passed=test_passed+1
                       break
                   elif (re.search(r"TEST FAILED",line)) or (re.search(r"\b^UVM_ERROR :    [1-9]*$\b",line)) or (re.search(r"\b^UVM_FATAL :    1\b",line)) :
                    #    print(line)
                       df.loc[test_name[1],"Status"]="Failed"
                       df.loc[test_name[1],"Remarks"]=temp
                       test_failed=test_failed+1
                       break
    planned_tests=pld_tests+planned_tests
    print("Test_planned:",planned_tests)
    return planned_tests,test_passed,test_failed

def PCB (planned_tests,test_passed,test_failed):
    # global i2c_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_PCB+"/*.log"
    # get_design_row = i2c_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate PCB log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        df.loc[test_name[1],"Hierarchy"]= "SoC"
        df.loc[test_name[1],["IP"]]="PCB"
        with open (log_file,'r') as read:
           lines = read.readlines()
           for line in lines:
                   if  (re.search (r"UVM_FATAL \[",line)) or (re.search(r"UVM_FATAL @ 0:",line)) or (re.search (r"UVM_ERROR \[",line))  :
                       temp=line
                   elif  re.search(r"TEST PASSED",line):
                       df.loc[test_name[1],"Status"]="Passed"
                       test_passed=test_passed+1
                       break
                   elif (re.search(r"TEST FAILED",line)) or (re.search(r"\b^UVM_ERROR :    [1-9]*$\b",line)) or (re.search(r"\b^UVM_FATAL :    1\b",line)) :
                    #    print(line)
                       df.loc[test_name[1],"Status"]="Failed"
                       df.loc[test_name[1],"Remarks"]=temp
                       test_failed=test_failed+1
                       break
    planned_tests=pld_tests+planned_tests
    print("Test_planned:",planned_tests)
    return planned_tests,test_passed,test_failed

def USB (planned_tests,test_passed,test_failed):
    # global i2c_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_USB+"/*.log"
    # get_design_row = i2c_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate USB log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        df.loc[test_name[1],"Hierarchy"]= "SoC"
        df.loc[test_name[1],["IP"]]="USB"
        with open (log_file,'r') as read:
           lines = read.readlines()
           for line in lines:
                   if  (re.search (r"UVM_FATAL \[",line)) or (re.search(r"UVM_FATAL @ 0:",line)) or (re.search (r"UVM_ERROR \[",line))  :
                       temp=line
                   elif  re.search(r"TEST PASSED",line):
                       df.loc[test_name[1],"Status"]="Passed"
                       test_passed=test_passed+1
                       break
                   elif (re.search(r"TEST FAILED",line)) or (re.search(r"\b^UVM_ERROR :    [1-9]*$\b",line)) or (re.search(r"\b^UVM_FATAL :    1\b",line)) :
                    #    print(line)
                       df.loc[test_name[1],"Status"]="Failed"
                       df.loc[test_name[1],"Remarks"]=temp
                       test_failed=test_failed+1
                       break
    planned_tests=pld_tests+planned_tests
    print("Test_planned:",planned_tests)
    return planned_tests,test_passed,test_failed
#
def GBE (planned_tests,test_passed,test_failed):
    # global i2c_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_GBE+"/*.log"
    # get_design_row = i2c_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate GBE log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        df.loc[test_name[1],"Hierarchy"]= "SoC"
        df.loc[test_name[1],["IP"]]="GBE"
        with open (log_file,'r') as read:
           lines = read.readlines()
           for line in lines:
                   if  (re.search (r"UVM_FATAL \[",line)) or (re.search(r"UVM_FATAL @ 0:",line)) or (re.search (r"UVM_ERROR \[",line))  :
                       temp=line
                   elif  re.search(r"TEST PASSED",line):
                       df.loc[test_name[1],"Status"]="Passed"
                       test_passed=test_passed+1
                       break
                   elif (re.search(r"TEST FAILED",line)) or (re.search(r"\b^UVM_ERROR :    [1-9]*$\b",line)) or (re.search(r"\b^UVM_FATAL :    1\b",line)) :
                    #    print(line)
                       df.loc[test_name[1],"Status"]="Failed"
                       df.loc[test_name[1],"Remarks"]=temp
                       test_failed=test_failed+1
                       break
    planned_tests=pld_tests+planned_tests
    print("Test_planned:",planned_tests)
    return planned_tests,test_passed,test_failed

def get_time():
#  TIME=0
 log_files= ip_UART0 +"/acpu_bfm_uart0_test.log"
 log_files_glb = glob.glob(log_files)
#  print("Log file is",log_files_glb)
 for log_file in log_files_glb:
    with open (log_file,'r') as read:
        lines = read.readlines()
        # print(lines)
        for line in lines:
                   if  (re.search (r"Compiler version",line)):
                       line=line.split(";")
                       line[-1] = line[-1].strip()
                    #    print("For Time Get",line[-1])
                       Time=line[-1]
                       break
 print(Time)
 return Time
 
def fina_csv (time):
    run_file = run_location+"/run.txt"
    with open (run_file,'r') as read:
           lines = read.readlines()
           for line in lines:
                line= line.split()
                line[-1]=line[-1].strip()
                print("Line is ...",line)
                line=int(line[-1])+1
                print("Updated Line ...",line)
           with open (run_file,'w') as write:
                write.write(str(line))
    sram_df_states = pd.read_csv('sram_css_states.csv')
    fcb_df_states = pd.read_csv('fcb_css_states.csv')
    # print(sram_df_states)
    # print(fcb_df_states)
    frames = [df, sram_df_states, fcb_df_states]
    result = pd.concat(frames)
    result['Run'] = [line] * len(result)
    result = result.explode('Run')
    result['Date'] = [time] * len(result)
    result = result.explode('Date')
    # print (result)
    filename_path= csv_location+"final.csv"
    result.to_csv(filename_path, encoding="utf-8-sig",index=True)                     

def df_to_csv (df,filename):
     filename_path= csv_location+filename
     df.to_csv(filename_path, encoding="utf-8-sig",index=False)
                    
    # df["IP"]="UART"  
global no_of_col
global design_collction
global test_collection
planned_tests = 0
test_passed = 0
test_failed = 0

df = pd.DataFrame()
# print(df)
df_grp_dash=pd.DataFrame()

row_no = len(df.index)
# design_collction = {"IP":row_no}
test_collection = {"Test":row_no}
#print(design_collction)
filename_css = 'css_states.csv'
filename_dash = 'css_states_dash.csv'
filename_time = 'time.csv'
filename_pie = 'pie_states_dash.csv'
#print (filename)
location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
df_grp_dash=pd.DataFrame(df,columns=["Category","Numbers"])
df_grp=pd.DataFrame(df,columns=["Category","Numbers"])
df=pd.DataFrame(df,columns=["IP","Test_Name","Status","Remarks"])
# df_time=pd.DataFrame(df,columns=["Regression_Run_Time"])
# df_time_n=pd.DataFrame(df,columns=["Regression_Run_Dat"])
# print (location)
###Paths####
logs_location = location+"/../results"
csv_location = location+"/../results/"
run_location = location+"/../../../../docs"
###IPs Log Files
ip_BOOT= logs_location +"/BOOT"
ip_DMA= logs_location +"/DMA"
ip_GPIO= logs_location +"/GPIO"
ip_GPT= logs_location +"/GPT"
ip_I2C= logs_location +"/I2C"
ip_SPI= logs_location +"/SPI"
ip_SRAM= logs_location +"/SRAM"
ip_UART0= logs_location +"/UART0"
ip_UART1= logs_location +"/UART1"
ip_WDT= logs_location +"/WDT"
#ip_CLK= logs_location +"/CLK"
ip_SCU= logs_location +"/SCU"
ip_FCB= logs_location +"/FCB"
ip_PCB= logs_location +"/PCB"
ip_DDR3= logs_location +"/DDR3"
ip_USB= logs_location +"/USB"
ip_GBE= logs_location +"/GBE"




# print (ip_I2C)
# get_ip_name(ip_I2C)
tests_plnd,tests_p,tests_f=I2C(planned_tests,test_passed,test_failed)
row_no = len(df.index)
design_collction = {"Test":row_no}
tests_plnd,tests_p,tests_f=UART0(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=UART1(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=BOOT(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=DMA(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=GPIO(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=GPT(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=SPI(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=SRAM(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=WDT(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

#tests_plnd,tests_p,tests_f=CLK(tests_plnd,tests_p,tests_f)
#row_no = len(df.index)

#tests_plnd,tests_p,tests_f=GATING(tests_plnd,tests_p,tests_f)
#row_no = len(df.index)
#design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=SCU(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

#tests_plnd,tests_p,tests_f=DDR3(tests_plnd,tests_p,tests_f)
#row_no = len(df.index)
#design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=FCB(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=PCB(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

# tests_plnd,tests_p,tests_f=USB(tests_plnd,tests_p,tests_f)
# row_no = len(df.index)
# design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=GBE(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

design_collction = {"Test":row_no}
print("Total tests planned",tests_plnd)
print("Total tests passed",tests_p)
print("Total tests failed",tests_f)



df_grp_dash.loc["0","Category"]="Tests Under Development"
df_grp_dash.loc["1","Category"]="Tests Passed"
df_grp_dash.loc["2","Category"]="Tests Failed"

df_grp_dash.loc["0","Numbers"]= 158-tests_p-tests_f
df_grp_dash.loc["1","Numbers"]= tests_p
df_grp_dash.loc["2","Numbers"]= tests_f

# df_grp.loc["0"]="Serial No"
df_grp.loc["0","Category"]="Tests Planned"
df_grp.loc["1","Category"]="Tests Passed"
df_grp.loc["2","Category"]="Tests Failed"
df_grp.loc["0","Numbers"]= "158"
df_grp.loc["1","Numbers"]= tests_p
df_grp.loc["2","Numbers"]= tests_f
# df_grp_dash = df_grp_dash.loc.astype(str).replace('\.\d+', '', regex=True).astype(int)

# df_to_csv (df)
# print(df_grp_dash)
# print(df)
# df['Date'] = ["21 August"] * len(df)
# df = df.explode('Date')

time= get_time()
fina_csv (time)

# df['Date'] = [time] * len(df)
# df = df.explode('Date')
# filename_path= csv_location+"final.csv"
# result.to_csv(filename_path, encoding="utf-8-sig",index=False) 

df_to_csv (df,filename_css)
df_to_csv (df_grp,filename_dash)
df_to_csv (df_grp_dash,filename_pie)
# df_to_csv (df_time,filename_time)
# print(df_grp)
# print(df)
# print(df_grp_dash)
# print(df_time)
# print(df_time_n)
