def get_city(city,country,population = ""):
    if population:
        cityinfo = city+","+country + " - "+ "population " + str(population)
    else:
        cityinfo = city+","+country
    return cityinfo.title()

    