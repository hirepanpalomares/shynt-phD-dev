
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
TITLE                     (idx, [1: 11])  = 'pin_problem' ;
CONFIDENTIAL_DATA         (idx, 1)        = 0 ;
INPUT_FILE_NAME           (idx, [1: 21])  = 'global_problem_1.serp' ;
WORKING_DIRECTORY         (idx, [1: 89])  = '/home/hirepan/Documents/chalmers/Project/codes/Shynt/repo/cases/pin_1x1cell/serpent_files' ;
HOSTNAME                  (idx, [1:  4])  = 'thor' ;
CPU_TYPE                  (idx, [1: 40])  = 'Intel(R) Core(TM) i9-10900 CPU @ 2.80GHz' ;
CPU_MHZ                   (idx, 1)        = 236.0 ;
START_DATE                (idx, [1: 24])  = 'Wed Nov  3 12:28:23 2021' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Wed Nov  3 12:28:49 2021' ;

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
OMP_HISTORY_PROFILE       (idx, [1:  18]) = [  1.04561E+00  9.57108E-01  9.70187E-01  9.74079E-01  9.69305E-01  9.73670E-01  9.62716E-01  9.72803E-01  1.17687E+00  1.12581E+00  1.08728E+00  9.53119E-01  9.70743E-01  9.71201E-01  9.70596E-01  9.74667E-01  9.69566E-01  9.74667E-01  ];
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

