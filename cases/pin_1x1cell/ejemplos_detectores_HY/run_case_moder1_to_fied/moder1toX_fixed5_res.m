
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
TITLE                     (idx, [1: 16])  = 'Single+fuel+cell' ;
CONFIDENTIAL_DATA         (idx, 1)        = 0 ;
INPUT_FILE_NAME           (idx, [1: 16])  = 'moder1toX_fixed5' ;
WORKING_DIRECTORY         (idx, [1:122])  = '/home/hirepan/Documents/chalmers/Project/codes/Shynt/repo/cases/pin_1x1cell/ejemplos_detectores_HY/run_case_moder1_to_fied' ;
HOSTNAME                  (idx, [1:  4])  = 'thor' ;
CPU_TYPE                  (idx, [1: 40])  = 'Intel(R) Core(TM) i9-10900 CPU @ 2.80GHz' ;
CPU_MHZ                   (idx, 1)        = 236.0 ;
START_DATE                (idx, [1: 24])  = 'Mon Dec 13 12:02:04 2021' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Mon Dec 13 12:02:34 2021' ;

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
OMP_HISTORY_PROFILE       (idx, [1:  18]) = [  9.99570E-01  1.02707E+00  9.50095E-01  1.03567E+00  9.43212E-01  9.56406E-01  9.52564E-01  1.14752E+00  9.70517E-01  1.07988E+00  9.53071E-01  9.90611E-01  9.53676E-01  9.59349E-01  1.01746E+00  1.10912E+00  9.77236E-01  9.76975E-01  ];
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

