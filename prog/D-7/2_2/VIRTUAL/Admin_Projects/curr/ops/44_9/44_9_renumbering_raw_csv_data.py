# -*- coding: utf-8 -*-
'''
file : C:\WORKS_2\WS\WS_Others.prog\prog\D-7\2_2\VIRTUAL\Admin_Projects\curr\ops\44_9\44_9_renumbering_raw_csv_data.py
orig : C:\WORKS_2\WS\WS_Others\prog\D-7\2_2\VIRTUAL\Admin_Projects\curr\ops\5.1\1_1.py
at : 2019/03/07 09:56:36

pushd C:\WORKS_2\WS\WS_Others.prog\prog\D-7\2_2\VIRTUAL\Admin_Projects\curr\ops\44_9\
python 44_9_renumbering_raw_csv_data.py

'''
###############################################
import sys
from _datetime import datetime
from numpy import append

'''###################
    import : original files        
###################'''
sys.path.append('.')
sys.path.append('..')

sys.path.append('C:/WORKS_2/WS/WS_Others/prog/D-7/2_2/VIRTUAL/Admin_Projects')
# sys.path.append('C:/WORKS_2/WS/WS_Others/prog/D-7/2_2/VIRTUAL/Admin_Projects/mm')

from mm.libs_mm import cons_mm, cons_fx, libs, libfx

'''###################
    import : built-in modules        
###################'''
import os

###############################################
def show_Message() :
    
    msg = '''
    <Options>
    '''
    
    print (msg)

def test_1():

    '''###################
        get : args
    ###################'''
    
    '''###################
        file path
    ###################'''
    #_20190307_144837
    dpath_CSV = "C:\\WORKS_2\\WS\\WS_Others.prog\\prog\\D-7\\2_2\\VIRTUAL\\Admin_Projects\\curr\\data\\csv_raw"
    
    if len(sys.argv) > 1 : #if len(sys.argv)
    
        fname_CSV = sys.argv[1]
    
    else : #if len(sys.argv)
    
        fname_CSV = "44_5.1_10_rawdata.(EURJPY).(Period-D1).(NumOfUnits-2000)"\
                    + ".(Bars-ALL).20190308_083617.csv"
    #     fname_CSV = "44_5.1_10_rawdata.(EURJPY).(Period-M15).(NumOfUnits-4500)"\
    #                 + ".(Bars-ALL).20190214_095445.csv"
    
    #/if len(sys.argv)
    
    
    
    
    fpath_CSV = os.path.join(dpath_CSV, fname_CSV)
    
    # validate
    if not os.path.isfile(fpath_CSV) : #if not os.path.isfile(fpath_CSV)
        
        print()
        print("[%s:%d] csv file NOT exist : %s" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
    
                        ), file=sys.stderr)
        
        return
    
    #/if not os.path.isfile(fpath_CSV)

    '''###################
        file : open
    ###################'''
    f_in_CSV = open(fpath_CSV, "r")
    
    
    '''###################
        read file content
    ###################'''
    data = f_in_CSV.readlines()
    
    print("[%s:%d] len(data) = %d" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , len(data)
            ), file=sys.stderr)
    
    '''###################
        file : close
    ###################'''
    f_in_CSV.close()

    '''###################
        op : renumbering
    ###################'''
    '''###################
        step : A : 1
            prep
    ###################'''
    lo_New_CSV_Lines = []
    
    cntOf_Lines = 1
    
    lenOf_Lines = len(data)
    
    # file path
    #_20190307_144916
    dpath_CSV_Dst = dpath_CSV
#     dpath_CSV_Dst = "C:\\WORKS_2\\WS\\WS_Others.prog\\prog\\D-7\\2_2\\VIRTUAL\\Admin_Projects\\curr\\data\\csv_raw"
    
    # E/J, H1
    # build : fname
    # 44_5.1_10_rawdata.(EURJPY).(Period-D1).(NumOfUnits-2000).(Bars-ALL).20190308_083617.csv
#     tokens = fname_CSV.split(".")
    
    fname_CSV_Dst = fname_CSV.replace("Bars-ALL", "Bars-ALL-%s" % libs.get_TimeLabel_Now())
#     fname_CSV_Dst = "44_5.1_10_rawdata.(EURJPY).(Period-H1).(NumOfUnits-4500)"
#     fname_CSV_Dst += ".(Bars-ALL-%s).20190307_144106.csv" % libs.get_TimeLabel_Now()
    
#     # E/J, M15
#     fname_CSV_Dst = "44_5.1_10_rawdata.(EURJPY).(Period-M15).(NumOfUnits-4500)"
#     fname_CSV_Dst += ".(Bars-ALL-%s).20190214_095445" % libs.get_TimeLabel_Now()
                   
#     fname_CSV_Dst += ".csv"
#     fname_CSV_Dst += ".(tmp-%s).csv" % libs.get_TimeLabel_Now()
    
    fpath_CSV_Dst = os.path.join(dpath_CSV_Dst, fname_CSV_Dst)
    
    '''###################
        step : A : 2.1
            read : header
    ###################'''
    lo_New_CSV_Lines.append(data[0])
    lo_New_CSV_Lines.append(data[1])
    
    '''###################
        step : A : 2.2
            read : body
    ###################'''
    # iteration
    for i in range(2, lenOf_Lines):
    
        # split
        tokens = data[i].split(";")
        
        # renumbering
        tokens[0] = str(cntOf_Lines)
#         tokens[0] = cntOf_Lines
        
        # counter
        cntOf_Lines += 1
        
        # append
        lo_New_CSV_Lines.append(";".join(tokens))
        
    #/for i in range(2, lenOf_Lines):
    
    #debug
    print()
    print("[%s:%d] lo_New_CSV_Lines[0] = %s, lo_New_CSV_Lines[-1] = %s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                     , lo_New_CSV_Lines[0]
                     , lo_New_CSV_Lines[-1]
                    ), file=sys.stderr)

    #ccc
    
#     for line in data:
#     
#         tokens = line.split(";")
#         
#         
#         
#     #/for line in data:

    
    '''###################
        step : A : 3.1
            file : open
    ###################'''
    f_out_CSV = open(fpath_CSV_Dst, "w")
    

    '''###################
        step : A : 3.2
            file : write
    ###################'''
    f_out_CSV.write("".join(lo_New_CSV_Lines))
#     f_out_CSV.write("\n".join(lo_New_CSV_Lines))
 
    '''###################
        step : A : 3.3
            file : close
    ###################'''
    f_out_CSV.close()

    #debug
    print()
    print("[%s:%d] file written ==> %s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                     , fpath_CSV_Dst
                    ), file=sys.stderr)
    
    '''###################
        extract target tokesn from each line
    ###################'''
    
    '''###################
        report
    ###################'''
    '''###################
        message
    ###################'''
    print()
    print("[%s:%d] test_1 =======================" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()

                    ), file=sys.stderr)
#/ def test_1():

def exec_prog():
    
    '''###################
        ops        
    ###################'''
    test_1()
    
    print("[%s:%d] exec_prog() => done" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    
#def exec_prog()

if __name__ == "__main__" :

    '''###################
    	validate : help option		
    ###################'''

    '''###################
    	get options		
    ###################'''

    '''###################
    	evecute		
    ###################'''
    exec_prog()

    print()
    
    print("[%s:%d] done" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
#     print "[%s:%d] done" % (thisfile(), linenum())
