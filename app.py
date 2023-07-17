import numpy as np
import pandas as pd
import pickle
import streamlit as st

pipeline = pickle.load(open('pipe.pkl','rb'))

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

st.title("International T20 Target Score Predictor")
st.markdown("""Predict the __`target score`__ for the T20 match you're watching right now with this tool and stay ahead of the game! """)
col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox("Select the batting team",sorted(teams))
    
with col2:
    bowling_team = st.selectbox("Select the bowling team",sorted(teams))
    
city = st.selectbox('Select city', sorted(cities))

col3, col4 = st.columns(2)

with col3:
    current_score = st.number_input('Current Score:')

with col4:
    wickets = st.number_input('How many wickets down?')

col5, col6, col7 = st.columns(3)

with col5:
    overs = st.number_input('How many overs done?')

with col6:
    balls = st.number_input('How many balls left in this over?')

with col7:
    last_five = st.number_input("Runs scored in last 5 overs:")
    

    
if st.button("Predict Score"):
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
    powerplay = 1 if overs<=6 else 0
    balls = 6 - balls
    input_df = pd.DataFrame({'batting_team':batting_team, 'city':city, 'bowling_team':bowling_team, 'score':current_score, 'balls_left':balls_left,
       'wickets_left':wickets_rem, 'crr':crr, 'powerplay':powerplay, 'death_overs':death_overs, 'top_order_batsmen':top_order,
       'middle_order_batsmen':middle_order, 'lower_order_batsmen':bottom_order, 'tail_order_batsmen':tail,
       'pressure_play':pressure, 'last_5_overs_score':last_five, 'agressive':agresive}, index=[0])
    
    result = pipeline.predict(input_df)
    
    st.header("Predicted Score should be between: " + str(int(result[0])+10) + " - " + str(int(result[0])+20))
    
    pass



