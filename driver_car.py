from Car import Car
speed =0;
started = 'True'
mycar = Car(speed, started)

#Accelerate 5 times
if(mycar._started == 'True'):
    mycar.accelerate()
    print('The current speed is: ', mycar.get_speed)
    mycar.accelerate()
    print('The current speed is: ', mycar.get_speed)
    mycar.accelerate()
    print('The current speed is: ', mycar.get_speed)
    mycar.accelerate()
    print('The current speed is: ', mycar.get_speed)
    mycar.accelerate()
    print('The current speed is: ', mycar.get_speed)

car1 = Car("10", True)
print(car1.is_started())