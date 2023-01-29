def concatenate(*args, **kwargs):
    final_string = ""

    for substring in args:
        final_string += substring

    for key in kwargs:
        if key in final_string:
            final_string = final_string.replace(key, kwargs[key])
    
    return final_string


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))= 