MIN_MACROXS               (idx, [1:   4]) = [  5.00000E-02 1.5E-09  0.00000E+00 0.0E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  2.99698E-03 0.00312  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.97003E-01 9.4E-06  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  8.31844E-01 8.6E-05  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  8.29658E-01 0.00010  0.00000E+00 0.0E+00 ];
AVG_TRACKING_LOOPS        (idx, [1:   8]) = [  5.64668E+00 0.00110  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  2.92215E+01 0.00059  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  2.92215E+01 0.00059  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  5.99973E+00 0.00080  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  4.59198E+01 0.00054  0.00000E+00 0.0E+00 ];
LOST_PARTICLES            (idx, 1)        = 0 ;

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 500 ;
SIMULATED_HISTORIES       (idx, 1)        = 1000545 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  2.00109E+03 0.00149 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  2.00109E+03 0.00149 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  8.96550E+00 ;
RUNNING_TIME              (idx, 1)        =  5.10100E-01 ;
INIT_TIME                 (idx, [1:  2])  = [  1.16500E-02  1.16500E-02 ];
PROCESS_TIME              (idx, [1:  2])  = [  1.00001E-04  1.00001E-04 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  4.98283E-01  4.98283E-01  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  5.10017E-01  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 17.57597 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  1.79445E+01 0.00143 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  9.60955E-01 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 64027.77 ;
ALLOC_MEMSIZE             (idx, 1)        = 390.09;
MEMSIZE                   (idx, 1)        = 203.14;
XS_MEMSIZE                (idx, 1)        = 74.10;
MAT_MEMSIZE               (idx, 1)        = 6.90;
RES_MEMSIZE               (idx, 1)        = 1.56;
IFC_MEMSIZE               (idx, 1)        = 0.00;
MISC_MEMSIZE              (idx, 1)        = 120.58;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 186.95;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 3 ;
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

NORM_COEF                 (idx, [1:   4]) = [  4.99750E-04 0.00084  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  7.85772E-01 0.00208 ];
U235_FISS                 (idx, [1:   4]) = [  4.21889E-01 0.00125  9.08889E-01 0.00046 ];
U238_FISS                 (idx, [1:   4]) = [  4.23129E-02 0.00491  9.11108E-02 0.00455 ];
U235_CAPT                 (idx, [1:   4]) = [  9.33095E-02 0.00315  1.73713E-01 0.00302 ];
U238_CAPT                 (idx, [1:   4]) = [  4.04536E-01 0.00156  7.52941E-01 0.00080 ];

% Neutron balance (particles/weight):

BALA_SRC_NEUTRON_SRC     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_FISS    (idx, [1:  2])  = [ 1000545 1.00000E+06 ];
BALA_SRC_NEUTRON_NXN     (idx, [1:  2])  = [ 0 1.96285E+03 ];
BALA_SRC_NEUTRON_VR      (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_TOT     (idx, [1:  2])  = [ 1000545 1.00196E+06 ];

BALA_LOSS_NEUTRON_CAPT    (idx, [1:  2])  = [ 536730 5.37502E+05 ];
BALA_LOSS_NEUTRON_FISS    (idx, [1:  2])  = [ 463815 4.64461E+05 ];
BALA_LOSS_NEUTRON_LEAK    (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_CUT     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_ERR     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_TOT     (idx, [1:  2])  = [ 1000545 1.00196E+06 ];

BALA_NEUTRON_DIFF         (idx, [1:  2])  = [ 0 3.14321E-09 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.50396E-11 0.00054 ];
TOT_POWDENS               (idx, [1:   2]) = [  2.77237E-15 0.00054 ];
TOT_GENRATE               (idx, [1:   2]) = [  1.14520E+00 0.00053 ];
TOT_FISSRATE              (idx, [1:   2]) = [  4.63301E-01 0.00054 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  5.36699E-01 0.00047 ];
TOT_ABSRATE               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.99499E-01 0.00084 ];
TOT_FLUX                  (idx, [1:   2]) = [  5.92240E+01 0.00066 ];
TOT_PHOTON_PRODRATE       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  2.92576E+01 0.00053 ];
INI_FMASS                 (idx, 1)        =  5.42481E-03 ;
TOT_FMASS                 (idx, 1)        =  5.42481E-03 ;

% Six-factor formula:

SIX_FF_ETA                (idx, [1:   2]) = [  1.67829E+00 0.00090 ];
SIX_FF_F                  (idx, [1:   2]) = [  9.42599E-01 0.00034 ];
SIX_FF_P                  (idx, [1:   2]) = [  5.51521E-01 0.00089 ];
SIX_FF_EPSILON            (idx, [1:   2]) = [  1.31632E+00 0.00077 ];
SIX_FF_LF                 (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
SIX_FF_LT                 (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
SIX_FF_KINF               (idx, [1:   2]) = [  1.14811E+00 0.00103 ];
SIX_FF_KEFF               (idx, [1:   2]) = [  1.14811E+00 0.00103 ];

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.47183E+00 3.6E-05 ];
FISSE                     (idx, [1:   2]) = [  2.02611E+02 3.1E-06 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.14816E+00 0.00106  1.13994E+00 0.00104  8.16434E-03 0.01691 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.14742E+00 0.00054 ];
COL_KEFF                  (idx, [1:   2]) = [  1.14625E+00 0.00112 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.14742E+00 0.00054 ];
ABS_KINF                  (idx, [1:   2]) = [  1.14742E+00 0.00054 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% ALF (Average lethargy of neutrons causing fission):
% Based on E0 = 2.000000E+01 MeV

ANA_ALF                   (idx, [1:   2]) = [  1.69351E+01 0.00045 ];
IMP_ALF                   (idx, [1:   2]) = [  1.69395E+01 0.00022 ];

% EALF (Energy corresponding to average lethargy of neutrons causing fission):

ANA_EALF                  (idx, [1:   2]) = [  8.96278E-07 0.00766 ];
IMP_EALF                  (idx, [1:   2]) = [  8.82685E-07 0.00372 ];

% AFGE (Average energy of neutrons causing fission):

ANA_AFGE                  (idx, [1:   2]) = [  2.98923E-01 0.00514 ];
IMP_AFGE                  (idx, [1:   2]) = [  2.98188E-01 0.00230 ];

% Forward-weighted delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
FWD_ANA_BETA_ZERO         (idx, [1:  18]) = [  6.72015E-03 0.01159  1.85715E-04 0.06933  9.65642E-04 0.03135  5.37018E-04 0.04004  1.23868E-03 0.02727  2.17575E-03 0.02114  7.61390E-04 0.03343  6.02915E-04 0.03795  2.53047E-04 0.05722 ];
FWD_ANA_LAMBDA            (idx, [1:  18]) = [  4.85148E-01 0.01879  4.21374E-03 0.06265  2.51230E-02 0.01590  2.97671E-02 0.02931  1.25592E-01 0.01090  2.89543E-01 0.00450  5.57184E-01 0.01983  1.23916E+00 0.02529  1.59957E+00 0.04949 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  18]) = [  7.13036E-03 0.01764  1.63251E-04 0.10868  1.04475E-03 0.04884  5.07242E-04 0.06050  1.35537E-03 0.04124  2.30279E-03 0.03153  8.23041E-04 0.05170  6.70837E-04 0.06059  2.63080E-04 0.09101 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  18]) = [  4.92639E-01 0.02794  1.24667E-02 0.0E+00  2.82917E-02 0.0E+00  4.25244E-02 6.0E-09  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 4.9E-09  3.55460E+00 0.0E+00 ];

% Adjoint weighted time constants using Nauchi's method:

IFP_CHAIN_LENGTH          (idx, 1)        = 15 ;
ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  2.94695E-05 0.00234  2.94373E-05 0.00235  3.35942E-05 0.02307 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  3.38160E-05 0.00206  3.37789E-05 0.00207  3.85783E-05 0.02320 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  18]) = [  7.10913E-03 0.01701  2.23302E-04 0.09868  9.65966E-04 0.04902  5.22627E-04 0.06191  1.32972E-03 0.03988  2.34798E-03 0.02967  7.96145E-04 0.05372  6.38846E-04 0.05893  2.84549E-04 0.08568 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  18]) = [  5.01015E-01 0.03107  1.24667E-02 0.0E+00  2.82917E-02 5.5E-09  4.25244E-02 8.2E-09  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 5.7E-09  3.55460E+00 4.9E-09 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  2.94724E-05 0.00531  2.94271E-05 0.00534  2.41962E-05 0.05908 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  3.38256E-05 0.00528  3.37736E-05 0.00530  2.77783E-05 0.05917 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  18]) = [  6.95945E-03 0.05365  1.90175E-04 0.27904  8.43111E-04 0.14673  5.20211E-04 0.20678  1.36271E-03 0.12614  2.39095E-03 0.08882  6.03234E-04 0.18399  6.00745E-04 0.16051  4.48309E-04 0.23617 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  18]) = [  5.25758E-01 0.07286  1.24667E-02 5.4E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 3.7E-09  2.92467E-01 5.7E-09  6.66488E-01 0.0E+00  1.63478E+00 0.0E+00  3.55460E+00 5.4E-09 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  18]) = [  6.94437E-03 0.05167  1.75603E-04 0.27312  8.35511E-04 0.14398  5.46715E-04 0.20839  1.40300E-03 0.12342  2.35954E-03 0.08616  6.03202E-04 0.17856  6.30203E-04 0.15393  3.90600E-04 0.23134 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  18]) = [  5.24397E-01 0.07208  1.24667E-02 3.8E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 3.7E-09  2.92467E-01 5.7E-09  6.66488E-01 0.0E+00  1.63478E+00 0.0E+00  3.55460E+00 3.8E-09 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -2.41608E+02 0.05483 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  2.95368E-05 0.00143 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  3.38932E-05 0.00092 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  7.13797E-03 0.00981 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -2.41830E+02 0.00984 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  4.15211E-07 0.00113 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  4.25827E-06 0.00096  4.25861E-06 0.00096  4.19898E-06 0.01255 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.95825E-05 0.00133  3.95835E-05 0.00134  3.96081E-05 0.01629 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.51989E-01 0.00089  5.51248E-01 0.00090  7.09957E-01 0.02052 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.21456E+01 0.02633 ];
ANA_MEAN_NCOL             (idx, [1:   4]) = [  2.92215E+01 0.00059  3.33136E+01 0.00078 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  1])  = '0' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  2.00000E+01  6.06550E+00  3.67900E+00  2.23100E+00  1.35300E+00  8.21000E-01  5.00000E-01  3.02500E-01  1.83000E-01  1.11000E-01  6.74300E-02  4.08500E-02  2.47800E-02  1.50300E-02  9.11800E-03  5.50000E-03  3.51910E-03  2.23945E-03  1.42510E-03  9.06898E-04  3.67262E-04  1.48728E-04  7.55014E-05  4.80520E-05  2.77000E-05  1.59680E-05  9.87700E-06  4.00000E-06  3.30000E-06  2.60000E-06  2.10000E-06  1.85500E-06  1.50000E-06  1.30000E-06  1.15000E-06  1.12300E-06  1.09700E-06  1.07100E-06  1.04500E-06  1.02000E-06  9.96000E-07  9.72000E-07  9.50000E-07  9.10000E-07  8.50000E-07  7.80000E-07  6.25000E-07  5.00000E-07  4.00000E-07  3.50000E-07  3.20000E-07  3.00000E-07  2.80000E-07  2.50000E-07  2.20000E-07  1.80000E-07  1.40000E-07  1.00000E-07  8.00000E-08  6.70000E-08  5.80000E-08  5.00000E-08  4.20000E-08  3.50000E-08  3.00000E-08  2.50000E-08  2.00000E-08  1.50000E-08  1.00000E-08  5.00000E-09  1.00000E-11 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Micro-group spectrum:

