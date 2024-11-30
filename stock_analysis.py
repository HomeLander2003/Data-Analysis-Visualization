mport logging
from tkinter.font import BOLD
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s [line %(lineno)d]')


class A:

   file_path=r"ipl_2025_auction_players.csv"

   def __init__(self):
      self.file_process=self.file_path
      self.filee=None
      
   
   def clean_file(self,file_path):
      try:
        
            self.filee=pd.read_csv(file_path)
            
            print(self.filee.head(10))
            print(self.filee.info())
            print(self.filee.isnull().sum())
            print("Duplicate rows :" , self.filee.duplicated().sum())

            if self.filee.duplicated().sum()>0:
               self.filee.drop_duplicates(inplace=True)
               self.filee.reset_index(drop=True,inplace=True)

            print(self.filee.info())
            print("Duplicate rows :" , self.filee.duplicated().sum())

            if "Team" in self.filee.columns:  # Check if the "Team" column exists
               self.filee["Team"] = self.filee["Team"].replace('-', "not decided")  

            print(self.filee.tail(20))

            return self.filee

      except FileNotFoundError as e:
         logging.error("File not found error: %s", e)
      except Exception as e:
         logging.error("An error occurred during file cleaning: %s", e)

   def analyze_visulaize_file(self):
      
      if self.filee is not None:
         print(self.filee.describe())
         print(self.filee.dtypes)

         gr1=self.filee.groupby(["Type"])["Type"].count()
         print(gr1)
         print()
         gr2=self.filee.groupby(["Team"])["Players"].count()
         print(gr2)
         print()
   
         print()
         print(gr1.ndim)
         print(gr2.ndim)

      
      
         plt.figure(figsize=(10,6))
         plt.title("Player Type Distribution",fontsize=25,weight=BOLD,color="purple",loc="left")

         # plt.pie(gr1.values,labels=gr1.index,autopct='%1.1f%%',textprops={'color':'black', 'fontsize': 9, 'weight': 'bold'},shadow=True
         #        ,explode=[0.05,0.05,0.05,0.05],pctdistance=1.15,labeldistance=1.275)
         
         for index, val in enumerate(gr2.values):
            plt.text(index, val + 2,  # Position the text above the bar
               str(val), ha='center', va='bottom', fontsize=10, color='black',weight="bold")

         plt.bar(gr2.index,gr2.values,label="Players in each team")
         
         plt.legend(loc="upper left",shadow=True)
         plt.show()
         

      else:
         logging.error("No file to analyze and visualize....... ")


if __name__=="main":
   a=A()
   print("******************Cleaning File**************")
   print()

   a.clean_file(file_path=a.file_process)
   print()

   print("***************Analyzing and visualizing file***************")
   a.analyze_visulaize_file()
