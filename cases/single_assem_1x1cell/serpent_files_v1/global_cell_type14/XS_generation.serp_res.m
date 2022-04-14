
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
INPUT_FILE_NAME           (idx, [1:136])  = '/home/hirepan/Documents/chalmers/Project/codes/Shynt/repo/cases/single_assem_1x1cell/serpent_files/global_cell_type14/XS_generation.serp' ;
WORKING_DIRECTORY         (idx, [1: 84])  = '/home/hirepan/Documents/chalmers/Project/codes/Shynt/repo/cases/single_assem_1x1cell' ;
HOSTNAME                  (idx, [1:  4])  = 'thor' ;
CPU_TYPE                  (idx, [1: 40])  = 'Intel(R) Core(TM) i9-10900 CPU @ 2.80GHz' ;
CPU_MHZ                   (idx, 1)        = 236.0 ;
START_DATE                (idx, [1: 24])  = 'Thu Mar 10 11:53:15 2022' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Mar 10 11:53:24 2022' ;

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
OMP_HISTORY_PROFILE       (idx, [1:  18]) = [  9.55744E-01  1.00225E+00  9.95431E-01  9.91688E-01  9.80360E-01  1.02858E+00  1.04800E+00  1.00673E+00  1.04293E+00  9.82077E-01  1.00153E+00  9.92881E-01  9.86833E-01  9.74051E-01  1.00231E+00  1.00646E+00  9.92178E-01  1.00996E+00  ];
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

