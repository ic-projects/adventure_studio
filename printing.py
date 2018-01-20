import sys, time, random

def slow_print(main, direction):
    speed = 60
    for l in main:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random() *10.0/speed)
    print ('') #newline
    for l in direction:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.03)
    print ('')

def print_at_speed(text, speed):
    for l in text:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random() *10.0/speed)
    print ('') #newline