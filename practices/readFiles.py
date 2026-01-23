

# Read Files

def read_Text_file(file_path):
    """Read and prints the file content"""
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
def read_CSV_file(file_path):
    pass

def read_excel_file(file_path):
    pass


print(read_Text_file(r'D:\Python\Python Notes.txt'))