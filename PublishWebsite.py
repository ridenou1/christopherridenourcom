import sys
import glob
from tkinter import SOLID
from colorama import Fore, Back, Style
import os
import time

def main():
    debugger = 0
    nicepage_foot_rem = 1
    git_push = 0
    custom_commit = "\"Remove footer - add python to new repo\""
    # Adding this comment to test github correctness
    print("\nFinding all website source HTML files...")

    # Need to modify for any programs requiring html files
    if nicepage_foot_rem:
        list_html = source_html(debugger)

    # Need to modify for any programs requiring css files

    if nicepage_foot_rem:
        print("\nRemoving all Nicepage html generation...")
        nicepage_footer_locator(list_html, debugger)

    if git_push:
        github_exec(debugger, custom_commit)

    return

def warning(in_string):
    print(Fore.RED + in_string + Style.RESET_ALL)
    return

def success(in_string):
    print(Fore.GREEN + in_string + Style.RESET_ALL)
    return

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