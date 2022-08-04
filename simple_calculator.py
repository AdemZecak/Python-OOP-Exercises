class Calculator():

    def __init__(self,operand_1,operand_2):

        self.operand_1 = operand_1
        self.operand_2 = operand_2 


    def add(self):
        return self.operand_1 + self.operand_2 

    def sub(self):
        return self.operand_1 - self.operand_2 

    def mul(self):
        return self.operand_1 * self.operand_2 

    def div(self):
        try:
            return self.operand_1 / self.operand_2 
        except ZeroDivisionError:
            return 0
        





calc = Calculator(20,0)

print("Your add score is:",calc.add())
print("Your subtraction score is:",calc.sub())
print("Your multiplication score is:",calc.mul())
print("Your division score is:",calc.div())