MIN_MACROXS               (idx, [1:   4]) = [  5.00000E-02 5.0E-09  0.00000E+00 0.0E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  8.70606E-03 0.00315  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.91294E-01 2.8E-05  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  8.37646E-01 0.00011  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  8.38032E-01 0.00011  0.00000E+00 0.0E+00 ];
AVG_TRACKING_LOOPS        (idx, [1:   8]) = [  2.31335E+00 0.00038  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  2.50515E+01 0.00054  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  2.50515E+01 0.00054  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  4.84181E+00 0.00081  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  1.90710E-01 0.00356  0.00000E+00 0.0E+00 ];
LOST_PARTICLES            (idx, 1)        = 0 ;

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 500 ;
SIMULATED_HISTORIES       (idx, 1)        = 1000567 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  2.00113E+03 0.00145 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  2.00113E+03 0.00145 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.32852E+00 ;
RUNNING_TIME              (idx, 1)        =  1.45267E-01 ;
INIT_TIME                 (idx, [1:  2])  = [  1.23333E-02  1.23333E-02 ];
PROCESS_TIME              (idx, [1:  2])  = [  1.16666E-04  1.16666E-04 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  1.32700E-01  1.32700E-01  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  1.45117E-01  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 16.02928 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  1.75686E+01 0.00427 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  7.49426E-01 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 64024.21 ;
ALLOC_MEMSIZE             (idx, 1)        = 390.09;
MEMSIZE                   (idx, 1)        = 204.06;
XS_MEMSIZE                (idx, 1)        = 74.10;
MAT_MEMSIZE               (idx, 1)        = 6.90;
RES_MEMSIZE               (idx, 1)        = 2.47;
IFC_MEMSIZE               (idx, 1)        = 0.00;
MISC_MEMSIZE              (idx, 1)        = 120.58;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 186.02;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 6 ;
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

NORM_COEF                 (idx, [1:   4]) = [  4.99716E-04 0.00080  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  5.58586E-01 0.00219 ];
U235_FISS                 (idx, [1:   4]) = [  4.80766E-01 0.00115  9.20774E-01 0.00040 ];
U238_FISS                 (idx, [1:   4]) = [  4.13903E-02 0.00503  7.92256E-02 0.00467 ];
U235_CAPT                 (idx, [1:   4]) = [  1.19691E-01 0.00283  2.49763E-01 0.00251 ];
U238_CAPT                 (idx, [1:   4]) = [  3.35213E-01 0.00175  6.99427E-01 0.00095 ];

% Neutron balance (particles/weight):

BALA_SRC_NEUTRON_SRC     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_FISS    (idx, [1:  2])  = [ 1000567 1.00000E+06 ];
BALA_SRC_NEUTRON_NXN     (idx, [1:  2])  = [ 0 1.98998E+03 ];
BALA_SRC_NEUTRON_VR      (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_TOT     (idx, [1:  2])  = [ 1000567 1.00199E+06 ];

BALA_LOSS_NEUTRON_CAPT    (idx, [1:  2])  = [ 478812 4.79499E+05 ];
BALA_LOSS_NEUTRON_FISS    (idx, [1:  2])  = [ 521755 5.22491E+05 ];
BALA_LOSS_NEUTRON_LEAK    (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_CUT     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_ERR     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_TOT     (idx, [1:  2])  = [ 1000567 1.00199E+06 ];

BALA_NEUTRON_DIFF         (idx, [1:  2])  = [ 0 -9.31323E-10 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.69293E-11 0.00054 ];
TOT_POWDENS               (idx, [1:   2]) = [  3.12072E-15 0.00054 ];
TOT_GENRATE               (idx, [1:   2]) = [  1.28768E+00 0.00054 ];
TOT_FISSRATE              (idx, [1:   2]) = [  5.21626E-01 0.00054 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  4.78374E-01 0.00059 ];
TOT_ABSRATE               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.99432E-01 0.00080 ];
TOT_FLUX                  (idx, [1:   2]) = [  5.42414E+01 0.00067 ];
TOT_PHOTON_PRODRATE       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  2.50814E+01 0.00053 ];
INI_FMASS                 (idx, 1)        =  5.42481E-03 ;
TOT_FMASS                 (idx, 1)        =  5.42481E-03 ;

% Six-factor formula:

SIX_FF_ETA                (idx, [1:   2]) = [  1.85744E+00 0.00082 ];
SIX_FF_F                  (idx, [1:   2]) = [  9.65717E-01 0.00027 ];
SIX_FF_P                  (idx, [1:   2]) = [  4.90491E-01 0.00101 ];
SIX_FF_EPSILON            (idx, [1:   2]) = [  1.46648E+00 0.00097 ];
SIX_FF_LF                 (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
SIX_FF_LT                 (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
SIX_FF_KINF               (idx, [1:   2]) = [  1.28968E+00 0.00099 ];
SIX_FF_KEFF               (idx, [1:   2]) = [  1.28968E+00 0.00099 ];

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.46859E+00 3.4E-05 ];
FISSE                     (idx, [1:   2]) = [  2.02568E+02 2.7E-06 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.28963E+00 0.00102  1.28047E+00 0.00099  9.20734E-03 0.01595 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.29017E+00 0.00054 ];
COL_KEFF                  (idx, [1:   2]) = [  1.28890E+00 0.00108 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.29017E+00 0.00054 ];
ABS_KINF                  (idx, [1:   2]) = [  1.29017E+00 0.00054 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% ALF (Average lethargy of neutrons causing fission):
% Based on E0 = 2.000000E+01 MeV

ANA_ALF                   (idx, [1:   2]) = [  1.63601E+01 0.00047 ];
IMP_ALF                   (idx, [1:   2]) = [  1.63519E+01 0.00024 ];

% EALF (Energy corresponding to average lethargy of neutrons causing fission):

ANA_EALF                  (idx, [1:   2]) = [  1.59379E-06 0.00786 ];
IMP_EALF                  (idx, [1:   2]) = [  1.58921E-06 0.00398 ];

% AFGE (Average energy of neutrons causing fission):

ANA_AFGE                  (idx, [1:   2]) = [  2.72772E-01 0.00509 ];
IMP_AFGE                  (idx, [1:   2]) = [  2.74849E-01 0.00235 ];

% Forward-weighted delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
FWD_ANA_BETA_ZERO         (idx, [1:  18]) = [  5.82853E-03 0.01206  1.50887E-04 0.07228  8.37322E-04 0.02908  5.17008E-04 0.03790  1.10426E-03 0.02697  1.81605E-03 0.02037  6.50140E-04 0.03664  5.28723E-04 0.03964  2.24130E-04 0.06008 ];
FWD_ANA_LAMBDA            (idx, [1:  18]) = [  4.83408E-01 0.01971  3.96441E-03 0.06556  2.48967E-02 0.01653  3.15531E-02 0.02640  1.24793E-01 0.01151  2.88958E-01 0.00493  5.31857E-01 0.02252  1.16069E+00 0.02861  1.54270E+00 0.05112 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  18]) = [  7.18991E-03 0.01735  1.74821E-04 0.10806  1.07162E-03 0.04375  6.53062E-04 0.06214  1.28679E-03 0.04070  2.26104E-03 0.03225  7.94022E-04 0.05098  6.56782E-04 0.05893  2.91771E-04 0.08778 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  18]) = [  4.89018E-01 0.02705  1.24667E-02 0.0E+00  2.82917E-02 0.0E+00  4.25244E-02 5.6E-09  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 5.0E-09  3.55460E+00 0.0E+00 ];

% Adjoint weighted time constants using Nauchi's method:

IFP_CHAIN_LENGTH          (idx, 1)        = 15 ;
ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  1.47478E-05 0.00228  1.47361E-05 0.00229  1.61743E-05 0.02236 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  1.90097E-05 0.00206  1.89947E-05 0.00208  2.08314E-05 0.02216 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  18]) = [  7.13624E-03 0.01632  2.03988E-04 0.09814  1.06485E-03 0.04098  6.43899E-04 0.05238  1.30110E-03 0.04015  2.22280E-03 0.02987  7.82025E-04 0.05046  6.44327E-04 0.05672  2.73253E-04 0.08545 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  18]) = [  4.77397E-01 0.02719  1.24667E-02 0.0E+00  2.82917E-02 0.0E+00  4.25244E-02 8.0E-09  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 5.5E-09  3.55460E+00 4.8E-09 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  1.49039E-05 0.00484  1.48899E-05 0.00486  1.22586E-05 0.05269 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  1.92082E-05 0.00467  1.91898E-05 0.00469  1.58135E-05 0.05273 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  18]) = [  6.82765E-03 0.05250  2.13848E-04 0.25717  1.13007E-03 0.12667  5.63039E-04 0.16917  1.42707E-03 0.10759  2.22671E-03 0.09309  6.32004E-04 0.15134  4.50184E-04 0.18787  1.84732E-04 0.25130 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  18]) = [  3.95057E-01 0.07212  1.24667E-02 2.7E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 4.4E-09  2.92467E-01 5.6E-09  6.66488E-01 4.8E-09  1.63478E+00 0.0E+00  3.55460E+00 6.0E-09 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  18]) = [  6.85168E-03 0.05156  2.02964E-04 0.27281  1.11151E-03 0.11892  5.73033E-04 0.15748  1.40878E-03 0.10677  2.21270E-03 0.09006  7.03454E-04 0.14570  4.63643E-04 0.18697  1.75604E-04 0.24473 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  18]) = [  3.91875E-01 0.07018  1.24667E-02 0.0E+00  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 4.6E-09  2.92467E-01 5.6E-09  6.66488E-01 4.8E-09  1.63478E+00 0.0E+00  3.55460E+00 4.7E-09 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -4.64263E+02 0.05410 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  1.48114E-05 0.00141 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  1.90920E-05 0.00105 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  7.12830E-03 0.01032 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -4.81909E+02 0.01048 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  2.54544E-07 0.00131 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  4.09916E-06 0.00112  4.09937E-06 0.00112  4.05422E-06 0.01338 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  2.30180E-05 0.00139  2.30149E-05 0.00140  2.33722E-05 0.01638 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  4.91147E-01 0.00101  4.90163E-01 0.00102  7.12182E-01 0.02172 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.25033E+01 0.02837 ];
ANA_MEAN_NCOL             (idx, [1:   4]) = [  2.50515E+01 0.00054  2.77443E+01 0.00074 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  7])  = 'u4gcu_1' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  2.00000E+01  6.06550E+00  3.67900E+00  2.23100E+00  1.35300E+00  8.21000E-01  5.00000E-01  3.02500E-01  1.83000E-01  1.11000E-01  6.74300E-02  4.08500E-02  2.47800E-02  1.50300E-02  9.11800E-03  5.50000E-03  3.51910E-03  2.23945E-03  1.42510E-03  9.06898E-04  3.67262E-04  1.48728E-04  7.55014E-05  4.80520E-05  2.77000E-05  1.59680E-05  9.87700E-06  4.00000E-06  3.30000E-06  2.60000E-06  2.10000E-06  1.85500E-06  1.50000E-06  1.30000E-06  1.15000E-06  1.12300E-06  1.09700E-06  1.07100E-06  1.04500E-06  1.02000E-06  9.96000E-07  9.72000E-07  9.50000E-07  9.10000E-07  8.50000E-07  7.80000E-07  6.25000E-07  5.00000E-07  4.00000E-07  3.50000E-07  3.20000E-07  3.00000E-07  2.80000E-07  2.50000E-07  2.20000E-07  1.80000E-07  1.40000E-07  1.00000E-07  8.00000E-08  6.70000E-08  5.80000E-08  5.00000E-08  4.20000E-08  3.50000E-08  3.00000E-08  2.50000E-08  2.00000E-08  1.50000E-08  1.00000E-08  5.00000E-09  1.00000E-11 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Micro-group spectrum:

