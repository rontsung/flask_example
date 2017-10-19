import requests as req
import json
# url = "http://nyt-mongo-scraper.herokuapp.com/api/headlines"
# response = requests.get(url)
# jsponse = response.json()
# n = [x for x in jsponse]
# print(json.dumps(n[0]), n[-1])
# #print(n)
# print(len(n))
# api_key = "25bc90a1196e6f153eece0bc0b0fc9eb"
# url = "http://api.openweathermap.org/data/2.5/weather?"
# city = "New Brunswick"
# query = url + "appid=" + api_key + "&q=" + city
# query2 = url + "q=" + city + "&appid=" + api_key
# print(query2)

# # weather_response = req.get(query)
# # weather_json = weather_response.json()
# # print(weather_json)
# from citipy import citipy

# # Some random coordinates
# coordinates = [(200, 200), (23, 200), (42, 100)]

# cities = []
# for coordinate_pair in coordinates:
#     lat, lon = coordinate_pair
#     cities.append(citipy.nearest_city(lat, lon))
#     print(citipy.nearest_city(lat, lon).city_name)

# import requests as req

# url = "https://api.nytimes.com/svc/search/v2/articlesearch.json?"
# api_key = "164b73c522a8420c8e05343ef1da0a7e"

# # Search for articles that mention granola
# q = "pizza"
# enddate = 20150901
# # Build query URL
# query = url + "api-key=" + api_key + "&q=" + q + "&end_date=" + str(enddate)

# # Populate articles
# articles = req.get(query).json()["response"]["docs"]
# print(query)
# print(json.dumps(articles))
# for article in articles:
#     print(article["headline"]["main"])

# # Loop through the JSON
# for article in articles:
#     # print(query)
#     # print(article)
#     print(article["headline"]["main"]) 

# import requests as req

# # Save config information.
# api_key = "25bc90a1196e6f153eece0bc0b0fc9eb"
# url = "http://api.openweathermap.org/data/2.5/weather?"
# city = "Bujumbura"
# units = "metric"

# # Build query URL and request your results in Celsius
# query_url = url + "appid=" + api_key + "&q=" + city + "&units=" + units
# print(query_url)

# # Get weather data
# weather_response = req.get(query_url)
# weather_json = weather_response.json()

# # Get temperature from JSON response
# temperature = weather_json["main"]["temp"]

# # Report temperature
# print("The temperature in Bujumbura is " + str(temperature) + ".")

# Create code to answer each of the following questions.
# Hint: You will need multiple target urls and multiple API requests.

# Dependencies
import requests as req
import json

# Google API Key
gkey = "AIzaSyCWbAc3T1L13jcP2K3HmvUkVea7CRom-fA"

# 1. What are the geocoordinates (latitude/longitude) of Seattle, Washington?
# Build the endpoint URL
target_city = ("Seattle, Washington")
target_city2 = ("White House, Washington, DC")
target_url = "https://maps.googleapis.com/maps/api/geocode/json" \
    "?address=%s&key=%s" % (target_city2, gkey)

# Print the assembled URL
print(target_url)
geo_data = req.get(target_url).json()
#print(json.dumps(geo_data, indent = 4, sort_keys = True))
#lat = geo_data["results"][0]["geometry"]["bounds"]["northeast"]["lat"]
lng = geo_data["results"][0]["geometry"]["bounds"]["northeast"]["lng"]
#print(lat,lng)

# 2. What are the geocoordinates (latitude/longitude) of The White House?
# ...


# 3. Find the names and addresses of a bike store in Seattle, Washington.
#    Hint: See https://developers.google.com/places/web-service/supported_types
# ...


# 4. Find a balloon store near the White House.
# ...


# 5. Find the nearest dentist to your house.
#    Hint: Use Google Maps to find your latitude and Google Places to find the
#    dentist. You will also need the rankby property.
# ...


# 6. Bonus: Find the names and addresses of the top five places Google suggests
#    for the phrase: "Happy Place ".
#    Hint: Read about "Text Search Results"
# (https://developers.google.com/places/web-service/search#TextSearchRequests)
# ...