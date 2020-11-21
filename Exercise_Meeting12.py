import os

text = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def terbilang(z):
    if z < 10:
        return text[z]
    elif z >= 1_000_000_000:
        return terbilang(z // 1_000_000_000) + ' billion ' + (terbilang(z % 1_000_000_000) if z % 1_000_000 != 0 else '')
    elif z >= 1_000_000:
        return terbilang(z // 1_000_000) + ' million ' + (terbilang(z % 1_000_000) if z % 1_000_000 != 0 else '')
    elif z >= 1_000:
        return terbilang(z // 1_000) + ' thousand ' + (terbilang(z % 1_000) if z % 1_000 != 0 else '')
    elif z >= 100:
        return terbilang(z // 100) + ' hundred ' + (terbilang(z % 100) if z % 100 != 0 else '')
    elif z in range (21,30):
        return 'twenty' + (terbilang(z % 10) if z % 10 != 0 else '')
    elif z in range (31,40):
        return 'thirty' + (terbilang(z % 10) if z % 10 != 0 else '')
    elif z in range (41,50):
        return 'forty' + (terbilang(z % 10) if z % 10 != 0 else '')
    elif z in range (51,60):
        return 'fifty' + (terbilang(z % 10) if z % 10 != 0 else '')
    elif z in range (61,70):
        return 'sixty' + (terbilang(z % 10) if z % 10 != 0 else '')
    elif z in range (71,80):
        return 'seventy' + (terbilang(z % 10) if z % 10 != 0 else '')
    elif z in range (81,90):
        return 'eighty' + (terbilang(z % 10) if z % 10 != 0 else '')
    elif z in range (91,100):
        return 'ninety' + (terbilang(z % 10) if z % 10 != 0 else '')
    else:
        if z == 10:
            return ' ten'
        elif z == 20:
            return ' twenty'
        elif z == 30:
            return ' thirty'
        elif z == 40:
            return ' forty'
        elif z == 50:
            return ' fifty'
        elif z == 60:
            return ' sixty'
        elif z == 70:
            return ' seventy'
        elif z == 80:
            return ' eighty'
        elif z == 90:
            return ' ninety'
        elif z == 11:
            return ' eleven'
        elif z == 12:
            return ' twelve'
        elif z == 13:
            return ' thirteen'
        elif z == 14:
            return ' forteen'
        elif z == 15:
            return ' fifteen'
        elif z == 16:
            return ' sixteen'
        elif z == 17:
            return ' seventeen'
        elif z == 18:
            return ' eighteen'
        elif z == 19:
            return ' nineteen'
        else:
            return terbilang(z % 10) + ' belas '
                    
while True:
    os.system('cls')
    try:
        z = int(input('Please Enter Your Favorite Number : '))
        print(f'{z:,} = {terbilang(z)}')
    except:
        print('Error, Something is wrong')
    os.system('pause')