import math


def input_x():
    return int(input("Nceda ufake uququzelelo x:"))


def input_y():
    return int(input("Nceda ufake uququzelelo y:"))


def input_name():
    return (input("Nceda ufake igama lendawo :"))


def calculate_distance(x, y):
    temp2 = pow(0, 2)
    temp1 = pow((x - y), 2)
    return math.sqrt(temp1 + temp2)


def reflection_x(y):
    return (-1) * y


def reflection_y(x):
    return (-1) * x


def quadrant(x, y):

    if x > 0 and y > 0:
        quad = " ilele kwikota yokuqala yokuqala, EMTLA MPUMA."
        if x < 0:
            quad = " ilele kwikota yesibini yesibini, EMTLA MPUMA."
            if y < 0:
                quad = " ilele kwikota yesithathu, EMZANTSI NTSHONA."
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