import numpy as np
import pandas as pd
import pickle as pickle
from sklearn.preprocessing import LabelEncoder

def load_data_and_model(city):
    if city == 'Mumbai':
        data = pd.read_csv('train.csv')  # Load Mumbai dataset
        model = pickle.load(open('model.pkl', 'rb'))  # Load Mumbai model
        x = LabelEncoder().fit_transform(data['Location'])
    elif city == 'Bangalore':
        data = pd.read_csv('Bangalore.csv')  # Load Bangalore dataset
        model = pickle.load(open('model2.pkl', 'rb'))  # Load Bangalore model
        x = LabelEncoder().fit_transform(data['Location'])
    else:
        raise ValueError("Invalid city selected.")

    return data, model, x
def extract_locations_from_csv(filename):
    locations = pd.read_csv(filename)['Location'].tolist()
    return locations
def predict(selected_city, location, area, bhk, ne, gy, ind, ca, jog):
    data, model, x = load_data_and_model(selected_city)

    n = data[data['Location'] == location].index[0]

    gym = 1 if gy == 'on' else 0
    jogg = 1 if jog == 'on' else 0
    car = 1 if ca == 'on' else 0
    indd = 1 if ind == 'on' else 0
    new = 1 if ne == 'on' else 0

    input_data = pd.DataFrame([[area, x[n], bhk, new, gym, car, indd, jogg]],
                              columns=['Area', 'Location', 'No. of Bedrooms',
                                       'New/Resale', 'Gymnasium', 'Car Parking',
                                       'Indoor Games', 'Jogging Track'])

    pred = model.predict(input_data)[0] * 1e6
    return pred
if __name__ == "__main__":
    mumbai_locations = extract_locations_from_csv('trainnames.csv')
    bangalore_locations = extract_locations_from_csv('Bangalorenames.csv')

    mumbai_data, mumbai_model, mumbai_encoder = load_data_and_model('Mumbai')
    bangalore_data, bangalore_model, bangalore_encoder = load_data_and_model('Bangalore')

    mumbai_prices = {}
    for location in mumbai_locations:
        prices = {
            'Location': location,
            '1BHK': predict('Mumbai', location, 1000, 1, 0, 0, 0, 0, 0),
            '2BHK': predict('Mumbai', location, 2000, 2, 0, 0, 0, 0, 0),
            '3BHK': predict('Mumbai', location, 2500, 3, 0, 0, 0, 0, 0)
        }
        mumbai_prices[location] = prices

    bangalore_prices = {}
    for location in bangalore_locations:
        prices = {
            'Location': location,
            '1BHK': predict('Bangalore', location, 1000, 1, 0, 0, 0, 0, 0),
            '2BHK': predict('Bangalore', location, 2000, 2, 0, 0, 0, 0, 0),
            '3BHK': predict('Bangalore', location, 2500, 3, 0, 0, 0, 0, 0)
        }
        bangalore_prices[location] = prices

    # Convert prices to DataFrames
    mumbai_df = pd.DataFrame(list(mumbai_prices.values()))
    bangalore_df = pd.DataFrame(list(bangalore_prices.values()))

    # Save DataFrames to CSV files
    mumbai_df.to_csv("mumbai_prices.csv", index=False)
    bangalore_df.to_csv("bangalore_prices.csv", index=False)