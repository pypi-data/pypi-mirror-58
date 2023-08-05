# tart2ms

[![Build Status](https://travis-ci.org/tmolteno/tart2ms.svg?branch=master)](https://travis-ci.org/tmolteno/tart2ms)

Convert data from a [TART radio telescope](https://tart.elec.ac.nz) to measurement set format. This module relies on the excellent dask-ms module as a helper to create the measurement sets. This packate requires python-casacore to be installed on your system

## Install

    sudo aptitude install python3-casacore
    sudo pip3 install tart2ms

## Examples

Download data from the TART in real time via the RESTful API (defaults to using the API at https://tart.elec.ac.nz/signal):

    tart2ms --ms data.ms

To convert a previously downloads JSON file to a measurement set (MS):

    tart2ms --json data.json --ms data.ms

To synthesize (using wsclean) the image from the measurement set:

    wsclean -name test -size 1280 1280 -scale 0.0275 -niter 0 data.ms
 
This will create an image called test-image.fits. You will need to install wsclean on your system.

## Usage

    usage: tart2ms [-h] [--json JSON] [--ms MS] [--api API] [--catalog CATALOG]
                [--vis VIS] [--pol2]

    Generate measurement set from a JSON file from the TART radio telescope.

    optional arguments:
    -h, --help         show this help message and exit
    --json JSON        Snapshot observation JSON file (visiblities, positions
                        and more). (default: None)
    --ms MS            Output MS table name. (default: tart.ms)
    --api API          Telescope API server URL. (default:
                        https://tart.elec.ac.nz/signal)
    --catalog CATALOG  Catalog API URL. (default:
                        https://tart.elec.ac.nz/catalog)
    --vis VIS          Use a local JSON file containing the visibilities for
                        visibility data (default: None)
    --pol2             Fake a second polarization. Some pipelines choke if there
                        is only one. (default: False)

## Credits

Thanks to Simon Perkins and Oleg Smirnov for help in interpreting the measurement set documentation.


## TODO

- 

## Changelog

- 0.1.4b4 clean up some bitrot in dask-ms (dealing with chunking objects)
- 0.1.4b3 Add SIGMA, FLAG, FLAG_CATEGORY to main table (:/)
- 0.1.4b1 Add RESOLUTION and EFFECTIVE_BW to the SPECTRAL_WINDOW
- 0.1.3b1 Sort out the timestamps correctly, added a handy function for converting to epoch time.
- 0.1.2 Correct pointing direction of the array (in J2000).
- 0.1.1 Added -pol2 switch to generate a second polarization.
- 0.1.0 first functioning release.
