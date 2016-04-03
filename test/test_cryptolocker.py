from test.test_dga import TestDGA
from dgacollection.Cryptolocker import Cryptolocker
from unittest import TestCase

"""Examples of domains.

Usually found with the reverse engineering analysis.

"""
cryptolocker_domains = ['19/12/2013', 
                          ['sljjjupfgagolpg.ru', 'vxagtvsyqxtrfcm.com',
                           'wxphewjnfhlyyjj.net', 'xckjffnjivafxen.biz']]


"""Performs a few unit tests on the Cryptolocker DGA.

"""
class TestCryptolocker(TestDGA, TestCase):

  """Checks that couldUseDomain returns True for correct domains.

  """
  def testCouldUseDomain(self):
    self.assertTrue(Cryptolocker.couldUseDomain('gfrtgcfgvopvgg.co.uk'))

  """Checks the lifetime value of domains for each DGA.

  """
  def testDomainLifetime(self):
    self.assertEqual(86400, Cryptolocker.domainsLifetime())

  """Checks that each DGA returns the expected number of domains for the current day.

  """
  def testNbDomains(self):
    self.assertEqual(1000, len(Cryptolocker.domains()))

  """Checks the presence of a few known domains for a given date.

  """
  def testDomains(self):
    self.assertTrue(self.checkDomains(Cryptolocker, cryptolocker_domains))
