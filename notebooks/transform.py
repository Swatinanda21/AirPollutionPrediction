import pandas as pd
import numpy as np
import os
def data_corr_coef():
    df=pd.read_csv('notebooks\Data\AQI_DELHI.csv')
    cols=['PM2.5','PM10','NO','NO2','NOx','NH3','SO2','CO','Ozone','Benzene','Toluene','RH','WS','WD','SR','BP','AT','RF','TOT-RF','AQI']

    data = df[cols]
    
    aqi_correlations = data.corr()['AQI'].drop('AQI')

    threshold = 0.80

    drop_cols = aqi_correlations[aqi_correlations.abs() > threshold].index.tolist()
    selected_features = [col for col in data.columns if col not in drop_cols and col != 'AQI']
    print("Features with correlation > 0.80 with AQI (to discard):", drop_cols)
    print("Selected features with acceptable correlation:", selected_features)

    return drop_cols
drop=data_corr_coef()
    
