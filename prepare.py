import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


def prep_telco(telco_df):
    
    '''This function is to prepare and clean the dataset of telco. After running the function it is ready for exploration and
    analysis, with the cleaned verison of the dataset'''
        
    telco_df = telco_df.drop(columns=['payment_type_id', 'internet_service_type_id', 'contract_type_id'])
    
    telco_df['gender_encoded'] = telco_df.gender.map({'Female': 1, 'Male': 0})

    telco_df['partner_encoded'] = telco_df.partner.map({'Yes': 1, 'No': 0})

    telco_df['dependents_encoded'] = telco_df.dependents.map({'Yes': 1, 'No': 0})

    telco_df['phone_service_encoded'] = telco_df.phone_service.map({'Yes': 1, 'No': 0})

    telco_df['paperless_billing_encoded'] = telco_df.paperless_billing.map({'Yes': 1, 'No': 0})

    telco_df['churn_encoded'] = telco_df.churn.map({'Yes': 1, 'No': 0})
    
    
    dummy_df = pd.get_dummies(telco_df[['multiple_lines', 'online_security', 
                              'online_backup', 'device_protection', 
                              'tech_support', 'streaming_tv',   'streaming_movies',
                              'contract_type', 'internet_service_type', 'payment_type']],
                              drop_first = False)
    
    
    telco_df = pd.concat([telco_df, dummy_df], axis = 1)
    
    return telco_df    


def train_val_test(df,col):
    seed = 42
    
    ''' This function is to split our data into our train, validate, and test subsets. We put in a dataframe
    and our target variable to then return the subsets of train, validate and test.'''
    
    train, test = train_test_split(df, train_size = 0.7, random_state = seed, stratify = df[col])
    
    validate, test = train_test_split(train, train_size = 0.5, random_state = seed, stratify = train[col])
    
    return train, validate, test





