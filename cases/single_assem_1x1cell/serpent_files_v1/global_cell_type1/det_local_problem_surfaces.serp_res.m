
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
INPUT_FILE_NAME           (idx, [1:148])  = '/home/hirepan/Documents/chalmers/Project/codes/Shynt/repo/cases/single_assem_1x1cell/serpent_files/global_cell_type1/det_local_problem_surfaces.serp' ;
WORKING_DIRECTORY         (idx, [1: 84])  = '/home/hirepan/Documents/chalmers/Project/codes/Shynt/repo/cases/single_assem_1x1cell' ;
HOSTNAME                  (idx, [1:  4])  = 'thor' ;
CPU_TYPE                  (idx, [1: 40])  = 'Intel(R) Core(TM) i9-10900 CPU @ 2.80GHz' ;
CPU_MHZ                   (idx, 1)        = 236.0 ;
START_DATE                (idx, [1: 24])  = 'Thu Mar 10 11:43:05 2022' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Mar 10 11:43:43 2022' ;

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
OMP_HISTORY_PROFILE       (idx, [1:  18]) = [  1.09670E+00  1.01690E+00  9.48098E-01  9.43013E-01  9.46888E-01  9.45842E-01  9.99549E-01  9.43700E-01  9.44910E-01  1.26889E+00  1.07517E+00  1.05682E+00  9.50060E-01  1.06472E+00  9.45221E-01  9.63009E-01  9.43733E-01  9.46790E-01  ];
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

