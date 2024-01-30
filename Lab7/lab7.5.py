import RPi.GPIO as GPIO
import time
import drivers

display = drivers.Lcd()
display.lcd_clear()

SW1 = 14
SW2 = 15

text = \
["LAB 7"," LAB 7","  LAB 7","   LAB 7","    LAB 7","     LAB 7","      LAB 7",\
"       LAB 7","        LAB 7","         LAB 7","          LAB 7","           LAB 7"]

GPIO.setmode(GPIO.BCM)
GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SW2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(SW1, GPIO.FALLING)
GPIO.add_event_detect(SW2, GPIO.FALLING)

num = 5

try:
    while True:
        if GPIO.event_detected(SW1):
            display.lcd_clear()
            num += 1
            if num > 11:
                num = 11
            display.lcd_display_string(text[num], 1)
        elif GPIO.event_detected(SW2):
            display.lcd_clear()
            num -= 1
            if num < 0:
                num = 0
            display.lcd_display_string(text[num], 1)
        time.sleep(0.5)

except KeyboardInterrupt:
    GPIO.remove_event_detect(SW1)
    GPIO.remove_event_detect(SW2)
    GPIO.cleanup()

    display.lcd_clear()
    print("\nBye...")
