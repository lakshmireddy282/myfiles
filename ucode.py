Suppose user selfies are saved locally in the format "name-ucode", where ucode is a unique code for that user. For example, for a user called Paul, his selfie will be saved as "paul-12345.jpg". Write a function which takes in the selfie name and returns the unique code. For example, the function will take input "paul-12345.jpg" and return "12345".

def ucode(string):
    res = ''.join(filter(lambda i: i.isdigit(), string))
    return res
string=input("enter the sefie_name:")
print(ucode(string))

   