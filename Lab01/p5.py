def cauta_nr_repetat(sir):
    frecventa = {}
    for i in range(len(sir)):
        if sir[i] in frecventa:
            return sir[i]
        else:
            frecventa[sir[i]] = True
    return -1

def test_nr_repetat():
    assert 2 == cauta_nr_repetat([1, 2, 3, 4, 2])
    assert 5 == cauta_nr_repetat([1,2,3,4,5,5])

test_nr_repetat
print("Tests successfull!")