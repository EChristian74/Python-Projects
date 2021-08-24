
# parent class of "Chair"
class Furniture:
    # attribute definitions
    ctype = "Seating"
    upholstery = "Cloth"
    framework = "Wood"
    joinery = "Mortise and Tenon"
    stain_resistant = True
    transport = "Delivery"

    def delivery(self):  # defines a method(function), gives access to child class of "Furniture"
        entry_transport = input("Furniture Transport: ")
        if (entry_transport == "Delivery", "Shipping"):  # if/else statement to establish shipping method
            print("A fee will be added to your invoice for delivery or shipping.  We encourage customer pick up for this item if cost is a concern.")
        else:
            print("A delivery fee will not be added to your bill.  Please call us at (806) 123-4567 to schedule a time to pick up your items.")
        return entry_transport  # statement inside the method(function) send the function's result back to the caller  
    
  
# child class instance of "ModelA"
class ModelA(Furniture):
    # attribute definitions
    name = "New Englander"
    sofa = "Sectional"
    configuration = "Bumper Chaise Sectional"
    base = "Platform"
    
    def delivery(self):  # defines a method(function), gives access to child class of "ModelA"
        entry_transport = input("Sectional Transport: ")
        if (entry_transport == "Delivery", "Pick-up"):  # if/else statement to establish shipping method
            print("Delivery and customer pick-up are not available for this item.  Our only method of delivery is shipping from our warehouse.")
        else:
            print("A delivery fee will not be added to your bill.")
        return entry_transport  # statement inside the method(function) send the function's result back to the caller  


        
# child class instance of "ModelB"
class ModelB(Furniture):
    # attribute definitions
    name = "Newport"
    chair = "Recliner"
    footrest = "Manual"
    base = "Swivel"

    def delivery(self):  # defines a method(function), gives access to child class of "ModelB"
        entry_transport = input("Recliner Transport: ")
        if (entry_transport == "Delivery", "Shipping"):  # if/else statement to establish shipping method
            print("Delivery and shipping are not available for this item.  This item must be picked up by the customer.")
        else:
            print("A delivery fee will not be added to your bill.")
        return entry_transport  # statement inside the method(function) send the function's result back to the caller  


   
if __name__ == "__main__":  #instantiates class objects
    furniture = Furniture()
    print(furniture.delivery())  # calls the delivery questionnaire for class of Furniture

    modelA = ModelA()
    print(modelA.delivery())  # calls the delivery questionnaire for class of ModelA

    modelB = ModelB()
    print(modelB.delivery())  # calls the delivery questionnaire for class of ModelB

        

