from time import sleep
import RPi.GPIO as GPIO
 
GPIO.setmode(GPIO.BCM)#以BCM模式使用引脚
GPIO.setwarnings(False)# 去除GPIO警告
 
 
def setServoAngle(servo, angle):#此函数将角度转换为占空比
    pwm = GPIO.PWM(servo, 50)#设置pwm波为50Hz，也就是20ms一周期
    pwm.start(8)#启动pwm
    dutyCycle = angle / 18. + 3.#此公式由舵机调零推算得出（+3是偏移量）（占空比=%2.5+（目标角度/180°）*（%12.5-%2.5））
    pwm.ChangeDutyCycle(dutyCycle)#调整pwm占空比
    sleep(0.3)
    pwm.stop()#关闭pwm
 
 
if __name__ == '__main__':
    import sys
 
    servo = int(sys.argv[1])#外部输入参数
    GPIO.setup(servo, GPIO.OUT)#设置指定的引脚为输出模式
    setServoAngle(servo, int(sys.argv[2]))
    GPIO.cleanup()#清除引脚占用