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
#  log_files= ip_abort3_bist_test_pcb +"/abort3_bist_test_pcb.log"
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
def abort2_bist_test_pcb (planned_tests,test_passed,test_failed):
    global abort2_bist_test_pcb_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_abort2_bist_test_pcb+"/"+"*_pcb.log"
    # get_design_row = abort2_bist_test_pcb_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate abort2_bist_test_pcb log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        #df.loc[test_name[1],["IP"]]="abort2_bist_test_pcb"
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
    # df["IP"]="abort2_bist_test_pcb"    
    # test_collection
def abort3_bist_test_pcb (planned_tests,test_passed,test_failed):
    # global abort2_bist_test_pcb_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_abort3_bist_test_pcb+"/"+"*_pcb.log"
    # get_design_row = abort2_bist_test_pcb_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate abort3_bist_test_pcb log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        #df.loc[test_name[1],["IP"]]="abort3_bist_test_pcb"
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

def abort4_bist_test_pcb (planned_tests,test_passed,test_failed):
    # global abort2_bist_test_pcb_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_abort4_bist_test_pcb+"/"+"*_pcb.log"
    # get_design_row = abort2_bist_test_pcb_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate abort4_bist_test_pcb log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        #df.loc[test_name[1],["IP"]]="abort4_bist_test_pcb"
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

def abort5_bist_test_pcb (planned_tests,test_passed,test_failed):
    # global abort2_bist_test_pcb_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_abort5_bist_test_pcb+"/"+"*_pcb.log"
    # get_design_row = abort2_bist_test_pcb_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate abort5_bist_test_pcb log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        #df.loc[test_name[1],["IP"]]="abort5_bist_test_pcb"
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

def abort6_bist_test_pcb (planned_tests,test_passed,test_failed):
    # global abort2_bist_test_pcb_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_abort6_bist_test_pcb+"/"+"*_pcb.log"
    # get_design_row = abort2_bist_test_pcb_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate abort6_bist_test_pcb log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        #df.loc[test_name[1],["IP"]]="abort6_bist_test_pcb"
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
def abort7_bist_test_pcb (planned_tests,test_passed,test_failed):
    # global abort2_bist_test_pcb_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_abort7_bist_test_pcb+"/"+"*_pcb.log"
    # get_design_row = abort2_bist_test_pcb_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate abort7_bist_test_pcb log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        #df.loc[test_name[1],["IP"]]="abort7_bist_test_pcb"
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
def abort8_bist_test_pcb (planned_tests,test_passed,test_failed):
    # global abort2_bist_test_pcb_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_abort8_bist_test_pcb+"/"+"*_pcb.log"
    # get_design_row = abort2_bist_test_pcb_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate abort8_bist_test_pcb log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        #df.loc[test_name[1],["IP"]]="abort8_bist_test_pcb"
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
def bist_fsm1_reset_test_pcb (planned_tests,test_passed,test_failed):
    # global abort2_bist_test_pcb_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_bist_fsm1_reset_test_pcb+"/"+"*_pcb.log"
    # get_design_row = abort2_bist_test_pcb_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate bist_fsm1_reset_test_pcb log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        #df.loc[test_name[1],["IP"]]="bist_fsm1_reset_test_pcb"
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

def bist_fsm9_reset_test_pcb (planned_tests,test_passed,test_failed):
    # global abort2_bist_test_pcb_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_bist_fsm9_reset_test_pcb+"/"+"*_pcb.log"
    # get_design_row = abort2_bist_test_pcb_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate bist_fsm9_reset_test_pcb log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        
        # print("*************dasd************",planned_tests)
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        #df.loc[test_name[1],["IP"]]="bist_fsm9_reset_test_pcb"
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

def bist_fsm10_reset_test_pcb (planned_tests,test_passed,test_failed):
    # global abort2_bist_test_pcb_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_bist_fsm10_reset_test_pcb+"/"+"*_pcb.log"
    # get_design_row = abort2_bist_test_pcb_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate bist_fsm10_reset_test_pcb log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        #df.loc[test_name[1],["IP"]]="bist_fsm10_reset_test_pcb"
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


