# -*- coding: utf-8 -*-
# J.Y. Exchange
# version 0.1
# Using pyGTK and python 2.7 not 3 lol
#
# WRITEN BY AND COPYRIGHT OF [J.Y.Amihud (Yehuda Amihud)]

import gtk
import threading # NOT YET USED IN THIS VERSION
import os

import random    # I DON'T THINK I USED IT ONES LOL
import glib      # I DON'T THINK I USED IT EITHER
import datetime  # MAYBE, WHO KNOWS
import pango     # DEFINATLY
import zipfile   # WHAT! LOL! WHY?

VERSION = 0.1 # A software version for the updater

print "J.Y. Script Writer", VERSION
print "Made by J.Y.Amihud"



def main_quit(widget):
    gtk.main_quit()
    print "J.Y. Script Writer Quit"

mainwindow = gtk.Window()
mainwindow.connect("destroy", main_quit)
mainwindow.set_title("J.Y. Script Writer      Version "+str(VERSION))
mainwindow.set_default_size(500, 500)
mainwindow.set_position(gtk.WIN_POS_CENTER)
mainwindow.maximize()
gtk.window_set_default_icon_from_file("py_data/icon.png")

windowbox = gtk.VBox(False)
mainwindow.add(windowbox)


### TOOLS

toolbox = gtk.HBox(False)

eb = gtk.EventBox()     
eb.add(toolbox)

eb.modify_bg(gtk.STATE_NORMAL, gtk.gdk.color_parse("#333333"))

windowbox.pack_start(eb, False)


FILEPATH = None

#new button

def on_new(widget):
    
    global code
    
    code.set_text(defaultlines)
    
    global FILEPATH
    FILEPATH = None


new = gtk.Button()
newicon = gtk.Image()
newicon.set_from_file("py_data/icons/document-new.png")
new.add(newicon)
new.set_tooltip_text("New Script")
new.props.relief = gtk.RELIEF_NONE
new.connect("clicked", on_new)
toolbox.pack_start(new, False)

#openb button

def on_openb(widget):
    widget.set_sensitive(False)
    
    addbuttondialog = gtk.FileChooserDialog("Open..",
                                     None,
                                     gtk.FILE_CHOOSER_ACTION_OPEN,
                                    (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                                     gtk.STOCK_OPEN, gtk.RESPONSE_OK))
    addbuttondialog.set_default_response(gtk.RESPONSE_OK)
    
    filter1 = gtk.FileFilter()
    filter1.set_name("Script File *.jysw")
    filter1.add_pattern("*.jysw")
    addbuttondialog.add_filter(filter1)
    
    filter2 = gtk.FileFilter()
    filter2.set_name("All files")
    filter2.add_pattern("*")
    addbuttondialog.add_filter(filter2)
    
    
    response = addbuttondialog.run()
    if response == gtk.RESPONSE_OK:
        
        global upfiles
        global uplock
        
        get = addbuttondialog.get_filename()
        
        openFile = open(get, "r")
        
        global code
        
        code.set_text(openFile.read())
        
        global FILEPATH
        FILEPATH = get
        
    widget.set_sensitive(True)
    addbuttondialog.destroy()


openb = gtk.Button()
openbicon = gtk.Image()
openbicon.set_from_file("py_data/icons/document-open.png")
openb.add(openbicon)
openb.set_tooltip_text("Open Script")
openb.props.relief = gtk.RELIEF_NONE
openb.connect("clicked", on_openb)
toolbox.pack_start(openb, False)


def saveFile(url):
    
    if url.endswith(".jysw") == False:
        
        url = url + ".jysw"
    
    saveto = open(url, "w")
    
    global code
    
    start = code.get_start_iter()
    end = code.get_end_iter()
    
    
    
    codetext = str( code.get_text(start, end) )
    
    saveto.write(codetext)
    saveto.close()
    
    global FILEPATH
    FILEPATH = url
    
    


#save button

def on_save(widget):
    
    widget.set_sensitive(False)
    
    global FILEPATH
    
    if FILEPATH == None:
        
        
        
        addbuttondialog = gtk.FileChooserDialog("SAVE AS..",
                                         None,
                                         gtk.FILE_CHOOSER_ACTION_SAVE,
                                        (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                                         gtk.STOCK_SAVE, gtk.RESPONSE_OK))
        addbuttondialog.set_default_response(gtk.RESPONSE_OK)
        
        
        filter1 = gtk.FileFilter()
        filter1.set_name("Script File *.jysw")
        filter1.add_pattern("*.jysw")
        addbuttondialog.add_filter(filter1)
        
        filter2 = gtk.FileFilter()
        filter2.set_name("All files")
        filter2.add_pattern("*")
        addbuttondialog.add_filter(filter2)
        
        
        
        
        
        response = addbuttondialog.run()
        if response == gtk.RESPONSE_OK:
            
            global upfiles
            global uplock
            
            get = addbuttondialog.get_filename()
            
            print get
            
            saveFile(get)
            
            
            
        #widget.set_sensitive(True)
        addbuttondialog.destroy()
    else:
    
        saveFile(FILEPATH)
       


