
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
INPUT_FILE_NAME           (idx, [1:147])  = '/home/hirepan/Documents/chalmers/Project/codes/Shynt/repo/cases/single_assem_1x1cell/serpent_files/global_cell_type4/det_local_problem_coolant.serp' ;
WORKING_DIRECTORY         (idx, [1: 84])  = '/home/hirepan/Documents/chalmers/Project/codes/Shynt/repo/cases/single_assem_1x1cell' ;
HOSTNAME                  (idx, [1:  4])  = 'thor' ;
CPU_TYPE                  (idx, [1: 40])  = 'Intel(R) Core(TM) i9-10900 CPU @ 2.80GHz' ;
CPU_MHZ                   (idx, 1)        = 236.0 ;
START_DATE                (idx, [1: 24])  = 'Thu Mar 10 11:45:40 2022' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Mar 10 11:46:03 2022' ;

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
OMP_HISTORY_PROFILE       (idx, [1:  18]) = [  1.01573E+00  1.00308E+00  9.69790E-01  1.12075E+00  1.08030E+00  9.38712E-01  9.61469E-01  9.52952E-01  9.64951E-01  1.05591E+00  1.04094E+00  9.47917E-01  9.52576E-01  9.54439E-01  9.92138E-01  1.05544E+00  1.00656E+00  9.86351E-01  ];
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
ST_FRAC                   (idx, [1:   4]) = [  3.61983E-03 0.00282  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.96380E-01 1.0E-05  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  8.36841E-01 0.00010  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  8.37226E-01 0.00010  0.00000E+00 0.0E+00 ];
AVG_TRACKING_LOOPS        (idx, [1:   8]) = [  3.41720E+00 0.00071  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  2.55007E+01 0.00053  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  2.55007E+01 0.00053  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  4.95787E+00 0.00076  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  4.25344E+01 0.00055  0.00000E+00 0.0E+00 ];
LOST_PARTICLES            (idx, 1)        = 0 ;

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 500 ;
SIMULATED_HISTORIES       (idx, 1)        = 1000417 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  2.00083E+03 0.00136 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  2.00083E+03 0.00136 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  6.53416E+00 ;
RUNNING_TIME              (idx, 1)        =  3.75750E-01 ;
INIT_TIME                 (idx, [1:  2])  = [  1.20000E-02  1.20000E-02 ];
PROCESS_TIME              (idx, [1:  2])  = [  9.99967E-05  9.99967E-05 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  3.63583E-01  3.63583E-01  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  3.75667E-01  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 17.38965 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  1.79516E+01 0.00188 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  9.40075E-01 ;

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

NORM_COEF                 (idx, [1:   4]) = [  4.98971E-04 0.00082  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  5.78085E-01 0.00216 ];
U235_FISS                 (idx, [1:   4]) = [  4.74923E-01 0.00116  9.19909E-01 0.00040 ];
U238_FISS                 (idx, [1:   4]) = [  4.13716E-02 0.00497  8.00913E-02 0.00461 ];
U235_CAPT                 (idx, [1:   4]) = [  1.16403E-01 0.00297  2.40698E-01 0.00268 ];
U238_CAPT                 (idx, [1:   4]) = [  3.41634E-01 0.00172  7.06353E-01 0.00094 ];

% Neutron balance (particles/weight):

BALA_SRC_NEUTRON_SRC     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_FISS    (idx, [1:  2])  = [ 1000417 1.00000E+06 ];
BALA_SRC_NEUTRON_NXN     (idx, [1:  2])  = [ 0 1.99927E+03 ];
BALA_SRC_NEUTRON_VR      (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_TOT     (idx, [1:  2])  = [ 1000417 1.00200E+06 ];

BALA_LOSS_NEUTRON_CAPT    (idx, [1:  2])  = [ 483835 4.84612E+05 ];
BALA_LOSS_NEUTRON_FISS    (idx, [1:  2])  = [ 516582 5.17387E+05 ];
BALA_LOSS_NEUTRON_LEAK    (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_CUT     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_ERR     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_TOT     (idx, [1:  2])  = [ 1000417 1.00200E+06 ];

BALA_NEUTRON_DIFF         (idx, [1:  2])  = [ 0 9.31323E-10 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.67497E-11 0.00048 ];
TOT_POWDENS               (idx, [1:   2]) = [  3.08762E-15 0.00048 ];
TOT_GENRATE               (idx, [1:   2]) = [  1.27414E+00 0.00048 ];
TOT_FISSRATE              (idx, [1:   2]) = [  5.16082E-01 0.00048 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  4.83918E-01 0.00051 ];
TOT_ABSRATE               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.97943E-01 0.00082 ];
TOT_FLUX                  (idx, [1:   2]) = [  5.47401E+01 0.00066 ];
TOT_PHOTON_PRODRATE       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  2.54936E+01 0.00052 ];
INI_FMASS                 (idx, 1)        =  5.42481E-03 ;
TOT_FMASS                 (idx, 1)        =  5.42481E-03 ;

% Six-factor formula:

SIX_FF_ETA                (idx, [1:   2]) = [  1.84269E+00 0.00083 ];
SIX_FF_F                  (idx, [1:   2]) = [  9.63622E-01 0.00028 ];
SIX_FF_P                  (idx, [1:   2]) = [  5.00140E-01 0.00097 ];
SIX_FF_EPSILON            (idx, [1:   2]) = [  1.43889E+00 0.00095 ];
SIX_FF_LF                 (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
SIX_FF_LT                 (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
SIX_FF_KINF               (idx, [1:   2]) = [  1.27730E+00 0.00095 ];
SIX_FF_KEFF               (idx, [1:   2]) = [  1.27730E+00 0.00095 ];

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.46888E+00 3.2E-05 ];
FISSE                     (idx, [1:   2]) = [  2.02572E+02 2.7E-06 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.27736E+00 0.00098  1.26814E+00 0.00095  9.16117E-03 0.01657 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.27666E+00 0.00048 ];
COL_KEFF                  (idx, [1:   2]) = [  1.27725E+00 0.00103 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.27666E+00 0.00048 ];
ABS_KINF                  (idx, [1:   2]) = [  1.27666E+00 0.00048 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% ALF (Average lethargy of neutrons causing fission):
% Based on E0 = 2.000000E+01 MeV

ANA_ALF                   (idx, [1:   2]) = [  1.64577E+01 0.00046 ];
IMP_ALF                   (idx, [1:   2]) = [  1.64485E+01 0.00023 ];

% EALF (Energy corresponding to average lethargy of neutrons causing fission):

ANA_EALF                  (idx, [1:   2]) = [  1.44434E-06 0.00760 ];
IMP_EALF                  (idx, [1:   2]) = [  1.44266E-06 0.00389 ];

% AFGE (Average energy of neutrons causing fission):

ANA_AFGE                  (idx, [1:   2]) = [  2.75579E-01 0.00481 ];
IMP_AFGE                  (idx, [1:   2]) = [  2.76618E-01 0.00221 ];

% Forward-weighted delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
FWD_ANA_BETA_ZERO         (idx, [1:  18]) = [  5.80467E-03 0.01192  1.59413E-04 0.07518  8.17622E-04 0.03205  4.77443E-04 0.03895  1.06878E-03 0.02677  1.86304E-03 0.02135  6.82673E-04 0.03578  5.23463E-04 0.03714  2.12233E-04 0.05981 ];
FWD_ANA_LAMBDA            (idx, [1:  18]) = [  4.81264E-01 0.01774  3.91454E-03 0.06617  2.48401E-02 0.01669  3.10428E-02 0.02723  1.25858E-01 0.01070  2.88373E-01 0.00533  5.34523E-01 0.02224  1.23589E+00 0.02543  1.51426E+00 0.05196 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  18]) = [  7.19168E-03 0.01761  1.94342E-04 0.10530  9.78979E-04 0.04695  6.11601E-04 0.05815  1.28083E-03 0.03966  2.37758E-03 0.03170  8.48191E-04 0.05260  6.24085E-04 0.05526  2.76083E-04 0.08994 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  18]) = [  4.87871E-01 0.02848  1.24667E-02 0.0E+00  2.82917E-02 0.0E+00  4.25244E-02 5.7E-09  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 4.9E-09  3.55460E+00 0.0E+00 ];

% Adjoint weighted time constants using Nauchi's method:

IFP_CHAIN_LENGTH          (idx, 1)        = 15 ;
ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  1.59807E-05 0.00218  1.59706E-05 0.00219  1.73605E-05 0.02344 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  2.04021E-05 0.00189  2.03892E-05 0.00190  2.21714E-05 0.02349 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  18]) = [  7.20262E-03 0.01674  2.19364E-04 0.09362  9.54334E-04 0.04538  6.14152E-04 0.05661  1.30606E-03 0.03839  2.36329E-03 0.03032  8.15328E-04 0.05395  6.17045E-04 0.05507  3.13050E-04 0.07585 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  18]) = [  4.99756E-01 0.02852  1.24667E-02 0.0E+00  2.82917E-02 3.9E-09  4.25244E-02 8.1E-09  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 5.5E-09  3.55460E+00 4.6E-09 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  1.60434E-05 0.00478  1.60346E-05 0.00480  1.27294E-05 0.05155 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  2.04839E-05 0.00468  2.04727E-05 0.00471  1.62315E-05 0.05145 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  18]) = [  7.16149E-03 0.05012  2.01055E-04 0.23020  8.41700E-04 0.13435  5.17255E-04 0.17974  1.37993E-03 0.11850  2.44670E-03 0.08891  7.51305E-04 0.14405  6.88888E-04 0.16065  3.34662E-04 0.22565 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  18]) = [  5.09074E-01 0.06948  1.24667E-02 5.4E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 3.2E-09  2.92467E-01 5.8E-09  6.66488E-01 5.3E-09  1.63478E+00 0.0E+00  3.55460E+00 6.5E-09 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  18]) = [  7.19361E-03 0.04707  2.27280E-04 0.22780  8.46245E-04 0.12559  5.63290E-04 0.17730  1.41907E-03 0.11275  2.38077E-03 0.08450  7.11592E-04 0.14159  6.99679E-04 0.15865  3.45681E-04 0.21181 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  18]) = [  5.06918E-01 0.06950  1.24667E-02 5.4E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 3.5E-09  2.92467E-01 5.9E-09  6.66488E-01 5.3E-09  1.63478E+00 0.0E+00  3.55460E+00 6.5E-09 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -4.53934E+02 0.05129 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  1.60077E-05 0.00132 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  2.04375E-05 0.00087 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  7.29227E-03 0.00965 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -4.56069E+02 0.00979 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  2.70883E-07 0.00116 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  4.12114E-06 0.00104  4.12135E-06 0.00104  4.10062E-06 0.01332 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  2.45814E-05 0.00137  2.45825E-05 0.00137  2.45006E-05 0.01677 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.00759E-01 0.00097  4.99743E-01 0.00098  7.27487E-01 0.02108 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.15951E+01 0.02595 ];
ANA_MEAN_NCOL             (idx, [1:   4]) = [  2.55007E+01 0.00053  2.83442E+01 0.00068 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  1])  = '0' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  2.00000E+01  6.06550E+00  3.67900E+00  2.23100E+00  1.35300E+00  8.21000E-01  5.00000E-01  3.02500E-01  1.83000E-01  1.11000E-01  6.74300E-02  4.08500E-02  2.47800E-02  1.50300E-02  9.11800E-03  5.50000E-03  3.51910E-03  2.23945E-03  1.42510E-03  9.06898E-04  3.67262E-04  1.48728E-04  7.55014E-05  4.80520E-05  2.77000E-05  1.59680E-05  9.87700E-06  4.00000E-06  3.30000E-06  2.60000E-06  2.10000E-06  1.85500E-06  1.50000E-06  1.30000E-06  1.15000E-06  1.12300E-06  1.09700E-06  1.07100E-06  1.04500E-06  1.02000E-06  9.96000E-07  9.72000E-07  9.50000E-07  9.10000E-07  8.50000E-07  7.80000E-07  6.25000E-07  5.00000E-07  4.00000E-07  3.50000E-07  3.20000E-07  3.00000E-07  2.80000E-07  2.50000E-07  2.20000E-07  1.80000E-07  1.40000E-07  1.00000E-07  8.00000E-08  6.70000E-08  5.80000E-08  5.00000E-08  4.20000E-08  3.50000E-08  3.00000E-08  2.50000E-08  2.00000E-08  1.50000E-08  1.00000E-08  5.00000E-09  1.00000E-11 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Micro-group spectrum:

