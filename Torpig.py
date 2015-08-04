#!/usr/bin/env python3
from DGAMalware import DGAMalware

"""A few constants for Torpig's DGA.

TLDs and suffixes used.

"""
suffixes = ["anj", "ebf", "arm", "pra", "aym", "unj", "ulj", "uag", "esp", "kot", "onv", "edc"]
tlds = ['.com', '.net', '.biz']


"""Domain Generation Algorithm for Torpig.

Source:
  Your Botnet is My Botnet: Analysis of a Botnet Takeover
  Stone-Gross Brett, Cova Marco, Cavallaro Lorenzo, Gilbert Bob,
  Szydlowski Martin, Kemmerer Richard, Kruegel Christopher and Vigna, Giovanni
  2009

"""
class Torpig(DGAMalware):

  @classmethod
  def domainsFor(self, date):
    label = self.labelFor(date)
    return [label + '.com', label + '.net', label + '.biz']

  @classmethod
  def labelFor(self, date):
    if date.year < 2007:
      date.year = 2007
    s = (((date.month ^ date.day) + date.day) * 8) + date.day + date.year
    c1 = (((date.year >> 2) & 0x3fc0) + s) % 25 + ord('a')
    c2 = (date.month + s) % 10 + ord('a')
    c3 = ((date.year & 0xff) + s) % 25 + ord('a')
    if date.day * 2 < ord('0') or date.day * 2 < ord('9'):
      c4 = (date.day * 2) % 25 + ord('a')
    else:
      c4 = date.day % 10 + ord('1')
    domain = chr(c1) + 'h' + chr(c2) + chr(c3) + 'x' + chr(c4) + suffixes[date.month - 1]
    return domain

  @classmethod
  def couldUseDomain(self, domain):
    useTLD = False
    for tld in tlds:
      if domain.endswith(tld):
        useTLD = True
        usedTLD = tld
        break
    if not useTLD:
      return False

    useSuffix = False
    for suffix in suffixes:
      if domain.endswith(suffix + usedTLD):
        useSuffix = True
        break
    if not useSuffix:
      return False

    return True
