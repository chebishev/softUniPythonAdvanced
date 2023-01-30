def add_songs(*args):

    songs_dictionary = {}

    for item in args:
        title = item[0]
        if title not in songs_dictionary:
            songs_dictionary[title] = []
        for line in item[1]:
            songs_dictionary[title].append(line)
    output_list = []

    for k, v in songs_dictionary.items():
        output_list.append(f"- {k}")
        if v:
            for value in v:
                output_list.append(value)
    return "\n".join(output_list)


print(add_songs(
    ("Bohemian Rhapsody", []),
    ("Just in Time",
     ["Just in time, I found you just in time",
      "Before you came, my time was running low",
      "I was lost, the losing dice were tossed",
      "My bridges all were crossed, nowhere to go"])
))

print(add_songs(
    ("Beat It", []),
    ("Beat It",
     ["Just beat it (beat it), beat it (beat it)",
      "No one wants to be defeated"]),
    ("Beat It", []),
    ("Beat It",
     ["Showin' how funky and strong is your fight",
      "It doesn't matter who's wrong or right"]),
))

print(add_songs(
    ("Love of my life",
     ["Love of my life, you've hurt me",
      "You've broken my heart, and now you leave me",
      "Love of my life, can't you see?",
      "Bring it back, bring it back"]),
    ("Beat It", []),
    ("Love of my life",
     ["Don't take it away from me",
      "Because you don't know",
      "What it means to me"]),
    ("Dream On",
     ["Every time that I look in the mirror"]),
))
