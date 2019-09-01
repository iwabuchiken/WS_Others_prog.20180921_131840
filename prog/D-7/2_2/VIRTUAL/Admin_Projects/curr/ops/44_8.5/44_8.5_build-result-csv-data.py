# -*- coding: utf-8 -*-
'''
file : C:\WORKS_2\WS\WS_Others.prog\prog\D-7\2_2\VIRTUAL\Admin_Projects\curr\ops\44_8.5\44_8.5_build-result-csv-data.py
orig : C:\WORKS_2\WS\WS_Others.prog\prog\D-7\2_2\VIRTUAL\Admin_Projects\curr\ops\44_9\44_9_renumbering_raw_csv_data.py
at : 2019/09/01 14:51:58

pushd C:\WORKS_2\WS\WS_Others.prog\prog\D-7\2_2\VIRTUAL\Admin_Projects\curr\ops\44_8.5\
python 44_8.5_build-result-csv-data.py

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

'''###################
    import : others
###################'''
#ref https://uxmilk.jp/39307 2019/09/01 15:22:25
# import urllib2
#ref https://teratail.com/questions/47744 2019/09/01 15:25:52
import urllib.request, urllib.error
#ref https://tonari-it.com/python-beautiful-soup-html-parse/#toc2
import bs4

'''###################
    vars : global
###################'''
SWITCH_DEBUG = True

###############################################
def show_Message() :
    
    msg = '''
    <Options>
    '''
    
    print (msg)

'''###################
    _build_result_csv_data__Dat_File()

    @return: lo_Order_Numbers

###################'''
def _build_result_csv_data__Dat_File():
    
    '''###################
        step : 1
            prep : vars
    ###################'''
    dpath_Dat_File = "C:\\Users\\iwabuchiken\\AppData\\Roaming\\MetaQuotes\\Terminal\\34B08C83A5AAE27A4079DE708E60511E\\MQL4\\Files\\Logs\\20190829_223434[eap-2.id-1].[EURJPY-1].dir"
    
    fname_Dat_File = "[eap-2.id-1].(20190829_223434).dat"
    
    fpath_Dat_File = os.path.join(dpath_Dat_File, fname_Dat_File)
    
    # lists
    lo_Order_Numbers = []
    
    '''###################
        step : 2
            read : file
    ###################'''
    '''###################
        step : 2 : 1
            open
    ###################'''
    f_in_Dat_File = open(fpath_Dat_File, "r")
    
    '''###################
        step : 2 : 2
            read
    ###################'''
    linesOf_Dat_File = f_in_Dat_File.readlines()

            # [2019.08.29 22:34:35 / lib_ea_2.mqh:249]    17307984    117.639    117.636    4    8    117.632    117.647    

    #debug
    if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
        
        # count
        cntOf_Lines = len(linesOf_Dat_File)
        
        msg = "[%s:%d] cntOf_Lines ==> %d" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                         , cntOf_Lines
                        )

        print()
        print(msg, file=sys.stderr)
        
    #/if SWITCH_DEBUG == True

    '''###################
        step : 3
            build list
    ###################'''
    for item in linesOf_Dat_File:
        '''###################
            step : 3 : 1
                split each line
        ###################'''
        tokens = item.split("\t")
        
        '''###################
            step : 3 : 2
                get : order number
        ###################'''
        tokeOf_Order_Number = tokens[1]
        
        # append
        lo_Order_Numbers.append(int(tokeOf_Order_Number))
        
    #/for item in linesOf_Dat_File:

    #debug
    if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
        
        msg = "[%s:%d] len(lo_Order_Numbers) ==> %d" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                         , len(lo_Order_Numbers)
                        )

        print()
        print(msg, file=sys.stderr)
        
        print(lo_Order_Numbers[0:10])
        
    #/if SWITCH_DEBUG == True

    
    '''###################
        step : 4
            file : close
    ###################'''
    f_in_Dat_File.close()
    
    #_20190901_150006:tmp
    #debug
    if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
        
        msg = "[%s:%d] file ==> closed : %s" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                         , fpath_Dat_File
                        )

        print()
        print(msg, file=sys.stderr)
        
    #/if SWITCH_DEBUG == True

    '''###################
        step : X
            return
    ###################'''
    return lo_Order_Numbers
    
#/ def build_result_csv_data():

'''###################
    _build_result_csv_data__Dat_File()

    @return: lo_Order_Numbers

###################'''
def _build_result_csv_data__Report_File():

