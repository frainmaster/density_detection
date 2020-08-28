# density_detection

### Installing requirements

`py -3.7 -m pip install -r requirements.txt`

NOTE:
- All files must be run using Python 3.7 and below because TensorFlow is not supported on latest Python versions yet.

### Running the program

`py -3.7 density_detection.py`

- An output file of type Excel and MP4 will be produced in `/ouput` directory.
- You can configure the input video in `/input` directory. Make sure to change the boundary box coordinates (the `start_point` and `end_point`) in `density_detection.py`.