INF_MICRO_FLX             (idx, [1: 140]) = [  1.69473E+04 0.00727  7.03608E+04 0.00325  1.47829E+05 0.00186  1.56607E+05 0.00175  1.50068E+05 0.00126  1.80624E+05 0.00161  1.22304E+05 0.00103  1.13709E+05 0.00128  8.62628E+04 0.00158  7.01954E+04 0.00181  6.08515E+04 0.00179  5.45325E+04 0.00194  5.02047E+04 0.00152  4.76266E+04 0.00170  4.61839E+04 0.00167  3.97903E+04 0.00178  3.92304E+04 0.00155  3.85881E+04 0.00187  3.75909E+04 0.00186  7.27834E+04 0.00188  6.95744E+04 0.00165  4.91536E+04 0.00177  3.15302E+04 0.00210  3.54924E+04 0.00242  3.25865E+04 0.00179  3.02137E+04 0.00273  4.65037E+04 0.00184  1.08716E+04 0.00302  1.36022E+04 0.00325  1.24235E+04 0.00336  7.22794E+03 0.00405  1.25800E+04 0.00360  8.53129E+03 0.00420  7.26385E+03 0.00390  1.38963E+03 0.00779  1.35845E+03 0.00762  1.39854E+03 0.00747  1.44524E+03 0.00716  1.43906E+03 0.00858  1.42344E+03 0.00661  1.46635E+03 0.00681  1.36791E+03 0.00887  2.57186E+03 0.00704  4.11158E+03 0.00461  5.26543E+03 0.00461  1.37825E+04 0.00316  1.44783E+04 0.00329  1.55713E+04 0.00308  1.02100E+04 0.00260  7.40687E+03 0.00312  5.55883E+03 0.00435  6.45454E+03 0.00442  1.16793E+04 0.00256  1.51120E+04 0.00254  2.75006E+04 0.00245  3.98538E+04 0.00209  5.61433E+04 0.00231  3.44187E+04 0.00277  2.41783E+04 0.00210  1.70850E+04 0.00244  1.51113E+04 0.00242  1.47295E+04 0.00298  1.22019E+04 0.00246  8.14716E+03 0.00356  7.49105E+03 0.00351  6.58215E+03 0.00295  5.50244E+03 0.00255  4.30881E+03 0.00353  2.84580E+03 0.00382  9.99540E+02 0.00516 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.14626E+00 0.00128 ];

