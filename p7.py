def k_cel_mai_mare(sir, k):
    return sorted(sir, reverse=True)[k-1]

def test_k_cel_mai_mare():
    assert 7 == k_cel_mai_mare([7,4,6,3,9,1], 2)
    assert 2 == k_cel_mai_mare([2,8,7,2,2,5,2,3,1], 5)

test_k_cel_mai_mare()
print("Tests successfull!")
