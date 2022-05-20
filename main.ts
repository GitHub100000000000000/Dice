input.onButtonPressed(Button.AB, function () {
    basic.showNumber(randint(1, 6))
    basic.clearScreen()
    basic.showLeds(`
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        `)
})
