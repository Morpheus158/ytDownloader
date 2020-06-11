import pafy
import os
import youtube_dl
from tkinter import Label, Button, Entry, StringVar, Tk, Checkbutton, IntVar, Listbox, Scrollbar, END
from pydub import AudioSegment

users_folder_name = r"C:\Users"
desktop_folder_name = "Desktop"
audio_bool = False

def download_action():
    my_video = pafy.new(url_value.get())
    my_stream = my_video.getbest()
    my_path_value = str(path_value.get())

    if my_path_value.strip() == "":
        my_path_value = os.path.join(users_folder_name,os.getlogin(),desktop_folder_name)

    if check_int.get() == 1:
        my_stream = my_video.getbestaudio()
        audio_bool = True
    elif check2_int.get() == 1:
        counter = 0
        title = ""
        for titles in my_video.allstreams:
            if titles.mediatype == "audio":
                title = titles.mediatype + ":" + titles.extension + "@" + titles.bitrate
            else:
                title = titles.mediatype + ":" + titles.extension + "@" + titles.resolution
            if title == selected_row:
                my_stream = my_video.allstreams[counter]
            counter = counter + 1
    else:
        my_stream = my_video.getbest()

    my_stream.download(my_path_value, quiet=False)

    if audio_bool == True:
        sound_input = AudioSegment.from_file(my_path_value + "\\" + str(my_stream.filename))
        if my_stream.filename.endswith("webm"):
            filename = my_stream.filename.replace("webm", "mp3")
        elif my_stream.filename.endswith("m4a"):
            filename = my_stream.filename.replace("m4a", "mp3")
        sound_input.export(my_path_value + "\\" + str(filename))

def quality_list():
    my_video = pafy.new(url_value.get())
    if check2_int.get() == 1:
        audio_checkbox.grid_forget()
        listall.delete(0,END)
        for stream in my_video.allstreams:
            listall.insert(END,stream)
    if check2_int.get() == 0:
        audio_checkbox.grid(row=4, column=0, sticky="W")
        listall.delete(0,END)

def get_row(event):
    global selected_row
    row_index = listall.curselection()[0]
    selected_row = listall.get(row_index)

window = Tk()

url_value = StringVar()
url_emtry = Entry(window, textvariable=url_value, width=30)
url_emtry.grid(row=1, column=1)

path_value = StringVar()
path_entry = Entry(window, textvariable=path_value, width=30)
path_entry.grid(row=2, column=1)

title_label = Label(window, text="Pájova appka na stahování z YT")
title_label.grid(row=0, column=0, columnspan=2)

url_label = Label(window, text="Odkaz na video: ")
url_label.grid(row=1, column=0)

path_label = Label(window, text="Uložit do: ")
path_label.grid(row=2, column=0)

down_button = Button(window, text="Stáhnout", command=download_action)
down_button.grid(row=4, column=0, columnspan=2)

check_int = IntVar()
audio_checkbox = Checkbutton(window, text="Jen audio (MP3)", variable=check_int)
audio_checkbox.grid(row=4, column=0, sticky="W")

check2_int = IntVar()
quality_checkbox = Checkbutton(window, text="Určit kvalitu", variable=check2_int, command=quality_list)
quality_checkbox.grid(row=4, column=1, sticky="E")

listall = Listbox(window, width=60, height=5)
listall.grid(row=3, column=0, columnspan=2)
listall.bind("<<ListboxSelect>>", get_row)

window.mainloop()