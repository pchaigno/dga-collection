from test.test_dga import TestDGA
from dgacollection.Torpig import Torpig
from unittest import TestCase


"""Performs a few unit tests on the Torpig DGA.

"""
class TestTorpig(TestDGA, TestCase):

  """Checks that couldUseDomain returns True for correct domains.

  """
  def testCouldUseDomain(self):
    self.assertTrue(Torpig.couldUseDomain('dhidxguag.biz'))

  """Checks the lifetime value of domains for each DGA.

  """
  def testDomainLifetime(self):
    self.assertEqual(86400, Torpig.domainsLifetime())

  """Checks that each DGA returns the expected number of domains for the current day.

  """
  def testNbDomains(self):
    self.assertEqual(3, len(Torpig.domains()))

  # """Checks the presence of a few known domains for a given date.

  # """
  # def testDomains(self):
  #   pass
