from inputs import get_gamepad
from numpy import clip

def convert_to_0_255(s):
    mn = 208
    mx = 255
    x = (s - mn) / (mx - mn) * 255
    x = clip([x], 0, 255)[0]
    return int(x)

def main():
    reverse = False
    while 1:
        events = get_gamepad()
        for event in events: # event.ev_type, event.code, event.state
            # steering
            if event.code == 'ABS_Z':
                steering = event.state
                print('steering', steering)

            # check reverse
            if event.code == 'BTN_PINKIE':
                reverse = event.state

            # trottle
            if event.code == 'ABS_Y':
                trottle = convert_to_0_255(event.state)
                trottle = -trottle if reverse else trottle
                print('trottle', trottle)


if __name__ == "__main__":
    main()