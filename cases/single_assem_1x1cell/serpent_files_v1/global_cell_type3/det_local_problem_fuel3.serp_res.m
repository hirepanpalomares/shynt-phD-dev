
% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.32' ;
COMPILE_DATE              (idx, [1: 20])  = 'Mar 29 2021 14:59:10' ;
DEBUG                     (idx, 1)        = 0 ;
TITLE                     (idx, [1:  8])  = 'Untitled' ;
CONFIDENTIAL_DATA         (idx, 1)        = 0 ;
INPUT_FILE_NAME           (idx, [1:145])  = '/home/hirepan/Documents/chalmers/Project/codes/Shynt/repo/cases/single_assem_1x1cell/serpent_files/global_cell_type3/det_local_problem_fuel3.serp' ;
WORKING_DIRECTORY         (idx, [1: 84])  = '/home/hirepan/Documents/chalmers/Project/codes/Shynt/repo/cases/single_assem_1x1cell' ;
HOSTNAME                  (idx, [1:  4])  = 'thor' ;
CPU_TYPE                  (idx, [1: 40])  = 'Intel(R) Core(TM) i9-10900 CPU @ 2.80GHz' ;
CPU_MHZ                   (idx, 1)        = 236.0 ;
START_DATE                (idx, [1: 24])  = 'Thu Mar 10 11:43:43 2022' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Mar 10 11:44:11 2022' ;

% Run parameters:

POP                       (idx, 1)        = 2000 ;
CYCLES                    (idx, 1)        = 500 ;
SKIP                      (idx, 1)        = 50 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1474468046 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 1 ;
B1_CALCULATION            (idx, [1:  3])  = [ 0 0 0 ];
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;

