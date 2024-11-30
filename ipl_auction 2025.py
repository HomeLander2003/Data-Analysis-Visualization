import logging
from tkinter.font import BOLD
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s [line %(lineno)d]')


class A:

   file_path=r"\ipl_2025_auction_players.csv"

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
            self.filee["Team"] = self.filee["Team"].replace('-', "TBD")  

         print(self.filee.tail(20))


         return self.filee

      except FileNotFoundError as e:
         logging.error("File not found error: %s", e)
      except Exception as e:
         logging.error("An error occurred during file cleaning: %s", e)

   def analyze_visualize_file(self):
      
      if self.filee is not None:
         try:
            print(self.filee.describe())
            print(self.filee.dtypes)

            gr1=self.filee.groupby(["Type"])["Type"].count()
            print(gr1)
            print()
            gr2=self.filee.groupby(["Team"])["Players"].count()
            print(gr2)
            print()
            gr3=self.filee.groupby(["Sold"])["Sold"].count()
            print(gr3)
      
            print()
            print(gr1.ndim)
            print(gr2.ndim)
            print(gr3.ndim)

         
            
            plt.style.use("dark_background")
            plt.figure(figsize=(10,6))
            plt.title("IPL 2025 AUCTION DETAILS",fontsize=25,weight=BOLD,color="purple",loc="left")


            #pie chart for player type
            # plt.pie(gr1.values,labels=gr1.index,autopct='%1.1f%%',textprops={'color':'black', 'fontsize': 9, 'weight': 'bold'},shadow=True
            #        ,explode=[0.05,0.05,0.05,0.05],pctdistance=1.15,labeldistance=1.275)


            #barchart for player distribution
            # for index, val in enumerate(gr2.values):
            #    plt.text(index, val + 2,  # Position the text above the bar
            #    str(val), ha='center', va='bottom', fontsize=10, color='white',weight="bold")
            # plt.bar(gr2.index,gr2.values,label="Players in each team")


            #barchart for player distribution per price
            for index, val in enumerate(gr3.values):
               plt.text(index, val + 2,  # Position the text above the bar
               str(val), ha='center', va='bottom', fontsize=10, color='white',weight="bold")
            plt.bar(gr3.index,gr3.values,label="Players Price",color="red",edgecolor="white")
            
            plt.legend(loc="upper left",shadow=True)
            plt.xticks(rotation=90)
            plt.tight_layout()
            plt.show()
         

         except KeyError as e:
            print(e)
         except AttributeError as e:
            print(e)

      else:
         logging.error("No file to analyze and visualize....... ")


   def save_file(self,path):
      if self.filee is not None:
        try:
            self.filee.to_csv(path, index=False)  
            logging.info(f"File has been saved at {path}")
        except Exception as e:
            logging.error(f"An error occurred while saving the file: {e}")

      
# if __name__=="main":
a=A()
print("******************Cleaning File**************")
print()

a.clean_file(file_path=a.file_process)
print()

print("***************Analyzing and visualizing file***************")
a.analyze_visualize_file()
print()
print("***************Analyzing and visualizing file***************")
a.save_file(path="ipl_mod.csv")
