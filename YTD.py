#KUNAL
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube
from PIL import Image,ImageTk

Folder_name=""
def openLocation():
    global Folder_name
    Folder_name=filedialog.askdirectory()
    if(len(Folder_name)>1):
        LocationError.config(text=Folder_name,fg="green")
    else:
        LocationError.config(text="Please Choose a Folder",fg="red")

#downloading the video
def Download_Video():
    choice=ytdchoose.get()
    URL=ytd_enter.get()
    if(len(URL)>1):
        ytdError.config(text="")
        yt=YouTube(URL)
        if(choice == choices[0]):
            select = yt.streams.filter(progressive=True).first()

        elif(choice == choices[1]):
            select = yt.streams.filter(progressive=True,file_extension='mp4').last()

        elif(choice == choices[2]):
            select = yt.streams.filter(only_audio=True).first()

        else:
            ytdError.config(text="Paste Link again!!",fg="red")
            

#download function 
    select.download(Folder_name)
    ytdError.config(text="Download Completed!!")

            
####################################################################################################
root = Tk()
root.title("YouTube Video Downloader")
#Gui geometry 
root.geometry('350x300')
root.maxsize(350,300)
root.minsize(350,300)
root.columnconfigure(0,weight=1)
ytd_lable = Label(root,text="Enter the URL to Download",font=("jost",15))
ytd_lable.grid()
#URL bOx
ytd_enterVar=StringVar()
ytd_enter=Entry(root,width=50,textvariable=ytd_enterVar)
ytd_enter.grid()
#error msg
ytdError=Label(root,text="Error",fg='red',font=('jost',10))
ytdError.grid()
#asking download path
ytdpath=Label(root,text="Download Path/Storage location",fg='Black',font=("jost",12,'bold'))
ytdpath.grid()
#location button 
Download_button= Button(root,width=15,bg="light blue",fg="black",text="Choose Location ",command=openLocation)
Download_button.grid()
#error msg for locaion 
LocationError=Label(root,text="Error download location...Choose location",fg="red",font=("Serif Bold",10,"bold"))
LocationError.grid()
#download quality 
quality=Label(root,text="Download Quality",fg='Black',font=("jost",12,'bold'))
quality.grid()
choices=["720p",'360p','Audio file']
ytdchoose=ttk.Combobox(root,value=choices)
ytdchoose.grid()
#download button 
Dbutton=Button(root,width=11,bg="MediumVioletRed",fg="black",text="Download",font=('Serif Bold',10,"bold"),command=Download_Video)
Dbutton.grid()
#my tag
kunal=Label(root,text="KKS",font=("Rando",10,'italic'))
kunal.grid()



root.mainloop()

