import shapes  # this is OK

# "from . import shapes" is relative import, so NG in toplevel
# ImportError: attempted relative import with no known parent package
# see also: ../04relative-nested/app/config.py

config = shapes.Config(host="localhost", port=44444)
