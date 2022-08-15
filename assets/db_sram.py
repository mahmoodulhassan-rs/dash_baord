#!/bin/python3
import codecs
import re
import csv
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
# ###############################################################################
# def get_time():
#  log_files= ip_test_all_one_write_read +"/test_all_one_write_read.log"
#  log_files_glb = glob.glob(log_files)
# #  print("Log file is",log_files_glb)
#  for log_file in log_files_glb:
#     with open (log_file,'r') as read:
#         lines = read.readlines()
#         # print(lines)
#         for line in lines:
#                    if  (re.search (r"Compiler version",line)):
#                        line=line.split(";")
#                        line[-1] = line[-1].strip()
#                     #    print("For Time Get",line[-1])
#                        df_time.loc["0","Regression_Run_Time"]=line[-1]
    
###############################################################################
def axi_master_base_test (planned_tests,test_passed,test_failed):
    global axi_master_base_test_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_axi_master_base_test +"/*.log"
    # get_design_row = axi_master_base_test_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate axi_master_base_test log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        #df.loc[test_name[1],["IP"]]="axi_master_base_test"
        with open (log_file,'r') as read:
           lines = read.readlines()
           for line in lines:
                   if  (re.search (r"UVM_FATAL ..",line)) or (re.search (r"UVM_ERROR ..",line))  :
                       temp=line
                   elif  re.search(r"TEST PASS",line):
                       df.loc[test_name[1],"Status"]="Passed"
                       test_passed=test_passed+1
                       break
                   elif (re.search(r"TEST FAIL",line)) or (re.search(r"\b^UVM_ERROR :    [1-9]*$\b",line)) or (re.search(r"\b^UVM_FATAL :    1\b",line)) :
                    #    print(line)
                       df.loc[test_name[1],"Status"]="Failed"
                       df.loc[test_name[1],"Remarks"]=temp
                       test_failed=test_failed+1
                       break
    planned_tests=pld_tests+planned_tests
    # print("Test_planned:",planned_tests)
    return planned_tests,test_passed,test_failed
    # df["IP"]="axi_master_base_test"    
    # test_collection
def test_all_one_write_read (planned_tests,test_passed,test_failed):
    # global axi_master_base_test_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_test_all_one_write_read+"/*.log"
    # get_design_row = axi_master_base_test_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate test_all_one_write_read log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        #df.loc[test_name[1],["IP"]]="test_all_one_write_read"
        with open (log_file,'r') as read:
           lines = read.readlines()
           for line in lines:
                   if  (re.search (r"UVM_FATAL ..",line)) or (re.search (r"UVM_ERROR ..",line))  :
                       temp=line
                   elif  re.search(r"TEST PASS",line):
                       df.loc[test_name[1],"Status"]="Passed"
                       test_passed=test_passed+1
                       break
                   elif (re.search(r"TEST FAIL",line)) or (re.search(r"\b^UVM_ERROR :    [1-9]*$\b",line)) or (re.search(r"\b^UVM_FATAL :    1\b",line)) :
                    #    print(line)
                       df.loc[test_name[1],"Status"]="Failed"
                       df.loc[test_name[1],"Remarks"]=temp
                       test_failed=test_failed+1
                       break
    planned_tests=pld_tests+planned_tests
    # print("Test_planned:",planned_tests)
    return planned_tests,test_passed,test_failed

def test_all_zero_write_read (planned_tests,test_passed,test_failed):
    # global axi_master_base_test_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_test_all_zero_write_read+"/*.log"
    # get_design_row = axi_master_base_test_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate test_all_zero_write_read log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        #df.loc[test_name[1],["IP"]]="test_all_zero_write_read"
        with open (log_file,'r') as read:
           lines = read.readlines()
           for line in lines:
                   if  (re.search (r"UVM_FATAL ..",line)) or (re.search (r"UVM_ERROR ..",line))  :
                       temp=line
                   elif  re.search(r"TEST PASS",line):
                       df.loc[test_name[1],"Status"]="Passed"
                       test_passed=test_passed+1
                       break
                   elif (re.search(r"TEST FAIL",line)) or (re.search(r"\b^UVM_ERROR :    [1-9]*$\b",line)) or (re.search(r"\b^UVM_FATAL :    1\b",line)) :
                    #    print(line)
                       df.loc[test_name[1],"Status"]="Failed"
                       df.loc[test_name[1],"Remarks"]=temp
                       test_failed=test_failed+1
                       break
    planned_tests=pld_tests+planned_tests
    # print("Test_planned:",planned_tests)
    return planned_tests,test_passed,test_failed

