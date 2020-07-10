from inputs import get_gamepad
from numpy import clip
import time

from message import Message, MessageSerializer
from server import SocketServer

def convert_to_0_255(s):
    mn = 208
    mx = 255
    x = (s - mn) / (mx - mn) * 255
    x = clip([x], 0, 255)[0]
    return int(x)

def main():
    reverse = False
    throttle = 0
    steering = 0
    while True:
        events = get_gamepad()
        
        for event in events: # event.ev_type, event.code, event.state
            # steering
            if event.code == 'ABS_Z':
                steering = clip([event.state], 0, 254)[0]
                # print(steering)

            # check reverse
            if event.code == 'BTN_PINKIE':
                reverse = event.state
                # print(reverse)

            # trottle
            if event.code == 'ABS_Y':
                throttle = convert_to_0_255(event.state)
                throttle = -throttle if reverse else throttle
                throttle = clip([throttle], 0, 254)[0]
                # print(throttle)

            message = Message(throttle=throttle,
                            steering=steering,
                            reverse=reverse)
            ss.send(msg=message)


if __name__ == "__main__":
    ss = SocketServer(host='0.0.0.0', port=5000)
    ss.start()
    main()