INF_MICRO_FLX             (idx, [1: 140]) = [  6.06855E+03 0.00773  2.53631E+04 0.00398  5.35385E+04 0.00251  5.66438E+04 0.00215  5.40899E+04 0.00185  6.53143E+04 0.00168  4.39343E+04 0.00254  4.05760E+04 0.00198  3.06322E+04 0.00247  2.49432E+04 0.00278  2.14445E+04 0.00228  1.90634E+04 0.00290  1.75062E+04 0.00282  1.64809E+04 0.00292  1.60340E+04 0.00324  1.37763E+04 0.00356  1.35283E+04 0.00332  1.32488E+04 0.00330  1.27577E+04 0.00312  2.46130E+04 0.00280  2.31673E+04 0.00298  1.61589E+04 0.00252  1.00887E+04 0.00332  1.09707E+04 0.00307  9.97645E+03 0.00394  9.51998E+03 0.00321  1.39025E+04 0.00339  3.40847E+03 0.00753  4.28861E+03 0.00715  3.96259E+03 0.00586  2.25247E+03 0.00680  3.94745E+03 0.00441  2.66818E+03 0.00735  2.25179E+03 0.00805  4.12474E+02 0.01789  4.12969E+02 0.01022  4.17215E+02 0.01079  4.32957E+02 0.01259  4.42101E+02 0.01268  4.19438E+02 0.01335  4.50061E+02 0.01489  4.01839E+02 0.01056  7.70344E+02 0.01106  1.23803E+03 0.00988  1.56340E+03 0.00921  4.17438E+03 0.00651  4.23946E+03 0.00670  4.35986E+03 0.00544  2.67516E+03 0.00604  1.80196E+03 0.00677  1.33309E+03 0.00526  1.45976E+03 0.00677  2.53913E+03 0.00472  3.15388E+03 0.00400  5.38367E+03 0.00404  7.34298E+03 0.00298  9.60913E+03 0.00357  5.49316E+03 0.00412  3.69616E+03 0.00320  2.59057E+03 0.00644  2.23079E+03 0.00542  2.11600E+03 0.00549  1.70513E+03 0.00569  1.10481E+03 0.00779  1.00841E+03 0.00720  8.54430E+02 0.00731  6.80423E+02 0.00811  5.08891E+02 0.00944  3.14113E+02 0.00819  8.73311E+01 0.01507 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.31784E+00 0.00089 ];

% Flux spectra in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  1.74215E+01 0.00081  1.65624E+00 0.00107 ];
INF_FISS_FLX              (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  4.29039E-01 0.00023  6.92962E-01 0.00025 ];
INF_CAPT                  (idx, [1:   4]) = [  1.97833E-02 0.00127  6.77041E-02 0.00055 ];
INF_ABS                   (idx, [1:   4]) = [  2.90388E-02 0.00083  2.85413E-01 0.00058 ];
INF_FISS                  (idx, [1:   4]) = [  9.25552E-03 0.00093  2.17709E-01 0.00059 ];
INF_NSF                   (idx, [1:   4]) = [  2.35180E-02 0.00095  5.30382E-01 0.00059 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.54097E+00 9.2E-05  2.43620E+00 0.0E+00 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.03233E+02 6.2E-06  2.02270E+02 2.7E-09 ];
INF_INVV                  (idx, [1:   4]) = [  4.98747E-08 0.00158  2.15883E-06 0.00049 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  3.99991E-01 0.00024  4.07126E-01 0.00072 ];
INF_SCATT1                (idx, [1:   4]) = [  4.39830E-02 0.00209  8.05849E-03 0.02876 ];
INF_SCATT2                (idx, [1:   4]) = [  2.32212E-02 0.00248  5.51932E-04 0.38883 ];
INF_SCATT3                (idx, [1:   4]) = [  1.21076E-02 0.00397 -3.81318E-05 1.00000 ];
INF_SCATT4                (idx, [1:   4]) = [  7.71764E-03 0.00787  3.05840E-05 1.00000 ];
INF_SCATT5                (idx, [1:   4]) = [  4.06766E-03 0.01437  1.21551E-04 1.00000 ];
INF_SCATT6                (idx, [1:   4]) = [  2.06611E-03 0.02279 -8.76340E-05 1.00000 ];
INF_SCATT7                (idx, [1:   4]) = [  8.97101E-04 0.05082 -2.73615E-04 0.45165 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  4.00105E-01 0.00023  4.07126E-01 0.00072 ];
INF_SCATTP1               (idx, [1:   4]) = [  4.39845E-02 0.00209  8.05849E-03 0.02876 ];
INF_SCATTP2               (idx, [1:   4]) = [  2.32228E-02 0.00247  5.51932E-04 0.38883 ];
INF_SCATTP3               (idx, [1:   4]) = [  1.21088E-02 0.00399 -3.81318E-05 1.00000 ];
INF_SCATTP4               (idx, [1:   4]) = [  7.71710E-03 0.00780  3.05840E-05 1.00000 ];
INF_SCATTP5               (idx, [1:   4]) = [  4.06822E-03 0.01437  1.21551E-04 1.00000 ];
INF_SCATTP6               (idx, [1:   4]) = [  2.06605E-03 0.02277 -8.76340E-05 1.00000 ];
INF_SCATTP7               (idx, [1:   4]) = [  8.96054E-04 0.05090 -2.73615E-04 0.45165 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  3.13450E-01 0.00071  6.51949E-01 0.00047 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.06345E+00 0.00071  5.11290E-01 0.00047 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  2.89246E-02 0.00086  2.85413E-01 0.00058 ];
INF_REMXS                 (idx, [1:   4]) = [  2.97734E-02 0.00101  2.88308E-01 0.00109 ];

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