def test_axi_boundary_write_read (planned_tests,test_passed,test_failed):
    # global axi_master_base_test_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_test_axi_boundary_write_read+"/*.log"
    # get_design_row = axi_master_base_test_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate test_axi_boundary_write_read log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        #df.loc[test_name[1],["IP"]]="test_axi_boundary_write_read"
        with open (log_file,'r') as read:
           lines = read.readlines()
           for line in lines:
                   if  (re.search (r"UVM_FATAL ..",line)) or (re.search (r"UVM_ERROR ..",line))  :
                       temp=line
                   elif  re.search(r"TEST PASS",line):
                       df.loc[test_name[1],"Status"]="Passed"
                       test_passed=test_passed+1
                       break
                   elif (re.search(r"TEST FAIL",line)) or (re.search(r"\b^UVM_ERROR :    [1-9]*$\b",line)) or (re.search(r"\b^UVM_FATAL :    1\b",line)) :
                    #    print(line)
                       df.loc[test_name[1],"Status"]="Failed"
                       df.loc[test_name[1],"Remarks"]=temp
                       test_failed=test_failed+1
                       break
    planned_tests=pld_tests+planned_tests
    # print("Test_planned:",planned_tests)
    return planned_tests,test_passed,test_failed

def test_axi_burst_sizes (planned_tests,test_passed,test_failed):
    # global axi_master_base_test_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_test_axi_burst_sizes+"/*.log"
    # get_design_row = axi_master_base_test_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate test_axi_burst_sizes log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        #df.loc[test_name[1],["IP"]]="test_axi_burst_sizes"
        with open (log_file,'r') as read:
           lines = read.readlines()
           for line in lines:
                   if  (re.search (r"UVM_FATAL ..",line)) or (re.search (r"UVM_ERROR ..",line))  :
                       temp=line
                   elif  re.search(r"TEST PASS",line):
                       df.loc[test_name[1],"Status"]="Passed"
                       test_passed=test_passed+1
                       break
                   elif (re.search(r"TEST FAIL",line)) :
                    #    print(line)
                       df.loc[test_name[1],"Status"]="Failed"
                       df.loc[test_name[1],"Remarks"]=temp
                       test_failed=test_failed+1
                       break
    planned_tests=pld_tests+planned_tests
    # print("Test_planned:",planned_tests)
    return planned_tests,test_passed,test_failed
def test_axi_consecutive_IDs (planned_tests,test_passed,test_failed):
    # global axi_master_base_test_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_test_axi_consecutive_IDs+"/*.log"
    # get_design_row = axi_master_base_test_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate test_axi_consecutive_IDs log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        #df.loc[test_name[1],["IP"]]="test_axi_consecutive_IDs"
        with open (log_file,'r') as read:
           lines = read.readlines()
           for line in lines:
                   if  (re.search (r"UVM_FATAL ..",line)) or (re.search (r"UVM_ERROR ..",line))  :
                       temp=line
                   elif  re.search(r"TEST PASS",line):
                       df.loc[test_name[1],"Status"]="Passed"
                       test_passed=test_passed+1
                       break
                   elif (re.search(r"TEST FAIL",line)) or (re.search(r"\b^UVM_ERROR :    [1-9]*$\b",line)) or (re.search(r"\b^UVM_FATAL :    1\b",line)) :
                    #    print(line)
                       df.loc[test_name[1],"Status"]="Failed"
                       df.loc[test_name[1],"Remarks"]=temp
                       test_failed=test_failed+1
                       break
    planned_tests=pld_tests+planned_tests
    # print("Test_planned:",planned_tests)
    return planned_tests,test_passed,test_failed
def test_axi_fixed_burst_read (planned_tests,test_passed,test_failed):
    # global axi_master_base_test_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_test_axi_fixed_burst_read+"/*.log"
    # get_design_row = axi_master_base_test_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate test_axi_fixed_burst_read log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        #df.loc[test_name[1],["IP"]]="test_axi_fixed_burst_read"
        with open (log_file,'r') as read:
           lines = read.readlines()
           for line in lines:
                   if  (re.search (r"UVM_FATAL ..",line)) or (re.search (r"UVM_ERROR ..",line))  :
                       temp=line
                   elif  re.search(r"TEST PASS",line):
                       df.loc[test_name[1],"Status"]="Passed"
                       test_passed=test_passed+1
                       break
                   elif (re.search(r"TEST FAIL",line)) or (re.search(r"\b^UVM_ERROR :    [1-9]*$\b",line)) or (re.search(r"\b^UVM_FATAL :    1\b",line)) :
                    #    print(line)
                       df.loc[test_name[1],"Status"]="Failed"
                       df.loc[test_name[1],"Remarks"]=temp
                       test_failed=test_failed+1
                       break
    planned_tests=pld_tests+planned_tests
    # print("Test_planned:",planned_tests)
    return planned_tests,test_passed,test_failed
