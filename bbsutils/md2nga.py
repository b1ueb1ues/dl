#!/usr/bin/env python
# -*- encoding:utf8 -*-
import sys
import markdown2
Markdown = markdown2.Markdown
mmain = markdown2.main
py3 = markdown2.py3

#sys.setdefaultencoding('utf-8')


#md = Markdown()
#print md.convert("## test\#")


def processall(a):
    alt = 1 # make p=quote quote=collapse
    replace = {
        '<p>'   : ''        , '</p>'   : ''         ,
       #'<p>'   : '[quote]' , '</p>'   : '[/quote]' ,
        '<pre>' : ''        , '</pre>' : ''         ,
       #-------------
        '<h1>' : '[h][b][size=150%]' , '</h1>' : '[/size][/b][/h]' , # #
        '<h2>' : '[h][b][size=130%]' , '</h2>' : '[/size][/b][/h]' , # ##
        '<h3>' : '[b][size=120%]'    , '</h3>' : '[/size][/b]'     , # ###
        '<h4>' : '[b][size=110%]'    , '</h4>' : '[/size][/b]'     , # ####
        '<h5>' : '[b][size=100%]'    , '</h5>' : '[/size][/b]'     , # #####
        '<h6>' : '[b][size=100%]'    , '</h6>' : '[/size][/b]'     , # ######
       # ## ### #### ##### ######
        '<ul>'         : '[list]'         , '</ul>'         : '[/list]'     , # - list
        '<ol>'         : '[list]'         , '</ol>'         : '[/list]'     , # 1. order list
        '<li>'         : '[*]'            , '</li>'         : ''            ,
       #-------------
        '<table>'      : '[table]'        , '</table>'      : '[/table]'    , # | table | table |
        '<thead>'      : ''               , '</thead>'      : ''            , # | :---- | ----: |
        '<th>'         : '[th]'           , '</th>'         : '[/th]'       , # | body  |  body |
        '<tbody>'      : ''               , '</tbody>'      : ''            ,
        '<tr>'         : '[tr]'           , '</tr>'         : '[/tr]'       ,
        '<td>'         : '[td]'           , '</td>'         : '[/td]'       ,
       #-------------
        '<strong>'     : '[b][size=110%]' , '</strong>'     : '[/size][/b]' , # **bold**
        '<em>'         : '[color=red]'    , '</em>'         : '[/color]'    , # *red*
        '<blockquote>' : '[quote]'        , '</blockquote>' : '[/quote]'    , # > quote
       #'<blockquote>' : '[collapse]'     , '</blockquote>' : '[/collapse]' , # > collapse
        '<strike>'     : '[del]'          , '</strike>'     : '[/del]'      , # ~~del~~
        '<hr />'       : '======'         , # -------------------------------------------
        '<code>'       : '[code]'         , '</code>'       : '[/code]'     , # `code`  
        # ```
        # code
        # ```
        #
        #   code
        #

        '__END__' : '__END__'
        }

    if alt :
        replace['<blockquote>'] = '[collapse]'
        replace['</blockquote>'] = '[/collapse]'
        replace['<p>'] = '[quote]'
        replace['</p>'] = '[/quote]'

    for i in replace:
        a = a.replace(i,replace[i])

    if py3:
        sys.stdout.write(a)
    else:
        sys.stdout.write(a.encode(
            sys.stdout.encoding or "utf-8", 'xmlcharrefreplace'))

    return a
    #print a


def processline(l):
    pass

def main():
    ext = {
            "tables":1,
            "fenced-code-blocks":1,
            "numbering":1,
            #"spoiler":1,
            "strike":1,
            "__END__":0
    }
    if len(sys.argv) >= 2:
        if sys.argv[1] :
            path = sys.argv[1]
    else:
        path = 'mwts.md'
    a = mmain(path=path,extras=ext)
    a = processall(a)
    f = open(path+".txt",'w')
    f.write(a.encode('utf-8'))
    f.close()

if __name__ == "__main__":
    main()

