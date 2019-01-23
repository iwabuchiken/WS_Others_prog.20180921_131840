# -*- coding: utf-8 -*-
'''
file : C:\WORKS_2\WS\WS_Others.prog\prog\D-7\2_2\VIRTUAL\Admin_Projects\curr\ops\5.1\38-\1_1.py
orig : C:\WORKS_2\WS\WS_Others\prog\D-7\2_2\VIRTUAL\Admin_Projects\curr\ops\5.1\1_1.py
at : 2019/01/20 21:26:44

pushd C:\WORKS_2\WS\WS_Others.prog\prog\D-7\2_2\VIRTUAL
start_env
pushd C:\WORKS_2\WS\WS_Others.prog\prog\D-7\2_2\VIRTUAL\Admin_Projects\curr\ops\5.1\38-\
python 1_1.py

python 1_1.py dpath_Src_HTML="C:\\Users\\iwabuchiken\\AppData\\Roaming\\MetaQuotes\\Terminal\\B9B5D4C0EA7B43E1F3A680F94F757B3D\\MQL4\\Files\\Report_Trades" timestamp fname_Dst_CSV="trade.down-down-buy.(20190122_230530).(e-j,M1).csv"

    dpath_Src_HTML = "C:\\Users\\iwabuchiken\\AppData\\Roaming\\MetaQuotes\\Terminal\\B9B5D4C0EA7B43E1F3A680F94F757B3D\\MQL4\\Files\\Report_Trades"
    
    fname_Src_HTML = "DetailedStatement.(20190122_230530).(e-j,M1).htm"
#     fname_Src_HTML = "DetailedStatement.(20190117_231722).(e-j,M1).htm"

    dpath_Dst_CSV = "C:\\Users\\iwabuchiken\\AppData\\Roaming\\MetaQuotes\\Terminal\\B9B5D4C0EA7B43E1F3A680F94F757B3D\\MQL4\\Files\\Report_Trades"
    fname_Dst_CSV = "trade_log.(20190122_230530).(e-j,M1).csv"
    fname_Dst_CSV="trade.down-down-buy.(20190122_230530).(e-j,M1).csv"


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
import os, io
# #ref https://uguisu.skr.jp/Windows/python3.html
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8') #
# # sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8') #

'''###################
    import : discrete modules
###################'''
#ref https://shimi-dai.com/python-beautifulsoup4/
import lxml
from bs4 import BeautifulSoup


###############################################
def show_Message() :
    
    msg = '''
    <Options>
    -v	Volume down the amplitude --> 1.0 * v / 1000
    -f	Base frequency ---> e.g. 262 for the A tone
    -p	Phase of the sine curves ---> sin(2 * np.pi * f0 * n * phase / fs)'''
    
    print (msg)

#xxx
def _test_2__20190123_100239__CommandLine_Args():
    
    '''###################
        vars
    ###################'''
    #ref C:\Users\iwabuchiken\AppData\Roaming\MetaQuotes\Terminal\B9B5D4C0EA7B43E1F3A680F94F757B3D\MQL4\Files\Report_Trades
    dpath_Src_HTML = "C:\\Users\\iwabuchiken\\AppData\\Roaming\\MetaQuotes\\Terminal\\B9B5D4C0EA7B43E1F3A680F94F757B3D\\MQL4\\Files\\Report_Trades"
    
    fname_Src_HTML = "DetailedStatement.(20190122_230530).(e-j,M1).htm"
