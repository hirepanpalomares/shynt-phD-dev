
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
INPUT_FILE_NAME           (idx, [1:147])  = '/home/hirepan/Documents/chalmers/Project/codes/Shynt/repo/cases/single_assem_1x1cell/serpent_files/global_cell_type3/det_local_problem_coolant.serp' ;
WORKING_DIRECTORY         (idx, [1: 84])  = '/home/hirepan/Documents/chalmers/Project/codes/Shynt/repo/cases/single_assem_1x1cell' ;
HOSTNAME                  (idx, [1:  4])  = 'thor' ;
CPU_TYPE                  (idx, [1: 40])  = 'Intel(R) Core(TM) i9-10900 CPU @ 2.80GHz' ;
CPU_MHZ                   (idx, 1)        = 236.0 ;
START_DATE                (idx, [1: 24])  = 'Thu Mar 10 11:44:11 2022' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Mar 10 11:44:34 2022' ;

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
OMP_HISTORY_PROFILE       (idx, [1:  18]) = [  1.12755E+00  9.63292E-01  9.54169E-01  9.68049E-01  1.10384E+00  9.56932E-01  9.56965E-01  9.66104E-01  1.03689E+00  1.17085E+00  9.44475E-01  9.52175E-01  1.01186E+00  9.71695E-01  9.57668E-01  9.85837E-01  1.01415E+00  9.57488E-01  ];
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

