#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

m1 = Motor(Port.B)
#m2 = Motor(Port.C)

def rotate(a):  #입력된 각도 a 만큼 회전
    p = 80      #모터 파워(p) 설정
    m1.run_angle(p,a,Stop.BRAKE,True)  #m1 모터를 a도 만큼 p의 속도로 회전 
    #m2.run_angle(p,a,Stop.BRAKE,True)   #m2 모터를 a도 만큼 p의 속도로 회전 ,BRAKE 방식으로 정지 (True : 모터의 동작이 끝날 때 까지 대기)


cp = 1 #current position 현재 위치 설정

def rtp(t): #rotate to position, t: target #타겟의 위치로 회전

    global cp

    angle = (t - cp) * 90 #현재 위치와 타겟의 위치 계산
    
    Motor(Port.B).run_angle(50,angle,Stop.BRAKE,True)

    cp = t #현재 위치 업데이트


# Write your program here.

ev3.speaker.beep()  #비프음 재생


while 1:
    ev3.screen.print(cp)
    if Button.UP in ev3.buttons.pressed():
        rotate(90)
        cp = cp + 1
        if cp == 5:
            cp = 1

    if Button.DOWN in ev3.buttons.pressed():
        rotate(-90)
        cp = cp - 1
        if cp == 0:
            cp = 4


    while Button.CENTER in ev3.buttons.pressed(): #CENTER 버튼을 누르는 동안
    
        if Button.UP in ev3.buttons.pressed():    #UP 버튼이 눌리면
            rtp(1)  # 1번째 위치로 이동
        
        if Button.LEFT in ev3.buttons.pressed():  #LEFT 버튼이 눌리면
            rtp(2)  # 2번째 위치로 이동
        
        if Button.RIGHT in ev3.buttons.pressed(): #RIGHT 버튼이 눌리면
            rtp(3)  # 3번째 위치로 이동
        
        if Button.DOWN in ev3.buttons.pressed():  #DOWN 버튼이 눌리면
            rtp(4)  # 4번째 위치로 이동
    
        wait(200) #0.2초 대기