import os
import requests
import smtplib

OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/forecast'
API_KEY = os.environ.get('OWM_API_KEY')
MY_LAT = -23.463751
MY_LON = -46.533550
EMAIL = os.environ.get('MY_EMAIL')
PASS = os.environ.get('EMAIL_PASSWORD')

parameters ={
    'lat': MY_LAT,
    'lon': MY_LON,
    'units': 'metric',
    'cnt': 4,
    'appid': API_KEY
}

request = requests.get(url=OWM_Endpoint, params=parameters)
request.raise_for_status()
weather_data = request.json()
will_rain = False

for i in weather_data['list']:
    condition_code = (i['weather'][0]['id'])
    if condition_code < 700:
        will_rain = True

if will_rain:
    with smtplib.SMTP('smtp.gmail.com') as conn:
        conn.starttls()
        conn.login(EMAIL, PASS)
        conn.sendmail(
            from_addr=EMAIL,
            to_addrs='pymailtest2000@yahoo.com',
            msg=f"Subject:Rain Alert\n\nBe alert! In the next 12 hours there's a chance that it'll rain!"
            )
