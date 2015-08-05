# Contributing

Any pull request to fix an issue or add a new DGA is welcome!

## Adding a new DGA class

See [`Torpig.py`](Torpig.py) for an example. Read [`DGAMalware.py`](DGAMalware.py) for details on each method to implement.

0. Create a new class `MyDGA` extending `DGAMalware`.
0. Add the source of the DGA in comment (link, author and date).
0. Define `domainsFor(self, date)` and `couldUseDomain(self, domain)`.
0. Define `domainsLifetime(self)` if the default lifetime is not of one day.
0. Add tests for the new DGA in [`test.py`](test.py).
0. Run the tests and open a pull request.
0. *Et voilà !*


## Adding a new DGA script

If you don't want to implement the Python class for the DGA you can also add the script in the [`sources`](sources/) directory and we will take care of the rest.
Please make sure to include the source (link, author and date) of the script in comment.


## Tests

Tests can be run with any version of Python >= 3.

```
$ ./test.py
....
----------------------------------------------------------------------
Ran 4 tests in 6.427s

OK
```

Please make sure you test any changes before opening a pull request.
