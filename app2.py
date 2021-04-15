import tkinter as tk
from tkinter import ttk as ttk
from tkinter import filedialog as fd

import pandas as pd
import numpy as np

###############################

class app(tk.Tk):

    def __init__(self):
        super(app, self).__init__()

        self.title('tutaj jest tytuł')
        self.geometry('500x500')

        self.wrapper1 = ttk.LabelFrame(self, text='wrapper1')
        self.wrapper2 = ttk.LabelFrame(self, text='wrapper2')
        self.wrapper3 = ttk.LabelFrame(self, text='wrapper3')
        self.wrapper4 = ttk.LabelFrame(self, text='wrapper3')


        self.wrapper1.pack(fill='both', expand='yes', padx=10, pady=10)
        self.wrapper2.pack(fill='both', expand='yes', padx=10, pady=10)
        self.wrapper3.pack(fill='both', expand='yes', padx=10, pady=10)
        self.wrapper4.pack(fill='both', expand='yes', padx=10, pady=10)


        # wrapper1
        self.base_path_btn = ttk.Button(self.wrapper1,
                                        text='Wybierz bazę',
                                        command=self.find_and_ETL_base)

        self.base_path_lbl = ttk.Label(self.wrapper1,
                                       text='')
        
        self.base_path_btn.grid(column=0, row=0, sticky='W')
        self.base_path_lbl.grid(column=0, row=1, sticky='W')

        # wrapper2
        


        # wrapper3
        self.trv = ttk.Treeview(self.wrapper3, show='headings', height='6')
        self.trv.pack()






    def find_and_ETL_base(self):
        self.base_path = fd.askopenfilename()
        self.base_path_lbl.configure(text=self.base_path)
        columns = [
            "Sales order","Reference number",
            "Line number", "Item number",
            "Text", "Quantity", "Unit"
        ]
        self.base = pd.read_excel(self.base_path)[columns].head(10)
        self.insert_trv()
  

    def ask_for_export_base_path(self):
        fd.asksaveasfilename()

    def insert_trv(self):
        df_col = self.base.columns.values
        self.trv['columns']=(df_col)
        for i in range(len(df_col)):
            self.trv.column(i, width=100)
            self.trv.heading(i, text=df_col[i])
            for j in range(len(self.base.index)):
                self.trv.insert('', 'end', values=(self.base[df_col[i]][j]))
        
            









root = app()
root.mainloop()
