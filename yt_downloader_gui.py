import pafy
import youtube_dl
from tkinter import Label, Button, Entry, StringVar, Tk, Checkbutton, IntVar

def download_action():
    my_video = pafy.new(url_value.get())
    if check_int.get() == 1:
        best = my_video.getbestaudio()
    else:
        best = my_video.getbest()
    best.download(path_value.get(), quiet=False)

window = Tk()

title_label = Label(window, text="Pájova appka na stahování z YT")
title_label.grid(row=0, column=0, columnspan=2)

url_label = Label(window, text="Odkaz na video: ")
url_label.grid(row=1, column=0)

path_label = Label(window, text="Uložit do: ")
path_label.grid(row=2, column=0)

down_button = Button(window, text="Stáhnout", command=download_action)
down_button.grid(row=3, column=0, columnspan=2)

check_int = IntVar()
audio_checkbox = Checkbutton(window, text="Jen audio", variable=check_int)
audio_checkbox.grid(row=3, column=0)

path_value = StringVar()
path_entry = Entry(window, textvariable=path_value, width=30)
path_entry.grid(row=2, column=1)

url_value = StringVar()
url_emtry = Entry(window, textvariable=url_value, width=30)
url_emtry.grid(row=1, column=1)

window.mainloop()