# Makes a blank image
SIZE=320x240
TMP_FILE=/tmp/frame.png

# Creates text and background for the image
convert -background lightblue -fill blue -font Times-Roman -pointsize 24 \
      -size $SIZE \
      label:'Created by Eric Morse' \
      -draw "text 80,200 'Fear the Penguin'" \
      $TMP_FILE
# Creates the text image atop of the previous image
convert $TMP_FILE \( tux.png -background none \) -composite result.png

# runs command to display onto Beaglebone
sudo fbi -noverbose -T 1 result.png

# convert -list font
