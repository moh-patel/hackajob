MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

print(MORSE_CODE_DICT['A'])


text = "The wizard quickly jinxed the gnomes before they vaporized."

translation = ""
for i in text:
    if not i.isspace():
        translation += MORSE_CODE_DICT[i.upper()] + " "
    else:
        translation +="  "
print(translation)

if translation.strip(" ") == "- .... .   .-- .. --.. .- .-. -..   --.- ..- .. -.-. -.- .-.. -.--   .--- .. -. -..- . -..   - .... .   --. -. --- -- . ...   -... . ..-. --- .-. .   - .... . -.--   ...- .- .--. --- .-. .. --.. . -.. .-.-.-":
    print(True)


REVERSED_CODE_DICT = dict((y,x.lower()) for x,y in MORSE_CODE_DICT.items())
print(REVERSED_CODE_DICT)
morse = "- .... .   .-- .. --.. .- .-. -..   --.- ..- .. -.-. -.- .-.. -.--   .--- .. -. -..- . -..   - .... .   --. -. --- -- . ...   -... . ..-. --- .-. .   - .... . -.--   ...- .- .--. --- .-. .. --.. . -.. .-.-.-"
print(REVERSED_CODE_DICT['....'])
translation = ""
char = ""
space = 0
for i in morse:
    if not i.isspace():
        if space == 0:
            char+=i
        
        elif space == 1:
            print(char)
            translation+= REVERSED_CODE_DICT[char]
            char =i
            space=0
        
        elif space ==3:
            translation+=REVERSED_CODE_DICT[char] + " "
            char=i
            space=0
        elif space ==2 or space%3!=0:
            translation = "Invalid Morse Code Or Spacing"
            break

    elif i.isspace():
        space+=1  
translation+=REVERSED_CODE_DICT[char]    
print(translation)