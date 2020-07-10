from inputs import get_gamepad


def main():
    while 1:
        events = get_gamepad()
        for event in events:
            # event.ev_type, event.code, event.state

            # rotate steering wheel
            if event.code == 'ABS_Z':
                if event.state > 135 or event.state < 125:
                    rotate = round(event.state / 255, 2)
                    print('rotate', rotate)

            # gas
            if event.code == 'ABS_Y':
                if event.state > 209:
                    gas = round((event.state - 208) / 47, 2)
                    print('gas', gas)


if __name__ == "__main__":
    main()