INF_S0                    (idx, [1:   8]) = [  3.99266E-01 0.00023  7.24996E-04 0.00888  2.47185E-03 0.01288  4.04654E-01 0.00072 ];
INF_S1                    (idx, [1:   8]) = [  4.41518E-02 0.00207 -1.68838E-04 0.01379 -2.16280E-04 0.10458  8.27477E-03 0.02649 ];
INF_S2                    (idx, [1:   8]) = [  2.32422E-02 0.00249 -2.09529E-05 0.13154 -1.11608E-04 0.14413  6.63540E-04 0.32351 ];
INF_S3                    (idx, [1:   8]) = [  1.21088E-02 0.00398 -1.17529E-06 1.00000 -2.52542E-05 0.52313 -1.28777E-05 1.00000 ];
INF_S4                    (idx, [1:   8]) = [  7.72019E-03 0.00785 -2.54706E-06 0.71115 -3.36873E-05 0.33809  6.42713E-05 1.00000 ];
INF_S5                    (idx, [1:   8]) = [  4.07098E-03 0.01424 -3.31590E-06 0.44648 -7.07762E-06 1.00000  1.28629E-04 1.00000 ];
INF_S6                    (idx, [1:   8]) = [  2.06707E-03 0.02291 -9.52595E-07 1.00000 -7.36094E-06 1.00000 -8.02731E-05 1.00000 ];
INF_S7                    (idx, [1:   8]) = [  8.97175E-04 0.05063 -7.41685E-08 1.00000  3.80480E-06 1.00000 -2.77420E-04 0.43023 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  3.99380E-01 0.00023  7.24996E-04 0.00888  2.47185E-03 0.01288  4.04654E-01 0.00072 ];
INF_SP1                   (idx, [1:   8]) = [  4.41533E-02 0.00207 -1.68838E-04 0.01379 -2.16280E-04 0.10458  8.27477E-03 0.02649 ];
INF_SP2                   (idx, [1:   8]) = [  2.32437E-02 0.00249 -2.09529E-05 0.13154 -1.11608E-04 0.14413  6.63540E-04 0.32351 ];
INF_SP3                   (idx, [1:   8]) = [  1.21100E-02 0.00399 -1.17529E-06 1.00000 -2.52542E-05 0.52313 -1.28777E-05 1.00000 ];
INF_SP4                   (idx, [1:   8]) = [  7.71965E-03 0.00778 -2.54706E-06 0.71115 -3.36873E-05 0.33809  6.42713E-05 1.00000 ];
INF_SP5                   (idx, [1:   8]) = [  4.07154E-03 0.01424 -3.31590E-06 0.44648 -7.07762E-06 1.00000  1.28629E-04 1.00000 ];
INF_SP6                   (idx, [1:   8]) = [  2.06700E-03 0.02289 -9.52595E-07 1.00000 -7.36094E-06 1.00000 -8.02731E-05 1.00000 ];
INF_SP7                   (idx, [1:   8]) = [  8.96128E-04 0.05071 -7.41685E-08 1.00000  3.80480E-06 1.00000 -2.77420E-04 0.43023 ];

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

CMM_TRANSPXS              (idx, [1:   4]) = [  2.55459E-01 0.00290  7.42008E-01 0.01224 ];
CMM_TRANSPXS_X            (idx, [1:   4]) = [  2.54296E-01 0.00388  7.52664E-01 0.02185 ];
CMM_TRANSPXS_Y            (idx, [1:   4]) = [  2.55072E-01 0.00420  7.48363E-01 0.02362 ];
CMM_TRANSPXS_Z            (idx, [1:   4]) = [  2.57197E-01 0.00453  7.39066E-01 0.01587 ];
CMM_DIFFCOEF              (idx, [1:   4]) = [  1.30510E+00 0.00289  4.50842E-01 0.01219 ];
CMM_DIFFCOEF_X            (idx, [1:   4]) = [  1.31128E+00 0.00391  4.47648E-01 0.02056 ];
CMM_DIFFCOEF_Y            (idx, [1:   4]) = [  1.30737E+00 0.00417  4.51215E-01 0.02283 ];
CMM_DIFFCOEF_Z            (idx, [1:   4]) = [  1.29666E+00 0.00451  4.53665E-01 0.01535 ];

% Delayed neutron parameters (Meulekamp method):

