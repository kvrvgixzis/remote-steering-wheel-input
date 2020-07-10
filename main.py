from inputs import get_gamepad


def main():
    while 1:
        events = get_gamepad()
        for event in events:
            # event.ev_type, event.code, event.state

            # rotate steering wheel (0..1)
            if event.code == 'ABS_Z':
                if event.state > 135 or event.state < 125:
                    rotate = round(event.state / 255, 2)
                    print('rotate', rotate)

            # gas / break (0..1 / -1)
            if event.code == 'ABS_Y':
                if event.state > 209 or event.state == 0:
                    gas = round((event.state - 208) / 47, 2) if event.state != 0 else -1
                    print('gas', gas)


if __name__ == "__main__":
    main()