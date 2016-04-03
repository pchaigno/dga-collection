#!/usr/bin/env python3
from dgacollection.DGAMalware import DGAMalware

"""A few constants for the Ranbyus' DGA.

The original code contains the TLD .org but it's never used due to a bug in the algorithm.

"""
tlds = ['.in', '.me', '.cc', '.su', '.tw', '.net', '.com', '.pw']
nb_domains = 40
uint_mask = 0xFFFFFFFF
default_seed = 0x65BA0743


"""Domain Generation Algorithm for Ranbyus

Sources:
  http://www.johannesbader.ch/2015/05/the-dga-of-ranbyus/
  Johannes Bader
  May 23, 2015

"""
class Ranbyus(DGAMalware):

  @classmethod
  def domainsFor(self, date):
    tld_index = date.day
    day = date.day
    month = date.month
    year = date.year
    domains = []
    seed = default_seed
    for d in range(nb_domains):
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
      domains.append(domain + tlds[tld_index % 8])
      tld_index += 1
    return domains

  """
  Ranbyus' domains don't contain the character 'z'.
  """
  @classmethod
  def couldUseDomain(self, domain):
    useTLD = False
    for tld in tlds:
      if domain.endswith(tld):
        useTLD = True
        break
    if not useTLD:
      return False

    label = domain.split('.', 1)[0]
    if 'z' in label:
      return False

    return not any(char.isdigit() for char in domain)
