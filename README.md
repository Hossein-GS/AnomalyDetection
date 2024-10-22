# Anomaly Detection

## Description
This Project simulates a data stream with random anomalies across the data. The anomalies will be detected using the Holt-Winters Algorithm and will be displayed in a plot. 

## Showcase
![Alt text](/images/Plot.PNG)

## Libraries Used
In this project the following libraries are used:
1. numpy==2.1.2
2. matplotlib==3.9.2
3. statsmodels==0.14.4

*__Note:__ the libraries and their versions can be viewed in requirements.txt file at the root directory*

## Algorithm Used (Holt-Winters)
For this project I used __Holt-Winters Algorithm__, which is a time series forcasting technique that models data with __trend__ and __seasonality__.

Holt-Winters method forcasts future values by adjusting for both trend and seasonal fluctations. 

In Holt-Winters anomaly detection, the difference between the actual values and the forcasted values can be analyzed, this difference can also be called residuals. If the residuals exceeds the threshold (_Predefined in the code as 3_), the data point will be flagged as anomaly. 

This makes anomaly detection effective, as long as the data has regular patterns.

The only downsides to using this algorithm are:

- Is not as effective if __Concept Drift__ occurs, since it assumes that the seasonal and trend patterns are stable.
- Requires __manual tuning__ of the Threshold for anomalies. 


## simulate_data_stream Function
This function generates a data stream of __200 frames__ along with __Noise__ and __Random Anomalies/Spikes__ 

## detect_anomalies_holt_winters function
This function creates a forcast (_future values_) of the data stream, and caluclates the difference (_residulas_) of the data stream and forcasted values.

The mean and standard devation values will be calculated using numpy's __mean()__ and __std()__.

The anomalies will be marked if the difference between residuals and __mean_residual__ is greater than the __threshold multiplied by std_residual__.

*__Note:__ I added error handling to the function, but it is not needed as all the values in the code is predefined*

## update function
This function updates the plot every frame. The __forcasted values__, and the __data stream__ will be plotted, and other plot attributes such as __title__, __xlabel__, and __ylabel__ will be set.



