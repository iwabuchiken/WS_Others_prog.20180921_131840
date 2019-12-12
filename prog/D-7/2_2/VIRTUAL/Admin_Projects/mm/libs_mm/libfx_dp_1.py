            
'''###################
    file : C:\WORKS_2\WS\WS_Others.prog\prog\D-7\2_2\VIRTUAL\Admin_Projects\mm\libs_mm\libfx_dp_1.py
    copy source : 
    
    at: 2019/12/11 13:52:08
    
###################'''
# from sympy.solvers.tests.test_constantsimp import C1
# from numpy.distutils.from_template import item_re
from copy import deepcopy

'''###################
    import : django        
###################'''
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django import template
#ref https://stackoverflow.com/questions/29304845/how-to-disable-cache-in-django-view
from django.views.decorators.cache import never_cache

'''###################
    import : VIRTUALENV        
###################'''

'''###################
    import : original files        
###################'''
import sys
sys.path.append('.')
sys.path.append('..')
# sys.path.append('C:/WORKS_2/WS/WS_Others/free/fx/82_')
# 
# sys.path.append('C:/WORKS_2/WS/WS_Others/free/VX7GLZ_science-research/31_Materials')
sys.path.append('C:/WORKS_2/WS/WS_Others/prog/D-7/2_2/VIRTUAL/Admin_Projects/mm')

from mm.libs_mm import cons_mm, cons_fx, libs, libfx, libfx_7
# from mm.libs_mm import libs
# from mm.libs_mm import libfx



from Admin_Projects.definitions import ROOT_DIR
from Admin_Projects.definitions import DPATH_ROOT_CURR

'''###################
    import : built-in modules        
###################'''
import os
#ref https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
from os import listdir
from os.path import isfile, join, splitext

import subprocess, copy, time, glob, re, datetime, math, traceback
# import subprocess, copy, time, glob, re, datetime, math

'''###################
    import : user-installed
###################'''
#ref pyplot https://matplotlib.org/users/pyplot_tutorial.html
import numpy, matplotlib.pyplot as plt

'''###################
    vars : global
###################'''

'''######################################
    funcs        
######################################'''
'''###################
    dp_1_Trend_Down

    at : 2019/12/11 13:52:16
    
    orig : 
    
    @param : 
    
    @return: 
    
###################'''
def dp_1_Trend_Down(\
          _lo_LO_Lines, _lo_BDs_Tmp
          , _typeOf_DP
          , _index_start
          , numOf_Target_Bars = 4
          ):
#_20191211_130902:caller
#_20191211_130909:head
#_20191211_130914:wl:in-func
    
    '''###################
        step : 0 : 1
            prep : unpack : lines
    ###################'''
    (lo_Lines_Log, lo_Lines_Dat, lo_Lines_Error) = _lo_LO_Lines

    '''###################
        step : 0 : 2
            prep : vars
    ###################'''
    valOf_Ret = False
    
    '''###################
        step : 0 : 3
            log
    ###################'''
    #_20191110_142858:caller
#     flg_commandline_ouput = SWITCH_COMMANDLINE_OUTPUT
    flg_commandline_ouput = cons_fx.Flags.SWITCH_COMMANDLINE_OUTPUT.value
    
    tmp_msg = "dp_1_Trend_Down ==> starting..."
    
    libfx_7.output_Log(os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
         , tmp_msg, lo_Lines_Log, flg_commandline_ouput)
    
    '''###################
        step : 1
            get : 4 bars
    ###################'''
    #_20191211_135133:next
    e0 = _lo_BDs_Tmp[_index_start - 0]
    e1 = _lo_BDs_Tmp[_index_start - 1]
    e2 = _lo_BDs_Tmp[_index_start - 2]
    e3 = _lo_BDs_Tmp[_index_start - 3]
    
    '''###################
        step : 2
            get : lower price
    ###################'''
    pr_Bottom_0 = e0.price_Close if (e0.price_Close < e0.price_Open) else e0.price_Open
    pr_Bottom_1 = e1.price_Close if (e1.price_Close < e1.price_Open) else e1.price_Open
    pr_Bottom_2 = e2.price_Close if (e2.price_Close < e2.price_Open) else e2.price_Open
    pr_Bottom_3 = e3.price_Close if (e3.price_Close < e3.price_Open) else e3.price_Open

    '''###################
        step : j1
            judge : trend down ?
    ###################'''
    '''###################
        step : j1 : 1
            conditions
    ###################'''
    cond_1 = (
              (pr_Bottom_0 < pr_Bottom_1) \
            and  (pr_Bottom_1 < pr_Bottom_2) \
            and (pr_Bottom_2 < pr_Bottom_3)
            )
    
    '''###################
        step : j1 : 2
            judge
    ###################'''
    if cond_1 == True : #if cond_1 == True
        '''###################
            step : j1 : Y
                judge : trend down
        ###################'''
        '''###################
            step : j1 : Y : 1
                log
        ###################'''
        #_20191110_142858:caller
        flg_commandline_ouput = cons_fx.Flags.SWITCH_COMMANDLINE_OUTPUT.value
        
        tmp_msg = "(step : 3 : 2) judge : trend down ==> True (cond_1 = %s)" % (cond_1)
        
        libfx_7.output_Log(os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
             , tmp_msg, lo_Lines_Log, flg_commandline_ouput)
        
        '''###################
            step : j1 : Y : 2
                set : vals
        ###################'''
        valOf_Ret = True
    
    else : #if cond_1 == True
        '''###################
            step : j1 : N
                judge : trend NOT down
        ###################'''
    
        '''###################
            step : j1 : N : 1
                log
        ###################'''
        #_20191110_142858:caller
        flg_commandline_ouput = cons_fx.Flags.SWITCH_COMMANDLINE_OUTPUT.value
        
        tmp_msg = "(step : 3 : 2) judge : trend down ==> False (cond_1 = %s)" % (cond_1)
        
        libfx_7.output_Log(os.path.basename(libs.thisfile()), libs.linenum(), libs.get_TimeLabel_Now()
             , tmp_msg, lo_Lines_Log, flg_commandline_ouput)
        
        '''###################
            step : j1 : N : 2
                set : vals
        ###################'''
        valOf_Ret = False
    
    #/if cond_1 == True
    
    
    
    '''###################
        step : X : 1
            return
    ###################'''
    '''###################
        step : X : 1.1
            return values
    ###################'''
#     ret = False
#     ret = True
    ret = valOf_Ret
    
    '''###################
        step : X : 1.2
            return
    ###################'''
    return ret
    
#/ def dp_1_Trend_Down( lo_LO_Lines, lo_BDs_Tmp, _index_start:int, numOf_Target_Bars = 4):

