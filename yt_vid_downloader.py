from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    try:
        yt= YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print('video downloadeed successfully!!')



    except Exception as e:
        print(e)

def open_file_dialouge():
    folder = filedialog.askdirectory()
    if folder:
        print(f"selected folder: {folder}")

    return folder

if __name__ =="__main__":
    root = tk.Tk()
    root.withdraw()

    url = input("enter yt url: ")
    save_path = open_file_dialouge()

    if not save_path:
        print("invalid save loaction")
    
    else:
        print("download started...")
        download_video(url, save_path)




