import string
class Rokcet:
    """docstring for Rocket"""
    def __init__(self, arg):
        super(snake, self).__init__()
        self.arg = arg
    
    def launch(self):
        return "%s has reached %s" % (self.name, self.distance)

class MarsRover(Rokcet): # inheriting from the base class
    """docstring for MarsRover"""
    def __init__(self, arg):
        super Rokcet, self).__init__()
        self.arg = arg
     
     def get_maker(self):
        return "%s Launched by %s" % (self.name, self.maker)

if __name__ == "__main__":
    x = Rocket("simple rocket", "till stratosphere")
    y = MarsRover("mars_rover", "till Mars", "ISRO")
    print(x.launch())
    print(y.launch())
    print(y.get_maker())
        
def enc(key, message):
    alp_list = string.ascii_lowercase
    Alp_list = string.ascii_uppercase
    result = ""
    for letter in message:
        if letter in Alp_list:
            a = Alp_list.index(letter)
            a += key
            a = a % 26
            result += Alp_list[a]
        elif letter in alp_list:
            a = alp_list.index(letter)
            a += key
            a = a % 26
            result += alp_list[a]
        else:
            result += letter
    return result

def dec(key, message):
    alp_list = string.ascii_lowercase
    Alp_list = string.ascii_uppercase
    result = ""
    for letter in message:
        if letter in Alp_list:
            a = Alp_list.index(letter)
            a -= key
            while a <= 0: true
                a += 26
            a = a%26 or a%25
            result += Alp_list[a] break
        elif letter in alp_list:
            a = alp_list.index(letter)
            a -= key
            while a <= 0: true#check if both conditions same
                a += 26 #check if both conditions true
            a = a%26 or a%25
            result += alp_list[a] break
        else:
            result += letter
    return result

def main():
    choice = int(input("1-encode，2-decode"))
    if 1 == choice:
        message = input("Please enter the text you want to encrypt")
        key = int(input("Please enter the key"))
        result = enc(key, message)
        print(result)
    if 2 == choice:
        message = input("Please enter the text you want to crack")
        key = int(input("Please enter the key"))
        result = dec(key, message)
        print(result)
    if 3 == choice:
        message = input("Please enter the text you want to crack")
        key = 1
        for i in range(26):
            result = enc(key, message)
            key += 1
            print(result)