def test_axi_fixed_burst_same_address_read (planned_tests,test_passed,test_failed):
    # global axi_master_base_test_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_test_axi_fixed_burst_same_address_read+"/*.log"
    # get_design_row = axi_master_base_test_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate test_axi_fixed_burst_same_address_read log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        #df.loc[test_name[1],["IP"]]="test_axi_fixed_burst_same_address_read"
        with open (log_file,'r') as read:
           lines = read.readlines()
           for line in lines:
                   if  (re.search (r"UVM_FATAL ..",line)) or (re.search (r"UVM_ERROR ..",line))  :
                       temp=line
                   elif  re.search(r"TEST PASS",line):
                       df.loc[test_name[1],"Status"]="Passed"
                       test_passed=test_passed+1
                       break
                   elif (re.search(r"TEST FAIL",line)) or (re.search(r"\b^UVM_ERROR :    [1-9]*$\b",line)) or (re.search(r"\b^UVM_FATAL :    1\b",line)) :
                    #    print(line)
                       df.loc[test_name[1],"Status"]="Failed"
                       df.loc[test_name[1],"Remarks"]=temp
                       test_failed=test_failed+1
                       break
    planned_tests=pld_tests+planned_tests
    # print("Test_planned:",planned_tests)
    return planned_tests,test_passed,test_failed

def test_axi_fixed_burst_same_address_write (planned_tests,test_passed,test_failed):
    # global axi_master_base_test_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_test_axi_fixed_burst_same_address_write+"/*.log"
    # get_design_row = axi_master_base_test_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate test_axi_fixed_burst_same_address_write log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        
        # print("*************dasd************",planned_tests)
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        #df.loc[test_name[1],["IP"]]="test_axi_fixed_burst_same_address_write"
        with open (log_file,'r') as read:
           lines = read.readlines()
           for line in lines:
                   if  (re.search (r"UVM_FATAL ..",line)) or (re.search (r"UVM_ERROR ..",line))  :
                       temp=line
                   elif  re.search(r"TEST PASS",line):
                       df.loc[test_name[1],"Status"]="Passed"
                       test_passed=test_passed+1
                       break
                   elif (re.search(r"TEST FAIL",line)) or (re.search(r"\b^UVM_ERROR :    [1-9]*$\b",line)) or (re.search(r"\b^UVM_FATAL :    1\b",line)) :
                    #    print(line)
                       df.loc[test_name[1],"Status"]="Failed"
                       df.loc[test_name[1],"Remarks"]=temp
                       test_failed=test_failed+1
                       break
    planned_tests=pld_tests+planned_tests
    print("Test_planned:",planned_tests)
    return planned_tests,test_passed,test_failed

def test_axi_fixed_burst_write (planned_tests,test_passed,test_failed):
    # global axi_master_base_test_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_test_axi_fixed_burst_write+"/*.log"
    # get_design_row = axi_master_base_test_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate test_axi_fixed_burst_write log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        #df.loc[test_name[1],["IP"]]="test_axi_fixed_burst_write"
        with open (log_file,'r') as read:
           lines = read.readlines()
           for line in lines:
                   if  (re.search (r"UVM_FATAL ..",line)) or (re.search (r"UVM_ERROR ..",line))  :
                       temp=line
                   elif  re.search(r"TEST PASS",line):
                       df.loc[test_name[1],"Status"]="Passed"
                       test_passed=test_passed+1
                       break
                   elif (re.search(r"TEST FAIL",line)) or (re.search(r"\b^UVM_ERROR :    [1-9]*$\b",line)) or (re.search(r"\b^UVM_FATAL :    1\b",line)) :
                    #    print(line)
                       df.loc[test_name[1],"Status"]="Failed"
                       df.loc[test_name[1],"Remarks"]=temp
                       test_failed=test_failed+1
                       break
    planned_tests=pld_tests+planned_tests
    print("Test_planned:",planned_tests)
    return planned_tests,test_passed,test_failed


def test_axi_incr_burst_read (planned_tests,test_passed,test_failed):
    # global axi_master_base_test_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_test_axi_incr_burst_read+"/*.log"
    # get_design_row = axi_master_base_test_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate test_axi_incr_burst_read log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        #df.loc[test_name[1],["IP"]]="test_axi_incr_burst_read"
        with open (log_file,'r') as read:
           lines = read.readlines()
           for line in lines:
                   if  (re.search (r"UVM_FATAL ..",line)) or (re.search (r"UVM_ERROR ..",line))  :
                       temp=line
                   elif  re.search(r"TEST PASS",line):
                       df.loc[test_name[1],"Status"]="Passed"
                       test_passed=test_passed+1
                       break
                   elif (re.search(r"TEST FAIL",line)) or (re.search(r"\b^UVM_ERROR :    [1-9]*$\b",line)) or (re.search(r"\b^UVM_FATAL :    1\b",line)) :
                    #    print(line)
                       df.loc[test_name[1],"Status"]="Failed"
                       df.loc[test_name[1],"Remarks"]=temp
                       test_failed=test_failed+1
                       break
    planned_tests=pld_tests+planned_tests
    print("Test_planned:",planned_tests)
    return planned_tests,test_passed,test_failed