CRIT_SPEC_MODE            (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
DOUBLE_INDEXING           (idx, 1)        = 0 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 18 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  18]) = [  9.54432E-01  9.22259E-01  9.49462E-01  9.45636E-01  9.46764E-01  9.49168E-01  9.52944E-01  9.56312E-01  9.63358E-01  9.62965E-01  1.09256E+00  9.48595E-01  1.22756E+00  1.25993E+00  9.53974E-01  1.03269E+00  9.52225E-01  1.02917E+00  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;
OMP_SHARED_QUEUE_LIM      (idx, 1)        = 0 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 71])  = '/home/hirepan/neutron_codes/Serpent2/xsdata/jeff311/sss_jeff311u.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1:  3])  = 'N/A' ;
SFY_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;
NFY_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;
BRA_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:   4]) = [  5.00000E-02 1.3E-09  0.00000E+00 0.0E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  2.21693E-03 0.00295  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.97783E-01 6.6E-06  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  8.30396E-01 8.9E-05  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  8.34580E-01 0.00011  0.00000E+00 0.0E+00 ];
AVG_TRACKING_LOOPS        (idx, [1:   8]) = [  4.89024E+00 0.00089  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  2.69137E+01 0.00056  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  2.69137E+01 0.00056  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  5.33454E+00 0.00078  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  4.37381E+01 0.00053  0.00000E+00 0.0E+00 ];
LOST_PARTICLES            (idx, 1)        = 0 ;

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 500 ;
SIMULATED_HISTORIES       (idx, 1)        = 1000610 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  2.00122E+03 0.00149 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  2.00122E+03 0.00149 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  8.26096E+00 ;
RUNNING_TIME              (idx, 1)        =  4.71517E-01 ;
INIT_TIME                 (idx, [1:  2])  = [  1.18167E-02  1.18167E-02 ];
PROCESS_TIME              (idx, [1:  2])  = [  1.16666E-04  1.16666E-04 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  4.59517E-01  4.59517E-01  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  4.71417E-01  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 17.51998 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  1.79618E+01 0.00144 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  9.51822E-01 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 64024.21 ;
ALLOC_MEMSIZE             (idx, 1)        = 390.08;
MEMSIZE                   (idx, 1)        = 203.14;
XS_MEMSIZE                (idx, 1)        = 74.10;
MAT_MEMSIZE               (idx, 1)        = 6.90;
RES_MEMSIZE               (idx, 1)        = 1.55;
IFC_MEMSIZE               (idx, 1)        = 0.00;
MISC_MEMSIZE              (idx, 1)        = 120.59;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 186.94;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 4 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 81823 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Unresolved resonance probability table sampling:

URES_DILU_CUT             (idx, 1)        =  1.00000E-09 ;
URES_EMIN                 (idx, 1)        =  1.00000E+37 ;
URES_EMAX                 (idx, 1)        = -1.00000E+37 ;
URES_AVAIL                (idx, 1)        = 2 ;
URES_USED                 (idx, 1)        = 0 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 6 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 6 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 131 ;
TOT_TRANSMU_REA           (idx, 1)        = 0 ;

% Neutron physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 0 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_PREPROCESSOR      (idx, 1)        = 0 ;
TMS_MODE                  (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Energy deposition:

EDEP_MODE                 (idx, 1)        = 0 ;
EDEP_DELAYED              (idx, 1)        = 1 ;
EDEP_KEFF_CORR            (idx, 1)        = 1 ;
EDEP_LOCAL_EGD            (idx, 1)        = 0 ;
EDEP_COMP                 (idx, [1:  9])  = [ 0 0 0 0 0 0 0 0 0 ];
EDEP_CAPT_E               (idx, 1)        =  0.00000E+00 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  0.00000E+00 ;
TOT_DECAY_HEAT            (idx, 1)        =  0.00000E+00 ;
TOT_SF_RATE               (idx, 1)        =  0.00000E+00 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  0.00000E+00 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  0.00000E+00 ;
INHALATION_TOXICITY       (idx, 1)        =  0.00000E+00 ;
INGESTION_TOXICITY        (idx, 1)        =  0.00000E+00 ;
ACTINIDE_INH_TOX          (idx, 1)        =  0.00000E+00 ;
ACTINIDE_ING_TOX          (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_INH_TOX   (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_ING_TOX   (idx, 1)        =  0.00000E+00 ;
SR90_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
TE132_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
I131_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
I132_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
CS134_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
CS137_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
PHOTON_DECAY_SOURCE       (idx, 1)        =  0.00000E+00 ;
NEUTRON_DECAY_SOURCE      (idx, 1)        =  0.00000E+00 ;
ALPHA_DECAY_SOURCE        (idx, 1)        =  0.00000E+00 ;
ELECTRON_DECAY_SOURCE     (idx, 1)        =  0.00000E+00 ;

% Normalization coefficient:

NORM_COEF                 (idx, [1:   4]) = [  5.00005E-04 0.00088  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  6.54393E-01 0.00217 ];
U235_FISS                 (idx, [1:   4]) = [  4.54877E-01 0.00123  9.15167E-01 0.00044 ];
U238_FISS                 (idx, [1:   4]) = [  4.21828E-02 0.00501  8.48329E-02 0.00471 ];
U235_CAPT                 (idx, [1:   4]) = [  1.06943E-01 0.00297  2.11836E-01 0.00268 ];
U238_CAPT                 (idx, [1:   4]) = [  3.67419E-01 0.00174  7.27682E-01 0.00087 ];

% Neutron balance (particles/weight):

BALA_SRC_NEUTRON_SRC     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_FISS    (idx, [1:  2])  = [ 1000610 1.00000E+06 ];
BALA_SRC_NEUTRON_NXN     (idx, [1:  2])  = [ 0 1.94557E+03 ];
BALA_SRC_NEUTRON_VR      (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_TOT     (idx, [1:  2])  = [ 1000610 1.00195E+06 ];

BALA_LOSS_NEUTRON_CAPT    (idx, [1:  2])  = [ 504152 5.04850E+05 ];
BALA_LOSS_NEUTRON_FISS    (idx, [1:  2])  = [ 496458 4.97096E+05 ];
BALA_LOSS_NEUTRON_LEAK    (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_CUT     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_ERR     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_TOT     (idx, [1:  2])  = [ 1000610 1.00195E+06 ];

BALA_NEUTRON_DIFF         (idx, [1:  2])  = [ 0 2.09548E-09 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.60978E-11 0.00054 ];
TOT_POWDENS               (idx, [1:   2]) = [  2.96744E-15 0.00054 ];
TOT_GENRATE               (idx, [1:   2]) = [  1.22488E+00 0.00054 ];
TOT_FISSRATE              (idx, [1:   2]) = [  4.95962E-01 0.00054 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  5.04038E-01 0.00053 ];
TOT_ABSRATE               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_SRCRATE               (idx, [1:   2]) = [  1.00001E+00 0.00088 ];
TOT_FLUX                  (idx, [1:   2]) = [  5.65305E+01 0.00068 ];
TOT_PHOTON_PRODRATE       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  2.69599E+01 0.00056 ];
INI_FMASS                 (idx, 1)        =  5.42481E-03 ;
TOT_FMASS                 (idx, 1)        =  5.42481E-03 ;

% Six-factor formula:

SIX_FF_ETA                (idx, [1:   2]) = [  1.78074E+00 0.00087 ];
SIX_FF_F                  (idx, [1:   2]) = [  9.56415E-01 0.00031 ];
SIX_FF_P                  (idx, [1:   2]) = [  5.23727E-01 0.00098 ];
SIX_FF_EPSILON            (idx, [1:   2]) = [  1.37711E+00 0.00089 ];
SIX_FF_LF                 (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
SIX_FF_LT                 (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
SIX_FF_KINF               (idx, [1:   2]) = [  1.22786E+00 0.00101 ];
SIX_FF_KEFF               (idx, [1:   2]) = [  1.22786E+00 0.00101 ];

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.46971E+00 3.3E-05 ];
FISSE                     (idx, [1:   2]) = [  2.02585E+02 2.9E-06 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.22759E+00 0.00103  1.21880E+00 0.00101  9.06067E-03 0.01656 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.22725E+00 0.00054 ];
COL_KEFF                  (idx, [1:   2]) = [  1.22545E+00 0.00119 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.22725E+00 0.00054 ];
ABS_KINF                  (idx, [1:   2]) = [  1.22725E+00 0.00054 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% ALF (Average lethargy of neutrons causing fission):
% Based on E0 = 2.000000E+01 MeV

ANA_ALF                   (idx, [1:   2]) = [  1.66945E+01 0.00047 ];
IMP_ALF                   (idx, [1:   2]) = [  1.67041E+01 0.00023 ];

% EALF (Energy corresponding to average lethargy of neutrons causing fission):

ANA_EALF                  (idx, [1:   2]) = [  1.14144E-06 0.00797 ];
IMP_EALF                  (idx, [1:   2]) = [  1.11733E-06 0.00393 ];

% AFGE (Average energy of neutrons causing fission):

ANA_AFGE                  (idx, [1:   2]) = [  2.85042E-01 0.00526 ];
IMP_AFGE                  (idx, [1:   2]) = [  2.82178E-01 0.00225 ];

% Forward-weighted delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
FWD_ANA_BETA_ZERO         (idx, [1:  18]) = [  6.26139E-03 0.01143  1.72099E-04 0.06959  8.65520E-04 0.03124  4.99260E-04 0.04207  1.16445E-03 0.02593  2.01078E-03 0.02006  7.32091E-04 0.03436  5.95597E-04 0.03889  2.21601E-04 0.06363 ];
FWD_ANA_LAMBDA            (idx, [1:  18]) = [  4.86763E-01 0.01873  4.31348E-03 0.06155  2.45006E-02 0.01761  2.93418E-02 0.03001  1.25858E-01 0.01070  2.89543E-01 0.00450  5.57184E-01 0.01983  1.23262E+00 0.02557  1.42184E+00 0.05483 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  18]) = [  7.60761E-03 0.01711  2.11709E-04 0.10243  1.00972E-03 0.04743  6.73982E-04 0.06356  1.47641E-03 0.03964  2.40067E-03 0.03082  9.28012E-04 0.05000  6.78589E-04 0.05688  2.28520E-04 0.10042 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  18]) = [  4.61417E-01 0.02626  1.24667E-02 0.0E+00  2.82917E-02 0.0E+00  4.25244E-02 6.2E-09  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 4.9E-09  3.55460E+00 0.0E+00 ];

% Adjoint weighted time constants using Nauchi's method:

IFP_CHAIN_LENGTH          (idx, 1)        = 15 ;
ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  2.07183E-05 0.00232  2.07002E-05 0.00234  2.28609E-05 0.02338 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  2.54200E-05 0.00208  2.53979E-05 0.00209  2.80431E-05 0.02331 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  18]) = [  7.38957E-03 0.01669  1.84748E-04 0.10594  1.03575E-03 0.04309  6.19015E-04 0.05795  1.33632E-03 0.03817  2.40403E-03 0.02933  8.86487E-04 0.04715  7.04103E-04 0.05546  2.19119E-04 0.09561 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  18]) = [  4.65467E-01 0.02505  1.24667E-02 0.0E+00  2.82917E-02 3.0E-09  4.25244E-02 8.1E-09  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 5.6E-09  3.55460E+00 5.1E-09 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  2.07589E-05 0.00508  2.07509E-05 0.00511  1.63495E-05 0.05030 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  2.54692E-05 0.00495  2.54589E-05 0.00497  2.00831E-05 0.05033 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  18]) = [  7.41486E-03 0.04926  2.49587E-04 0.30482  1.09048E-03 0.12040  6.68125E-04 0.16842  1.39006E-03 0.12326  2.31853E-03 0.08205  7.85375E-04 0.14424  6.87019E-04 0.18216  2.25690E-04 0.28011 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  18]) = [  4.19716E-01 0.06598  1.24667E-02 5.4E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 3.2E-09  2.92467E-01 6.0E-09  6.66488E-01 5.3E-09  1.63478E+00 0.0E+00  3.55460E+00 0.0E+00 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  18]) = [  7.37009E-03 0.04754  2.20901E-04 0.30268  1.07952E-03 0.11672  6.82108E-04 0.16758  1.39389E-03 0.11957  2.34346E-03 0.07837  7.85940E-04 0.14098  6.57826E-04 0.17056  2.06451E-04 0.27709 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  18]) = [  4.19040E-01 0.06394  1.24667E-02 0.0E+00  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 3.2E-09  2.92467E-01 6.1E-09  6.66488E-01 5.5E-09  1.63478E+00 0.0E+00  3.55460E+00 0.0E+00 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -3.61295E+02 0.04928 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  2.07801E-05 0.00138 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  2.54965E-05 0.00098 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  7.41226E-03 0.00985 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -3.57241E+02 0.01007 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  3.26571E-07 0.00121 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  4.19479E-06 0.00103  4.19481E-06 0.00104  4.20135E-06 0.01168 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.01585E-05 0.00138  3.01556E-05 0.00139  3.02696E-05 0.01536 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.24314E-01 0.00098  5.23322E-01 0.00098  7.30824E-01 0.02029 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.19923E+01 0.02648 ];
ANA_MEAN_NCOL             (idx, [1:   4]) = [  2.69137E+01 0.00056  3.02741E+01 0.00076 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  1])  = '0' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  2.00000E+01  6.06550E+00  3.67900E+00  2.23100E+00  1.35300E+00  8.21000E-01  5.00000E-01  3.02500E-01  1.83000E-01  1.11000E-01  6.74300E-02  4.08500E-02  2.47800E-02  1.50300E-02  9.11800E-03  5.50000E-03  3.51910E-03  2.23945E-03  1.42510E-03  9.06898E-04  3.67262E-04  1.48728E-04  7.55014E-05  4.80520E-05  2.77000E-05  1.59680E-05  9.87700E-06  4.00000E-06  3.30000E-06  2.60000E-06  2.10000E-06  1.85500E-06  1.50000E-06  1.30000E-06  1.15000E-06  1.12300E-06  1.09700E-06  1.07100E-06  1.04500E-06  1.02000E-06  9.96000E-07  9.72000E-07  9.50000E-07  9.10000E-07  8.50000E-07  7.80000E-07  6.25000E-07  5.00000E-07  4.00000E-07  3.50000E-07  3.20000E-07  3.00000E-07  2.80000E-07  2.50000E-07  2.20000E-07  1.80000E-07  1.40000E-07  1.00000E-07  8.00000E-08  6.70000E-08  5.80000E-08  5.00000E-08  4.20000E-08  3.50000E-08  3.00000E-08  2.50000E-08  2.00000E-08  1.50000E-08  1.00000E-08  5.00000E-09  1.00000E-11 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Micro-group spectrum:

