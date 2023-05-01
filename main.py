def on_button_pressed_a():
    global run, scount, soglia
    run = 0
    scount += 1
    soglia = soglia / scount
    basic.show_number(scount)
    basic.pause(2000)
    run = 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global run, scount, soglia
    run = 0
    scount += -1
    if scount < 1:
        scount = 1
    soglia = soglia * scount
    basic.show_number(scount)
    basic.pause(2000)
    run = 1
input.on_button_pressed(Button.B, on_button_pressed_b)

lp = 0
lr = 0
run = 0
scount = 0
soglia = 0
soglia = 0.1
scount = 1
run = 1

def on_forever():
    global lr, lp
    if run == 1:
        basic.clear_screen()
        lr = 0
        lp = 0
        for index in range(100):
            lr += input.rotation(Rotation.ROLL)
            lp += input.rotation(Rotation.PITCH)
        lr = lr / 100
        lp = lp / 100
        if abs(lp) < soglia and abs(lr) < soglia:
            basic.show_leds("""
                . . # . .
                                . . # . .
                                # # # # #
                                . . # . .
                                . . # . .
            """)
        else:
            if abs(Math.sqrt(lp * lp + lr * lr)) > soglia:
                led.plot(2.5 + 2 * (lr / Math.sqrt(lp * lp + lr * lr)),
                    2.5 + 2 * (lp / Math.sqrt(lp * lp + lr * lr)))
basic.forever(on_forever)
