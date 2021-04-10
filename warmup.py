# Another file with PYTHON exercises to practice

# Exercise 1.- Write the code to take a string and produce a dictionary out of that string such that the output looks like the following: Some thoughts

truck = "toyota tacoma"
sedan = "hyundai sonata"
sports_car = "lambourgini diablo"

make_and_model = truck.split()
make = make_and_model[0]
model = make_and_model[1]
#print(make_and_model)
cars = {}
cars["make"] = [make]
cars["model"] = [model]
#print(cars)

# Exercise 2.- Write the code that takes a dictionary containing make/model for a vehicle and capitalizes the first character of the make and the model

cars.update({"make": make.capitalize(), "model": model.capitalize()})
#print(cars)

# Exercise 3.- Create a list of 3 dictionaries where each dictionary represents a vehicle,
# as above Write the code that operates on that list of dictionaries in order to uppercase the entire make and model values

make = []
model = []
  
truck = {

    "Make": "Toyota",
    "Model": "Tacoma"
    }
sedan = {
    "Make": "hiunday",
    "Model": "sonata"
    }

sports_car = {
    "Make": "lambourgini",
    "Model": "diablo"
    }

# car_catalogue = [truck, sedan, sports_car]
#car_catalogue[1]["Make"]

for k in truck.keys():
    truck[k.upper()] = truck[k]

print(truck)
# car_catalogue.keys()

#make = car_catalogue[0, "make"]
#model = car_catalogue["model"]
#for car in car_catalogue:


#print(car_catalogue)
#print(make)
#for car in cars:
#    [truck.update({"make": make.upper(), "model": model.upper()}), sedan.update({"make": make.upper(), "model": model.upper()}), sports_car.upper({"make": make.upper(), "model": model.upper()})]


#cars = [truck, sedan, sports_car]
#for car in cars:

#   car.update({"make": make.upper(), "model": model.upper()})

#print(cars)
