def draw_cards(*first_deck, **second_deck):
    monster_cards = []
    spell_cards = []

    for card in first_deck:
        card_name, card_type = card
        if card_type == "monster":
            monster_cards.append(card_name)
        else:
            spell_cards.append(card_name)

    for name, value in second_deck.items():
        if value == "monster":
            monster_cards.append(name)
        else:
            spell_cards.append(name)

    sorted_monsters = sorted(monster_cards)[::-1]
    sorted_spells = sorted(spell_cards)
    output = ""
    if sorted_monsters:
        output += "Monster cards:\n"
        for monster in sorted_monsters:
            output += f"  ***{monster}\n"
    if sorted_spells:
        output += "Spell cards:\n"
        for spell in sorted_spells:
            output += f"  $$${spell}\n"
    return output[:-1]


# print(draw_cards(("cyber dragon", "monster"), freeze="spell",))
# print(draw_cards(("celtic guardian", "monster"),
#                  ("earthquake", "spell"), ("fireball", "spell"), raigeki="spell", destroy="spell",))
# print(draw_cards(("brave attack", "spell"), ("freeze", "spell"), lightning_bolt="spell", fireball="spell",))