def test_axi_incr_burst_write (planned_tests,test_passed,test_failed):
    # global axi_master_base_test_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_test_axi_incr_burst_write+"/*.log"
    # get_design_row = axi_master_base_test_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Skipping test_axi_incr_burst_write")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        #df.loc[test_name[1],["IP"]]="test_axi_incr_burst_write"
        with open (log_file,'r') as read:
           lines = read.readlines()
           for line in lines:
                   if  (re.search (r"UVM_FATAL ..",line)) or (re.search (r"UVM_ERROR ..",line))  :
                       temp=line
                   elif  re.search(r"TEST PASS",line):
                       df.loc[test_name[1],"Status"]="Passed"
                       test_passed=test_passed+1
                       break
                   elif (re.search(r"TEST FAIL",line)) or (re.search(r"\b^UVM_ERROR :    [1-9]*$\b",line)) or (re.search(r"\b^UVM_FATAL :    1\b",line)) :
                    #    print(line)
                       df.loc[test_name[1],"Status"]="Failed"
                       df.loc[test_name[1],"Remarks"]=temp
                       test_failed=test_failed+1
                       break
    planned_tests=pld_tests+planned_tests
    print("Test_planned:",planned_tests)
    return planned_tests,test_passed,test_failed
# 
def test_axi_random (planned_tests,test_passed,test_failed):
    # global axi_master_base_test_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_test_axi_random+"/*.log"
    # get_design_row = axi_master_base_test_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate test_axi_random log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        #df.loc[test_name[1],["IP"]]="test_axi_random"
        with open (log_file,'r') as read:
           lines = read.readlines()
           for line in lines:
                   if  (re.search (r"UVM_FATAL ..",line)) or (re.search (r"UVM_ERROR ..",line))  :
                       temp=line
                   elif  re.search(r"TEST PASS",line):
                       df.loc[test_name[1],"Status"]="Passed"
                       test_passed=test_passed+1
                       break
                   elif (re.search(r"TEST FAIL",line)) or (re.search(r"\b^UVM_ERROR :    [1-9]*$\b",line)) or (re.search(r"\b^UVM_FATAL :    1\b",line)) :
                    #    print(line)
                       df.loc[test_name[1],"Status"]="Failed"
                       df.loc[test_name[1],"Remarks"]=temp
                       test_failed=test_failed+1
                       break
    planned_tests=pld_tests+planned_tests
    print("Test_planned:",planned_tests)
    return planned_tests,test_passed,test_failed

def test_axi_read_after_write (planned_tests,test_passed,test_failed):
    # global axi_master_base_test_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_test_axi_read_after_write+"/*.log"
    # get_design_row = axi_master_base_test_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate test_axi_read_after_write log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        #df.loc[test_name[1],["IP"]]="test_axi_read_after_write"
        with open (log_file,'r') as read:
           lines = read.readlines()
           for line in lines:
                   if  (re.search (r"UVM_FATAL ..",line)) or (re.search (r"UVM_ERROR ..",line))  :
                       temp=line
                   elif  re.search(r"TEST PASS",line):
                       df.loc[test_name[1],"Status"]="Passed"
                       test_passed=test_passed+1
                       break
                   elif (re.search(r"TEST FAIL",line)) or (re.search(r"\b^UVM_ERROR :    [1-9]*$\b",line)) or (re.search(r"\b^UVM_FATAL :    1\b",line)) :
                    #    print(line)
                       df.loc[test_name[1],"Status"]="Failed"
                       df.loc[test_name[1],"Remarks"]=temp
                       test_failed=test_failed+1
                       break
    planned_tests=pld_tests+planned_tests
    print("Test_planned:",planned_tests)
    return planned_tests,test_passed,test_failed


