def bmi_status(bmi):
    if(bmi>25):
        print("you are over weight")
        print("1")
    if( 15<= bmi <=25):
        print("you are in good shape")
        print("0")
    if(bmi<15):
        print("you need to gain some weight")
        print("-1")


def calculate_and_print_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight / (height * height)
    print("BMI: " + str(bmi))
    bmi_status(bmi)
    return bmi
calculate_and_print_bmi(1.79, 76)



    