
import pandas as pd 
from datetime import datetime
import numpy as np

class cohort_analysis():
    def assign_month_id(self,df):
        '''
        Assigns month id, 
        '''
        df['month_id'] = np.arange(len(df))+1
        return df 

    def create_cohort(self, input_df):
        """
        Creates Cohorts

        """
        first_month = input_df.groupby('CustomerID')['datetime'].min().apply(lambda x: x.to_period('M'))
        output_df = input_df.merge(first_month,on='CustomerID')
        output_df.rename(columns={"datetime_y":"Cohort_ID"},inplace=True)
        return output_df

    def analysis(self,input_df,user_id='user_id'):
        '''
        Takes input as pandas dataframe
        and creates data frame with the cohorts and analysis
        '''
        input_df = input_df[['CustomerID','datetime']].drop_duplicates()
        input_df['month_purchase'] = input_df['datetime'].apply(lambda x: x.to_period('M'))
        cohort_df = self.create_cohort(input_df)
        monthly_ids = cohort_df.groupby(['CustomerID','Cohort_ID']).apply(self.assign_month_id)
        cohort_table = monthly_ids.pivot_table(index='Cohort_ID',values='CustomerID',columns='month_id',aggfunc=pd.Series.nunique)
        return cohort_table


# ca = cohort_analysis()
# input_df = pd.read_csv('./data.csv',encoding='latin',parse_dates={'datetime':['InvoiceDate']})
# ca.analysis(input_df)



