import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import logging
import os

logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s [line %(lineno)d] ')

class loadfile():
    def __init__(self,file_path):
        self.file=None
        if os.path.isfile(file_path):
            try:
                 self.file=pd.read_csv(file_path)
                 print(self.file)
            except Exception as e:
                logging.error(e)
        
        else:
                logging.error("Invalid file path........")


class cleanfile(loadfile):
    def __init__(self,file_path):
        super().__init__(file_path)

    def clean(self):
         
        if self.file is not None:

            try:
                print(self.file.info())
                
                if self.file.isnull().sum().sum()>0:
                    self.file.dropna(inplace=True)
                    logging.info("Null Value Dropped........")

                else:
                    logging.info("No Null Value Found")
                
                if self.file.duplicated().sum()>0:
                    self.file.drop_duplicates(keep="first",inplace=True)
                    self.file.reset_index(drop=True,inplace=True)
                    logging.info("Duplicate Value Dropped........")

                else:
                    logging.info("No Duplicates Found........")

                columns_to_drop=["Angina","Follow_Up"]

                for col in columns_to_drop:
                    if col in self.file.columns:
                        self.file.drop(col,axis=1,inplace=True)
                    
                        logging.info("Column dropped........")
                    else:
                        logging.error("Column not found to drop........")                

                
                print(self.file.columns)
                print(self.file.info())
            
            except Exception as e:
                logging.error(e)


class savefile(cleanfile):
    def __init__(self, file_path):
        super().__init__(file_path)

    def save(self):
        if self.file is not None:
            try:
                self.file.to_csv("heart_attack_youth_vs_adult_pakistan_mod.csv",index=False)
                logging.info("File has been Saved........")
            
            except Exception as e:
                logging.error(e)
        
        else:
            logging.error("Unable to save file........")

class analyzefile(savefile):

    def __init__(self, file_path):
        super().__init__(file_path)

    
    def analyze(self):

        if self.file is not None:
         
         try:

        #    gr=self.file.groupby("Gender")["Gender"].count()
        #    print(gr)
        #    print(gr.ndim)

        #    region_counts=self.file["Region"].value_counts()
        #    print(region_counts)

        #    gr2=self.file.groupby("Gender")["BMI"].mean()
        #    print(gr2)

        #    gr3=self.file.groupby("Gender")[["Smoker","Diabetes","Hypertension"]].count()
        #    print(gr3)
        #    print(gr3.ndim)

        #    long_data = gr3.reset_index().melt(id_vars="Gender",value_vars=["Smoker", "Diabetes", "Hypertension"], 
        #     var_name="Condition", value_name="Count")
        #    print(long_data)
        #    print(long_data.ndim)
        #    long_data["Count"] = pd.to_numeric(long_data["Count"], errors="coerce")


        #    gr4=self.file.groupby("Gender")[["Cholesterol_Level","BMI"]].mean()
        #    print(gr4)
        #    print(gr4.ndim)

        #    gr5=self.file.groupby("Age")[["Sleep_Hours","Blood_Pressure","Heart_Rate"]].mean()
        #    print(gr5)

           gr6=self.file[["Sleep_Hours","Blood_Pressure","Heart_Rate"]]
           correl=gr6.corr()
           print(correl)
          

        #    return gr,region_counts,gr2
         
        #    return gr4,gr5

           return correl

         except Exception as e: 
            logging.error(e)

        else:
            logging.error("Unable to analyze file........")
             


