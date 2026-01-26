import os


def get_width_high():
    width = int(input('Width : '))
    high = int(input('High  : '))

    return width, high


def calculate_up_scale(width, high):
    up_scale = int(input('\nUpscale : x'))

    up_width = width * up_scale
    up_high = high * up_scale

    return up_width, up_high


while True:
    os.system('cls')

    width, high = get_width_high()

    lock = input('Lock width and high? (y/n): ').strip().lower()

    if lock == 'y':
        attempt = 0
        while True:
            up_width, up_high = calculate_up_scale(width, high)
            print(f'{up_width} x {up_high}')
            attempt += 1

            if attempt == 10:
                again = input('Again? (y/n): ').strip().lower()
                if again != 'y':
                    break

    up_width, up_high = calculate_up_scale(width, high)
    print(f'{up_width} x {up_high}')

    again = input('Again? (y/n): ').strip().lower()
    if again != 'y':
        break
