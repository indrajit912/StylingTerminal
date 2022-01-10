# Color RGB values
#
# Author: Indrajit Ghosh
#
# Date: Dec 14, 2021
#


from rgb import COLORS
from main import convert_rgb_values_to_ANSI_escape_code


def preview_color_rainbow():
    
    ITALLIC = '\033[3m'
    END = '\033[0m'

    print("\n\n")

    for color_name, color_val in COLORS.items():
        color_rgb = convert_rgb_values_to_ANSI_escape_code(color_val['rgb'], 'bg')
        output = f"""
        {color_rgb}                           {END}
        {color_rgb}                           {END}       {ITALLIC + color_name + END}
        {color_rgb}                           {END}\n\t      {color_val['rgb']}
    """
        print(output)
    

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