from plates import is_valid

def test_valid_plates():
    assert is_valid("CS50") == True
    assert is_valid("HELLO") == True
    assert is_valid("AAA222") == True  

def test_invalid_length():
    assert is_valid("A") == False      
    assert is_valid("ABCDEFG") == False  

def test_start_with_two_letters():
    assert is_valid("50CS") == False   
    assert is_valid("A2") == False     

def test_no_leading_zero():
    assert is_valid("CS05") == False   
    assert is_valid("CS50") == True    

def test_no_middle_numbers():
    assert is_valid("AAA22A") == False  
    assert is_valid("AA2A2") == False   

def test_no_punctuation():
    assert is_valid("PI3.14") == False
    assert is_valid("HELLO!") == False
