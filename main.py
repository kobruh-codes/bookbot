
def main():
   
    letters = {
        'a' : 0,
        'b' : 0,
        'c' : 0,
        'd' : 0,
        'e' : 0,
        'f' : 0,
        'g' : 0,
        'h' : 0,
        'i' : 0,
        'j' : 0,
        'k' : 0,
        'l' : 0,
        'm' : 0,
        'n' : 0,
        'o' : 0,
        'p' : 0,
        'q' : 0,
        'r' : 0,
        's' : 0,
        't' : 0,
        'u' : 0,
        'v' : 0,
        'w' : 0,
        'x' : 0,
        'y' : 0,
        'z' : 0,
    }

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = len(file_contents.split())
        my_string = file_contents.lower()
        for char in my_string:
            if char == 'a':
                letters['a'] += 1
            if char == 'b':
                letters['b'] += 1
            if char == 'c':
                letters['c'] += 1
            if char == 'd':
                letters['d'] += 1
            if char == 'e':
                letters['e'] += 1               
            if char == 'f':
                letters['f'] += 1
            if char == 'g':
                letters['g'] += 1
            if char == 'h':
                letters['h'] += 1
            if char == 'i':
                letters['i'] += 1
            if char == 'j':
                letters['j'] += 1
            if char == 'k':
                letters['k'] += 1
            if char == 'l':
                letters['l'] += 1
            if char == 'm':
                letters['m'] += 1
            if char == 'n':
                letters['n'] += 1
            if char == 'o':
                letters['o'] += 1
            if char == 'p':
                letters['p'] += 1
            if char == 'q':
                letters['q'] += 1
            if char == 'r':
                letters['r'] += 1
            if char == 's':
                letters['s'] += 1
            if char == 't':
                letters['t'] += 1
            if char == 'u':
                letters['u'] += 1
            if char == 'v':
                letters['v'] += 1
            if char == 'w':
                letters['w'] += 1
            if char == 'x':
                letters['x'] += 1
            if char == 'y':
                letters['y'] += 1
            if char == 'z':
                letters['z'] += 1      

        letter_list = [{'char':char, 'num':count} for char, count in letters.items()]
        letter_list.sort(reverse=True, key=sort_on)

        print(letter_list)

                       
def sort_on(dict):
    return dict["num"]

main()
