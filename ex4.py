# 车辆数
cars = 100
# 车内空间（座位数）
space_in_a_car = 4.0
# 如果将该值设为整型，则计算所得的结果亦是整型
# space_in_a_car = 4
# 司机数
drivers = 30
# 乘客数
passengers = 90
# 没有被开走的车辆数
cars_not_driven = cars - drivers
# 被开走的车辆数
cars_driven = drivers
# 车辆可载总人数
carpool_capacity = cars_driven * space_in_a_car
# 车均乘客数
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")