# function to return output
def power_of_two(power):
     # for loop starting from 0 till a - 1
        for i in range(0, power + 1):
            # to calculate power
            print("2 ^ ", i, " : ", 2 ** i)



if __name__ == "__main__":
        number = int(input("Enter he power of two till you want the output : "))
        print("Power of two are")
        power_of_two(number)