INF_MICRO_FLX             (idx, [1: 140]) = [  1.68764E+04 0.00873  7.03071E+04 0.00296  1.48656E+05 0.00219  1.56906E+05 0.00147  1.49571E+05 0.00147  1.80232E+05 0.00112  1.21910E+05 0.00199  1.12976E+05 0.00129  8.60161E+04 0.00177  6.99481E+04 0.00116  6.05250E+04 0.00179  5.40654E+04 0.00164  4.99169E+04 0.00140  4.72425E+04 0.00212  4.59119E+04 0.00158  3.94030E+04 0.00197  3.89097E+04 0.00157  3.82675E+04 0.00205  3.70230E+04 0.00194  7.14280E+04 0.00119  6.77285E+04 0.00126  4.73865E+04 0.00180  2.99515E+04 0.00232  3.34778E+04 0.00178  3.05295E+04 0.00171  2.78685E+04 0.00247  4.28430E+04 0.00180  9.95793E+03 0.00301  1.24557E+04 0.00356  1.14943E+04 0.00373  6.57195E+03 0.00416  1.14411E+04 0.00313  7.82707E+03 0.00490  6.51259E+03 0.00443  1.21523E+03 0.00768  1.21102E+03 0.00785  1.22823E+03 0.00640  1.29453E+03 0.00697  1.27568E+03 0.00886  1.23803E+03 0.00775  1.30476E+03 0.00801  1.21285E+03 0.00620  2.32052E+03 0.00599  3.69460E+03 0.00412  4.71119E+03 0.00486  1.22945E+04 0.00333  1.27109E+04 0.00231  1.31532E+04 0.00238  8.18932E+03 0.00369  5.63321E+03 0.00335  4.14774E+03 0.00505  4.60061E+03 0.00357  8.11035E+03 0.00240  9.99772E+03 0.00233  1.74419E+04 0.00279  2.39026E+04 0.00158  3.16341E+04 0.00197  1.86986E+04 0.00219  1.27731E+04 0.00236  8.93672E+03 0.00293  7.81568E+03 0.00233  7.52971E+03 0.00304  6.16974E+03 0.00260  4.09663E+03 0.00393  3.73061E+03 0.00362  3.26176E+03 0.00306  2.72670E+03 0.00348  2.11918E+03 0.00410  1.38209E+03 0.00456  4.82321E+02 0.00510 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.27725E+00 0.00096 ];

