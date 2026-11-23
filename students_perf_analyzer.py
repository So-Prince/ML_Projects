import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

class StuPerAnal:
    def __init__(self):
        # self.file = file
        pass

    def loadfile(self):
        try:
            file = pd.read_csv("students.csv")
            print(file)
        except FileNotFoundError:
            print("File does not exit")
        
    def mean(self):
        file = pd.read_csv("students.csv")
        # ff = file['math'].mean()  #pandas
        # ff = np.mean(file['math'])      #numpy
        print(f"Math mean value: {np.mean(file['math'])}")
        print(f"English mean value: {np.mean(file['english'])}")
        print(f"Science mean value: {np.mean(file['science'])}")

    def median(self):
        file = pd.read_csv("students.csv")
        print(f"Math median value: {np.median(file['math'])}")
        print(f"English median value: {np.median(file['english'])}")
        print(f"Science median value: {np.median(file['science'])}")

    def mode(self):
        file = pd.read_csv("students.csv")
        print(f"Math mode value: {stats.mode(file['math'])}")
        print(f"English mode value: {stats.mode(file['english'])}")
        print(f"Science mode value: {stats.mode(file['science'])}")

    def std(self):
        file = pd.read_csv("students.csv")
        print(f"Math std value: {np.std(file['math'])}")
        print(f"English std value: {np.std(file['english'])}")
        print(f"Science std value: {np.std(file['science'])}")

    def var(self):
        file = pd.read_csv("students.csv")
        print(f"Math variance value: {np.var(file['math'])}")
        print(f"English variance value: {np.var(file['english'])}")
        print(f"Science variance value: {np.var(file['science'])}")
        
    def percentile(self):
        file = pd.read_csv("students.csv")
        # print(f"Math percentile value: {np.percentile(file['math'],50)}")
        # print(f"English percentile value: {np.percentile(file['english'],75)}")
        # print(f"Science percentile value: {np.percentile(file['science'],90)}")
        print("50th percentile:", file.quantile(0.50))
        print("75th percentile:", file.quantile(0.75))
        print("90th percentile:", file.quantile(0.90))
        
    def histogram(self):
        file = pd.read_csv("students.csv")
        plt.hist(file, bins=10)
        # plt.hist(file['english'])
        # plt.hist(file['science'])
        plt.xlabel("scores")
        plt.ylabel("students")
        plt.title("Histogram chart of scores vs subjects")
        plt.show()

        # plt.hist(file['english'])
        # plt.xlabel("scores")
        # plt.ylabel("students")
        # plt.title("Histogram chart of student scores vs english")
        # plt.show()
        # plt.hist(file['science'])
        # plt.xlabel("scores")
        # plt.ylabel("students")
        # plt.title("Histogram chart of student scores vs science")
        # plt.show()

call = StuPerAnal()


name = input("What's your name Sir/Ma? ").title().strip()
print("-"*30)
print("STUDENT PERFORMANCE ANALYZER".center(30))
print("-"*30)
print(f"Welcome {name} to our easy-to-use analyzer.\n")

while True:
    print("1. Type '1' to view the student database")
    print("2. Type '2' to calculate/get the mean score")
    print("3. Type '3' to calculate/get the median score")
    print("4. Type '4' to calculate/get the mode score")
    print("5. Type '5' to calculate/get the standard deviation score")
    print("6. Type '6' to calculate/get the variance value")
    print("7. Type '7' to calculate/get the percentile score")
    print("8. Type '8' to plot graphs")
    print("9. Type '9' to exit the program\n")

    try:
            activity = int(input("What do you want to do? "))
            if activity == 1:
                call.loadfile()
                print()
            elif activity == 2:
                call.mean()
                print()
            elif activity == 3:
                call.median()
                print()
            elif activity == 4:
                call.mode()
                print()
            elif activity == 5:
                call.std()
                print()
            elif activity == 6:
                call.var()
                print()
            elif activity == 7:
                call.percentile()
                print()
            elif activity == 8:
                call.histogram()
                print()
            elif activity == 9:
                print("Goodbye, see you later!")
                exit(0)
            else:
                print("Wrong integer. Try again using 1-9\n")
    except ValueError:
            print("You used an invalid int or a str. Try again!\n")