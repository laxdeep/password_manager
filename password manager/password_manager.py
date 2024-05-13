from cryptography.fernet import Fernet

def create_key():
    key = Fernet.generate_key()
    with open('key.key','wb') as key_file:
        key_file.write(key)

def load_key():
    file = open('key.key','rb')
    key = file.read()
    return key

master_password = input("enter your master password")#encode function also converts string into its byte format
key = load_key() + master_password.encode() #we need to convert master to bytes bcoz load_key is in bytes
fer = Fernet(key)




def view():
    with open("password.txt",'r') as f:
        print("User | Password")
        for line in f.readlines():
            data = line.strip('\n')
            user , pas = data.split('|')
            print("USER: "+ user + " , " + "PASSWORD : " + fer.decrypt(pas.encode()).decode() )

def add():
    name = input("account name: ")
    pwd = input("password :")
    with open("password.txt",'a') as f: # for 'a' if file not exist new file will be created else will append in existing
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n") 

while True:
    mode = input("add new password or view existing(add,view,q)")
    if mode == 'q':
        break
    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print("invalid mode")
        continue
