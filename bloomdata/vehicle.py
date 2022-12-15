# pylint: disable=missing-final-newline
'''
This file holds two classes: Vehicle and Convertible.
They are a parent and child class
'''
# This is the parent class

class Vehicle:
    '''
    This class holds functions for vehicle info, if it honks
    and it's miles driven
    '''

    def __init__(self, make, model, color, year, mileage):
        '''
        Method for Vehicle class
        '''
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.mileage = mileage

    def honk(self):
        '''
        Honk function for vehicle
        '''
        return 'HOOOOOOOOOOONK!'

    def drive(self, miles_driven):
        '''
        Method for vehicle's miles driven
        '''
        self.mileage += miles_driven
        return self.mileage

    def __repr__(self):
        return f'A {self.color} {self.year} {self.make} {self.model} with {self.mileage} miles.'

if __name__ == '__main__':
    my_veh = Vehicle('Honda', 'CR-V', 'Blue', 2021, 98000)
    # print(my_veh)

# the more specific class is called the child class
# Convertible inherits from Vehicle
# put parent class in () and get the values from parent class using super().__init__()
class Convertible(Vehicle):
    '''
    Docstring for Convertible function
    '''

    def __init__(self, make, model, color, year, mileage, top_down = True):
        super().__init__(make, model, color, year, mileage)
        self.top_down = top_down

    def change_top_status(self):
        '''
        Method that changes the top status of convertible
        '''
        if self.top_down:
            self.top_down = False
            return 'Top is now Up!'
        else:
            self.top_down = True
            return 'Top is now Down!'


    def __repr__(self):
        return f'A {self.color} {self.year} {self.make} {self.model} convertible with {self.mileage} miles.'

if __name__ == '__main__':
    my_veh = Convertible('Honda', 'CR-V', 'Blue', 2021, 98000)

    print(my_veh)
    print(my_veh.top_down)
    print(my_veh.change_top_status())
    print(my_veh.top_down)
    print(my_veh.honk())
    print(my_veh.drive(50000))