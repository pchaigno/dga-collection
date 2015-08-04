#!/usr/bin/env python3
import unittest
from datetime import datetime, timedelta

from Cryptolocker import Cryptolocker
from Torpig import Torpig
from ZeusBot import ZeusBot
from Necurs import Necurs
from Symmi import Symmi


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
cryptolocker_domains = ['19/12/2013', 
                          ['sljjjupfgagolpg.ru', 'vxagtvsyqxtrfcm.com',
                           'wxphewjnfhlyyjj.net', 'xckjffnjivafxen.biz']]
necurs_domains = ['19/02/2015', 
                  ['boymlujtgp.nu', 'ybynentfsjvmsgtktcoog.im', 'oiijxplrnmvgskxwaye.ru', 
                  'imgirmyddbsniuh.pw', 'ultrttvbvjaanrj.jp', 'porgtemsbycy.ki']]
symmi_domains = ['20/12/2015', 
                  ['veeswaehsisa.ddns.net', 'uhbacoinm.ddns.net', 'baugkoosdui.ddns.net']]


"""Performs a few unit tests on the DGA classes.

"""
class TestDGAs(unittest.TestCase):

  """Checks that couldUseDomain returns True for correct domains.

  """
  def testCouldUseDomain(self):
    self.assertTrue(Torpig.couldUseDomain('dhidxguag.biz'))
    self.assertTrue(ZeusBot.couldUseDomain('zrtokdghbcdgkijfcxvbh.com'))
    self.assertTrue(Cryptolocker.couldUseDomain('gfrtgcfgvopvgg.co.uk'))
    self.assertTrue(Necurs.couldUseDomain('ultrttvbvjaanrj.jp'))
    self.assertTrue(Symmi.couldUseDomain('baugkoosdui.ddns.net'))

  """Checks the lifetime value of domains for each DGA.

  """
  def testDomainLifetime(self):
    self.assertEqual(86400, Torpig.domainsLifetime())
    self.assertEqual(7 * 86400, ZeusBot.domainsLifetime())
    self.assertEqual(86400, Cryptolocker.domainsLifetime())
    self.assertEqual(4 * 86400, Necurs.domainsLifetime())
    self.assertEqual(16 * 86400, Symmi.domainsLifetime())

  """Checks that each DGA returns the expected number of domains for the current day.

  """
  def testNbDomains(self):
    self.assertEqual(3, len(Torpig.domains()))
    self.assertEqual(1000, len(ZeusBot.domains()))
    self.assertEqual(1000, len(Cryptolocker.domains()))
    self.assertEqual(2048, len(Necurs.domains()))
    self.assertEqual(64, len(Symmi.domains()))

  """Checks the presence of a few known domains for a given date.

  """
  def testDomains(self):

    """Subroutine to check that a given DGA generates certain domains on a given date.

    The DGA must at least generate the expected domains but can generate more of them.

    Args:
      dga: Domain generation algorithm.
      samples: Array with a date and an array of domains generated on that date.

    Returns:
      True if the DGA generates the expected domains.
    """
    def checkDomains(dga, samples):
      date = datetime.strptime(samples[0], "%d/%m/%Y")
      domains = dga.domainsFor(date)
      return set(samples[1]).issubset(set(domains))

    self.assertTrue(checkDomains(Cryptolocker, cryptolocker_domains))
    self.assertTrue(checkDomains(ZeusBot, zeusbot_domains))
    self.assertTrue(checkDomains(Necurs, necurs_domains))
    self.assertTrue(checkDomains(Symmi, symmi_domains))


if __name__ == '__main__':
  unittest.main()
