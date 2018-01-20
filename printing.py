import sys, time, random

speed = 60
def slow_print(main, direction):
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
