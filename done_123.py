from pathlib import Path
import pandas as pd

from geopy.geocoders import Nominatim
import folium


def read_the_points(file_name: str) -> pd.DataFrame:
    df_address = pd.read_excel(file_name)
    return df_address


def convert_addrs_to_coords(addrs: pd.DataFrame) -> list:
    geolocator = Nominatim(user_agent="example app")

    points_coords = list()
    for row in addrs.itertuples():
        serch_row = F"{row.building}, {row.street}, {row.city}, {row.region}, {row.country}"  #
        # location = geolocator.geocode("9, Науки, Северодонецк, Луганская область")
        location = geolocator.geocode(serch_row)
        if location:
            points_coords.append((location.latitude, location.longitude))
            print(row, '------->',  (location.latitude, location.longitude))
        print(".")

    return points_coords


def show_points_by_coords(geo_coords: list):
    map = folium.Map(location=[48.94512, 38.47734], zoom_start=15)
    #  [[48.94512,38.47734], [48.94876306772694, 38.49722793082553],[48.94065233937393, 38.50110957662567],[48.93861804327843, 38.50574308487394],[48.94950994156189, 38.499434103869774]]:
    for coordinates in geo_coords:
        folium.Marker(location=coordinates, icon=folium.Icon(color='green')).add_to(map)

    map.save("D:/Python/Flask/templates/map.html")


if __name__ == '__main__':
    file_name = r"D:/Python/Flask/templates/точки.xlsx"
    df_addrs = read_the_points(file_name)
    geo_coords = convert_addrs_to_coords(df_addrs)
    show_points_by_coords(geo_coords)
