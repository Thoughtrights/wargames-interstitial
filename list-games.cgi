#!/usr/bin/python3

# clay@thoughtrights.com, Thoughtrights, Apr-11 2024

import wargames

print(f"""Content-Type: text/html\n\n
<head>
  <title>Wargames WOPR List Games</title>
  <meta property="og:title" content="Wargames WOPR List Games">
  <meta name="twitter:title" content="Wargames WOPR List Games">
  <meta name="twitter:card" content="summary_large_image">
  <meta property="og:image" content="https://www.thoughtrights.com/WOPR/WOPR-preview.png">
  <meta name="twitter:image" content="https://www.thoughtrights.com/WOPR/WOPR-preview.png">
  <link rel="stylesheet" href="WOPR.css">
</head>
<body>""")

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
print("</span></div></body></html>\n")



