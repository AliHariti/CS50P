import sys
import random
from pyfiglet import Figlet

# This program is working correctly now, qnd passed check50

figlet = Figlet()

if not len(sys.argv) in [1,3]:
    sys.exit("Invalid usage")
elif len(sys.argv) == 3:
    if not sys.argv[1] in ["-f", "-font"] or not sys.argv[2] in figlet.getFonts():
        sys.exit("Invalid usage")
    text = input("")
    figlet.setFont(font=sys.argv[2])
    print(figlet.renderText(text))
elif len(sys.argv) == 1:
    text = input("")
    fontch = random.choice(figlet.getFonts())
    figlet.setFont(font=fontch)
    print(figlet.renderText(text))
