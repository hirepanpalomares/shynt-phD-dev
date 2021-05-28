def read_file(detector_names, file_path, absolute_path):
    data_detector = {}
    with open(absolute_path + file_path, 'r') as file:
        for line in file:
            splitted = line.split()
            if line.startswith('DET') and splitted[0] in detector_names:
                det_name = splitted[0]
                next_line = file.readline().split()
                counts = float(next_line[-1])
                data_detector[det_name] = counts
    return data_detector