# Train the neural network
history = regression_model.fit(
    X_train_norm, y_train,
    epochs=12,
    batch_size=32,
    validation_data=(X_test_norm, y_test),
    verbose=1
)
