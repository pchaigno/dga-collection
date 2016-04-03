from test.test_dga import TestDGA
from dgacollection.Ranbyus import Ranbyus
from unittest import TestCase


"""Examples of domains.

Usually found with the reverse engineering analysis.

"""
ranbyus_domains = ['19/05/2015',
                  ['hcfoopojnuqxho.su', 'undrdsbhivryqn.tw', 'dkehliueofdued.net',
                  'mpuakxjqpscfpj.com', 'eelolbwmfmtkae.pw', 'noppsmyiijqujh.in',
                  'joxrsxwdybbgqb.me']]


"""Performs a few unit tests on the Ranbyus DGA.

"""
class TestRanbyus(TestDGA, TestCase):

  """Checks that couldUseDomain returns True for correct domains.

  """
  def testCouldUseDomain(self):
    self.assertTrue(Ranbyus.couldUseDomain('hcfoopojnuqxho.su'))

  """Checks the lifetime value of domains for each DGA.

  """
  def testDomainLifetime(self):
    self.assertEqual(86400, Ranbyus.domainsLifetime())

  """Checks that each DGA returns the expected number of domains for the current day.

  """
  def testNbDomains(self):
    self.assertEqual(40, len(Ranbyus.domains()))

  """Checks the presence of a few known domains for a given date.

  """
  def testDomains(self):
    self.assertTrue(self.checkDomains(Ranbyus, ranbyus_domains))
