#!/usr/bin/env python3
# basic_classes.py

class Circle():
    """class Circle with attributes and methods"""
    def __init__(self, color, radius):
         self.color = color
         self.radius = radius

    def diameter(self):
        """finds the diameter of this circle object"""
        return self.radius * 2 

    def circumference(self):
        """finds the circumference of the circle"""
        return 2 * 3.14 * self.radius

    def isRed(self):
        """returns True if this circle is red"""
        return isRed =="red"

circle_1= Circle("red", 10)
circle_2= Circle("blue", 15)

circle_1.color
circle_2.radius

class GraduateStudent():
    """class GraduateStudent with attributes and methods"""
    def __init__(self, first_name, last_name, year, major):
        self.first_name = first_name
        self.last_name = last_name
        self.year = year
        self.major = major

    def year_matriculated(self):
        """returns year this student matriculated"""
        return "201" + self.year

graduate_student1 = GraduateStudent("John", "Smith", "5", "Bioinformatics")
graduate_student2 = GraduateStudent("Li", "Shang", "1", "History")

graduate_student1.first_name
graduate_student2.major

