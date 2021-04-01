import tabula
import json
from tabula import convert_into
import os 

os.system("clear")
# file = "myfitness.pdf"
# table = tabula.read_pdf(file, pages=1)
# print(table[0])

# file = "data2.pdf"
# table1 = tabula.read_pdf(file, pages=1)
# table2 = tabula.read_pdf(file, pages=2)
# print(table1[0])
# print(table2[0])

# file = "data3.pdf"
# table = tabula.read_pdf(file, pages=1, multiple_tables=True)
# print(table[0])
# print(table[1])

# file = "data3.pdf"
# table = tabula.read_pdf(file, pages=1, multiple_tables=False)
# print(table[0])

# file = "https://raw.githubusercontent.com/chezou/tabula-py/master/tests/resources/data.pdf"
# dfs = tabula.read_pdf(file, stream=True, output_format="json")
# print(json.dumps(dfs[0], indent=2))
# print(str(len(dfs)) + " table/s found!")


# file = "https://raw.githubusercontent.com/chezou/tabula-py/master/tests/resources/data.pdf"
# dfs = tabula.read_pdf(file, stream=True, pages="all")
# print(str(len(dfs)) + " table/s found!")
# print(dfs)


file = "https://raw.githubusercontent.com/chezou/tabula-py/master/tests/resources/data.pdf"
convert_into(file, "test.csv", stream=True, output_format="csv")

