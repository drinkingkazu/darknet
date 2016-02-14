import os

l = ["eminus","gamma","pizero","piminus","proton","muminus","kminus"]

for word in l:
    os.system("convert -fill black -background white -bordercolor white -border 4 -font futura-normal -pointsize 18 label:\"%s\" \"%s.png\""%(word, word))