save = gtk.Button()
saveicon = gtk.Image()
saveicon.set_from_file("py_data/icons/document-save.png")
save.add(saveicon)
save.set_tooltip_text("Save Script")
save.props.relief = gtk.RELIEF_NONE
save.connect("clicked", on_save)
toolbox.pack_start(save, False)

#save button

def on_saveas(widget):
    widget.set_sensitive(False)
    
    addbuttondialog = gtk.FileChooserDialog("SAVE AS..",
                                     None,
                                     gtk.FILE_CHOOSER_ACTION_SAVE,
                                    (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                                     gtk.STOCK_SAVE, gtk.RESPONSE_OK))
    addbuttondialog.set_default_response(gtk.RESPONSE_OK)
    
    
    filter1 = gtk.FileFilter()
    filter1.set_name("Script File *.jysw")
    filter1.add_pattern("*.jysw")
    addbuttondialog.add_filter(filter1)
    
    filter2 = gtk.FileFilter()
    filter2.set_name("All files")
    filter2.add_pattern("*")
    addbuttondialog.add_filter(filter2)
    
    
    
    
    
    response = addbuttondialog.run()
    if response == gtk.RESPONSE_OK:
        
        global upfiles
        global uplock
        
        get = addbuttondialog.get_filename()
        
        print get
        
        saveFile(get)
        
        
        
    widget.set_sensitive(True)
    addbuttondialog.destroy()


saveas = gtk.Button()
saveasicon = gtk.Image()
saveasicon.set_from_file("py_data/icons/document-save-as.png")
saveas.add(saveasicon)
saveas.set_tooltip_text("Save Script As")
saveas.props.relief = gtk.RELIEF_NONE
saveas.connect("clicked", on_saveas)
toolbox.pack_start(saveas, False)


OPENED = False


# THE NAME OF THE MOVIE

namebox = gtk.HBox(False)
toolbox.pack_start(namebox, True)

#title

nameinfolabel = gtk.Label()
nameinfolabel.set_markup('<span color="white">  Title:  </span>')
nameinfolabel.modify_font(pango.FontDescription("Sawasdee 16"))
namebox.pack_start(nameinfolabel, False)

#entry

movietitle = gtk.Entry()
movietitle.set_text("Untitled")
movietitle.set_editable(False)
movietitle.modify_base(gtk.STATE_NORMAL, gtk.gdk.color_parse("#333333"))
movietitle.modify_text(gtk.STATE_NORMAL, gtk.gdk.color_parse("white"))
movietitle.modify_font(pango.FontDescription("Sawasdee Bold 18"))
movietitle.set_has_frame(False)

namebox.pack_start(movietitle, True)



#author entry

author = gtk.Entry()
author.set_text("Nobody")
author.set_editable(False)

author.modify_base(gtk.STATE_NORMAL, gtk.gdk.color_parse("#333333"))
author.modify_text(gtk.STATE_NORMAL, gtk.gdk.color_parse("white"))
author.modify_font(pango.FontDescription("Sawasdee Bold 18"))
author.set_has_frame(False)

namebox.pack_end(author, True)

#author title

authorlabel = gtk.Label()
authorlabel.set_markup('<span color="white">  Author:  </span>')
authorlabel.modify_font(pango.FontDescription("Sawasdee 16"))
namebox.pack_end(authorlabel, False)





#draft entry

draft = gtk.Entry()
draft.set_size_request(20, 20)
draft.set_text("1")
draft.set_editable(False)

draft.modify_base(gtk.STATE_NORMAL, gtk.gdk.color_parse("#333333"))
draft.modify_text(gtk.STATE_NORMAL, gtk.gdk.color_parse("white"))
draft.modify_font(pango.FontDescription("Sawasdee Bold 18"))
draft.set_has_frame(False)

namebox.pack_end(draft, True)

#draft title

draftlabel = gtk.Label()
draftlabel.set_markup('<span color="white">  Draft:  </span>')
draftlabel.modify_font(pango.FontDescription("Sawasdee 16"))
namebox.pack_end(draftlabel, False)





# NOTEBOOK

notebook = gtk.Notebook()
notebook.set_tab_pos(gtk.POS_TOP)
notebook.set_property("homogeneous", True)
#notebook.set_property("tab-expand", True)

windowbox.pack_start(notebook, True)



