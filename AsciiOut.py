#! /usr/bin/env python

#

print("""
                     `/osyyysso+:.
                      ../oymdddddddy+.
                    `/sdddddddddddddddh/
                  .odhddddddddddddddddddd/
                `odhddddddddddddddddddddddy`
             -:--.``.:ohdddh+:.``.-/yddddddd.
           ./`         `/h:          -sdddddd.
          .:            :`            .odddddh`
          +     `       :      `      `.ddddddo
          +    .+       :     -o      ..hddddddo
          --      `-::/+o            `./ddddddddy`
           y/ `-/++//////+.         ..oddddddddddh.
         `sdhy+///////////+//-````-/sdddddddddddddd-
        .hmddhysooooooooooosdddddddddddddddddddddddd:
       :mdmddddddhyyso++//odddddddddddddddddddddddddm:
      /mddmddddddddddddyso/:::/+oshddddddddddddddddddd`
     /mdddmdddddddddh+-..```````..-:sddddddddmmddddddm/
    `mmmhs+dhhdddddo.```````````````.:ydddhhmmmmdmdddms
     ``   :s///+yd+```````````````````-hs+//odNy :ymdmy
      ./+oo+//////oo.````````````````-s+//////+ooo:-hm+
     `y////////////+s/.`````````````:s///////////+y  .
     .y+/////////////s+.```````````.y////////////+s:
    -o+//////////////+y/.``````````s+//////////////+o/
   :s/////////////////+y-.````````.y////////////////oo
    oo+++/////////////+s/-.```..``:s+///////////+++s/
     -+sooo+++++////++oodysssossyhdso+++++++++ooso/`
        .:/+osooooooooos`          sooooooooso+:.
              .-::::::.            `:////:-.

""")

print("##################### Welcome to AsciiOut.py #################################\n")
print("Easily copy and paste terminal art in C++\n")
print("author : jkap1")
print("##############################################################################")

cout = ('cout << "')
endl = ('" << endl;')

def cppFile():
    fd = open('art.txt')
    contents = fd.read().splitlines()
    for line in contents:
        print(cout,line,endl, sep= '')

cppFile()