#     fname_Src_HTML = "DetailedStatement.(20190117_231722).(e-j,M1).htm"

    dpath_Dst_CSV = "C:\\Users\\iwabuchiken\\AppData\\Roaming\\MetaQuotes\\Terminal\\B9B5D4C0EA7B43E1F3A680F94F757B3D\\MQL4\\Files\\Report_Trades"
    fname_Dst_CSV = "trade_log.(20190122_230530).(e-j,M1).csv"

    #ddd
    '''###################
        get : command line args
            fname_Src_HTML
    ###################'''
    #ref https://www.tutorialspoint.com/python/python_command_line_arguments.htm
    lo_Args = sys.argv

    print()
    
    print("[%s:%d] lo_Args =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            ), file=sys.stdout)
    print(lo_Args)
    
    # arg for file name?
    for item in lo_Args[1:]:
                    
        # detection
        '''###################
            fname_Src_HTML
        ###################'''
        #ref https://www.tutorialspoint.com/python/string_startswith.htm
#         if item.startswith("filename=") : #if item.startswith("filename=")
        if item.startswith("fname_Src_HTML=") : #if item.startswith("filename=")
            # update : file name
            fname_Src_HTML = item.split("=")[1]

            print()
            
            print("[%s:%d] fname_Src_HTML => updated : %s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                     , fname_Src_HTML
                    ), file=sys.stdout)
    
    #/if item.startswith("filename=")
    
        '''###################
            dpath_Src_HTML
        ###################'''
        #ref https://www.tutorialspoint.com/python/string_startswith.htm
#         if item.startswith("filename=") : #if item.startswith("filename=")
        if item.startswith("dpath_Src_HTML=") : #if item.startswith("filename=")
            # update : file name
            dpath_Src_HTML = item.split("=")[1]

            print()
            
            print("[%s:%d] dpath_Src_HTML => updated : %s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                     , dpath_Src_HTML
                    ), file=sys.stdout)
    
        '''###################
            dpath_Dst_CSV
        ###################'''
        #ref https://www.tutorialspoint.com/python/string_startswith.htm
#         if item.startswith("filename=") : #if item.startswith("filename=")
        if item.startswith("dpath_Dst_CSV=") : #if item.startswith("filename=")
            # update : file name
            dpath_Dst_CSV = item.split("=")[1]

            print()
            
            print("[%s:%d] dpath_Dst_CSV => updated : %s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                     , dpath_Dst_CSV
                    ), file=sys.stdout)
            
        '''###################
            fname_Dst_CSV
        ###################'''
        #ref https://www.tutorialspoint.com/python/string_startswith.htm
#         if item.startswith("filename=") : #if item.startswith("filename=")
        if item.startswith("fname_Dst_CSV=") : #if item.startswith("filename=")
            # update : file name
            fname_Dst_CSV = item.split("=")[1]

            print()
            
            print("[%s:%d] fname_Dst_CSV => updated : %s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                     , fname_Dst_CSV
                    ), file=sys.stdout)
            
        '''###################
            add time stamp
        ###################'''
        #ref https://www.tutorialspoint.com/python/string_startswith.htm
        if item.startswith("timestamp") : #if item.startswith("filename=")
            # update : file name
            #ref https://stackoverflow.com/questions/541390/extracting-extension-from-filename-in-python#541394
            filetrunk, ext = os.path.splitext(fname_Dst_CSV)
            
            fname_Dst_CSV = "%s.%s%s" % (filetrunk, libs.get_TimeLabel_Now(), ext)

            print()
            
            print("[%s:%d] fname_Dst_CSV => updated : %s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                     , fname_Dst_CSV
                    ), file=sys.stdout)

        
        
    #/if item.startswith("filename=")
        
    #/for item in lo_Args[1:]:

    print()
    
    print("[%s:%d] source file info --------------\n" % \
            (os.path.basename(libs.thisfile()), libs.linenum()

            ), file=sys.stdout)
    
    print()
    
    print("fname_Src_HTML => %s\n" % \
            (fname_Src_HTML), file=sys.stdout)
    
    print("dpath_Src_HTML => %s\n" % \
            (dpath_Src_HTML), file=sys.stdout)
    
    '''###################
        return        
    ###################'''
    return (dpath_Src_HTML, fname_Src_HTML, dpath_Dst_CSV, fname_Dst_CSV)
#     return (dpath_Src_HTML, fname_Src_HTML)

