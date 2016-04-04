# DGA Collection

[![Build Status](https://travis-ci.org/pchaigno/dga-collection.svg?branch=master)](https://travis-ci.org/pchaigno/dga-collection)
[![Coverage Status](https://coveralls.io/repos/github/pchaigno/dga-collection/badge.svg?branch=master)](https://coveralls.io/github/pchaigno/dga-collection?branch=master)

A collection of known [Domain Generation Algorithms](https://en.wikipedia.org/wiki/Domain_generation_algorithm):
- [Torpig](https://seclab.cs.ucsb.edu/media/uploads/papers/torpig.pdf)
- [ZeusBot](http://vrt-blog.snort.org/2014/03/decoding-domain-generation-algorithms.html)
- [Cryptolocker](https://blog.fortinet.com/post/a-closer-look-at-cryptolocker-s-dga)
- [Necurs](http://www.johannesbader.ch/2015/02/the-dgas-of-necurs/)
- [Symmi](http://www.johannesbader.ch/2015/01/the-dga-of-symmi/)
- [Ranbyus](http://www.johannesbader.ch/2015/05/the-dga-of-ranbyus/)


## Usage

For each DGA, the list of domains can be easily generated:
```python
from datetime import date
from Necurs import Necurs

# Compute domains for the current day/period:
Necurs.domains()

# Compute domains for a given date:
Necurs.domainsFor(date(2015, 1, 20))
```

The `couldUseDomain` method can also prove useful to help classify domains:
```python
Necurs.couldUseDomain('thislabelcontainsaz.biz')
# => False

Necurs.couldUseDomain('boymlujtgp.nu')
# => True
```


## Contributing

Please see [`CONTRIBUTING.md`](CONTRIBUTING.md) for instructions on how to add a new DGA.


## License

This project is under [MIT license](LICENSE).

It uses results from reverse-engineering analyses published on various blogs including:
- [Johannes Bader's blog](http://www.johannesbader.ch)
- [VRT blog](http://vrt-blog.snort.org)
- [Fortinet blog](https://blog.fortinet.com)
