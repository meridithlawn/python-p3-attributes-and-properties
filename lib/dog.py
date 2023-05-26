#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name = "Fido", breed = "Mastiff"):
        self.name = name
        self.breed = breed

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if(type(name) in (str,)) and (1 <= len(name) <= 25):
            # print(f"Setting dog name to, {name}.")
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")

    @property
    def breed(self):
        # print("Retrieving breed")
        return self._breed
    
    @breed.setter
    def breed(self, breed):
        if(breed in APPROVED_BREEDS):
            # print(f"The breed is {breed}.")
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")
    # def get_name(self):
    #     print("Retrieving name.")
    #     return self._name

    # def set_name(self, name):
    #     if(type(name) in (str,)) and (1 <= len(name) <= 25):
    #         print(f"Setting dog name to, {name}.")
    #         self._name = name
    #     else:
    #         print("Name must be string between 1 and 25 characters.")
   

   

    # name = property(get_name, set_name)
