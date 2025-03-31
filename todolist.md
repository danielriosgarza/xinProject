# **Weekly Planning**

General goals:

- Familiarize yourself with the system, step-by-step:
0) Prepare you raspberry pi
1) Assemble a reactor
2) Control and program: temperature, stirring, Optical density, pH, current density one-by-one in water, in one reactor, in multiple reactors
3) Cultivate a bacteria isolate in the system: goal is to produce some electrical current in the working electrode
4) Control: pumps and do cultivation with control programs
- 

### **Week 1**
**Mon**

- Printed model
- Meeting with Chrystelle to see the lab
- Assemble a reactor

- Read about the pioreactor (the base we are using for the mCPU): [here](https://docs.pioreactor.com/user-guide/getting-started)

- Challenge 1: control the temperature: make a squeme of 3h with 25C, 3h with 30, 3h with 35.



**Tue**
On reactor 6

Part 1: set the temperature
  
  pioreactor - manage - setting - temperature(add label)

part 2: program a small script to change the temperature at specific time

One by one control the reactor parameters with water

**Wed**

One by one control the reactor parameters with water

**Thu**

One by one control the reactor parameters with water

**Fri**

Prepare the media for the inoculation

### **Week 2**

**Tue**
1) add the missing 5 pioreactors to the cluster

2) Blink them to see if they are recognized and working

3) Check the print and upload a picture

### **Week 3**

1) Turn off all the reactors
2) Remove the tubes, align them and take a picture.
3) Clean the tubes: throw the bacteria in the bleach, careful with the magnet
4) wash the tube being very careful with the magnet.
5) fill them with water and, together we update the system and make all the self-tests and calibration.
6) simulate the profiles with 10X less time with water
7) Repeat last week's experiment: 1) preculture; 2) culture. (in case we need to prepare media, we do it together)

8) late afternoon, we write some python scripts to get the data from the pioreactor and make our own plots.
9) Finish printing the other parts of the model, then we can test your design for the pH flow. 

/


### **week 4**

the main goal of the week is to test and calibrate the pH. First with water, then with the culture.

1) Make a new printed reactor;

For the pH test with water:
1) Assemble the reactor;
2) Add the pH to the interface.
3) calibrate the pH meter; [check](https://files.atlas-scientific.com/EZO-pH-complete-datasheet.pdf)
4) we simulate an experiment, where we add some acid to water;
5) pre-culture, inoculate the assembled reactor with culture and measure OD, temperature, and pH.
