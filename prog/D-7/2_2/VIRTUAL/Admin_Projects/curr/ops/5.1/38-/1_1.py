# -*- coding: utf-8 -*-
'''
file : C:\WORKS_2\WS\WS_Others.prog\prog\D-7\2_2\VIRTUAL\Admin_Projects\curr\ops\5.1\38-\1_1.py
orig : C:\WORKS_2\WS\WS_Others\prog\D-7\2_2\VIRTUAL\Admin_Projects\curr\ops\5.1\1_1.py
at : 2019/01/20 21:26:44

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
import os

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

                    ), file=sys.stderr)

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
    
    '''###################
        get : soup instance
    ###################'''
    soup = BeautifulSoup(html_text, "lxml")
    
    print()
    
    print("[%s:%d] soup => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , type(soup)
            ), file=sys.stderr)
            #     soup => <class 'bs4.BeautifulSoup'>

    print()
    
    print("[%s:%d] soup.find(\"title\")\n" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            ), file=sys.stderr)
    
    print(soup.find("title"))    
            # <title>The Dormouse''s story</title>

    print()
    
    print("[%s:%d] soup.find(\"a\", id=\"link3\")\n" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            ), file=sys.stderr)
    
    print(soup.find("a", id="link3"))
            # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>    

    print()
    
    print("[%s:%d] soup.html.head\n" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            ), file=sys.stderr)

    print(soup.html.head)

            # <head>
            # <title>The Dormouse''s story</title>
            # </head>

    print()
    
    print("[%s:%d] soup.html.head.title\n" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            ), file=sys.stderr)

    print(soup.html.head.title)
            # <title>The Dormouse''s story</title>



    #ccc

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
