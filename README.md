# Kiosque Project

## Overview

The Kiosque project is a Python-based application designed to run on a kiosk system. It provides a graphical user interface (GUI) using the Tkinter library, allowing users to interact with various options such as opening web pages, launching applications, and displaying PDF documents.

## Features

- Fullscreen mode for kiosk display
- User activity detection to reset inactivity timer
- Various options to open web pages, launch applications, and display PDF documents
- Automatic return to the main screen after a period of inactivity
- Administrative privileges check and elevation

## Requirements

- Python 3.x
- Tkinter library
- Pillow library
- psutil library
- ctypes library

## Installation

1. Install Python 3.x from the official website: https://www.python.org/
2. Install the required libraries using pip:
    ```sh
    pip install tkinter pillow psutil
    ```

## Usage

1. Ensure you have administrative privileges to run the application.
2. Place the required images and PDF documents in the specified paths.
3. Run the `main.py` script:
    ```sh
    python main.py
    ```

## File Structure

```
Kiosque/
├── main.py
├── README.md
└── images/
    ├── ats.png
    ├── seu motora.png
    ├── CAM.png
    ├── Detran.png
    ├── CTE.png
    ├── Checklist.png
    ├── Onde.png
    ├── manual.png
    ├── Regulamento.png
    └── background.png
└── documents/
    └── Manual do Motorista - IMP.pdf
```

## main.py

The main script of the project. It initializes the Tkinter GUI, sets up the fullscreen mode, binds user activity events to reset the inactivity timer, and defines functions to handle various options.

### Key Functions

- `is_admin()`: Checks if the script is running with administrative privileges.
- `open_option1()`: Launches the `xTotenGeneric.exe` application.
- `open_option2()`: Opens the login page of `seumotora.contatto.com.br`.
- `open_option3()`: Opens the search page of `seumotora.contatto.com.br`.
- `open_option4()`: Opens the Detran SP points consultation page.
- `open_option5()`, `open_option6()`, `open_option7()`, `open_option9()`: Display a message indicating the option is under development.
- `open_option8()`: Opens the specified PDF document in fullscreen mode.
- `close_app()`: Closes the application.
- `close_other_windows()`: Closes any opened processes and returns to the main screen after a period of inactivity.
- `reset_inactivity_timer()`: Resets the inactivity timer based on user activity.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License.
```