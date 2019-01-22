# -*- coding: utf-8 -*-
'''
file : C:\WORKS_2\WS\WS_Others.prog\prog\D-7\2_2\VIRTUAL\Admin_Projects\curr\ops\5.1\38-\1_1.py
orig : C:\WORKS_2\WS\WS_Others\prog\D-7\2_2\VIRTUAL\Admin_Projects\curr\ops\5.1\1_1.py
at : 2019/01/20 21:26:44

pushd C:\WORKS_2\WS\WS_Others.prog\prog\D-7\2_2\VIRTUAL
start_env
pushd C:\WORKS_2\WS\WS_Others.prog\prog\D-7\2_2\VIRTUAL\Admin_Projects\curr\ops\5.1\38-\
python 1_1.py

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
#ref https://uguisu.skr.jp/Windows/python3.html
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8') #
# sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8') #

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

#     ccc

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
