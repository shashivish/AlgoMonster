class Pokemon:
    def __init__(self, name, attack):
        self.name = name
        self.attack = attack

    def __repr__(self):
        return repr((self.name, self.attack))  # repr -> returns string representation of object


if __name__ == '__main__':
    # Python Comparator
    pokemon_object = [Pokemon("Beedril", 70),
                      Pokemon('Charmander', 90),
                      Pokemon('Blastoise', 13)]


    print(f"Before Sorting {pokemon_object}")
    pokemon_object.sort(key=lambda x: x.attack)
    print(f"After Sorting {pokemon_object}")