def test_axi_read_burst_length (planned_tests,test_passed,test_failed):
    # global axi_master_base_test_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_test_axi_read_burst_length+"/*.log"
    # get_design_row = axi_master_base_test_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate test_axi_read_burst_length log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        #df.loc[test_name[1],["IP"]]="test_axi_read_burst_length"
        with open (log_file,'r') as read:
           lines = read.readlines()
           for line in lines:
                   if  (re.search (r"UVM_FATAL ..",line)) or (re.search (r"UVM_ERROR ..",line))  :
                       temp=line
                   elif  re.search(r"TEST PASS",line):
                       df.loc[test_name[1],"Status"]="Passed"
                       test_passed=test_passed+1
                       break
                   elif (re.search(r"TEST FAIL",line)) or (re.search(r"\b^UVM_ERROR :    [1-9]*$\b",line)) or (re.search(r"\b^UVM_FATAL :    1\b",line)) :
                    #    print(line)
                       df.loc[test_name[1],"Status"]="Failed"
                       df.loc[test_name[1],"Remarks"]=temp
                       test_failed=test_failed+1
                       break
    planned_tests=pld_tests+planned_tests
    print("Test_planned:",planned_tests)
    return planned_tests,test_passed,test_failed



def test_axi_read_write_strobes (planned_tests,test_passed,test_failed):
    # global axi_master_base_test_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_test_axi_read_write_strobes+"/*.log"
    # get_design_row = axi_master_base_test_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate test_axi_read_write_strobes log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        #df.loc[test_name[1],["IP"]]="test_axi_read_write_strobes"
        with open (log_file,'r') as read:
           lines = read.readlines()
           for line in lines:
                   if  (re.search (r"UVM_FATAL ..",line)) or (re.search (r"UVM_ERROR ..",line))  :
                       temp=line
                   elif  re.search(r"TEST PASS",line):
                       df.loc[test_name[1],"Status"]="Passed"
                       test_passed=test_passed+1
                       break
                   elif (re.search(r"TEST FAIL",line)) or (re.search(r"\b^UVM_ERROR :    [1-9]*$\b",line)) or (re.search(r"\b^UVM_FATAL :    1\b",line)) :
                    #    print(line)
                       df.loc[test_name[1],"Status"]="Failed"
                       df.loc[test_name[1],"Remarks"]=temp
                       test_failed=test_failed+1
                       break
    planned_tests=pld_tests+planned_tests
    print("Test_planned:",planned_tests)
    return planned_tests,test_passed,test_failed

def test_axi_wrap_burst_read (planned_tests,test_passed,test_failed):
    # global axi_master_base_test_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_test_axi_wrap_burst_read+"/*.log"
    # get_design_row = axi_master_base_test_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate test_axi_wrap_burst_read log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        #df.loc[test_name[1],["IP"]]="test_axi_wrap_burst_read"
        with open (log_file,'r') as read:
           lines = read.readlines()
           for line in lines:
                   if  (re.search (r"UVM_FATAL ..",line)) or (re.search (r"UVM_ERROR ..",line))  :
                       temp=line
                   elif  re.search(r"TEST PASS",line):
                       df.loc[test_name[1],"Status"]="Passed"
                       test_passed=test_passed+1
                       break
                   elif (re.search(r"TEST FAIL",line)) or (re.search(r"\b^UVM_ERROR :    [1-9]*$\b",line)) or (re.search(r"\b^UVM_FATAL :    1\b",line)) :
                    #    print(line)
                       df.loc[test_name[1],"Status"]="Failed"
                       df.loc[test_name[1],"Remarks"]=temp
                       test_failed=test_failed+1
                       break
    planned_tests=pld_tests+planned_tests
    print("Test_planned:",planned_tests)
    return planned_tests,test_passed,test_failed

def test_axi_wrap_burst_write (planned_tests,test_passed,test_failed):
    # global axi_master_base_test_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_test_axi_wrap_burst_write+"/*.log"
    # get_design_row = axi_master_base_test_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate test_axi_wrap_burst_write log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        #df.loc[test_name[1],["IP"]]="test_axi_wrap_burst_write"
        with open (log_file,'r') as read:
           lines = read.readlines()
           for line in lines:
                   if  (re.search (r"UVM_FATAL ..",line)) or (re.search (r"UVM_ERROR ..",line))  :
                       temp=line
                   elif  re.search(r"TEST PASS",line):
                       df.loc[test_name[1],"Status"]="Passed"
                       test_passed=test_passed+1
                       break
                   elif (re.search(r"TEST FAIL",line)) or (re.search(r"\b^UVM_ERROR :    [1-9]*$\b",line)) or (re.search(r"\b^UVM_FATAL :    1\b",line)) :
                    #    print(line)
                       df.loc[test_name[1],"Status"]="Failed"
                       df.loc[test_name[1],"Remarks"]=temp
                       test_failed=test_failed+1
                       break
    planned_tests=pld_tests+planned_tests
    print("Test_planned:",planned_tests)
    return planned_tests,test_passed,test_failed

