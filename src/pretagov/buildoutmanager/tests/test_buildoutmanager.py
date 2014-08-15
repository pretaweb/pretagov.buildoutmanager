

import unittest
import doctest

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocFileSuite("test.txt"))
    return tests