MIN_MACROXS               (idx, [1:   4]) = [  5.00000E-02 0.0E+00  0.00000E+00 0.0E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  3.55086E-03 0.00290  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.96449E-01 1.0E-05  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  8.34028E-01 0.00010  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  8.34403E-01 0.00010  0.00000E+00 0.0E+00 ];
AVG_TRACKING_LOOPS        (idx, [1:   8]) = [  3.42962E+00 0.00063  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  2.69611E+01 0.00058  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  2.69611E+01 0.00058  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  5.35076E+00 0.00078  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  4.38691E+01 0.00055  0.00000E+00 0.0E+00 ];
LOST_PARTICLES            (idx, 1)        = 0 ;

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 500 ;
SIMULATED_HISTORIES       (idx, 1)        = 1000490 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  2.00098E+03 0.00143 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  2.00098E+03 0.00143 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  6.82571E+00 ;
RUNNING_TIME              (idx, 1)        =  3.91333E-01 ;
INIT_TIME                 (idx, [1:  2])  = [  1.17667E-02  1.17667E-02 ];
PROCESS_TIME              (idx, [1:  2])  = [  1.16666E-04  1.16666E-04 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  3.79383E-01  3.79383E-01  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  3.91233E-01  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 17.44220 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  1.79617E+01 0.00180 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  9.42675E-01 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 64024.21 ;
ALLOC_MEMSIZE             (idx, 1)        = 390.09;
MEMSIZE                   (idx, 1)        = 203.15;
XS_MEMSIZE                (idx, 1)        = 74.10;
MAT_MEMSIZE               (idx, 1)        = 6.90;
RES_MEMSIZE               (idx, 1)        = 1.56;
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

NORM_COEF                 (idx, [1:   4]) = [  4.98608E-04 0.00086  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  6.55882E-01 0.00212 ];
U235_FISS                 (idx, [1:   4]) = [  4.53788E-01 0.00121  9.16115E-01 0.00042 ];
U238_FISS                 (idx, [1:   4]) = [  4.15730E-02 0.00496  8.38853E-02 0.00461 ];
U235_CAPT                 (idx, [1:   4]) = [  1.06168E-01 0.00283  2.10809E-01 0.00266 ];
U238_CAPT                 (idx, [1:   4]) = [  3.67050E-01 0.00171  7.28597E-01 0.00087 ];

% Neutron balance (particles/weight):

BALA_SRC_NEUTRON_SRC     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_FISS    (idx, [1:  2])  = [ 1000490 1.00000E+06 ];
BALA_SRC_NEUTRON_NXN     (idx, [1:  2])  = [ 0 1.88891E+03 ];
BALA_SRC_NEUTRON_VR      (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_TOT     (idx, [1:  2])  = [ 1000490 1.00189E+06 ];

BALA_LOSS_NEUTRON_CAPT    (idx, [1:  2])  = [ 504401 5.05119E+05 ];
BALA_LOSS_NEUTRON_FISS    (idx, [1:  2])  = [ 496089 4.96770E+05 ];
BALA_LOSS_NEUTRON_LEAK    (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_CUT     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_ERR     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_TOT     (idx, [1:  2])  = [ 1000490 1.00189E+06 ];

BALA_NEUTRON_DIFF         (idx, [1:  2])  = [ 0 -9.31323E-10 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.61097E-11 0.00051 ];
TOT_POWDENS               (idx, [1:   2]) = [  2.96963E-15 0.00051 ];
TOT_GENRATE               (idx, [1:   2]) = [  1.22570E+00 0.00051 ];
TOT_FISSRATE              (idx, [1:   2]) = [  4.96330E-01 0.00051 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  5.03670E-01 0.00051 ];
TOT_ABSRATE               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.97217E-01 0.00086 ];
TOT_FLUX                  (idx, [1:   2]) = [  5.64192E+01 0.00067 ];
TOT_PHOTON_PRODRATE       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  2.69307E+01 0.00053 ];
INI_FMASS                 (idx, 1)        =  5.42481E-03 ;
TOT_FMASS                 (idx, 1)        =  5.42481E-03 ;

% Six-factor formula:

SIX_FF_ETA                (idx, [1:   2]) = [  1.78143E+00 0.00085 ];
SIX_FF_F                  (idx, [1:   2]) = [  9.55901E-01 0.00031 ];
SIX_FF_P                  (idx, [1:   2]) = [  5.24170E-01 0.00095 ];
SIX_FF_EPSILON            (idx, [1:   2]) = [  1.37499E+00 0.00088 ];
SIX_FF_LF                 (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
SIX_FF_LT                 (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
SIX_FF_KINF               (idx, [1:   2]) = [  1.22684E+00 0.00098 ];
SIX_FF_KEFF               (idx, [1:   2]) = [  1.22684E+00 0.00098 ];

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.46954E+00 3.4E-05 ];
FISSE                     (idx, [1:   2]) = [  2.02584E+02 3.0E-06 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.22680E+00 0.00101  1.21817E+00 0.00098  8.66354E-03 0.01791 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.22804E+00 0.00051 ];
COL_KEFF                  (idx, [1:   2]) = [  1.22965E+00 0.00111 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.22804E+00 0.00051 ];
ABS_KINF                  (idx, [1:   2]) = [  1.22804E+00 0.00051 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% ALF (Average lethargy of neutrons causing fission):
% Based on E0 = 2.000000E+01 MeV

ANA_ALF                   (idx, [1:   2]) = [  1.67126E+01 0.00045 ];
IMP_ALF                   (idx, [1:   2]) = [  1.67132E+01 0.00023 ];

% EALF (Energy corresponding to average lethargy of neutrons causing fission):

ANA_EALF                  (idx, [1:   2]) = [  1.11943E-06 0.00760 ];
IMP_EALF                  (idx, [1:   2]) = [  1.10727E-06 0.00396 ];

% AFGE (Average energy of neutrons causing fission):

ANA_AFGE                  (idx, [1:   2]) = [  2.81533E-01 0.00496 ];
IMP_AFGE                  (idx, [1:   2]) = [  2.80874E-01 0.00229 ];

% Forward-weighted delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
FWD_ANA_BETA_ZERO         (idx, [1:  18]) = [  6.15833E-03 0.01198  1.64753E-04 0.07117  8.58089E-04 0.03232  4.91256E-04 0.04208  1.17907E-03 0.02701  1.99917E-03 0.02176  6.97301E-04 0.03236  5.45691E-04 0.03799  2.22997E-04 0.05842 ];
FWD_ANA_LAMBDA            (idx, [1:  18]) = [  4.83478E-01 0.01831  4.13894E-03 0.06350  2.46138E-02 0.01730  2.93418E-02 0.03001  1.25059E-01 0.01131  2.88958E-01 0.00493  5.61183E-01 0.01939  1.22936E+00 0.02571  1.55691E+00 0.05071 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  18]) = [  7.24206E-03 0.01824  1.95284E-04 0.10411  9.85749E-04 0.05145  5.82219E-04 0.05833  1.43074E-03 0.04069  2.37974E-03 0.02996  8.33977E-04 0.04882  5.87560E-04 0.05780  2.46796E-04 0.10085 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  18]) = [  4.57639E-01 0.02594  1.24667E-02 0.0E+00  2.82917E-02 0.0E+00  4.25244E-02 6.1E-09  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 4.9E-09  3.55460E+00 0.0E+00 ];

% Adjoint weighted time constants using Nauchi's method:

IFP_CHAIN_LENGTH          (idx, 1)        = 15 ;
ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  2.07933E-05 0.00233  2.07775E-05 0.00234  2.23537E-05 0.02472 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  2.54937E-05 0.00200  2.54742E-05 0.00201  2.74168E-05 0.02470 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  18]) = [  7.06599E-03 0.01793  1.73614E-04 0.11078  9.86973E-04 0.04632  5.41483E-04 0.06293  1.36635E-03 0.04144  2.34232E-03 0.02964  8.27279E-04 0.04908  5.86943E-04 0.05918  2.41028E-04 0.08800 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  18]) = [  4.67499E-01 0.02889  1.24667E-02 0.0E+00  2.82917E-02 4.5E-09  4.25244E-02 8.2E-09  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 5.7E-09  3.55460E+00 5.0E-09 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  2.08184E-05 0.00490  2.08139E-05 0.00493  1.53139E-05 0.05333 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  2.55253E-05 0.00478  2.55198E-05 0.00481  1.87746E-05 0.05328 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  18]) = [  6.95924E-03 0.05118  1.55869E-04 0.34115  1.13778E-03 0.12367  5.65698E-04 0.17911  1.54154E-03 0.11676  1.82079E-03 0.09055  9.28471E-04 0.14119  5.68811E-04 0.17257  2.40283E-04 0.27543 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  18]) = [  4.50748E-01 0.06497  1.24667E-02 3.9E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 4.0E-09  2.92467E-01 5.1E-09  6.66488E-01 4.8E-09  1.63478E+00 0.0E+00  3.55460E+00 7.1E-09 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  18]) = [  7.03219E-03 0.04959  1.34580E-04 0.33589  1.15761E-03 0.11750  5.78188E-04 0.18525  1.54005E-03 0.11316  1.89471E-03 0.08880  8.99158E-04 0.13570  5.73024E-04 0.16381  2.54865E-04 0.24626 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  18]) = [  4.57937E-01 0.06372  1.24667E-02 0.0E+00  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 4.0E-09  2.92467E-01 5.3E-09  6.66488E-01 4.8E-09  1.63478E+00 0.0E+00  3.55460E+00 6.6E-09 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -3.36061E+02 0.05194 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  2.08509E-05 0.00140 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  2.55666E-05 0.00094 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  7.10875E-03 0.01045 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -3.41561E+02 0.01072 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  3.27991E-07 0.00119 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  4.19992E-06 0.00105  4.20001E-06 0.00105  4.22040E-06 0.01246 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.03049E-05 0.00133  3.03039E-05 0.00134  3.00103E-05 0.01604 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.24727E-01 0.00095  5.23736E-01 0.00096  7.41681E-01 0.02214 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.16685E+01 0.02696 ];
ANA_MEAN_NCOL             (idx, [1:   4]) = [  2.69611E+01 0.00058  3.03411E+01 0.00075 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  1])  = '0' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  2.00000E+01  6.06550E+00  3.67900E+00  2.23100E+00  1.35300E+00  8.21000E-01  5.00000E-01  3.02500E-01  1.83000E-01  1.11000E-01  6.74300E-02  4.08500E-02  2.47800E-02  1.50300E-02  9.11800E-03  5.50000E-03  3.51910E-03  2.23945E-03  1.42510E-03  9.06898E-04  3.67262E-04  1.48728E-04  7.55014E-05  4.80520E-05  2.77000E-05  1.59680E-05  9.87700E-06  4.00000E-06  3.30000E-06  2.60000E-06  2.10000E-06  1.85500E-06  1.50000E-06  1.30000E-06  1.15000E-06  1.12300E-06  1.09700E-06  1.07100E-06  1.04500E-06  1.02000E-06  9.96000E-07  9.72000E-07  9.50000E-07  9.10000E-07  8.50000E-07  7.80000E-07  6.25000E-07  5.00000E-07  4.00000E-07  3.50000E-07  3.20000E-07  3.00000E-07  2.80000E-07  2.50000E-07  2.20000E-07  1.80000E-07  1.40000E-07  1.00000E-07  8.00000E-08  6.70000E-08  5.80000E-08  5.00000E-08  4.20000E-08  3.50000E-08  3.00000E-08  2.50000E-08  2.00000E-08  1.50000E-08  1.00000E-08  5.00000E-09  1.00000E-11 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Micro-group spectrum:

INF_MICRO_FLX             (idx, [1: 140]) = [  1.66847E+04 0.00673  6.99513E+04 0.00396  1.47946E+05 0.00256  1.56476E+05 0.00132  1.49593E+05 0.00175  1.80315E+05 0.00133  1.21812E+05 0.00114  1.13181E+05 0.00156  8.61173E+04 0.00158  7.00675E+04 0.00148  6.05737E+04 0.00172  5.38262E+04 0.00151  5.00926E+04 0.00173  4.74670E+04 0.00164  4.60247E+04 0.00171  3.95192E+04 0.00215  3.90699E+04 0.00205  3.83992E+04 0.00196  3.74017E+04 0.00192  7.21464E+04 0.00124  6.87081E+04 0.00164  4.83603E+04 0.00193  3.07818E+04 0.00194  3.44024E+04 0.00200  3.15974E+04 0.00225  2.89835E+04 0.00205  4.48075E+04 0.00154  1.03385E+04 0.00409  1.31659E+04 0.00260  1.18907E+04 0.00313  6.90165E+03 0.00494  1.20911E+04 0.00418  8.13401E+03 0.00325  6.88282E+03 0.00398  1.29864E+03 0.00746  1.29695E+03 0.00895  1.30790E+03 0.00658  1.33948E+03 0.00676  1.34834E+03 0.00710  1.31140E+03 0.00794  1.38546E+03 0.00788  1.28941E+03 0.00641  2.44393E+03 0.00493  3.91849E+03 0.00484  4.99466E+03 0.00488  1.30483E+04 0.00334  1.36023E+04 0.00302  1.42737E+04 0.00364  9.10752E+03 0.00392  6.40739E+03 0.00328  4.75037E+03 0.00475  5.38220E+03 0.00349  9.56376E+03 0.00375  1.20794E+04 0.00267  2.13410E+04 0.00239  3.00074E+04 0.00217  4.09987E+04 0.00213  2.46802E+04 0.00178  1.70562E+04 0.00288  1.19687E+04 0.00252  1.05586E+04 0.00234  1.01620E+04 0.00259  8.36959E+03 0.00289  5.57183E+03 0.00367  5.08963E+03 0.00323  4.46915E+03 0.00319  3.74950E+03 0.00374  2.90676E+03 0.00511  1.90658E+03 0.00395  6.63207E+02 0.00489 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.22965E+00 0.00109 ];

