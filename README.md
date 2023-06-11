![license
status](https://img.shields.io/github/license/johnwslee/extrucal_dashboard)

# Dashboard for Throughput Estimation in Single Screw Extrusion

**Author:** John W.S. Lee

Link to the dashboard: https://extrucal.onrender.com/

## Description of Extrucal Dashboard App

The [dashboard](https://extrucal.onrender.com/) consists of 5 main sections: 

(i) "Throughput Calculation" tab: Here, the user can find the predicted throughput in plots and tables by specifing the screw size, melt density of polymer material, number of screw flight, minimum screw RPM, maximum screw RPM, and increment of screw RPM.

(ii) "Cable Extrusion" tab: Here, the user can find the requred screw RPMs in plots and tables for the specified cable geometries (i.e., outer diameter and insulation thickness), material information(i.e., solid/melt density), processing conditions(i.e., line speeds), and extruder specs(i.e., extruder size, screw channel depth).

(iii) "Tube Extrusion" tab: Here, the user can find the requred screw RPMs in plots and tables for the specified tube geometries (i.e., outer diameter and inner diameter), material information(i.e., solid/melt density), processing conditions(i.e., line speeds), and extruder specs(i.e., extruder size, screw channel depth).

(iv) "Rod Extrusion" tab: Here, the user can find the requred screw RPMs in plots and tables for the specified rod die geometries (i.e., rod outer diameter and number of die holes), material information(i.e., solid/melt density), processing conditions(i.e., line speeds), and extruder specs(i.e., extruder size, screw channel depth).

(v) "Sheet Extrusion" tab: Here, the user can find the requred screw RPMs in plots and tables for the specified sheet geometries (i.e., sheet width and thickness), material information(i.e., solid/melt density), processing conditions(i.e., line speeds), and extruder specs(i.e., extruder size, screw channel depth).

All plots are updated when the user presses enter or clicks out of the box.  

![](https://github.com/johnwslee/extrucal_dashboard/blob/main/img/extrucal_dashboard_demo.gif)

## How to Run the Dashboard Locally

To download the contents of this GitHub page on to your local machine follow these steps:

1. Copy and paste the following link: `git clone https://github.com/johnwslee/extrucal_dashboard.git` to your Terminal.

2. On your terminal, type: `cd extrucal_dashboard`.

3. To run a development instance locally, first create a virtualenv by typing: `conda create --name new_env_name`

4. Install the requirements from ***requirements.txt*** by typing: `pip install -r requirements.txt` 

5. Type the following command if the environment isn't automatically activated after Step 3: `conda activate new_env_name`

6. Launch ***app.py*** using the Python executable from the virtualenv: `python src/app.py`

7. Using any modern web browser, visit http://127.0.0.1:8050/ to access the app.

**Note that for Steps 3 - 6 to work smoothly, you have to be in the our_changing_world directory.**
