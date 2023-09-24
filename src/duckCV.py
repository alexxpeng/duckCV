import sensor, image, time, os, tf, pyb, math, utime, gc, uos

redLED = pyb.LED(1)
greenLED = pyb.LED(2)
blueLED = pyb.LED (3)

sensor.reset()                         # Reset and initialize the sensor.
sensor.set_pixformat(sensor.RGB565)    # Set pixel format to RGB565 (or GRAYSCALE)
sensor.set_framesize(sensor.QVGA)      # Set frame size to QVGA (320x240)
sensor.set_vflip(True)
sensor.set_hmirror(True)
sensor.set_windowing((240, 240))       # Set 240x240 window.
sensor.skip_frames(time=2000)          # Let the camera adjust for 2 sec.

#custom firmware flashed on nicla vision with custom model made with edge impulse
labels, net = tf.load_builtin_model("duckrec")

clock = time.clock()

#loop indefinitely checking for ducks in image
while (True):
    clock.tick()
    img = sensor.snapshot()
    for i, detection_list in enumerate(net.detect(img)):
        #checking correct object and background detection
        #print("%s" % labels[i])
        for d in detection_list:
            [x,y,w,h] = d.rect();
            center_x = math.floor(x+(w/2));
            center_y = math.floor(y+(h/2));
            if labels[i] == "duck" :
                img.draw_circle(center_x, center_y, 20, (108,52,131), 6,0)
                print("======================")
                print("=====Duck Found:)=====")
                print("======================")
                print("======================")
                blueLED.on()
            else: blueLED.off()

    print(clock.fps(), "fps")
    print("======================")
