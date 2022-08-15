# Manufacturing-Line-Scan-Camera-Application
<!-- omit in toc -->
<a href="https://github.com/msf4-0/Manufacturing-Line-Scan-Camera-Application/blob/master/LICENSE">
    <img alt="GitHub" src="https://img.shields.io/github/license/msf4-0/Manufacturing-Line-Scan-Camera-Application">
<a href="https://github.com/msf4-0/Manufacturing-Line-Scan-Camera-Application/releases">
    <img alt="Releases" src="https://img.shields.io/github/release/msf4-0/Integrated-Vision-Inspection-System?color=success" />
</a>
<a href="https://github.com/msf4-0/Manufacturing-Line-Scan-Camera-Application/releases">
    <img alt="Downloads" src="https://img.shields.io/github/downloads/msf4-0/Manufacturing-Line-Scan-Camera-Application/total.svg?color=success" />
</a>
<a href="https://github.com/msf4-0/Manufacturing-Line-Scan-Camera-Application">
      <img alt="Issues" src="https://img.shields.io/github/issues/msf4-0/Manufacturing-Line-Scan-Camera-Application?color=blue" />
</a>
<a href="https://github.com/msf4-0/Manufacturing-Line-Scan-Camera-Application/pulls">
    <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/msf4-0/Manufacturing-Line-Scan-Camera-Application?color=blue" />
</a>
<br><br>

The ***Manufacturing-Line-Scan-Camera-Application*** is one of the implementation of Integrated-Vision-Inspection-System (IVIS) in a manufacturing scenario using a Basler line scan camera. As the proof of concept, this project has been tested (acting as an automated quality control) on a RFID-based Production Line.

## Basic User Guide :open_book:
***NOTE: For more detailed user guide, counsult the wiki.***
#### Parameters calculation
1. In the Calculator page, user will be able to calculate one of the required variable (object speed, working distance, or exposure time) accordingly.
2. Once every other information has been filled, the result of the calculation will be shown above the "Apply the parameters above" button.
3. To use the calculated parameters, press on the "Apply the parameters above" button.
<img src="https://github.com/msf4-0/Manufacturing-Line-Scan-Camera-Application/blob/main/resources/images/page_calculator.png" width=70% height=70% />

### Paramaters Adjustment
1. In this page, the camera's parameters can be adjusted.
2. To apply the adjustments/changes, click on the "Apply the parameters above" button.
3. If the user did not make any adjusment to the parameters, the default value will be selected.
<img src="https://github.com/msf4-0/Manufacturing-Line-Scan-Camera-Application/blob/main/resources/images/page_parameters_adjustment.png" width=70% height=70% />

### Deployment 
1. To deploy the camera, go to the deployment page.
2. Click the "Connect" button.
3. Check the "Deploy" checkbox.
After this step, the image acquisition should run continuously until the "Deploy" checkbox is unchecked.
<img src="https://github.com/msf4-0/Manufacturing-Line-Scan-Camera-Application/blob/main/resources/images/page_deployment.png" width=70% height=70% />

## Node-RED:link:
This repo also features some integration with Node-RED. The sample flow of the MQTT communication between camGUI with IVIS & RFID Production Line can be found [here](https://github.com/msf4-0/Manufacturing-Line-Scan-Camera-Application/tree/main/node-RED).

<img src="https://github.com/msf4-0/Manufacturing-Line-Scan-Camera-Application/blob/main/resources/images/node_red_flow.png" width=30% height=30% />

## Citation
```tex
@misc{Manufacturing Line Scan Camera Application,
  title={{Manufacturing Line Scan Camera Application}},
  url={https://github.com/msf4-0/Manufacturing-Line-Scan-Camera-Application},
  author={
    Nathanael Virlian Wijaya},
  year={2022},
}
```
