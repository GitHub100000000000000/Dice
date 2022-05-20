def on_button_pressed_ab():
    basic.show_number(randint(1, 6))
    basic.clear_screen()
    basic.show_leds("""
        # # # # #
                # # # # #
                # # # # #
                # # # # #
                # # # # #
    """)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_gesture_shake():
    pass
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