def test_axi_write_burst_length (planned_tests,test_passed,test_failed):
    # global axi_master_base_test_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_test_axi_write_burst_length+"/*.log"
    # get_design_row = axi_master_base_test_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate test_axi_write_burst_length log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        #df.loc[test_name[1],["IP"]]="test_axi_write_burst_length"
        with open (log_file,'r') as read:
           lines = read.readlines()
           for line in lines:
                   if  (re.search (r"UVM_FATAL ..",line)) or (re.search (r"UVM_ERROR ..",line))  :
                       temp=line
                   elif  re.search(r"TEST PASS",line):
                       df.loc[test_name[1],"Status"]="Passed"
                       test_passed=test_passed+1
                       break
                   elif (re.search(r"TEST FAIL",line)) or (re.search(r"\b^UVM_ERROR :    [1-9]*$\b",line)) or (re.search(r"\b^UVM_FATAL :    1\b",line)) :
                    #    print(line)
                       df.loc[test_name[1],"Status"]="Failed"
                       df.loc[test_name[1],"Remarks"]=temp
                       test_failed=test_failed+1
                       break
    planned_tests=pld_tests+planned_tests
    print("Test_planned:",planned_tests)
    return planned_tests,test_passed,test_failed

def test_debug (planned_tests,test_passed,test_failed):
    # global axi_master_base_test_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_test_debug+"/*.log"
    # get_design_row = axi_master_base_test_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate test_debug log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        #df.loc[test_name[1],["IP"]]="test_debug"
        with open (log_file,'r') as read:
           lines = read.readlines()
           for line in lines:
                   if  (re.search (r"UVM_FATAL ..\/",line)) or (re.search (r"^\bUVM_ERROR ..\/\b",line))  :
                       temp=line
                   elif  re.search(r"TEST PASS",line):
                       df.loc[test_name[1],"Status"]="Passed"
                       test_passed=test_passed+1
                       break
                   elif (re.search(r"TEST FAIL",line)) or (re.search(r"UVM_FATAL :    1",line)):                                                   
                    #    print(line)
                       df.loc[test_name[1],"Status"]="Failed"
                       df.loc[test_name[1],"Remarks"]=temp
                       test_failed=test_failed+1
                       break
    planned_tests=pld_tests+planned_tests
    print("Test_planned:",planned_tests)
    return planned_tests,test_passed,test_failed

def test_mixed_bursts_settings (planned_tests,test_passed,test_failed):
    # global axi_master_base_test_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_test_mixed_bursts_settings+"/*.log"
    # get_design_row = axi_master_base_test_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate test_mixed_bursts_settings log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        #df.loc[test_name[1],["IP"]]="test_mixed_bursts_settings"
        with open (log_file,'r') as read:
           lines = read.readlines()
           for line in lines:
                   if  (re.search (r"UVM_FATAL ..",line)) or (re.search (r"UVM_ERROR ..",line))  :
                       temp=line
                   elif  re.search(r"TEST PASS",line):
                       df.loc[test_name[1],"Status"]="Passed"
                       test_passed=test_passed+1
                       break
                   elif (re.search(r"TEST FAIL",line)) or (re.search(r"\b^UVM_ERROR :    [1-9]*$\b",line)) or (re.search(r"\b^UVM_FATAL :    1\b",line)) :
                    #    print(line)
                       df.loc[test_name[1],"Status"]="Failed"
                       df.loc[test_name[1],"Remarks"]=temp
                       test_failed=test_failed+1
                       break
    planned_tests=pld_tests+planned_tests
    print("Test_planned:",planned_tests)
    return planned_tests,test_passed,test_failed

def test_parallel_banks_access (planned_tests,test_passed,test_failed):
    # global axi_master_base_test_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_test_parallel_banks_access+"/*.log"
    # get_design_row = axi_master_base_test_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate test_parallel_banks_access log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        #df.loc[test_name[1],["IP"]]="test_parallel_banks_access"
        with open (log_file,'r') as read:
           lines = read.readlines()
           for line in lines:
                   if  (re.search (r"UVM_FATAL ..",line)) or (re.search (r"UVM_ERROR ..",line))  :
                       temp=line
                   elif  re.search(r"TEST PASS",line):
                       df.loc[test_name[1],"Status"]="Passed"
                       test_passed=test_passed+1
                       break
                   elif (re.search(r"TEST FAIL",line)) or (re.search(r"\b^UVM_ERROR :    [1-9]*$\b",line)) or (re.search(r"\b^UVM_FATAL :    1\b",line)) :
                    #    print(line)
                       df.loc[test_name[1],"Status"]="Failed"
                       df.loc[test_name[1],"Remarks"]=temp
                       test_failed=test_failed+1
                       break
    planned_tests=pld_tests+planned_tests
    print("Test_planned:",planned_tests)
    return planned_tests,test_passed,test_failed