#/def _test_2__20190123_100239__CommandLine_Args():    
'''###################
    _test_2__20190123_100239__Write_To_CSVFile
    
    @return: 
            0<    : file written (num of written lines)
            -1    : file not exist (source)
            -2    : file not exist (dst)
    
    @created : 20190123_105056
    
###################'''
def _test_2__20190123_100239__Write_To_CSVFile( \
        lo_File_Info, lo_TDs):
    
    '''###################
        get : file infos        
    ###################'''
    [dpath_Src_HTML, fname_Src_HTML, dpath_Dst_CSV, fname_Dst_CSV] = \
                lo_File_Info

    '''###################
        file : open
    ###################'''
    fpath_Src_Full = os.path.join(dpath_Src_HTML, fname_Src_HTML)
    fpath_Dst_Full = os.path.join(dpath_Dst_CSV, fname_Dst_CSV)

    print()
    
    print("[%s:%d] fpath_Dst_Full ===> '%s'\n" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
             , fpath_Dst_Full
            ), file=sys.stdout)
    
#     # validate : existence
#     #ref is file http://gesource.jp/programming/python/code/0008.html
#     if not os.path.isfile(fpath_Src_Full) : #if not os.path.isfile(fpath_Src_Full)
#         
#         # report
#         print()
#         print("[%s:%d] file(source) ---> not exist : '%s'" % \
#                         (os.path.basename(libs.thisfile()), libs.linenum()
#                          , fpath_Src_Full
#                         ), file=sys.stdout)
#         
#         return -1
#     
#     #/if not os.path.isfile(fpath_Src_Full)
#     
#     # file : dest
#     if not os.path.isfile(fpath_Dst_Full) : #if not os.path.isfile(fpath_Dst_Full)
#         
#         # report
#         print()
#         print("[%s:%d] file(dest) ---> not exist : '%s'" % \
#                         (os.path.basename(libs.thisfile()), libs.linenum()
#                          , fpath_Dst_Full
#                         ), file=sys.stdout)
#         
#         return -2
#     
#     #/if not os.path.isfile(fpath_Dst_Full)

    # open
    fout = open(fpath_Dst_Full, "w")
    
    '''###################
        file : write
    ###################'''
    '''###################
        file : write : meta info
    ###################'''
    fout.write("dpath_Src_HTML\t%s" % dpath_Src_HTML)
    fout.write("\n")
    fout.write("fname_Src_HTML\t%s" % fname_Src_HTML)
    fout.write("\n")
    
    fout.write("dpath_Dst_CSV\t%s" % dpath_Dst_CSV)
    fout.write("\n")
    fout.write("fname_Dst_CSV\t%s" % fname_Dst_CSV)
    fout.write("\n")
    
    '''###################
        file : write : TDs
    ###################'''
    for item in lo_TDs:
    
        # build line
        str_TD_Data = "\t".join(item)
        
        # write
        fout.write(str_TD_Data)
        fout.write("\n")
        
    #/for item in lo_TDs:

    '''###################
        file : close
    ###################'''
    fout.close()

    print()
    print("[%s:%d] file ---> written : '%s'" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                     , fpath_Dst_Full
                    ), file=sys.stdout)
    
    #ddd
    '''###################
        return
    ###################'''
    return True
        
#/def _test_2__20190123_100239__Write_To_CSVFile():
    
'''###################
    _test_2__20190123_100239__Collect_TDs
    
    @return: 
        list of TDs
        
    @created : 20190123_123256
    
###################'''
def _test_2__20190123_100239__Collect_TDs(soup):

    '''###################
        vars
    ###################'''
    cntOf_Debug = 0
    maxOf_CntOf_Debug = 10

    
    '''###################
        collect : TRs
    ###################'''
    # TRs
    lo_TRs = soup.find_all("tr")
#     lo_TRs = soup.find("tr")
    
    print()
    
    print("[%s:%d] len(lo_TRs) => %d" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
             , len(lo_TRs)
            ), file=sys.stdout)
    
    '''###################
        collect : TDs
    ###################'''
    # list of scraped TDs
    lo_TDs = []
    
    for TR in lo_TRs:

        '''###################
            step 1 : 
                collect tags : TDs
        ###################'''
        # find : TDs
        TDs = TR.find_all("td")
        
        # get : strings
        #ref replace https://orangain.hatenablog.com/entry/20100503/1272900555
        lo_TD_Strings = [x.string.replace('\xa0', ' ') for x in TDs]
