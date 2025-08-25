from sklearn.metrics import mean_absolute_error, mean_squared_error

# Generate predictions on test set
y_pred = regression_model.predict(X_test_norm)

# Evaluate using MAE
mae_score = mean_absolute_error(y_test, y_pred)
print("Mean Absolute Error:", mae_score)
