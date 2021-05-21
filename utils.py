import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

mouth = kit.servo[0]
body = kit.servo[1]
left_arm = kit.servo[2]
right_arm = kit.servo[3]

# Set the minimum and maximum angles the servos can go
mouth.range = (5, 36)
body.range = (2, 178)
left_arm.range = (10, 178)
right_arm.range = (25, 140)

def init():
    """Initializes the angles with default pozition values

    When the robot arm is plugged for the first time,
    the initial values given as 2038. This will cause
    invalid variable errors if the init() function is not
    run first.
    
    Caution: If the robot arm is not at the predefined
    default position, this may cause the robot to position
    itself very fast and cause damage to the equipment
    if there is anythin on its way.
    """
    mouth.angle = 35
    body.angle = 106
    right_arm.angle = 20 
    left_arm.angle = 180 - right_arm.angle
    
def speed_to_sleep(speed):
    """Converts the speed value (0-100) to seconds for time.sleep() function"""
    return 0.1-(int(speed)/1000) if speed < 100 else 0.001

def exceeds_min(servo_obj):
    """Checks whether a given servo exceeds its predefined minimum"""
    return servo_obj.angle < servo_obj.range[0]

def exceeds_max(servo_obj):
    """Checks whether a given servo exceeds its predefined maximum"""
    return servo_obj.angle > servo_obj.range[1]
            
def open_():
      
    while True:
        if exceeds_min(mouth):
            break
        mouth.angle -= 1
        time.sleep(0.01)

def close_():
      
    while True:
        if exceeds_max(mouth):
            break
        mouth.angle += 1
        time.sleep(0.01)
       
def right_(degree, speed=100):
    
    sleep_time = speed_to_sleep(speed)

    while body.angle > degree:
        
        if exceeds_min(body):
            break
            
        body.angle -= 1
        
        time.sleep(sleep_time)

def left_(degree, speed=100):
    
    sleep_time = speed_to_sleep(speed)

    while body.angle < degree:
        
        if exceeds_max(body):
            break
            
        body.angle += 1
        
        time.sleep(sleep_time)
        
def backward_(degree, speed=100):
    
    sleep_time = speed_to_sleep(speed)
    
    while right_arm.angle > degree:
    
        # If the left arm is too down, first increase that by 2
        if right_arm.angle < 180 - left_arm.angle:
            left_arm.angle += 2
            
        elif exceeds_min(right_arm):
            break
        
        right_arm.angle -= 1
        
        time.sleep(sleep_time)
        
def forward_(degree, speed=100):
    
    sleep_time = speed_to_sleep(speed)
    
    while right_arm.angle < degree:
    
        if exceeds_max(right_arm):
            break

        right_arm.angle += 1
        
        time.sleep(sleep_time)
              
def down_(degree, speed=100):
    
    sleep_time = speed_to_sleep(speed)
    
    while left_arm.angle > degree:
        
        if (left_arm.angle < 180 - right_arm.angle
            or exceeds_min(left_arm)):
            break
        else:
            left_arm.angle -= 1
        
        time.sleep(sleep_time)
        
def up_(degree, speed=100):
    
    sleep_time = speed_to_sleep(speed)
    
    while left_arm.angle < degree:
        
        if exceeds_max(left_arm):
            break
        left_arm.angle += 1
        
        time.sleep(sleep_time)
        
def move_body_to(degree, speed=100):
    
    if body.angle > degree:
        right_(degree, speed)
    elif body.angle < degree:
        left_(degree, speed)
        
def move_arm_to(degree, speed=100):
    
    if right_arm.angle > degree:
        backward_(degree, speed)
    elif right_arm.angle < degree:
        forward_(degree, speed)
        
def move_head_to(degree, speed=100):
    
    if left_arm.angle > degree:
        down_(degree, speed)
    elif left_arm.angle < degree:
        up_(degree, speed)
        
def go_to_default_position():
    
    move_body_to(105)
    move_arm_to(0)
    move_head_to(0)
    close_()
        
def open_close():
    
    open_()
    time.sleep(0.5)
    close_()
        
def feed_the_cat():
    
    move_body_to(105)
    move_arm_to(140)
    move_head_to(0)
    open_close()
    move_head_to(180)
    move_body_to(0)
    open_close()
    move_body_to(105)

