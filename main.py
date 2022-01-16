# Text styling in terminal
#
# Author: Indrajit Ghosh
#
# Date: Dec 13, 2021
#
#   URL: "https://en.wikipedia.org/wiki/ANSI_escape_code"
#   RGB: "https://www.rapidtables.com/web/color/RGB_Color.html#color-table"
#   STACK_OVERFLOW: "https://stackoverflow.com/questions/8924173/how-do-i-print-bold-text-in-python"
#   REPO: "https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html"
#

import matplotlib, pprint
from fg_colors import FG_COLORS
from bg_colors import BG_COLORS
from terminal_style import IndraStyle
from rgb import COLORS


def generate_rgb():
    rgb_colors = {}
    for name, hex in matplotlib.colors.cnames.items():
        rgb = matplotlib.colors.to_rgb(hex)
        # rgb = tuple(rgb)
        # print(type(rgb[0]))
        rgb_colors[name] = (int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255))
        
    return rgb_colors


def convert_rgb_values_to_ANSI_escape_code(color_rgb_value, fg_or_bg='fg'):
    """
        'fg' : foreground 
        'bg' : background
    """

    fg_or_bg = 38 if fg_or_bg == 'fg' else 48
    r, g, b = color_rgb_value

    ansi_code_for_rgb = '\033[{0};2;{1};{2};{3}m'.format(fg_or_bg, r, g, b)

    return ansi_code_for_rgb


def write_my_class():
    """
    Function that writes the class 'IndraStyle' on behalf of Indrajit!
    """

    descriptions = '''
    """
    Class that provides various styles (based on ANSI escape codes)
    to the terminal.

    Author: Indrajit Ghosh
    Date: Dec 16, 2021
    
        USAGES:
        1.
            >>> import IndraStyle
            >>> print(f"{IndraStyle.BLINK + IndraStyle.CRIMSON}Hello World!{IndraStyle.END}")

        2.
            To change the 'background' color use the following:
            >>> print(f"{IndraStyle.BG_RED + Hello World!{IndraStyle.END}")

        CAUTION:
            If you are using 'windows' make sure to include the following lines
            at the top of your code:

                # The following things make ANSI works on different platforms too!
                 PLATFORMS = {
                     "linux": ['linux'],
                     "windows": ['win32', 'cygwin', 'msys'],
                     "mac": ['darwin']
                }

                import sys
                if sys.platform in PLATFORMS['windows']: # To make ANSI work on windows system
                    import os
                    os.system("color")
                ##########  xxx  ##########

    """
    '''
    
    with open("updated_class.py", "w") as f:

        f.write("class Style:\n")
        f.write(descriptions)

        f.write("\n\n")


        f.write(r"    # Foreground Colors")
        f.write('\n')
        for color_name, val in COLORS.items():
            color_name = color_name.replace(' ', '_').upper()
            ansi_code = convert_rgb_values_to_ANSI_escape_code(val['rgb'])
            to_save = pprint.pformat(ansi_code)
            f.write("    " + color_name + " = " + to_save)
            f.write('\n')
        

        f.write("\n\n")
        f.write(r"    # Background Colors")
        f.write('\n')
        for color_name, val in COLORS.items():
            color_name = color_name.replace(' ', '_').upper()
            ansi_code = convert_rgb_values_to_ANSI_escape_code(val['rgb'], 'bg')
            to_save = pprint.pformat(ansi_code)
            f.write("    " + color_name + "_BG" + " = " + to_save)
            f.write('\n')


def preview_all_colors():

    for color_name, color in BG_COLORS.items():
        print(f"    {color}                 {IndraStyle.END}{IndraStyle.ITALLIC}   {color_name}{IndraStyle.END}")
        print()


def get_color_name_from_rgb(rgb_val):

    for color_name, val in COLORS.items():
        if rgb_val == val['rgb']:
            return color_name
    return 'unknown'


def generate_color_output_from_rgb(rgb_value:tuple):
    """
    Accepts: tuple of int
    Prints: the corresponding color output on the terminal
    """
    color_name = get_color_name_from_rgb(rgb_value)
    color_ansi = convert_rgb_values_to_ANSI_escape_code(rgb_value, 'bg')

    output = f"""
        {color_ansi}                     {IndraStyle.END}
        {color_ansi}                     {IndraStyle.END}       {IndraStyle.ITALLIC + IndraStyle.WHITE + color_name + IndraStyle.END}
        {color_ansi}                     {IndraStyle.END}\n\t   {rgb_value}
    """

    print(output)



def generate_color_output(rgb_or_listOfRgb_or_colorName):
    """
    Accepts: tuple or list or str
    Prints: color output(s) on the terminal
    """
    if isinstance(rgb_or_listOfRgb_or_colorName, tuple):
        generate_color_output_from_rgb(rgb_or_listOfRgb_or_colorName)
    elif isinstance(rgb_or_listOfRgb_or_colorName, str):
        if rgb_or_listOfRgb_or_colorName.startswith('#'):
            not_found = True
            for k, v in COLORS.items():
                if v['hex_code'] == rgb_or_listOfRgb_or_colorName:
                    generate_color_output_from_rgb(v['rgb'])
                    not_found = False
                    break
            if not_found:
                print(f"The hex code is not in the database!\n")
            
        else:
            if rgb_or_listOfRgb_or_colorName in COLORS.keys():
                rgb = COLORS[rgb_or_listOfRgb_or_colorName]['rgb']
                generate_color_output_from_rgb(rgb)

            else:
                print(f" Sorry, '{rgb_or_listOfRgb_or_colorName}' is not in our database!\n")
    else:
        try:
            for rgb in rgb_or_listOfRgb_or_colorName:
                generate_color_output_from_rgb(rgb)
        except TypeError:
            print(" Sorry, that didn't work!")


def colored_number_output(fg_or_bg='fg'):
    n = 38 if fg_or_bg == 'fg' else 48
    for i in range(16):
        for j in range(16):
            code = str(16 * i + j)
            print(f"\033[{n};5;{code}m {code.ljust(4)}", end='')
        print(IndraStyle.END)


def isi_address():
    isi_address = f"""
    {IndraStyle.HOT_PINK + IndraStyle.BOLD}Indrajit{IndraStyle.END} Ghosh.

    {IndraStyle.ITALLIC}Research Scholar{IndraStyle.END}; Stat-Math Unit,
    {IndraStyle.LAVENDER}Indian Statistical Institute Bangalore{IndraStyle.END},
    {IndraStyle.BURLY_WOOD}Email:{IndraStyle.END}{IndraStyle.ITALLIC}rs_math1902@isibang.ac.in{IndraStyle.END}
    
    8{IndraStyle.SUPERSCRIPT}th{IndraStyle.END} Mile, Mysore Road. RVCE Post.
    Bengaluru - {IndraStyle.KHAKI + IndraStyle.BOLD}560059{IndraStyle.END},
    India.
    """

    print(" "*3 + IndraStyle.GRINNING_FACE_WITH_SMILING_EYES)

    print(isi_address)


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

    RGB_DATASET = [
        (255, 0, 0),
        (0, 255, 0),
        (0, 0, 255),
        (240, 255, 255),
        (245, 255, 250),
        (218, 112, 214),
        (255, 78, 81),
        (135, 206, 235),
        (154, 205, 50),
    ]


    generate_color_output('#BDA589') # Change the argument of this function
    # colored_number_output()
    # isi_address()



if __name__ == '__main__':
    main()

 