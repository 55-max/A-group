from buildhat import Motor
motor_a = Motor('A')
motor_a.run_for_seconds(10, speed=-10)


from buildhat import Motor

class lego_motor:
    def __init__(self, port):
        self.port = port
        self.motor = Motor(self.port)
        self.dc = 0.0

    def set_dc(self, dc):
        self.dc = dc
        self.motor.run_for_seconds(0.4, speed=dc)
        self.motor.stop()

    def get_dc(self):
        return self.dc
    
    def run(self):
        self.motor.run_for_seconds(10, speed=4)
    
if __name__ == '__main__':
    motor = lego_motor('D')
    motor.run()