BETA_EFF                  (idx, [1:  18]) = [  7.18991E-03 0.01735  1.74821E-04 0.10806  1.07162E-03 0.04375  6.53062E-04 0.06214  1.28679E-03 0.04070  2.26104E-03 0.03225  7.94022E-04 0.05098  6.56782E-04 0.05893  2.91771E-04 0.08778 ];
LAMBDA                    (idx, [1:  18]) = [  4.89018E-01 0.02705  1.24667E-02 0.0E+00  2.82917E-02 0.0E+00  4.25244E-02 5.6E-09  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 5.0E-09  3.55460E+00 0.0E+00 ];


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
INPUT_FILE_NAME           (idx, [1:136])  = '/home/hirepan/Documents/chalmers/Project/codes/Shynt/repo/cases/single_assem_1x1cell/serpent_files/global_cell_type14/XS_generation.serp' ;
WORKING_DIRECTORY         (idx, [1: 84])  = '/home/hirepan/Documents/chalmers/Project/codes/Shynt/repo/cases/single_assem_1x1cell' ;
HOSTNAME                  (idx, [1:  4])  = 'thor' ;
CPU_TYPE                  (idx, [1: 40])  = 'Intel(R) Core(TM) i9-10900 CPU @ 2.80GHz' ;
CPU_MHZ                   (idx, 1)        = 236.0 ;
START_DATE                (idx, [1: 24])  = 'Thu Mar 10 11:53:15 2022' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Mar 10 11:53:24 2022' ;

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
OMP_HISTORY_PROFILE       (idx, [1:  18]) = [  9.55744E-01  1.00225E+00  9.95431E-01  9.91688E-01  9.80360E-01  1.02858E+00  1.04800E+00  1.00673E+00  1.04293E+00  9.82077E-01  1.00153E+00  9.92881E-01  9.86833E-01  9.74051E-01  1.00231E+00  1.00646E+00  9.92178E-01  1.00996E+00  ];
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

