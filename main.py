
def delete_file():
    file_path = 'file.txt'
    try:
        os.remove(file_path)
        return True
    except:
        print("The system cannot find the file specified")
        return False

def read_txt_file(): 
    file = 'file.txt'
    with open(file, 'r', encoding='utf-8') as f:
        data = f.read()
        print(data)
        return data

