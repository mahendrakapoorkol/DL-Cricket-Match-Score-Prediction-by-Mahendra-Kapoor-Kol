import numpy as np
import ipywidgets as widgets
from IPython.display import display, clear_output
import warnings
warnings.filterwarnings("ignore")

# Dropdown menus for categorical inputs
venue_dd = widgets.Dropdown(
    options=list(encoders["venue"].classes_),
    description="Match Venue:",
    style={"description_width": "initial"}
)

bat_team_dd = widgets.Dropdown(
    options=list(encoders["bat_team"].classes_),
    description="Batting Team:",
    style={"description_width": "initial"}
)

bowl_team_dd = widgets.Dropdown(
    options=list(encoders["bowl_team"].classes_),
    description="Bowling Team:",
    style={"description_width": "initial"}
)

striker_dd = widgets.Dropdown(
    options=list(encoders["batsman"].classes_),
    description="Striker:",
    style={"description_width": "initial"}
)

bowler_dd = widgets.Dropdown(
    options=list(encoders["bowler"].classes_),
    description="Bowler:",
    style={"description_width": "initial"}
)

# Numeric inputs
runs_inp = widgets.IntText(value=0, description="Current Runs:", style={"description_width": "initial"})
wickets_inp = widgets.IntText(value=0, description="Wickets Down:", style={"description_width": "initial"})
overs_inp = widgets.FloatText(value=0.0, description="Overs Played:", style={"description_width": "initial"})
striker_flag = widgets.IntText(value=0, description="Striker Index:", style={"description_width": "initial"})  # custom indicator

# Button for prediction
predict_btn = widgets.Button(description="Predict Match Score", button_style="success")

# Output display
out = widgets.Output()

def show_prediction(btn):
    with out:
        clear_output()
        
        # Encode categorical inputs
        v = encoders["venue"].transform([venue_dd.value])[0]
        bat = encoders["bat_team"].transform([bat_team_dd.value])[0]
        bowl = encoders["bowl_team"].transform([bowl_team_dd.value])[0]
        s = encoders["batsman"].transform([striker_dd.value])[0]
        bwl = encoders["bowler"].transform([bowler_dd.value])[0]
        
        # Prepare input feature vector
        features = [
            bat, bowl, v, 
            runs_inp.value, 
            wickets_inp.value, 
            overs_inp.value, 
            striker_flag.value, 
            s, bwl
        ]
        
        input_vector = np.array(features).reshape(1, -1)
        input_vector = minmax_scaler.transform(input_vector)
        
        # Predict using trained model
        predicted_runs = regression_model.predict(input_vector)
        print(f"🔮 Predicted Innings Total: {int(predicted_runs[0])} runs")

# Bind function to button
predict_btn.on_click(show_prediction)

# Display widgets
display(venue_dd, bat_team_dd, bowl_team_dd, striker_dd, bowler_dd,
        runs_inp, wickets_inp, overs_inp,
        striker_flag, predict_btn, out)
