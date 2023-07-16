# T20 Cricket: Men's International

The primary objective here is to predict the final score in the first innings at any stage of the match.

### Step taken in this project:

1. Data collection from source: https://cricsheet.org/downloads/
  - Data was present as a seperate YAML file for each match.
  - These datasets were manipulated heavily to convert from a JSON formatting to a tabular structure.

2. Data Cleaning
  - This includes cleaning up dictionary formatted JSON values to columnar values.
  - Redacting over 120 columns and wrangling other columns to product 17 usable columns

3. Feature Engineering
  - Several columns were created using the data presented, such as:
      - Current run rate
      - Batsman order (Top/Middle/Bottom/Tail)
      - Powerplay
      - Death overs
      - Under pressure
      - Agressive stance

4. Finally, preparing the data for modelling and retaining columns which had value.
  - Built a `RandomForest Regression` model with __93% R2 Score__ (with a standard deviation of 0.001 with 3Fold CV)

5. The model is built to be deployed on streamlit.

   ## Link: <a href="https://kaushalt20.streamlit.app/">https://kaushalt20.streamlit.app/</a>

![](https://s11.gifyu.com/images/SW8A1.gif)


