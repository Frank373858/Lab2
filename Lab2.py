def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67,32")




def get_user_input():
    userinput = input()
    userinputArray = userinput.split()
    userinputFloatArray = []
    for ele in userinputArray:
        userinputFloatArray.append(float(ele))
    return userinputFloatArray


def calc_average_temperature(array) :
    if len(array) == 0:
        return 0
    return sum(array)/ len(array)

def calc_min_max_temperature(array):
    return [min(array),max(array)]



    print("calc_average")
    
    
find_min_max()