# Mini Sumo Robot with Raspberry Pi Pico 

![](https://github.com/byronin/Pico_Sumo_Robot/blob/main/Hardware/Sumo2.png)

Actually, the goal of this project was not to build a mini sumo robot, but to create a robot control board that can be used with Raspberry Pi Pico. By making a mini sumo robot, I demonstrated a project that can be done with the control board. I made a small addition to the design so that everyone can easily solder the board in the workshop by choosing the preferred component shape. You can quickly and professionally manufacture this board via PCBWay.com. You can follow the necessary directions for the project below.
## Sponsor
[![](https://github.com/byronin/MQTT-DMD/blob/main/Hardware/PCBWay_logo.png)](https://www.pcbway.com/project/shareproject/LoRa_Module_for_Raspberry_Pi_Arduino_ESP8266_Testing_LoRa_under_sea_83c3da00.html)
#### Thanks to PCBWay for handling PCB production.
<a href="https://www.pcbway.com/project/shareproject/LoRa_Module_for_Raspberry_Pi_Arduino_ESP8266_Testing_LoRa_under_sea_83c3da00.html"><img src="https://www.pcbway.com/project/img/images/frompcbway-1220.png" alt="PCB from PCBWay" /></a>

  ## Schematic
[![](https://github.com/byronin/Pico_Sumo_Robot/blob/main/Hardware/Schematic.png)](https://github.com/byronin/Pico_Sumo_Robot/blob/main/Hardware/Schematic.png)
 

## Hardware & BOM
![PCBs](https://github.com/byronin/Pico_Sumo_Robot/blob/main/Hardware/Board1.png "PCBs")
 [![This PCB Desing with Eagle ](https://www.snapeda.com/static/img/eda/eagle.png "PCB Desing with Eagle ")](https://www.autodesk.com/products/eagle/free-download "This PCB Desing with Eagle ") 
  ##### This PCB Desing with Eagle  
  ![PCBs](https://github.com/byronin/Pico_Sumo_Robot/blob/main/Hardware/PCB2.png "PCBs")
  ![BOM](https://github.com/byronin/Pico_Sumo_Robot/blob/main/Hardware/bom.png "BOM")
## Robot Parts

|No| PCB Components  | Piece ||No| PCB Components  |Piece | 
| ------------- |  ------------- |------------- |---------| ------------- | ------------- |------------- |
|1| [12mm 625rpm DC Motor](https://www.sumozade.com/tr/urun/force-up-6v-625-rpm-ultrapower-dc-gear-motor "12mm 625rpm DC Motor")  |  2 pcs  ||2| [2s 7.4v LiPo Battery](https://www.jsumo.com/gens-ace-300mah-74v-25c-2s1p-lipo-battery "2s 7.4v LiPo Battery") | 1 pcs |
|3| [Sumo Wheel](https://www.sumozade.com/tr/urun/spare-bond-silicone-wheel-30x23mm-pair-black "Sumo Wheel")  |  1 pcs ||4| [FS80NK-Sensor](https://tr.aliexpress.com/item/4000859937540.html?spm=a2g0o.store_pc_allProduct.8148356.1.7bd05891yVFRjr&pdp_npi=2%40dis%21TRY%21TRY%20252.96%21TRY%20139.03%21%21%21%21%21%40210323f716798632990806175e3706%2110000009682121651%21sh "FS80NK-Sensor") | 2 pcs |
### 3D File
[![](https://github.com/byronin/Pico_Sumo_Robot/blob/main/Robot/Chasis.png)](https://github.com/byronin/Pico_Sumo_Robot/tree/main/Robot)

[Click for the files](https://www.sumozade.com/tr/urun/force-up-6v-625-rpm-ultrapower-dc-gear-motor "Click for the files")

## Software 
[![](https://github.com/byronin/Pico_Sumo_Robot/blob/main/Hardware/Code.png)](https://github.com/byronin/Pico_Sumo_Robot/blob/main/Software/sumo.py)

You can code your robot on any platform that is supported by Raspberry Pi Pico. I wrote a micropython code using "Thonny IDE". You need to save the [sumo.py](https://github.com/byronin/Pico_Sumo_Robot/blob/main/Software/sumo.py "sumo.py") code as the main file on your board.