def test_read_fixed_latency (planned_tests,test_passed,test_failed):
    # global axi_master_base_test_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_test_read_fixed_latency+"/*.log"
    # get_design_row = axi_master_base_test_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate test_read_fixed_latency log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        #df.loc[test_name[1],["IP"]]="test_read_fixed_latency"
        with open (log_file,'r') as read:
           lines = read.readlines()
           for line in lines:
                   if  (re.search (r"UVM_FATAL ..",line)) or (re.search (r"UVM_ERROR ..",line))  :
                       temp=line
                   elif  re.search(r"TEST PASS",line):
                       df.loc[test_name[1],"Status"]="Passed"
                       test_passed=test_passed+1
                       break
                   elif (re.search(r"TEST FAIL",line)) or (re.search(r"\b^UVM_ERROR :    [1-9]*$\b",line)) or (re.search(r"\b^UVM_FATAL :    1\b",line)) :
                    #    print(line)
                       df.loc[test_name[1],"Status"]="Failed"
                       df.loc[test_name[1],"Remarks"]=temp
                       test_failed=test_failed+1
                       break
    planned_tests=pld_tests+planned_tests
    print("Test_planned:",planned_tests)
    return planned_tests,test_passed,test_failed

def test_read_incr_latency (planned_tests,test_passed,test_failed):
    # global axi_master_base_test_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_test_read_incr_latency+"/*.log"
    # get_design_row = axi_master_base_test_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate test_read_incr_latency log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        #df.loc[test_name[1],["IP"]]="test_read_incr_latency"
        with open (log_file,'r') as read:
           lines = read.readlines()
           for line in lines:
                   if  (re.search (r"UVM_FATAL ..",line)) or (re.search (r"UVM_ERROR ..",line))  :
                       temp=line
                   elif  re.search(r"TEST PASS",line):
                       df.loc[test_name[1],"Status"]="Passed"
                       test_passed=test_passed+1
                       break
                   elif (re.search(r"TEST FAIL",line)) or (re.search(r"\b^UVM_ERROR :    [1-9]*$\b",line)) or (re.search(r"\b^UVM_FATAL :    1\b",line)) :
                    #    print(line)
                       df.loc[test_name[1],"Status"]="Failed"
                       df.loc[test_name[1],"Remarks"]=temp
                       test_failed=test_failed+1
                       break
    planned_tests=pld_tests+planned_tests
    print("Test_planned:",planned_tests)
    return planned_tests,test_passed,test_failed

def test_read_wrap_latency (planned_tests,test_passed,test_failed):
    # global axi_master_base_test_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_test_read_wrap_latency+"/*.log"
    # get_design_row = axi_master_base_test_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate test_read_wrap_latency log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        #df.loc[test_name[1],["IP"]]="test_read_wrap_latency"
        with open (log_file,'r') as read:
           lines = read.readlines()
           for line in lines:
                   if  (re.search (r"UVM_FATAL ..",line)) or (re.search (r"UVM_ERROR ..",line))  :
                       temp=line
                   elif  re.search(r"TEST PASS",line):
                       df.loc[test_name[1],"Status"]="Passed"
                       test_passed=test_passed+1
                       break
                   elif (re.search(r"TEST FAIL",line)) or (re.search(r"\b^UVM_ERROR :    [1-9]*$\b",line)) or (re.search(r"\b^UVM_FATAL :    1\b",line)) :
                    #    print(line)
                       df.loc[test_name[1],"Status"]="Failed"
                       df.loc[test_name[1],"Remarks"]=temp
                       test_failed=test_failed+1
                       break
    planned_tests=pld_tests+planned_tests
    print("Test_planned:",planned_tests)
    return planned_tests,test_passed,test_failed

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
filename_css = 'sram_css_states.csv'
filename_dash = 'sram_css_states_dash.csv'
filename_time = 'sram_time.csv'
filename_pie = 'sram_pie_states_dash.csv'
#print (filename)
location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
df_grp_dash=pd.DataFrame(df,columns=["Category","Numbers"])
df_grp=pd.DataFrame(df,columns=["Category","Numbers"])
df=pd.DataFrame(df,columns=["Test_Name","Status","Remarks"])
df_time=pd.DataFrame(df,columns=["Regression_Run_Time"])
# print (location)
###Paths####
logs_location = location+"/../results/regression_folder"
csv_location = location+"/../results/"

