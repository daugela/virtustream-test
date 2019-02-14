## Virtustream test

This is a minimal Flask app with Fibonacci numbers API functionality.
For demo purposes plese see [here](http://46.101.202.234:8000)

## Setup on a mac or some other unix based machine

Clone this repo

`git clone https://github.com/daugela/virtustream-test.git`

Go inside

`cd virtustream-test`

Download prerequisites and prepare Python environment

`wget https://bootstrap.pypa.io/get-pip.py`
`sudo python3 get-pip.py`
`sudo pip3 install virtualenv`

Create virtual environment directory (djenv)
`virtualenv -p python3 djenv`

Activate environment
`source djenv/bin/activate`

Install dependencies
`pip install -r requirements.txt`