class visualizefile(analyzefile):
    def __init__(self, file_path):
        super().__init__(file_path)

    
    def pie1visualize(self,gr):

        if self.file is not None:
         try:
           
           plt.style.use("dark_background")
           plt.figure(figsize=(10,6))
           plt.title("Total Gender Count",weight="bold",fontsize=25,color="purple")
           plt.pie(gr.values,labels=gr.index,autopct='%1.1f%%',textprops={'fontsize':16,'weight':"bold",'color':"black"},startangle=90)
           plt.legend(shadow=True,loc="upper right",bbox_to_anchor=(0.95, 1))
           plt.show()

         except Exception as e:
            logging.error(e)

        else:
            logging.error("Unable to visualize file.........")


    def pie2visualize(self,region_counts):

        if self.file is not None:
         try:
           
           plt.style.use("dark_background")
           plt.figure(figsize=(10,6))
           plt.title("Regions",weight="bold",fontsize=25,color="purple")
           plt.pie(region_counts.values,labels=region_counts.index,autopct='%1.1f%%',textprops={'fontsize':16,'weight':"bold",'color':"black"},startangle=90)
           plt.legend(shadow=True,loc="upper right",bbox_to_anchor=(0.95, 1))
           plt.show()

         except Exception as e:
            logging.error(e)

        else:
            logging.error("Unable to visualize file.........")


    
    def pie3visualize(self,long_data):

        if self.file is not None:
         try:
           condition_data = long_data.groupby("Condition")["Count"].sum()

           plt.style.use("dark_background")
           plt.figure(figsize=(10,6))
           plt.title("Regions",weight="bold",fontsize=25,color="purple")
           plt.pie(condition_data.values,labels=condition_data.index,autopct='%1.1f%%',textprops={'fontsize':16,'weight':"bold",'color':"black"},startangle=90)
           plt.legend(shadow=True,loc="upper right",bbox_to_anchor=(0.95, 1))
           plt.show()

         except Exception as e:
            logging.error(e)

        else:
            logging.error("Unable to visualize file.........")


    
    def barplot1(self,gr2):

        if self.file is not None:
         try:
           
           plt.style.use("dark_background")
           plt.figure(figsize=(10,6))
           plt.title("BMI(Male and Femal AVG)",weight="bold",fontsize=25,color="purple")
           plt.ylabel("Body Mass Index" ,color="purple",weight="bold",fontsize=23,labelpad=20)
           plt.xlabel("Gender" ,color="purple",weight="bold",fontsize=23)

           for i,val in enumerate(gr2.values.round(2)):
            plt.text(i,val-2,str(val),ha="center",va="baseline",color="black",weight="bold")

           sns.barplot(x=gr2.index,y=gr2.values,palette="coolwarm")
           plt.show()

         except Exception as e:
            logging.error(e)

        else:
            logging.error("Unable to visualize file.........")

    
    def barplot2(self,gr4):

        if self.file is not None:
         try:
           
           plt.style.use("dark_background")
           plt.figure(figsize=(10,6))
           plt.title("Cholestrol_Level(Male and Female AVG With BMI)",weight="bold",fontsize=25,color="purple")
           plt.ylabel("Cholestrol_Level" ,color="purple",weight="bold",fontsize=23,labelpad=20)
           plt.xlabel("Gender" ,color="purple",weight="bold",fontsize=23)

           for i,val in enumerate(gr4["BMI"].values.round(2)):
            plt.text(i,val-2,f'BMI: {val}',ha="center",va="baseline",color="black",weight="bold")

           for i,val in enumerate(gr4["Cholesterol_Level"].values.round(2)):
            plt.text(i,val+1,f'CHOL_LVL: {val}',ha="center",va="bottom",color="white",weight="bold")

           sns.barplot(x=gr4.index,y=gr4["Cholesterol_Level"],palette="coolwarm")
           plt.show()

         except Exception as e:
            logging.error(e)

        else:
            logging.error("Unable to visualize file.........")

    
      
    def barplot3(self,gr5):

        if self.file is not None:
         try:
           
           plt.style.use("dark_background")
           plt.figure(figsize=(10,6))
           plt.title("Sleep_Hours,Heart_Rate,Blood_Pressure(Male and Female)",weight="bold",fontsize=25,color="purple")
           plt.ylabel("Index" ,color="purple",weight="bold",fontsize=23,labelpad=20)
           plt.xlabel("AGE" ,color="purple",weight="bold",fontsize=23,labelpad=20)


           sns.barplot(x=gr5.index,y=gr5["Blood_Pressure"],color="red",label="Blood_pressure")
           sns.barplot(x=gr5.index,y=gr5["Heart_Rate"],color="green",label="Heart_Rate")
           sns.barplot(x=gr5.index,y=gr5["Sleep_Hours"],color="blue",label="Sleep_Hours")
           plt.legend(shadow=True,loc="upper right",bbox_to_anchor=(1.155, 1))
           plt.tight_layout()
           plt.xticks(rotation=90)
           plt.show()

         except Exception as e:
            logging.error(e)

        else:
            logging.error("Unable to visualize file.........")

            

    def heatmap(self,correl):
        plt.figure(figsize=(10,6))
        plt.title("Sleep_Hours,Heart_Rate,Blood_Pressure(Male and Female)",weight="bold",fontsize=25,color="purple")
        sns.heatmap(correl, annot=True, cmap="coolwarm", fmt=".1f", linewidths=0.015,vmin=-1, vmax=1)
        plt.show()

    
              
file_path=r"heart_attack_youth_vs_adult_pakistan.csv"

cf=visualizefile(file_path)
# cf.clean()
# cf.save()
# gr,region_counts,gr2=cf.analyze()
# long_data=cf.analyze()
# gr4,gr5=cf.analyze()
correl=cf.analyze()
# cf.pie1visualize(gr)
# cf.pie2visualize(region_counts)
# cf.pie3visualize(long_data)
# cf.barplot1(gr2)
# cf.barplot2(gr4)
# cf.barplot3(gr5)
cf.heatmap(correl)
