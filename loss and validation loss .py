# Convert training history to DataFrame
loss_history = pd.DataFrame(history.history)

# Plot training and validation loss curves
loss_history.plot(figsize=(8,5), title="Model Training History")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.show()
