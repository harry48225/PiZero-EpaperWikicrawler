from PIL import Image, ImageDraw, ImageFont
from wikipediaCrawl import Crawly
import textwrap

print("hello world")

SMALL_SIZE = 16
font20 = ImageFont.truetype("hack/Hack-Bold.ttf", 20)

fontSmall = ImageFont.truetype("hack/Hack-Regular.ttf", SMALL_SIZE)

c = Crawly() # Our crawler object

def getImage():


    image = Image.new('1', (250, 122), 255) # Empty image of the correct size

    draw = ImageDraw.Draw(image) # Create a drawing object to draw on the image

    wiki_data = c.get_next_page()


    draw.text((0,0), wiki_data['title'], font = font20, fill = 0)

    for i, line in enumerate(textwrap.wrap(wiki_data['summary'], width=25)):

        draw.text((0,(22 + i*SMALL_SIZE)), line, font = fontSmall, fill = 0)

    return image