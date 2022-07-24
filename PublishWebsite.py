import sys
import glob
from tkinter import SOLID
from colorama import Fore, Back, Style
import os
import time

def specifics():
    debugger = 0
    backup_en = 0
    nicepage_foot_rem = 1
    color_change = 0
    git_push = 0
    custom_commit = "\"Remove footer - add python to new repo\""
    return debugger, backup_en, nicepage_foot_rem, color_change, git_push, custom_commit

def main():
    debugger, backup_en, nicepage_foot_rem, color_change, git_push, custom_commit = specifics()
    # Adding this comment to test github correctness
    print("\nFinding all website source HTML files...")

    # Need to modify for any programs requiring html files
    if nicepage_foot_rem:
        list_html = source_html(debugger)

    # Need to modify for any programs requiring css files
    if color_change:
        list_css = source_css(debugger)
        if (backup_en == 0):
            warning("Experimental portion - creating backup without user consent...")
            backup_en = 1

    if backup_en:
        create_backup(debugger)
    
    if nicepage_foot_rem:
        print("\nRemoving all Nicepage html generation...")
        nicepage_footer_locator(list_html, debugger)

    if color_change:
        color_match(list_css, debugger)

    if git_push:
        github_exec(debugger, custom_commit)

    return

def warning(in_string):
    print(Fore.RED + in_string + Style.RESET_ALL)
    return

def success(in_string):
    print(Fore.GREEN + in_string + Style.RESET_ALL)
    return

def create_backup(debugger):
    if debugger:
        print("Creating backup...")
    local_storage = '~/Documents/Website/crsourceweb'
    backup_location = '~/Documents/Website/backup'
    # folderExist = os.path.isfile(backup_location)
    # if (folderExist):
    #     warning("Backup does not already exist, generating backup...")
    backup_string = 'cp -R ' + local_storage + ' ' + backup_location
    os.system(backup_string)
    success("Backup created.")
    return

def color_match(list_css, debugger):
    def color_find(color1, color2, sub1, sub2, type_color):
        # To Be Implemented

        if type_color == "solid":
            #Solid
            for file in list_css:
                if debugger == 0:
                    print("Changing colors [SOLID " + str(color1) + "] in " + str(file) + "...", "\r", end="")
                else:
                    print("Changing colors [SOLID " + str(color1) + "] in  " + str(file) + " in debug mode...")
        elif type_color == "linear-gradient":
            # Gradient
            # Base Statements
            up_arr = []
            left_arr = []
            right_arr = []
            down_arr = []
            found_lines = 0

            # Check if it says left
            bsl = "background-image: linear-gradient(to left, " + color1 + ", " + color2 + ");"
            bsr = "background-image: linear-gradient(to right, " + color1 + ", " + color2 + ");"
            # Check if it says up
            bsu = "background-image: linear-gradient(" + color1 + ", " + color2 + ");"
            # Check if it says down
            bsd = "background-image: linear-gradient(to down, " + color1 + ", " + color2 + ");"

            for file in list_css:
                if debugger == 0:
                    print("Changing colors [GRADIENT " + str(color1) + " " + str(color2) + "] in " + str(file) + "...", "\r", end="")
                else:
                    print("Changing colors [GRADIENT " + str(color1) + " " + str(color2) + "] in " + str(file) + " in debug mode...")
                with open(file, 'r') as f:
                    print(str(file) + " opened")
                    for num, line in enumerate(f, 1):
                        if bsr in line:
                            if debugger:
                                print("Found replacement needed in line " + str(num))
                            print(bsr)
                            right_arr.append(num)
                            found_lines += 1
                        if bsl in line:
                            if debugger:
                                print("Found replacement needed in line " + str(num))
                            print(bsl)
                            left_arr.append(num)
                            found_lines += 1
                        if bsu in line:
                            if debugger:
                                print("Found replacement needed in line " + str(num))
                            print(bsu)
                            up_arr.append(num)
                            found_lines += 1
                        if bsd in line:
                            if debugger:
                                print("Found replacement needed in line " + str(num))
                            print(bsd)
                            down_arr.append(num)
                            found_lines += 1
                print(str(found_lines))
                with open(file, 'r') as fr:
                    lines = fr.readlines()

                # for i in right_arr:
                #     right_arr[i] += 1
                # for i in left_arr:
                #     left_arr[i] += 1
                # for i in up_arr:
                #     up_arr[i] += 1
                # for i in down_arr:
                #     down_arr[i] += 1
                # print(str(right_arr))
                # print(str(left_arr))
                # print(str(up_arr))
                # print(str(down_arr))

                with open(file, 'w') as fw:
                    for num, line in enumerate(lines):
                        num = num + 1
                        # print(str(num) + "num")
                        if num in right_arr:
                            if debugger:
                                print("Right found")
                            fw.write("  background-image: linear-gradient(to right, " + sub1 + ", " + sub2 + ");\n")
                        elif num in left_arr:
                            if debugger:
                                print("Left found")
                            fw.write("  background-image: linear-gradient(to left, " + sub1 + ", " + sub2 + ");\n")
                        elif num in up_arr:
                            if debugger:
                                print("Up found")
                            fw.write("  background-image: linear-gradient(" + sub1 + ", " + sub2 + ");\n")
                        elif num in down_arr:
                            if debugger:
                                print("Down found")
                            fw.write("  background-image: linear-gradient(to down, " + sub1 + ", " + sub2 + ");\n")
                        else:
                            # if debugger:
                            #     print("none found")
                            fw.write(line)

        else:
            warning("Error: color matching type invalid.")
    
    # Contacts gradient
    color_find("#2cccc4", "#41807c", "#0c6524", "#093514", "linear-gradient")


