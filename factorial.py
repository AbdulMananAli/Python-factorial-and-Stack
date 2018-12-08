class factorial:
    def calFactorial(self, n):
        self.n = n
        if(self.n<=1):
            return 1
        elif (self.n<0):
            return "Negative value"
        else:
            return(self.n*self.calFactorial(self.n-1))

def main():
    objectOne = factorial()
    value = input("Enter factorial value?")
    print objectOne.calFactorial(value)

if __name__ == "__main__": main()
