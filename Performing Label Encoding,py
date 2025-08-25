from sklearn.preprocessing import LabelEncoder

# Columns with categorical data
categorical_features = ["bat_team", "bowl_team", "venue", "batsman", "bowler"]

# Copy dataset for transformation
encoded_df = df.copy()

# Dictionary to store encoders for later use
encoders = {}

# Apply label encoding to each categorical column
for feature in categorical_features:
    encoder = LabelEncoder()
    encoded_df[feature] = encoder.fit_transform(encoded_df[feature])
    encoders[feature] = encoder
