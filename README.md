# ez.chat backend

The backend for ez.chat, built with either Flask or CherryPy

## Setup

This setup assumes `pip` is available and redirects to pip for Python 3, also assumes `python3` is in PATH and you have both Python 3 and pip (generally included with former) installed.

NOTE: If you have Python 3.3+, a module named `venv` is already provided with Python. You may skip installing virtualenv and proceed further.

(This assumes `virtualenv` is not already available in your Linux package repos. If so, then follow distribution specific installation methods.) To install `virtualenv`, run `pip install virtualenv` and confirm the installation with `python3 -m virtualenv --version`.

To setup a virtual environment, run `python3 -m virtualenv venv` (if using `venv`, run `python3 -m venv venv`) in the project directory.

Once done, run `\venv\Scripts\activate` in the command line to activate the virtual environment on Windows, or `source venv/bin/activate` on Linux. This will replace your `python` and `pip` executables for the current terminal with PATH and allow you to use these executables directly. When finished working, type `deactivate` on either platform to deactivate the environment (or close the terminal).

To install the necessary packages (CherryPy, Flake8, Pylint and Flask), run `pip install -r requirements.txt` and to save dependencies after installing a package, run `pip freeze > requirements.txt`.

VSCode will automatically detect the virtual environment and use packages inside the venv when using the Python extension. PyCharm may or may not do the same.
