import os
def write_in_txt_file():
    a = input("Введите текст:\n")
    with open('file.txt', 'w') as writer:
        writer.write(a)
        return True

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

if __name__ == "__main__":
    if(write_in_txt_file()):
        print("[ok] i write")
    print(read_txt_file())
    delete_file()
    print("[ok] i delete")