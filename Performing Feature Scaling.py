from sklearn.preprocessing import MinMaxScaler

# Initialize the scaler
minmax_scaler = MinMaxScaler()

# Scale training and testing features
X_train_norm = minmax_scaler.fit_transform(X_train)
X_test_norm = minmax_scaler.transform(X_test)