% Flux spectra in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  5.01464E+01 0.00091  9.08448E+00 0.00099 ];
INF_FISS_FLX              (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  4.14160E-01 0.00022  9.35035E-01 0.00031 ];
INF_CAPT                  (idx, [1:   4]) = [  6.85513E-03 0.00104  2.12548E-02 0.00058 ];
INF_ABS                   (idx, [1:   4]) = [  8.97232E-03 0.00087  6.05875E-02 0.00070 ];
INF_FISS                  (idx, [1:   4]) = [  2.11719E-03 0.00092  3.93327E-02 0.00077 ];
INF_NSF                   (idx, [1:   4]) = [  5.48709E-03 0.00093  9.58222E-02 0.00077 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.59169E+00 9.8E-05  2.43620E+00 2.7E-09 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.03758E+02 7.5E-06  2.02270E+02 2.7E-09 ];
INF_INVV                  (idx, [1:   4]) = [  5.56322E-08 0.00075  2.40030E-06 0.00043 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  4.05182E-01 0.00023  8.74354E-01 0.00035 ];
INF_SCATT1                (idx, [1:   4]) = [  1.69155E-01 0.00043  2.21703E-01 0.00090 ];
INF_SCATT2                (idx, [1:   4]) = [  6.70109E-02 0.00058  5.48579E-02 0.00234 ];
INF_SCATT3                (idx, [1:   4]) = [  6.05496E-03 0.00606  1.65129E-02 0.00475 ];
INF_SCATT4                (idx, [1:   4]) = [ -6.21177E-03 0.00503 -3.99666E-03 0.01977 ];
INF_SCATT5                (idx, [1:   4]) = [  6.28333E-04 0.04229  3.20848E-03 0.03336 ];
INF_SCATT6                (idx, [1:   4]) = [  3.75017E-03 0.00539 -8.50132E-03 0.00935 ];
INF_SCATT7                (idx, [1:   4]) = [  6.17839E-04 0.04244 -1.34577E-04 0.48928 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  4.05221E-01 0.00023  8.74354E-01 0.00035 ];
INF_SCATTP1               (idx, [1:   4]) = [  1.69155E-01 0.00043  2.21703E-01 0.00090 ];
INF_SCATTP2               (idx, [1:   4]) = [  6.70116E-02 0.00058  5.48579E-02 0.00234 ];
INF_SCATTP3               (idx, [1:   4]) = [  6.05458E-03 0.00606  1.65129E-02 0.00475 ];
INF_SCATTP4               (idx, [1:   4]) = [ -6.21162E-03 0.00503 -3.99666E-03 0.01977 ];
INF_SCATTP5               (idx, [1:   4]) = [  6.28512E-04 0.04231  3.20848E-03 0.03336 ];
INF_SCATTP6               (idx, [1:   4]) = [  3.75052E-03 0.00539 -8.50132E-03 0.00935 ];
INF_SCATTP7               (idx, [1:   4]) = [  6.17754E-04 0.04246 -1.34577E-04 0.48928 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  1.85510E-01 0.00049  6.38213E-01 0.00045 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.79686E+00 0.00049  5.22294E-01 0.00045 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  8.93320E-03 0.00087  6.05875E-02 0.00070 ];
INF_REMXS                 (idx, [1:   4]) = [  2.02003E-02 0.00041  6.19482E-02 0.00108 ];

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

