from test.test_dga import TestDGA
from dgacollection.ZeusBot import ZeusBot
from unittest import TestCase


"""Examples of domains.

Usually found with the reverse engineering analysis.

"""
zeusbot_domains = ['31/01/2014', 
                  ['kbbtstweabiwoblruspxkqo.com', 'gitlvseiypdqhkrhajltsfejnvc.ru', 
                  'orhztukmjmfgumdayltkamovnbuc.info', 'txokrdqgojropeixcingdwg.org', 
                  'tkugtwhuoxwypqktdedqlbeae.biz', 'pveizqseuwoirojgiscgezlbnzsxs.com',
                  'hvctguthqpzecmonaqxekbcp.ru', 'qkdmfqpjtceidlvuolyttwdm.com',
                  'wkfirgqomtcudyeulfrsydrkj.net', 'rhexgwoxoaiprdibuxwwtyhst.biz',
                  'tkzlaibqdamzinqcifdbuhidxhq.info']]


"""Performs a few unit tests on the ZeusBot DGA.

"""
class TestZeusBot(TestDGA, TestCase):

  """Checks that couldUseDomain returns True for correct domains.

  """
  def testCouldUseDomain(self):
    self.assertTrue(ZeusBot.couldUseDomain('zrtokdghbcdgkijfcxvbh.com'))

  """Checks the lifetime value of domains for each DGA.

  """
  def testDomainLifetime(self):
    self.assertEqual(7 * 86400, ZeusBot.domainsLifetime())

  """Checks that each DGA returns the expected number of domains for the current day.

  """
  def testNbDomains(self):
    self.assertEqual(1000, len(ZeusBot.domains()))

  """Checks the presence of a few known domains for a given date.

  """
  def testDomains(self):
    self.assertTrue(self.checkDomains(ZeusBot, zeusbot_domains))
