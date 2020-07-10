from inputs import get_gamepad

def main():
    reverse = False
    while 1:
        events = get_gamepad()
        for event in events:
            # event.ev_type, event.code, event.state

            # steering
            if event.code == 'ABS_Z':
                steering = event.state
                print('steering', steering)

            if event.code == 'BTN_PINKIE':
                if event.state == 1:
                    reverse = True
                if event.state == 0:
                    reverse = False


            # trottle
            if event.code == 'ABS_Y':
                trottle = -event.state if reverse else event.state
                print('trottle', trottle)

if __name__ == "__main__":
    main()