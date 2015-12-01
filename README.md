# PiMon

A Raspberry Pi build monitor for use with NeoPixels. It currently supports CircleCI, 
though support is intended for Jenkins as well.

## Parts List

* 1 [LED Pixel Strip](http://www.amazon.com/gp/product/B00JR0MJIU)
* 1 [5V Power Supply for the Pixel Strip](http://www.amazon.com/gp/product/B00MHV7576)
* 1 [Raspberry Pi 1B+](https://www.raspberrypi.org/products/model-b-plus/) - the library may or may not work with Pi 2
* 1 [MicroUSB Power Supply](http://www.amazon.com/CanaKit-Raspberry-Supply-Adapter-Charger/dp/B00MARDJZ4/ref=sr_1_2)
* 1 [USB WiFi Adapter](http://www.amazon.com/Edimax-EW-7811Un-150Mbps-Raspberry-Supports/dp/B003MTTJOY/ref=sr_1_1) - Optional
* 1 [1000µF 6.3V Capacitor](http://www.amazon.com/gp/product/B00H8Q85OW)
* 1 [1N4001 diode](http://www.amazon.com/1N4001-Molded-Plastic-Rectifier-Diodes/dp/B0087YKE02/ref=sr_1_1)
* 1 [2.1mm Female DC Power adapter](http://www.amazon.com/HitLights-Female-Screw-Terminal-Connector/dp/B00ZGDF7AY/ref=sr_1_2)
* [Assorted jumper cables](http://www.amazon.com/Multicolored-Female-Breadboard-Jumper-Blovess/dp/B013DSZE8I/ref=sr_1_3)
* 1 ethernet cable

You will probably also need a monitor and keyboard for initial setup.
 
## Setup

1) Get the Pi on the network.
  * Power up (plug it in).
  * Login -- username: pi - password: raspberry
  * If your network is setup for DHCP, the Pi _should_ just receive an IP address once it's connected with the ethernet cable. You can optionally follow the [instructions](https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md) to setup WiFi.
  * If you need multiple WiFi networks, the accepted answer [here](http://raspberrypi.stackexchange.com/questions/11631/wifi-setup-for-multiple-networks) worked for me.

2) Install updates and such.
  * Most of the things you need should be in [bin/setup.sh](bin/setup.sh). This sets up the Pi-Pixel library and installs the python requests library for HTTP handling.

3) Turn off the Pi.  

4) Wire up the pixels. **TL;DR - For those that like pictures, I found [this guide](https://learn.adafruit.com/neopixels-on-raspberry-pi/wiring) invaluable.** The only difference there is that I didn't use the Pi GPIO extender into the breadboard.
  * **DO NOT PLUG ANYTHING INTO LIVE CURRENT YET**
  * Put one of the capacitor's pins in the female power adapter's ground jack, the other in the positive jack.
  * Wire the Pixels' ground wire to the ground jack on the female power adapter.
  * Wire the Pixels' +5V power-in wire to the diode, strip-side facing the pixels. The non-strip-side should connect to the positive jack on the female power adapter.
  * Connect the Pi's GPIO ground to the ground jack on the female power adapter.
  * Connect the Pi's GPIO Pin 18 to the Pixels' DIN.
  * Power up the pixels.
  * Power up the Pi.

5) Verify wiring.
  * There are a number of example scripts available. The low-level Pi interface provides some [testing scripts](https://github.com/jgarff/rpi_ws281x/blob/master/python/examples/strandtest.py), or you can jump straight to some of the examples [here](bin/examples).

6) Profit.

![Tree1](https://cloud.githubusercontent.com/assets/1172512/11493781/6dac0486-97b9-11e5-8cf8-e4892a7aff8d.jpg)
![Tree2](https://cloud.githubusercontent.com/assets/1172512/11493805/9d3de6ba-97b9-11e5-840a-2575e83cf893.jpg)
