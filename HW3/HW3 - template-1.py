#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Notice: do not change these function name
class MovingAverage:

    def __init__(self, size):
        self.size = size
        self.data = []

    def next(self, val):
        self.data.append(val)
        if len(self.data) == 0:
            return 0
        elif(len(self.data) > self.size):
            return sum(self.data[(len(self.data)-self.size):])/self.size
        else:
            return sum(self.data)/len(self.data)


class subway:

    def __init__(self):
        self.getOn = dict()
        self.getOff = dict()
        self.average = dict()

    def checkIn(self, id, stationName, t):
        self.getOn[id] = (stationName, t)

    def checkOut(self, id, stationName, t):
        self.getOff[id] = (stationName, t)
        if ((self.getOn[id][0], self.getOff[id][0]) in self.average):
            self.average[(self.getOn[id][0], self.getOff[id][0])].append(
                (int(self.getOff[id][1])-int(self.getOn[id][1])))
        else:
            self.average[(self.getOn[id][0], self.getOff[id][0])] = [int(
                self.getOff[id][1])-int(self.getOn[id][1])]

    def getAverageTime(self, startStation, endStation):
        return sum(self.average[(startStation, endStation)])/len(self.average[(startStation, endStation)])


class Linear_regression:

    def __init__(self, x, y, m, c, epochs, L=0.001):
        self.x = x
        self.y = y
        self.m = m
        self.c = c
        self.epochs = epochs
        self.L = L

    def gradient_descent(self):

        loop = 0
        while loop < self.epochs:
            Dw = []
            Dc = []
            for i in range(len(self.x)):
                y_pred = (self.x[i][0] * self.m) + self.c
                valueb = self.x[i][0]*(y_pred - self.y[i])
                Dw.append(valueb)
                valuec = y_pred - self.y[i]
                Dc.append(valuec)

            dw = sum(Dw)/len(Dw)
            dc = sum(Dc)/len(Dc)
            self.m = self.m - self.L * dw
            self.c = self.c - self.L * dc
            loop += 1
        return(self.m, self.c)

    def predict(self, x_new):
        answer = []
        for i in range(len(x_new)):
            answer.append(self.m*x_new[i] + self.c)
        return (answer)


class LCG:

    def __init__(self, seed, multiplier, increment, modulus):
        self.seed = seed % modulus
        self.multiplier = multiplier
        self.increment = increment % modulus
        self.modulus = modulus

    def get_seed(self):
        return self.seed

    def set_seed(self, new_seed):
        self.seed = new_seed % self.modulus
        return self.seed

    def initialize(self):
        pass

    def gen(self):
        pass

    def seq(self, num):
        pass


if __name__ == "__main__":

    x = [[0.18], [1.0], [0.92], [0.07], [0.85], [0.99], [0.87]]
    y = [109.85, 155.72, 137.66, 76.17, 139.75, 162.6, 151.77]
    x_new = [0.9, 0.8, 0.40, 0.7]

    # Test Question 1
    print("\nQ1")
    windowsize = 3
    moving_average = MovingAverage(windowsize)
    step1 = moving_average.next(1)
    print("my answer: ", step1)
    print("right answer: 1.0")
    print("--------------")
    step2 = moving_average.next(10)
    print("my answer: ", step2)
    print("right answer: 5.5")
    print("--------------")
    step3 = moving_average.next(3)
    print("my answer: ", step3)
    print("right answer: 4.66667")
    print("--------------")
    step4 = moving_average.next(5)
    print("my answer: ", step4)
    print("right answer: 6.0")
    print("--------------")

    # Test Question 2
    print("\nQ2")
    s = subway()
    s.checkIn(10, 'Leyton', 3)
    s.checkOut(10, 'Paradise', 8)
    print("my answer: ", s.getAverageTime('Leyton', 'Paradise'))
    print("right answer: 5.0")
    print("--------------")
    s.checkIn(10, 'Leyton', 10)
    s.checkOut(10, 'Paradise', 16)
    print("my answer: ", s.getAverageTime('Leyton', 'Paradise'))
    print("right answer: 5.5")
    print("--------------")
    s.checkIn(10, 'Leyton', 21)
    s.checkOut(10, 'Paradise', 30)
    print("my answer: ", s.getAverageTime('Leyton', 'Paradise'))
    print("right answer: 6.667")
    print("--------------")

    # Test Question 3
    print("\nQ3")
    Linear_model = Linear_regression(x, y, 0, 0, 500, 0.001)
    print("I use m=0, c=0, epochs=500, L=0.001")
    print("my m and c: ", Linear_model.gradient_descent())
    print("right m and c:(35.97890301691016, 46.54235227399102)")
    print("--------------")
    print("my predict: ", Linear_model.predict(x_new))
    print(
        " right predict: [78.92336498921017, 75.32547468751915, 60.93391348075509, 71.72758438582812]")

    # Bonus Question
    print("\nBonus")
    print("set seed = 1, multiplier = 1103515245, increment = 12345, modulus = 2**32")
    lcg = LCG(1, 1103515245, 12345, 2**32)
    print("my seed is: ", lcg.get_seed())
    print("right seed is: 1")
    print("the seed is setted with: ", lcg.set_seed(5))
    print("right seed is setted with 5")
    print("the LCG is initialized with seed: ", lcg.initialize())
    print("the LCG is initialized with seed 5")
    print("the next random number is: ", lcg.gen())
    print("right next random number is: 0.2846636981703341")
    print("the first ten sequence is: ", lcg.seq(10))
    print("the first ten sequence is: ", [0.6290451611857861, 0.16200014390051365, 0.4864134492818266, 0.655532845761627,
          0.8961918593849987, 0.2762452410534024, 0.8611323081422597, 0.9970241007395089, 0.798466683132574, 0.46138259768486023])
