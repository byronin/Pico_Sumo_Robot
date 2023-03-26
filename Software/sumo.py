from machine import Pin , PWM
import time
# define the GPIO pins to which the device sensor outputs are connected
sensor1 = Pin(4, Pin.IN)
sensor2 = Pin(5, Pin.IN)
# Define pins and frequency for PWM (Pulse Width Modulation)
PWM_A1 = PWM(Pin(16))
PWM_A2 = PWM(Pin(18))
PWM_B1 = PWM(Pin(17))
PWM_B2 = PWM(Pin(19))
PWM_FREQ = 1000
PWM_A1.freq(PWM_FREQ)
PWM_B1.freq(PWM_FREQ)
PWM_A2.freq(PWM_FREQ)
PWM_B2.freq(PWM_FREQ)

def move_motor(motor, speed):
    """
    Move the motor in the specified direction and speed.
    :param motor: motor identifier (string) "A" or "B"
    :param speed: motor speed, range -100 to 100
    """
    # If motor A is selected
    if motor == "A":
        # If speed is positive, set PWM_A1 duty cycle and PWM_A2 duty cycle to 0
        if speed > 0:
            PWM_A1.duty_u16(int((speed / 100) * 65535))
            PWM_A2.duty_u16(0)
        # If speed is negative, set PWM_A1 duty cycle to 0 and PWM_A2 duty cycle to speed
        elif speed < 0:
            speed = abs(speed)
            PWM_A1.duty_u16(0)
            PWM_A2.duty_u16(int((speed / 100) * 65535))
        # If speed is 0, set both PWM_A1 and PWM_A2 duty cycle to 0
        else:
            PWM_A1.duty_u16(0)
            PWM_A2.duty_u16(0)
            speed = 0
    # If motor B is selected
    elif motor == "B":
        # If speed is positive, set PWM_B1 duty cycle and PWM_B2 duty cycle to 0
        if speed > 0:
            PWM_B1.duty_u16(int((speed / 100) * 65535))
            PWM_B2.duty_u16(0)
        # If speed is negative, set PWM_B1 duty cycle to 0 and PWM_B2 duty cycle to speed
        elif speed < 0:
            speed = abs(speed)
            PWM_B1.duty_u16(0)
            PWM_B2.duty_u16(int((speed / 100) * 65535))
        # If speed is 0, set both PWM_B1 and PWM_B2 duty cycle to 0
        else:
            PWM_B1.duty_u16(0)
            PWM_B2.duty_u16(0)
            speed = 0
turn = 1
move_motor("A", 40)
move_motor("B", 40)
time.sleep(2)
while True:
    # read sensor values
    sensor1_value = sensor1.value()
    sensor2_value = sensor2.value()
    
    # controlling motors according to sensor values
    if sensor1_value == 0 and sensor2_value == 1:
        move_motor("A", 50)
        move_motor("B", 30)
        time.sleep(0.1)
        turn = 1
    elif sensor1_value == 1 and sensor2_value == 0:
        move_motor("A", 30)
        move_motor("B", 50)
        time.sleep(0.1)
        turn = 2
    elif sensor1_value == 0 and sensor2_value == 0:
        move_motor("A", 80)
        move_motor("B", 80)
        time.sleep(0.1)
    else:  
        if turn == 2:
            move_motor("A", -40)
            move_motor("B", 40)
            time.sleep(0.1)
        elif turn == 1:
            move_motor("A", 40)
            move_motor("B", -40)
            time.sleep(0.1)
    
    # a short cooldown
    time.sleep(0.1)