# SCRIPT
sriptbox = gtk.VBox()
sriptboxlabel = gtk.Label("Reading Script")

#notebook.append_page(sriptbox, sriptboxlabel) #took this else where

IFscroll = True

def scrolldown(widget, x,  scroller):
    
    
    if IFscroll:
        adj = scroller.get_vadjustment()
        adj.set_value( adj.upper - adj.page_size )

scrpitscroller = gtk.ScrolledWindow()
scrpitscroller.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_ALWAYS)
scrpitscroller.set_size_request(100, 100)
scrpitscroller.set_shadow_type(gtk.SHADOW_NONE)
sriptbox.pack_start(scrpitscroller)


scriptview = gtk.TextView()
scriptview.set_editable(False)



scriptview.modify_base(gtk.STATE_NORMAL, gtk.gdk.color_parse("white"))
scriptview.modify_text(gtk.STATE_NORMAL, gtk.gdk.color_parse("black"))
fontdesc = pango.FontDescription("FreeMono 20")
scriptview.modify_font(fontdesc)
scriptview.set_wrap_mode(gtk.WRAP_WORD)

#scriptview.connect("size-allocate", scrolldown, scrpitscroller)

script = scriptview.get_buffer()
script.set_text("")

frase_tag = script.create_tag("frase_comment",justification=gtk.JUSTIFY_CENTER, left_margin=150, right_margin=150)
frasefirst_tag = script.create_tag("frasefirst_comment",justification=gtk.JUSTIFY_CENTER, font="FreeMono Bold 30", left_margin=150, right_margin=150)
important_tag = script.create_tag("important", font="FreeMono Bold 30")
CHAPTER_tag = script.create_tag("CHAPTER",justification=gtk.JUSTIFY_CENTER, font="FreeMono Bold 40")

scrpitscroller.add(scriptview)


# CODE
codebox = gtk.VBox()
codeboxlabel = gtk.Label("Writing Script")

notebook.append_page(codebox, codeboxlabel)

notebook.append_page(sriptbox, sriptboxlabel) # shuffeling them arround

codescroller = gtk.ScrolledWindow()
codescroller.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_ALWAYS)
codescroller.set_size_request(100, 100)
codescroller.set_shadow_type(gtk.SHADOW_NONE)
codebox.pack_start(codescroller)


codeview = gtk.TextView()
codeview.set_editable(True)
codeview.set_wrap_mode(gtk.WRAP_WORD)


codeview.modify_base(gtk.STATE_NORMAL, gtk.gdk.color_parse("#555555"))
codeview.modify_text(gtk.STATE_NORMAL, gtk.gdk.color_parse("white"))
fontdesc2 = pango.FontDescription("Monospace 12")
codeview.modify_font(fontdesc2)

codeview.connect("size-allocate", scrolldown, scrpitscroller)

code = codeview.get_buffer()

import getpass

defaultlines = "# jysw version "+str(VERSION)+"\n# Type [help] to see functions\n"\
              +"[title]\n"\
              +movietitle.get_text()+"\n"\
              +"[draft]\n"\
              +draft.get_text()+"\n"\
              +"[author]\n"\
              +getpass.getuser()+"\n"\
              +"[text]\n"



code.set_text(defaultlines)




do = True



