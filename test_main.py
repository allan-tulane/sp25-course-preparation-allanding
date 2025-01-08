from main import *


def test_one():
	""" done. """
	assert myfunction('Hello') == 'Hello'
	assert myfunction(11) == 11
	# assert myfunction(6) == -1


def test_two():
	assert myfunction(3 + 4) == 7
	assert myfunction(9 + 4) == 13