MIN_MACROXS               (idx, [1:   4]) = [  5.00000E-02 6.0E-09  0.00000E+00 0.0E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  3.46916E-03 0.00282  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.96531E-01 9.8E-06  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  8.31157E-01 0.00010  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  8.31527E-01 0.00010  0.00000E+00 0.0E+00 ];
AVG_TRACKING_LOOPS        (idx, [1:   8]) = [  3.44697E+00 0.00068  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  2.82449E+01 0.00057  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  2.82449E+01 0.00057  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  5.72272E+00 0.00080  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  4.50680E+01 0.00053  0.00000E+00 0.0E+00 ];
LOST_PARTICLES            (idx, 1)        = 0 ;

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 500 ;
SIMULATED_HISTORIES       (idx, 1)        = 1000464 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  2.00093E+03 0.00148 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  2.00093E+03 0.00148 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  1.10860E+01 ;
RUNNING_TIME              (idx, 1)        =  6.29600E-01 ;
INIT_TIME                 (idx, [1:  2])  = [  1.24000E-02  1.24000E-02 ];
PROCESS_TIME              (idx, [1:  2])  = [  1.16666E-04  1.16666E-04 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  6.17083E-01  6.17083E-01  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  6.29567E-01  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 17.60798 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  1.79521E+01 0.00123 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  9.61589E-01 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 64024.21 ;
ALLOC_MEMSIZE             (idx, 1)        = 390.13;
MEMSIZE                   (idx, 1)        = 203.20;
XS_MEMSIZE                (idx, 1)        = 74.10;
MAT_MEMSIZE               (idx, 1)        = 6.90;
RES_MEMSIZE               (idx, 1)        = 1.58;
IFC_MEMSIZE               (idx, 1)        = 0.00;
MISC_MEMSIZE              (idx, 1)        = 120.62;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 186.93;

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

NORM_COEF                 (idx, [1:   4]) = [  4.98852E-04 0.00086  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  7.25697E-01 0.00203 ];
U235_FISS                 (idx, [1:   4]) = [  4.35799E-01 0.00122  9.12851E-01 0.00045 ];
U238_FISS                 (idx, [1:   4]) = [  4.16288E-02 0.00508  8.71490E-02 0.00473 ];
U235_CAPT                 (idx, [1:   4]) = [  9.86381E-02 0.00310  1.88906E-01 0.00283 ];
U238_CAPT                 (idx, [1:   4]) = [  3.87606E-01 0.00161  7.42264E-01 0.00081 ];

% Neutron balance (particles/weight):

BALA_SRC_NEUTRON_SRC     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_FISS    (idx, [1:  2])  = [ 1000464 1.00000E+06 ];
BALA_SRC_NEUTRON_NXN     (idx, [1:  2])  = [ 0 1.91223E+03 ];
BALA_SRC_NEUTRON_VR      (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_TOT     (idx, [1:  2])  = [ 1000464 1.00191E+06 ];

BALA_LOSS_NEUTRON_CAPT    (idx, [1:  2])  = [ 522511 5.23351E+05 ];
BALA_LOSS_NEUTRON_FISS    (idx, [1:  2])  = [ 477953 4.78561E+05 ];
BALA_LOSS_NEUTRON_LEAK    (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_CUT     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_ERR     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_TOT     (idx, [1:  2])  = [ 1000464 1.00191E+06 ];

BALA_NEUTRON_DIFF         (idx, [1:  2])  = [ 0 -2.21189E-09 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.55176E-11 0.00055 ];
TOT_POWDENS               (idx, [1:   2]) = [  2.86049E-15 0.00055 ];
TOT_GENRATE               (idx, [1:   2]) = [  1.18114E+00 0.00054 ];
TOT_FISSRATE              (idx, [1:   2]) = [  4.78057E-01 0.00055 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  5.21943E-01 0.00051 ];
TOT_ABSRATE               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.97704E-01 0.00086 ];
TOT_FLUX                  (idx, [1:   2]) = [  5.79881E+01 0.00068 ];
TOT_PHOTON_PRODRATE       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  2.82267E+01 0.00055 ];
INI_FMASS                 (idx, 1)        =  5.42481E-03 ;
TOT_FMASS                 (idx, 1)        =  5.42481E-03 ;

% Six-factor formula:

SIX_FF_ETA                (idx, [1:   2]) = [  1.72428E+00 0.00089 ];
SIX_FF_F                  (idx, [1:   2]) = [  9.47935E-01 0.00031 ];
SIX_FF_P                  (idx, [1:   2]) = [  5.41458E-01 0.00093 ];
SIX_FF_EPSILON            (idx, [1:   2]) = [  1.33647E+00 0.00085 ];
SIX_FF_LF                 (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
SIX_FF_LT                 (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
SIX_FF_KINF               (idx, [1:   2]) = [  1.18238E+00 0.00103 ];
SIX_FF_KEFF               (idx, [1:   2]) = [  1.18238E+00 0.00103 ];

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.47071E+00 3.6E-05 ];
FISSE                     (idx, [1:   2]) = [  2.02598E+02 3.1E-06 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.18253E+00 0.00104  1.17362E+00 0.00104  8.75718E-03 0.01720 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.18344E+00 0.00054 ];
COL_KEFF                  (idx, [1:   2]) = [  1.18439E+00 0.00117 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.18344E+00 0.00054 ];
ABS_KINF                  (idx, [1:   2]) = [  1.18344E+00 0.00054 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% ALF (Average lethargy of neutrons causing fission):
% Based on E0 = 2.000000E+01 MeV

ANA_ALF                   (idx, [1:   2]) = [  1.68719E+01 0.00047 ];
IMP_ALF                   (idx, [1:   2]) = [  1.68624E+01 0.00023 ];

% EALF (Energy corresponding to average lethargy of neutrons causing fission):

ANA_EALF                  (idx, [1:   2]) = [  9.56081E-07 0.00802 ];
IMP_EALF                  (idx, [1:   2]) = [  9.53823E-07 0.00395 ];

% AFGE (Average energy of neutrons causing fission):

ANA_AFGE                  (idx, [1:   2]) = [  2.89093E-01 0.00516 ];
IMP_AFGE                  (idx, [1:   2]) = [  2.89472E-01 0.00235 ];

% Forward-weighted delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
FWD_ANA_BETA_ZERO         (idx, [1:  18]) = [  6.61271E-03 0.01204  1.64074E-04 0.07336  9.53718E-04 0.02867  5.18894E-04 0.04192  1.25448E-03 0.02503  2.04506E-03 0.02130  7.66935E-04 0.03342  6.68307E-04 0.03523  2.41246E-04 0.05652 ];
FWD_ANA_LAMBDA            (idx, [1:  18]) = [  4.98688E-01 0.01753  3.93948E-03 0.06586  2.59152E-02 0.01356  2.93418E-02 0.03001  1.25858E-01 0.01070  2.89543E-01 0.00450  5.59850E-01 0.01954  1.30456E+00 0.02252  1.59246E+00 0.04969 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  18]) = [  7.55673E-03 0.01851  1.97560E-04 0.11232  1.04652E-03 0.04619  5.84812E-04 0.06376  1.39350E-03 0.03866  2.44831E-03 0.03040  8.52388E-04 0.04998  7.45514E-04 0.05793  2.88118E-04 0.09935 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  18]) = [  4.93189E-01 0.02578  1.24667E-02 0.0E+00  2.82917E-02 0.0E+00  4.25244E-02 6.2E-09  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 5.2E-09  3.55460E+00 0.0E+00 ];

% Adjoint weighted time constants using Nauchi's method:

IFP_CHAIN_LENGTH          (idx, 1)        = 15 ;
ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  2.54875E-05 0.00239  2.54632E-05 0.00238  2.90995E-05 0.02603 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  3.01234E-05 0.00214  3.00945E-05 0.00214  3.44075E-05 0.02600 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  18]) = [  7.40268E-03 0.01727  1.68560E-04 0.11155  1.07340E-03 0.04516  5.39015E-04 0.06188  1.40812E-03 0.03880  2.35885E-03 0.02896  8.29108E-04 0.04916  7.60613E-04 0.05250  2.65018E-04 0.09332 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  18]) = [  4.92461E-01 0.02795  1.24667E-02 0.0E+00  2.82917E-02 3.6E-09  4.25244E-02 8.3E-09  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 5.5E-09  3.55460E+00 5.0E-09 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  2.54573E-05 0.00517  2.54230E-05 0.00521  2.09425E-05 0.05770 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  3.00863E-05 0.00503  3.00454E-05 0.00507  2.47971E-05 0.05784 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  18]) = [  7.03797E-03 0.05401  7.53412E-05 0.35415  1.12300E-03 0.12937  4.38847E-04 0.17317  1.32042E-03 0.12019  2.28106E-03 0.09979  7.88266E-04 0.15581  7.85621E-04 0.16959  2.25416E-04 0.27326 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  18]) = [  5.00302E-01 0.07141  1.24667E-02 0.0E+00  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 3.2E-09  2.92467E-01 4.9E-09  6.66488E-01 4.6E-09  1.63478E+00 0.0E+00  3.55460E+00 0.0E+00 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  18]) = [  7.01898E-03 0.05151  8.43697E-05 0.34898  1.15187E-03 0.12660  4.51234E-04 0.16476  1.24663E-03 0.11542  2.27658E-03 0.09445  7.65533E-04 0.14904  7.89471E-04 0.16312  2.53295E-04 0.27072 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  18]) = [  5.07290E-01 0.07156  1.24667E-02 0.0E+00  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 3.2E-09  2.92467E-01 5.2E-09  6.66488E-01 5.1E-09  1.63478E+00 0.0E+00  3.55460E+00 0.0E+00 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -2.80609E+02 0.05440 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  2.55621E-05 0.00144 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  3.02113E-05 0.00098 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  7.35169E-03 0.01136 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -2.87680E+02 0.01133 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  3.77202E-07 0.00117 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  4.23709E-06 0.00105  4.23681E-06 0.00105  4.23525E-06 0.01173 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.54376E-05 0.00127  3.54302E-05 0.00128  3.62671E-05 0.01571 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.41975E-01 0.00093  5.41094E-01 0.00094  7.38120E-01 0.02506 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.16031E+01 0.02561 ];
ANA_MEAN_NCOL             (idx, [1:   4]) = [  2.82449E+01 0.00057  3.20352E+01 0.00080 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  1])  = '0' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  2.00000E+01  6.06550E+00  3.67900E+00  2.23100E+00  1.35300E+00  8.21000E-01  5.00000E-01  3.02500E-01  1.83000E-01  1.11000E-01  6.74300E-02  4.08500E-02  2.47800E-02  1.50300E-02  9.11800E-03  5.50000E-03  3.51910E-03  2.23945E-03  1.42510E-03  9.06898E-04  3.67262E-04  1.48728E-04  7.55014E-05  4.80520E-05  2.77000E-05  1.59680E-05  9.87700E-06  4.00000E-06  3.30000E-06  2.60000E-06  2.10000E-06  1.85500E-06  1.50000E-06  1.30000E-06  1.15000E-06  1.12300E-06  1.09700E-06  1.07100E-06  1.04500E-06  1.02000E-06  9.96000E-07  9.72000E-07  9.50000E-07  9.10000E-07  8.50000E-07  7.80000E-07  6.25000E-07  5.00000E-07  4.00000E-07  3.50000E-07  3.20000E-07  3.00000E-07  2.80000E-07  2.50000E-07  2.20000E-07  1.80000E-07  1.40000E-07  1.00000E-07  8.00000E-08  6.70000E-08  5.80000E-08  5.00000E-08  4.20000E-08  3.50000E-08  3.00000E-08  2.50000E-08  2.00000E-08  1.50000E-08  1.00000E-08  5.00000E-09  1.00000E-11 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Micro-group spectrum:

INF_MICRO_FLX             (idx, [1: 140]) = [  1.69556E+04 0.00774  6.98705E+04 0.00261  1.47702E+05 0.00178  1.56759E+05 0.00130  1.49882E+05 0.00197  1.80872E+05 0.00154  1.22143E+05 0.00121  1.13575E+05 0.00126  8.61894E+04 0.00164  7.03052E+04 0.00174  6.07106E+04 0.00135  5.43079E+04 0.00149  5.02244E+04 0.00158  4.74591E+04 0.00158  4.61916E+04 0.00175  3.97243E+04 0.00195  3.92141E+04 0.00234  3.85638E+04 0.00202  3.75485E+04 0.00221  7.27061E+04 0.00148  6.89702E+04 0.00179  4.87936E+04 0.00153  3.12661E+04 0.00179  3.51441E+04 0.00254  3.21706E+04 0.00163  2.97727E+04 0.00192  4.59858E+04 0.00215  1.06263E+04 0.00437  1.34893E+04 0.00312  1.22476E+04 0.00430  7.06500E+03 0.00496  1.23676E+04 0.00365  8.40934E+03 0.00454  7.12181E+03 0.00440  1.34395E+03 0.00912  1.33278E+03 0.00630  1.38250E+03 0.00598  1.44983E+03 0.00801  1.40376E+03 0.00785  1.38995E+03 0.00851  1.43764E+03 0.00960  1.35355E+03 0.00807  2.55668E+03 0.00482  4.03932E+03 0.00634  5.15245E+03 0.00505  1.35473E+04 0.00357  1.42896E+04 0.00328  1.50498E+04 0.00332  9.75783E+03 0.00254  6.98212E+03 0.00389  5.25018E+03 0.00402  5.97806E+03 0.00343  1.07560E+04 0.00349  1.37804E+04 0.00290  2.48103E+04 0.00184  3.55048E+04 0.00146  4.94139E+04 0.00186  3.01431E+04 0.00215  2.09811E+04 0.00228  1.47453E+04 0.00241  1.30767E+04 0.00238  1.27535E+04 0.00213  1.05012E+04 0.00263  6.98674E+03 0.00261  6.40516E+03 0.00221  5.62762E+03 0.00253  4.70991E+03 0.00256  3.66997E+03 0.00363  2.40449E+03 0.00461  8.43049E+02 0.00428 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.18438E+00 0.00096 ];