% Flux spectra in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  4.92767E+01 0.00070  5.46978E+00 0.00073 ];
INF_FISS_FLX              (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  4.12545E-01 0.00021  9.45021E-01 0.00026 ];
INF_CAPT                  (idx, [1:   4]) = [  7.07613E-03 0.00094  2.47485E-02 0.00059 ];
INF_ABS                   (idx, [1:   4]) = [  1.01817E-02 0.00065  9.11572E-02 0.00072 ];
INF_FISS                  (idx, [1:   4]) = [  3.10559E-03 0.00086  6.64087E-02 0.00077 ];
INF_NSF                   (idx, [1:   4]) = [  7.90806E-03 0.00085  1.61785E-01 0.00077 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.54639E+00 8.4E-05  2.43620E+00 0.0E+00 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.03288E+02 6.9E-06  2.02270E+02 0.0E+00 ];
INF_INVV                  (idx, [1:   4]) = [  5.20276E-08 0.00094  2.24265E-06 0.00036 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  4.02381E-01 0.00021  8.53772E-01 0.00032 ];
INF_SCATT1                (idx, [1:   4]) = [  1.67955E-01 0.00033  2.25937E-01 0.00110 ];
INF_SCATT2                (idx, [1:   4]) = [  6.66153E-02 0.00067  5.82229E-02 0.00334 ];
INF_SCATT3                (idx, [1:   4]) = [  6.04067E-03 0.00484  1.77376E-02 0.01078 ];
INF_SCATT4                (idx, [1:   4]) = [ -6.11123E-03 0.00441 -3.28169E-03 0.03787 ];
INF_SCATT5                (idx, [1:   4]) = [  7.17214E-04 0.04646  3.06254E-03 0.04453 ];
INF_SCATT6                (idx, [1:   4]) = [  3.74192E-03 0.00675 -7.76638E-03 0.01549 ];
INF_SCATT7                (idx, [1:   4]) = [  5.86896E-04 0.03748 -2.49021E-04 0.44564 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  4.02421E-01 0.00021  8.53772E-01 0.00032 ];
INF_SCATTP1               (idx, [1:   4]) = [  1.67956E-01 0.00033  2.25937E-01 0.00110 ];
INF_SCATTP2               (idx, [1:   4]) = [  6.66157E-02 0.00067  5.82229E-02 0.00334 ];
INF_SCATTP3               (idx, [1:   4]) = [  6.04020E-03 0.00484  1.77376E-02 0.01078 ];
INF_SCATTP4               (idx, [1:   4]) = [ -6.11184E-03 0.00440 -3.28169E-03 0.03787 ];
INF_SCATTP5               (idx, [1:   4]) = [  7.17414E-04 0.04639  3.06254E-03 0.04453 ];
INF_SCATTP6               (idx, [1:   4]) = [  3.74160E-03 0.00674 -7.76638E-03 0.01549 ];
INF_SCATTP7               (idx, [1:   4]) = [  5.87235E-04 0.03750 -2.49021E-04 0.44564 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  1.84394E-01 0.00057  6.41209E-01 0.00044 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.80774E+00 0.00057  5.19854E-01 0.00044 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  1.01412E-02 0.00064  9.11572E-02 0.00072 ];
INF_REMXS                 (idx, [1:   4]) = [  2.04987E-02 0.00050  9.31077E-02 0.00086 ];

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

