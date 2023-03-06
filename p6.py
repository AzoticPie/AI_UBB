def cauta_nr_majoritar(sir):
    frecventa = {}
    for i in range(len(sir)):
        if sir[i] in frecventa:
            frecventa[sir[i]] += 1
        else:
            frecventa[sir[i]] = 1
        
        if frecventa[sir[i]] >= len(sir)/2:
            nr = sir[i]
            break
    return nr

def test_cauta_nr_majoritar():
    assert 2 == cauta_nr_majoritar([2, 8, 7, 2, 2, 5, 2, 3, 1, 2, 2])
    assert 1 == cauta_nr_majoritar([1,1,1,1])
    assert 2 == cauta_nr_majoritar([2,3,2,3,2])

test_cauta_nr_majoritar()
print("Tests successfull!")