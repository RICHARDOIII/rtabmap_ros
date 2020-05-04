from tkinter import *

def donothind():
    pass
def replace_queue():
    s=disp_["text"]
    arg= s.split()
    for x in arg:
        if "queue_size:=" in x:
            arg.remove(x)
    if  que_entry.get() != "":
        added=f" queue_size:={que_entry.get()} "+" "
        disp_["text"]=" ".join(arg)+added
def rvizt():
    s = disp_["text"]
    arg = s.split()
    for x in arg:
        if "rviz:=" in x:
            arg.remove(x)
    added = f" rviz:=true" + " "
    disp_["text"] = " ".join(arg) + added
def rvizf():
    s = disp_["text"]
    arg = s.split()
    for x in arg:
        if "rviz:=" in x:
            arg.remove(x)
    added = f" rviz:=false" + " "
    disp_["text"] = "  ".join(arg) + added
def rmvizt():
    s = disp_["text"]
    arg = s.split()
    for x in arg:
        if "rtabmapviz:=" in x:
            arg.remove(x)
    added = f" rtabmapviz:=true" + " "
    disp_["text"] = " ".join(arg) + added
def rmvizf():
    s = disp_["text"]
    arg = s.split()
    for x in arg:
        if "rtabmapviz:=" in x:
            arg.remove(x)
    added = f" rtabmapviz:=false" + " "
    disp_["text"] = "  ".join(arg) + added

def db():
    s = disp_["text"]
    arg = s.split()
    for x in arg:
        if "rtabmap_args:=" in x:
            arg.remove(x)
    added = f" rtabmap_args:=""-d""" + " "
    disp_["text"] = "  ".join(arg) + added

def dbn():
    s = disp_["text"]
    arg = s.split()
    for x in arg:
        if "rtabmap_args:=" in x:
            arg.remove(x)
    disp_["text"] = "  ".join(arg)


root = Tk()

menu = Menu(root)
root.config(menu=menu)
root.resizable(width=FALSE, height=TRUE)
root.geometry('{}x{}'.format(450, 800))

# set up frames for GUI
odomFrame   = Frame(master=root, relief=SUNKEN, borderwidth=5, width=450, height=80)
depthFrame  = Frame(master=root, relief=SUNKEN, borderwidth=5, width=450, height=80)
cameraFrame = Frame(master=root, relief=SUNKEN, borderwidth=5, width=450, height=80)
VizFrame    = Frame(master=root, relief=SUNKEN, borderwidth=5, width=450, height=80)
dispFrame   = Frame(master=root, relief=SUNKEN, borderwidth=5, width=450, height=80)

Frames=[odomFrame,depthFrame,cameraFrame,VizFrame,dispFrame]
for i in range(5):

    Frames[i].grid(row=i, column=0, padx=5, pady=5, sticky=(S,N, E, W))


    root.columnconfigure(i, weight=1, minsize=450)
    root.rowconfigure(i, weight=1, minsize=100)

#put frame into place

labelO = Label(master=odomFrame,text =" Odometry Topic ")
labelO.pack(padx=5,pady=5)
labelD = Label(master=depthFrame,text =" Depth Topic ")
labelD.pack(padx=5,pady=5)

labelC = Label(master=cameraFrame,text =" Camera Topic ")
labelC.pack(padx=5,pady=5)

labelV = Label(master=VizFrame,text =" Visualization Topic ")
labelV.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
labelDi= Label(master= dispFrame, text =" Arguments")
labelDi.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
# VIZ FRAME

que_entry= Entry(master=VizFrame,width=10)
que_entry.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
quelabel = Label(master=VizFrame, text= " Queue Size ")
quelabel.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
btn_convert = Button(master=VizFrame,text="Add",command=replace_queue)
btn_convert.grid(row=1, column=2, sticky="ew", padx=5, pady=5)
#rviz
btn_rvizt = Button(master=VizFrame,text="Yes",command=rvizt)
btn_rvizt.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
btn_rvizf = Button(master=VizFrame,text="No",command=rvizf)
btn_rvizf.grid(row=2, column=1, sticky="ew", padx=5, pady=5)
rvizlabel = Label(master=VizFrame, text= " RVIZ ")
rvizlabel.grid(row=2, column=2, sticky="ew", padx=5, pady=5)
#rtabmapviz

btn_rmvizt = Button(master=VizFrame,text="Yes",command=rmvizt)
btn_rmvizt.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
btn_rmvizf = Button(master=VizFrame,text="No",command=rmvizf)
btn_rmvizf.grid(row=3, column=1, sticky="ew", padx=5, pady=5)
rmvizlabel = Label(master=VizFrame, text= " rtabmapviz ")
rmvizlabel.grid(row=3, column=2, sticky="ew", padx=5, pady=5)

# delete database
btn_bd = Button(master=VizFrame,text="Yes",command=db)
btn_bd.grid(row=4, column=0, sticky="ew", padx=5, pady=5)
btn_bd = Button(master=VizFrame,text="No",command=dbn)
btn_bd.grid(row=4, column=1, sticky="ew", padx=5, pady=5)
bdlabel = Label(master=VizFrame, text= " Delete Maps Stored ")
bdlabel.grid(row=4, column=2, sticky="ew", padx=5, pady=5)








# DISP FRAME
disp_= Label(master= dispFrame, wraplength=400, text =" roslaunch rtabmap_ros rtabmap.launch")
disp_.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
root.mainloop()