INF_S0                    (idx, [1:   8]) = [  3.92046E-01 0.00021  1.03350E-02 0.00071  1.85858E-03 0.00993  8.51913E-01 0.00032 ];
INF_S1                    (idx, [1:   8]) = [  1.65021E-01 0.00033  2.93435E-03 0.00183  5.92153E-04 0.02035  2.25345E-01 0.00111 ];
INF_S2                    (idx, [1:   8]) = [  6.75308E-02 0.00067 -9.15489E-04 0.00601  3.32354E-04 0.02295  5.78906E-02 0.00333 ];
INF_S3                    (idx, [1:   8]) = [  7.09691E-03 0.00404 -1.05624E-03 0.00334  1.10414E-04 0.06283  1.76272E-02 0.01081 ];
INF_S4                    (idx, [1:   8]) = [ -5.77830E-03 0.00465 -3.32927E-04 0.01195 -9.10276E-06 0.68910 -3.27259E-03 0.03838 ];
INF_S5                    (idx, [1:   8]) = [  6.97322E-04 0.04665  1.98915E-05 0.21103 -5.81541E-05 0.10718  3.12070E-03 0.04348 ];
INF_S6                    (idx, [1:   8]) = [  3.82881E-03 0.00656 -8.68924E-05 0.04451 -6.70311E-05 0.07324 -7.69934E-03 0.01549 ];
INF_S7                    (idx, [1:   8]) = [  6.89777E-04 0.02907 -1.02881E-04 0.04010 -5.79159E-05 0.09370 -1.91105E-04 0.57994 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  3.92086E-01 0.00021  1.03350E-02 0.00071  1.85858E-03 0.00993  8.51913E-01 0.00032 ];
INF_SP1                   (idx, [1:   8]) = [  1.65022E-01 0.00033  2.93435E-03 0.00183  5.92153E-04 0.02035  2.25345E-01 0.00111 ];
INF_SP2                   (idx, [1:   8]) = [  6.75312E-02 0.00067 -9.15489E-04 0.00601  3.32354E-04 0.02295  5.78906E-02 0.00333 ];
INF_SP3                   (idx, [1:   8]) = [  7.09644E-03 0.00403 -1.05624E-03 0.00334  1.10414E-04 0.06283  1.76272E-02 0.01081 ];
INF_SP4                   (idx, [1:   8]) = [ -5.77892E-03 0.00464 -3.32927E-04 0.01195 -9.10276E-06 0.68910 -3.27259E-03 0.03838 ];
INF_SP5                   (idx, [1:   8]) = [  6.97523E-04 0.04659  1.98915E-05 0.21103 -5.81541E-05 0.10718  3.12070E-03 0.04348 ];
INF_SP6                   (idx, [1:   8]) = [  3.82849E-03 0.00656 -8.68924E-05 0.04451 -6.70311E-05 0.07324 -7.69934E-03 0.01549 ];
INF_SP7                   (idx, [1:   8]) = [  6.90116E-04 0.02908 -1.02881E-04 0.04010 -5.79159E-05 0.09370 -1.91105E-04 0.57994 ];

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

