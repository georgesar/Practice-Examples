import winsound, time

mc = {
    'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.', 'g':'--.', 'h':'....',
    'i':'..','j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--', 'n':'-.', 'o':'---', 'p':'.--.',
    'q':'--.-', 'r':'.-.','s':'...', 't':'-', 'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-',
    'y':'-.--', 'z':'--..', ' ' : ' '
}

inp = raw_input('Please enter a word to convert to Morse: ').lower()
w = []
def con(inp):
    for i in inp:
        w.append(mc[i])
    print '|'.join(w)
    for el in str(w):
        if el == '.':
            winsound.Beep(1700, 300)
        elif el == '-':
            winsound.Beep(1700, 800)
        else:
            time.sleep(0.3)

con(inp)