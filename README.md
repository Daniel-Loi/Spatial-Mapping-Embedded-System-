# Spatial-Mapping-Embedded-System-
2DX4 Final Project

  The MSP432E401Y is the main component of this system, it allows for I2C communication with
peripherals and UART communication with the PC. When the microcontroller is powered on, the
microcontroller immediately configures all the input and output ports used in this system. Then it starts
the configuration of the UART program and the I2C communication protocol for the ToF sensor. Using an
interrupt-based program, the system will not start taking measurements until the on-board button PJ1 is
pressed which lets the sensor immediately take a measurement at the horizontal then starts to rotate
the stepper motor at an angle depending on how many points the user wants to have. At each distance
measurements the microcontroller receives the data from the distance measurement using I2C and
transfers that data to the PC using UART to prepare with the visualization.

  The external push button uses an active low system which means that when its idle it has a
voltage of 3.3V and goes to 0V when the button is pressed. The button has a connection with the
microcontroller at port PM1. The button is programmed to have a higher priority than the on-board
button to prioritize the need to stop, otherwise the system will continue to run normally.

  The MOT-28BYJ48 stepper motor is used to have more precision with angles allowing for more
accurate mapping of the area that is being measured. The connection of the motor uses PH[0:3]
connected to IN[1:4] respectively and operates with a voltage of 5V. After completing a complete cycle,
the motor will rotate back 360 degrees to untangle the wires that the ToF sensor uses while it is
mounted on the motor.

  The VL53L1X Time-of-Flight sensor uses LIDAR technology to obtain the measurements by
measuring the time it takes for a photon to hit the target and reflect onto the sensor. This sensor is
mounted onto the stepper motor where it moves along with the angle that the motor rotates through to
stop and take a measurement each time.
