import Shynt
from assembly import model_universe


# Generating file
serp_root_input_file = Shynt.file_generator.generate_root_serpent_file(model_universe)


# Then run the file and the reference flux will be in a detector output file