MIN_MACROXS               (idx, [1:   4]) = [  5.00000E-02 4.1E-09  0.00000E+00 0.0E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  3.41775E-03 0.00298  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.96582E-01 1.0E-05  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  8.29106E-01 0.00010  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  8.29471E-01 0.00010  0.00000E+00 0.0E+00 ];
AVG_TRACKING_LOOPS        (idx, [1:   8]) = [  3.45746E+00 0.00068  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  2.92271E+01 0.00060  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  2.92271E+01 0.00060  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  6.00883E+00 0.00080  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  4.59369E+01 0.00051  0.00000E+00 0.0E+00 ];
LOST_PARTICLES            (idx, 1)        = 0 ;

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 500 ;
SIMULATED_HISTORIES       (idx, 1)        = 1000597 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  2.00119E+03 0.00163 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  2.00119E+03 0.00163 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  7.52578E+00 ;
RUNNING_TIME              (idx, 1)        =  4.29000E-01 ;
INIT_TIME                 (idx, [1:  2])  = [  1.13000E-02  1.13000E-02 ];
PROCESS_TIME              (idx, [1:  2])  = [  1.00001E-04  1.00001E-04 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  4.17533E-01  4.17533E-01  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  4.28917E-01  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 17.54262 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  1.79926E+01 0.00160 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  9.57032E-01 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 64032.54 ;
ALLOC_MEMSIZE             (idx, 1)        = 390.10;
MEMSIZE                   (idx, 1)        = 203.18;
XS_MEMSIZE                (idx, 1)        = 74.10;
MAT_MEMSIZE               (idx, 1)        = 6.90;
RES_MEMSIZE               (idx, 1)        = 1.58;
IFC_MEMSIZE               (idx, 1)        = 0.00;
MISC_MEMSIZE              (idx, 1)        = 120.60;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 186.92;

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

NORM_COEF                 (idx, [1:   4]) = [  4.99544E-04 0.00086  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  7.85433E-01 0.00217 ];
U235_FISS                 (idx, [1:   4]) = [  4.21884E-01 0.00124  9.08623E-01 0.00046 ];
U238_FISS                 (idx, [1:   4]) = [  4.24595E-02 0.00503  9.13774E-02 0.00457 ];
U235_CAPT                 (idx, [1:   4]) = [  9.31938E-02 0.00333  1.73639E-01 0.00304 ];
U238_CAPT                 (idx, [1:   4]) = [  4.04287E-01 0.00170  7.53189E-01 0.00080 ];

% Neutron balance (particles/weight):

BALA_SRC_NEUTRON_SRC     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_FISS    (idx, [1:  2])  = [ 1000597 1.00000E+06 ];
BALA_SRC_NEUTRON_NXN     (idx, [1:  2])  = [ 0 1.99988E+03 ];
BALA_SRC_NEUTRON_VR      (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_TOT     (idx, [1:  2])  = [ 1000597 1.00200E+06 ];

BALA_LOSS_NEUTRON_CAPT    (idx, [1:  2])  = [ 536392 5.37184E+05 ];
BALA_LOSS_NEUTRON_FISS    (idx, [1:  2])  = [ 464205 4.64816E+05 ];
BALA_LOSS_NEUTRON_LEAK    (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_CUT     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_ERR     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_TOT     (idx, [1:  2])  = [ 1000597 1.00200E+06 ];

BALA_NEUTRON_DIFF         (idx, [1:  2])  = [ 0 1.51340E-09 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.50414E-11 0.00056 ];
TOT_POWDENS               (idx, [1:   2]) = [  2.77270E-15 0.00056 ];
TOT_GENRATE               (idx, [1:   2]) = [  1.14533E+00 0.00056 ];
TOT_FISSRATE              (idx, [1:   2]) = [  4.63356E-01 0.00057 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  5.36644E-01 0.00049 ];
TOT_ABSRATE               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.99087E-01 0.00086 ];
TOT_FLUX                  (idx, [1:   2]) = [  5.91860E+01 0.00064 ];
TOT_PHOTON_PRODRATE       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  2.92509E+01 0.00050 ];
INI_FMASS                 (idx, 1)        =  5.42481E-03 ;
TOT_FMASS                 (idx, 1)        =  5.42481E-03 ;

% Six-factor formula:

SIX_FF_ETA                (idx, [1:   2]) = [  1.67722E+00 0.00093 ];
SIX_FF_F                  (idx, [1:   2]) = [  9.42889E-01 0.00034 ];
SIX_FF_P                  (idx, [1:   2]) = [  5.51362E-01 0.00095 ];
SIX_FF_EPSILON            (idx, [1:   2]) = [  1.31829E+00 0.00087 ];
SIX_FF_LF                 (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
SIX_FF_LT                 (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
SIX_FF_KINF               (idx, [1:   2]) = [  1.14909E+00 0.00114 ];
SIX_FF_KEFF               (idx, [1:   2]) = [  1.14909E+00 0.00114 ];

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.47182E+00 3.8E-05 ];
FISSE                     (idx, [1:   2]) = [  2.02611E+02 3.2E-06 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.14879E+00 0.00114  1.14074E+00 0.00114  8.35422E-03 0.01751 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.14757E+00 0.00056 ];
COL_KEFF                  (idx, [1:   2]) = [  1.14689E+00 0.00117 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.14757E+00 0.00056 ];
ABS_KINF                  (idx, [1:   2]) = [  1.14757E+00 0.00056 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% ALF (Average lethargy of neutrons causing fission):
% Based on E0 = 2.000000E+01 MeV

ANA_ALF                   (idx, [1:   2]) = [  1.69305E+01 0.00049 ];
IMP_ALF                   (idx, [1:   2]) = [  1.69407E+01 0.00024 ];

% EALF (Energy corresponding to average lethargy of neutrons causing fission):

ANA_EALF                  (idx, [1:   2]) = [  9.03249E-07 0.00853 ];
IMP_EALF                  (idx, [1:   2]) = [  8.82189E-07 0.00409 ];

% AFGE (Average energy of neutrons causing fission):

ANA_AFGE                  (idx, [1:   2]) = [  3.00390E-01 0.00516 ];
IMP_AFGE                  (idx, [1:   2]) = [  2.98074E-01 0.00243 ];

% Forward-weighted delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
FWD_ANA_BETA_ZERO         (idx, [1:  18]) = [  6.72354E-03 0.01173  1.97553E-04 0.06805  9.71070E-04 0.03101  5.45723E-04 0.03923  1.23245E-03 0.02778  2.12966E-03 0.01962  7.71828E-04 0.03479  6.20085E-04 0.03906  2.55166E-04 0.05828 ];
FWD_ANA_LAMBDA            (idx, [1:  18]) = [  4.89712E-01 0.01878  4.46308E-03 0.05995  2.52362E-02 0.01558  3.08727E-02 0.02750  1.26390E-01 0.01027  2.90127E-01 0.00402  5.51852E-01 0.02040  1.19339E+00 0.02723  1.54981E+00 0.05092 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  18]) = [  7.34199E-03 0.01840  2.10636E-04 0.10572  1.05970E-03 0.04782  5.68288E-04 0.05788  1.32477E-03 0.04080  2.34648E-03 0.03368  8.24848E-04 0.05030  7.08293E-04 0.06101  2.98971E-04 0.08350 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  18]) = [  5.10828E-01 0.02836  1.24667E-02 0.0E+00  2.82917E-02 0.0E+00  4.25244E-02 5.8E-09  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 4.9E-09  3.55460E+00 0.0E+00 ];

% Adjoint weighted time constants using Nauchi's method:

IFP_CHAIN_LENGTH          (idx, 1)        = 15 ;
ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  2.94274E-05 0.00242  2.93991E-05 0.00242  3.27265E-05 0.02668 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  3.37841E-05 0.00214  3.37516E-05 0.00214  3.75967E-05 0.02667 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  18]) = [  7.28804E-03 0.01773  2.04603E-04 0.09962  1.04005E-03 0.04486  6.50379E-04 0.05620  1.32605E-03 0.04314  2.24831E-03 0.02993  8.26009E-04 0.05345  6.99085E-04 0.05803  2.93552E-04 0.08100 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  18]) = [  5.05781E-01 0.02889  1.24667E-02 0.0E+00  2.82917E-02 3.8E-09  4.25244E-02 8.2E-09  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 5.5E-09  3.55460E+00 4.8E-09 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  2.94274E-05 0.00541  2.94098E-05 0.00541  2.14490E-05 0.05988 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  3.37758E-05 0.00520  3.37563E-05 0.00520  2.46418E-05 0.05981 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  18]) = [  7.44097E-03 0.05344  1.78472E-04 0.30367  1.09518E-03 0.14892  6.93910E-04 0.18202  1.52729E-03 0.11883  2.14108E-03 0.09493  9.12361E-04 0.16335  6.76780E-04 0.15656  2.15901E-04 0.26021 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  18]) = [  4.89211E-01 0.06842  1.24667E-02 5.4E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 3.2E-09  2.92467E-01 5.0E-09  6.66488E-01 4.6E-09  1.63478E+00 0.0E+00  3.55460E+00 4.7E-09 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  18]) = [  7.55814E-03 0.05233  2.07544E-04 0.29104  1.10055E-03 0.14495  7.06106E-04 0.17786  1.54405E-03 0.11457  2.14921E-03 0.09413  9.26293E-04 0.16200  7.09754E-04 0.15343  2.14630E-04 0.24715 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  18]) = [  4.87253E-01 0.06843  1.24667E-02 2.7E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 3.2E-09  2.92467E-01 4.8E-09  6.66488E-01 4.2E-09  1.63478E+00 0.0E+00  3.55460E+00 2.7E-09 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -2.57622E+02 0.05401 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  2.94314E-05 0.00151 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  3.37875E-05 0.00093 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  7.51282E-03 0.01035 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -2.55512E+02 0.01046 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  4.15924E-07 0.00122 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  4.26479E-06 0.00103  4.26557E-06 0.00103  4.17622E-06 0.01147 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.96659E-05 0.00130  3.96656E-05 0.00130  3.95324E-05 0.01625 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.51834E-01 0.00095  5.51095E-01 0.00096  7.15997E-01 0.02099 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.21554E+01 0.02673 ];
ANA_MEAN_NCOL             (idx, [1:   4]) = [  2.92271E+01 0.00060  3.33212E+01 0.00083 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  1])  = '0' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  2.00000E+01  6.06550E+00  3.67900E+00  2.23100E+00  1.35300E+00  8.21000E-01  5.00000E-01  3.02500E-01  1.83000E-01  1.11000E-01  6.74300E-02  4.08500E-02  2.47800E-02  1.50300E-02  9.11800E-03  5.50000E-03  3.51910E-03  2.23945E-03  1.42510E-03  9.06898E-04  3.67262E-04  1.48728E-04  7.55014E-05  4.80520E-05  2.77000E-05  1.59680E-05  9.87700E-06  4.00000E-06  3.30000E-06  2.60000E-06  2.10000E-06  1.85500E-06  1.50000E-06  1.30000E-06  1.15000E-06  1.12300E-06  1.09700E-06  1.07100E-06  1.04500E-06  1.02000E-06  9.96000E-07  9.72000E-07  9.50000E-07  9.10000E-07  8.50000E-07  7.80000E-07  6.25000E-07  5.00000E-07  4.00000E-07  3.50000E-07  3.20000E-07  3.00000E-07  2.80000E-07  2.50000E-07  2.20000E-07  1.80000E-07  1.40000E-07  1.00000E-07  8.00000E-08  6.70000E-08  5.80000E-08  5.00000E-08  4.20000E-08  3.50000E-08  3.00000E-08  2.50000E-08  2.00000E-08  1.50000E-08  1.00000E-08  5.00000E-09  1.00000E-11 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Micro-group spectrum:

