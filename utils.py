import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

mouth = kit.servo[0]
body = kit.servo[1]
left_arm = kit.servo[2]
right_arm = kit.servo[3]

def move(direction, degree, speed=100):
    
    sleep_time = 0.1-(int(speed)/1000) if speed < 100 else 0.001

    for i in range(degree):
        
        if direction.lower() in ['right', 'r']:
            if body.angle < 2:
                print("This is the most right I can go")
                break
            else:
                body.angle -= 1
            
        if direction.lower() in ['left', 'l']:
        
            if body.angle > 178:
                print("This is the most left I can go")
                break
            else:
                body.angle += 1
                
        if direction.lower() in ['up', 'u']:
        
            if left_arm.angle > 178:
                print("This is the most up I can go")
                break
            else:
                left_arm.angle += 1
        
        if direction.lower() in ['down', 'd']:
            if left_arm.angle < 10:
                print("This is the most down I can go")
                break
            else:
                left_arm.angle -= 1
        
        if direction.lower() in ['back', 'b']:
            if right_arm.angle < 10:
                print("This is the most backward I can go")
                break
            else:
                right_arm.angle -= 1
            
        if direction.lower() in ['forward', 'f']:
        
            if right_arm.angle > 178:
                print("This is the most forward I can go")
                break
            else:
                right_arm.angle += 1
   
        time.sleep(sleep_time)
        
def close_mouth():
      
    while True:
        if mouth.angle > 36:
            print('Mouth closed')
            break
        mouth.angle += 1
        time.sleep(0.01)
        
def open_mouth():
      
    while True:
        if mouth.angle < 5:
            print('Mouth open')
            break
        mouth.angle -= 1
        time.sleep(0.01)

def open_close():
    
    open_mouth()
    time.sleep(0.5)
    close_mouth()
        
def take_up(degree):
    
    open_close()
    move('u', degree)
    move('b', int(degree/2))
    open_close()
    
def get_down(degree):
    
    move('f', degree)
    move('d', int(degree/2))
    
def default_position():
    
    move('u', 1000, 100)
    move('b', 1000, 100)
    
    while True:
        if int(body.angle) == 105:
            break
        
        if body.angle < 105:
            body.angle += 1
        else:
            body.angle -= 1
            
        time.sleep(0.01)

