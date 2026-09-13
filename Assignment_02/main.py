from rental import Vehicle, Renter, ElectricCar, Motorbike 

print("--- 1. Testing Vehicles and Renters ---")

v1 = Vehicle("Toyota", "Probox", "TO123")
print(f"\n{v1}")

r1 = Renter("John Doe", 123456) 
print(f"\nRenter: {r1.name}, License No: {r1.license_no}")

print("\n--- Renting ---")

v1.rent()                 
r1.rented.append(v1)       
print(f"\n{v1}")
print(f"{r1.name} currently has {len(r1.rented)} vehicle(s) rented.")


print("\n--- Returning ---")

v1.return_vehicle()        
r1.rented.remove(v1)       
print(f"\n{v1}")
print(f"{r1.name} currently has {len(r1.rented)} vehicle(s) rented.")

ec1 = ElectricCar("Tesla", "Cybertruck", "TES123", 75)
print(f"\n{ec1}")

mb1 = Motorbike("Honda", "2000", "HON123", 1200)
print(f"\n{mb1}")


print("\n--- 2. Testing Encapsulation (Catching Errors) ---")

try:
    bad_name_renter = Renter("", 12345)
except ValueError as e:
    print(f"Caught Error (Bad Name): {e}")

try:
    bad_license_renter = Renter("Alice", -50)
except ValueError as e:
    print(f"Caught Error (Bad License): {e}")


print("\n--- 3. Testing Polymorphism ---")

list1 = [v1, ec1, mb1]
ec1.rent()
for vehicle in list1:
    print(f"\n{vehicle}")
    
    
# print("\n--- 4. Testing Rent and Return ---")

# print(v1.rent())
# print(v1.rent())  #already rented
# print(v1.return_vehicle())

