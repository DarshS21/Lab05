'''
Library for interacting with the PokeAPI.
https://pokeapi.co/
'''
import requests

POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'

def main():
    # Test out the get_pokemon_info() function
    # Use breakpoints to view returned dictionary
    poke_info = get_pokemon_info("rattata")
    for p in poke_info['results']:
        print(p['name'])

    return

def get_pokemon_info(pokemon_name):
    """Gets information about a specified Pokemon from the PokeAPI.

    Args:
        pokemon_name (str): Pokemon name (or Pokedex number)

    Returns:
        dict: Dictionary of Pokemon information, if successful. Otherwise None.
    """

    # TODO: Clean the Pokemon name parameter
    pokemon_name = str(pokemon_name).strip().lower()

    headers = {
        'Accept': 'application/json'  # To get poke_info in JSON-formatted text
    }

    params = {
        'poke_name': pokemon_name
    }

    # TODO: Build a clean URL and use it to send a GET request
    print(f'Getting information for {pokemon_name}...', end='')
    url = POKE_API_URL + pokemon_name
    resp_msg = requests.get(url, headers=headers, params=params)

    # TODO: If the GET request was successful, convert the JSON-formatted message body text to a dictionary and return it
    if resp_msg.status_code == requests.codes.ok:
        print('success')
        return resp_msg.json()
    else:

    # TODO: If the GET request failed, print the error reason and return None
        print('failure')
        print(f'Response code: {resp_msg.status_code} ({resp_msg.reason})')
        return

if __name__ == '__main__':
    main()