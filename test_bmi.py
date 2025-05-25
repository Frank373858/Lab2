import bmi


print ("test_bmi")

def test_bmi_overweight():
    result= bmi.calculate_and_print_bmi(height=1.8, weight=1000)
    expectedresult=1
    assert(result == expectedresult)


