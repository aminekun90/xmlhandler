#XML Handler

The XML handler can read and parse any xml file very efficiently in less than 1s for huge file using generators/iterators.

##Run the script

Make sure you have python 3.6 or above, pip 3 and virtualenv installed.

###Setup the environement

```bash
virtualenv .env
pip install -r requirements.txt
# for windows
.env/Script/activate.ps1
# for linux
.env/lib/activate
```

###Configuration

##Database
Edit the `run_me.ps1` for the SQL_ALCHEMY_URI



###Run the script

```bash
run_me.ps1
python start.py
```