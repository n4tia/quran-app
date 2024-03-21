import quranapi as quranapi
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import tkinter as tk
root=Tk()

def get_Q_data():
    global x, my_search,new_win,text_plus
    x=[]
    the_edition=combo_edition.get()
    for items in quranapi.get_api(f'https://api.alquran.cloud/v1/quran/{the_edition}')['data']['surahs']:

        name_of_surah=items['englishName']
        for item in items['ayahs']:
    
            x.append([name_of_surah, item['text']])
            
    new_win=Toplevel(root)
    new_win.title('search')
    my_frame=Frame(new_win)
    my_frame.grid(row=0,column=0,sticky=W)
    my_search=Entry(my_frame,width=25)
    my_search.grid(row=0,column=0)
    btn_=Button(new_win, text='Search', command=religuos)
    btn_.grid(row=1,column=0,pady=5,sticky=W)
    


def search_(search_item='Grace'):
    global x,new_win,text_plus
    my_row=1
    temp=''
    text_plus=''
    for items in x:
        temp=items[0]
        if search_item in items[1]:
            if items[0] != temp:
                print(items[0],temp)
                text_plus+=items[0]
            text_plus+='\n \n'+items[1]
    yyy=Text(new_win,padx=10, pady=5)
    yyy.tag_configure('my_text')
    yyy.insert('1.0',text_plus)
    yyy.tag_add('my_text','1.0','end')
    yyy.grid(row=2,column=0)  
    canvas = tk.Canvas(new_win,  
                   width = 200,  
                   height = 200) 
  
 
    save_btn = Button(new_win, 
            text ='Save', 
            width=25,
            command = option_to_save).grid(column=0, row=4, columnspan=3,sticky=W)
    canvas.create_window(100, 100,  
                     window = save_btn)       
        
def religuos():
    global my_search,new_win,x,text_plus
    search_(my_search.get())
    
def option_to_save():
    global new_win,text_plus
    save_qeust=mb.askquestion('Do you want to save information to file?', 'Do you want to save information to file?')
    if save_qeust == 'yes' :
        with open('save_information.txt', 'w',encoding='utf-8') as f:
          f.write(text_plus)
        
        mb.showinfo('Save','Saved.')
        
    else :
        mb.showinfo('Return', 'Returning to main application')
     
def display_text():
   global str,new_win,text_plus
   str= Entry.get()
   Label.configure(text=str)
 
 
 
    
get_edition=[]

for items in quranapi.get_api('https://api.alquran.cloud/v1/edition')['data']:
  
    get_edition.append(items['identifier'])
    
get_edition=sorted(get_edition)

combo_edition=ttk.Combobox(root, values=get_edition)
combo_edition.grid(row=0,column=0)
btn=Button(root, text='click here', command=get_Q_data)
btn.grid(row=0, column=1)


root.mainloop()