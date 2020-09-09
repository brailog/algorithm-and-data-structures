# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 21:01:07 2018

@author: grro
"""

import cProfile

def profilefunc(func):
    def _wrapper(*args, **kwargs):
        prof = cProfile.Profile()
        retval = prof.runcall(func, *args, **kwargs)
        prof.print_stats()
        return retval
    return _wrapper