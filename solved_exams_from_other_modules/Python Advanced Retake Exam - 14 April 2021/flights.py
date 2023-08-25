def flights(*args):
    flights_dictionary = {}
    last_element = ""
    for index, element in enumerate(args):
        if element == "Finish":
            break
        if index % 2 == 0:
            if element not in flights_dictionary:
                flights_dictionary[element] = 0
            last_element = element
        else:
            flights_dictionary[last_element] += element

    return flights_dictionary


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