#_20190901_151726:caller
#_20190901_151733:head
#_20190901_151746:wl

    '''###################
        step : 1
            prep : vars
    ###################'''
    dpath_Report_File = "C:\\Users\\iwabuchiken\\AppData\\Roaming\\MetaQuotes\\Terminal\\34B08C83A5AAE27A4079DE708E60511E\\MQL4\\Logs\\logs_trading"
    
    fname_Report_File = "DetailedStatement.[20190901_145309].htm"
    
    fpath_Report_File = os.path.join(dpath_Report_File, fname_Report_File)
    
    # lists
    lo_Orders = []
    
    # [ [tag_TR, lo_TDs], [], ...]
    lo_TR_and_TDs = []
    
    #
    lo_Orders_From_Report_File = []
    
    '''###################
        step : 2 : 1
            read : source file
    ###################'''
    f_in_Report_File = open(fpath_Report_File, "r")
    
    contentOf_Report_File = f_in_Report_File.read()

    '''###################
        step : 2 : 1.1
            source file : close
    ###################'''
    f_in_Report_File.close()
    
    '''###################
        step : 2 : 2
            read : as html
    ###################'''
    #ref https://tonari-it.com/python-beautiful-soup-html-parse/#toc2
    soup = bs4.BeautifulSoup(contentOf_Report_File, "html.parser")
    
    print()
    print(soup.title)

    '''###################
        step : 2 : 3
            read : TR tags
    ###################'''
    #ref https://tonari-it.com/python-html-tag-list-bs4/#toc5
    lo_TRs = soup.select("tr")

    #debug
    if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
        
        # count
        cntOf_LO_TRs = len(lo_TRs)
        
        msg = "[%s:%d] cntOf_LO_TRs ==> %d" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                         , cntOf_LO_TRs
                        )

        print()
        print(msg, file=sys.stderr)
        
    #/if SWITCH_DEBUG == True

    '''###################
        step : 2 : 4
            read : TD tags
    ###################'''
    for item in lo_TRs:
        
        '''###################
            step : 2 : 4.1
                select : TD tags
        ###################'''
        lo_TDs = item.select("td")
        
        '''###################
            step : 2 : 4.2
                append
        ###################'''
        lo_TR_and_TDs.append([item, lo_TDs])
        
    #/for item in lo_TRs:

    #debug
    if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
        
        # count
        cntOf_LO_TR_and_TDs = len(lo_TR_and_TDs)
        
        msg = "[%s:%d] cntOf_LO_TR_and_TDs ==> %d" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                         , cntOf_LO_TR_and_TDs
                        )

        print()
        print(msg, file=sys.stderr)
        
#         print(lo_TR_and_TDs[10])
        
    #/if SWITCH_DEBUG == True
    
    '''###################
        step : 2 : 5
            read : TD texts
    ###################'''
#     for item in lo_TR_and_TDs:
#     for item in lo_TR_and_TDs[:50] :
    for item in lo_TR_and_TDs[:20] :
         
        '''###################
            step : 2 : 5.1
                get : TDs
        ###################'''
        lo_TDs = item[1]
        
        '''###################
            step : 2 : 5.2
                get : texts
        ###################'''
        for item_2 in lo_TDs:

            '''###################
                step : 2 : 5.2 : 1
                    get : "title" attribute value
            ###################'''
            # get text
            textOf_TD_With_Title_Attribute = item_2.get("title")
#             textOf_TD = item_2.getText()

            '''###################
                step : 2 : 5.2 : 2
                    validate
            ###################'''
            if textOf_TD_With_Title_Attribute == None : #if textOf_TD == None
        
#                 #debug
#                 if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
#     
#                     msg = "[%s:%d] textOf_TD_With_Title_Attribute ==> none" % \
#                                     (os.path.basename(libs.thisfile()), libs.linenum()
#                                      
#                                     )
#              
#                     print(item_2)
#                     print(msg, file=sys.stderr)
#                      
#                 #/if SWITCH_DEBUG == True
                
                # continue
                continue
            
            #/if textOf_TD == None

            '''###################
                step : 2 : 5.2 : 3
                    if "My order" in the text ==> append
            ###################'''
           #_20190901_161624:next
           
            if "My order" in textOf_TD_With_Title_Attribute : #if "My order" in textOf_TD_With_Title_Attribute
                
                #_20190901_161249:tmp
                #debug
                if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
    
                    msg = "[%s:%d] My order ==> detected" % \
                                    (os.path.basename(libs.thisfile()), libs.linenum()
                                     
                                    )
             
                    print(item_2)
                    print(msg, file=sys.stderr)
                     
                #/if SWITCH_DEBUG == True
                
            #/if "My order" in textOf_TD_With_Title_Attribute



#             #debug
#             if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
# 
#                 msg = "[%s:%d] textOf_TD ==> %s" % \
#                                 (os.path.basename(libs.thisfile()), libs.linenum()
#                                  , textOf_TD
#                                 )
#          
#                 print()
#                 print(msg, file=sys.stderr)
#                  
#             #/if SWITCH_DEBUG == True
            
#             # 
#             #ref https://www.afternerd.com/blog/python-string-contains/
#             if "My order" in textOf_TD : #if "My order" in textoff
#                 
#                 #debug
#                 if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
# 
#                     msg = "[%s:%d] My order ==> detected" % \
#                                     (os.path.basename(libs.thisfile()), libs.linenum()
#                                      
#                                     )
#              
#                     print()
#                     print(msg, file=sys.stderr)
#                      
#                     print(item)
#                      
#                 #/if SWITCH_DEBUG == True
#             
#             #/if "My order" in textoff

            
#             #debug
#             if SWITCH_DEBUG == True : #if SWITCH_DEBUG == True
#                 
#                 # count
#                 cntOf_LO_TR_and_TDs = len(lo_TR_and_TDs)
#                 
#                 msg = "[%s:%d] cntOf_LO_TR_and_TDs ==> %d" % \
#                                 (os.path.basename(libs.thisfile()), libs.linenum()
#                                  , cntOf_LO_TR_and_TDs
#                                 )
#         
#                 print()
#                 print(msg, file=sys.stderr)
#                 
#                 print(lo_TR_and_TDs[10])
#                 
#             #/if SWITCH_DEBUG == True
            
            
        #/for item_2 in lo_TDs:

        
         
    #/for item in lo_TR_and_TDs:

    
    '''###################
        step : X
            return
    ###################'''
#     return lo_Orders
#/ def _build_result_csv_data__Report_File():


def build_result_csv_data():
    
    '''###################
        step : 1
            dat file
    ###################'''
    lo_Order_Numbers = _build_result_csv_data__Dat_File()
    
    '''###################
        step : 2
            file : report file
    ###################'''
    #_20190901_151726:caller
    lo_Order_Reports = _build_result_csv_data__Report_File()
    
    
#/ def build_result_csv_data():

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
#     test_1()
    build_result_csv_data()
    
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