INF_MICRO_FLX             (idx, [1: 140]) = [  1.67845E+04 0.00721  7.01461E+04 0.00312  1.48096E+05 0.00174  1.55949E+05 0.00150  1.49464E+05 0.00113  1.80442E+05 0.00118  1.21837E+05 0.00147  1.13408E+05 0.00164  8.59654E+04 0.00120  7.00996E+04 0.00130  6.06398E+04 0.00163  5.42089E+04 0.00181  4.98546E+04 0.00178  4.75422E+04 0.00155  4.60980E+04 0.00208  3.95520E+04 0.00148  3.91284E+04 0.00167  3.83699E+04 0.00203  3.74251E+04 0.00232  7.21677E+04 0.00129  6.86083E+04 0.00154  4.83311E+04 0.00134  3.06386E+04 0.00229  3.43165E+04 0.00170  3.15018E+04 0.00202  2.89661E+04 0.00222  4.46559E+04 0.00166  1.03925E+04 0.00361  1.31124E+04 0.00257  1.19461E+04 0.00403  6.86077E+03 0.00379  1.20069E+04 0.00374  8.12449E+03 0.00356  6.85431E+03 0.00382  1.28666E+03 0.00928  1.29791E+03 0.00720  1.32859E+03 0.00778  1.36515E+03 0.00751  1.35503E+03 0.00665  1.31038E+03 0.00860  1.39338E+03 0.00826  1.28419E+03 0.00743  2.45430E+03 0.00628  3.92264E+03 0.00424  4.97696E+03 0.00501  1.30698E+04 0.00375  1.35156E+04 0.00217  1.42089E+04 0.00214  9.03152E+03 0.00319  6.36153E+03 0.00412  4.72990E+03 0.00402  5.35748E+03 0.00414  9.55901E+03 0.00252  1.19563E+04 0.00306  2.12021E+04 0.00245  2.98037E+04 0.00232  4.07282E+04 0.00271  2.45080E+04 0.00267  1.69531E+04 0.00233  1.18699E+04 0.00226  1.04907E+04 0.00314  1.01250E+04 0.00302  8.30228E+03 0.00295  5.56108E+03 0.00250  5.07487E+03 0.00257  4.44253E+03 0.00330  3.70184E+03 0.00386  2.89447E+03 0.00321  1.91288E+03 0.00487  6.68650E+02 0.00548 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.22544E+00 0.00122 ];

