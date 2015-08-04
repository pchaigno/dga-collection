#!/usr/bin/env python3
from DGAMalware import DGAMalware

"""TLDs used by Necurs.

"""
tlds = ['tj','in','jp','tw','ac','cm','la','mn','so','sh','sc','nu','nf','mu',
        'ms','mx','ki','im','cx','cc','tv','bz','me','eu','de','ru','co','su','pw',
        'kz','sx','us','ug','ir','to','ga','com','net','org','biz','xxx','pro','bit']


"""Domain Generation Algorithm for Necurs.

Source:
  http://www.johannesbader.ch/2015/02/the-dgas-of-necurs/
  Johannes Bader
  February 20, 2015

"""
class Necurs(DGAMalware):

  @classmethod
  def domainsLifetime(self):
    return 4 * 24 * 3600

  @classmethod
  def domainsFor(self, date):
    domains = []
    for sequence_nr in range(2048):
      domains.append(self.generateDomain(sequence_nr, 9, date))
    return domains

  @classmethod
  def generateDomain(self, sequence_nr, magic_nr, date):
    n = self.pseudoRandom(date.year)
    n = self.pseudoRandom(n + date.month + 43690)
    n = self.pseudoRandom(n + (date.day>>2))
    n = self.pseudoRandom(n + sequence_nr)
    n = self.pseudoRandom(n + magic_nr)
    domain_length = self.mod64(n, 15) + 7

    domain = "" 
    for i in range(domain_length):
      n = self.pseudoRandom(n+i)
      ch = self.mod64(n, 25) + ord('a')
      domain += chr(ch)
      n += 0xABBEDF
      n = self.pseudoRandom(n)

    tld = tlds[self.mod64(n, 43)]
    domain += '.' + tld
    return domain

  @classmethod
  def pseudoRandom(self, value):
    loops = (value & 0x7F) + 21
    for index in range(loops):
      value += ((value * 7) ^ (value << 15)) + 8 * index - (value >> 5)
      value &= ((1 << 64) - 1)
    return value

  @classmethod
  def mod64(self, nr1, nr2):
    return nr1 % nr2

  @classmethod
  def couldUseDomain(self, domain):
    useTLD = False
    for tld in tlds:
      if domain.endswith(tld):
        useTLD = True
        break
    if not useTLD:
      return False
    return not any(char.isdigit() for char in domain)
