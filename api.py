import status 
from datetime import date 
from tornado import web, escape, ioloop, httpclient, gen 
from drone import Altimer, Drone , Hexacopter, LightEmittingDiode

drone = Drone()

class HexacopterHandler(web.RequestHandler):
    SUPPORTED_METHODS = ("GET", "PATCH")
    HEXACOPTER_ID = 1

    def get(self,id):
        if int(id) is not self.__class__.HEXACOPTER_ID:
            self.set_status(status.HTTP_404_NOT_FOUND)
            return 
        print("I've started retrieving hexacopter's status")
        hexacopter_status = drone.hexacopter.get_hexacopter_status()
        print("I've finished retrieving hexacopter's status")
        response = {
            'speed': hexacopter_status.motor_speed,
            'turned_on': hexacopter_status.turned_on
        }
        self.set_status(status.HTTP_200_O
        # Tornado automatically writes the chunk in json 
        self.write(response)

    def patch(self,id):
        if int(id) is not self.__class__.HEXACOPTER_ID:
            self.set_status(status.HTTP_404_NOT_FOUND)

