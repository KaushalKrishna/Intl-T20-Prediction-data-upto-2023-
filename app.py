import numpy as np
import pandas as pd
import pickle
import streamlit as st

pipeline = pickle.load(open('pipe.pkl','rb'))

teams = ['West Indies', 'England', 'South Africa', 'Pakistan',
       'New Zealand', 'Australia', 'Afghanistan', 'India', 'Bangladesh',
       'Sri Lanka', 'Zimbabwe']

venues = ['Central Broward Regional Park Stadium Turf Ground',
       'Beausejour Stadium, Gros Islet', 'Trent Bridge', 'Newlands',
       'The Wanderers Stadium, Johannesburg', 'Westpac Stadium',
       'Shere Bangla National Stadium, Mirpur', 'Harare Sports Club',
       'Dubai International Cricket Stadium', 'Seddon Park',
       'Punjab Cricket Association IS Bindra Stadium, Mohali',
       'Sharjah Cricket Stadium', 'R Premadasa Stadium',
       'Pallekele International Cricket Stadium', 'The Rose Bowl',
       'Melbourne Cricket Ground', 'Kingsmead',
       'Kensington Oval, Bridgetown, Barbados',
       'Shere Bangla National Stadium', 'Eden Park',
       'The Wanderers Stadium', 'Eden Gardens', 'Kennington Oval',
       'Sydney Cricket Ground', 'SuperSport Park, Centurion',
       'R Premadasa Stadium, Colombo', 'Hagley Oval, Christchurch',
       'Perth Stadium', 'Kensington Oval, Bridgetown', 'Wankhede Stadium',
       'Stadium Australia', 'New Wanderers Stadium',
       'Gaddafi Stadium, Lahore', 'Gaddafi Stadium',
       'National Stadium, Karachi', 'National Stadium', 'Bay Oval',
       'Sophia Gardens', 'Hagley Oval', 'Sheikh Zayed Stadium',
       'Old Trafford', 'Adelaide Oval', 'Arun Jaitley Stadium',
       'Punjab Cricket Association Stadium, Mohali',
       'Zayed Cricket Stadium, Abu Dhabi',
       'Western Australia Cricket Association Ground', "Lord's",
       'Narendra Modi Stadium',
       'Darren Sammy National Cricket Stadium, St Lucia',
       'Brisbane Cricket Ground, Woolloongabba', 'SuperSport Park',
       'Feroz Shah Kotla',
       'Daren Sammy National Cricket Stadium, Gros Islet, St Lucia',
       'The Rose Bowl, Southampton', 'R.Premadasa Stadium, Khettarama',
       'Central Broward Regional Park Stadium Turf Ground, Lauderhill',
       'Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium',
       'AMI Stadium', 'Brisbane Cricket Ground, Woolloongabba, Brisbane',
       'Trent Bridge, Nottingham',
       'Punjab Cricket Association IS Bindra Stadium, Mohali, Chandigarh',
       'Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow',
       'Eden Park, Auckland', 'Arun Jaitley Stadium, Delhi',
       'Narendra Modi Stadium, Ahmedabad', 'Old Trafford, Manchester',
       'Sophia Gardens, Cardiff', 'Jade Stadium', 'Moses Mabhida Stadium',
       'Eden Gardens, Kolkata', 'Bay Oval, Mount Maunganui',
       'Sardar Patel Stadium, Motera']

st.title("International T20 Target Score Predictor")
st.markdown("""Predict the __`target score`__ for the T20 match you're watching right now with this tool and stay ahead of the game! """)
col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox("Select the batting team",sorted(teams))
    
with col2:
    bowling_team = st.selectbox("Select the bowling team",sorted(teams))
    
venues = st.selectbox('Select Venue:', sorted(venues))

col3, col4 = st.columns(2)

with col3:
    current_score = st.number_input('Current Score:',min_value=0, max_value=400, value=100, step=1)

with col4:
    wickets = st.number_input('How many wickets down?',min_value=0,max_value=10, value=5, step=1)

col5, col6, col7 = st.columns(3)

with col5:
    overs = st.number_input('How many overs done?',min_value=0,max_value=19, value=5, step=1)

with col6:
    balls = st.number_input('How many balls left in this over?',min_value=0,max_value=10, value=3, step=1)

with col7:
    last_five = st.number_input("Runs scored in last 5 overs:",min_value=0,max_value=120, value=30, step=1)
    

    
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
    input_df = pd.DataFrame({'batting_team':batting_team, 'venue':venues, 'bowling_team':bowling_team, 'score':current_score, 'balls_left':balls_left,
       'wickets_left':(wickets), 'crr':crr, 'powerplay':powerplay, 'death_overs':death_overs, 'top_order_batsmen':top_order,
       'middle_order_batsmen':middle_order, 'lower_order_batsmen':bottom_order, 'tail_order_batsmen':tail,
       'pressure_play':pressure, 'last_5_overs_score':last_five, 'agressive':agresive}, index=[0])
    
    result = pipeline.predict(input_df)
    st.header("Predicted Score : " + str(int(result[0])))
    #st.header("Predicted Score should be between: " + str(int(result[0])+10) + " - " + str(int(result[0])+20))
    
    pass



