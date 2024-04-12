#!/usr/bin/python3

# clay@thoughtrights.com, Thoughtrights, Apr-11 2024

import wargames

print(f"""Content-Type: text/html\n\n
<link rel="stylesheet" href="WOPR.css">""")

# LIST GAMES
print("""<div class="woprScroll"><span class="woprStyle woprAnimate">""")
for game in wargames.woprListGames:
    print (f"{game}<br />")
spacer=''
for i in range(15):
    spacer+= "<br />\n"
print (spacer)
print (spacer)
   
# CPE1704TKS
for scenario in wargames.woprListNukes:
    print (f"{scenario}<br />")
print (spacer)
print("</span></div>\n")


# ML
print("""<div class="woprScroll joshua1"><span class="woprStyle">""")
for line in wargames.woprConcludes1:
    print (f"{line}<br />")
print("</span></div>\n")
print("""<div class="woprScroll joshua2"><span class="woprStyle">""")
for line in wargames.woprConcludes2:
    print (f"{line}<br />")
print("</span></div>\n")