def github_exec(debugger, custom_commit):
    # os.system("echo Now ready to push to Github")
    success("Now ready to push to GitHub")
    # Will add later
    os.system("git add *")
    os.system("git commit * -m " + custom_commit)
    os.system("git push")
    warning("Git Pages takes roughly one minute for files to reflect website")
    time_elapse = 0
    time_max = 60
    time_step = 0.1
    # time.sleep(60)
    while time_elapse <= time_max:
        time_frac = time_elapse / time_max
        time_frac = time_frac * 100
        print("Github is loading page, progress " + str(round(time_frac, 2)) + "%...", "\r", end="")
        time.sleep(time_step)
        time_elapse = time_elapse + time_step
    print('\n')
    success("Git Pages should recognize changes")


def source_html(debugger):
    if debugger:
        print("WARNING: HTML files are only being examined in the current folder.")
    path = r'*.html'
    file_arr = glob.glob(path)
    if debugger:
        print("Found files = " + str(file_arr))
    return file_arr

def source_css(debugger):
    if debugger:
        print("WARNING: CSS files are only being examined in the current folder.")
    path = r'*.css'
    file_arr = glob.glob(path)
    if debugger:
        print("Found files = " + str(file_arr))
    return file_arr


def nicepage_footer_remover(file, start, end, debugger):
    if debugger:
        print("File " + str(file))
    print("Rewriting without footer for " + str(file))
    with open(file, 'r') as fr:
        lines = fr.readlines()
    with open(file, 'w') as fw:
        for num, line in enumerate(lines):
            if start <= num <= end:
                continue
            fw.write(line)

def nicepage_footer_locator(list_html, debugger):
    if debugger:
        print("Enters nicepage_footer_locator")

    # Used for most html pages
    line1 = '<section class="u-backlink u-clearfix u-grey-80">'
    line2 = '<a class="u-link" href="https://nicepage.com/website-templates" target="_blank">'
    line3 = '<span>Website Templates</span>'
    line4 = '</a>'
    line5 = '<p class=\"u-text\">'
    line6 = '<span>created with</span>'
    line7 = '</p>'
    line8 = '<a class=\"u-link\" href=\"\" target=\"_blank\">'
    line9 = '<span>Website Builder Software</span>'
    line10 = '</a>.' 
    line11 = '</section>'

    # Used for Home and Index
    line8_alt = '<a class="u-link" href="https://nicepage.com/html-website-builder" target="_blank">'
    line9_alt = '<span>HTML Creator</span>'

    for file in list_html:
        if debugger == 0:
            print("Examining " + str(file) + "...", "\r", end="")
        else:
            print("Examine " + str(file) + " in debug mode...")
        # time.sleep(1)
        with open(file, "r") as f:
            line_num_1 = 0
            line_num_2 = 0
            line_num_3 = 0
            line_num_4 = 0
            line_num_5 = 0
            line_num_6 = 0
            line_num_7 = 0
            line_num_8 = 0
            line_num_9 = 0
            line_num_10 = 0
            line_num_11 = 0
            for num, line in enumerate(f, 1):
                if line1 in line:
                    line_num_1 = num
                    if debugger:
                        print("Found line 1 + " + str(num))
                elif line2 in line and line_num_1 != 0:
                    line_num_2 = num
                    if debugger:
                        print("Found line 2 + " + str(num))
                elif line3 in line and line_num_2 != 0:
                    line_num_3 = num
                    if debugger:
                        print("Found line 3 + " + str(num))
                elif line4 in line and line_num_3 != 0 and line_num_4 == 0:
                    line_num_4 = num
                    if debugger:
                        print("Found line 4 + " + str(num))
                elif line5 in line and line_num_4 != 0:
                    line_num_5 = num
                    if debugger:
                        print("Found line 5 + " + str(num))
                elif line6 in line and line_num_5 != 0:
                    line_num_6 = num
                    if debugger:
                        print("Found line 6 + " + str(num))
                elif line7 in line and line_num_6 != 0 and line_num_7 == 0:
                    line_num_7 = num
                    if debugger:
                        print("Found line 7 + " + str(num))
                elif (line8 in line or line8_alt in line) and line_num_7 != 0:
                    line_num_8 = num
                    if debugger:
                        print("Found line 8 + " + str(num))
                elif (line9 in line  or line9_alt in line) and line_num_8 != 0:
                    line_num_9 = num
                    if debugger:
                        print("Found line 9 + " + str(num))
                elif line10 in line  and line_num_9 != 0:
                    line_num_10 = num
                    if debugger:
                        print("Found line 10 + " + str(num))
                elif line11 in line and line_num_10 != 0:
                    line_num_11 = num
                    if debugger:
                        print("Found line 11 + " + str(num))
                    break
            f.close()
        if (line_num_11 - line_num_1 == 10) and (line_num_11 - line_num_2 == 9) and \
            (line_num_11 - line_num_3 == 8) and (line_num_11 - line_num_4 == 7) and \
            (line_num_11 - line_num_5 == 6) and (line_num_11 - line_num_6 == 5) and (line_num_11 - line_num_7 == 4) and \
            (line_num_11 - line_num_8 == 3) and (line_num_11 - line_num_9 == 2) and (line_num_11 - line_num_10 == 1):
            if debugger:
                success("Successful find of Nicepage footer")
            endline = line_num_11
            startline = line_num_1
            nicepage_footer_remover(file, startline, endline, debugger)
        else:
            warning("Unsuccessful find of Nicepage footer - Check manually.")
            print(str(file) + " will publish as is.\n")

if __name__ == "__main__":
    main()