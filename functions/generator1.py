
def acronym_generator(listofword):
    for word in listofword:
        wl = word.split()
        acr = ''
        for w in wl:
            acr += w[0].upper()
        yield acr

words = ['Project Manager','Software Engineer','Database Administrator']
for acr in acronym_generator(words):
    print(acr)