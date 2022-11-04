class Question3:
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
            if alphabet == 'c':
                state = 1
            elif alphabet == 'a':
                state = 2
            elif alphabet == 'b':
                state = 2
            else:
                print("Invalid Chracter: ", alphabet)

        elif state == 1:
            if alphabet == 'a':
                state = 3
            elif alphabet == 'b':
                state = 2
            elif alphabet == 'c':
                state = 2
            else:
                print("Invalid Chracter: ", alphabet)

        elif state == 2:
            if alphabet == 'a':
                state = 3
            elif alphabet == 'b':
                state = 3
            elif alphabet == 'c':
                state = 3
            else:
                print("Invalid Chracter: ", alphabet)

        elif state == 3:
            if alphabet == 'a':
                state = 3
            elif alphabet == 'b':
                state = 3
            elif alphabet == 'c':
                state = 3
            else:
                print("invalid Chracter: ", alphabet)
        return state


    def Checking_DFA(self, neword):
        self.chracter = neword
        for i in self.chracter:
            self.current_state = self.transition(str(i), self.current_state)
        if self.current_state == 2:
            print("Valid String")
            
        else:
            print("Invalid String")


if __name__ == "__main__":
    print("Quetion3 DFA Starting")
    inputString = str(input("Enter Your String: "))
    S = Question3()
    S.Checking_DFA(inputString)