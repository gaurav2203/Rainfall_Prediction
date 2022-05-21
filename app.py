import streamlit as st
import pandas as pd 
import numpy as np 
import joblib

header= st.container()
body= st.container()
side_bar= st.container()
pred= st.container()

def get_data(filename):
   cat= joblib.load('models/cat.pkl')

   df= pd.read_csv(filename)
   return df, cat

df, cat= get_data('weatherAUS.csv')

with header:
   #st.image('rain_banner.jpg')
   st.title('Rainfall Prediction')
   st.write('')
   st.write('')

location_mapper= ['Portland', 'Cairns', 'Walpole', 'Dartmoor', 'MountGambier',
       'NorfolkIsland', 'Albany', 'Witchcliffe', 'CoffsHarbour', 'Sydney',
       'Darwin', 'MountGinini', 'NorahHead', 'Ballarat', 'GoldCoast',
       'SydneyAirport', 'Hobart', 'Watsonia', 'Newcastle', 'Wollongong',
       'Brisbane', 'Williamtown', 'Launceston', 'Adelaide', 'MelbourneAirport',
       'Perth', 'Sale', 'Melbourne', 'Canberra', 'Albury', 'Penrith',
       'Nuriootpa', 'BadgerysCreek', 'Tuggeranong', 'PerthAirport', 'Bendigo',
       'Richmond', 'WaggaWagga', 'Townsville', 'PearceRAAF', 'SalmonGums',
       'Moree', 'Cobar', 'Mildura', 'Katherine', 'AliceSprings', 'Nhil',
       'Woomera', 'Uluru']
windgustdir_mapper = ['NNW', 'NW', 'WNW', 'N', 'W', 'WSW', 'NNE', 'S', 'SSW', 'SW', 'SSE',
       'NE', 'SE', 'ESE', 'ENE', 'E']
winddir9am_mapper = ['NNW', 'N', 'NW', 'NNE', 'WNW', 'W', 'WSW', 'SW', 'SSW', 'NE', 'S',
       'SSE', 'ENE', 'SE', 'ESE', 'E']
winddir3pm_mapper = ['NW', 'NNW', 'N', 'WNW', 'W', 'NNE', 'WSW', 'SSW', 'S', 'SW', 'SE',
       'NE', 'SSE', 'ENE', 'E', 'ESE']


