class Person(object):
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
    def printPerson(self):
        print "Name:", self.lastName + ",", self.firstName
        print "ID:", self.idNumber

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        super(Student, self).__init__(firstName, lastName, idNumber)
        self.scores = scores
        
    def calculate(self):
        total_score = 0
        for score in self.scores:
            total_score += score

        average = total_score / len(self.scores)
            
        if average < 40:
	       return 'T'

        elif average >= 40 and average < 55:
	       return 'D'

        elif average >= 55 and average < 70:
            return 'P'

        elif average >= 70 and average < 80:
            return 'A'

        elif average >= 80 and average < 90:
            return 'E'
            
        elif average >=90 and average <= 100:
            return 'O'


jill = Student('Jill', 'Berardini', '1', [95, 90, 100, 105])
print jill.calculate()
print jill.firstName