def bist_status_reg_test_pcb (planned_tests,test_passed,test_failed):
    # global abort2_bist_test_pcb_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_bist_status_reg_test_pcb+"/"+"*_pcb.log"
    # get_design_row = abort2_bist_test_pcb_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate bist_status_reg_test_pcb log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        #df.loc[test_name[1],["IP"]]="bist_status_reg_test_pcb"
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

def bist_test_pcb (planned_tests,test_passed,test_failed):
    # global abort2_bist_test_pcb_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_bist_test_pcb+"/"+"*_pcb.log"
    # get_design_row = abort2_bist_test_pcb_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Skipping bist_test_pcb")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        #df.loc[test_name[1],["IP"]]="bist_test_pcb"
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
def braodcast2_test_pcb (planned_tests,test_passed,test_failed):
    # global abort2_bist_test_pcb_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_braodcast2_test_pcb+"/"+"*_pcb.log"
    # get_design_row = abort2_bist_test_pcb_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate braodcast2_test_pcb log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        #df.loc[test_name[1],["IP"]]="braodcast2_test_pcb"
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

def braodcast_test_pcb (planned_tests,test_passed,test_failed):
    # global abort2_bist_test_pcb_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_braodcast_test_pcb+"/"+"*_pcb.log"
    # get_design_row = abort2_bist_test_pcb_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate braodcast_test_pcb log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        #df.loc[test_name[1],["IP"]]="braodcast_test_pcb"
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


def calib_fsm1_reset_test_pcb (planned_tests,test_passed,test_failed):
    # global abort2_bist_test_pcb_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_calib_fsm1_reset_test_pcb+"/"+"*_pcb.log"
    # get_design_row = abort2_bist_test_pcb_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate calib_fsm1_reset_test_pcb log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        #df.loc[test_name[1],["IP"]]="calib_fsm1_reset_test_pcb"
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



def calib_fsm2_reset_test_pcb (planned_tests,test_passed,test_failed):
    # global abort2_bist_test_pcb_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_calib_fsm2_reset_test_pcb+"/"+"*_pcb.log"
    # get_design_row = abort2_bist_test_pcb_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate calib_fsm2_reset_test_pcb log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        #df.loc[test_name[1],["IP"]]="calib_fsm2_reset_test_pcb"
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

def calib_fsm3_reset_test_pcb (planned_tests,test_passed,test_failed):
    # global abort2_bist_test_pcb_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_calib_fsm3_reset_test_pcb+"/"+"*_pcb.log"
    # get_design_row = abort2_bist_test_pcb_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate calib_fsm3_reset_test_pcb log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        #df.loc[test_name[1],["IP"]]="calib_fsm3_reset_test_pcb"
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

def calib_fsm4_reset_test_pcb (planned_tests,test_passed,test_failed):
    # global abort2_bist_test_pcb_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_calib_fsm4_reset_test_pcb+"/"+"*_pcb.log"
    # get_design_row = abort2_bist_test_pcb_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate calib_fsm4_reset_test_pcb log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        #df.loc[test_name[1],["IP"]]="calib_fsm4_reset_test_pcb"
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

def calib_fsm5_reset_test_pcb (planned_tests,test_passed,test_failed):
    # global abort2_bist_test_pcb_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_calib_fsm5_reset_test_pcb+"/"+"*_pcb.log"
    # get_design_row = abort2_bist_test_pcb_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate calib_fsm5_reset_test_pcb log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        #df.loc[test_name[1],["IP"]]="calib_fsm5_reset_test_pcb"
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

def calibrate_test_pcb (planned_tests,test_passed,test_failed):
    # global abort2_bist_test_pcb_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_calibrate_test_pcb+"/"+"*_pcb.log"
    # get_design_row = abort2_bist_test_pcb_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate calibrate_test_pcb log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        #df.loc[test_name[1],["IP"]]="calibrate_test_pcb"
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

