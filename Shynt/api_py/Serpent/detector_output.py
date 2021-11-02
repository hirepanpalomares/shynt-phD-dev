
def read_detector_file(fname):
    """
        Helper to extract the data from the detectors

        -----------
        returns:
            - dectors data in a dictionary
        Structure of the dictionary

        dictionary = {
            "detector_name": {
                "neutrons": [
                    (counts_g1, std_dev_g1), 
                    ..., (counts_gN, std_dev_gN)
                ],
                "energy": [
                    (energy_bin_1_low, energy_bin_1_high), 
                    ..., 
                    (energy_bin_N_low, energy_bin_N_high)
                ],
            },
        }
    """
    data = {}
    with open(fname, "r") as f:
        counts = False
        energy = False
        for line in f:
            line_sp = line.split()
            if line.startswith("DET"):
                det_name = line_sp[0].split("DET")[1]
                if det_name[-1] == "E":
                    counts = False
                    energy = True
                    det_name = det_name[:-1]
                else:
                    data[det_name] = {
                        "neutrons": [],
                        "energy": []
                    }
                    counts = True
                    energy = False
            if counts and len(line_sp) == 12:
                g = int(line_sp[0]) - 1
                neutrons = float(line_sp[-2])
                std = float(line_sp[-1])
                data[det_name]["neutrons"].append((neutrons, std))
            if energy and len(line_sp) == 3 and line_sp[-1] != "[":
                g0 = float(line_sp[0])
                gf = float(line_sp[1])
                another_number = float(line_sp[2])
                data[det_name]["energy"].append((g0, gf))
    return data