#         lo_TD_Strings = [x.string for x in TDs]
        
        '''###################
            step : j1 :
                "Open Trades:" ?
        ###################'''
        if lo_TD_Strings[0] == "Open Trades:" : #if lo_TD_Strings[0] == 
        
            # report : break
            print()
            
            print("[%s:%d] lo_TD_Strings[0] (%d) => 'Open Trades:' ; breaking..." % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                     , cntOf_Debug
                    ), file=sys.stdout)
            print(lo_TD_Strings)
        
#             # report : last element in the list
#             print()
#             
#             print("[%s:%d]\nlo_TDs[-1] =>" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum()
#                     ), file=sys.stdout)
#             print("\t", lo_TDs[-1])
#                         # ['Closed P/L:', '-71 710']            
#                         
#             print("[%s:%d]\nlo_TDs[-2] =>" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum()
#                     ), file=sys.stdout)
#             print("\t", lo_TDs[-2])
#                         # ['\xa0', '0', '0', '0', '-71 710']            
#                         
#             print("[%s:%d]\nlo_TDs[-3] =>" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum()
#                     ), file=sys.stdout)
#             print("\t", lo_TDs[-3])
#                         #          ['5207241', '2019.01.22 16:01:00', 'sell', '0.10', 'eurjpy_', '124.118', '124.159', '124.05
#                         # 9', '2019.01.22 16:01:30', '124.059', '0', '0', '0', '590']
        
            # break
            break
        
        #/if lo_TD_Strings[0] == 
    
        '''###################
            append : TDs
        ###################'''
        # append
        lo_TDs.append(lo_TD_Strings)
        
        # counter
        cntOf_Debug += 1
         
        #/if cntOf_Debug > maxOf_CntOf_Debug
        
    #/for TR in lo_TRs:

    '''###################
        return
    ###################'''
    return lo_TDs

#/def _test_2__20190123_100239__Collect_TDs(soup):
    
def test_2__20190123_100239():

    print()
    print("[%s:%d] test_2 =======================" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()

                    ), file=sys.stdout)
    
    '''###################
        vars
    ###################'''
    (dpath_Src_HTML, fname_Src_HTML, dpath_Dst_CSV, fname_Dst_CSV) = \
                _test_2__20190123_100239__CommandLine_Args()
#     (dpath_Src_HTML, fname_Src_HTML) = _test_2__20190123_100239__CommandLine_Args()
    
    '''###################
        get : file
    ###################'''
    fin_HTML = open(os.path.join(dpath_Src_HTML, fname_Src_HTML), "r")
    
    lo_HTML_Lines = fin_HTML.read()
    
    fin_HTML.close()
    
    print()
    
    print("[%s:%d] Read HTML content => done" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            ), file=sys.stdout)
    
    '''###################
        load : html file
    ###################'''

    '''###################
        get : soup instance
    ###################'''
    soup = BeautifulSoup(lo_HTML_Lines, "lxml")
    
#     print()
#     
#     print("[%s:%d] soup => %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , type(soup)
#             ), file=sys.stdout)
#             #     soup => <class 'bs4.BeautifulSoup'>

    '''###################
        collect tags : TRs
    ###################'''
#     # TRs
#     lo_TRs = soup.find_all("tr")
# #     lo_TRs = soup.find("tr")
#     
#     print()
#     
#     print("[%s:%d] len(lo_TRs) => %d" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#              , len(lo_TRs)
#             ), file=sys.stdout)
    
#     print()
#     
#     print("[%s:%d] lo_TRs[0] =>" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#              
#             ), file=sys.stdout)
#             
#     print(lo_TRs[0])

    '''###################
        collect tags : TR > TDs
    ###################'''
#     cntOf_Debug = 0
#     maxOf_CntOf_Debug = 10
    
    # list of scraped TDs
    lo_TDs = _test_2__20190123_100239__Collect_TDs(soup)
    
