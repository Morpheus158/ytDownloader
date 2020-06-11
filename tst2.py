from pydub import AudioSegment
import os

users_folder_name = r"C:\Users"
desktop_folder_name = "Desktop"
filename = "The Massive 2003 Half Life 2 Leak Explained _ MVG.webm"

my_path_value = os.path.join(users_folder_name,os.getlogin(),desktop_folder_name)

sound_input = AudioSegment.from_file(my_path_value + "\\" + str(filename))
if filename.endswith("webm"):
    filename = filename.replace("webm", "mp3")
elif filename.endswith("m4a"):
    filename = filename.replace("m4a", "mp3")
sound_input.export(my_path_value + "\\" + str(filename))