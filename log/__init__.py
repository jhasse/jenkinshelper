"""Print colored messages"""

def info(text):
    """Print a blue message"""
    print("\x1b[1;34m{}\x1b[0m".format(text))
