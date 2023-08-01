import requests

API_KEY = 'b6907d289e10d714a6e88b30761fae22'
CITY_NAME = 'London'
COUNTRY_CODE = 'uk'
BASE_URL = f'https://samples.openweathermap.org/data/2.5/forecast/hourly?q={CITY_NAME},{COUNTRY_CODE}&appid={API_KEY}'

def get_hourly_forecast():
    url = BASE_URL
    response = requests.get(url)
    data = response.json()

    if 'list' in data:
        return data['list']
    else:
        print("Error: Unable to fetch hourly forecast data.")
        return None

def get_temperature(date):
    hourly_forecast = get_hourly_forecast()
    if hourly_forecast:
        for entry in hourly_forecast:
            if date in entry['dt_txt']:
                return entry['main']['temp']
        print("Date not found in the forecast.")
        return None
    else:
        return None

def get_wind_speed(date):
    hourly_forecast = get_hourly_forecast()
    if hourly_forecast:
        for entry in hourly_forecast:
            if date in entry['dt_txt']:
                return entry['wind']['speed']
        print("Date not found in the forecast.")
        return None
    else:
        return None

def get_pressure(date):
    hourly_forecast = get_hourly_forecast()
    if hourly_forecast:
        for entry in hourly_forecast:
            if date in entry['dt_txt']:
                return entry['main']['pressure']
        print("Date not found in the forecast.")
        return None
    else:
        return None

def main():
    while True:
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            date = input("Enter the date (yyyy-mm-dd hh:mm): ")
            temperature = get_temperature(date)
            if temperature:
                print(f"Temperature on {date}: {temperature}°C")
        elif choice == '2':
            date = input("Enter the date (yyyy-mm-dd hh:mm): ")
            wind_speed = get_wind_speed(date)
            if wind_speed:
                print(f"Wind Speed on {date}: {wind_speed} m/s")
        elif choice == '3':
            date = input("Enter the date (yyyy-mm-dd hh:mm): ")
            pressure = get_pressure(date)
            if pressure:
                print(f"Pressure on {date}: {pressure} hPa")
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
