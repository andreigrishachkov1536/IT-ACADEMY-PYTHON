def power_factory(power):
    def power_number(x):
        return x ** power

    return power_number


square = power_factory(2)
cube = power_factory(3)

print(square(5))  # 25
print(cube(2))  # 8
print(square(10))  # 100