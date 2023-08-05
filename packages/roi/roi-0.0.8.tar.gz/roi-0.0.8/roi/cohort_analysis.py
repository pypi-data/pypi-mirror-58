
import pandas as pd 
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

class cohort_analysis():
    """
    Input:
    CustomerID,
    InvoiceDate,
    Cohort
    """
    cohort_table = None
    retention_table= None
    pivoted = None
    def assign_id(self,df):
        df['Cohort_ID']=np.arange(len(df))+1
        return df
    
    def analysis(self,input_df):
        input_df['Purchase_month'] = input_df['datetime'].apply(lambda x: x.to_period('M'))
        if(1):
            # create cohort based on first month, if cohort is not known 
            print('Creating Cohorts')
            first_month_df = input_df.groupby('CustomerID')['datetime'].apply(lambda x: min(x).to_period('M'))
            merged_df = pd.merge(input_df,first_month_df,on='CustomerID').rename(columns={'datetime_y':'Cohort'})
            pivoted = merged_df.pivot_table(index=['Cohort','Purchase_month'],values=['UnitPrice','CustomerID'],aggfunc={'UnitPrice':np.sum,'CustomerID':pd.Series.nunique})
            self.pivoted=pivoted.groupby(['Cohort']).apply(self.assign_id)
            self.cohort_table = self.pivoted.pivot_table(index=['Cohort'],columns=['Cohort_ID'])
            self.retention_table =self.cohort_table['CustomerID'].divide(self.cohort_table['CustomerID'][1],axis='rows')

        return self.cohort_table
    def plot_retention(self):
      """
      Input: 
      """
      sns.set(style='white')
      fig,ax = plt.subplots(figsize=self.retention_table.shape)
      sns.heatmap(self.retention_table,annot=True,fmt='.0%')
      ax.xaxis.tick_top()
      ax.xaxis.set_label_position('top') 
      ax.tick_params(axis=u'both', which=u'both',length=0)