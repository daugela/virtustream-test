activate_this = '/home/andrius/www-virtustream/djenv/bin/activate_this.py'
with open(activate_this) as file_:
	exec(file_.read(), dict(__file__=activate_this))

import sys

sys.path.append('/home/andrius/www-virtustream')
from pythoncode import app as application