% Flux spectra in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  4.99031E+01 0.00060  8.09178E+00 0.00098 ];
INF_FISS_FLX              (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  4.13951E-01 0.00026  9.36066E-01 0.00021 ];
INF_CAPT                  (idx, [1:   4]) = [  6.90320E-03 0.00107  2.19480E-02 0.00067 ];
INF_ABS                   (idx, [1:   4]) = [  9.21495E-03 0.00086  6.67970E-02 0.00079 ];
INF_FISS                  (idx, [1:   4]) = [  2.31176E-03 0.00094  4.48490E-02 0.00085 ];
INF_NSF                   (idx, [1:   4]) = [  5.96246E-03 0.00098  1.09261E-01 0.00085 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.57919E+00 0.00010  2.43620E+00 0.0E+00 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.03630E+02 7.3E-06  2.02270E+02 3.8E-09 ];
INF_INVV                  (idx, [1:   4]) = [  5.50397E-08 0.00111  2.36422E-06 0.00031 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  4.04745E-01 0.00027  8.69304E-01 0.00027 ];
INF_SCATT1                (idx, [1:   4]) = [  1.68941E-01 0.00038  2.22625E-01 0.00116 ];
INF_SCATT2                (idx, [1:   4]) = [  6.68744E-02 0.00071  5.55780E-02 0.00320 ];
INF_SCATT3                (idx, [1:   4]) = [  6.04214E-03 0.00642  1.69923E-02 0.00751 ];
INF_SCATT4                (idx, [1:   4]) = [ -6.25025E-03 0.00544 -3.79286E-03 0.03109 ];
INF_SCATT5                (idx, [1:   4]) = [  6.41088E-04 0.03760  3.24853E-03 0.03042 ];
INF_SCATT6                (idx, [1:   4]) = [  3.75854E-03 0.00783 -8.15971E-03 0.01253 ];
INF_SCATT7                (idx, [1:   4]) = [  6.05594E-04 0.03842 -1.14970E-04 0.93233 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  4.04783E-01 0.00027  8.69304E-01 0.00027 ];
INF_SCATTP1               (idx, [1:   4]) = [  1.68942E-01 0.00038  2.22625E-01 0.00116 ];
INF_SCATTP2               (idx, [1:   4]) = [  6.68747E-02 0.00071  5.55780E-02 0.00320 ];
INF_SCATTP3               (idx, [1:   4]) = [  6.04189E-03 0.00642  1.69923E-02 0.00751 ];
INF_SCATTP4               (idx, [1:   4]) = [ -6.25022E-03 0.00546 -3.79286E-03 0.03109 ];
INF_SCATTP5               (idx, [1:   4]) = [  6.41172E-04 0.03769  3.24853E-03 0.03042 ];
INF_SCATTP6               (idx, [1:   4]) = [  3.75829E-03 0.00781 -8.15971E-03 0.01253 ];
INF_SCATTP7               (idx, [1:   4]) = [  6.05482E-04 0.03844 -1.14970E-04 0.93233 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  1.85401E-01 0.00062  6.37826E-01 0.00044 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.79792E+00 0.00062  5.22611E-01 0.00044 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  9.17672E-03 0.00087  6.67970E-02 0.00079 ];
INF_REMXS                 (idx, [1:   4]) = [  2.02609E-02 0.00040  6.81784E-02 0.00113 ];

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

