
# Reading a text file and splitting each line by comma
file=open(r"D:/Python/Emp1.txt")
# print(file.read()) # Read entire file content
# file.seek(0)  # Move the cursor to the beginning of the file
# print(file.readline()) # Read single line (First Line)

print("Splitting First Line by Comma and split always returns a list")
file.seek(0)
print(file.readline().split(',')) # Splitting First Line by Comma and split always returns a list
print("Read all lines data from file")
# Read all lines data from file
file.seek(0)
all_lines = file.readlines() # Read all lines at once and returns a list
# print(all_lines)
# print(type(all_lines))

f=open(r"D:/Python/Emp00.txt","w")
# Writing all lines to new file
f.writelines(all_lines)
f.close()
print("Read All Lines using loop and split by Comma and print only those lines which contain gender as 'Male'")
# Read All Lines using loop and split by Comma and print only those lines which contain gender as 'Male'
file.seek(0)
for line in file:
    position=line.find('Male')
    if position!=-1:
        print(line)
print("Removing Duplicates from file based on all columns")
file.seek(0)
# remove duplicates from text file
unique_lines=set()  # Using set to store unique lines
for line in file:
    unique_lines.add(line)
print("Unique Lines are:", len(unique_lines))
# print(unique_lines) # Print set of unique lines
# for line in unique_lines:
#     print(line)
f=open(r"D:/Python/Emp10.txt","w")
# Writing all lines to new file
f.writelines(sorted(unique_lines))
f.close()

# # Writing unique lines to a new file by reading from set line by line
# outfile=open(r"D:/Python/Emp11.txt","w")
# for line in unique_lines:
#     outfile.write(line)
# outfile.close()

# print(sorted(list(unique_lines)))
file.close()