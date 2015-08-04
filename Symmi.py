#!/usr/bin/env python3
from DGAMalware import DGAMalware

"""A few constants for the DGA.

Number of domains for a day, validity period for each domain, 
letters used, length of the third label and seed.

"""
seed_const = 42
days_period = 16
nr_of_domains = 64
third_lvl_min_len = 8
third_lvl_max_len = 15
letters = ["aeiouy", "bcdfghklmnpqrstvwxz"]


"""Pseudo-random generator for Symmi.

"""
class Rand:

  """Constructor

  """
  def __init__(self, seed):
    self.seed = seed

  """Generates the next number depending only on the previous one.

  """
  def rand(self):
    self.seed = (self.seed * 214013 + 2531011) & 0xFFFFFFFF
    return (self.seed >> 16) & 0x7FFF


"""Domain Generation Algorithm for Symmi.

Source:
  http://www.johannesbader.ch/2015/01/the-dga-of-symmi/
  Johannes Bader
  January 21, 2015

"""
class Symmi(DGAMalware):

  @classmethod
  def domainsFor(self, date):
    seed = self.create_seed(date)
    return self.dga(seed, '.ddns.net', nr_of_domains)

  @classmethod
  def next_domain(self, r, second_and_top_lvl, third_lvl_domain_len):
    domain = ""
    for i in range(third_lvl_domain_len):
      if not i % 2:
        offset_1 = 0 if r.rand() & 0x100 == 0 else 1
      s = r.rand()
      offset = (offset_1 + i) % 2
      symbols = letters[offset]
      domain += symbols[s % (len(symbols) - 1)]
    return domain + second_and_top_lvl

  @classmethod
  def dga(self, seed, second_and_top_lvl, nr):
    r = Rand(seed)
    domains = []
    for i in range(nr):
      span = third_lvl_max_len - third_lvl_min_len + 1
      third_lvl_len = third_lvl_min_len + r.rand() % span
      domains.append(self.next_domain(r, second_and_top_lvl, third_lvl_len))
    return domains

  @classmethod
  def create_seed(self, date):
    return 10000 * (date.day // days_period * 100 + date.month) + date.year + seed_const

  @classmethod
  def couldUseDomain(self, domain):
    if not domain.endswith('.ddns.net'):
      return False
    return not any(char.isdigit() for char in domain)
