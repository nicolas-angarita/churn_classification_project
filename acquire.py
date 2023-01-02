import pandas as pd
import numpy as np
import os
from env import username, host, password

def get_connection(db, username=username, host=host, password=password):
    return f'mysql+pymysql://{username}:{password}@{host}/{db}'

def get_telco_data():
    '''
    This function is to get the telco dataset either from a local csv file or from SQL Ace to our working notebook to be able
    to use the data and perform various tasks using the data
    '''
    if os.path.isfile('telco.csv'):
        
        return pd.read_csv('telco.csv')
    
    else:
       
        url = get_connection('telco_churn')
        
        query = '''
        SELECT *
        FROM customers
        JOIN contract_types USING(contract_type_id)
        JOIN internet_service_types USING(internet_service_type_id)
        JOIN payment_types USING(payment_type_id);
        '''

        df = pd.read_sql(query, url)
        
        df.to_csv('telco.csv', index = False)

        return df                