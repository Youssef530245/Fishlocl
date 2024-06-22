import geocoder

def print_banner(word):
    letters = {
        'F': ['  #####', '  #', '  #####', '  #', '  #'],
        'i': ['   #', '   #', '   #', '   #', '   #'],
        's': ['  #####', '  #', '  #####', '      #', '  #####'],
        'h': ['  #    #', '  #    #', '  ######', '  #    #', '  #    #'],
        'l': ['  #', '  #', '  #', '  #', '  #####'],
        'o': ['   ###', '  #   #', '  #   #', '  #   #', '   ###'],
        'c': ['  #####', '  #', '  #', '  #', '  #####']
    }

    for i in range(5):
        for letter in word:
            print(letters[letter][i], end='  ')
        print()

if __name__ == "__main__":
    word = "Fishloc"
    print_banner(word)
    print()
    print()
    print("                          Made by Eng/Youssef Mohamed")
    
    
    
#--------------------------------------------------------------------------------#

def get_location_from_ip(ip_address):
    g = geocoder.ip(ip_address)
    if g.ok:
        return f"{g.country}, {g.city}"
    else:
        return "Location not found"
print()
ip_address = input("     Enter the IP address: ")
location = get_location_from_ip(ip_address)
print()
print("     Location:", location)
    
    
    





