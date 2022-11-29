from pokedex import pokedex as p


def poke_api(pokedex):
    user_poke = input('Enter a pokemon: ')

    pokedex = pokedex.Pokedex(version='v1', user_agent='ExampleApp (https://example.com, v2.0.1)')
    pokemon = pokedex.get_pokemon_by_name(user_poke)

    try:
        a = pokemon[0]
        my_dict = dict(a)

        type = my_dict["types"]
        abilities = my_dict["abilities"]["normal"]

        print(f'Pokemon: {my_dict["name"]}\nSpecies: {my_dict["species"]}\nType: {type[0]}\nAbilities: {abilities[0]}')

    except KeyError:
        print('Invalid pokemon!')
        poke_api()

poke_api(p)