INF_MICRO_FLX             (idx, [1: 140]) = [  1.69649E+04 0.00651  6.98676E+04 0.00500  1.48181E+05 0.00194  1.56650E+05 0.00205  1.49677E+05 0.00154  1.80421E+05 0.00153  1.22065E+05 0.00150  1.13612E+05 0.00127  8.64100E+04 0.00178  7.02134E+04 0.00119  6.08391E+04 0.00137  5.42719E+04 0.00153  5.01466E+04 0.00161  4.75850E+04 0.00110  4.63128E+04 0.00187  3.96670E+04 0.00209  3.92279E+04 0.00164  3.85777E+04 0.00177  3.75511E+04 0.00152  7.27025E+04 0.00140  6.96600E+04 0.00129  4.92664E+04 0.00178  3.14391E+04 0.00220  3.54848E+04 0.00160  3.25301E+04 0.00198  3.01862E+04 0.00141  4.67311E+04 0.00133  1.08282E+04 0.00280  1.36611E+04 0.00228  1.24596E+04 0.00334  7.21458E+03 0.00446  1.25466E+04 0.00385  8.52296E+03 0.00432  7.23005E+03 0.00368  1.39792E+03 0.00827  1.36842E+03 0.00722  1.40507E+03 0.00931  1.44516E+03 0.00618  1.43307E+03 0.00840  1.41091E+03 0.00556  1.46803E+03 0.00664  1.38904E+03 0.00701  2.59513E+03 0.00650  4.15468E+03 0.00479  5.25879E+03 0.00451  1.38386E+04 0.00260  1.45525E+04 0.00357  1.55898E+04 0.00327  1.01948E+04 0.00442  7.36522E+03 0.00311  5.58947E+03 0.00421  6.43447E+03 0.00409  1.17086E+04 0.00380  1.50894E+04 0.00303  2.75947E+04 0.00250  3.99312E+04 0.00190  5.60603E+04 0.00191  3.45570E+04 0.00212  2.42068E+04 0.00204  1.70538E+04 0.00259  1.51690E+04 0.00235  1.47927E+04 0.00277  1.22163E+04 0.00246  8.18120E+03 0.00299  7.47693E+03 0.00302  6.56371E+03 0.00240  5.54231E+03 0.00262  4.31569E+03 0.00279  2.86622E+03 0.00373  1.00206E+03 0.00521 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.14691E+00 0.00110 ];

