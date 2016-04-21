## Article Search using DRF and DH with Whoosh 
Article search application using django-haystack + Whoosh + django-rest-farmework

##### Use virtual env, It is optional but better to use to avoid dependency conflicts [ Skip this step if already have virtual env ]
```
sudo pip install virtualenv
sudo pip install virtualenvwrapper
```
After it's installed, add the following lines to your shell's start-up file (.zshrc, .bashrc, .profile, etc).
```
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
```
Reload .bashrc file
```
source ~/.bashrc
```

##### Virtual env wrapper commands
1. **mkvirtualenv:** To create a new environment. Example: mkvirtualenv blog
2. **deactivate:** To get out/off your virtualenv. Example: deactivate
3. **workon:** To jump back on the virtualenv. Example: workon blog
4. **rmvirtualenv:** To remove the virtualenv. Example: rmvirtualenv blog

##### Install project prerequisites libraries

**Note:** If you are using virtual env, first activate it using **workon** command.

##### Install project requirements

```
pip install -r requirements.txt
```

##### Schema migration
```
python manage.py makemigrations
python manage.py migrate
```

##### Rebuild index
```
python manage.py rebuild_index
```
