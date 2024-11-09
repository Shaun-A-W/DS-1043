"""
Testing module for fuzzy matching functions.
Constructed by Shaun W. alongside Lab 9.

"""

import lab9 as ds

# Test switch variable. true = on. false = off.
# IF statement located at end of file.
SWITCH = True

def test_ngrams():
    assert ds.ngrams('cop') == ['cop','co','op','c','o','p']
    assert ds.ngrams('part') == ['part','par','art','pa','ar','rt','p','a','r','t']
    assert ds.ngrams('as') == ['as','a','s']


# Note that the build_index() function utilizes a second add_to_index()
# function. Though, it cannot be tested on its own with its current construction
def test_build_index():
    assert ds.build_index(['car','art']) == {
        'c': ['car'], 'a': ['car','art'], 'r': ['car','art'],
        'ca':['car'], 'ar':['car','art'], 'car': ['car'],
        't': ['art'], 'rt': ['art'], 'art': ['art']}
    assert ds.build_index(['is','as']) == {
        'i':['is'], 's':['is','as'], 'is':['is'], 'a':['as'], 'as':['as'],}


def test_fuzzy():
    test_index = ds.build_index(['car','art','stop','cop','knock'])
    assert ds.fuzzy_pick('ar',test_index) == {'car':'ar', 'art':'ar'}
    assert ds.fuzzy_pick('co',test_index) == {'cop':'co', 'car':'c', 'stop':'o', 'knock':'c'}


# Test switch
if SWITCH:
    test_ngrams()
    test_build_index()
    test_fuzzy()