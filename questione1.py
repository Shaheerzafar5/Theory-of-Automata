class question1:
    chracter = ''
    initial_state = 0
    current_state = 0
    valid = False

    def __int__(self):
        self.chracter = ''
        self.initial_state = 0

    def constructor(self, c, i):
        self.chracter = c
        self.initial_state = i

    def transition(self, alphabet, state):
        if state == 0:
            if alphabet == 0:
                state = 1
            elif alphabet == 1:
                state = 3
            else:
                print("Invalid Chracter: ", alphabet)
        elif state == 1:
            if alphabet == 0:
                state = 0
            elif alphabet == 1:
                state = 2
            else:
                print("Invalid Chracter: ", alphabet)
        elif state == 2:
            if alphabet == 0:
                state = 3
            elif alphabet == 1:
                state = 1
            else:
                print("Invalid Chracter: ", alphabet)
        elif state == 3:
            if alphabet == 0:
                state = 2
            elif alphabet == 1:
                state = 0
            else:
                print("Invalid Chracter: ", alphabet)
        return state

    def DFA_working(self, neword):
        self.chracter = neword
        for i in self.chracter:
            self.current_state = self.transition(int(i), self.current_state)
        if self.current_state == 0:
            print("Valid String")
           
        else:
            print("Invalid String")


if __name__ == "__main__":
    print("Task1 DFA Starting")
    inputString = str(input("Enter Your String: "))
    S = question1()
    S.DFA_working(inputString)