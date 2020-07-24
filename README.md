# project-file

Set up your dev environment

Before you build your Flask web app, you'll need to create a working directory for your project and install a few Python packages.
Create a working directory

    Open command line (Windows) or terminal (macOS/Linux). Then, create a working directory and sub directories for your project:

mkdir -p flask-cog-services/static/scripts && mkdir flask-cog-services/templates

Change to your project's working directory:

    cd flask-cog-services

Create and activate your virtual environment with virtualenv

Let's create a virtual environment for our Flask app using virtualenv. Using a virtual environment ensures that you have a clean environment to work from.

    In your working directory, run this command to create a virtual environment: macOS/Linux:

virtualenv venv --python=python3

We've explicitly declared that the virtual environment should use Python 3. This ensures that users with multiple Python installations are using the correct version.

Windows CMD / Windows Bash:

    virtualenv venv

    To keep things simple, we're naming your virtual environment venv.

    The commands to activate your virtual environment will vary depending on your platform/shell:
    Table 1
    Platform 	Shell 	Command
    macOS/Linux 	bash/zsh 	source venv/bin/activate
    Windows 	bash 	source venv/Scripts/activate
    	Command Line 	venv\Scripts\activate.bat
    	PowerShell 	venv\Scripts\Activate.ps1

    After running this command, your command line or terminal session should be prefaced with venv.

    You can deactivate the session at any time by typing this into the command line or terminal: deactivate.

Note

Python has extensive documentation for creating and managing virtual environments, see virtualenv.
Install requests

Requests is a popular module that is used to send HTTP 1.1 requests. There's no need to manually add query strings to your URLs, or to form-encode your POST data.

    To install requests, run:

    pip install requests

Note

If you'd like to learn more about requests, see Requests: HTTP for Humans.
Install and configure Flask

Next we need to install Flask. Flask handles the routing for our web app, and allows us to make server-to-server calls that hide our subscription keys from the end user.

    To install Flask, run:

pip install Flask

Let's make sure Flask was installed. Run:

flask --version

The version should be printed to terminal. Anything else means something went wrong.

To run the Flask app, you can either use the flask command or Python's -m switch with Flask. Before you can do that you need to tell your terminal which app to work with by exporting the FLASK_APP environment variable:

macOS/Linux:

export FLASK_APP=app.py

Windows:

set FLASK_APP=app.py
