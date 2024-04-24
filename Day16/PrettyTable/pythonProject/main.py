from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])

table.add_column("Type", ["Electic", "Water", "Fire"])

table.align = "l"

print(table)