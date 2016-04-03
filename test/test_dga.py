from abc import ABCMeta, abstractmethod
from datetime import datetime, timedelta

"""Abstract class for tests of DGAs.

"""
class TestDGA(object):
  __metaclass__ = ABCMeta

  """Checks that couldUseDomain returns True for correct domains.

  """
  @abstractmethod
  def testCouldUseDomain(self):
    pass

  """Checks the lifetime value of domains for each DGA.

  """
  @abstractmethod
  def testDomainLifetime(self):
    pass

  """Checks that each DGA returns the expected number of domains for the current day.

  """
  @abstractmethod
  def testNbDomains(self):
    pass

  """Checks the presence of a few known domains for a given date.

  """
  @abstractmethod
  def testDomains(self):
    pass

  """Subroutine to check that a given DGA generates certain domains on a given date.

  The DGA must at least generate the expected domains but can generate more of them.

  Args:
    dga: Domain generation algorithm.
    samples: Array with a date and an array of domains generated on that date.

  Returns:
    True if the DGA generates the expected domains.
  """
  def checkDomains(self, dga, samples):
    date = datetime.strptime(samples[0], "%d/%m/%Y")
    domains = dga.domainsFor(date)
    return set(samples[1]).issubset(set(domains))
