#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "Holberton"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
model_json = my_model.to_dict()
print(model_json)
print("JSON of my_model:")
for k in model_json.keys():
    print("\t{}: ({}) - {}".format(k, type(model_json[k]), model_json[k]))