def col_braodcast2_test_pcb (planned_tests,test_passed,test_failed):
    # global abort2_bist_test_pcb_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_col_braodcast2_test_pcb+"/"+"*_pcb.log"
    # get_design_row = abort2_bist_test_pcb_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate col_braodcast2_test_pcb log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        #df.loc[test_name[1],["IP"]]="col_braodcast2_test_pcb"
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

def col_braodcast_test_pcb (planned_tests,test_passed,test_failed):
    # global abort2_bist_test_pcb_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_col_braodcast_test_pcb+"/"+"*_pcb.log"
    # get_design_row = abort2_bist_test_pcb_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate col_braodcast_test_pcb log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        #df.loc[test_name[1],["IP"]]="col_braodcast_test_pcb"
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

def ctrl_a_inc_test_pcb (planned_tests,test_passed,test_failed):
    # global abort2_bist_test_pcb_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_ctrl_a_inc_test_pcb+"/"+"*_pcb.log"
    # get_design_row = abort2_bist_test_pcb_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate ctrl_a_inc_test_pcb log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        #df.loc[test_name[1],["IP"]]="ctrl_a_inc_test_pcb"
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

def ctrl_s_inc_test_pcb (planned_tests,test_passed,test_failed):
    # global abort2_bist_test_pcb_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_ctrl_s_inc_test_pcb+"/"+"*_pcb.log"
    # get_design_row = abort2_bist_test_pcb_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate ctrl_s_inc_test_pcb log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        #df.loc[test_name[1],["IP"]]="ctrl_s_inc_test_pcb"
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

def enable_test_pcb (planned_tests,test_passed,test_failed):
    # global abort2_bist_test_pcb_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_enable_test_pcb+"/"+"*_pcb.log"
    # get_design_row = abort2_bist_test_pcb_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate enable_test_pcb log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        #df.loc[test_name[1],["IP"]]="enable_test_pcb"
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

def fail_bist_test_pcb (planned_tests,test_passed,test_failed):
    # global abort2_bist_test_pcb_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_fail_bist_test_pcb+"/"+"*_pcb.log"
    # get_design_row = abort2_bist_test_pcb_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate fail_bist_test_pcb log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        #df.loc[test_name[1],["IP"]]="fail_bist_test_pcb"
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

def parity_test_pcb (planned_tests,test_passed,test_failed):
    # global abort2_bist_test_pcb_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_parity_test_pcb+"/"+"*_pcb.log"
    # get_design_row = abort2_bist_test_pcb_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate parity_test_pcb log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        #df.loc[test_name[1],["IP"]]="parity_test_pcb"
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

def pl_ram_test_pcb (planned_tests,test_passed,test_failed):
    # global abort2_bist_test_pcb_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_pl_ram_test_pcb+"/"+"*_pcb.log"
    # get_design_row = abort2_bist_test_pcb_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate pl_ram_test_pcb log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        #df.loc[test_name[1],["IP"]]="pl_ram_test_pcb"
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

def register_wr_test_pcb (planned_tests,test_passed,test_failed):
    # global abort2_bist_test_pcb_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_register_wr_test_pcb+"/"+"*_pcb.log"
    # get_design_row = abort2_bist_test_pcb_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate register_wr_test_pcb log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        #df.loc[test_name[1],["IP"]]="register_wr_test_pcb"
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

def row_braodcast2_test_pcb (planned_tests,test_passed,test_failed):
    # global abort2_bist_test_pcb_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_row_braodcast2_test_pcb+"/"+"*_pcb.log"
    # get_design_row = abort2_bist_test_pcb_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate row_braodcast2_test_pcb log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        #df.loc[test_name[1],["IP"]]="row_braodcast2_test_pcb"
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

