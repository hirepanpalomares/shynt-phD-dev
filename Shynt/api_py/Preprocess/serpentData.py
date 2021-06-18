import math
import sys
import multiprocessing as mp

class SerpentOut(object):
    """
    
    """
    def __init__(self, outSerp):
        """
            The parameter outSerp is the  name of the res output file given by 
            serpent
        """
        
        self.__outFile = outSerp
        self.__filesData = {}
        totalFiles = len(self.__outFile)
        i = 1
        for file in self.__outFile:
            print("Processing file: %s ...... (%s/%s)" %(file,i,totalFiles))
            self.__readFile(file)
            print("  Ok")
            i += 1

    def __readFile(self, res_m):

        burn_step = 0
        burn = 0.0
        burn_time = 0.0
        self.__filesData[res_m] = {}
        self.__filesData[res_m][burn_time] = {}
        self.__filesData[res_m][burn_time]["XS"] = {}
        f = open(res_m, 'r')
        u_name = ''
        for line in f:
            if line.startswith('BURN_STEP'):

                burn_step = int(line.split()[4])
                burn = float(f.readline().split()[6])
                burn_time = float(f.readline().split()[4])
                #print(burn_time)
                if burn_time not in self.__filesData[res_m]:
                    self.__filesData[res_m][burn_time] = {}
                    self.__filesData[res_m][burn_time]["XS"] = {}

            if line.startswith('GC_UNIVERSE_NAME'):
                u_name = line.split()[5].replace("'", "")
                self.__filesData[res_m][burn_time]["XS"][u_name] = {}
                self.__filesData[res_m][burn_time]["XS"][u_name]["total"] = {}
                self.__filesData[res_m][burn_time]["XS"][u_name]["flux"] = {}
                self.__filesData[res_m][burn_time]["XS"][u_name]["transport"] = {}
                self.__filesData[res_m][burn_time]["XS"][u_name]["capture"] = {}
                self.__filesData[res_m][burn_time]["XS"][u_name]["fission"] = {}
                self.__filesData[res_m][burn_time]["XS"][u_name]["nu_fission"] = {}
                self.__filesData[res_m][burn_time]["XS"][u_name]["absorption"] = {}
                self.__filesData[res_m][burn_time]["XS"][u_name]["chi_total"] = {}
                self.__filesData[res_m][burn_time]["XS"][u_name]["chi_prompt"] = {}
                self.__filesData[res_m][burn_time]["XS"][u_name]["chi_delay"] = {}
                self.__filesData[res_m][burn_time]["XS"][u_name]["scattering_P0"] = {}
                self.__filesData[res_m][burn_time]["XS"][u_name]["scattering_P1"] = {}
                self.__filesData[res_m][burn_time]["XS"][u_name]["scattering_P2"] = {}
                self.__filesData[res_m][burn_time]["XS"][u_name]["scattering_P3"] = {}
                self.__filesData[res_m][burn_time]["XS"][u_name]["scattering_P4"] = {}
                self.__filesData[res_m][burn_time]["XS"][u_name]["scattering_P5"] = {}
                self.__filesData[res_m][burn_time]["XS"][u_name]["scattering_P6"] = {}
                self.__filesData[res_m][burn_time]["XS"][u_name]["scattering_P7"] = {}
            if line.startswith('ABS_KEFF'):
                k = [float(v) for v in line.split()[6:8]]
                #print(k)
                self.__filesData[res_m][burn_time]["keff"] = k
            if line.startswith('INF_TOT'):
                array = [float(v) for v in line.split()[6:-1]]
                separated = self.__separate_XSfromSTD(array)
                xs = separated[0]
                #print(xs)
                std = separated[1]
                self.__filesData[res_m][burn_time]["XS"][u_name]["total"] = {"xs": xs, "std":std}
            if line.startswith('INF_TRANSPXS'):
                array = [float(v) for v in line.split()[6:-1]]
                separated = self.__separate_XSfromSTD(array)
                xs = separated[0]
                #print(xs)
                std = separated[1]
                self.__filesData[res_m][burn_time]["XS"][u_name]["transport"] = {"xs": xs, "std":std}
            if line.startswith('INF_CAPT'):
                array = [float(v) for v in line.split()[6:-1]]
                separated = self.__separate_XSfromSTD(array)
                xs = separated[0]
                std = separated[1]
                self.__filesData[res_m][burn_time]["XS"][u_name]["capture"] = {"xs": xs, "std":std}
            if line.startswith('INF_FLX '):
                array = [float(v) for v in line.split()[6:-1]]
                separated = self.__separate_XSfromSTD(array)
                xs = separated[0]
                std = separated[1]
                self.__filesData[res_m][burn_time]["XS"][u_name]["flux"] = {"xs": xs, "std":std}
            if line.startswith('INF_FISS '):
                array = [float(v) for v in line.split()[6:-1]]
                separated = self.__separate_XSfromSTD(array)
                xs = separated[0]
                std = separated[1]
                self.__filesData[res_m][burn_time]["XS"][u_name]["fission"] = {"xs": xs, "std":std}
            if line.startswith('INF_NSF'):
                array = [float(v) for v in line.split()[6:-1]]
                separated = self.__separate_XSfromSTD(array)
                xs = separated[0]
                std = separated[1]
                self.__filesData[res_m][burn_time]["XS"][u_name]["nu_fission"] = {"xs": xs, "std":std}
            if line.startswith('INF_ABS'):
                array = [float(v) for v in line.split()[6:-1]]
                separated = self.__separate_XSfromSTD(array)
                xs = separated[0]
                std = separated[1]
                self.__filesData[res_m][burn_time]["XS"][u_name]["absorption"] = {"xs": xs, "std":std}
            if line.startswith('INF_CHIT'):
                array = [float(v) for v in line.split()[6:-1]]
                separated = self.__separate_XSfromSTD(array)
                xs = separated[0]
                std = separated[1]
                self.__filesData[res_m][burn_time]["XS"][u_name]["chi_total"] = {"xs": xs, "std":std}
            if line.startswith('INF_CHIP'):
                array = [float(v) for v in line.split()[6:-1]]
                separated = self.__separate_XSfromSTD(array)
                xs = separated[0]
                std = separated[1]
                self.__filesData[res_m][burn_time]["XS"][u_name]["chi_prompt"] = {"xs": xs, "std":std}
            if line.startswith('INF_CHID'):
                array = [float(v) for v in line.split()[6:-1]]
                separated = self.__separate_XSfromSTD(array)
                xs = separated[0]
                std = separated[1]
                self.__filesData[res_m][burn_time]["XS"][u_name]["chi_delay"] = {"xs": xs, "std":std}
            if line.startswith('INF_S0'):
                array = [float(v) for v in line.split()[6:-1]]
                separated = self.__separate_XSfromSTD(array, matrix=1)
                xs = separated[0]
                std = separated[1]
                self.__filesData[res_m][burn_time]["XS"][u_name]["scattering_P0"] = {"xs": xs, "std":std}
            if line.startswith('INF_S1'):
                array = [float(v) for v in line.split()[6:-1]]
                separated = self.__separate_XSfromSTD(array, matrix=1)
                xs = separated[0]
                std = separated[1]
                self.__filesData[res_m][burn_time]["XS"][u_name]["scattering_P1"] = {"xs": xs, "std":std}
            if line.startswith('INF_S2'):
                array = [float(v) for v in line.split()[6:-1]]
                separated = self.__separate_XSfromSTD(array, matrix=1)
                xs = separated[0]
                std = separated[1]
                self.__filesData[res_m][burn_time]["XS"][u_name]["scattering_P2"] = {"xs": xs, "std":std}
            if line.startswith('INF_S3'):
                array = [float(v) for v in line.split()[6:-1]]
                separated = self.__separate_XSfromSTD(array, matrix=1)
                xs = separated[0]
                std = separated[1]
                self.__filesData[res_m][burn_time]["XS"][u_name]["scattering_P3"] = {"xs": xs, "std":std}
            if line.startswith('INF_S4'):
                array = [float(v) for v in line.split()[6:-1]]
                separated = self.__separate_XSfromSTD(array, matrix=1)
                xs = separated[0]
                std = separated[1]
                self.__filesData[res_m][burn_time]["XS"][u_name]["scattering_P4"] = {"xs": xs, "std":std}
            if line.startswith('INF_S5'):
                array = [float(v) for v in line.split()[6:-1]]
                separated = self.__separate_XSfromSTD(array, matrix=1)
                xs = separated[0]
                std = separated[1]
                self.__filesData[res_m][burn_time]["XS"][u_name]["scattering_P5"] = {"xs": xs, "std":std}
            if line.startswith('INF_S6'):
                array = [float(v) for v in line.split()[6:-1]]
                separated = self.__separate_XSfromSTD(array, matrix=1)
                xs = separated[0]
                std = separated[1]
                self.__filesData[res_m][burn_time]["XS"][u_name]["scattering_P6"] = {"xs": xs, "std":std}
            if line.startswith('INF_S7'):
                array = [float(v) for v in line.split()[6:-1]]
                separated = self.__separate_XSfromSTD(array, matrix=1)
                xs = separated[0]
                std = separated[1]
                self.__filesData[res_m][burn_time]["XS"][u_name]["scattering_P7"] = {"xs": xs, "std":std}
        #print("Memory occupied: ", sys.getsizeof(self.__filesData))
        f.close()

    def __separate_XSfromSTD(self, array, matrix=0):
        if matrix:
            xs_vec = []
            std_vec = []
            for i in range(len(array)):
                if i%2 == 0:
                    xs_vec.append(array[i])
                else:
                    std_vec.append(array[i])
            vec_len = math.sqrt(len(xs_vec))
            band_xs = []
            band_std = []
            xs_mat = []
            std_mat = []
            for v in range(len(xs_vec)):
                band_xs.append(xs_vec[v])
                band_std.append(std_vec[v])
                if len(band_xs) == vec_len:
                    xs_mat.append(band_xs)
                    std_mat.append(band_std)
                    band_xs = []
                    band_std = []
            return [xs_mat, std_mat]
        else:
            xs = []
            std = []
            for i in range(len(array)):
                if i%2 == 0:
                    xs.append(array[i])
                else:
                    std.append(array[i])
            return [xs, std]

    def getData(self):
        return self.__filesData

    def getBurnSteps(self):
        steps = list(self.__filesData[self.__outFile[0]].keys())
        sortedSteps = sorted(steps)
        return sortedSteps

    def getFluxCollapsed(self, universe, file):
        steps = list(self.__filesData[self.__outFile[0]].keys())
        sortedSteps = sorted(steps)
        fluxArray = []
        for s in sortedSteps:
            fluxMultigroup = self.__filesData[file][s]["XS"][universe]['flux']['xs']
            fluxArray.append(sum(fluxMultigroup))
        return fluxArray

    def getFlux(self, universe='', file=''):
        steps = list(self.__filesData[self.__outFile[0]].keys())
        sortedSteps = sorted(steps)
        fluxArray = {}
        for s in range(len(sortedSteps)):
            if universe != '':
                fluxMultigroup = self.__filesData[self.__outFile[0]][sortedSteps[s]]["XS"][universe]['flux']['xs']
                fluxArray[s]  = fluxMultigroup
            else:
                fluxArray[s] = {}
                for uni, flux in self.__filesData[self.__outFile[0]][sortedSteps[s]]["XS"].items():
                    fluxArray[s][uni] = flux['flux']['xs']
        return fluxArray

    def getUniverses(self):
        pass

    def getTotalParams(self):
        pass

    def getParam_xs(self, param, burn, uni, file):
        return self.__filesData[file][burn]["XS"][uni][param]['xs']

    def getParam_std(self, param, burn, uni):
        pass
