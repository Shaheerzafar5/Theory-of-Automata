class question2:
    chracter = ''
    initial_state = 0
    current_state = 0
    valid = False

    def __int__(self):
        self.chracter = ''
        self.initial_state = 0

    def constructor(self, w, i):
        self.chracter = w
        self.initial_state = i

    def transition(self, alphabet, state):
        if state == 0:
            if alphabet == 0:
                state = 3
            elif alphabet == 1:
                state = 1
            else:
                print("Invalid Chracter: ", alphabet)

        elif state == 1:
            if alphabet == 0:
                state = 1
            elif alphabet == 1:
                state = 2
            else:
                print("Invalid Chracter: ", alphabet)

        elif state == 2:
            if alphabet == 0:
                state = 2
            elif alphabet == 1:
                state = 2
            else:
                print("Invalid Chracter: ", alphabet)

        elif state == 3:
            if alphabet == 0:
                state = 4
            elif alphabet == 1:
                state = 3
            else:
                print("Invalid Chracter: ", alphabet)

        elif state == 4:
            if alphabet == 0:
                state = 4
            elif alphabet == 1:
                state = 4
            else:
                print("Invalid Chracter: ", alphabet)

        return state

    def Checking_DFA(self, neword):
        self.chracter = neword
        for i in self.chracter:
            self.current_state = self.transition(int(i), self.current_state)
        if self.current_state == 2 or self.current_state == 4:
            print("Valid String")
        else:
            print("Invalid String")


if __name__ == "__main__":
    print("Question2 DFA Starting")
    inputString = str(input("Enter Your String: "))
    S = question2()
    S.Checking_DFA(inputString)