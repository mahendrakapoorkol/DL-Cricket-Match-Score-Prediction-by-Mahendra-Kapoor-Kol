from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.losses import Huber
from tensorflow.keras.optimizers import Adam

# Build a neural network model
regression_model = Sequential([
    Input(shape=(X_train_norm.shape[1],)),
    Dense(512, activation="relu"),
    Dense(256, activation="relu"),
    Dense(1, activation="linear")
])

# Compile the model with Huber loss
loss_fn = Huber(delta=1.0)
regression_model.compile(optimizer=Adam(), loss=loss_fn)
