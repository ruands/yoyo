def get_temps_from_forecast(forecast):
    # Get hours from days and clean up
    forecast_days = forecast.get("forecastday")
    forecast_hours = []
    for day in forecast_days:
        forecast_hours.append(day["hour"])
    flat_hours = [item for sublist in forecast_hours for item in sublist]
    del forecast_days
    del forecast_hours

    # Get temps from hours
    temps = []
    for hour in flat_hours:
        temps.append(hour.get("temp_c"))
    return temps

def get_avg_temp(temps):
    # Return sum / len, and round to 2 decimals
    return round(sum(temps) / len(temps), 2) if temps else 0