% Flux spectra in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  5.01009E+01 0.00096  9.09278E+00 0.00087 ];
INF_FISS_FLX              (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  4.14217E-01 0.00026  9.35278E-01 0.00024 ];
INF_CAPT                  (idx, [1:   4]) = [  6.85838E-03 0.00101  2.12463E-02 0.00051 ];
INF_ABS                   (idx, [1:   4]) = [  8.97710E-03 0.00078  6.05534E-02 0.00061 ];
INF_FISS                  (idx, [1:   4]) = [  2.11872E-03 0.00099  3.93070E-02 0.00067 ];
INF_NSF                   (idx, [1:   4]) = [  5.49100E-03 0.00102  9.57598E-02 0.00067 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.59165E+00 9.4E-05  2.43620E+00 4.7E-09 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.03758E+02 7.4E-06  2.02270E+02 0.0E+00 ];
INF_INVV                  (idx, [1:   4]) = [  5.57294E-08 0.00086  2.40083E-06 0.00029 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  4.05230E-01 0.00026  8.74696E-01 0.00027 ];
INF_SCATT1                (idx, [1:   4]) = [  1.69210E-01 0.00033  2.21955E-01 0.00082 ];
INF_SCATT2                (idx, [1:   4]) = [  6.70293E-02 0.00071  5.50480E-02 0.00223 ];
INF_SCATT3                (idx, [1:   4]) = [  6.09788E-03 0.00692  1.67105E-02 0.00673 ];
INF_SCATT4                (idx, [1:   4]) = [ -6.23938E-03 0.00539 -3.94183E-03 0.02857 ];
INF_SCATT5                (idx, [1:   4]) = [  5.71917E-04 0.05592  3.24789E-03 0.02933 ];
INF_SCATT6                (idx, [1:   4]) = [  3.66696E-03 0.00780 -8.41231E-03 0.01138 ];
INF_SCATT7                (idx, [1:   4]) = [  5.57632E-04 0.04251 -1.16652E-04 0.72690 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  4.05270E-01 0.00026  8.74696E-01 0.00027 ];
INF_SCATTP1               (idx, [1:   4]) = [  1.69210E-01 0.00033  2.21955E-01 0.00082 ];
INF_SCATTP2               (idx, [1:   4]) = [  6.70295E-02 0.00072  5.50480E-02 0.00223 ];
INF_SCATTP3               (idx, [1:   4]) = [  6.09852E-03 0.00691  1.67105E-02 0.00673 ];
INF_SCATTP4               (idx, [1:   4]) = [ -6.23928E-03 0.00539 -3.94183E-03 0.02857 ];
INF_SCATTP5               (idx, [1:   4]) = [  5.72058E-04 0.05600  3.24789E-03 0.02933 ];
INF_SCATTP6               (idx, [1:   4]) = [  3.66740E-03 0.00780 -8.41231E-03 0.01138 ];
INF_SCATTP7               (idx, [1:   4]) = [  5.57357E-04 0.04247 -1.16652E-04 0.72690 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  1.85553E-01 0.00086  6.38144E-01 0.00036 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.79646E+00 0.00086  5.22350E-01 0.00036 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  8.93722E-03 0.00081  6.05534E-02 0.00061 ];
INF_REMXS                 (idx, [1:   4]) = [  2.02109E-02 0.00045  6.18481E-02 0.00093 ];

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