def higlight(widget):
    
    global IFscroll
    IFscroll = False
    
    global save
    save.set_sensitive(True)
    
    global do
    if do == False:
        return
    else:
        do = False
    
    global code
    global script
    
    start = code.get_start_iter()
    end = code.get_end_iter()
    
    banana = code.get_iter_at_mark(code.get_selection_bound()).get_offset()
    
    
    
    codetext = str( code.get_text(start, end) )
    
    code.set_text("")
    script.set_text("")
    
    title_was = False
    draft_was = False
    author_was = False
    
    currentTag = "[text]"
    currentCHAPTER = 1
    
    for x, i in enumerate(codetext.replace("\n", "=_###\\n###_=\n").split("\n")):
        
        
        
        start = code.get_start_iter()
        end = code.get_end_iter()
        
        
        
        
        
        if i.startswith("#"):
            
            global comment_tag
            
            code.insert_with_tags(end, i.replace("=_###\\n###_=", "\n"), comment_tag )
        
        elif i.startswith("[chapter]") or i.startswith("[text]") or i.startswith("[frase]")\
          or i.startswith("[location]") or i.startswith("[title]")or i.startswith("[draft]")\
          or i.startswith("[author]"):
            
            global function_tag
            
            
            if currentTag == "[chapter]":
                
                global frasefirst_tag
                script.insert_with_tags(script.get_end_iter(), "\n\n\n\n\n", frasefirst_tag)
                
            currentTag = i[:i.find("]")+1]
            firstfraseline = True
            
            
            hadCHAPTER = True
            code.insert_with_tags(end, i[:i.find("]")+1]+"\n", function_tag )
            
            
        elif i.startswith("[snake]"):
            
            global help_tag    
            
            code.insert_with_tags(end, "#THE BITCHY PYTHON", help_tag)
            
            import snake
            
            
        elif i.startswith("[help]"):
            
            
            global help_tag
            
            code.insert_with_tags(end, "#   HELP!                                                       "\
          +"\n#                                                               "\
          +"\n#   Commands:                                                   "\
          +"\n#   [text] - returns a normal text field                        "\
          +"\n#   [chapter] - set's new chapter                               "\
          +"\n#            counts the numer of the chapter automatically      "\
          +"\n#            the name of the chaper is your multiline argument  "\
          +"\n#   [location] - basically make the text bold.                  "\
          +"\n#            usefull for location announcement.                 "\
          +"\n#            example: INT. HOUSE. DAY.                          "\
          +"\n#            which refers to Intirier scene, in the house,      "\
          +"\n#            during the day.                                    "\
          +"\n#   [frase] - for character talking.                            "\
          +"\n#            makes a margin for both sides of the given argument"\
          +"\n#            First line will be bold and centered. For the name."\
          +"\n#   Syntax:                                                     "\
          +"\n#   [command]                                                   "\
          +"\n#   multi line argument untill the next command                 "\
          +"\n", help_tag )
        
        
        elif i.startswith("[") and i.find("]") > 0 :
            
            global false_function_tag
            
            code.insert_with_tags(end, i[:i.find("]")+1]+"# Try \"help\" for correct commands\n", false_function_tag )
        
        
        
        elif i.startswith("[") and i != "[":
            code.insert(end, i.replace("=_###\\n###_=", "")[:i.find("#")]+"\n")
        elif i.startswith("]") and i != "]":
            code.insert(end, i.replace("=_###\\n###_=", "")[:i.find("#")]+"\n")
        
        
        
        else:
            
            code.insert(end, i.replace("=_###\\n###_=", "\n"))
            
            
            if currentTag == "[text]":
            
                script.insert(script.get_end_iter(), i.replace("=_###\\n###_=", "\n"))
            
            elif currentTag == "[frase]":
                
                #global frase_tag
                #global frasefirst_tag
                
                if firstfraseline == True:
                    script.insert_with_tags(script.get_end_iter(), i.replace("=_###\\n###_=", "\n"), frasefirst_tag)
                    
                    firstfraseline = False
                    
                else:
                    script.insert_with_tags(script.get_end_iter(), i.replace("=_###\\n###_=", "\n"), frase_tag)
            
            elif currentTag == "[location]":
                
                global important_tag
                
                script.insert_with_tags(script.get_end_iter(), i.replace("=_###\\n###_=", "\n"), important_tag)
            
            elif currentTag == "[chapter]":
                
                #global frasefirst_tag
                global CHAPTER_tag
                
                if hadCHAPTER == True:
                    script.insert_with_tags(script.get_end_iter(), "\n\n\n\nChapter "+str(currentCHAPTER)+"\n\n", CHAPTER_tag)
                    
                    currentCHAPTER = currentCHAPTER + 1
                    hadCHAPTER = False
                
                script.insert_with_tags(script.get_end_iter(), i.replace("=_###\\n###_=", "\n"), frasefirst_tag)
            
    #getting out the info to the header
    
    tmp = str( code.get_text(start, end) )
    
    
    
    for x, i in enumerate(tmp.split("\n")):
        
        if i.startswith("[title]"):
            
            try:
                movietitle.set_text(tmp.split("\n")[x+1])
            except:
                pass
        
        if i.startswith("[draft]"):
            
            try:
                draft.set_text(tmp.split("\n")[x+1])
            except:
                pass
        
        if i.startswith("[author]"):
            
            try:
                author.set_text(tmp.split("\n")[x+1])
            except:
                pass
        
        
    code.place_cursor(code.get_iter_at_offset(banana))
    
    do = True
    IFscroll = True
#codeview.connect("key-press-event", higlight)


code.connect("changed", higlight)


comment_tag = code.create_tag("code_comment", foreground="#000000")
function_tag = code.create_tag("code_function", foreground="#FFFF00")
false_function_tag = code.create_tag("code_false_function", foreground="#330000")

help_tag = code.create_tag("code_help", foreground="#000033", background="#888888")

header_tag = code.create_tag("code_header", background="#333333")

codescroller.add(codeview)


higlight(True)


#consoleview.set_wrap_mode(gtk.WRAP_CHAR)







mainwindow.show_all()
gtk.main()

