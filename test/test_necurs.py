from test.test_dga import TestDGA
from dgacollection.Necurs import Necurs
from unittest import TestCase


"""Examples of domains.

Usually found with the reverse engineering analysis.

"""
necurs_domains = ['19/02/2015', 
                  ['boymlujtgp.nu', 'ybynentfsjvmsgtktcoog.im', 'oiijxplrnmvgskxwaye.ru', 
                  'imgirmyddbsniuh.pw', 'ultrttvbvjaanrj.jp', 'porgtemsbycy.ki']]


"""Performs a few unit tests on the Necurs DGA.

"""
class TestNecurs(TestDGA, TestCase):

  """Checks that couldUseDomain returns True for correct domains.

  """
  def testCouldUseDomain(self):
    self.assertTrue(Necurs.couldUseDomain('ultrttvbvjaanrj.jp'))

  """Checks the lifetime value of domains for each DGA.

  """
  def testDomainLifetime(self):
    self.assertEqual(4 * 86400, Necurs.domainsLifetime())

  """Checks that each DGA returns the expected number of domains for the current day.

  """
  def testNbDomains(self):
    self.assertEqual(2048, len(Necurs.domains()))

  """Checks the presence of a few known domains for a given date.

  """
  def testDomains(self):
    self.assertTrue(self.checkDomains(Necurs, necurs_domains))