INF_S0                    (idx, [1:   8]) = [  3.93960E-01 0.00022  1.12224E-02 0.00086  1.26783E-03 0.00915  8.73086E-01 0.00035 ];
INF_S1                    (idx, [1:   8]) = [  1.65948E-01 0.00043  3.20723E-03 0.00255  4.19980E-04 0.02018  2.21283E-01 0.00091 ];
INF_S2                    (idx, [1:   8]) = [  6.79758E-02 0.00057 -9.64917E-04 0.00772  2.39589E-04 0.02842  5.46183E-02 0.00236 ];
INF_S3                    (idx, [1:   8]) = [  7.20152E-03 0.00503 -1.14656E-03 0.00495  8.42033E-05 0.05914  1.64287E-02 0.00486 ];
INF_S4                    (idx, [1:   8]) = [ -5.82940E-03 0.00543 -3.82374E-04 0.01208 -2.63968E-06 1.00000 -3.99402E-03 0.02008 ];
INF_S5                    (idx, [1:   8]) = [  6.18924E-04 0.04020  9.40940E-06 0.46302 -3.86512E-05 0.09305  3.24713E-03 0.03308 ];
INF_S6                    (idx, [1:   8]) = [  3.84174E-03 0.00516 -9.15641E-05 0.04698 -4.43770E-05 0.08857 -8.45694E-03 0.00955 ];
INF_S7                    (idx, [1:   8]) = [  7.17248E-04 0.03775 -9.94091E-05 0.03349 -4.36987E-05 0.05943 -9.08780E-05 0.73660 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  3.93999E-01 0.00022  1.12224E-02 0.00086  1.26783E-03 0.00915  8.73086E-01 0.00035 ];
INF_SP1                   (idx, [1:   8]) = [  1.65948E-01 0.00043  3.20723E-03 0.00255  4.19980E-04 0.02018  2.21283E-01 0.00091 ];
INF_SP2                   (idx, [1:   8]) = [  6.79765E-02 0.00057 -9.64917E-04 0.00772  2.39589E-04 0.02842  5.46183E-02 0.00236 ];
INF_SP3                   (idx, [1:   8]) = [  7.20114E-03 0.00503 -1.14656E-03 0.00495  8.42033E-05 0.05914  1.64287E-02 0.00486 ];
INF_SP4                   (idx, [1:   8]) = [ -5.82924E-03 0.00544 -3.82374E-04 0.01208 -2.63968E-06 1.00000 -3.99402E-03 0.02008 ];
INF_SP5                   (idx, [1:   8]) = [  6.19103E-04 0.04023  9.40940E-06 0.46302 -3.86512E-05 0.09305  3.24713E-03 0.03308 ];
INF_SP6                   (idx, [1:   8]) = [  3.84208E-03 0.00516 -9.15641E-05 0.04698 -4.43770E-05 0.08857 -8.45694E-03 0.00955 ];
INF_SP7                   (idx, [1:   8]) = [  7.17163E-04 0.03776 -9.94091E-05 0.03349 -4.36987E-05 0.05943 -9.08780E-05 0.73660 ];

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

