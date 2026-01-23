
""" Removing Duplicates from file based on all columns """

# Reading a text file and splitting each line by comma
file=open(r"D:/Python/Emp1.txt")
cols=file.readline().strip().split(',') # Returns list of columns   
print("Columns:", cols)
print(len(cols))


file1=open(r"D:/Python/Emp20.txt","w")
file.seek(0)
key_columns=set() 

for line in file:
    values=line.strip().split(',')
    # print(values)
    key=values[0]
    # key="|".join([values[0],values[2]])  # Creating a unique key based on first and third column
    if key not in key_columns:
        file1.write(line)
    key_columns.add(key)  # Storing set of keys to remove duplicates
file1.close()

file.close()