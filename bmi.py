def bmi_status(bmi):
    if bmi>25:
        print("you are over weight")
        sta =1
    if( 15<= bmi <=25):
        print("you are in good shape")
        sta =0
    if(bmi<15):
        print("you need to gain some weight")
        sta =-1
    return sta

def calculate_and_print_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight / (height * height)
    print("BMI: " + str(bmi))
    status =bmi_status(bmi)
    return status


    
calculate_and_print_bmi(1.65 ,60)



    