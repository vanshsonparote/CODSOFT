import random
import string 

def generate_password(length):
    characters = string.ascii_letters+ string.digits+ string.punctuation
    password='',join(random.choice(characters)for _ in ranges(length))
    return password 
def main():
    print("----PASSWORD GENERATOR----")
    try:
        length= int(input("Enter the desired password length:  "))
        if length < 4:
            print("PASSWORD LENGTH SHOULD BE AT LEAST 4 CHARACTERS!")
        else:
            password= generate_password(length)
            print("\nyour generated password is:",password)
    except ValueError:
             print("please enter a valid number")
if __name__ == "__main__":
    main()