CMM_TRANSPXS              (idx, [1:   4]) = [  1.91818E-01 0.00104  5.92027E-01 0.00552 ];
CMM_TRANSPXS_X            (idx, [1:   4]) = [  1.91993E-01 0.00206  5.91501E-01 0.00806 ];
CMM_TRANSPXS_Y            (idx, [1:   4]) = [  1.92101E-01 0.00226  5.96888E-01 0.00884 ];
CMM_TRANSPXS_Z            (idx, [1:   4]) = [  1.91401E-01 0.00170  5.89630E-01 0.00903 ];
CMM_DIFFCOEF              (idx, [1:   4]) = [  1.73781E+00 0.00104  5.63451E-01 0.00554 ];
CMM_DIFFCOEF_X            (idx, [1:   4]) = [  1.73635E+00 0.00206  5.64430E-01 0.00817 ];
CMM_DIFFCOEF_Y            (idx, [1:   4]) = [  1.73541E+00 0.00226  5.59506E-01 0.00888 ];
CMM_DIFFCOEF_Z            (idx, [1:   4]) = [  1.74167E+00 0.00171  5.66417E-01 0.00890 ];

% Delayed neutron parameters (Meulekamp method):

BETA_EFF                  (idx, [1:  18]) = [  7.13036E-03 0.01764  1.63251E-04 0.10868  1.04475E-03 0.04884  5.07242E-04 0.06050  1.35537E-03 0.04124  2.30279E-03 0.03153  8.23041E-04 0.05170  6.70837E-04 0.06059  2.63080E-04 0.09101 ];
LAMBDA                    (idx, [1:  18]) = [  4.92639E-01 0.02794  1.24667E-02 0.0E+00  2.82917E-02 0.0E+00  4.25244E-02 6.0E-09  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 4.9E-09  3.55460E+00 0.0E+00 ];