% Flux spectra in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  4.95787E+01 0.00073  6.84739E+00 0.00082 ];
INF_FISS_FLX              (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  4.13566E-01 0.00028  9.39299E-01 0.00021 ];
INF_CAPT                  (idx, [1:   4]) = [  6.97983E-03 0.00088  2.30404E-02 0.00053 ];
INF_ABS                   (idx, [1:   4]) = [  9.60656E-03 0.00072  7.65364E-02 0.00063 ];
INF_FISS                  (idx, [1:   4]) = [  2.62673E-03 0.00102  5.34960E-02 0.00067 ];
INF_NSF                   (idx, [1:   4]) = [  6.73299E-03 0.00103  1.30327E-01 0.00067 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.56326E+00 0.00012  2.43620E+00 2.7E-09 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.03468E+02 1.0E-05  2.02270E+02 0.0E+00 ];
INF_INVV                  (idx, [1:   4]) = [  5.39199E-08 0.00125  2.31261E-06 0.00031 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  4.03957E-01 0.00029  8.62962E-01 0.00026 ];
INF_SCATT1                (idx, [1:   4]) = [  1.68654E-01 0.00043  2.24252E-01 0.00099 ];
INF_SCATT2                (idx, [1:   4]) = [  6.68216E-02 0.00062  5.67722E-02 0.00341 ];
INF_SCATT3                (idx, [1:   4]) = [  6.05338E-03 0.00627  1.72376E-02 0.00827 ];
INF_SCATT4                (idx, [1:   4]) = [ -6.26319E-03 0.00599 -3.55011E-03 0.02616 ];
INF_SCATT5                (idx, [1:   4]) = [  6.14414E-04 0.05167  3.09171E-03 0.02923 ];
INF_SCATT6                (idx, [1:   4]) = [  3.71748E-03 0.00606 -8.11299E-03 0.01241 ];
INF_SCATT7                (idx, [1:   4]) = [  6.02620E-04 0.03862 -4.83363E-04 0.16977 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  4.03995E-01 0.00029  8.62962E-01 0.00026 ];
INF_SCATTP1               (idx, [1:   4]) = [  1.68655E-01 0.00043  2.24252E-01 0.00099 ];
INF_SCATTP2               (idx, [1:   4]) = [  6.68213E-02 0.00063  5.67722E-02 0.00341 ];
INF_SCATTP3               (idx, [1:   4]) = [  6.05368E-03 0.00628  1.72376E-02 0.00827 ];
INF_SCATTP4               (idx, [1:   4]) = [ -6.26327E-03 0.00599 -3.55011E-03 0.02616 ];
INF_SCATTP5               (idx, [1:   4]) = [  6.14549E-04 0.05175  3.09171E-03 0.02923 ];
INF_SCATTP6               (idx, [1:   4]) = [  3.71757E-03 0.00605 -8.11299E-03 0.01241 ];
INF_SCATTP7               (idx, [1:   4]) = [  6.02491E-04 0.03859 -4.83363E-04 0.16977 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  1.85074E-01 0.00083  6.38417E-01 0.00047 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.80111E+00 0.00084  5.22127E-01 0.00047 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  9.56857E-03 0.00069  7.65364E-02 0.00063 ];
INF_REMXS                 (idx, [1:   4]) = [  2.03712E-02 0.00046  7.79259E-02 0.00094 ];

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