MIN_MACROXS               (idx, [1:   4]) = [  5.00000E-02 5.0E-09  0.00000E+00 0.0E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  8.70606E-03 0.00315  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.91294E-01 2.8E-05  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  8.37646E-01 0.00011  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  8.38032E-01 0.00011  0.00000E+00 0.0E+00 ];
AVG_TRACKING_LOOPS        (idx, [1:   8]) = [  2.31335E+00 0.00038  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  2.50515E+01 0.00054  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  2.50515E+01 0.00054  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  4.84181E+00 0.00081  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  1.90710E-01 0.00356  0.00000E+00 0.0E+00 ];
LOST_PARTICLES            (idx, 1)        = 0 ;

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 500 ;
SIMULATED_HISTORIES       (idx, 1)        = 1000567 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  2.00113E+03 0.00145 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  2.00113E+03 0.00145 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.32853E+00 ;
RUNNING_TIME              (idx, 1)        =  1.45267E-01 ;
INIT_TIME                 (idx, [1:  2])  = [  1.23333E-02  1.23333E-02 ];
PROCESS_TIME              (idx, [1:  2])  = [  1.16666E-04  1.16666E-04 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  1.32700E-01  1.32700E-01  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  1.45117E-01  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 16.02933 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  1.75686E+01 0.00427 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  7.49426E-01 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 64024.21 ;
ALLOC_MEMSIZE             (idx, 1)        = 390.09;
MEMSIZE                   (idx, 1)        = 204.06;
XS_MEMSIZE                (idx, 1)        = 74.10;
MAT_MEMSIZE               (idx, 1)        = 6.90;
RES_MEMSIZE               (idx, 1)        = 2.47;
IFC_MEMSIZE               (idx, 1)        = 0.00;
MISC_MEMSIZE              (idx, 1)        = 120.58;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 186.02;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 6 ;
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

NORM_COEF                 (idx, [1:   4]) = [  4.99716E-04 0.00080  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  5.58586E-01 0.00219 ];
U235_FISS                 (idx, [1:   4]) = [  4.80766E-01 0.00115  9.20774E-01 0.00040 ];
U238_FISS                 (idx, [1:   4]) = [  4.13903E-02 0.00503  7.92256E-02 0.00467 ];
U235_CAPT                 (idx, [1:   4]) = [  1.19691E-01 0.00283  2.49763E-01 0.00251 ];
U238_CAPT                 (idx, [1:   4]) = [  3.35213E-01 0.00175  6.99427E-01 0.00095 ];

% Neutron balance (particles/weight):

BALA_SRC_NEUTRON_SRC     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_FISS    (idx, [1:  2])  = [ 1000567 1.00000E+06 ];
BALA_SRC_NEUTRON_NXN     (idx, [1:  2])  = [ 0 1.98998E+03 ];
BALA_SRC_NEUTRON_VR      (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_TOT     (idx, [1:  2])  = [ 1000567 1.00199E+06 ];

BALA_LOSS_NEUTRON_CAPT    (idx, [1:  2])  = [ 478812 4.79499E+05 ];
BALA_LOSS_NEUTRON_FISS    (idx, [1:  2])  = [ 521755 5.22491E+05 ];
BALA_LOSS_NEUTRON_LEAK    (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_CUT     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_ERR     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_TOT     (idx, [1:  2])  = [ 1000567 1.00199E+06 ];

BALA_NEUTRON_DIFF         (idx, [1:  2])  = [ 0 -9.31323E-10 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.69293E-11 0.00054 ];
TOT_POWDENS               (idx, [1:   2]) = [  3.12072E-15 0.00054 ];
TOT_GENRATE               (idx, [1:   2]) = [  1.28768E+00 0.00054 ];
TOT_FISSRATE              (idx, [1:   2]) = [  5.21626E-01 0.00054 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  4.78374E-01 0.00059 ];
TOT_ABSRATE               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.99432E-01 0.00080 ];
TOT_FLUX                  (idx, [1:   2]) = [  5.42414E+01 0.00067 ];
TOT_PHOTON_PRODRATE       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  2.50814E+01 0.00053 ];
INI_FMASS                 (idx, 1)        =  5.42481E-03 ;
TOT_FMASS                 (idx, 1)        =  5.42481E-03 ;

% Six-factor formula:

SIX_FF_ETA                (idx, [1:   2]) = [  1.85744E+00 0.00082 ];
SIX_FF_F                  (idx, [1:   2]) = [  9.65717E-01 0.00027 ];
SIX_FF_P                  (idx, [1:   2]) = [  4.90491E-01 0.00101 ];
SIX_FF_EPSILON            (idx, [1:   2]) = [  1.46648E+00 0.00097 ];
SIX_FF_LF                 (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
SIX_FF_LT                 (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
SIX_FF_KINF               (idx, [1:   2]) = [  1.28968E+00 0.00099 ];
SIX_FF_KEFF               (idx, [1:   2]) = [  1.28968E+00 0.00099 ];

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.46859E+00 3.4E-05 ];
FISSE                     (idx, [1:   2]) = [  2.02568E+02 2.7E-06 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.28963E+00 0.00102  1.28047E+00 0.00099  9.20734E-03 0.01595 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.29017E+00 0.00054 ];
COL_KEFF                  (idx, [1:   2]) = [  1.28890E+00 0.00108 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.29017E+00 0.00054 ];
ABS_KINF                  (idx, [1:   2]) = [  1.29017E+00 0.00054 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% ALF (Average lethargy of neutrons causing fission):
% Based on E0 = 2.000000E+01 MeV

ANA_ALF                   (idx, [1:   2]) = [  1.63601E+01 0.00047 ];
IMP_ALF                   (idx, [1:   2]) = [  1.63519E+01 0.00024 ];

% EALF (Energy corresponding to average lethargy of neutrons causing fission):

ANA_EALF                  (idx, [1:   2]) = [  1.59379E-06 0.00786 ];
IMP_EALF                  (idx, [1:   2]) = [  1.58921E-06 0.00398 ];

% AFGE (Average energy of neutrons causing fission):

ANA_AFGE                  (idx, [1:   2]) = [  2.72772E-01 0.00509 ];
IMP_AFGE                  (idx, [1:   2]) = [  2.74849E-01 0.00235 ];

% Forward-weighted delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
FWD_ANA_BETA_ZERO         (idx, [1:  18]) = [  5.82853E-03 0.01206  1.50887E-04 0.07228  8.37322E-04 0.02908  5.17008E-04 0.03790  1.10426E-03 0.02697  1.81605E-03 0.02037  6.50140E-04 0.03664  5.28723E-04 0.03964  2.24130E-04 0.06008 ];
FWD_ANA_LAMBDA            (idx, [1:  18]) = [  4.83408E-01 0.01971  3.96441E-03 0.06556  2.48967E-02 0.01653  3.15531E-02 0.02640  1.24793E-01 0.01151  2.88958E-01 0.00493  5.31857E-01 0.02252  1.16069E+00 0.02861  1.54270E+00 0.05112 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  18]) = [  7.18991E-03 0.01735  1.74821E-04 0.10806  1.07162E-03 0.04375  6.53062E-04 0.06214  1.28679E-03 0.04070  2.26104E-03 0.03225  7.94022E-04 0.05098  6.56782E-04 0.05893  2.91771E-04 0.08778 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  18]) = [  4.89018E-01 0.02705  1.24667E-02 0.0E+00  2.82917E-02 0.0E+00  4.25244E-02 5.6E-09  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 5.0E-09  3.55460E+00 0.0E+00 ];

% Adjoint weighted time constants using Nauchi's method:

IFP_CHAIN_LENGTH          (idx, 1)        = 15 ;
ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  1.47478E-05 0.00228  1.47361E-05 0.00229  1.61743E-05 0.02236 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  1.90097E-05 0.00206  1.89947E-05 0.00208  2.08314E-05 0.02216 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  18]) = [  7.13624E-03 0.01632  2.03988E-04 0.09814  1.06485E-03 0.04098  6.43899E-04 0.05238  1.30110E-03 0.04015  2.22280E-03 0.02987  7.82025E-04 0.05046  6.44327E-04 0.05672  2.73253E-04 0.08545 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  18]) = [  4.77397E-01 0.02719  1.24667E-02 0.0E+00  2.82917E-02 0.0E+00  4.25244E-02 8.0E-09  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 5.5E-09  3.55460E+00 4.8E-09 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  1.49039E-05 0.00484  1.48899E-05 0.00486  1.22586E-05 0.05269 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  1.92082E-05 0.00467  1.91898E-05 0.00469  1.58135E-05 0.05273 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  18]) = [  6.82765E-03 0.05250  2.13848E-04 0.25717  1.13007E-03 0.12667  5.63039E-04 0.16917  1.42707E-03 0.10759  2.22671E-03 0.09309  6.32004E-04 0.15134  4.50184E-04 0.18787  1.84732E-04 0.25130 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  18]) = [  3.95057E-01 0.07212  1.24667E-02 2.7E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 4.4E-09  2.92467E-01 5.6E-09  6.66488E-01 4.8E-09  1.63478E+00 0.0E+00  3.55460E+00 6.0E-09 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  18]) = [  6.85168E-03 0.05156  2.02964E-04 0.27281  1.11151E-03 0.11892  5.73033E-04 0.15748  1.40878E-03 0.10677  2.21270E-03 0.09006  7.03454E-04 0.14570  4.63643E-04 0.18697  1.75604E-04 0.24473 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  18]) = [  3.91875E-01 0.07018  1.24667E-02 0.0E+00  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 4.6E-09  2.92467E-01 5.6E-09  6.66488E-01 4.8E-09  1.63478E+00 0.0E+00  3.55460E+00 4.7E-09 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -4.64263E+02 0.05410 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  1.48114E-05 0.00141 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  1.90920E-05 0.00105 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  7.12830E-03 0.01032 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -4.81909E+02 0.01048 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  2.54544E-07 0.00131 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  4.09916E-06 0.00112  4.09937E-06 0.00112  4.05422E-06 0.01338 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  2.30180E-05 0.00139  2.30149E-05 0.00140  2.33722E-05 0.01638 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  4.91147E-01 0.00101  4.90163E-01 0.00102  7.12182E-01 0.02172 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.25033E+01 0.02837 ];
ANA_MEAN_NCOL             (idx, [1:   4]) = [  2.50515E+01 0.00054  2.77443E+01 0.00074 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  7])  = 'u4gcu_2' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  2.00000E+01  6.06550E+00  3.67900E+00  2.23100E+00  1.35300E+00  8.21000E-01  5.00000E-01  3.02500E-01  1.83000E-01  1.11000E-01  6.74300E-02  4.08500E-02  2.47800E-02  1.50300E-02  9.11800E-03  5.50000E-03  3.51910E-03  2.23945E-03  1.42510E-03  9.06898E-04  3.67262E-04  1.48728E-04  7.55014E-05  4.80520E-05  2.77000E-05  1.59680E-05  9.87700E-06  4.00000E-06  3.30000E-06  2.60000E-06  2.10000E-06  1.85500E-06  1.50000E-06  1.30000E-06  1.15000E-06  1.12300E-06  1.09700E-06  1.07100E-06  1.04500E-06  1.02000E-06  9.96000E-07  9.72000E-07  9.50000E-07  9.10000E-07  8.50000E-07  7.80000E-07  6.25000E-07  5.00000E-07  4.00000E-07  3.50000E-07  3.20000E-07  3.00000E-07  2.80000E-07  2.50000E-07  2.20000E-07  1.80000E-07  1.40000E-07  1.00000E-07  8.00000E-08  6.70000E-08  5.80000E-08  5.00000E-08  4.20000E-08  3.50000E-08  3.00000E-08  2.50000E-08  2.00000E-08  1.50000E-08  1.00000E-08  5.00000E-09  1.00000E-11 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Micro-group spectrum:

INF_MICRO_FLX             (idx, [1: 140]) = [  1.08546E+04 0.00933  4.50694E+04 0.00412  9.46964E+04 0.00271  9.97701E+04 0.00234  9.53372E+04 0.00139  1.14670E+05 0.00124  7.78487E+04 0.00170  7.21990E+04 0.00104  5.51330E+04 0.00146  4.51323E+04 0.00126  3.90415E+04 0.00164  3.49958E+04 0.00137  3.23052E+04 0.00158  3.05732E+04 0.00174  2.97602E+04 0.00118  2.55331E+04 0.00158  2.53121E+04 0.00162  2.48010E+04 0.00183  2.42132E+04 0.00136  4.65197E+04 0.00125  4.41305E+04 0.00109  3.10346E+04 0.00134  1.95858E+04 0.00138  2.19487E+04 0.00136  2.01466E+04 0.00137  1.80454E+04 0.00207  2.83081E+04 0.00185  6.39387E+03 0.00364  8.04107E+03 0.00324  7.35307E+03 0.00298  4.20492E+03 0.00387  7.33152E+03 0.00352  4.99087E+03 0.00418  4.19832E+03 0.00297  7.76809E+02 0.00816  7.79070E+02 0.00828  8.09824E+02 0.00706  8.28001E+02 0.00930  8.12556E+02 0.00884  8.13633E+02 0.00941  8.36274E+02 0.00831  7.76016E+02 0.00834  1.47758E+03 0.00666  2.34143E+03 0.00592  2.98655E+03 0.00405  7.83317E+03 0.00344  8.10046E+03 0.00398  8.32332E+03 0.00282  5.18821E+03 0.00402  3.56889E+03 0.00506  2.61684E+03 0.00495  2.91363E+03 0.00571  5.11272E+03 0.00377  6.28352E+03 0.00293  1.08201E+04 0.00216  1.47148E+04 0.00287  1.95074E+04 0.00189  1.15124E+04 0.00217  7.94444E+03 0.00340  5.55721E+03 0.00381  4.86406E+03 0.00274  4.70237E+03 0.00380  3.85144E+03 0.00322  2.58516E+03 0.00362  2.35988E+03 0.00378  2.09248E+03 0.00506  1.74513E+03 0.00425  1.37802E+03 0.00497  9.36600E+02 0.00432  3.46050E+02 0.00717 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];

