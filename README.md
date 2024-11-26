# Data-Analysis-Visualization
import logging
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s [line %(lineno)d]')


class A:
    def __init__(self,file_path):
        self.filepath=file_path

class B:

    def __init__(self):
        self.filee = None 

    def file_clean(self,file_path):

         if os.path.isfile(file_path):

            self.filee=pd.read_csv(file_path)
            print(self.filee)
            print(self.filee.info())
            print(self.filee.columns)

            #printing null values and duplicate 
            print(self.filee.isnull().sum())
            print("duplicate rows found " , self.filee.duplicated().sum())
            #no null values and duplicate rows found so we are not using dropna and dropduplicate method

            #renaming unnamed column
            if 'Unnamed: 0' in self.filee.columns:
                self.filee.rename(columns={'Unnamed: 0':"Date"},inplace=True)

            #converting whole date info into single year
            if 'Date' in self.filee.columns:
             self.filee['Date']=pd.to_datetime(self.filee['Date']).dt.year
             
            print(self.filee.head(10)) 
                     

            return self.filee  

         else:
            logging.error("file not found.......")

    def file_analyze_visualize(self):

        if self.filee is not None:
          print(self.filee.columns)
          print(self.filee.describe())

          samp = self.filee.groupby("Date")[["Open", "Close"]].max().reset_index()
          print(samp)
          print(samp.columns)
          samp = self.filee.groupby("Date")[["High", "Low"]].max().reset_index()
          print(samp)
          print(samp.columns)
          
          plt.style.use("dark_background")
          plt.figure(figsize=(10,6))

          #using line plot
          # plt.plot(samp["Date"],samp["Open"],label="Open Price",color="red")
          # plt.plot(samp["Date"],samp["Close"],label="Close Price",color="green")

          # using bar plot
          plt.bar(samp["Date"],samp["High"],label="High Price",color="red")
          plt.bar(samp["Date"],samp["Low"],label="Low Price",color="green")

        #   plt.scatter(samp["Date"],samp["Open"])
        #   plt.scatter(samp["Date"],samp["Close"])
          plt.title("Samsung Stock......",color="green",weight="bold",fontsize=50)
          plt.xlabel("Year(2007-2014)",labelpad=8,color="green",weight="bold",fontsize=20)
          plt.ylabel("Price(Open And Close)",labelpad=8,color="green",weight="bold",fontsize=20)
          plt.xticks(samp["Date"], rotation=90) 
          plt.tight_layout()
          plt.legend(shadow=True)
          plt.gray()
          plt.grid()
          plt.show()

        else:
           logging.error("No file to analyze......")


a=A(file_path=r"yourfilepath")
b=B()
print("******************Cleaning File**************")
print()
b.file_clean(a.filepath)
print()
print("***************Analyzing and visualizing file***************")
print()
b.file_analyze_visualize()
