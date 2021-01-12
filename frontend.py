"""
    A program that stores this book information:
        - Title
        - Author
        - Year
        - ISBN

    User can:
        - View all records
        - Search an entry
        - Add entry
        - Update entry
        - Delete entry
        - Close
"""

from tkinter import *
import backend

def get_selected_row(event):
    global selected_tuple
    index = books_list.curselection()
    try:
        selected_tuple = books_list.get(index)
        title_entry.delete(0, END)
        title_entry.insert(END, selected_tuple[1])
        author_entry.delete(0, END)
        author_entry.insert(END, selected_tuple[2])
        year_entry.delete(0, END)
        year_entry.insert(END, selected_tuple[3])
        isbn_entry.delete(0, END)
        isbn_entry.insert(END, selected_tuple[4])
    except IndexError:
        pass


def view_command():
    books_list.delete(0, END)
    for row in backend.view():
        books_list.insert(END, row)

def search_command():
    books_list.delete(0, END)
    for row in backend.search(title_value.get(), author_value.get(), year_value.get(), isbn_value.get()):
        books_list.insert(END, row)

def add_command():
    backend.insert(title_value.get(), author_value.get(), year_value.get(), isbn_value.get())
    view_command()

def update_command():
    backend.update(selected_tuple[0], title_value.get(), author_value.get(), year_value.get(), isbn_value.get())
    view_command()

def delete_command():
    backend.delete(selected_tuple[0])
    view_command()

window = Tk()
window.wm_title("BookStore")

# Labels
title_label  = Label(window, text="Title")
author_label = Label(window, text="Author")
year_label   = Label(window, text="Year")
isbn_label   = Label(window, text="ISBN")

title_label.grid(row=0,column=0)
author_label.grid(row=0,column=2)
year_label.grid(row=1,column=0)
isbn_label.grid(row=1,column=2)

# Entries
title_value = StringVar()
author_value = StringVar()
year_value = StringVar()
isbn_value = StringVar()

title_entry = Entry(window, textvariable=title_value)
author_entry = Entry(window, textvariable=author_value)
year_entry = Entry(window, textvariable=year_value)
isbn_entry = Entry(window, textvariable=isbn_value)

title_entry.grid(row=0,column=1)
author_entry.grid(row=0,column=3)
year_entry.grid(row=1,column=1)
isbn_entry.grid(row=1,column=3)


# List
books_list = Listbox(window, height=6, width=35)
books_list.grid(row=2, column=0, rowspan=6, columnspan=2)

# Scroll bar
scrollbar = Scrollbar(window)
scrollbar.grid(row=2, column=2, rowspan=6)

books_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=books_list.yview)

books_list.bind('<<ListboxSelect>>', get_selected_row)

# Buttons
all_button = Button(window, text="View all", width=12, command=view_command)
search_button = Button(window, text="Search Entry", width=12, command=search_command)
add_button = Button(window, text="Add Entry", width=12, command=add_command)
update_button = Button(window, text="Update Entry", width=12, command=update_command)
delete_button = Button(window, text="Delete Entry", width=12, command=delete_command)
close_button = Button(window, text="Close", width=12, command=window.destroy)

all_button.grid(row=2 , column=3)
search_button.grid(row=3 , column=3)
add_button.grid(row=4 , column=3)
update_button.grid(row=5 , column=3)
delete_button.grid(row=6 , column=3)
close_button.grid(row=7 , column=3)




window.mainloop()