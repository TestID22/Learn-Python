#!/usr/bin/env python
# -*- coding: utf-8 -*-
from initdata import fsociety
import pickle

dbfile = open('people-pickle','wb')
pickle.dump(fsociety, dbfile)
dbfile.close()