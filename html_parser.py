from bs4 import BeautifulSoup
import codecs
import re
import csv
import sys
import glob
import pandas as pd
import numpy as np
import os 
import pathlib
import html2text
from itertools import islice
# import urllib2
import csv




location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
print(location)
location_html = location+"/assets/soc"
print(location_html)

html_files= location_html + "/*.html"
html_files=location_html+"/hierarchy22.html"
# print(html_files)

for html_file in glob.glob(html_files):
        # print(html_file)
        with open (html_file,'r') as read:
                # index = html_file.read()
                # print(lines)
                S = BeautifulSoup(read, 'lxml')
                # Tag = S.select_one('li:nth-of-type(2)')
                # strips = list(S.stripped_strings)
                # print(strips)
                # print(S.prettify())
                Tag = S.select_one('li:nth-of-type(2)')
                strips = list(S.stripped_strings)
                # print(strips)
                for x in strips:
                    index=strips.index(x)
                    if 'uart0' in strips[index]:
                        print("found",strips[index+4])
                    if 'uart1' in strips[index]:
                        print("found",strips[index+4])
                    if 'dma' in strips[index]:
                        print("found",strips[index+4])

