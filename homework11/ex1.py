def power_factory(power):
    def power_number(x):
        return x ** power

    return power_number


square = power_factory(2)
cube = power_factory(3)

print(square(5))
print(cube(2))
print(square(10))