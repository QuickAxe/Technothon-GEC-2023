# connects to the fitbit api,
# but that needs our app to get authorised,
# and due to our lack of time, 
# this is a dummy api call and returns dummy data
#  
# The actual api contains details as follows, sent as a json file: 
# 
# Active Zone Minutes Time Series provides a user's heart-pumping activity throughout the day.
# Activity and Activity Time Series provides information about a user's activity and their activity goals. The time series endpoints can be used to observe trends.
# Authorization contains the endpoints needed to manage consent to Fitbit user data.
# Body and Body Time Series provides data on a user's weight and body fat percentage. The time series endpoints can be used to observe trends.
# Breathing Rate provides a user's average breaths per minute at night.
# Cardio Fitness Score (VO2 Max) returns the maximum or optimum rate at which the user’s heart, lungs, and muscles can effectively use oxygen during exercise.
# Devices contains information about the devices paired to a user's account and when their last sync time.
# Electrocardiogram contains information about the user's on-device electrocardiogram readings.
# Friends contains information about a user's friends and their leaderboard.
# Heart Rate Time Series returns a user's heart rate and resting heart rate values. The time series endpoints can be used to observe trends.
# Heart Rate Variability provides the room mean square of successive differences values recorded during a user's period of sleep.
# Intraday provides a daily, granular-level of detail to a user's active zone minutes, activity, breathing rate, heart rate, heart rate variability and SpO2 metrics.
# Nutrition and Nutrition Time Series allows a user to record the foods they consumed and include the food's nutritional metadata. The time series endpoints can be used to observe trends.
# Sleep returns information about a user's sleep patterns.
# SpO2 provides a user's blood oxygen levels.
# Subscription notifies your application via webhooks when new data is available.
# Temperature returns a user's core and skin temperature.
# User returns basic information about the user who shared their data with your application

def fitData():
    data = {"heartRate" : 72,
            "sleep" : 7,
            "SpO2" : 95,
            "stepGoal": 12000}

    return data