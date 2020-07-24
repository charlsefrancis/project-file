from flask_frozen import Freezer
from myapp import append

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()