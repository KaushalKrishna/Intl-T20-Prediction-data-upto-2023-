import numpy as np
import pandas as pd
import pickle
import streamlit as st

#pipeline = pickle.load(open('pipe.pkl','rb'))

teams = ['West Indies', 'England', 'South Africa', 'Pakistan',
       'New Zealand', 'Australia', 'Afghanistan', 'India', 'Bangladesh',
       'Sri Lanka', 'Zimbabwe']

cities = ['Lauderhill', 'St Lucia', 'Nottingham', 'Cape Town',
       'Johannesburg', 'Wellington', 'Dhaka', 'Harare', 'Dubai',
       'Hamilton', 'Chandigarh', 'Sharjah', 'Colombo', 'Pallekele',
       'Southampton', 'Melbourne', 'Durban', 'Bridgetown', 'Auckland',
       'Kolkata', 'Mirpur', 'London', 'Sydney', 'Centurion',
       'Christchurch', 'Perth', 'Barbados', 'Mumbai', 'Lahore', 'Karachi',
       'Mount Maunganui', 'Cardiff', 'Abu Dhabi', 'Manchester',
       'Adelaide', 'Delhi', 'Ahmedabad', 'Gros Islet', 'Brisbane',
       'Lucknow']

st.title("International T20 Score Predictor")

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox("Select the batting team",sorted(teams))
    
with col2:
    bowling_team = st.selectbox("Select the bowling team",sorted(teams))
    
city = st.selectbox('Select city', sorted(cities))

col3,col4,col5, col6 = st.columns(4)

with col3:
    current_score = st.number_input('Current Score:')

with col4:
    overs = st.number_input('How many overs done?')

with col5:
    wickets_rem = st.number_input('How many wickets remaining?')
    
with col6:
    balls = st.number_input('How many balls in this over?')

col7, col8 = st.columns(2)

with col7:
    last_five = st.number_input("Runs scored in last 5 overs:")
    
with col8:
    powerplay = st.checkbox("Is it powerplay?",0)
    
if st.button("Predict Score"):
    wickets = 10 - wickets_rem
    crr = current_score/(overs*6 + balls)
    balls_remaining = 120 - balls
    death_overs = 1 if overs>=15 else 0
    top_order = 1 if wickets < 3 else 0
    middle_order = 1 if (wickets >= 3)&(wickets<=4) else 0
    bottom_order = 1 if (wickets >= 5)&(wickets<=7) else 0
    tail = 1 if wickets>7 else 0
    pressure = 1 if (crr<7)&(overs>=2) else 0
    agresive = 1 if last_five>=45 else 0
    balls_left = overs*6 + balls
    input_df = pd.DataFrame({'batting_team':batting_team, 'city':city, 'bowling_team':bowling_team, 'score':current_score, 'balls_left':balls_left,
       'wickets_left':wickets_rem, 'crr':crr, 'powerplay':powerplay, 'death_overs':death_overs, 'top_order_batsmen':top_order,
       'middle_order_batsmen':middle_order, 'lower_order_batsmen':bottom_order, 'tail_order_batsmen':tail,
       'pressure_play':pressure, 'last_5_overs_score':last_five, 'agressive':agresive}, index=[0])
    
    result = pickle.load(open('pipe.pkl', 'rb')).predict(input_df)
    
    st.header("Predicted Score should be between: " + str(int(result[0])-8) + " - " + str(int(result[0])+8))
    
    pass


