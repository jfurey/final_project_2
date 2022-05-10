from tkinter import *
from scrape import *


class GUI():
    def __init__(self, window):
        '''
        Constructor to set default state of GUI.
        '''
        self.window = window
        self.window.title('Adopt a Dog')
        
        self.frame_top = Frame(self.window)
        self.label_welcome = Label(self.frame_top, text='Welcome! We\'re here to help you find your next dog!', font=("Arial", 16, 'bold'), fg='#660099')
        self.label_select_age = Label(self.frame_top, text='Please select the age group you\'re interested in and click SUBMIT:', font=("Arial", 14))
        self.label_welcome.pack(pady=30)
        self.label_select_age.pack()
        self.frame_top.pack()
        
        self.frame_middle = Frame(self.window)
        self.radio_1 = IntVar()
        self.radio_1.set(0)
        self.radio_baby = Radiobutton(self.frame_middle, text='Baby', font=('Arial', 12), variable=self.radio_1, value=0)
        self.radio_young = Radiobutton(self.frame_middle, text='Young', font=('Arial', 12), variable=self.radio_1, value=1)
        self.radio_adult = Radiobutton(self.frame_middle, text='Adult', font=('Arial', 12), variable=self.radio_1, value=2)
        self.radio_senior = Radiobutton(self.frame_middle, text='Senior', font=('Arial', 12), variable=self.radio_1, value=3)
        self.radio_baby.pack(side='top', anchor=W)
        self.radio_young.pack(side='top', anchor=W)
        self.radio_adult.pack(side='top', anchor=W)
        self.radio_senior.pack(side='top', anchor=W)
        self.frame_middle.pack()
        
        self.frame_bottom = Frame(self.window)
        self.button_submit = Button(self.frame_middle, text='SUBMIT', font=('Arial', 14, 'bold'), bg='#ffcc00', command=self.clicked)
        self.label_results = Label(self.frame_bottom, text='', font=("Arial", 16, 'bold'), fg='#660099')
        self.button_submit.pack(pady=20)
        self.label_results.pack()
        self.frame_bottom.pack()
        
    def clicked(self):
        '''
        Method to perform web scrape and output results when user clicks SUBMIT button.
        '''
        age_selected = self.radio_1.get()
        web_scrape(age_selected)
        self.label_results.config(text='Results generated!')