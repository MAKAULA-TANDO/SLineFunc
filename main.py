import math


def input_x():
    x = int(input("Nceda ufake uququzelelo x:"))
    return x


def input_y():
    y = int(input("Nceda ufake uququzelelo y:"))
    return y


def input_name():
    point_name = (input("Nceda ufake igama lendawo :"))
    return point_name


def calculate_distance(x, y):
    x2 = 0
    y2 = 0
    temp1 = pow((x - y), 2)
    temp2 = pow((x2 - y2), 2)
    result = math.sqrt(temp1 + temp2)
    return result


def reflection_x(y):
    x_ref = (-1) * y
    return x_ref


def reflection_y(x):
    y_ref = (-1) * x
    return y_ref


def quadrant(x, y):

    if x > 0 and y > 0:
        quad = " ilele kwikota yokuqala yokuqala, EMTLA MPUMA."
        if x < 0 and y > 0:
            quad = " ilele kwikota yesibini yesibini, EMTLA MPUMA."
            if x < 0 and y < 0:
                quad = " ilele kwikota yesithathu, EMZANTSI NTSHONA."
                if x > 0 and y < 0:
                    quad = " ilele kwikota yesine, EMZANTSI MPUMA."
                    if x == 0 and y == 0:
                        quad = "ISIPHAMBUKA"
    return quad


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("==================================================================================================")
    print("                          Wamkelekile kwi MATHS APP                                               ")
    print("==================================================================================================")
    x = input_x()
    y = input_y()
    name = input_name()
    print("==================================================================================================")
    finalResult = calculate_distance(x, y)
    ref_X = reflection_x(y)
    ref_Y = reflection_y(x)
    print("**************************************************************************************************")
    print("Imbonakalo X-Axis ngu : (", x, " , ", ref_X, ") Kwinqaku :  ", name)
    print("Imbonakalo Y-Axis ngu : (", ref_Y, " , ", y, ") Kwinqaku :  ", name)
    print("Ifomula yomgca ochanekileyo yile ", "", "y = ", ((y - 0) / (x - 0), "x  + ", y))
    Quadrant = quadrant(x, y)
    print("Ulungelelwaniso lwenqaku: ", "'", name, "'", "", Quadrant)
    print("Umgama phakathi konxibelelaniso kwa (", x, ",", y, ") kunye ( 0,0) :", finalResult)
    print("***********************************************************************************************")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/