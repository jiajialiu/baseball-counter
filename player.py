#!/usr/bin/python
class Player:
    
    def __init__(self, name):
        self.name=name
        self.bats=0
        self.hits=0
        self.bat_average=0;

    def set_batting_average(self):
        self.bat_average = round(float(self.hits)/self.bats,3)
        
    def get_average(self):
        return self.bat_average