def row_braodcast_test_pcb (planned_tests,test_passed,test_failed):
    # global abort2_bist_test_pcb_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_row_braodcast_test_pcb+"/"+"*_pcb.log"
    # get_design_row = abort2_bist_test_pcb_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate row_braodcast_test_pcb log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        #df.loc[test_name[1],["IP"]]="row_braodcast_test_pcb"
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

def split_test_pcb (planned_tests,test_passed,test_failed):
    # global abort2_bist_test_pcb_ip
    temp='NaN'
    log_no=0
    log_count=0
    log_files= ip_split_test_pcb+"/"+"*_pcb.log"
    # get_design_row = abort2_bist_test_pcb_ip   
    # print (get_design_row)
    log_files_glb = glob.glob(log_files)
    if log_files_glb:
        #  print (log_files_glb)
         pass
    else:
         print("Error: glob failed to locate split_test_pcb log files")
    log_count=len(log_files_glb)
    for log_file in log_files_glb:
        # print(count)
        log_no=log_no+1
        pld_tests=log_no
        # planned_tests=pld_tests+planned_tests
        print("[",log_no,"/",log_count,"] Currently processing \n",log_file)
        test_name=get_test_name (log_file)
        df.loc[test_name[1],"Test_Name"]= test_name[0]
        #df.loc[test_name[1],["IP"]]="split_test_pcb"
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
filename_css = 'fcb_css_states.csv'
filename_dash = 'fcb_css_states_dash.csv'
filename_time = 'fcb_time.csv'
filename_pie = 'fcb_pie_states_dash.csv'
#print (filename)
location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
df_grp_dash=pd.DataFrame(df,columns=["Category","Numbers"])
df_grp=pd.DataFrame(df,columns=["Category","Numbers"])
df=pd.DataFrame(df,columns=["Test_Name","Status","Remarks"])
df_time=pd.DataFrame(df,columns=["Regression_Run_Time"])
# print (location)
###Paths####
logs_location = location+"/../results"
csv_location = location+"/../results/"

