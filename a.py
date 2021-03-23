import pandas

path = str(input("Write your excel file's path: "))
path = path.replace("\\", "/")
filename = input("Write excel file name without .xlsx: ")

if path[-1] == "/":
    pass
else:
    path = path+"/"

data = pandas.read_excel(path+filename+".xlsx")
columnname = input("Write columnn name: ")
columndata = data[columnname].unique()

# Creates an excel file with the name of that value for each different value in a column.
for i in columndata:

    a = data[data[columnname].str.contains(i)]
    a.to_excel(path+i+".xlsx")
