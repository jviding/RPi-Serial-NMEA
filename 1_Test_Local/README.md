# Test Serial Locally

Verify the serial interface works on the RPi.

1. Connect the RPi onboard TX and RX to one another.

Wiring: TX -> 220ohm -> RX
Add 10k pull-down to both RX and TX.

2. Start sending from TX and reading from RX.

Run simultaneously both:
> read.py
> write.py

3. Both scripts should now produce output

Troubleshoot:
  The scripts assume serial is enabled on /dev/ttyS0.
  If they don't work, check the RPi configurations.