INF_S0                    (idx, [1:   8]) = [  3.93194E-01 0.00029  1.07624E-02 0.00076  1.58846E-03 0.00938  8.61373E-01 0.00027 ];
INF_S1                    (idx, [1:   8]) = [  1.65575E-01 0.00043  3.07911E-03 0.00203  5.33677E-04 0.02314  2.23719E-01 0.00099 ];
INF_S2                    (idx, [1:   8]) = [  6.77612E-02 0.00062 -9.39681E-04 0.00488  2.92933E-04 0.03207  5.64792E-02 0.00342 ];
INF_S3                    (idx, [1:   8]) = [  7.15465E-03 0.00529 -1.10128E-03 0.00389  1.10755E-04 0.06200  1.71269E-02 0.00839 ];
INF_S4                    (idx, [1:   8]) = [ -5.90110E-03 0.00635 -3.62085E-04 0.01452 -1.00813E-07 1.00000 -3.55001E-03 0.02553 ];
INF_S5                    (idx, [1:   8]) = [  6.03557E-04 0.05265  1.08567E-05 0.33350 -4.46739E-05 0.10759  3.13639E-03 0.02878 ];
INF_S6                    (idx, [1:   8]) = [  3.80261E-03 0.00565 -8.51297E-05 0.04478 -5.46146E-05 0.08520 -8.05838E-03 0.01248 ];
INF_S7                    (idx, [1:   8]) = [  7.07663E-04 0.03224 -1.05043E-04 0.03544 -5.88489E-05 0.08773 -4.24514E-04 0.19367 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  3.93232E-01 0.00030  1.07624E-02 0.00076  1.58846E-03 0.00938  8.61373E-01 0.00027 ];
INF_SP1                   (idx, [1:   8]) = [  1.65576E-01 0.00043  3.07911E-03 0.00203  5.33677E-04 0.02314  2.23719E-01 0.00099 ];
INF_SP2                   (idx, [1:   8]) = [  6.77610E-02 0.00062 -9.39681E-04 0.00488  2.92933E-04 0.03207  5.64792E-02 0.00342 ];
INF_SP3                   (idx, [1:   8]) = [  7.15496E-03 0.00529 -1.10128E-03 0.00389  1.10755E-04 0.06200  1.71269E-02 0.00839 ];
INF_SP4                   (idx, [1:   8]) = [ -5.90118E-03 0.00635 -3.62085E-04 0.01452 -1.00813E-07 1.00000 -3.55001E-03 0.02553 ];
INF_SP5                   (idx, [1:   8]) = [  6.03692E-04 0.05272  1.08567E-05 0.33350 -4.46739E-05 0.10759  3.13639E-03 0.02878 ];
INF_SP6                   (idx, [1:   8]) = [  3.80270E-03 0.00564 -8.51297E-05 0.04478 -5.46146E-05 0.08520 -8.05838E-03 0.01248 ];
INF_SP7                   (idx, [1:   8]) = [  7.07534E-04 0.03222 -1.05043E-04 0.03544 -5.88489E-05 0.08773 -4.24514E-04 0.19367 ];

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

