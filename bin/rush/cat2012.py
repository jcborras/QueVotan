#!/usr/bin/env python
# -*- coding: utf-8; mode: python; -*-

""" Parses and extracts results from web pages """

from csv import QUOTE_NONNUMERIC, register_dialect, writer
from functools import reduce
from os import listdir
from os.path import isfile, join
from re import compile, match

from bs4 import BeautifulSoup

w_re = compile('\w')

def convert(s):
    return int(s.replace('.', ''))

    
def process_catalunya_2012(filename):
    
    with open(filename, encoding="ISO-8859-1") as f:
        soup = BeautifulSoup(f, 'lxml')

    ti =  soup.find('span', {"class": 'tit1'}).text.strip()

    t1 = soup.find(id="TVGEN")
    l1 = t1.find_all('tr')
    d1 = [(ti, l1[i].th.text, convert(l1[i].td.text)) for i in [1,2,3,4,5]]

    t2 = soup.find(id="TVOTOS")
    l2 = t2.find_all('tr', {"class": ['r1 ', 'r1', 'r2']})
    d2 = []
    for i in l2:
        if w_re.match(i.th.text):
            d2.append((ti, i.th.text, convert(i.td.text)))

    return d1 + d2



DATADIR = '../../dat/'
ROOTDIR = '../../tmp/www.gencat.cat/governacio/resultats-parlament2012/09AU/'
FILENAME = 'DAU0908903499_L1.htm'
TARGET = ROOTDIR + FILENAME

onlyfiles = [f for f in listdir(ROOTDIR) if isfile(join(ROOTDIR, f))]
re = compile('DAU\d{10}_L1')
fua = filter(lambda a: re.match(a), onlyfiles)

l = map(lambda a: process_catalunya_2012(ROOTDIR + a), fua)
l2 = reduce(lambda a, b: a+b, l)

with open(DATADIR + 'parlament2012.csv', 'w', encoding='utf-8') as f:
    writer = writer(f, quoting=QUOTE_NONNUMERIC)
    writer.writerows(l2)
