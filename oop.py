
from enum import Enum

class Position:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def log(self):
        print(f"x: {self.x}, y: {self.y}, z: {self.z}")

class Camera:
    def __init__(self, serial_number, position, camera_type):
        self.serial_number = serial_number
        self.position = position
        self.camera_type = camera_type
        
    def log(self):
        self.position.log()
        print(f"Serial Number: {self.serial_number}, Camera Type: {self.camera_type}")
        
    class CameraType(Enum):
        PTZ = 1
        FIXED = 2
        THERMAL = 3

c = Camera(12345, Position(1, 2, 3), Camera.CameraType.PTZ)
c.log()