CMM_TRANSPXS              (idx, [1:   4]) = [  1.90303E-01 0.00141  5.86532E-01 0.00496 ];
CMM_TRANSPXS_X            (idx, [1:   4]) = [  1.90102E-01 0.00217  5.86235E-01 0.00985 ];
CMM_TRANSPXS_Y            (idx, [1:   4]) = [  1.90710E-01 0.00200  5.85651E-01 0.00844 ];
CMM_TRANSPXS_Z            (idx, [1:   4]) = [  1.90135E-01 0.00239  5.90199E-01 0.00878 ];
CMM_DIFFCOEF              (idx, [1:   4]) = [  1.75168E+00 0.00141  5.68647E-01 0.00494 ];
CMM_DIFFCOEF_X            (idx, [1:   4]) = [  1.75364E+00 0.00216  5.69942E-01 0.00997 ];
CMM_DIFFCOEF_Y            (idx, [1:   4]) = [  1.74803E+00 0.00200  5.70154E-01 0.00855 ];
CMM_DIFFCOEF_Z            (idx, [1:   4]) = [  1.75337E+00 0.00238  5.65844E-01 0.00893 ];

% Delayed neutron parameters (Meulekamp method):

BETA_EFF                  (idx, [1:  18]) = [  7.19168E-03 0.01761  1.94342E-04 0.10530  9.78979E-04 0.04695  6.11601E-04 0.05815  1.28083E-03 0.03966  2.37758E-03 0.03170  8.48191E-04 0.05260  6.24085E-04 0.05526  2.76083E-04 0.08994 ];
LAMBDA                    (idx, [1:  18]) = [  4.87871E-01 0.02848  1.24667E-02 0.0E+00  2.82917E-02 0.0E+00  4.25244E-02 5.7E-09  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 4.9E-09  3.55460E+00 0.0E+00 ];

