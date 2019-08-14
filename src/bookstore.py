############################################
# A program that stores book information   #
# Title, Author,                           #
# Year, ISBN                               #
#                                          #
# User can:                                #
#                                          #
# View all records                         #
# Search an entry                          #
# Add an entry                             #
# Delete                                   #
# Close                                    #
############################################

from tkinter import *
from bookstore_backend import Database

db=Database("books.db")
root=Tk()
root.title('Bookstore')

def get_selected_row(event):
    global selected_tuple
    index=book_list.curselection()[0]
    selected_tuple=book_list.get(index)
    title_entry.delete(0,END)
    title_entry.insert(END,selected_tuple[1])
    author_entry.delete(0,END)
    author_entry.insert(END,selected_tuple[2])
    year_entry.delete(0,END)  
    year_entry.insert(END,selected_tuple[3])
    isbn_entry.delete(0,END)
    isbn_entry.insert(END,selected_tuple[4])

def view_command():
    book_list.delete(0,END)
    for row in db.view():
        book_list.insert(END,row)

def search_command():
    book_list.delete(0,END)
    for row in db.search(title_value.get(),author_value.get(),year_value.get(),isbn_value.get()):
        book_list.insert(END,row)

def add_command():
    db.insert(title_value.get(),author_value.get(),year_value.get(),isbn_value.get())
    search_command()

def update_command():
    db.update(selected_tuple[0],title_value.get(),author_value.get(),year_value.get(),isbn_value.get())
    view_command()

def delete_command():
    db.delete(selected_tuple[0])
    view_command()


# LABELS

title_label=Label(root, text = 'Title')
title_label.grid(row=0,column=0)

year_label=Label(root, text = 'Year')
year_label.grid(row=1,column=0)

author_label=Label(root, text = 'Author')
author_label.grid(row=0,column=2)

isbn_label=Label(root, text = 'ISBN')
isbn_label.grid(row=1,column=2)

#Entries

title_value=StringVar()
title_entry=Entry(root,textvariable=title_value)
title_entry.grid(row=0,column=1)

year_value=StringVar()
year_entry=Entry(root,textvariable=year_value)
year_entry.grid(row=1,column=1)

author_value=StringVar()
author_entry=Entry(root,textvariable=author_value)
author_entry.grid(row=0,column=3)

isbn_value=StringVar()
isbn_entry=Entry(root,textvariable=isbn_value)
isbn_entry.grid(row=1,column=3)

#List

book_list=Listbox(root,height=6,width=35)
book_list.grid(row=1,column=0,rowspan=6,columnspan=2)

book_scrollbar=Scrollbar(root)
book_scrollbar.grid(row=2,column=2,rowspan=6)

book_list.configure(yscrollcommand=book_scrollbar.set)
book_scrollbar.configure(command=book_list.yview)

book_list.bind('<<ListboxSelect>>',get_selected_row)

#Buttons

view_button=Button(root,text="View all",width=12,command=view_command)
view_button.grid(row=2,column=3)

search_button=Button(root,text="Search entry",width=12,command=search_command)
search_button.grid(row=3,column=3)

add_button=Button(root,text="Add entry",width=12,command=add_command)
add_button.grid(row=4,column=3)

update_button=Button(root,text="Update",width=12,command=update_command)
update_button.grid(row=5,column=3)

delete_button=Button(root,text="Delete",width=12,command=delete_command)
delete_button.grid(row=6,column=3)

exit_button=Button(root,text="Exit",width=12,command=root.destroy)
exit_button.grid(row=7,column=3)


root.mainloop()