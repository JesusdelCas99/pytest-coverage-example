import requests

def check_age(age, citizenship):
    if age >= 65 and citizenship == "Local":
        return "Senior Local"
    elif age >= 65 and citizenship == "Foreigner":
        return "Senior Foreigner"
    elif age >= 18 and citizenship == "Local":
        return "Adult Local"
    elif age >= 18 and citizenship == "Foreigner":
        return "Adult Foreigner"
    else:
        return "Minor"
    

def check_height(height):
    if height >= 180:
        return "Tall"
    elif height >= 150:
        return "Average"
    else:
        return "Short"
    

def check_population(country):
    url = f"https://api.population.io/1.0/population/{country}/today-and-tomorrow/"
    response = requests.get(url=url)
    return response