% Flux spectra in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  4.97137E+01 0.00077  6.82388E+00 0.00109 ];
INF_FISS_FLX              (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  4.13463E-01 0.00019  9.39361E-01 0.00021 ];
INF_CAPT                  (idx, [1:   4]) = [  6.97560E-03 0.00104  2.30655E-02 0.00063 ];
INF_ABS                   (idx, [1:   4]) = [  9.60429E-03 0.00090  7.66286E-02 0.00075 ];
INF_FISS                  (idx, [1:   4]) = [  2.62869E-03 0.00082  5.35631E-02 0.00080 ];
INF_NSF                   (idx, [1:   4]) = [  6.73828E-03 0.00081  1.30490E-01 0.00080 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.56336E+00 9.9E-05  2.43620E+00 0.0E+00 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.03467E+02 5.9E-06  2.02270E+02 2.7E-09 ];
INF_INVV                  (idx, [1:   4]) = [  5.38722E-08 0.00110  2.31343E-06 0.00028 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  4.03843E-01 0.00020  8.62610E-01 0.00030 ];
INF_SCATT1                (idx, [1:   4]) = [  1.68490E-01 0.00037  2.23942E-01 0.00080 ];
INF_SCATT2                (idx, [1:   4]) = [  6.66844E-02 0.00057  5.69777E-02 0.00292 ];
INF_SCATT3                (idx, [1:   4]) = [  5.99180E-03 0.00700  1.72599E-02 0.00702 ];
INF_SCATT4                (idx, [1:   4]) = [ -6.22808E-03 0.00473 -3.68358E-03 0.03636 ];
INF_SCATT5                (idx, [1:   4]) = [  6.43834E-04 0.04260  2.95994E-03 0.04491 ];
INF_SCATT6                (idx, [1:   4]) = [  3.76028E-03 0.00699 -8.17705E-03 0.01175 ];
INF_SCATT7                (idx, [1:   4]) = [  6.14885E-04 0.03986 -2.27366E-04 0.39921 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  4.03882E-01 0.00020  8.62610E-01 0.00030 ];
INF_SCATTP1               (idx, [1:   4]) = [  1.68492E-01 0.00037  2.23942E-01 0.00080 ];
INF_SCATTP2               (idx, [1:   4]) = [  6.66842E-02 0.00057  5.69777E-02 0.00292 ];
INF_SCATTP3               (idx, [1:   4]) = [  5.99138E-03 0.00701  1.72599E-02 0.00702 ];
INF_SCATTP4               (idx, [1:   4]) = [ -6.22746E-03 0.00473 -3.68358E-03 0.03636 ];
INF_SCATTP5               (idx, [1:   4]) = [  6.43831E-04 0.04260  2.95994E-03 0.04491 ];
INF_SCATTP6               (idx, [1:   4]) = [  3.76001E-03 0.00700 -8.17705E-03 0.01175 ];
INF_SCATTP7               (idx, [1:   4]) = [  6.14764E-04 0.03990 -2.27366E-04 0.39921 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  1.85054E-01 0.00064  6.38780E-01 0.00044 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.80130E+00 0.00064  5.21830E-01 0.00044 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  9.56516E-03 0.00089  7.66286E-02 0.00075 ];
INF_REMXS                 (idx, [1:   4]) = [  2.03741E-02 0.00049  7.83500E-02 0.00123 ];

