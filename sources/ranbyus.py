#!/usr/bin/env python3
# Translated into Python from:
# Source: 
# http://www.johannesbader.ch/2015/05/the-dga-of-ranbyus/
# Johannes Bader
# May 23, 2015
from datetime import date

def dga(date, seed, nr):
  tlds = ['.in', '.me', '.cc', '.su', '.tw', '.net', '.com', '.pw', '.org']
  tld_index = date.day
  day = date.day
  month = date.month
  year = date.year
  uint_mask = 0xFFFFFFFF
  for d in range(nr):
    domain = ''
    for i in range(14):
      day = (day >> 15) ^ 16 * (day & 0x1FFF ^ 4 * (seed ^ day))
      day &= uint_mask
      year_times7 = 7 * year & uint_mask
      year = (((year & 0xFFFFFFF0) << 17) & uint_mask) ^ ((year ^ year_times7) >> 11)
      month_times4 = 4 * month & uint_mask
      month = (14 * (month & 0xFFFFFFFE) & uint_mask) ^ ((month ^ month_times4) >> 8)
      seed_times8 = 8 * seed & uint_mask
      seed = (seed >> 6) ^ ((day + seed_times8 << 8) & uint_mask) & 0x3FFFF00
      x = ((day ^ month ^ year) % 25) + 97
      domain += chr(x)
    print(domain + tlds[tld_index % 8])
    tld_index += 1

dga(date(2015, 8, 5), 0xb6354bc3, 40)
