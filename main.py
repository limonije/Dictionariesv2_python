# Do not modify these lines
from helpers import get_countries

__winc_id__ = "00a4ab32f1024f5da525307a1959958e"
__human_name__ = "dictionariesv2"


def create_passport(name, date_of_birth, place_of_birth, height, nationality):
    countries = get_countries()
    person = {}
    person['name'] = name
    person['date_of_birth'] = date_of_birth
    person['place_of_birth'] = place_of_birth
    person['height'] = height
    if nationality in countries:
        person['nationality'] = nationality
    return person


def add_stamp(person, countries):
    country_list = countries
    country_list_clean = (set(country_list))
    home_country = person['nationality']
    country_list_new = [country for country in country_list_clean if country != home_country]
    person.update([('stamps', country_list_new)])
    return person


# Add your code after this line
if __name__ == "__main__":
    omari = (create_passport("Omari Muchumba", "1995-07-16", "Kampala", 184.31, "Uganda"))
    omari = (add_stamp(omari, ['Afghanistan', 'Austria', 'Austria', 'Belgium', 'Uganda']))
    print(omari)