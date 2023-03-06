def cuvinte_unice(text):
    cuvinte = text.lower().strip('.,?!').split()
    frecventa_cuvinte = {}
    for cuv in cuvinte:
        if cuv not in frecventa_cuvinte:
          frecventa_cuvinte[cuv] = 1
        else:
          frecventa_cuvinte[cuv] += 1

    cuvinte_unice_rez = []
    for cuv in frecventa_cuvinte.keys():
       if frecventa_cuvinte[cuv] == 1:
            cuvinte_unice_rez.append(cuv)

    return cuvinte_unice_rez

def test_cuvinte_unice():
    assert ["mere", "rosii"] == cuvinte_unice("ana are ana are mere rosii ana")
    assert [] == cuvinte_unice("ana are ana are mere rosii ana Mere Rosii.")
    assert ["hai"] == cuvinte_unice("Hai!")


test_cuvinte_unice()
print("Tests successfull!")