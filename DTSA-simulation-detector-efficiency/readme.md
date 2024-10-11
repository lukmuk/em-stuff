## Detector efficiency curve calculator

This notebook can be used to apply a custom detector efficiency envelope to simulated DTSA-II spectra.

As pointed out [here](https://probesoftware.com/smf/index.php?topic=1225.msg9676#msg9676) by Nicholas Ritchie, one can alternatively modify the `custom.csv` file in DTSA-II with the desired transmission percentages. The `custom.csv` file in this repository is build from the detector efficiency curve from the publication by Schlossmacher et al. as described in the Jupyter notebook. Note that (i) the data was extracted from a pixelated figure from the publication and (ii) a simple interpolation was used to build the curve. Therefore, there is uncertainty in the detector efficiency.

See also the main page of NIST DTSA-II: https://cstl.nist.gov/div837/837.02/epq/dtsa2/

![NIST_DEC](https://github.com/lukmuk/em-stuff/blob/main/DTSA-simulation-detector-efficiency/images/DTSA_DEC.png)
