#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      aarna
#
# Created:     12/10/2022
# Copyright:   (c) aarna 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Livingbeings:
    property="breathing"
    def shownature(self):
        print("All biological processes occuring")

class Animal(Livingbeings):
    habitat="forest"
    def nature(self):
        print("lives in",(self.habitat))

class Herbivores(Animal):
    type="plant eating"
    def giveexamples(self):
        print("cow,horse,rabbit")


class Carnivores(Animal):
    type="animal eating"
    def givexample(self):
        print("lion,tiger,wolf")


class Mammals(Herbivores,Carnivores):
    characteristic="warm blooded"
    def showproperty(self):
        print("Give birth to babies")
        print("They are",(self.characteristic))
l=Livingbeings()
a=Animal()
h=Herbivores()
c=Carnivores()
m=Mammals()
print(m.habitat)
h.giveexamples()
m.nature()
c.shownature()
print(c.property)