INF_S0                    (idx, [1:   8]) = [  3.94006E-01 0.00026  1.12248E-02 0.00096  1.26626E-03 0.01170  8.73430E-01 0.00028 ];
INF_S1                    (idx, [1:   8]) = [  1.66001E-01 0.00033  3.20940E-03 0.00214  4.28772E-04 0.01678  2.21526E-01 0.00082 ];
INF_S2                    (idx, [1:   8]) = [  6.79965E-02 0.00072 -9.67193E-04 0.00681  2.28494E-04 0.02376  5.48195E-02 0.00225 ];
INF_S3                    (idx, [1:   8]) = [  7.23428E-03 0.00576 -1.13640E-03 0.00496  7.99887E-05 0.05951  1.66305E-02 0.00674 ];
INF_S4                    (idx, [1:   8]) = [ -5.86502E-03 0.00568 -3.74357E-04 0.01198 -6.10184E-06 0.65553 -3.93573E-03 0.02849 ];
INF_S5                    (idx, [1:   8]) = [  5.63888E-04 0.05644  8.02840E-06 0.45680 -4.14359E-05 0.06340  3.28933E-03 0.02907 ];
INF_S6                    (idx, [1:   8]) = [  3.75404E-03 0.00788 -8.70845E-05 0.05091 -4.82958E-05 0.05878 -8.36401E-03 0.01148 ];
INF_S7                    (idx, [1:   8]) = [  6.64620E-04 0.03307 -1.06988E-04 0.03472 -4.75332E-05 0.05417 -6.91188E-05 1.00000 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  3.94045E-01 0.00026  1.12248E-02 0.00096  1.26626E-03 0.01170  8.73430E-01 0.00028 ];
INF_SP1                   (idx, [1:   8]) = [  1.66001E-01 0.00033  3.20940E-03 0.00214  4.28772E-04 0.01678  2.21526E-01 0.00082 ];
INF_SP2                   (idx, [1:   8]) = [  6.79967E-02 0.00072 -9.67193E-04 0.00681  2.28494E-04 0.02376  5.48195E-02 0.00225 ];
INF_SP3                   (idx, [1:   8]) = [  7.23492E-03 0.00575 -1.13640E-03 0.00496  7.99887E-05 0.05951  1.66305E-02 0.00674 ];
INF_SP4                   (idx, [1:   8]) = [ -5.86492E-03 0.00568 -3.74357E-04 0.01198 -6.10184E-06 0.65553 -3.93573E-03 0.02849 ];
INF_SP5                   (idx, [1:   8]) = [  5.64029E-04 0.05650  8.02840E-06 0.45680 -4.14359E-05 0.06340  3.28933E-03 0.02907 ];
INF_SP6                   (idx, [1:   8]) = [  3.75449E-03 0.00788 -8.70845E-05 0.05091 -4.82958E-05 0.05878 -8.36401E-03 0.01148 ];
INF_SP7                   (idx, [1:   8]) = [  6.64345E-04 0.03304 -1.06988E-04 0.03472 -4.75332E-05 0.05417 -6.91188E-05 1.00000 ];

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

