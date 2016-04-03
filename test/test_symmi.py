from test.test_dga import TestDGA
from dgacollection.Symmi import Symmi
from unittest import TestCase


"""Examples of domains.

Usually found with the reverse engineering analysis.

"""
symmi_domains = ['20/12/2015', 
                  ['veeswaehsisa.ddns.net', 'uhbacoinm.ddns.net', 'baugkoosdui.ddns.net']]


"""Performs a few unit tests on the Symmi DGA.

"""
class TestSymmi(TestDGA, TestCase):

  """Checks that couldUseDomain returns True for correct domains.

  """
  def testCouldUseDomain(self):
    self.assertTrue(Symmi.couldUseDomain('baugkoosdui.ddns.net'))

  """Checks the lifetime value of domains for each DGA.

  """
  def testDomainLifetime(self):
    self.assertEqual(16 * 86400, Symmi.domainsLifetime())

  """Checks that each DGA returns the expected number of domains for the current day.

  """
  def testNbDomains(self):
    self.assertEqual(64, len(Symmi.domains()))

  """Checks the presence of a few known domains for a given date.

  """
  def testDomains(self):
    self.assertTrue(self.checkDomains(Symmi, symmi_domains))
