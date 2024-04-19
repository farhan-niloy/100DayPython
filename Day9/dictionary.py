programming_dictionary = {
    "Hello World": "The Programmers",
    "Fahmida": "Farhan",
    "Star": "Wars",
}

empty_dictionary = {}

empty_dictionary["1"] = "One"
empty_dictionary["2"] = "Two"

print(empty_dictionary)

print(programming_dictionary["Fahmida"])

for thing in programming_dictionary:
    print(thing)
    print(programming_dictionary[thing])