#     # list of scraped TDs
#     lo_TDs = []
#     
#     for TR in lo_TRs:
# 
#         '''###################
#             step 1 : 
#                 collect tags : TDs
#         ###################'''
#         # find : TDs
#         TDs = TR.find_all("td")
#         
#         # get : strings
#         #ref replace https://orangain.hatenablog.com/entry/20100503/1272900555
#         lo_TD_Strings = [x.string.replace('\xa0', ' ') for x in TDs]
# #         lo_TD_Strings = [x.string for x in TDs]
#         
#         '''###################
#             step : j1 :
#                 "Open Trades:" ?
#         ###################'''
#         if lo_TD_Strings[0] == "Open Trades:" : #if lo_TD_Strings[0] == 
#         
#             # report : break
#             print()
#             
#             print("[%s:%d] lo_TD_Strings[0] (%d) => 'Open Trades:' ; breaking..." % \
#                     (os.path.basename(libs.thisfile()), libs.linenum()
#                      , cntOf_Debug
#                     ), file=sys.stdout)
#             print(lo_TD_Strings)
#         
#             # report : last element in the list
#             print()
#             
#             print("[%s:%d]\nlo_TDs[-1] =>" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum()
#                     ), file=sys.stdout)
#             print("\t", lo_TDs[-1])
#                         # ['Closed P/L:', '-71 710']            
#                         
#             print("[%s:%d]\nlo_TDs[-2] =>" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum()
#                     ), file=sys.stdout)
#             print("\t", lo_TDs[-2])
#                         # ['\xa0', '0', '0', '0', '-71 710']            
#                         
#             print("[%s:%d]\nlo_TDs[-3] =>" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum()
#                     ), file=sys.stdout)
#             print("\t", lo_TDs[-3])
#                         #          ['5207241', '2019.01.22 16:01:00', 'sell', '0.10', 'eurjpy_', '124.118', '124.159', '124.05
#                         # 9', '2019.01.22 16:01:30', '124.059', '0', '0', '0', '590']
#         
#             # break
#             break
#         
#         #/if lo_TD_Strings[0] == 
#     
#         '''###################
#             append : TDs
#         ###################'''
#         # append
#         lo_TDs.append(lo_TD_Strings)
#         
#         # counter
#         cntOf_Debug += 1
#          
#         #/if cntOf_Debug > maxOf_CntOf_Debug
#         
#     #/for TR in lo_TRs:

    '''###################
        report : TDs
    ###################'''
    print()
    
    print("[%s:%d] len(lo_TDs) => %d" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
             , len(lo_TDs)
            ), file=sys.stdout)

    '''###################
        TDs : write to file
    ###################'''
#     #ref C:\Users\iwabuchiken\AppData\Roaming\MetaQuotes\Terminal\B9B5D4C0EA7B43E1F3A680F94F757B3D\MQL4\Files\Report_Trades
#     dpath_Dst_CSV = "C:\\Users\\iwabuchiken\\AppData\\Roaming\\MetaQuotes\\Terminal\\B9B5D4C0EA7B43E1F3A680F94F757B3D\\MQL4\\Files\\Report_Trades"
#     
#     fname_Dst_CSV = "trade_log.(20190122_230530).(e-j,M1).csv"

    # write to file
    res = _test_2__20190123_100239__Write_To_CSVFile(
                [dpath_Src_HTML, fname_Src_HTML, dpath_Dst_CSV, fname_Dst_CSV]
                , lo_TDs
                )

    #ccc

    #debug
    return


#/def test_2__20190123_100239()

