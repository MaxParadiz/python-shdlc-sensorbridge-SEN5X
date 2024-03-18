# SEN5X Python Scripts

I have created a fork of Sensirion's SEK-SensorBridge and added my own scripts to it for making use of the SEN55-Sensor Bridge.

To make use of this, install the SHDLC driver for the SEK SensorBridge by following the official instructions. 

You can use:

```
pip install sensirion-shdlc-sensorbridge
```

My small additions can be found inside of the folder sen5x. These are scripts for interfacing with the SEN5x through the Sensor Bridge.

My main motivation for this was that I could not get their software running in Arch Linux. 
But in the process I have found that, by interfacing the device with python, it is easier to control the flow of output data.

I am also including some instructions on how to set up a postgresql database and how to populate it from the sensor's output data. This structure is very conveninent if you would like to collect continuous data. With this structure, you can measure continuously for 1 year at 1 sample per second and your database will weight about 3.65 GB. This is probably a good way of handling the data acquisition in a raspberry pi.



# Python Driver for Sensirion SEK-SensorBridge

This repository contains the SHDLC driver for the
[Sensirion SEK-SensorBridge](https://www.sensirion.com/sensorbridge/)
as a Python package. For details, please read the package description in
[README.rst](README.rst).

## Usage

See package description in [README.rst](README.rst) and user manual at
https://sensirion.github.io/python-shdlc-sensorbridge/.

## Development

We develop and test this driver using our company internal tools (version
control, continuous integration, code review etc.) and automatically
synchronize the `master` branch with GitHub. But this doesn't mean that we
don't respond to issues or don't accept pull requests on GitHub. In fact,
you're very welcome to open issues or create pull requests :)

### Check coding style

The coding style can be checked with [`flake8`](http://flake8.pycqa.org/):

```bash
pip install -e .[test]  # Install requirements
flake8                  # Run style check
```

In addition, we check the formatting of files with
[`editorconfig-checker`](https://editorconfig-checker.github.io/):

```bash
pip install editorconfig-checker==2.0.3   # Install requirements
editorconfig-checker                      # Run check
```

### Run tests

Unit tests can be run with [`pytest`](https://pytest.org/):

```bash
pip install -e .[test]          # Install requirements
pytest -m "not needs_device"    # Run tests without hardware
pytest                          # Run all tests
```

The tests with the marker `needs_device` have following requirements:

- A SensorBridge must be connected to the computer:
  - Firmware version must be 5.8
  - Default settings (baudrate 460800, address 0)
  - Port 0: SHTC3 connected
  - Port 1: No device connected
- Pass the serial port where the SensorBridge is connected with `--serial-port`,
  e.g. `pytest --serial-port=COM7`


### Build documentation

The documentation can be built with [Sphinx](http://www.sphinx-doc.org/):

```bash
python setup.py install                        # Install package
pip install -r docs/requirements.txt           # Install requirements
sphinx-versioning build docs docs/_build/html  # Build documentation
```

## License

See [LICENSE](LICENSE).
