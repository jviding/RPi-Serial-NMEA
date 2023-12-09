# Test Serial with External Source

Verify the external peripheral sends output.

## Using scope

Easiest is to analyze the signals with a scope.
It allows verifying there's output, and reading the baudrate.

Note: 
  Add resistance if necessary, to avoid burning the probes.
  For example, in the wiring below, use 4.7k ohm resistors.

## Using RPi

1. Connect the RPi with the external peripheral

Note:
  Check the output voltage of the peripheral.
  Add more resistance / voltage drop, if necessary.

Wiring:
> TX  -> input pin (RX)
> RX  -> output pin (TX)
> GND -> GND

Pull-down is not needed with the common ground.

2. Start reading the peripheral output

Note:
  Adjust the baudrate as needed.
  Try utf-8 decoding if there's output.

Run:
> read.py

3. You should now see the peripheral output

Troubleshoot:
  Try switching the TX and RX.
  They are easily mixed.

  Try adding pull-down, it may stabilize the signals.
  Verify the waveform with a scope.

  Fall back to 1_Test_Local to verify the RPi still works.
  The pins might've been burned if the voltage was too high.
