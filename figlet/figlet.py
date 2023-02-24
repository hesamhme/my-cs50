import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    shart = True
elif len(sys.argv) == 3 and (sys.argv[1]=='-f' or sys.argv[1]=='--font' ):
    shart = False
else:
    sys.exit(1)



figlet.getFonts()

if shart == False:
    try:
        figlet.setFont(font=sys.argv[2])

    except:
        print('error')
        sys.exit(1)
else:
    font= random.choice(figlet.getFonts())

vorood=input('input:')
print(figlet.renderText(vorood))



