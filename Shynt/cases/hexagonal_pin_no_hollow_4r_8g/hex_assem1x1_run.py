from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

import Shynt


from Shynt.cases.hexagonal_pin_no_hollow_4r_8g.hex_pin import root_universe

Shynt.run(root_universe)
