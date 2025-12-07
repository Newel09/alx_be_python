import os
import sys

# Make local imports work whether executed from repository root or this directory
sys.path.insert(0, os.path.dirname(__file__))

from main import main


if __name__ == "__main__":
    main()