CMM_TRANSPXS              (idx, [1:   4]) = [  1.91322E-01 0.00145  5.92330E-01 0.00526 ];
CMM_TRANSPXS_X            (idx, [1:   4]) = [  1.91924E-01 0.00172  5.99320E-01 0.00843 ];
CMM_TRANSPXS_Y            (idx, [1:   4]) = [  1.91152E-01 0.00212  5.90592E-01 0.01113 ];
CMM_TRANSPXS_Z            (idx, [1:   4]) = [  1.90921E-01 0.00218  5.89940E-01 0.00901 ];
CMM_DIFFCOEF              (idx, [1:   4]) = [  1.74235E+00 0.00145  5.63123E-01 0.00525 ];
CMM_DIFFCOEF_X            (idx, [1:   4]) = [  1.73692E+00 0.00172  5.57126E-01 0.00835 ];
CMM_DIFFCOEF_Y            (idx, [1:   4]) = [  1.74400E+00 0.00213  5.66087E-01 0.01115 ];
CMM_DIFFCOEF_Z            (idx, [1:   4]) = [  1.74612E+00 0.00218  5.66155E-01 0.00920 ];

% Delayed neutron parameters (Meulekamp method):

BETA_EFF                  (idx, [1:  18]) = [  7.34199E-03 0.01840  2.10636E-04 0.10572  1.05970E-03 0.04782  5.68288E-04 0.05788  1.32477E-03 0.04080  2.34648E-03 0.03368  8.24848E-04 0.05030  7.08293E-04 0.06101  2.98971E-04 0.08350 ];
LAMBDA                    (idx, [1:  18]) = [  5.10828E-01 0.02836  1.24667E-02 0.0E+00  2.82917E-02 0.0E+00  4.25244E-02 5.8E-09  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 4.9E-09  3.55460E+00 0.0E+00 ];

