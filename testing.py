#!/usr/bin/python3
class BaseModel:
    def __init__(self, count):
        self.new = 4
        self.numeros = count
model = BaseModel(56)

print("[{} {}".format(model.new, (model.numeros)))
