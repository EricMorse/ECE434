# Here's how to use imagemagick to display text
# Make a blank image
SIZE=320x240
TMP_FILE=/tmp/frame.png

# From: http://www.imagemagick.org/Usage/text/
convert -background lightblue -fill blue -font Times-Roman -pointsize 24 \
      -size $SIZE \
      label:'Created by Eric Morse' \
      -draw "text 80,200 'Fear the Penguin'" \
      $TMP_FILE

convert $TMP_FILE \( tux.png -background none \) -composite result.png


sudo fbi -noverbose -T 1 result.png

# convert -list font
