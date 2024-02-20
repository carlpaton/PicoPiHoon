from machine import Pin
import random, time

dice1_led1 = Pin(0, Pin.OUT)
dice1_led2 = Pin(1, Pin.OUT)
dice1_led3 = Pin(5, Pin.OUT)
dice1_led4 = Pin(6, Pin.OUT)
dice1_led5 = Pin(9, Pin.OUT)
dice1_led6 = Pin(10, Pin.OUT)
dice1_led7 = Pin(14, Pin.OUT)

dice2_led1 = Pin(13, Pin.OUT)
dice2_led2 = Pin(28, Pin.OUT)
dice2_led3 = Pin(27, Pin.OUT)
dice2_led4 = Pin(21, Pin.OUT)
dice2_led5 = Pin(22, Pin.OUT)
dice2_led6 = Pin(16, Pin.OUT)
dice2_led7 = Pin(18, Pin.OUT)

button = Pin(3, Pin.IN, Pin.PULL_UP)

def all_led_off():
    dice1_led1.off()
    dice1_led2.off()
    dice1_led3.off()
    dice1_led4.off()
    dice1_led5.off()
    dice1_led6.off()
    dice1_led7.off()

    dice2_led1.off()
    dice2_led2.off()
    dice2_led3.off()
    dice2_led4.off()
    dice2_led5.off()
    dice2_led6.off()
    dice2_led7.off()

def roll_dice1():
    dice_tumbles = random.randint(1,20)
    dice1_value = 0

    while dice_tumbles >= 0:
        dice1_value = random.randint(1,6)
        dice_tumbles -= 1

    if dice1_value == 1:
       dice1_led4.on()
    elif dice1_value == 2:
       dice1_led1.on()
       dice1_led7.on()
    elif dice1_value == 3:
       dice1_led1.on()
       dice1_led7.on()
       dice1_led4.on()
    elif dice1_value == 4:
       dice1_led1.on()
       dice1_led3.on()
       dice1_led5.on()
       dice1_led7.on()
    elif dice1_value == 5:
       dice1_led1.on()
       dice1_led3.on()
       dice1_led4.on()
       dice1_led5.on()
       dice1_led7.on()
    else:
       dice1_led1.on()
       dice1_led2.on()
       dice1_led3.on()
       dice1_led5.on()
       dice1_led6.on()
       dice1_led7.on()

def roll_dice2():
    dice_tumbles = random.randint(1,20)
    dice2_value = 0

    while dice_tumbles >= 0:
        dice2_value = random.randint(1,6)
        dice_tumbles -= 1
 
    if dice2_value == 1:
       dice2_led4.on()
    elif dice2_value == 2:
       dice2_led1.on()
       dice2_led7.on()
    elif dice2_value == 3:
       dice2_led1.on()
       dice2_led7.on()
       dice2_led4.on()
    elif dice2_value == 4:
       dice2_led1.on()
       dice2_led3.on()
       dice2_led5.on()
       dice2_led7.on()
    elif dice2_value == 5:
       dice2_led1.on()
       dice2_led3.on()
       dice2_led4.on()
       dice2_led5.on()
       dice2_led7.on()
    else:
       dice2_led1.on()
       dice2_led2.on()
       dice2_led3.on()
       dice2_led5.on()
       dice2_led6.on()
       dice2_led7.on()

def show_loading():
    dice1_led2.on()
    time.sleep(0.05)
    dice1_led2.toggle()
    dice1_led4.on()
    time.sleep(0.05)
    dice1_led4.toggle()
    dice1_led6.on()
    time.sleep(0.05)
    dice1_led6.toggle()
    dice2_led2.on()
    time.sleep(0.05)
    dice2_led2.toggle()
    dice2_led4.on()
    time.sleep(0.05)
    dice2_led4.toggle()
    dice2_led6.on()
    time.sleep(0.05)
    dice2_led6.toggle()

while True:
    if not button.value():
        all_led_off()
        time.sleep(0.2)
        show_loading()
        roll_dice1()
        roll_dice2()
        time.sleep(2)