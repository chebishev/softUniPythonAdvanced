def team_lineup(*players_info):
    team = {}
    for player in players_info:
        name, country = player
        if country not in team:
            team[country] = []
        team[country].append(name)

    output = ""
    for country, players in sorted(team.items(), key=lambda x: (-len(x[1]), x[0])):
        output += f"{country}:\n"
        for player in players:
            output += f"  -{player}\n"

    return output


print(team_lineup(
    ("Harry Kane", "England"),
    ("Manuel Neuer", "Germany"),
    ("Raheem Sterling", "England"),
    ("Toni Kroos", "Germany"),
    ("Cristiano Ronaldo", "Portugal"),
    ("Thomas Muller", "Germany")))

print(team_lineup(
    ("Lionel Messi", "Argentina"),
    ("Neymar", "Brazil"),
    ("Cristiano Ronaldo", "Portugal"),
    ("Harry Kane", "England"),
    ("Kylian Mbappe", "France"),
    ("Raheem Sterling", "England")))

print(team_lineup(
    ("Harry Kane", "England"),
    ("Manuel Neuer", "Germany"),
    ("Raheem Sterling", "England"),
    ("Toni Kroos", "Germany"),
    ("Cristiano Ronaldo", "Portugal"),
    ("Thomas Muller", "Germany"),
    ("Bruno Fernandes", "Portugal"),
    ("Bernardo Silva", "Portugal"),
    ("Harry Maguire", "England")))