INF_S0                    (idx, [1:   8]) = [  3.93690E-01 0.00027  1.10550E-02 0.00087  1.41662E-03 0.00846  8.67887E-01 0.00028 ];
INF_S1                    (idx, [1:   8]) = [  1.65799E-01 0.00038  3.14224E-03 0.00237  4.77914E-04 0.01326  2.22147E-01 0.00117 ];
INF_S2                    (idx, [1:   8]) = [  6.78373E-02 0.00068 -9.62968E-04 0.00718  2.52786E-04 0.02486  5.53252E-02 0.00322 ];
INF_S3                    (idx, [1:   8]) = [  7.16278E-03 0.00539 -1.12064E-03 0.00383  9.46975E-05 0.06867  1.68976E-02 0.00737 ];
INF_S4                    (idx, [1:   8]) = [ -5.87581E-03 0.00609 -3.74437E-04 0.01176 -1.70703E-06 1.00000 -3.79116E-03 0.03094 ];
INF_S5                    (idx, [1:   8]) = [  6.22405E-04 0.03996  1.86831E-05 0.18571 -4.17230E-05 0.10495  3.29025E-03 0.03048 ];
INF_S6                    (idx, [1:   8]) = [  3.84236E-03 0.00750 -8.38134E-05 0.03498 -5.27999E-05 0.06574 -8.10691E-03 0.01261 ];
INF_S7                    (idx, [1:   8]) = [  7.11226E-04 0.03220 -1.05632E-04 0.02763 -4.57834E-05 0.06900 -6.91865E-05 1.00000 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  3.93728E-01 0.00027  1.10550E-02 0.00087  1.41662E-03 0.00846  8.67887E-01 0.00028 ];
INF_SP1                   (idx, [1:   8]) = [  1.65799E-01 0.00038  3.14224E-03 0.00237  4.77914E-04 0.01326  2.22147E-01 0.00117 ];
INF_SP2                   (idx, [1:   8]) = [  6.78376E-02 0.00067 -9.62968E-04 0.00718  2.52786E-04 0.02486  5.53252E-02 0.00322 ];
INF_SP3                   (idx, [1:   8]) = [  7.16253E-03 0.00539 -1.12064E-03 0.00383  9.46975E-05 0.06867  1.68976E-02 0.00737 ];
INF_SP4                   (idx, [1:   8]) = [ -5.87579E-03 0.00611 -3.74437E-04 0.01176 -1.70703E-06 1.00000 -3.79116E-03 0.03094 ];
INF_SP5                   (idx, [1:   8]) = [  6.22489E-04 0.04004  1.86831E-05 0.18571 -4.17230E-05 0.10495  3.29025E-03 0.03048 ];
INF_SP6                   (idx, [1:   8]) = [  3.84210E-03 0.00749 -8.38134E-05 0.03498 -5.27999E-05 0.06574 -8.10691E-03 0.01261 ];
INF_SP7                   (idx, [1:   8]) = [  7.11114E-04 0.03220 -1.05632E-04 0.02763 -4.57834E-05 0.06900 -6.91865E-05 1.00000 ];

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

