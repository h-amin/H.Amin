x = input("Geef een tekst:")
y = int(input("Geef een rotatie:"))

alfabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w', 'x', 'y', 'z']
caesarlst = []


def caesarcijfer():
    for i in range(0, len(alfabet)):
        caesarlst.append( alfabet[(i+y)%len(alfabet)] )
    input_text = list(x)
    for j in range(len(input_text)):
        if input_text[j] in (' ',',',';'):
            continue
        elif input_text[j].isupper():
            z = alfabet.index(input_text[j].lower())
            input_text[j] = caesarlst[z].upper()
        else:
            z = alfabet.index(input_text[j])
            input_text[j] = caesarlst[z]
    q = ""

    print("Caesarcode: ", q.join(input_text))


caesarcijfer()
