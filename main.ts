input.onButtonPressed(Button.A, function () {
    run = 0
    scount += 1
    soglia = soglia / scount
    basic.showNumber(scount)
    basic.pause(2000)
    run = 1
})
input.onButtonPressed(Button.B, function () {
    run = 0
    scount += -1
    if (scount < 1) {
        scount = 1
    }
    soglia = soglia * scount
    basic.showNumber(scount)
    basic.pause(2000)
    run = 1
})
let lp = 0
let lr = 0
let run = 0
let scount = 0
let soglia = 0
soglia = 0.1
scount = 1
run = 1
basic.forever(function () {
    if (run == 1) {
        basic.clearScreen()
        lr = 0
        lp = 0
        for (let index = 0; index < 100; index++) {
            lr += input.rotation(Rotation.Roll)
            lp += input.rotation(Rotation.Pitch)
        }
        lr = lr / 100
        lp = lp / 100
        if (Math.abs(lp) < soglia && Math.abs(lr) < soglia) {
            basic.showLeds(`
                . . # . .
                . . # . .
                # # # # #
                . . # . .
                . . # . .
                `)
        } else if (Math.abs(Math.sqrt(lp * lp + lr * lr)) > soglia) {
            led.plot(2.5 + 2 * (lr / Math.sqrt(lp * lp + lr * lr)), 2.5 + 2 * (lp / Math.sqrt(lp * lp + lr * lr)))
        }
    }
})
