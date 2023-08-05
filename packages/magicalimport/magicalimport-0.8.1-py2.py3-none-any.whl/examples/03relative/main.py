from magicalimport import import_symbol

config = import_symbol("./config.py:config", here=__file__)
print(config)

