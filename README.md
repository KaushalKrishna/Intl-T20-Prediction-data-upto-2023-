# T20 Cricket: Men's International

The primary objective here is to predict the final score in the first innings at any stage of the match.

### Step taken in this project:

1. Data collection from source: https://cricsheet.org/downloads/
  - Data was present as a seperate YAML file for each match.
  - These datasets were manipulated heavily to convert from a JSON formatting to a tabular structure.
  - Link to the exact source: https://cricsheet.org/downloads/all.zip

2. Data Cleaning
  - This includes cleaning JSON-artefacted values to columnar values.
  - Redacting over 120 columns and wrangling other columns to produce 17 usable columns

3. Feature Engineering
  - Several columns were created using the data presented, such as:
      - Current run rate
      - Batsman order (Top/Middle/Bottom/Tail)
      - Powerplay
      - Death overs
      - Under pressure
      - Agressive stance
  - Cleaned and feature engineered output is the `t2_cleaned.csv` file

4. Finally, preparing the data for modelling and retaining columns which were useful and made sure to control the dimensionality.
  - Built a `XGB Regressor` model with
    - __95.3% R2 Score__
    - __RMSE__ of __5.2__
    (with a standard deviation of 0.001 with 3Fold CV)

5. The model is now deployed on streamlit.

   ## Link: <a href="https://kaushalt20.streamlit.app/">https://kaushalt20.streamlit.app/</a>

![Screenshot of the tool](https://github.com/KaushalKrishna/Intl-T20-Prediction-data-upto-2023-/blob/main/Screenshot%202023-07-17%20at%209.12.54%20PM.png)
