import numpy

class matixMath:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.matix = []
        for row in self.rows:
            self.matix.append([])
            for column in self.columns:
                self.matix[row].append(0)

    # member function for dot product
    def dot(self, matrix2):
        if self.rows == matrix2.rows:
            if self.columns == matrix2.columns:
                for row in self.rows:
                    for column in self.columns:
                        self.matix[row][column] *= matrix2.matrix[row][column]
    
    # non-member function for dot product
    def dot1(matrix1, matrix2):
        if matrix1.rows == matrix2.rows:
            if matrix1.columns == matrix2.columns:
                matrix3 = matixMath(matrix1.rows, matrix1.columns)
                for row in matrix1.rows:
                    for column in matrix1.columns:
                        matrix3.matix[row][column] = matrix1.matix[row][column] * matrix2.matrix[row][column]
                return matrix3

    # elementwise operation
    # addition
    def add(self, value):
        for row in self.rows:
            for columns in self.columns:
                self.matix[row][columns] += value
            
    # subtraction
    def subtraction(self, value):
        for row in self.rows:
            for columns in self.columns:
                self.matix[row][columns] -= value
            
    # multiplication
    def multiplication(self, value):
        for row in self.rows:
            for columns in self.columns:
                self.matix[row][columns] *= value
            
    # division
    def division(self, value):
        for row in self.rows:
            for columns in self.columns:
                self.matix[row][columns] /= value

    # activation function application

    def activation(self,func):
        for row in self.rows:
            for columns in self.columns:
                self.matix[row][columns] = func(self.matix[row][columns])

    # transpostion
    def transpose(self):
        tempMatrix = []
        for column in self.columns:
            tempMatrix.append([])
            for row in self.rows:
                tempMatrix[column].append(self.matix[row][column])
        self.rows, self.columns = self.columns, self.rows
        self.matrix = tempMatrix
