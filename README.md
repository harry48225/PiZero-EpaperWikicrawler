# PiZero-EpaperWikicrawler
Displays crawled wikipedia pages on the waveshare 2.13" eInk pHAT

![Image of the project](https://github.com/harry48225/PiZero-EpaperWikicrawler/blob/master/example.jpg)

# Installation and usage
Create the venv (don't use sudo)

``` sudo apt install libatlas3-base libgfortran5``` (Will fix the numpy c import errors)

``` pip install -r requirements.txt ```(Make sure that numpy is a version from pywheels otherwise 2h+ compile time eeeee)

Then just running main should work

Futher notes:

I have modified the lib from the waveshare github,

in the epdconfig I have removed the jetson class (was getting some sort of ctypes error)

in epd2in13_V2 I have set epd = epd.RaspberryPi() (I'm not sure how it worked in their examples)

---

Use viewImage to get the image on a normal computer (with a gui)
run main to display the image on the epaper.


> Hack font from https://sourcefoundry.org/hack/
