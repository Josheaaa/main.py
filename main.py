import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

class CountryStatistics:

    def __init__(self):


        file = "Project_File.xlsx"
        xls = pd.ExcelFile(file)



        self.df = xls.parse(0,usecols=[0,1,2,3,4,5,6,7,8,9,10,11,12],
                            names=["Year","Brunei","Indonesia","Malaysia","Philippines","Thailand","Viet Nam","Myanmar","Japan","Hong Kong","China","Taiwan","Korea"])
        self.df = self.df.replace(['na'], 0)
        self.splits = self.df['Year'].str.split(' ', n=1, expand=True)
        self.df = self.df.assign(year=self.splits[0])
        self.df = self.df.assign(month=self.splits[1])

        self.whatIwant = self.df[self.df["year"].str.contains("1998")]
        self.whatIwant = self.df[self.df["month"].str.contains("Jan")]



        self.whatIwant = self.df[
            (self.df["year"].astype(int) >= 1998)&
            (self.df["year"].astype(int) <= 2007)
        ]




    def Top3Countries2002StaticMean(self):
         self.filter=self.df[290: 301]["Japan"].mean()
         self.filter1=self.df[290: 301]["Indonesia"].mean()
         self.filter2 = self.df[290: 301]["China"].mean()
         print(f'The Mean number of visitors in Japan from 2002 is {self.filter}.')
         print(f'The Mean number of visitors in Indonesia from 2002 is {self.filter1}.')
         print(f'The Mean number of visitors in China from 2002 is {self.filter2}.')

    #     print(f'The total number of Visitors from Indonesia {self.Total1}.')
    def Top3Countries2002StaticMedian(self):
        self.filters=self.df[290: 301]["Japan"].median()
        self.filters1 = self.df[290: 301]["Indonesia"].median()
        self.filters2 = self.df[290: 301]["China"].median()
        print(f'The Median number of visitors in Japan from 2002 is {self.filters}.')
        print(f'The Median number of visitors in Indonesia from 2002 is {self.filters1}.')
        print(f'The Median number of visitors in China from 2002 is {self.filters2}.')



    def Top3Countries2002StaticSum(self):
        self.filterss = self.df[290: 301]["Japan"].sum()
        self.filterss1 = self.df[290: 301]["Indonesia"].sum()
        self.filterss2 = self.df[290: 301]["China"].sum()
        print(f'The Sum number of visitors in Japan from 2002 is {self.filterss}.')
        print(f'The Sum number of visitors in Indonesia from 2002 is {self.filterss1}.')
        print(f'The Sum number of visitors in China from 2002 is {self.filterss2}.')



    def Top3CountrieswiththemostVisitors(self):
         self.top3Countries = pd.DataFrame(self.df, columns=['Indonesia','Japan','China'])
         print(f'The top  3 countries with the most visitors are {list(self.top3Countries)}.')


    def getChina2002Visitors(self):
        self.filterss2 = self.df[290: 301]["China"].sum()
        return self.df[290: 301]["China"].sum()





    # def SumAllCountries(self):
    #
    #     self.Total = self.df["Brunei"].sum()
    #     self.Total1 = self.df["Indonesia"].sum()
    #     self.Total2 = self.df["Malaysia"].sum()
    #     self.Total3 = self.df["Philippines"].sum()
    #     self.Total4 = self.df["Thailand"].sum()
    #     self.Total5 = self.df["Viet Nam"].sum()
    #     self.Total6 = self.df["Myanmar"].sum()
    #     self.Total7 = self.df["Japan"].sum()
    #     self.Total8 = self.df["Hong Kong"].sum()
    #     self.Total9 = self.df["China"].sum()
    #     self.Total10 = self.df["Taiwan"].sum()
    #     self.Total11 = self.df["Korea"].sum()

        #print(self.Total)
        #print(self.Total1)
        #print(self.Total2)
        #print(self.Total3)
        #print(self.Total4)
        #print(self.Total5)
        #print(self.Total6)
        #print(self.Total7)
        #print(self.Total8)
        #print(self.Total9)
        #print(self.Total10)
        #print(self.Total11)






    # def VisitorNumbersFromTop3Countries(self):
    #
    #     self.total1 = self.df['Indonesia'].sum()
    #     self.total7 = self.df['Japan'].sum()
    #     self.total9 = self.df['China'].sum()
    #
    #     print(f'The total number of Visitors from Indonesia {self.Total1}.')
    #     print(f'The total number of Visitors from Japan {self.Total7}.')
    #     print(f'The total number of Visitors from China {self.Total9}.')


    # def MeanNumberFromTop3Countries(self):
    #     self.mean = self.df['Indonesia'].mean()
    #     self.mean1 = self.df['Japan'].mean()
    #     self.mean2 = self.df['China'].mean()
    #
    #     print(f'The mean number of Visitors from Idonesia {self.mean}.')
    #     print(f'The mean number of Visitors from Japan {self.mean1}.')
    #     print(f'The mean number of Visitors from China {self.mean2}.')


    # def MedianNumberFromTop3Countries(self):
    #
    #     self.median = self.df['Indonesia'].median()
    #     self.median1 = self.df['Japan'].median()
    #     self.median2 = self.df['China'].median()
    #
    #     print(f'The median number of Visitors from Indonesia {self.median}.')
    #     print(f'The median number of Visitors from Japan {self.median1}.')
    #     print(f'The median number of Visitors from China {self.median2}.')


    def Chart1(self):
        self.whatIneed = self.whatIwant[
            (self.whatIwant["year"].astype(int) >= 2002)&
            (self.whatIwant["year"].astype(int) <= 2005)
        ]
        #print(self.whatIneed)

        plt.scatter(self.whatIneed['Japan'], self.whatIneed['year'])
        plt.show();





    def Chart2(self):
        self.ax = self.whatIneed['China'].plot(kind='bar', title="Visitors", figsize=(10,10), legend=True, fontsize=12)
        plt.show();


# #self.whatIwant = self.df[
#             (self.df["year"].astype(int) >= 1998)&
#             (self.df["year"].astype(int) <= 2007)
#         ]









asia = CountryStatistics()
asia.Top3CountrieswiththemostVisitors()
asia.Top3Countries2002StaticMean()
asia.Top3Countries2002StaticMedian()
asia.Top3Countries2002StaticSum()
# asia.SumAllCountries()
# asia.VisitorNumbersFromTop3Countries()
# asia.MeanNumberFromTop3Countries()
# asia.MedianNumberFromTop3Countries()
asia.Chart1()
asia.Chart2()
