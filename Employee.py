
# create a class
class Employee:
    
    # create a class attribute
    vacation_days = 10


# create an object/instance from the class
Mike = Employee()
Jane = Employee()
Bob = Employee()

print(f'Vacation days of Mike is {Mike.vacation_days}')
print(f'Vacation days of Bob is {Bob.vacation_days}')
print(f'Vacation days of Jane is {Jane.vacation_days}')

# change object attribute value
print('Vacations days of Jane increased to 20')
Jane.vacation_days = 20
Jane.is_manager = True

print(Jane.is_manager)

# # change class attribute value
# print('Minimum vacations days of all employess increased to 12')
# Employee.vacation_days = 12

# print(f'Vacation days of Mike is {Mike.vacation_days}')
# print(f'Vacation days of Bob is {Bob.vacation_days}')
# print(f'Vacation days of Jane is {Jane.vacation_days}')

# print(id(Employee.vacation_days))
# print(id(Mike.vacation_days))
# print(id(Bob.vacation_days))
# print(id(Jane.vacation_days))

# # print(Mike)
# # print(type(Mike))
# # print(isinstance(Mike, Employee))
# # print(isinstance('test', str))
# # print(isinstance(1000, int))
# # print(isinstance(True, bool))