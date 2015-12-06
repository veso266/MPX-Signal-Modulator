# MPX-Signal-Modulator
## To use this Flowgraph you will need: 
```
Stereo Tool: http://www.stereotool.com/download/ (or some other MPX Generator)
Jack Audio Connection (sudo apt-get install jackd2)
libjack-jackd2-dev (sudo apt-get install libjack-jackd2-dev)
Jack Gui (like QjackCtl): http://qjackctl.sourceforge.net/
```
Run the flowgraph: 
```
1. Run QjackCtl and set its samle rate to 192khz
2. Run GNU Radio and start the flowgraph
3. Run Stereo Tool
  Download Stereo Tool (optionaly rename it to st) 
  chmod it (sudo chmod +x st)
  Run it ./st
4. enable FM Transmitter and FM Output 
5. in FM Output settings Set left chanel to FM-LR:0 and right to FM-LR:1
  (Optionaly you can load my FM Preset (Velkaton.sts))
  
