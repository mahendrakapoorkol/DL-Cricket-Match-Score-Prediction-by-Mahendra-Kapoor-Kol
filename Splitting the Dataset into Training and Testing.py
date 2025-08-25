from sklearn.model_selection import train_test_split

# Select predictor features and target variable
input_features = ["bat_team", "bowl_team", "venue", "runs", "wickets", 
                  "overs", "striker", "batsman", "bowler"]
target = "total"

X = encoded_df[input_features]
y = encoded_df[target]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=7
)