% Poison cross sections:

INF_I135_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_XE135_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM147_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM148_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM148M_YIELD          (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM149_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SM149_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_I135_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_XE135_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM147_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM148_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM148M_MICRO_ABS      (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM149_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SM149_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_XE135_MACRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SM149_MACRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Poison decay constants:

PM147_LAMBDA              (idx, 1)        =  0.00000E+00 ;
PM148_LAMBDA              (idx, 1)        =  0.00000E+00 ;
PM148M_LAMBDA             (idx, 1)        =  0.00000E+00 ;
PM149_LAMBDA              (idx, 1)        =  0.00000E+00 ;
I135_LAMBDA               (idx, 1)        =  0.00000E+00 ;
XE135_LAMBDA              (idx, 1)        =  0.00000E+00 ;
XE135M_LAMBDA             (idx, 1)        =  0.00000E+00 ;
I135_BR                   (idx, 1)        =  0.00000E+00 ;

% Fission spectra:

INF_CHIT                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_CHIP                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_CHID                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Scattering matrixes:

INF_S0                    (idx, [1:   8]) = [  3.93089E-01 0.00020  1.07544E-02 0.00092  1.59932E-03 0.01049  8.61011E-01 0.00030 ];
INF_S1                    (idx, [1:   8]) = [  1.65427E-01 0.00037  3.06325E-03 0.00181  5.39822E-04 0.01791  2.23402E-01 0.00081 ];
INF_S2                    (idx, [1:   8]) = [  6.76279E-02 0.00057 -9.43496E-04 0.00540  2.85632E-04 0.02608  5.66921E-02 0.00294 ];
INF_S3                    (idx, [1:   8]) = [  7.08965E-03 0.00582 -1.09785E-03 0.00412  1.06081E-04 0.07222  1.71538E-02 0.00710 ];
INF_S4                    (idx, [1:   8]) = [ -5.87336E-03 0.00472 -3.54718E-04 0.01168 -8.65926E-06 0.63397 -3.67492E-03 0.03649 ];
INF_S5                    (idx, [1:   8]) = [  6.28965E-04 0.04246  1.48688E-05 0.23329 -4.73681E-05 0.09030  3.00731E-03 0.04372 ];
INF_S6                    (idx, [1:   8]) = [  3.84715E-03 0.00711 -8.68753E-05 0.03740 -7.01842E-05 0.06409 -8.10686E-03 0.01170 ];
INF_S7                    (idx, [1:   8]) = [  7.14321E-04 0.03476 -9.94359E-05 0.03872 -5.15927E-05 0.07799 -1.75774E-04 0.51685 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  3.93128E-01 0.00020  1.07544E-02 0.00092  1.59932E-03 0.01049  8.61011E-01 0.00030 ];
INF_SP1                   (idx, [1:   8]) = [  1.65428E-01 0.00037  3.06325E-03 0.00181  5.39822E-04 0.01791  2.23402E-01 0.00081 ];
INF_SP2                   (idx, [1:   8]) = [  6.76277E-02 0.00057 -9.43496E-04 0.00540  2.85632E-04 0.02608  5.66921E-02 0.00294 ];
INF_SP3                   (idx, [1:   8]) = [  7.08923E-03 0.00582 -1.09785E-03 0.00412  1.06081E-04 0.07222  1.71538E-02 0.00710 ];
INF_SP4                   (idx, [1:   8]) = [ -5.87274E-03 0.00472 -3.54718E-04 0.01168 -8.65926E-06 0.63397 -3.67492E-03 0.03649 ];
INF_SP5                   (idx, [1:   8]) = [  6.28962E-04 0.04246  1.48688E-05 0.23329 -4.73681E-05 0.09030  3.00731E-03 0.04372 ];
INF_SP6                   (idx, [1:   8]) = [  3.84689E-03 0.00712 -8.68753E-05 0.03740 -7.01842E-05 0.06409 -8.10686E-03 0.01170 ];
INF_SP7                   (idx, [1:   8]) = [  7.14200E-04 0.03481 -9.94359E-05 0.03872 -5.15927E-05 0.07799 -1.75774E-04 0.51685 ];

% Micro-group spectrum:

B1_MICRO_FLX              (idx, [1: 140]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Integral parameters:

B1_KINF                   (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
B1_KEFF                   (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
B1_B2                     (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
B1_ERR                    (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];

% Critical spectra in infinite geometry:

B1_FLX                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISS_FLX               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reaction cross sections:

B1_TOT                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CAPT                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_ABS                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISS                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NSF                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NUBAR                  (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_KAPPA                  (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_INVV                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Total scattering cross sections:

B1_SCATT0                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT1                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT2                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT3                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT4                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT5                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT6                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT7                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Total scattering production cross sections:

B1_SCATTP0                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP1                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP2                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP3                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP4                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP5                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP6                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP7                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Diffusion parameters:

B1_TRANSPXS               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_DIFFCOEF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reduced absoption and removal:

B1_RABSXS                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_REMXS                  (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Poison cross sections:

B1_I135_YIELD             (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_XE135_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM147_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM148_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM148M_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM149_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SM149_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_I135_MICRO_ABS         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_XE135_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM147_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM148_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM148M_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM149_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SM149_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_XE135_MACRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SM149_MACRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Fission spectra:

B1_CHIT                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHIP                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHID                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Scattering matrixes:

B1_S0                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S1                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S2                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S3                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S4                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S5                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S6                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S7                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Scattering production matrixes:

B1_SP0                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP1                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP2                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP3                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP4                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP5                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP6                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP7                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Additional diffusion parameters:

CMM_TRANSPXS              (idx, [1:   4]) = [  1.90934E-01 0.00119  5.92595E-01 0.00634 ];
CMM_TRANSPXS_X            (idx, [1:   4]) = [  1.90770E-01 0.00223  5.88723E-01 0.01045 ];
CMM_TRANSPXS_Y            (idx, [1:   4]) = [  1.91199E-01 0.00178  6.03390E-01 0.00943 ];
CMM_TRANSPXS_Z            (idx, [1:   4]) = [  1.90864E-01 0.00178  5.88316E-01 0.00940 ];
CMM_DIFFCOEF              (idx, [1:   4]) = [  1.74587E+00 0.00119  5.63034E-01 0.00626 ];
CMM_DIFFCOEF_X            (idx, [1:   4]) = [  1.74751E+00 0.00223  5.67689E-01 0.01049 ];
CMM_DIFFCOEF_Y            (idx, [1:   4]) = [  1.74352E+00 0.00178  5.53635E-01 0.00958 ];
CMM_DIFFCOEF_Z            (idx, [1:   4]) = [  1.74657E+00 0.00178  5.67778E-01 0.00929 ];

% Delayed neutron parameters (Meulekamp method):

BETA_EFF                  (idx, [1:  18]) = [  7.60761E-03 0.01711  2.11709E-04 0.10243  1.00972E-03 0.04743  6.73982E-04 0.06356  1.47641E-03 0.03964  2.40067E-03 0.03082  9.28012E-04 0.05000  6.78589E-04 0.05688  2.28520E-04 0.10042 ];
LAMBDA                    (idx, [1:  18]) = [  4.61417E-01 0.02626  1.24667E-02 0.0E+00  2.82917E-02 0.0E+00  4.25244E-02 6.2E-09  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 4.9E-09  3.55460E+00 0.0E+00 ];