def test_1():

    print()
    print("[%s:%d] test_1 =======================" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()

                    ), file=sys.stdout)
    
    '''###################
        vars
    ###################'''
    #ref https://shimi-dai.com/python-beautifulsoup4/
    html_text = '''
    <html>
     <head>
      <title>The Dormouse''s story</title>
     </head>
     <body>
      <p class="title"><b>The Dormouse''s story</b></p>
      <p class="story">
       Once upon a time there were three little sisters; and their names were
       <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
       ,
       <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
       and
       <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
      </p>
     </body>
    </html>
    '''    
    
    #ref C:\Users\iwabuchiken\AppData\Roaming\MetaQuotes\Terminal\B9B5D4C0EA7B43E1F3A680F94F757B3D\MQL4\Files\Report_Trades
    dpath_Src_HTML = "C:\\Users\\iwabuchiken\\AppData\\Roaming\\MetaQuotes\\Terminal\\B9B5D4C0EA7B43E1F3A680F94F757B3D\\MQL4\\Files\\Report_Trades"
    
    fname_Src_HTML = "DetailedStatement.(20190117_231722).(e-j,M1).htm"
    
    '''###################
        get : command line args
    ###################'''
    #ref https://www.tutorialspoint.com/python/python_command_line_arguments.htm
    lo_Args = sys.argv

    print()
    
    print("[%s:%d] lo_Args =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            ), file=sys.stdout)
    print(lo_Args)
    
    # arg for file name?
    for item in lo_Args[1:]:
                    
        # detection
        #ref https://www.tutorialspoint.com/python/string_startswith.htm
        if item.startswith("filename=") : #if item.startswith("filename=")
            # update : file name
            fname_Src_HTML = item.split("=")[1]

            print()
            
            print("[%s:%d] fname_Src_HTML => updated : %s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                     , fname_Src_HTML
                    ), file=sys.stdout)
    
    #/if item.startswith("filename=")
        
    #/for item in lo_Args[1:]:

    print()
    
    print("[%s:%d] fname_Src_HTML => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , fname_Src_HTML
            ), file=sys.stdout)
            #     soup => <class 'bs4.BeautifulSoup'>
    
    '''###################
        get : file
    ###################'''
    fin_HTML = open(os.path.join(dpath_Src_HTML, fname_Src_HTML), "r")
    
    lo_HTML_Lines = fin_HTML.read()
    
    fin_HTML.close()
    
    print()
    
    print("[%s:%d] Read HTML content => done" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            ), file=sys.stdout)
            # <head>
            # <title>Statement: 1218411527 - iwabuchik2019</title>
            # <meta content="MetaQuotes Software Corp." name="generator"/>
            # <link href="https://www.metaquotes.net" rel="help"/>
            # <style media="screen" type="text/css">
            #     <!--
            #     td { font: 8pt Tahoma,Arial; }
            #     //-->
            #     </style>
            # <style media="print" type="text/css">
            #     <!--
            #     td { font: 7pt Tahoma,Arial; }
            #     //-->
            #     </style>
            # <style type="text/css">
            #     <!--
            #     .msdate { mso-number-format:"General Date"; }
            #     .mspt   { mso-number-format:\#\,\#\#0\.00;  }
            #     //-->
            #     </style>
            # </head>    
    
    '''###################
        load : html file
    ###################'''

    '''###################
        get : soup instance
    ###################'''
    soup = BeautifulSoup(lo_HTML_Lines, "lxml")
#     soup = BeautifulSoup(html_text, "lxml")
    
    print()
    
    print("[%s:%d] soup => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , type(soup)
            ), file=sys.stdout)
            #     soup => <class 'bs4.BeautifulSoup'>

#     print()
#     
#     print("[%s:%d] soup.find(\"title\")\n" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             ), file=sys.stdout)
#     
#     print(soup.find("title"))    
#             # <title>The Dormouse''s story</title>

#     print()
#     
#     print("[%s:%d] soup.find(\"a\", id=\"link3\")\n" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             ), file=sys.stdout)
#     
#     print(soup.find("a", id="link3"))
#             # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>    

#     print()
#     
#     print("[%s:%d] soup.html.head\n" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             ), file=sys.stdout)
# 
#     print(soup.html.head)
# 
#             # <head>
#             # <title>The Dormouse''s story</title>
#             # </head>

    print()
    
    print("[%s:%d] soup.html.head.title\n" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            ), file=sys.stdout)

    print(soup.html.head.title)
            # <title>The Dormouse''s story</title>

    '''###################
        collect tags : TRs
    ###################'''
    # TRs
    lo_TRs = soup.find_all("tr")
