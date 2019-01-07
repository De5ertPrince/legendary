
# Wade’s Project
## Project Topic: Deep Learning

## Project Title: What’s Eating My Pets?

## My Purpose: 
The purpose of my experiment is to keep my chickens alive. I will build an an early warning system with a raspberry pi with and a camera.  I will write a program that detects predators using a convolutional neural network and send my parents na SMS if there is a predator detected near the chicken coop. 

## Background: 
In the Tanque Verde Valley many chicken owners have lost chickens to predators. We have lost over a dozen chickens. We think we lost them to hawks, coyotes, bobcats, and maybe even a raccoon, but we don’t know for sure. We’ve even rebuilt our coop multiple times but have still lost chickens to predators. We hope the Raspberry Pi solution will help us solve this mystery and save our chickens lives. 

### Raspberry Pi
What is a Raspberry Pi and why did you use it for this project?

#### Module: Camera 
https://www.amazon.com/gp/product/B01ER2SKFS/ref=ox_sc_act_title_2?smid=A2E7RYXKRFD586&th=1 
What is it? How does it work? Why is it useful for this project?

#### Module: Camera with Night Vision
https://www.amazon.com/gp/product/B07HMH1C59/ref=ox_sc_act_title_2?smid=A2E7RYXKRFD586&psc=1 
What is it? How does it work? Why is it useful for this project?

### Open Source 
What is Open Source Software and why is it important for this project?

Key term/project: Github

### Deep Learning:
What is Deep Learning and why did you use it for this project?

Key terms: Predictive Model, Artificial Neural Networks, Convolutional Neural Nets, YOLO

### SMS and Twilio:
https://www.hackster.io/matthew-wagner/sending-texts-with-the-raspberry-pi-faaab3 


## Methods:
### Materials:
Raspberry Pi 3
Raspberry Pi-compatible camera
Raspberry Pi-compatible Infrared camera (for photographs in dark)
Weather protection
#### Software setup:
##### Pi:
Install NOOBS new out of box software for Pi
##### Model:
Install the YOLO machine learning software from Github
Download model weights for the YOLO machine learning models
##### Camera:
Learn how to use the camera to take photos in python

### Testing:
#### Testing the YOLO model
Download photos of predators and non-predators we might see near the chicken coop: bobcats, bears, javelina, babies, kittens, tortoises, snakes, roadrunners, hawks, mice, packrats, moles, lizards, gila monsters, coatimundi, ringtail cats, mountain lions, deer, dogs, coyotes, foxes, raccoons, skunks, and my baby sister. Run the YOLO model on these photos and measure the accuracy. 

#### Testing the camera
Attach camera to Pi according to directions and take photos with Pi software. Use photos with YOLO model to classify Baby Jane, me, my dad, the dog, and the chickens.

### Algorithm
```
Do this forever:
  Take picture
  Run YOLO on picture
    For each object identified by YOLO:
    If the object is a predator AND the confidence greater than 25%:
      Save the photo
      Send SMS to Mom and Dad
      Ring an alarm
```
Implement the algorithm in python. Some pieces may have to run as a system process (e.g., darknet).
 
### Diagram (of hardware): 

### Diagram (of the program)

### Program code:
Github Link
