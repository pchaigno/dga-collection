#!/usr/bin/env python3
from DGAMalware import DGAMalware

import os

"""TLDs used by Cryptolocker.

"""
tlds = ["com", "net", "biz", "ru", "org", "co.uk", "info"]


"""Domain Generation Algorithm for more advanced version of Cryptolocker.

Sources:
  https://blog.fortinet.com/post/a-closer-look-at-cryptolocker-s-dga
  Sousan Yazdi
  January 16, 2014

  https://github.com/seifreed/DGA-scripts
  Marc Rivero López
  November 4, 2013

"""
class Cryptolocker(DGAMalware):

  @classmethod
  def domainsFor(self, date):
    domains = []
    for z in range(1000):
      d = date.day
      m = date.month
      y = date.year + z

      d *= 65537
      m *= 65537
      y *= 65537
      
      s = d >> 3 ^ y >> 8 ^ y >> 11
      s &= 3
      s += 12

      n = ""
      for i in range(s):
        d = ((d << 13 & 0xFFFFFFFF) >> 19 & 0xFFFFFFFF) ^ ((d >> 1 & 0xFFFFFFFF) << 13 & 0xFFFFFFFF) ^ (d >> 19 & 0xFFFFFFFF)
        d &= 0xFFFFFFFF
        m = ((m << 2 & 0xFFFFFFFF) >> 25 & 0xFFFFFFFF) ^ ((m >> 3 & 0xFFFFFFFF) << 7 & 0xFFFFFFFF)  ^ (m >> 25 & 0xFFFFFFFF)
        m &= 0xFFFFFFFF
        y = ((y << 3 & 0xFFFFFFFF) >> 11 & 0xFFFFFFFF) ^ ((y >> 4 & 0xFFFFFFFF) << 21 & 0xFFFFFFFF) ^ (y >> 11 & 0xFFFFFFFF)
        y &= 0xFFFFFFFF
        
        n += chr(ord('a') + (y ^ m ^ d) % 25)

      domain = n + "." + tlds[z % 7]
      domains.append(domain)
    return domains


  @classmethod
  def couldUseDomain(self, domain):
    basename = domain.split('.')[0]
    if len(basename) < 12 or len(basename) > 15:
      print("OK" + basename)
      return False
    useTLD = False
    for tld in tlds:
      if domain.endswith(tld):
        useTLD = True
        break
    if not useTLD:
      return False
    return not any(char.isdigit() for char in domain)
