import requests

class CityValidator:
    @staticmethod
    def validate(city):
        # Checks if the city name is valid by ensuring it's not empty and contains letters
        return city.isalpha()

class WeatherFetcher:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.tomorrow.io/v4/weather/realtime"

    def get_weather(self, city):
        params = {
            'location': city,
            'apikey': self.api_key,
            'units': 'metric'  # Celsius temperature
        }
        
        response = requests.get(self.base_url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            temperature = data['data']['values']['temperature']
            return temperature
        else:
            return None

class WeatherApp:
    def __init__(self, api_key):
        self.fetcher = WeatherFetcher(api_key)

    def get_city_from_user(self):
        while True:
            city = input("Enter a city name: ")
            if CityValidator.validate(city):
                return city
            else:
                print("Invalid city name. Please enter letters only.")

    def display_weather(self):
        city = self.get_city_from_user()
        temperature = self.fetcher.get_weather(city)
        
        if temperature is not None:
            print(f"The temperature in {city} is {temperature}°C.")
        else:
            print("City not found or there was an error with the API request.")
            self.retry_display_weather()

    def retry_display_weather(self):
        retry = input("Would you like to try again? (yes/no): ").strip().lower()
        if retry == 'yes':
            self.display_weather()
        else:
            print("Thank you for using the weather app!")

# Initialize and run the app
api_key = "D17tZoSAFaMUaoSQbpoliaQlViCy8MhR"  # Replace with your Tomorrow.io API key
app = WeatherApp(api_key)
app.display_weather()