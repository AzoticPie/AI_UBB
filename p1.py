def ultimul_cuvant(text):
    cuvinte = text.lower().strip('.,?!').split()
    return sorted(cuvinte)[-1]

def test_ultimul_cuvant():
    assert "si" == ultimul_cuvant("Ana are mere rosii si galbene")
    assert "zoaie" == ultimul_cuvant("Cine a castigat ultimul concurs de mancat zoaie.")

test_ultimul_cuvant()
print("Tests successfull!")
