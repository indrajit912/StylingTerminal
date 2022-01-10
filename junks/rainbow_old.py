import requests, pprint
from junks.sorted_rgb import COLOR_RGB
from rgb import COLORS
from bs4 import BeautifulSoup
from main import convert_rgb_values_to_ANSI_escape_code


# def get_color_names_accor_to_shades():

#     url = "https://www.rapidtables.com/web/color/RGB_Color.html#color-table"
#     res = requests.get(url)
#     res.raise_for_status()

#     soup = BeautifulSoup(res.text, "html.parser")
    

#     pprint.pprint(soup.text)


def preview_shades_of_colors():

    color_name = "orangered"
    color_rgb_value = COLOR_RGB[color_name]

    print(f"\t{color_rgb_value} \t\t {color_name}")


def get_colors():

    ls = []

    with open("test.txt", "r") as f:
        for line in f:
            ls.append(line.rstrip())

    color_dict = {}

    for n in range(len(ls)):
        try:
            color_name = ls[6 * n][1:-3].strip()
            # print(color_name)
            rgb_val = ls[6 * n + 2][1:-3]
            # print(rgb_val)
            color_hex = ls[6 * n + 1][1:-3]
            # print(color_hex)
            color_dict.setdefault(color_name, {"hex_code":color_hex, "rgb":rgb_val})
        except IndexError:
            pass

    print(color_dict)
    # for color, v in color_dict.items():
    #     print(color)
    #     print(v)
    #     print()
    #     print()


def convert_str_into_rgb_tuple(str_rgb):
    """
    Accepts a str : '(234,123,0)'
    Returns a tuple of int: (234, 123, 0)
    """
    converted = tuple([int(x) for x in str_rgb[1:-1].split(',')])
    
    return converted


def preview_color_rainbow():

    ITALLIC = '\033[3m'
    END = '\033[0m'

    print("\n\n")

    for color_name, color_val in COLORS.items():
        color_rgb = convert_rgb_values_to_ANSI_escape_code(color_val['rgb'], 'bg')
        print(f"\t{color_rgb}                            {END}\t{ITALLIC}{color_name + END}\n\t      {color_val['rgb']}")
        print()

    print("\n\n")


def main():

    # The following things make ANSI works on different platforms too!
    PLATFORMS = {
        "linux": ['linux'],
        "windows": ['win32', 'cygwin', 'msys'],
        "mac": ['darwin']
    }

    import sys
    if sys.platform in PLATFORMS['windows']: # To make ANSI works on windows system
        import os
        os.system("color")
    
    preview_color_rainbow()


if __name__ == '__main__':
    main()