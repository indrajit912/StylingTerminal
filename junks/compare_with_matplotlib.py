from rgb import COLORS


def preview_color_info():
    for color_name, val in COLORS.items():
        color_hex = val['hex_code']
        color_rgb = val['rgb']
        print(f" - {color_name.ljust(25)}\t\t{color_hex.ljust(8)}\t{color_rgb}")
        print()


def main():

    preview_color_info()


if __name__ == '__main__':
    main()
    