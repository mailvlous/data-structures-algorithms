class SecurityDevice:
    def __init__(self, active, location):
        self.active = active
        self.location = location
        
    def reset(self):
        print("Resetting device")
        self.active = True
        
class Sensor(SecurityDevice):
    def __init__(self, distance, resolution):
        self.distance = distance
        self.resolution = resolution

semsoor = Sensor(10, 20)

semsoor.reset()
print(semsoor.active)

print(type(semsoor))
print(isinstance(semsoor, Sensor))
print(isinstance(semsoor, SecurityDevice))
print(isinstance(SecurityDevice, Sensor))
print(issubclass(Sensor, SecurityDevice))