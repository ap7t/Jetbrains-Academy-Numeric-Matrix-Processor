from matrix import *

class Menu:
    def __init__(self):
        # self.handle_choice()
        pass

    def print_options(self, options):
        for opt in options:
            print(f"{opt[0]}. {opt[1]}")

    def read_input(self):
        """
            Present menu to user and read input
        """
        options = [(1, "Add matrices"), (2, "Multiply matrix by a constant"),
                   (3, "Multiply matrices"), (4, "Transpose Matrix"), (0, "Exit")]

        self.print_options(options)

        choice = int(input())
        return choice

    def handle_transpose(self):
        options = [(1, "Main diagonal"), (2, "Side diagonal"),
                   (3, "Vertical Line"), (4, "Horizontal Line")]

        self.print_options(options)
        choice = int(input())

        m = Matrix.create()
        if choice == 1:
            mT = m.transpose_diagonal()
        elif choice == 2:
            mT = m.transpose_side_diagonal()
        elif choice == 3:
            mT = m.transpose_vertical()
        elif choice == 4:
            mT = m.transpose_horizontal()

        print(f"The result is \n{mT}")

    def handle_choice(self):
        """
           Perform operation that user wants
        """
        choice = self.read_input()
        if choice == 0:
            quit()
        elif choice == 1:
            m1 = Matrix.create()
            m2 = Matrix.create()
            try:
                m3 = m1 + m2
                print(f"The result is \n{m3}")
            except MatrixException:
                print("The operation can not be performed")
        elif choice == 2:
            m1 = Matrix.create()
            scalar = int(input("Enter constant: "))
            m2 = m1 * scalar
            print(f"The result is \n{m2}")
        elif choice == 3:
            m1 = Matrix.create()
            m2 = Matrix.create()
            try:
                m3 = m1 * m2
                print(f"The result is \n{m3}")
            except MatrixException:
                print("The operation can not be performed")
        elif choice == 4:
            self.handle_transpose()

if __name__ == '__main__':
    m = Menu()