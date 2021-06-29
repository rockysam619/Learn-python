from prettytable import PrettyTable
my_table = PrettyTable()

my_table.add_column("City name",["Adelaide","Brisbane","Darwin","Hobart","Sydney","Melbourne","Perth"])
my_table.add_column("Area", [1295, 5905, 112, 1357, 2058, 1566, 5386]) 
my_table.add_column("Population", [1158259, 1857594, 120900, 205556, 4336374, 3806092, 1554769]) 
my_table.add_column("Annual Rainfall",[600.5, 1146.4, 1714.7, 619.5, 1214.8, 646.9, 869.4])
my_table.align = "r"
print(my_table)
