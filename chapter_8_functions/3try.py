# def city_country(city_name, country_name):
#     full_name = f"{country_name}, {city_name}"
#     return full_name.title()

# city = city_country('knezevo', 'bih')
# print(city)


def make_album(artist_name, album_title, album_year=None):
    if album_year:
        album = {'artist': artist_name, 'title': album_title, 'year': album_year}
    else:
         album = {'artist': artist_name, 'title': album_title}   
    return album

album_data = make_album('Zdravko', 'Krasiva', 1999)
print(album_data)

while True:
    print("\nPlease enter album and artist name: ")
    print("Enter 'q' anytime to quit.")
    ar_name = input("Artist name is: ")
    if ar_name == 'q':
        break
    al_name = input("Album name is: ")
    if al_name == 'q':
        break
    album_data = make_album(ar_name, al_name)
    print(album_data)