#     lo_TRs = soup.find("tr")
    
    print()
    
    print("[%s:%d] len(lo_TRs) => %d" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
             , len(lo_TRs)
            ), file=sys.stdout)
    
    print()
    
#     print("[%s:%d] lo_TRs =>" % \
    print("[%s:%d] lo_TRs[0] =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
             
            ), file=sys.stdout)
            
    print(lo_TRs[0])
#     print(lo_TRs)

    index = 4
#     index = 3
    
    print()
    
    print("[%s:%d] lo_TRs[%d] =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
             , index
            ), file=sys.stdout)
            
    print(lo_TRs[index])

    '''###################
        collect tags : TR > TDs
    ###################'''
    soup_TRs_1 = lo_TRs[index]
    
    print()
    
    print("[%s:%d] type(soup_TRs_1) => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
             , type(soup_TRs_1)
            ), file=sys.stdout)
            # [1_1.py:267] type(str_New_HTML) => <class 'bs4.element.Tag'>
            
    #soup = BeautifulSoup(lo_HTML_Lines, "lxml")
#     soup_TR_1_TDs = BeautifulSoup(lo_TRs[index], "lxml")
            # TypeError: 'NoneType' object is not callable    
            
    soup_TR_1_TDs = soup_TRs_1.find_all("td")
#     soup_TR_1_TDs = lo_TRs.find_all("td")
#     soup_TR_1_TDs = soup.find_all("td")

    print()
    
    print("[%s:%d] len(soup_TR_1_TDs) => %d" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
             , len(soup_TR_1_TDs)
            ), file=sys.stdout)

    print(soup_TR_1_TDs)    
            #   File "1_1.py", line 285, in test_1
            #     print(soup_TR_1_TDs)
            # UnicodeEncodeError: 'cp932' codec can't encode character '\xa0' in position 72648: illegal multibyte
            #  sequence
            
            # [1_1.py:286] len(soup_TR_1_TDs) => 5
            # [<td title="1218411527">4460746</td>, <td class="msdate" nowrap="">2019.01.08 07:41:19</td>, <td>bal
            # ance</td>, <td align="left" colspan="10">1218411527</td>, <td class="mspt">10 000 000</td>]    

    # show tds
    for item in soup_TR_1_TDs:
            
        # print : td
        print(item)
        
        # print : string
        print("\t\t==>", item.string)
        
    #/for item in soup_TR_1_TDs:
            # <td title="#10001 ">4473128</td>
            #                 ==> 4473128
            # <td class="msdate" nowrap="">2019.01.14 05:03:01</td>
            #                 ==> 2019.01.14 05:03:01
            # <td>buy</td>
            #                 ==> buy
            # <td class="mspt">0.10</td>
            #                 ==> 0.10
            # <td>eurjpy_</td>
            #                 ==> eurjpy_
            # <td style="mso-number-format:0\.000;">124.088</td>
            #                 ==> 124.088
            # <td style="mso-number-format:0\.000;">0.000</td>
            #                 ==> 0.000
            # <td style="mso-number-format:0\.000;">0.000</td>
            #                 ==> 0.000
            # <td class="msdate" nowrap="">2019.01.14 05:36:04</td>
            #                 ==> 2019.01.14 05:36:04
            # <td style="mso-number-format:0\.000;">123.981</td>
            #                 ==> 123.981
            # <td class="mspt">0</td>
            #                 ==> 0
            # <td class="mspt">0</td>
            #                 ==> 0
            # <td class="mspt">0</td>
            #                 ==> 0
            # <td class="mspt">-1 070</td>
            #                 ==> -1 070

#     @_20190122_140536

#/ def test_1():

def exec_prog():
    
    '''###################
        ops        
    ###################'''
    test_2__20190123_100239()
#     test_1()
    
    print("[%s:%d] exec_prog() => done" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    
#def exec_prog()

'''
<usage>
'''
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
