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
#################CAMERA #######################33

def compressedt():
    s = disp_["text"]
    arg = s.split()
    for x in arg:
        if "compressed:=" in x:
            arg.remove(x)
    added = f" compressed:=true" + " "
    disp_["text"] = " ".join(arg) + added
def compressedf():
    s = disp_["text"]
    arg = s.split()
    for x in arg:
        if "compressed:=" in x:
            arg.remove(x)
    added = f" compressed:=false" + " "
    disp_["text"] = "  ".join(arg) + added

def rbgd_synct():
    s = disp_["text"]
    arg = s.split()
    for x in arg:
        if "rbgd_sync:=" in x:
            arg.remove(x)
    added = f" rbgd_sync:=true" + " "
    disp_["text"] = " ".join(arg) + added
def rbgd_syncf():
    s = disp_["text"]
    arg = s.split()
    for x in arg:
        if "rbgd_sync:=" in x:
            arg.remove(x)
    added = f" rbgd_sync:=false" + " "
    disp_["text"] = "  ".join(arg) + added
def rgb_topicadd():
    s=disp_["text"]
    arg= s.split()
    for x in arg:
        if "rgb_topic:=" in x:
            arg.remove(x)
    if  rgb_topic_entry.get() != "":
        added=f" rgb_topic:={rgb_topic_entry.get()} "+" "
        disp_["text"]=" ".join(arg)+added
def camera_info_topicadd():
    s=disp_["text"]
    arg= s.split()
    for x in arg:
        if "camera_info_topic:=" in x:
            arg.remove(x)
    if  camera_info_topic_entry.get() != "":
        added=f" camera_info_topic:={camera_info_topic_entry.get()} "+" "
        disp_["text"]=" ".join(arg)+added
###############ODom #############

########################Depth
def depth_topicadd():
    s=disp_["text"]
    arg= s.split()
    for x in arg:
        if "depth_topic:=" in x:
            arg.remove(x)
    if  depth_topic_entry.get() != "":
        added=f" depth_topic:={depth_topic_entry.get()} "+" "
        disp_["text"]=" ".join(arg)+added

root = Tk()

menu = Menu(root)
root.config(menu=menu)
root.resizable(width=FALSE, height=TRUE)
root.geometry('{}x{}'.format(600, 800))

# set up frames for GUI
odomFrame   = Frame(master=root, relief=SUNKEN, borderwidth=5, width=600, height=80)
depthFrame  = Frame(master=root, relief=SUNKEN, borderwidth=5, width=600, height=80)
cameraFrame = Frame(master=root, relief=SUNKEN, borderwidth=5, width=600, height=80)
VizFrame    = Frame(master=root, relief=SUNKEN, borderwidth=5, width=600, height=80)
dispFrame   = Frame(master=root, relief=SUNKEN, borderwidth=5, width=600, height=80)

Frames=[odomFrame,depthFrame,cameraFrame,VizFrame,dispFrame]
for i in range(4):

    Frames[i].grid(row=i, column=0, padx=5, pady=5, sticky=(S,N, E, W))


    root.columnconfigure(i, weight=1, minsize=600)
    root.rowconfigure(i, weight=1, minsize=100)


Frames[4].grid(row=4, column=0, padx=5, pady=5, sticky=(S,N, E, W))
root.columnconfigure(4, weight=6, minsize=600)
root.rowconfigure(4, weight=6, minsize=100)

#put frame into place

labelO = Label(master=odomFrame,text =" Odometry Topic ")
labelO.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
labelD = Label(master=depthFrame,text =" Depth Topic ")
labelD.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

labelC = Label(master=cameraFrame,text =" Camera Topic ")
labelC.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

labelV = Label(master=VizFrame,text =" Visualization Topic ")
labelV.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
labelDi= Label(master= dispFrame, text =" Arguments")
labelDi.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
####################### VIZ FRAME ###############################3

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
################################ CAMERA #######################################

#rbgd sync
btn_rbgd = Button(master=cameraFrame,text="Yes",command=rbgd_synct)
btn_rbgd.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
btn_rbgd = Button(master=cameraFrame,text="No",command=rbgd_syncf)
btn_rbgd.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
rbgdlabel = Label(master=cameraFrame, text= " rbgd_sync ")
rbgdlabel.grid(row=1, column=2, sticky="ew", padx=5, pady=5)

#compressed
btn_bd = Button(master=cameraFrame,text="Yes",command=compressedt)
btn_bd.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
btn_bd = Button(master=cameraFrame,text="No",command=compressedt)
btn_bd.grid(row=2, column=1, sticky="ew", padx=5, pady=5)
bdlabel = Label(master=cameraFrame, text= " compressed ")
bdlabel.grid(row=2, column=2, sticky="ew", padx=5, pady=5)

#rgb_topic
rgb_topic_entry= Entry(master=cameraFrame,width=10)
rgb_topic_entry.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
rgb_topiclabel = Label(master=cameraFrame, text= " rgb_topic ")
rgb_topiclabel.grid(row=3, column=1, sticky="ew", padx=5, pady=5)
rgb_topic_convert = Button(master=cameraFrame,text="Change",command=rgb_topicadd)
rgb_topic_convert.grid(row=3, column=2, sticky="ew", padx=5, pady=5)
rgb_dlabel = Label(master=cameraFrame,wraplength=220, text= "/camera/throttled/rgb/image_rect_color if rbgd_sync:=false on camera")
rgb_dlabel.grid(row=3, column=3, sticky="ew", padx=5, pady=5)

#camera_info
camera_info_topic_entry= Entry(master=cameraFrame,width=10)
camera_info_topic_entry.grid(row=4, column=0, sticky="ew", padx=5, pady=5)
camera_info_topiclabel = Label(master=cameraFrame, text= " camera_info_topic ")
camera_info_topiclabel.grid(row=4, column=1, sticky="ew", padx=5, pady=5)
camera_info_topic_convert = Button(master=cameraFrame,text="Change",command=camera_info_topicadd)
camera_info_topic_convert.grid(row=4, column=2, sticky="ew", padx=5, pady=5)
camera_info_topic_dlabel = Label(master=cameraFrame,wraplength=220, text= "/camera/throttled/rgb/camera_info if rbgd_sync:=false on cam")
camera_info_topic_dlabel.grid(row=4, column=3, sticky="ew", padx=5, pady=5)

################################ ODOM ###############33333

###################### DEPTH ##########
depth_topic_entry= Entry(master=depthFrame,width=10)
depth_topic_entry.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
depth_topiclabel = Label(master=depthFrame, text= " depth_info_topic ")
depth_topiclabel.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
depth_topic_convert = Button(master=depthFrame,text="Change",command=depth_topicadd)
depth_topic_convert.grid(row=1, column=2, sticky="ew", padx=5, pady=5)
depth_topic_dlabel = Label(master=depthFrame,wraplength=220, text= "/camera/throttled/depth_registered/image_raw if rbgd_sync:=false on cam")
depth_topic_dlabel.grid(row=1, column=3, sticky="ew", padx=5, pady=5)





################################## DISP FRAME #########################
disp_= Label(master= dispFrame, wraplength=600, text =" roslaunch rtabmap_ros rtabmap.launch")
disp_.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
root.mainloop()