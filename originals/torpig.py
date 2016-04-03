#!/usr/bin/env python
# Source:
# Your Botnet is My Botnet: Analysis of a Botnet Takeover
# Stone-Gross Brett, Cova Marco, Cavallaro Lorenzo, Gilbert Bob,
# Szydlowski Martin, Kemmerer Richard, Kruegel Christopher and Vigna, Giovanni
# 2009
import datetime

suffix = ["anj", "ebf", "arm", "pra", "aym", "unj", "ulj", "uag", "esp", "kot", "onv", "edc"]

def generate_daily_domain():
	t = datetime.date.today()
	p = 8
	return generate_domain(t, p)

def scramble_date(t, p):
	return (((t.month ^ t.day) + t.day) * p) + t.day + t.year

def generate_domain(t, p):
	if t.year < 2007:
		t.year = 2007
	s = scramble_date(t, p)
	c1 = (((t.year >> 2) & 0x3fc0) + s) % 25 + ord('a')
	c2 = (t.month + s) % 10 + ord('a')
	c3 = ((t.year & 0xff) + s) % 25 + ord('a')
	if t.day * 2 < '0' or t.day * 2 < ord('9'):
		c4 = (t.day * 2) % 25 + ord('a')
	else:
		c4 = t.day % 10 + ord('1')
	return chr(c1) + 'h' + chr(c2) + chr(c3) + 'x' + chr(c4) + suffix[t.month - 1]

print generate_daily_domain()