ip_test_axi_boundary_write_read= logs_location +"/test_axi_boundary_write_read"
ip_test_axi_burst_sizes= logs_location +"/test_axi_burst_sizes"
ip_test_axi_consecutive_IDs= logs_location +"/test_axi_consecutive_IDs"
ip_test_axi_fixed_burst_read= logs_location +"/test_axi_fixed_burst_read"
ip_axi_master_base_test= logs_location +"/axi_master_base_test"
ip_test_axi_fixed_burst_same_address_read= logs_location +"/test_axi_fixed_burst_same_address_read"
ip_test_axi_fixed_burst_same_address_write= logs_location +"/test_axi_fixed_burst_same_address_write"
ip_test_all_one_write_read= logs_location +"/test_all_one_write_read"
ip_test_all_zero_write_read= logs_location +"/test_all_zero_write_read"
ip_test_axi_fixed_burst_write= logs_location +"/test_axi_fixed_burst_write"
ip_test_axi_incr_burst_read= logs_location +"/test_axi_incr_burst_read"
ip_test_axi_incr_burst_write= logs_location +"/test_axi_incr_burst_write"
ip_test_axi_random= logs_location +"/test_axi_random"
ip_test_axi_read_after_write= logs_location +"/test_axi_read_after_write"
ip_test_axi_read_burst_length= logs_location +"/test_axi_read_burst_length"
ip_test_axi_read_write_strobes= logs_location +"/test_axi_read_write_strobes"
ip_test_axi_wrap_burst_read= logs_location +"/test_axi_wrap_burst_read"
ip_test_axi_wrap_burst_write= logs_location +"/test_axi_wrap_burst_write"
ip_test_axi_write_burst_length= logs_location +"/test_axi_write_burst_length"
ip_test_debug= logs_location +"/test_debug"
ip_test_mixed_bursts_settings= logs_location +"/test_mixed_bursts_settings"
ip_test_parallel_banks_access= logs_location +"/test_parallel_banks_access"
ip_test_read_fixed_latency= logs_location +"/test_read_fixed_latency"
ip_test_read_incr_latency= logs_location +"/test_read_incr_latency"
ip_test_read_wrap_latency= logs_location +"/test_read_wrap_latency"
# print (ip_axi_master_base_test)
# get_ip_name(ip_axi_master_base_test)
tests_plnd,tests_p,tests_f=axi_master_base_test(planned_tests,test_passed,test_failed)
row_no = len(df.index)
design_collction = {"Test":row_no}
tests_plnd,tests_p,tests_f=test_all_one_write_read(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=test_all_zero_write_read(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=test_axi_boundary_write_read(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=test_axi_burst_sizes(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=test_axi_consecutive_IDs(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=test_axi_fixed_burst_read(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=test_axi_fixed_burst_same_address_read(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=test_axi_fixed_burst_same_address_write(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=test_axi_fixed_burst_write(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}


tests_plnd,tests_p,tests_f=test_axi_incr_burst_read(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=test_axi_incr_burst_write(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=test_axi_random(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=test_axi_read_after_write(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=test_axi_read_burst_length(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=test_axi_read_write_strobes(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=test_axi_wrap_burst_read(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=test_axi_wrap_burst_write(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=test_axi_write_burst_length(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=test_debug(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=test_mixed_bursts_settings(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=test_parallel_banks_access(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=test_read_fixed_latency(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=test_read_incr_latency(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=test_read_wrap_latency(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

design_collction = {"Test":row_no}
print("Total tests planned",tests_plnd)
print("Total tests passed",tests_p)
print("Total tests failed",tests_f)



df_grp_dash.loc["0","Category"]="Tests Under Development"
df_grp_dash.loc["1","Category"]="Tests Passed"
df_grp_dash.loc["2","Category"]="Tests Failed"

df_grp_dash.loc["0","Numbers"]= 25-tests_p-tests_f
df_grp_dash.loc["1","Numbers"]= tests_p
df_grp_dash.loc["2","Numbers"]= tests_f

# df_grp.loc["0"]="Serial No"
df_grp.loc["0","Category"]="Tests Planned"
df_grp.loc["1","Category"]="Tests Passed"
df_grp.loc["2","Category"]="Tests Failed"
df_grp.loc["0","Numbers"]= "25"
df_grp.loc["1","Numbers"]= tests_p
df_grp.loc["2","Numbers"]= tests_f
# df_grp_dash = df_grp_dash.loc.astype(str).replace('\.\d+', '', regex=True).astype(int)

# df_to_csv (df)
# print(df_grp_dash)
# print(df)
###############################################################################
def get_time():
 log_files= ip_test_all_one_write_read +"/test_all_one_write_read.log"
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
                       df_time.loc["0","Regression_Run_Time"]=line[-1]
get_time()
df_to_csv (df,filename_css)
df_to_csv (df_grp,filename_dash)
df_to_csv (df_grp_dash,filename_pie)
df_to_csv (df_time,filename_time)
print(df_grp)
print(df)
print(df_grp_dash)
print(df_time)
