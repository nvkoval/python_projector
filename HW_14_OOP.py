# 1. Modify the Country class to include a third instance attribute called capital as a string.
# Store your new class in a script and test it out by adding the following code
# at the bottom of the script:
'''japan = Country('Japan', 140_000_000, 'Tokyo')
print(f"{japan.name} population is {japan.population} and capital is {japan.capital}.")
The output of your script should be:

Japan population is 140000000 and capital is Tokyo.
'''


class Country:
    def __init__(self, name, population, capital):
        self.name = name
        self.population = population
        self.capital = capital


japan = Country('Japan', 140_000_000, 'Tokyo')
print(f"{japan.name} population is {japan.population} and capital is {japan.capital}.")


# 2. Add increase_population method to country class.
# This method should take an argument and increase population of the country on this number.

class Country:
    def __init__(self, name, population, capital):
        self.name = name
        self.population = population
        self.capital = capital

    def increase_population(self, number):
        return self.population + number


japan = Country('Japan', 140_000_000, 'Tokyo')
number = 400_000
print(f"{japan.name} population after increasing on {number} is {japan.increase_population(number)}")


# 3. Create add method to add two countries together.
# This method should create another country object with the name of the two countries combined
# and population of the two countries added together.
'''bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia.add(herzegovina)
bosnia_herzegovina.population -> 15_000_000
bosnia_herzegovina.name -> 'Bosnia Herzegovina'
'''


class Country:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def add(self, other):
        self.name = f"{self.name} {other.name}"
        self.population = self.population + other.population
        return self


bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia.add(herzegovina)
print(bosnia_herzegovina.population)
print(bosnia_herzegovina.name)


# 4. (Optional) Implement previous method with magic method
'''bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia + herzegovina
bosnia_herzegovina.population -> 15_000_000
bosnia_herzegovina.name -> 'Bosnia Herzegovina'
'''


class Country:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __add__(self, other):
        self.name = f"{self.name} {other.name}"
        self.population = self.population + other.population
        return self


bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia + herzegovina
print(bosnia_herzegovina.population)
print(bosnia_herzegovina.name)
