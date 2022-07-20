def format_title(title) : 
    print("="*(64-int((len(title)/2))) + title + (64-int((len(title)/2)))*"=")

def login_check(file_path): 
    id = input("Enter your id \n- ")
    file = open(file_path, "r")
    user_list = file.readlines()
    id_list = []
    pass_list = []
    for i in user_list : 
        a = i.split()
        id_list.append(a[0])
        pass_list.append(a[1])
    while id not in id_list :
        print("Invalid id")
        id = input("Enter your id\n- ")
    password = input("Enter your passwrod\n- ")
    while password != pass_list[id_list.index(id)] :
        print("Wrong password")
        password = input("Enter your password\n- ")
    print(format_title("WELCOME BACK"))
    file.close()


def login_create(file_path) :
    id = input("Enter the id you want to keep\n- ")
    password = input("Enter the password you want to keep\n- ")
    file = open(file_path, "a+")
    id_str =   id + " " + password + "\n"
    file.write(id_str)
    print(format_title("Id created"))
    login_check(file_path)
    file.close()

file_path = r"C:\Users\Nikhil\OneDrive\Desktop\database.txt"
try : 
    file = open(file_path, "r")
    print("File exists")
except : 
    file = open(file_path, "w+")
    print("File created")
file.close()

while 2 > 1 :
    answer = input("Are you an existing user?\n*yes\n*no\n- ")
    while answer.lower() not in ["yes", "no"] :
        print("Invalid answer")
        answer = input("Are you an existing user?\n*yes\n*no\n- ") 

    if answer.lower() == "yes" :
        print(format_title("SIGN IN PAGE"))
        login_check(file_path)
    else :
        print(format_title("SIGN UP PAGE"))
        login_create(file_path)
