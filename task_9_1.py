import time


class TrafficLight:
    __color = {'RED': 7, 'YELLOW': 2, 'GREEN': 5}

    def running(self):
        for col in self.__color:
            print(col)
            time.sleep(self.__color.get(col))


a = TrafficLight()
a.running()