CMM_TRANSPXS              (idx, [1:   4]) = [  1.91150E-01 0.00151  5.86783E-01 0.00489 ];
CMM_TRANSPXS_X            (idx, [1:   4]) = [  1.92007E-01 0.00228  5.92219E-01 0.00899 ];
CMM_TRANSPXS_Y            (idx, [1:   4]) = [  1.91187E-01 0.00209  5.76006E-01 0.00874 ];
CMM_TRANSPXS_Z            (idx, [1:   4]) = [  1.90303E-01 0.00236  5.94402E-01 0.00737 ];
CMM_DIFFCOEF              (idx, [1:   4]) = [  1.74393E+00 0.00151  5.68394E-01 0.00486 ];
CMM_DIFFCOEF_X            (idx, [1:   4]) = [  1.73627E+00 0.00229  5.63925E-01 0.00882 ];
CMM_DIFFCOEF_Y            (idx, [1:   4]) = [  1.74368E+00 0.00210  5.79762E-01 0.00876 ];
CMM_DIFFCOEF_Z            (idx, [1:   4]) = [  1.75183E+00 0.00236  5.61493E-01 0.00711 ];

% Delayed neutron parameters (Meulekamp method):

BETA_EFF                  (idx, [1:  18]) = [  7.55673E-03 0.01851  1.97560E-04 0.11232  1.04652E-03 0.04619  5.84812E-04 0.06376  1.39350E-03 0.03866  2.44831E-03 0.03040  8.52388E-04 0.04998  7.45514E-04 0.05793  2.88118E-04 0.09935 ];
LAMBDA                    (idx, [1:  18]) = [  4.93189E-01 0.02578  1.24667E-02 0.0E+00  2.82917E-02 0.0E+00  4.25244E-02 6.2E-09  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 5.2E-09  3.55460E+00 0.0E+00 ];

