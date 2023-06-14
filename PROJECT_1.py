#student management system
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk


class Student:
    def __init__(self,root):
        self.root=root
        self.geometry("1530x790+0+0")
        self.title("Student Management System")