% Flux spectra in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  3.17456E+01 0.00070  3.42365E+00 0.00115 ];
INF_FISS_FLX              (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  4.03113E-01 0.00040  1.07084E+00 0.00020 ];
INF_CAPT                  (idx, [1:   4]) = [  1.56780E-04 0.00148  4.88626E-03 0.00036 ];
INF_ABS                   (idx, [1:   4]) = [  1.56780E-04 0.00148  4.88626E-03 0.00036 ];
INF_FISS                  (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_NSF                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_NUBAR                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_KAPPA                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_INVV                  (idx, [1:   4]) = [  5.22699E-08 0.00106  2.25059E-06 0.00036 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  4.02951E-01 0.00040  1.06593E+00 0.00021 ];
INF_SCATT1                (idx, [1:   4]) = [  2.35626E-01 0.00047  3.32321E-01 0.00084 ];
INF_SCATT2                (idx, [1:   4]) = [  9.01286E-02 0.00071  8.67946E-02 0.00318 ];
INF_SCATT3                (idx, [1:   4]) = [  2.72269E-03 0.01343  2.58884E-02 0.00779 ];
INF_SCATT4                (idx, [1:   4]) = [ -1.37551E-02 0.00215 -5.14234E-03 0.02810 ];
INF_SCATT5                (idx, [1:   4]) = [ -1.07958E-03 0.03423  4.17631E-03 0.03509 ];
INF_SCATT6                (idx, [1:   4]) = [  4.73153E-03 0.00768 -1.17729E-02 0.01278 ];
INF_SCATT7                (idx, [1:   4]) = [  4.97446E-04 0.07895 -5.90771E-04 0.24679 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  4.02951E-01 0.00040  1.06593E+00 0.00021 ];
INF_SCATTP1               (idx, [1:   4]) = [  2.35626E-01 0.00047  3.32321E-01 0.00084 ];
INF_SCATTP2               (idx, [1:   4]) = [  9.01286E-02 0.00071  8.67946E-02 0.00318 ];
INF_SCATTP3               (idx, [1:   4]) = [  2.72269E-03 0.01343  2.58884E-02 0.00779 ];
INF_SCATTP4               (idx, [1:   4]) = [ -1.37551E-02 0.00215 -5.14234E-03 0.02810 ];
INF_SCATTP5               (idx, [1:   4]) = [ -1.07958E-03 0.03423  4.17631E-03 0.03509 ];
INF_SCATTP6               (idx, [1:   4]) = [  4.73153E-03 0.00768 -1.17729E-02 0.01278 ];
INF_SCATTP7               (idx, [1:   4]) = [  4.97446E-04 0.07895 -5.90771E-04 0.24679 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  1.06285E-01 0.00110  6.32742E-01 0.00063 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  3.13631E+00 0.00109  5.26813E-01 0.00063 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  1.56780E-04 0.00148  4.88626E-03 0.00036 ];
INF_REMXS                 (idx, [1:   4]) = [  1.55173E-02 0.00093  6.59784E-03 0.00812 ];

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

INF_CHIT                  (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_CHIP                  (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_CHID                  (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Scattering matrixes:

INF_S0                    (idx, [1:   8]) = [  3.87596E-01 0.00040  1.53552E-02 0.00091  1.68936E-03 0.01482  1.06424E+00 0.00022 ];
INF_S1                    (idx, [1:   8]) = [  2.31069E-01 0.00047  4.55652E-03 0.00235  1.07081E-03 0.01687  3.31250E-01 0.00084 ];
INF_S2                    (idx, [1:   8]) = [  9.15279E-02 0.00071 -1.39923E-03 0.00579  5.77423E-04 0.01616  8.62172E-02 0.00317 ];
INF_S3                    (idx, [1:   8]) = [  4.33109E-03 0.00805 -1.60840E-03 0.00484  2.10417E-04 0.04917  2.56780E-02 0.00781 ];
INF_S4                    (idx, [1:   8]) = [ -1.32420E-02 0.00218 -5.13107E-04 0.00884  8.86601E-06 0.94796 -5.15120E-03 0.02812 ];
INF_S5                    (idx, [1:   8]) = [ -1.10834E-03 0.03324  2.87653E-05 0.20785 -6.84594E-05 0.10078  4.24477E-03 0.03436 ];
INF_S6                    (idx, [1:   8]) = [  4.85436E-03 0.00729 -1.22832E-04 0.03390 -9.01516E-05 0.05527 -1.16828E-02 0.01293 ];
INF_S7                    (idx, [1:   8]) = [  6.46686E-04 0.05743 -1.49240E-04 0.03908 -8.91802E-05 0.07856 -5.01591E-04 0.29054 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  3.87596E-01 0.00040  1.53552E-02 0.00091  1.68936E-03 0.01482  1.06424E+00 0.00022 ];
INF_SP1                   (idx, [1:   8]) = [  2.31069E-01 0.00047  4.55652E-03 0.00235  1.07081E-03 0.01687  3.31250E-01 0.00084 ];
INF_SP2                   (idx, [1:   8]) = [  9.15279E-02 0.00071 -1.39923E-03 0.00579  5.77423E-04 0.01616  8.62172E-02 0.00317 ];
INF_SP3                   (idx, [1:   8]) = [  4.33109E-03 0.00805 -1.60840E-03 0.00484  2.10417E-04 0.04917  2.56780E-02 0.00781 ];
INF_SP4                   (idx, [1:   8]) = [ -1.32420E-02 0.00218 -5.13107E-04 0.00884  8.86601E-06 0.94796 -5.15120E-03 0.02812 ];
INF_SP5                   (idx, [1:   8]) = [ -1.10834E-03 0.03324  2.87653E-05 0.20785 -6.84594E-05 0.10078  4.24477E-03 0.03436 ];
INF_SP6                   (idx, [1:   8]) = [  4.85436E-03 0.00729 -1.22832E-04 0.03390 -9.01516E-05 0.05527 -1.16828E-02 0.01293 ];
INF_SP7                   (idx, [1:   8]) = [  6.46686E-04 0.05743 -1.49240E-04 0.03908 -8.91802E-05 0.07856 -5.01591E-04 0.29054 ];

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

CMM_TRANSPXS              (idx, [1:   4]) = [  1.22786E-01 0.00143  3.94337E-01 0.00630 ];
CMM_TRANSPXS_X            (idx, [1:   4]) = [  1.22698E-01 0.00186  4.01428E-01 0.01255 ];
CMM_TRANSPXS_Y            (idx, [1:   4]) = [  1.22903E-01 0.00183  3.90705E-01 0.01088 ];
CMM_TRANSPXS_Z            (idx, [1:   4]) = [  1.22776E-01 0.00244  3.93668E-01 0.01154 ];
CMM_DIFFCOEF              (idx, [1:   4]) = [  2.71488E+00 0.00144  8.46122E-01 0.00643 ];
CMM_DIFFCOEF_X            (idx, [1:   4]) = [  2.71693E+00 0.00187  8.33452E-01 0.01232 ];
CMM_DIFFCOEF_Y            (idx, [1:   4]) = [  2.71238E+00 0.00183  8.55541E-01 0.01067 ];
CMM_DIFFCOEF_Z            (idx, [1:   4]) = [  2.71535E+00 0.00243  8.49372E-01 0.01125 ];

% Delayed neutron parameters (Meulekamp method):

BETA_EFF                  (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
LAMBDA                    (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

