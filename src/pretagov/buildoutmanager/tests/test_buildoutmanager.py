

import unittest
import doctest

import os
import tempfile
import shutil

def setUp(t):
	t.bm_cwd = os.getcwd()
	t.bm_wd = tempfile.mkdtemp()
	os.chdir(t.bm_wd)

def tearDown(t):
	os.chdir(t.bm_cwd)
	shutil.rmtree(t.bm_wd)
	del t.bm_cwd
	del t.bm_wd


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocFileSuite("test.txt", globs={'os': os, 'tempfile': tempfile},
    	setUp=setUp, tearDown=tearDown))
    return tests