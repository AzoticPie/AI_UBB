import math

def distanta_euclidiana(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1))

def test_distanta_euclidiana():
    assert 5 == distanta_euclidiana([1,5], [4,1])
    assert 10 == distanta_euclidiana([0,0], [10,0])
    assert 0 == distanta_euclidiana([4,3], [4,3])


test_distanta_euclidiana()
print("Tests successfull!")