CMM_TRANSPXS              (idx, [1:   4]) = [  1.91011E-01 0.00169  5.88301E-01 0.00497 ];
CMM_TRANSPXS_X            (idx, [1:   4]) = [  1.91152E-01 0.00227  5.88452E-01 0.01002 ];
CMM_TRANSPXS_Y            (idx, [1:   4]) = [  1.91274E-01 0.00262  5.86395E-01 0.01011 ];
CMM_TRANSPXS_Z            (idx, [1:   4]) = [  1.90654E-01 0.00253  5.92987E-01 0.00877 ];
CMM_DIFFCOEF              (idx, [1:   4]) = [  1.74522E+00 0.00169  5.66937E-01 0.00493 ];
CMM_DIFFCOEF_X            (idx, [1:   4]) = [  1.74403E+00 0.00227  5.67829E-01 0.01005 ];
CMM_DIFFCOEF_Y            (idx, [1:   4]) = [  1.74299E+00 0.00261  5.69807E-01 0.00988 ];
CMM_DIFFCOEF_Z            (idx, [1:   4]) = [  1.74864E+00 0.00253  5.63175E-01 0.00886 ];

% Delayed neutron parameters (Meulekamp method):

BETA_EFF                  (idx, [1:  18]) = [  7.24206E-03 0.01824  1.95284E-04 0.10411  9.85749E-04 0.05145  5.82219E-04 0.05833  1.43074E-03 0.04069  2.37974E-03 0.02996  8.33977E-04 0.04882  5.87560E-04 0.05780  2.46796E-04 0.10085 ];
LAMBDA                    (idx, [1:  18]) = [  4.57639E-01 0.02594  1.24667E-02 0.0E+00  2.82917E-02 0.0E+00  4.25244E-02 6.1E-09  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 4.9E-09  3.55460E+00 0.0E+00 ];

