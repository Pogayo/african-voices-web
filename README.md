# african-voices-web
Visit the African Voices website [here](https://www.africanvoices.tech).
## Installation
  * Install python 2.7 or newer
  * Create a virtual environment `python3 -m venv virtual_environment_name`
  * Activate the virtual environment `cd your_virtual_environment_name` and then `source bin/activate`
  * Install all dependencies needed by the project. Run the command `pip3 install -r requirements.txt` in the project root folder
  * Run make migrations and then migrate. `python manage.py makemigrations` and then `python manage.py migrate` to create the tables from models in the database
  * Run `python manage.py runserver` on the project root folder to run project on local machine
  
# System Requirements
For the project to work, you need to have festvox and its dependencies installed.
 1. Install prerequisites:
```
sudo apt-get install git build-essential libncurses5-dev sox wget
sudo apt-get install csh ffmpeg html2text
```
 2. Download and run [fest_build.sh](http://tts.speech.cs.cmu.edu/awb/11-492/homework/tts/fest_build.sh).
On your terminal run:
```
chmod +x festvox_setup.sh
./festvox_setup.sh
```
Learn more about [Festvox](https://github.com/festvox/festvox#installation)

# Want to create your own synthesizer?
Follow the instructions in [NewlangTech](https://github.com/neulab/newlang-tech/tree/main/speech-synthesis) to create your own synthesizer in simple steps.