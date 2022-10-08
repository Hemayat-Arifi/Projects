from tkinter import *
from pytube import YouTube
from tkinter import messagebox


# TODO: _____________________________ Create Download Function ______________________________
def do_low():
    high.config(bg='#5AA897')
    audio.config(bg='#5AA897')
    low.config(bg='silver')


def do_audio():
    high.config(bg='#5AA897')
    low.config(bg='#5AA897')
    audio.config(bg='silver')


def do_high():
    low.config(bg='#5AA897')
    high.config(bg='silver')
    audio.config(bg='#5AA897')


def yes():

    url = link.get()
    low_value = low.cget('bg')
    high_value = high.cget('bg')
    audio_value = audio.cget('bg')

    if len(url) != 0:
        if low_value == 'silver':
            yt = YouTube(url)
            video = yt.streams.get_lowest_resolution()
            video.download()

        elif high_value == 'silver':
            yt = YouTube(url)
            video = yt.streams.get_highest_resolution()
            video.download()

        elif audio_value == 'silver':
            yt = YouTube(url)
            video = yt.streams.get_audio_only()
            video.download()

        else:
            messagebox.showerror(title="invalid progress", message="please select the video quality")
    else:
        messagebox.showerror(title='invalid input', message='paste the link')


# TODO: _________________________________ create app GUI _______________________________________
title_space = ' ' * 40
window = Tk()
window.config(padx=25, pady=25, bg='#1B2438')
window.title(f'{title_space}Youtube Video Downloader')
window.minsize(width=450, height=500)

logo_image = PhotoImage(file='logo.png')

canvas = Canvas(width=225, height=105, bg='#1B2438', highlightthickness=0)
canvas.create_image(120, 50, image=logo_image)
canvas.grid(column=0, row=0, columnspan=3)


choose = Label(text='_______________________________________________________', bg='#1B2438', fg='#345B63', font=("san-serif", 11, "bold"))
choose.grid(column=0, row=1, columnspan=3)


# Create link input and label
link_label = Label(text='Paste Link', bg='#1B2438', fg='#E6E6E6', font=("Arial", 11, "bold"))
link_label.grid(column=0, row=2)

link = Entry(width=40)
link.grid(column=1, row=2, pady=30, padx=0, columnspan=2)


# Create Two Buttons --> 1.low  2.high and choose Label
choose = Label(text='Video Preference', bg='#1B2438', fg='#345B63', font=("san-serif", 11, "bold"))
choose.grid(column=0, row=4, columnspan=3, pady=10)

low = Button(text='Low Dimension', command=do_low, bg='#5AA897', fg='#1B2438', font=("Comic Sans MS", 11, "bold"))
low.grid(column=0, row=5)

audio = Button(text='Audio Only', command=do_audio, bg='#5AA897', fg='#1B2438', font=("Comic Sans MS", 11, "bold"))
audio.grid(column=1, row=5)

high = Button(text='High Dimension', command=do_high, bg='#5AA897', fg='#1B2438', font=("Comic Sans MS", 11, "bold"))
high.grid(column=2, row=5)


# space between download and quality buttons
space = Label(text='_________________', bg='#1B2438', fg='#345B63', font=("san-serif", 12, "bold"))
space.grid(column=0, row=6, columnspan=3, pady=10)

# Download Button
download = Button(text='D o w n l o a d', command=yes, bg='#5AA897', fg='black', font=("Harlow Solid Italic", 11, "bold"), width=30)
download.grid(column=0, row=7, columnspan=3, pady=20)


window.mainloop()
