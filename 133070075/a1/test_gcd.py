from gcd import gcd
def test_gcd():
	assert gcd(48,16)==16
	assert gcd(44,19)==1
	assert gcd(-48,16)
	assert gcd(49.5,16)
