def produs_scalar(v1, v2):
    if isinstance(v1, int):
        return v1*v2

    produs = 0
    for i in range(len(v1)):
        produs += produs_scalar(v1[i], v2[i]) 

    return produs

def test_produs_scalar():
    assert 4 == produs_scalar([1,0,2,0,3], [1,2,0,3,1])
    assert 11 == produs_scalar([[1,0,4], 7, [3,6,2]], [[2,4,0], 1, [0,0,1]]) # 1*2 + 1*7 +1*2

test_produs_scalar()
print("Tests successfull!")