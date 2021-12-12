#!/usr/bin/env python3


import sys
sys.path.append("..")
import classes.class_example as ex

#if module import is not done in the root direcotry, common root directory to import module and importing module 
# will have to be added to the bath like above

e = ex.Employee("Test Name", 500)
CountObj = ex.JustCounterClass()

