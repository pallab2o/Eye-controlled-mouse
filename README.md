# Eye-Controlled Mouse using OpenCV and IP Camera

This project aims to create an eye-controlled mouse using the inbuilt camera of a computer or an IP camera via a smartphone and OpenCV for image processing. By tracking the user's eye movements, the mouse cursor can be controlled, providing an alternative input method for individuals with limited mobility.

## Features

- **Capture frames from the inbuilt camera or an IP camera (using a smartphone)**
- **Process frames to detect and track eye movements**
- **Control the mouse cursor based on detected eye movements**
- **Use the right eye to move the mouse cursor**
- **Use the left eye to click**
- **Press 'Esc' key to exit the program**

## Requirements

- Python 3.x
- OpenCV library (opencv-python)
- An IP camera app installed on a smartphone (for using the phone camera as an IP camera)

## Installation

Clone the repository:

```bash
git clone https://github.com/pallab2o/eye-controlled-mouse.git
cd eye-controlled-mouse
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the application:

```bash
python main.py
```

The application will start capturing frames from the inbuilt camera or the IP camera (using the smartphone) and processing them to detect eye movements. The mouse cursor will be controlled based on detected eye movements.

- **Use your right eye to move the mouse cursor.** The cursor will follow the movement of your right eye.
- **Use your left eye to click.** Blinking your left eye will simulate a mouse click.
- **Press the 'Esc' key to exit the application.**

## Troubleshooting

- If you encounter issues with frame capture or processing, ensure that the camera (inbuilt or IP camera) is functioning correctly and is not being used by any other application.
- Verify that your system meets the requirements specified in the Requirements section.
- Check for any errors reported by the application and search online for solutions or ask for help on relevant forums or communities.

## Contributing

Contributions are welcome! If you have ideas for improvements or new features, feel free to open an issue or submit a pull request.

## Acknowledgments

This project was inspired by the desire to create accessible input methods for individuals with limited mobility. Thanks to the developers of OpenCV for providing powerful tools for image processing. This project is credited to Sanyu Project World. Visit their YouTube channel for more inspiring projects: [Sanyu Project World](https://www.youtube.com/@sanyuprojectsworld)
