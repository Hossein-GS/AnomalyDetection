# Please refer to the README.md for detailed explanation of the code
# The explanation of the chosen algorithm and it's effectiveness is provided in the README.md file

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# Function to simulate the data stream
def simulate_data_stream(n):
    time = np.arange(n) # Generates an array of time steps
    seasonal_pattern = np.sin(time / 20) * 10 # Creates a seasonal pattern using sine function
    noise = np.random.normal(0, 1, n) #  Creates random noise
    anomalies = np.random.choice([0, 50], size=n, p=[0.98, 0.02]) # Creates random anomalies in the data
    return seasonal_pattern + noise + anomalies


# Detect anomalies using Holt-Winters method
def detect_anomalies_holt_winters(data, threshold=3):
    if not isinstance(data, np.ndarray) or data.size == 0:
        raise ValueError("Input data must be a non-empty numpy array.")

    try:
        # Fits the data to the Holt-Winters model
        model = ExponentialSmoothing(data, trend='add', seasonal='add', seasonal_periods=50) 
        fitted_model = model.fit()
        
        forecasted = fitted_model.fittedvalues  # Gets the forecasted values
        residuals = np.abs(data - forecasted)  # Calculate the difference
        
        # Calculate the mean and standard deviation of the residuals
        mean_residual = np.mean(residuals)
        std_residual = np.std(residuals)
        
        # Mark points as anomalies
        anomalies = np.abs(residuals - mean_residual) > threshold * std_residual
        return anomalies, forecasted
    except Exception as e:
        print(f"An error occurred during anomaly detection: {e}")
        return np.array([]), np.array([])  # Return empty arrays on error


# Set up the figure and axis for animation
fig, ax = plt.subplots()

# Simulate the data stream and detect anomalies
data_stream = simulate_data_stream(200)
anomalies, forecasted_values = detect_anomalies_holt_winters(data_stream)

# Function to update the animation frame by frame
def update(i):
    # Clear the axis and plot the data stream and forecasted values
    ax.clear()
    ax.plot(data_stream[:i], label="Data Stream")
    ax.plot(forecasted_values[:i], color='green', linestyle='--', label="Forecasted")
    ax.set_title(f"Data Stream with Holt-Winters Anomalies (Frame {i})")
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    
    # Detect anomalies in the current data window
    anomaly_indices = np.where(anomalies[:i])[0]
    if len(anomaly_indices) > 0:
        ax.scatter(anomaly_indices, data_stream[anomaly_indices], color='r', label="Anomalies")

    ax.legend()

# Set up the animation for the figure
ani = animation.FuncAnimation(fig, update, frames=range(50, len(data_stream)), repeat=False)

# Display the animation
plt.show()
