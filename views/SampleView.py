from tkinter import *
from tkinter import ttk

class SampleView:

    def __init__(self):
        window = Tk()
        window.title("Simple Application")

        # Create a tab like structure
        tab_control = ttk.Notebook(window)

        # Create Empty containers
        page1_frame = ttk.Frame(tab_control)
        page2_frame = ttk.Frame(tab_control)
        page3_frame = ttk.Frame(tab_control)

        # add the containers into to the tabs
        tab_control.add(page1_frame,text="PAGE 1")
        tab_control.add(page2_frame, text="PAGE 2")
        tab_control.add(page3_frame, text="PAGE 3")

        tab_control.pack()

        self.page1(page1_frame)
        self.page2(page2_frame)
        self.page3(page3_frame)

        window.mainloop()


    def page1(self,frame):

        l1 = Label(frame,text="This is a text from page 1")
        l1.pack()
        print("page 1")

    def page2(self,frame):
        l1 = Label(frame, text="This is a text from page 2")
        l1.pack()
        print("page 2")

    def page3(self,frame):
        l1 = Label(frame, text="This is a text from page 3")
        l1.pack()
        print("page 3")

sample = SampleView()
