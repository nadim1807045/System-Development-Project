# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 16:47:24 2022

@author: mahfu
"""

from flask import Flask,render_template
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import imageio
import cv2
import winsound


app = Flask(__name__)

from Project import Window

@app.route("/")
def hello():
    root = Tk()
    
    #root.geometry("%dx%d"%(535, 380))

    
    Window(root)
    root.mainloop()
    
    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True)