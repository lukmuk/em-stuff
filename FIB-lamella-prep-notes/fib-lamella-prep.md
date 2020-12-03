# FIB TEM lamella preparation

Some personal notes and experiences I had with sample preparation for transmission electron microscopy (TEM) using a focused ion beam (FIB)/scanning electron microscopy dual-beam system. Hopefully, some of the following notes are useful for anyone, even though modifications may be necessary for other material system/application/instrument. Especially the final thinning steps often require on-the-fly adjustments on sample tilt/beam parameters which can only be judged from personal experience with the instrument/sample. Therefore, different operators of FIB instruments use different settings and workflows which work for them.

## Youtube videos

Todo: Add links

## Useful software

* [CASINO]((https://www.gel.usherbrooke.ca/casino/index.html)): Monte-Carlo simulation

## Monte-Carlo simulation for thickness estimation

Before going to the FIB, you can use Monte-Carlo simulation to get an idea at which sample thicknesses a contrast change appears in the SEM view during final thinning. When the sample get thin enough that electrons can penetrate the lamella, secondary electrons will also be emitted from the backside, which causes a contrast change in the SE image. The ETD image normally gets brigher, while the TLD signal gets darker when the sample gets electron transparent for a certain e-beam energy.

The simulation can be done relatively quickly in Casino:

1. Define your material in the `Sample Definition` menu as a bulk sample (the material density must be known roughly). For thin films on a substrate I normally use the substrate material to judge the lamella thickness during the final thinning steps.

2. Simulate between 1 to 10 keV in 1 keV steps, e.g. around 10000 trajectories each. These parameters can be set in the `Microscope SetUp` menu.

3. The default values can be kept for the other parameters. Run `Begin Simulation`, wait for it to finish, then save the results as a .cas file and the trajectory image for each voltage.

4. You can also use the projected `ZMax` distribution.

## Sample preparation

1. Fix sample on a SEM stub (use conductive C-tape or 1-2 drops of silver glue), ensure electrical contact to ground to avoid sample charging.

2. Use sputter coater to deposit a protective layer of C (or other material)...
   
   * ...if your sample is insulating/charging (ca. 5-10 nm C) but otherwise stable under the e-beam.
   
   * ...your region of interest (ROI) is near the surface or the surface itself (e.g. a thin film on a substrate) to protect the surface (ca. 20-100 nm C). This can protect the surface features during dose-intensive electron-beam induced deposition (EBID) of Pt. See also this [application note](https://www.leica-microsystems.com/science-lab/each-atom-counts-protect-your-samples-prior-to-fib-processing/) by Leica. The simulated penetration depth (ca. 60 nm) of 2 keV electrons in C (2 g/cm$^3$ ) is shown below.

| <img title="" src="file:///C:/Users/gruenewald/Github/em-stuff/FIB-lamella-prep-notes/images/C-2keV-Casino.PNG" alt="" width="416" data-align="center"> | Monte-Carlo simulation of 2 keV electrons in C. |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------- |

## EBID

* After loading the sample and the FIB grid into the microscope, make sure the sample surface is at eucentric height, i.e. a feature does not move when tilting the stage to 52°. Tilt back to 0° for EBID.

* As an optional step, rotate the sample so that the TEM sample is close to a specific zone-axis (e.g. align the substrate edge horizontally in the SEM image).

* Switch SEM beam parameters to 2 keV and about 1-5 nA of current.

* Locate an ROI, double-check that your ROI is at eucentric height.

* From the patterning menu, select a rectangle and draw it onto the e-beam screen as a marker for EBID. You can choose the width (X) of the lamella depending on your needs. I normally use X = 10 µm, Y = 1 µm.

* Insert the gas injection system (GIS) needle.

* On newer FIBs (e.g. Helios) there might be an EBID application file that you can use. On an older machine, or if you want more control over the process, you can also use the manual way:
  
  * **Automatic EBID**: Start pattern with EBID application file, adjust Z so that pattern deposits around 100-300 nm Pt (about 3-5 min).
  
  * **Manual EBID**: Use reduced area window (F7 on FEI/ThermoFisher machines), make it same size as the rectangle pattern over your ROI and change dwell time to 1 µs. Open the GIS Pt gas flow and start scanning in the reduced window to grow the Pt layer. You can use beam shift to keep the ROI in the scanning window. See also this [video](https://www.youtube.com/watch?v=rvmF2wPJTbY) for a nice demonstration.

* After a few minutes of deposition, stop the gas flow, then stop the e-beam. Then retract the GIS needle.

## IBID

* Tilt stage to 52°. Use an i-beam current of a few 100 pA and 30 keV. Focus and stigmate the i-beam **near** your EBID pad, but minimize exposure of the pad itself as to not mill it away.

* Insert the GIS. Then create a rectangle pattern of size X = 10 µm, Y = 1.5 µm and Z = 1.5 µm. Get another image of the ROI and place the pattern over the EBID pad. Start the pattern, which should take a few minutes to finish.

After C deposition, EBID, and IBID. The sample is protected during further FIB milling. In the final cross-section TEM sample you should see a stack similar to the one below (from the Leica application note above):

<img title="" src="file:///C:/Users/gruenewald/Github/em-stuff/FIB-lamella-prep-notes/images/EBID-stack.PNG" alt="" data-align="center" width="300">

Note that the 30 keV Ga ions penetrate roughly 30-40 nm into the EBID layer (transition region between EBID and IBID layer). This shows how much damage the i-beam can do to an unprotected sample surface if one deposits only an IBID layer directly on the bare surface (or a thin C layer).
