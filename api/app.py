from flask import Flask, request, jsonify
from flask_cors import CORS
from lib.get_countries import *
from lib.get_cities import *
from lib.Location import *
from flask import jsonify
from datetime import datetime
from dateutil.relativedelta import relativedelta
import random 

# Create the Flask app
app = Flask(__name__)
CORS(app)

@app.route('/continents', methods=['POST'])
def receive_continents():
    try:
        data = request.get_json()
        continents = data
        continent_count = len(continents)
        country_list = {}
        for continent in continents:
            country_list.update(get_countries(continent, continent_count))
        
        # ^ We initialise a country_list and use get countries to store the countries we grab from our continet preference

        cities_by_country_dict = {}
        for id, country_name in country_list.items():
            cities = get_cities(id)
            cities_by_country_dict[country_name] = cities
        
        # ^ We turn country list into items of (id, country_name) and call get_cities on each of them. This will return a city 
        # for each country and then we add this to the cities_by_country dict to be returned to the front end

        return jsonify(cities_by_country_dict), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/preferences', methods=['POST'])
def receive_preferences():
    try:
        data = request.get_json()
        # Process the received data as needed
        cities_by_country_dict = data['citiesData'][0]
        min_temp = data['MinTemp'][0]
        max_temp = data['MaxTemp'][0]
        start_date = datetime.strptime(data['startD'][0], '%Y-%m-%d') - relativedelta(years=1)
        end_date = datetime.strptime(data['endD'][0], '%Y-%m-%d') - relativedelta(years=1)
        # ^ Creating datetime objects from dates passed in and minusing a year from them ^
        
        start_date = datetime.strftime(start_date, '%Y-%m-%d')
        end_date = datetime.strftime(end_date, '%Y-%m-%d')
        # ^ Turning processed datetime objects back into strings ^ 
        
        locations_lst = []

        for country_name, cities in cities_by_country_dict.items():
            location = Location(country_name, cities)
            location.get_weather(min_temp, max_temp, start_date, end_date)
            if location.city_details == {}:
                pass
            else:
                locations_lst.append(location.city_details)
            
        print("THIS IS THE FINAL LOCATION LST")
        print(locations_lst)
        
        random.shuffle(locations_lst)
        # ^ We shuffle locations_lst to make sure if user does same input a few times, it returns a different order of countries. 
        
        return jsonify(locations_lst), 201
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)