ip_abort5_bist_test_pcb= logs_location +"/abort5_bist_test_pcb"
ip_abort6_bist_test_pcb= logs_location +"/abort6_bist_test_pcb"
ip_abort7_bist_test_pcb= logs_location +"/abort7_bist_test_pcb"
ip_abort8_bist_test_pcb= logs_location +"/abort8_bist_test_pcb"
ip_abort2_bist_test_pcb= logs_location +"/abort2_bist_test_pcb"
ip_bist_fsm1_reset_test_pcb= logs_location +"/bist_fsm1_reset_test_pcb"
ip_bist_fsm9_reset_test_pcb= logs_location +"/bist_fsm9_reset_test_pcb"
ip_abort3_bist_test_pcb= logs_location +"/abort3_bist_test_pcb"
ip_abort4_bist_test_pcb= logs_location +"/abort4_bist_test_pcb"
ip_bist_fsm10_reset_test_pcb= logs_location +"/bist_fsm10_reset_test_pcb"
ip_bist_status_reg_test_pcb= logs_location +"/bist_status_reg_test_pcb"
ip_bist_test_pcb= logs_location +"/bist_test_pcb"
ip_braodcast2_test_pcb= logs_location +"/braodcast2_test_pcb"
ip_braodcast_test_pcb= logs_location +"/braodcast_test_pcb"
ip_calib_fsm1_reset_test_pcb= logs_location +"/calib_fsm1_reset_test_pcb"
ip_calib_fsm2_reset_test_pcb= logs_location +"/calib_fsm2_reset_test_pcb"
ip_calib_fsm3_reset_test_pcb= logs_location +"/calib_fsm3_reset_test_pcb"
ip_calib_fsm4_reset_test_pcb= logs_location +"/calib_fsm4_reset_test_pcb"
ip_calib_fsm5_reset_test_pcb= logs_location +"/calib_fsm5_reset_test_pcb"
ip_calibrate_test_pcb= logs_location +"/calibrate_test_pcb"
ip_col_braodcast2_test_pcb= logs_location +"/col_braodcast2_test_pcb"
ip_col_braodcast_test_pcb= logs_location +"/col_braodcast_test_pcb"
ip_ctrl_a_inc_test_pcb= logs_location +"/ctrl_a_inc_test_pcb"
ip_ctrl_s_inc_test_pcb= logs_location +"/ctrl_s_inc_test_pcb"
ip_enable_test_pcb= logs_location +"/enable_test_pcb"
ip_fail_bist_test_pcb= logs_location +"/fail_bist_test_pcb"
ip_parity_test_pcb= logs_location +"/parity_test_pcb"
ip_pl_ram_test_pcb= logs_location +"/pl_ram_test_pcb"
ip_register_wr_test_pcb= logs_location +"/register_wr_test_pcb"
ip_row_braodcast2_test_pcb= logs_location +"/row_braodcast2_test_pcb"
ip_row_braodcast_test_pcb= logs_location +"/row_braodcast_test_pcb"
ip_split_test_pcb= logs_location +"/split_test_pcb"
# print (ip_abort2_bist_test_pcb)
# get_ip_name(ip_abort2_bist_test_pcb)
tests_plnd,tests_p,tests_f=abort2_bist_test_pcb(planned_tests,test_passed,test_failed)
row_no = len(df.index)
design_collction = {"Test":row_no}
tests_plnd,tests_p,tests_f=abort3_bist_test_pcb(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=abort4_bist_test_pcb(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=abort5_bist_test_pcb(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=abort6_bist_test_pcb(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=abort7_bist_test_pcb(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=abort8_bist_test_pcb(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=bist_fsm1_reset_test_pcb(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=bist_fsm9_reset_test_pcb(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=bist_fsm10_reset_test_pcb(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}


tests_plnd,tests_p,tests_f=bist_status_reg_test_pcb(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=bist_test_pcb(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=braodcast2_test_pcb(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=braodcast_test_pcb(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=calib_fsm1_reset_test_pcb(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=calib_fsm2_reset_test_pcb(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=calib_fsm3_reset_test_pcb(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=calib_fsm4_reset_test_pcb(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=calib_fsm5_reset_test_pcb(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=calibrate_test_pcb(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=col_braodcast2_test_pcb(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=col_braodcast_test_pcb(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=ctrl_a_inc_test_pcb(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=ctrl_s_inc_test_pcb(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=enable_test_pcb(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=fail_bist_test_pcb(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=parity_test_pcb(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=pl_ram_test_pcb(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=register_wr_test_pcb(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}


tests_plnd,tests_p,tests_f=row_braodcast2_test_pcb(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=row_braodcast_test_pcb(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

tests_plnd,tests_p,tests_f=split_test_pcb(tests_plnd,tests_p,tests_f)
row_no = len(df.index)
design_collction = {"Test":row_no}

design_collction = {"Test":row_no}
print("Total tests planned",tests_plnd)
print("Total tests passed",tests_p)
print("Total tests failed",tests_f)



df_grp_dash.loc["0","Category"]="Tests Under Development"
df_grp_dash.loc["1","Category"]="Tests Passed"
df_grp_dash.loc["2","Category"]="Tests Failed"

df_grp_dash.loc["0","Numbers"]= 32-tests_p-tests_f
df_grp_dash.loc["1","Numbers"]= tests_p
df_grp_dash.loc["2","Numbers"]= tests_f

# df_grp.loc["0"]="Serial No"
df_grp.loc["0","Category"]="Tests Planned"
df_grp.loc["1","Category"]="Tests Passed"
df_grp.loc["2","Category"]="Tests Failed"
df_grp.loc["0","Numbers"]= "32"
df_grp.loc["1","Numbers"]= tests_p
df_grp.loc["2","Numbers"]= tests_f
# df_grp_dash = df_grp_dash.loc.astype(str).replace('\.\d+', '', regex=True).astype(int)

# df_to_csv (df)
# print(df_grp_dash)
# print(df)
###############################################################################
def get_time():
 log_files= ip_abort3_bist_test_pcb +"/abort3_bist_test_pcb.log"
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
