
# parent class of "Chair"
class Chair:
    # placeholders for attributes
    ctype = "Unknown"
    style = "Unknown"
    size = "Unknown"
    material = "Unknown"
    incline = "Unknown"
    joinery = "Unknown"
    seat = "Unknown"
    weatherproof = True

    def info(self):  # defines a method(function), gives access to parent class of "Chair"
        msg = "\nType: {}\nStyle: {}\nSize: {}\nMaterial: {}\nIncline: {}\nJoinery: {}\nSeat: {}\nWeatherproof: {}".format(self.ctype,self.style,self.size,self.material,self.incline,self.joinery,self.seat,self.weatherproof)
        return msg  # statement inside the method(function) send the function's result back to the caller  
    
    
# child class instance of "Model"
class Model(Chair):
    # attribute definitions
    ctype = "Indoor/Outdoor"
    style = "Rocker"
    size = "Full"
    material = "Cedar"
    incline = "Ergonomic"
    joinery = "Mortise and Tenon"
    seat = "Contoured"
    weatherproof = True

    def greeting(self):  # defines a method(function), gives access to child class of "Model"
         msg = "\nOur Rocking Chairs are designed for comfort, and built to last. Here are some of the features you won’t find in rocking chairs available at superstores."
         return msg  # statement inside the method(function) send the function's result back to the caller  


if __name__ == "__main__":  #instantiates class objects
    model = Model()
    print(model.info())  # calls the return msg for parent class of "Chair" and prints to the console
    print(model.greeting())  # calls the return msg for child class of "Model" and prints to the console
