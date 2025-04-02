## **OD Calibration**

### **Protocol 1:** single_vial (for: single_device_quick_calibration)

Steps:
1. Prepare the sample: Use a 10 mL tube of the culture solution (the concentration should be at the highest OD600—we used a bacterial sample that was cultured for 24 hours).

*Use the spectrophotometer and add 1 mL of medium to one cuvette and 0.5 mL of culture to another.
Use the cuvette with medium to blank the spectrophotometer and measure the other cuvette. Determine the sample's OD as two times the measured OD.*

\\

2. Place the sample tube in the Pioreactor and ensure the magnetic stirring is working.

3. To start calibration, type `pio calibrations run --device od` and type single_vial.

(Copied from moba）:
```bash
This routine will calibrate the current Pioreactor to (offline) OD600 readings. You'll need.
    1. The Pioreactor you wish to calibrate (the one you are using)
    2. At least 10mL of a culture with the highest density you'll ever observe, and its OD600 measurement {Question: do I need to measure it myself with a spectrophotometer?}
    3. A micro-pipette, or accurate tool to dispense 1ml of liquid. 4.
    4. Accurate 10mL measurement tool (ex: graduated cylinder)
    5. Sterile media, amount to be determined shortly.
```

4. Follow the system prompts:
- The program will prompt to dilute the sample by adding some medium;
- After each dilution, have the designated Pioreactor take a reading of the current od value; (we try to take a reading of each reactor using the terminal, at the same dilution, in each of the six reactors)
- Every few rounds, you will be prompted to use a pipette to remove some liquid to keep the bottle at 10 mL to prevent spillage;
- (Optional) If you have another way of measuring the actual OD600 {Question:spectrophotometer?}

*During the calibration, take 1 mL add to a cuvette and measure the OD in the spectophotometer*

5. Finish calibration: The system will fit a calibration curve based on the collected data and store it as a new calibration file.


Protocol 2: standards (faster for calibrating multiple Pioreactors)
1. Prepare a standards sample: Use multiple vials. {Question: Is it also based on the original sample with different degrees of dilution?}