with side_bar:
   st.sidebar.header('Input Parameters')
   def mapper_fun(feature, mapper):
      for num, loc in enumerate(mapper):
         if loc == feature:
            return num+1

   def report():
      with st.form(key='form1'):
         with st.sidebar:
            Location= st.selectbox('Location', ('Portland', 'Cairns', 'Walpole', 'Dartmoor', 'MountGambier',
               'NorfolkIsland', 'Albany', 'Witchcliffe', 'CoffsHarbour', 'Sydney',
               'Darwin', 'MountGinini', 'NorahHead', 'Ballarat', 'GoldCoast',
               'SydneyAirport', 'Hobart', 'Watsonia', 'Newcastle', 'Wollongong',
               'Brisbane', 'Williamtown', 'Launceston', 'Adelaide', 'MelbourneAirport',
               'Perth', 'Sale', 'Melbourne', 'Canberra', 'Albury', 'Penrith',
               'Nuriootpa', 'BadgerysCreek', 'Tuggeranong', 'PerthAirport', 'Bendigo',
               'Richmond', 'WaggaWagga', 'Townsville', 'PearceRAAF', 'SalmonGums',
               'Moree', 'Cobar', 'Mildura', 'Katherine', 'AliceSprings', 'Nhil',
               'Woomera', 'Uluru'))
            MinTemp= st.slider('Minimum Temprature', df.MinTemp.min(), df.MinTemp.max(), df.MinTemp.mean())
            MaxTemp= st.slider('Maximum Temprature', df.MaxTemp.min(), df.MaxTemp.max(), df.MaxTemp.mean())
            Rainfall= st.slider('Rainfall', df.Rainfall.min(), df.Rainfall.max(), df.Rainfall.mean())
            Evaporation= st.slider('Evaporation', df.Evaporation.min(), df.Evaporation.max(), df.Evaporation.mean())
            Sunshine= st.slider('Sunshine', df.Sunshine.min(), df.Sunshine.max(), df.Sunshine.mean())
            WindGustDir= st.selectbox('WindGustDir', ('NNW', 'NW', 'WNW', 'N', 'W', 'WSW', 'NNE', 'S', 'SSW', 'SW', 'SSE',
               'NE', 'SE', 'ESE', 'ENE', 'E'))
            WindGustSpeed= st.slider('WindGustSpeed', df.WindGustSpeed.min(), df.WindGustSpeed.max(), df.WindGustSpeed.mean())
            WindDir9am= st.selectbox('WindDir9am',('NNW', 'N', 'NW', 'NNE', 'WNW', 'W', 'WSW', 'SW', 'SSW', 'NE', 'S',
               'SSE', 'ENE', 'SE', 'ESE', 'E'))
            WindDir3pm= st.selectbox('WindDir3am',('NW', 'NNW', 'N', 'WNW', 'W', 'NNE', 'WSW', 'SSW', 'S', 'SW', 'SE',
               'NE', 'SSE', 'ENE', 'E', 'ESE'))
            WindSpeed9am= st.slider('WindSpeed9am', df.WindSpeed9am.min(), df.WindSpeed9am.max(), df.WindSpeed9am.mean())
            WindSpeed3pm= st.slider('WindSpeed3pm', df.WindSpeed3pm.min(), df.WindSpeed3pm.max(), df.WindSpeed3pm.mean())
            Humidity9am= st.slider('Humidity9am', df.Humidity9am.min(), df.Humidity9am.max(), df.Humidity9am.mean())
            Humidity3pm= st.slider('Humidity3pm', df.Humidity3pm.min(), df.Humidity3pm.max(), df.Humidity3pm.mean())
            Pressure9am= st.slider('Pressure9am', df.Pressure9am.min(), df.Pressure9am.max(), df.Pressure9am.mean())
            Pressure3pm= st.slider('Pressure3pm', df.Pressure3pm.min(), df.Pressure3pm.max(), df.Pressure3pm.mean())
            Cloud9am= st.slider('Cloud9am', df.Cloud9am.min(), df.Cloud9am.max(), df.Cloud9am.mean())
            Cloud3pm= st.slider('Cloud3pm', df.Cloud3pm.min(), df.Cloud3pm.max(), df.Cloud3pm.mean())
            Temp9am= st.slider('Temp9am', df.Temp9am.min(), df.Temp9am.max(), df.Temp9am.mean())
            Temp3pm= st.slider('Temp3pm', df.Temp3pm.min(), df.Temp3pm.max(), df.Temp3pm.mean())
            RainToday= st.selectbox('RainToday', ('Yes', 'No'))
            Date_month= st.slider('Date_month', 1, 12, 6)
            Date_day= st.slider('Date_day', 1, 31, 15)
            submit= st.form_submit_button(label= 'Submit')

      report= {
         'Location': Location,
         'MinTemp': MinTemp,
         'MaxTemp': MaxTemp,
         'Rainfall': Rainfall,
         'Evaporation': Evaporation,
         'Sunshine': Sunshine,
         'WindGustDir': WindGustDir,
         'WindGustSpeed': WindGustSpeed,
         'WindDir9am': WindDir9am,
         'WindDir3pm': WindDir3pm,
         'WindSpeed9am': WindSpeed9am,
         'WindSpeed3pm': WindSpeed3pm,
         'Humidity9am': Humidity9am,
         'Humidity3pm': Humidity3pm,
         'Pressure9am': Pressure9am,
         'Pressure3pm': Pressure3pm,
         'Cloud9am': Cloud9am,
         'Cloud3pm': Cloud3pm,
         'Temp9am': Temp9am,
         'Temp3pm': Temp3pm,
         'RainToday': RainToday,
         'Date_month': Date_month,
         'Date_day': Date_day

      }
      orig= pd.DataFrame(report, index=[0])
      report['Location']= mapper_fun(report['Location'], location_mapper)
      report['WindGustDir']= mapper_fun(report['WindGustDir'], windgustdir_mapper)
      report['WindDir9am']= mapper_fun(report['WindDir9am'], winddir9am_mapper)
      report['WindDir3pm']= mapper_fun(report['WindDir3pm'], winddir3pm_mapper)
      report['RainToday']= 1 if report['RainToday']=='Yes' else 0
      features= pd.DataFrame(report, index=[0])
      return orig,features

with body:
   orig, data= report()
   st.write(orig)
   st.write('')
   st.write('')


with pred:
   cat_pred= cat.predict(data)

   if cat_pred[0] == 1:
      st.image('static/rainy.jpg')
      st.write('**It will Rain**')
   else:
      st.image('static/not_rainy.jpg')
      st.write('**It will not Rain**')
