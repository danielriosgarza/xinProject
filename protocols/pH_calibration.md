# **pH Calibratio**

1. Check ph device connections
2. Prepare three calibrated pH test solutions (pH 4, 7, 10)
3. Enter the reactor to be calibrated in the terminal (ssh pioreactor@100.117.2.9), (ssh pioreactor@mCPUworker03.local)
4. Run the py file that has been written (python) followed by (import testPh as pH)
5. Enter (pH.send_command('R')) to test if the ph device can be read properly
6. Place the pH meter in the reference liquid and follow the steps pH7 (pH.send_command('Cal,mid,7.00')); pH4 (pH.send_command('Cal,low,4.00')); pH10 (pH.send_command('Cal,high, 10.00')) in order for the device to take a reading in sequence. Note: Flush the pH meter each time the fluid is changed.
7.Afterwards use (pH.send_command('Cal,?')) and (pH.send_command('C,0')) to confirm the calibration, and when finished you can measure with a liquid of known pH to ensure calibration!
