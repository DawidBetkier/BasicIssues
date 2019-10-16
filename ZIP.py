"""Get city from zip code"""

digit_to_area = {
    0: "Warszawa",
    1: "Olsztyn",
    2: "Lublin",
    3: "Kraków",
    4: "Katowice",
    5: "Wrocław",
    6: "Poznań",
    7: "Szczecin",
    8: "Gdańsk",
    9: "Łódź",

}

def get_city(zip_code):
    """
    Validate input and return city
    :param zip_code:
    :return:
    """
    if len(zip_code) != 6 :
        return None
    if zip_code[2] != "-" :
        return None
    if not (zip_code[:2] + zip_code[3:]).isdigit() :
        return None

    city_code = int(zip_code[0])
    return digit_to_area[city_code]

if __name__ == "__main__" :
    code = input("Please provide zip code: ")
    city = get_city(code)

    if city:
        print(f"Witaj gościu z miasta {city}")
    else:
        print("Nieprawidłowy kod pocztowy")