
% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.29' ;
COMPILE_DATE              (idx, [1: 20])  = 'Oct 19 2017 17:01:10' ;
DEBUG                     (idx, 1)        = 0 ;
TITLE                     (idx, [1: 13])  = 'UO2 PIN MODEL' ;
CONFIDENTIAL_DATA         (idx, 1)        = 0 ;
INPUT_FILE_NAME           (idx, [1: 11])  = 'GroupConst4' ;
WORKING_DIRECTORY         (idx, [1: 50])  = '/home/huaiqian/Serpent2.1.29/src/GroupConstforpin4' ;
HOSTNAME                  (idx, [1:  8])  = 'huaiqian' ;
CPU_TYPE                  (idx, [1: 40])  = 'Intel(R) Core(TM) i5-3570K CPU @ 3.40GHz' ;
CPU_MHZ                   (idx, 1)        = 28.0 ;
START_DATE                (idx, [1: 24])  = 'Fri Nov  3 13:22:53 2017' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Fri Nov  3 13:24:22 2017' ;

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
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 1 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
SHARE_BUF_ARRAY           (idx, 1)        = 1 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 57])  = '/home/huaiqian/Serpent2.1.29/xs/endfb7/sss_endfb7u.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1:  3])  = 'N/A' ;
SFY_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;
NFY_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;
BRA_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:   4]) = [  5.00000E-02 0.0E+00  0.00000E+00 0.0E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  8.50237E-03 0.00274  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.91498E-01 2.3E-05  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  8.35876E-01 0.00011  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  8.36258E-01 0.00011  0.00000E+00 0.0E+00 ];
AVG_TRACKING_LOOPS        (idx, [1:   8]) = [  2.34030E+00 0.00038  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  2.61113E+01 0.00053  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  2.61113E+01 0.00053  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  5.11272E+00 0.00077  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  1.94541E-01 0.00311  0.00000E+00 0.0E+00 ];
LOST_PARTICLES            (idx, 1)        = 0 ;

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 500 ;
SOURCE_POPULATION         (idx, 1)        = 1000535 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  2.00107E+03 0.00142 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  2.00107E+03 0.00142 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  1.48139E+00 ;
RUNNING_TIME              (idx, 1)        =  1.48187E+00 ;
INIT_TIME                 (idx, [1:  2])  = [  1.30000E-02  1.30000E-02 ];
PROCESS_TIME              (idx, [1:  2])  = [  9.99993E-05  9.99993E-05 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  1.46877E+00  1.46877E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  1.48155E+00  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 0.99968 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  9.99736E-01 0.00011 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  9.84648E-01 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 7926.86 ;
ALLOC_MEMSIZE             (idx, 1)        = 95.40;
MEMSIZE                   (idx, 1)        = 57.11;
XS_MEMSIZE                (idx, 1)        = 31.20;
MAT_MEMSIZE               (idx, 1)        = 7.52;
RES_MEMSIZE               (idx, 1)        = 5.30;
MISC_MEMSIZE              (idx, 1)        = 13.08;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 38.30;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 4 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 81953 ;
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
TOT_REA_CHANNELS          (idx, 1)        = 137 ;
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
BETA_DECAY_SOURCE         (idx, 1)        =  0.00000E+00 ;

% Normaliation coefficient:

NORM_COEF                 (idx, [1:   4]) = [  4.98672E-04 0.00081  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  6.13131E-01 0.00211 ];
U235_FISS                 (idx, [1:   4]) = [  4.64967E-01 0.00112  9.16233E-01 0.00042 ];
U238_FISS                 (idx, [1:   4]) = [  4.25423E-02 0.00502  8.37674E-02 0.00459 ];
U235_CAPT                 (idx, [1:   4]) = [  1.11325E-01 0.00297  2.26337E-01 0.00268 ];
U238_CAPT                 (idx, [1:   4]) = [  3.53150E-01 0.00169  7.17912E-01 0.00091 ];

% Neutron balance (particles/weight):

BALA_SRC_NEUTRON_SRC        (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_FISS       (idx, [1:  2])  = [ 1000535 1.00000E+06 ];
BALA_SRC_NEUTRON_NXN        (idx, [1:  2])  = [ 0 2.06970E+03 ];
BALA_SRC_NEUTRON_VR         (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_TOT        (idx, [1:  2])  = [ 1000535 1.00207E+06 ];

BALA_LOSS_NEUTRON_CAPT       (idx, [1:  2])  = [ 492364 4.93175E+05 ];
BALA_LOSS_NEUTRON_FISS       (idx, [1:  2])  = [ 508171 5.08895E+05 ];
BALA_LOSS_NEUTRON_LEAK       (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_CUT        (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_TOT        (idx, [1:  2])  = [ 1000535 1.00207E+06 ];

BALA_NEUTRON_DIFF            (idx, [1:  2])  = [ 0 6.98492E-10 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.64928E-11 0.00054 ];
TOT_POWDENS               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_GENRATE               (idx, [1:   2]) = [  1.25403E+00 0.00053 ];
TOT_FISSRATE              (idx, [1:   2]) = [  5.07919E-01 0.00054 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  4.92081E-01 0.00055 ];
TOT_ABSRATE               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.97344E-01 0.00081 ];
TOT_FLUX                  (idx, [1:   2]) = [  5.56331E+01 0.00066 ];
TOT_PHOTON_PRODRATE       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  2.60879E+01 0.00053 ];
INI_FMASS                 (idx, 1)        =  0.00000E+00 ;
TOT_FMASS                 (idx, 1)        =  0.00000E+00 ;

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.46897E+00 3.4E-05 ];
FISSE                     (idx, [1:   2]) = [  2.02670E+02 3.7E-06 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.25665E+00 0.00101  1.24758E+00 0.00098  8.83069E-03 0.01675 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.25666E+00 0.00053 ];
COL_KEFF                  (idx, [1:   2]) = [  1.25787E+00 0.00110 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.25666E+00 0.00053 ];
ABS_KINF                  (idx, [1:   2]) = [  1.25666E+00 0.00053 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% ALF (Average lethargy of neutrons causing fission):
% Based on E0 = 2.000000E+01 MeV

ANA_ALF                   (idx, [1:   2]) = [  1.65579E+01 0.00048 ];
IMP_ALF                   (idx, [1:   2]) = [  1.65467E+01 0.00024 ];

% EALF (Energy corresponding to average lethargy of neutrons causing fission):

ANA_EALF                  (idx, [1:   2]) = [  1.30849E-06 0.00798 ];
IMP_EALF                  (idx, [1:   2]) = [  1.30782E-06 0.00394 ];

% AFGE (Average energy of neutrons causing fission):

ANA_AFGE                  (idx, [1:   2]) = [  2.86690E-01 0.00497 ];
IMP_AFGE                  (idx, [1:   2]) = [  2.87487E-01 0.00230 ];

% Forward-weighted delayed neutron parameters:

FWD_ANA_BETA_ZERO         (idx, [1:  14]) = [  5.88552E-03 0.01215  1.48889E-04 0.07266  9.32426E-04 0.02999  9.18020E-04 0.03047  2.72437E-03 0.01689  8.71194E-04 0.03083  2.90629E-04 0.05145 ];
FWD_ANA_LAMBDA            (idx, [1:  14]) = [  8.11279E-01 0.02825  3.87215E-03 0.06679  2.87335E-02 0.01409  9.97119E-02 0.01478  3.21560E-01 0.00055  1.18104E+00 0.01654  4.65333E+00 0.04335 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  14]) = [  7.21176E-03 0.01807  1.78149E-04 0.11070  1.16382E-03 0.04606  1.10271E-03 0.04694  3.34073E-03 0.02623  1.07192E-03 0.04544  3.54435E-04 0.08201 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  14]) = [  8.05282E-01 0.04198  1.24908E-02 5.8E-06  3.15850E-02 0.00071  1.10577E-01 0.00089  3.21582E-01 0.00074  1.34253E+00 0.00049  8.98758E+00 0.00391 ];

% Adjoint weighted time constants using Nauchi's method:

ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  1.80625E-05 0.00227  1.80496E-05 0.00226  1.97371E-05 0.02206 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  2.26872E-05 0.00204  2.26709E-05 0.00204  2.47945E-05 0.02201 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  14]) = [  7.05235E-03 0.01672  1.74008E-04 0.10494  1.09835E-03 0.04368  1.11323E-03 0.04309  3.23441E-03 0.02460  1.06389E-03 0.04363  3.68453E-04 0.07745 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  14]) = [  8.22851E-01 0.04295  1.24907E-02 6.3E-06  3.15683E-02 0.00088  1.10615E-01 0.00107  3.21498E-01 0.00087  1.34285E+00 0.00058  8.96335E+00 0.00507 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  1.79431E-05 0.00497  1.79230E-05 0.00497  1.51621E-05 0.04997 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  2.25393E-05 0.00490  2.25146E-05 0.00492  1.90366E-05 0.04991 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  14]) = [  7.50389E-03 0.04626  9.14303E-05 0.29834  1.24980E-03 0.11607  1.03453E-03 0.12980  3.56688E-03 0.07465  1.12185E-03 0.11884  4.39400E-04 0.21379 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  14]) = [  8.85096E-01 0.10229  1.24910E-02 2.7E-05  3.15836E-02 0.00170  1.11021E-01 0.00261  3.21453E-01 0.00170  1.34337E+00 0.00120  8.89745E+00 0.01010 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  14]) = [  7.45371E-03 0.04467  1.06048E-04 0.29739  1.20884E-03 0.11231  1.04066E-03 0.12163  3.58804E-03 0.07069  1.05102E-03 0.11729  4.59094E-04 0.20840 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  14]) = [  8.86433E-01 0.10275  1.24910E-02 2.7E-05  3.15852E-02 0.00169  1.11019E-01 0.00261  3.21453E-01 0.00171  1.34347E+00 0.00120  8.89745E+00 0.01010 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -4.20041E+02 0.04617 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  1.80234E-05 0.00138 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  2.26376E-05 0.00094 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  7.05289E-03 0.00828 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -3.91625E+02 0.00834 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  2.95515E-07 0.00125 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  4.15570E-06 0.00106  4.15544E-06 0.00106  4.19556E-06 0.01358 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  2.71350E-05 0.00130  2.71318E-05 0.00130  2.72924E-05 0.01686 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.11974E-01 0.00100  5.10938E-01 0.00100  7.49153E-01 0.02166 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  9.70242E+00 0.02582 ];
ANA_MEAN_NCOL             (idx, [1:   4]) = [  2.61113E+01 0.00053  2.91703E+01 0.00071 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  2])  = '11' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  1.00000E-11  5.00000E-09  1.00000E-08  1.50000E-08  2.00000E-08  2.50000E-08  3.00000E-08  3.50000E-08  4.20000E-08  5.00000E-08  5.80000E-08  6.70000E-08  8.00000E-08  1.00000E-07  1.40000E-07  1.80000E-07  2.20000E-07  2.50000E-07  2.80000E-07  3.00000E-07  3.20000E-07  3.50000E-07  4.00000E-07  5.00000E-07  6.25000E-07  7.80000E-07  8.50000E-07  9.10000E-07  9.50000E-07  9.72000E-07  9.96000E-07  1.02000E-06  1.04500E-06  1.07100E-06  1.09700E-06  1.12300E-06  1.15000E-06  1.30000E-06  1.50000E-06  1.85500E-06  2.10000E-06  2.60000E-06  3.30000E-06  4.00000E-06  9.87700E-06  1.59680E-05  2.77000E-05  4.80520E-05  7.55014E-05  1.48728E-04  3.67262E-04  9.06898E-04  1.42510E-03  2.23945E-03  3.51910E-03  5.50000E-03  9.11800E-03  1.50300E-02  2.47800E-02  4.08500E-02  6.74300E-02  1.11000E-01  1.83000E-01  3.02500E-01  5.00000E-01  8.21000E-01  1.35300E+00  2.23100E+00  3.67900E+00  6.06550E+00  2.00000E+01 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Micro-group spectrum:

INF_MICRO_FLX             (idx, [1: 140]) = [  1.13999E+04 0.00845  4.67624E+04 0.00429  9.74235E+04 0.00272  1.00858E+05 0.00194  9.58976E+04 0.00169  1.13926E+05 0.00108  7.72712E+04 0.00160  7.18093E+04 0.00150  5.51579E+04 0.00173  4.50776E+04 0.00158  3.91014E+04 0.00165  3.50232E+04 0.00158  3.24598E+04 0.00171  3.07046E+04 0.00158  2.99260E+04 0.00138  2.56649E+04 0.00157  2.53743E+04 0.00179  2.48830E+04 0.00165  2.43786E+04 0.00167  4.68610E+04 0.00153  4.47981E+04 0.00115  3.15536E+04 0.00182  2.00232E+04 0.00151  2.25896E+04 0.00152  2.07943E+04 0.00159  1.85741E+04 0.00191  2.93696E+04 0.00160  6.68009E+03 0.00253  8.34294E+03 0.00285  7.60391E+03 0.00353  4.37663E+03 0.00380  7.60136E+03 0.00319  5.15425E+03 0.00343  4.35587E+03 0.00369  8.23609E+02 0.01054  8.05938E+02 0.01055  8.29896E+02 0.00883  8.83094E+02 0.00744  8.54536E+02 0.00778  8.47775E+02 0.00961  8.72712E+02 0.00879  8.30860E+02 0.00791  1.55343E+03 0.00558  2.46682E+03 0.00516  3.15047E+03 0.00461  8.22632E+03 0.00309  8.61491E+03 0.00277  8.94931E+03 0.00371  5.65667E+03 0.00317  3.97293E+03 0.00451  2.92521E+03 0.00444  3.28531E+03 0.00452  5.81788E+03 0.00302  7.27762E+03 0.00362  1.27064E+04 0.00283  1.76732E+04 0.00271  2.38442E+04 0.00243  1.43446E+04 0.00255  9.91710E+03 0.00245  6.91463E+03 0.00292  6.15075E+03 0.00276  5.92211E+03 0.00330  4.89703E+03 0.00390  3.27375E+03 0.00255  3.03139E+03 0.00341  2.63553E+03 0.00380  2.21338E+03 0.00372  1.76045E+03 0.00345  1.18745E+03 0.00548  4.36765E+02 0.00597 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];

% Flux spectra in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  3.20128E+01 0.00073  4.07429E+00 0.00117 ];
INF_FISS_FLX              (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  4.03490E-01 0.00025  1.08464E+00 0.00027 ];
INF_CAPT                  (idx, [1:   4]) = [  1.56383E-04 0.00119  4.99911E-03 0.00048 ];
INF_ABS                   (idx, [1:   4]) = [  1.56383E-04 0.00119  4.99911E-03 0.00048 ];
INF_FISS                  (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_NSF                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_NUBAR                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_KAPPA                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_INVV                  (idx, [1:   4]) = [  5.35754E-08 0.00111  2.30218E-06 0.00048 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  4.03336E-01 0.00025  1.07968E+00 0.00027 ];
INF_SCATT1                (idx, [1:   4]) = [  2.35891E-01 0.00030  3.31535E-01 0.00058 ];
INF_SCATT2                (idx, [1:   4]) = [  9.03030E-02 0.00058  8.54354E-02 0.00324 ];
INF_SCATT3                (idx, [1:   4]) = [  2.79179E-03 0.01607  2.56264E-02 0.00926 ];
INF_SCATT4                (idx, [1:   4]) = [ -1.37798E-02 0.00293 -5.41981E-03 0.03870 ];
INF_SCATT5                (idx, [1:   4]) = [ -1.16034E-03 0.02889  4.49424E-03 0.03610 ];
INF_SCATT6                (idx, [1:   4]) = [  4.68912E-03 0.00656 -1.18295E-02 0.01298 ];
INF_SCATT7                (idx, [1:   4]) = [  4.33286E-04 0.05199 -3.85795E-04 0.27852 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  4.03336E-01 0.00025  1.07968E+00 0.00027 ];
INF_SCATTP1               (idx, [1:   4]) = [  2.35891E-01 0.00030  3.31535E-01 0.00058 ];
INF_SCATTP2               (idx, [1:   4]) = [  9.03030E-02 0.00058  8.54354E-02 0.00324 ];
INF_SCATTP3               (idx, [1:   4]) = [  2.79179E-03 0.01607  2.56264E-02 0.00926 ];
INF_SCATTP4               (idx, [1:   4]) = [ -1.37798E-02 0.00293 -5.41981E-03 0.03870 ];
INF_SCATTP5               (idx, [1:   4]) = [ -1.16034E-03 0.02889  4.49424E-03 0.03610 ];
INF_SCATTP6               (idx, [1:   4]) = [  4.68912E-03 0.00656 -1.18295E-02 0.01298 ];
INF_SCATTP7               (idx, [1:   4]) = [  4.33286E-04 0.05199 -3.85795E-04 0.27852 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  1.05659E-01 0.00074  6.45225E-01 0.00055 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  3.15485E+00 0.00074  5.16619E-01 0.00055 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  1.56383E-04 0.00119  4.99911E-03 0.00048 ];
INF_REMXS                 (idx, [1:   4]) = [  1.60090E-02 0.00092  6.50614E-03 0.00736 ];

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

% Fission spectra:

INF_CHIT                  (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_CHIP                  (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_CHID                  (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Scattering matrixes:

INF_S0                    (idx, [1:   8]) = [  3.87481E-01 0.00025  1.58546E-02 0.00092  1.55239E-03 0.01386  1.07813E+00 0.00027 ];
INF_S1                    (idx, [1:   8]) = [  2.31160E-01 0.00030  4.73113E-03 0.00252  9.80745E-04 0.01615  3.30554E-01 0.00058 ];
INF_S2                    (idx, [1:   8]) = [  9.17205E-02 0.00056 -1.41754E-03 0.00730  5.30062E-04 0.02108  8.49054E-02 0.00321 ];
INF_S3                    (idx, [1:   8]) = [  4.45373E-03 0.00998 -1.66193E-03 0.00369  1.92229E-04 0.04223  2.54341E-02 0.00927 ];
INF_S4                    (idx, [1:   8]) = [ -1.32426E-02 0.00304 -5.37212E-04 0.01239  1.07793E-05 0.53416 -5.43059E-03 0.03820 ];
INF_S5                    (idx, [1:   8]) = [ -1.19185E-03 0.02671  3.15076E-05 0.16975 -6.45193E-05 0.09692  4.55876E-03 0.03541 ];
INF_S6                    (idx, [1:   8]) = [  4.81344E-03 0.00606 -1.24322E-04 0.03285 -8.98027E-05 0.07126 -1.17397E-02 0.01296 ];
INF_S7                    (idx, [1:   8]) = [  5.93649E-04 0.03680 -1.60363E-04 0.02727 -8.82570E-05 0.07157 -2.97538E-04 0.36286 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  3.87481E-01 0.00025  1.58546E-02 0.00092  1.55239E-03 0.01386  1.07813E+00 0.00027 ];
INF_SP1                   (idx, [1:   8]) = [  2.31160E-01 0.00030  4.73113E-03 0.00252  9.80745E-04 0.01615  3.30554E-01 0.00058 ];
INF_SP2                   (idx, [1:   8]) = [  9.17205E-02 0.00056 -1.41754E-03 0.00730  5.30062E-04 0.02108  8.49054E-02 0.00321 ];
INF_SP3                   (idx, [1:   8]) = [  4.45373E-03 0.00998 -1.66193E-03 0.00369  1.92229E-04 0.04223  2.54341E-02 0.00927 ];
INF_SP4                   (idx, [1:   8]) = [ -1.32426E-02 0.00304 -5.37212E-04 0.01239  1.07793E-05 0.53416 -5.43059E-03 0.03820 ];
INF_SP5                   (idx, [1:   8]) = [ -1.19185E-03 0.02671  3.15076E-05 0.16975 -6.45193E-05 0.09692  4.55876E-03 0.03541 ];
INF_SP6                   (idx, [1:   8]) = [  4.81344E-03 0.00606 -1.24322E-04 0.03285 -8.98027E-05 0.07126 -1.17397E-02 0.01296 ];
INF_SP7                   (idx, [1:   8]) = [  5.93649E-04 0.03680 -1.60363E-04 0.02727 -8.82570E-05 0.07157 -2.97538E-04 0.36286 ];

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

CMM_TRANSPXS              (idx, [1:   4]) = [  2.25620E-01 0.00192 -3.02934E-02 0.00172 ];
CMM_TRANSPXS_X            (idx, [1:   4]) = [  2.26551E-01 0.00273 -3.04218E-02 0.00254 ];
CMM_TRANSPXS_Y            (idx, [1:   4]) = [  2.26171E-01 0.00292 -3.03812E-02 0.00278 ];
CMM_TRANSPXS_Z            (idx, [1:   4]) = [  2.24245E-01 0.00353 -3.00935E-02 0.00374 ];
CMM_DIFFCOEF              (idx, [1:   4]) = [  1.47754E+00 0.00192 -1.10043E+01 0.00172 ];
CMM_DIFFCOEF_X            (idx, [1:   4]) = [  1.47160E+00 0.00272 -1.09587E+01 0.00253 ];
CMM_DIFFCOEF_Y            (idx, [1:   4]) = [  1.47411E+00 0.00291 -1.09737E+01 0.00279 ];
CMM_DIFFCOEF_Z            (idx, [1:   4]) = [  1.48691E+00 0.00355 -1.10804E+01 0.00380 ];

% Delayed neutron parameters (Meulekamp method):

BETA_EFF                  (idx, [1:  14]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
LAMBDA                    (idx, [1:  14]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];


% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.29' ;
COMPILE_DATE              (idx, [1: 20])  = 'Oct 19 2017 17:01:10' ;
DEBUG                     (idx, 1)        = 0 ;
TITLE                     (idx, [1: 13])  = 'UO2 PIN MODEL' ;
CONFIDENTIAL_DATA         (idx, 1)        = 0 ;
INPUT_FILE_NAME           (idx, [1: 11])  = 'GroupConst4' ;
WORKING_DIRECTORY         (idx, [1: 50])  = '/home/huaiqian/Serpent2.1.29/src/GroupConstforpin4' ;
HOSTNAME                  (idx, [1:  8])  = 'huaiqian' ;
CPU_TYPE                  (idx, [1: 40])  = 'Intel(R) Core(TM) i5-3570K CPU @ 3.40GHz' ;
CPU_MHZ                   (idx, 1)        = 28.0 ;
START_DATE                (idx, [1: 24])  = 'Fri Nov  3 13:22:53 2017' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Fri Nov  3 13:24:22 2017' ;

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
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 1 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
SHARE_BUF_ARRAY           (idx, 1)        = 1 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 57])  = '/home/huaiqian/Serpent2.1.29/xs/endfb7/sss_endfb7u.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1:  3])  = 'N/A' ;
SFY_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;
NFY_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;
BRA_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:   4]) = [  5.00000E-02 0.0E+00  0.00000E+00 0.0E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  8.50237E-03 0.00274  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.91498E-01 2.3E-05  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  8.35876E-01 0.00011  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  8.36258E-01 0.00011  0.00000E+00 0.0E+00 ];
AVG_TRACKING_LOOPS        (idx, [1:   8]) = [  2.34030E+00 0.00038  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  2.61113E+01 0.00053  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  2.61113E+01 0.00053  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  5.11272E+00 0.00077  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  1.94541E-01 0.00311  0.00000E+00 0.0E+00 ];
LOST_PARTICLES            (idx, 1)        = 0 ;

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 500 ;
SOURCE_POPULATION         (idx, 1)        = 1000535 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  2.00107E+03 0.00142 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  2.00107E+03 0.00142 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  1.48140E+00 ;
RUNNING_TIME              (idx, 1)        =  1.48187E+00 ;
INIT_TIME                 (idx, [1:  2])  = [  1.30000E-02  1.30000E-02 ];
PROCESS_TIME              (idx, [1:  2])  = [  9.99993E-05  9.99993E-05 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  1.46877E+00  1.46877E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  1.48155E+00  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 0.99968 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  9.99736E-01 0.00011 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  9.84648E-01 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 7926.86 ;
ALLOC_MEMSIZE             (idx, 1)        = 95.40;
MEMSIZE                   (idx, 1)        = 57.11;
XS_MEMSIZE                (idx, 1)        = 31.20;
MAT_MEMSIZE               (idx, 1)        = 7.52;
RES_MEMSIZE               (idx, 1)        = 5.30;
MISC_MEMSIZE              (idx, 1)        = 13.08;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 38.30;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 4 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 81953 ;
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
TOT_REA_CHANNELS          (idx, 1)        = 137 ;
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
BETA_DECAY_SOURCE         (idx, 1)        =  0.00000E+00 ;

% Normaliation coefficient:

NORM_COEF                 (idx, [1:   4]) = [  4.98672E-04 0.00081  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  6.13131E-01 0.00211 ];
U235_FISS                 (idx, [1:   4]) = [  4.64967E-01 0.00112  9.16233E-01 0.00042 ];
U238_FISS                 (idx, [1:   4]) = [  4.25423E-02 0.00502  8.37674E-02 0.00459 ];
U235_CAPT                 (idx, [1:   4]) = [  1.11325E-01 0.00297  2.26337E-01 0.00268 ];
U238_CAPT                 (idx, [1:   4]) = [  3.53150E-01 0.00169  7.17912E-01 0.00091 ];

% Neutron balance (particles/weight):

BALA_SRC_NEUTRON_SRC        (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_FISS       (idx, [1:  2])  = [ 1000535 1.00000E+06 ];
BALA_SRC_NEUTRON_NXN        (idx, [1:  2])  = [ 0 2.06970E+03 ];
BALA_SRC_NEUTRON_VR         (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_TOT        (idx, [1:  2])  = [ 1000535 1.00207E+06 ];

BALA_LOSS_NEUTRON_CAPT       (idx, [1:  2])  = [ 492364 4.93175E+05 ];
BALA_LOSS_NEUTRON_FISS       (idx, [1:  2])  = [ 508171 5.08895E+05 ];
BALA_LOSS_NEUTRON_LEAK       (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_CUT        (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_TOT        (idx, [1:  2])  = [ 1000535 1.00207E+06 ];

BALA_NEUTRON_DIFF            (idx, [1:  2])  = [ 0 6.98492E-10 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.64928E-11 0.00054 ];
TOT_POWDENS               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_GENRATE               (idx, [1:   2]) = [  1.25403E+00 0.00053 ];
TOT_FISSRATE              (idx, [1:   2]) = [  5.07919E-01 0.00054 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  4.92081E-01 0.00055 ];
TOT_ABSRATE               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.97344E-01 0.00081 ];
TOT_FLUX                  (idx, [1:   2]) = [  5.56331E+01 0.00066 ];
TOT_PHOTON_PRODRATE       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  2.60879E+01 0.00053 ];
INI_FMASS                 (idx, 1)        =  0.00000E+00 ;
TOT_FMASS                 (idx, 1)        =  0.00000E+00 ;

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.46897E+00 3.4E-05 ];
FISSE                     (idx, [1:   2]) = [  2.02670E+02 3.7E-06 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.25665E+00 0.00101  1.24758E+00 0.00098  8.83069E-03 0.01675 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.25666E+00 0.00053 ];
COL_KEFF                  (idx, [1:   2]) = [  1.25787E+00 0.00110 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.25666E+00 0.00053 ];
ABS_KINF                  (idx, [1:   2]) = [  1.25666E+00 0.00053 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% ALF (Average lethargy of neutrons causing fission):
% Based on E0 = 2.000000E+01 MeV

ANA_ALF                   (idx, [1:   2]) = [  1.65579E+01 0.00048 ];
IMP_ALF                   (idx, [1:   2]) = [  1.65467E+01 0.00024 ];

% EALF (Energy corresponding to average lethargy of neutrons causing fission):

ANA_EALF                  (idx, [1:   2]) = [  1.30849E-06 0.00798 ];
IMP_EALF                  (idx, [1:   2]) = [  1.30782E-06 0.00394 ];

% AFGE (Average energy of neutrons causing fission):

ANA_AFGE                  (idx, [1:   2]) = [  2.86690E-01 0.00497 ];
IMP_AFGE                  (idx, [1:   2]) = [  2.87487E-01 0.00230 ];

% Forward-weighted delayed neutron parameters:

FWD_ANA_BETA_ZERO         (idx, [1:  14]) = [  5.88552E-03 0.01215  1.48889E-04 0.07266  9.32426E-04 0.02999  9.18020E-04 0.03047  2.72437E-03 0.01689  8.71194E-04 0.03083  2.90629E-04 0.05145 ];
FWD_ANA_LAMBDA            (idx, [1:  14]) = [  8.11279E-01 0.02825  3.87215E-03 0.06679  2.87335E-02 0.01409  9.97119E-02 0.01478  3.21560E-01 0.00055  1.18104E+00 0.01654  4.65333E+00 0.04335 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  14]) = [  7.21176E-03 0.01807  1.78149E-04 0.11070  1.16382E-03 0.04606  1.10271E-03 0.04694  3.34073E-03 0.02623  1.07192E-03 0.04544  3.54435E-04 0.08201 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  14]) = [  8.05282E-01 0.04198  1.24908E-02 5.8E-06  3.15850E-02 0.00071  1.10577E-01 0.00089  3.21582E-01 0.00074  1.34253E+00 0.00049  8.98758E+00 0.00391 ];

% Adjoint weighted time constants using Nauchi's method:

ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  1.80625E-05 0.00227  1.80496E-05 0.00226  1.97371E-05 0.02206 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  2.26872E-05 0.00204  2.26709E-05 0.00204  2.47945E-05 0.02201 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  14]) = [  7.05235E-03 0.01672  1.74008E-04 0.10494  1.09835E-03 0.04368  1.11323E-03 0.04309  3.23441E-03 0.02460  1.06389E-03 0.04363  3.68453E-04 0.07745 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  14]) = [  8.22851E-01 0.04295  1.24907E-02 6.3E-06  3.15683E-02 0.00088  1.10615E-01 0.00107  3.21498E-01 0.00087  1.34285E+00 0.00058  8.96335E+00 0.00507 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  1.79431E-05 0.00497  1.79230E-05 0.00497  1.51621E-05 0.04997 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  2.25393E-05 0.00490  2.25146E-05 0.00492  1.90366E-05 0.04991 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  14]) = [  7.50389E-03 0.04626  9.14303E-05 0.29834  1.24980E-03 0.11607  1.03453E-03 0.12980  3.56688E-03 0.07465  1.12185E-03 0.11884  4.39400E-04 0.21379 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  14]) = [  8.85096E-01 0.10229  1.24910E-02 2.7E-05  3.15836E-02 0.00170  1.11021E-01 0.00261  3.21453E-01 0.00170  1.34337E+00 0.00120  8.89745E+00 0.01010 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  14]) = [  7.45371E-03 0.04467  1.06048E-04 0.29739  1.20884E-03 0.11231  1.04066E-03 0.12163  3.58804E-03 0.07069  1.05102E-03 0.11729  4.59094E-04 0.20840 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  14]) = [  8.86433E-01 0.10275  1.24910E-02 2.7E-05  3.15852E-02 0.00169  1.11019E-01 0.00261  3.21453E-01 0.00171  1.34347E+00 0.00120  8.89745E+00 0.01010 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -4.20041E+02 0.04617 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  1.80234E-05 0.00138 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  2.26376E-05 0.00094 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  7.05289E-03 0.00828 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -3.91625E+02 0.00834 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  2.95515E-07 0.00125 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  4.15570E-06 0.00106  4.15544E-06 0.00106  4.19556E-06 0.01358 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  2.71350E-05 0.00130  2.71318E-05 0.00130  2.72924E-05 0.01686 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.11974E-01 0.00100  5.10938E-01 0.00100  7.49153E-01 0.02166 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  9.70242E+00 0.02582 ];
ANA_MEAN_NCOL             (idx, [1:   4]) = [  2.61113E+01 0.00053  2.91703E+01 0.00071 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  2])  = '12' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  1.00000E-11  5.00000E-09  1.00000E-08  1.50000E-08  2.00000E-08  2.50000E-08  3.00000E-08  3.50000E-08  4.20000E-08  5.00000E-08  5.80000E-08  6.70000E-08  8.00000E-08  1.00000E-07  1.40000E-07  1.80000E-07  2.20000E-07  2.50000E-07  2.80000E-07  3.00000E-07  3.20000E-07  3.50000E-07  4.00000E-07  5.00000E-07  6.25000E-07  7.80000E-07  8.50000E-07  9.10000E-07  9.50000E-07  9.72000E-07  9.96000E-07  1.02000E-06  1.04500E-06  1.07100E-06  1.09700E-06  1.12300E-06  1.15000E-06  1.30000E-06  1.50000E-06  1.85500E-06  2.10000E-06  2.60000E-06  3.30000E-06  4.00000E-06  9.87700E-06  1.59680E-05  2.77000E-05  4.80520E-05  7.55014E-05  1.48728E-04  3.67262E-04  9.06898E-04  1.42510E-03  2.23945E-03  3.51910E-03  5.50000E-03  9.11800E-03  1.50300E-02  2.47800E-02  4.08500E-02  6.74300E-02  1.11000E-01  1.83000E-01  3.02500E-01  5.00000E-01  8.21000E-01  1.35300E+00  2.23100E+00  3.67900E+00  6.06550E+00  2.00000E+01 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Micro-group spectrum:

INF_MICRO_FLX             (idx, [1: 140]) = [  6.31511E+03 0.00905  2.62832E+04 0.00475  5.48329E+04 0.00301  5.72029E+04 0.00263  5.42046E+04 0.00199  6.48688E+04 0.00210  4.35430E+04 0.00200  4.05198E+04 0.00207  3.07772E+04 0.00255  2.48335E+04 0.00288  2.13917E+04 0.00353  1.90009E+04 0.00370  1.75832E+04 0.00352  1.64971E+04 0.00350  1.60791E+04 0.00336  1.37308E+04 0.00347  1.34887E+04 0.00316  1.33552E+04 0.00399  1.29674E+04 0.00377  2.48367E+04 0.00268  2.34563E+04 0.00242  1.64076E+04 0.00399  1.03504E+04 0.00338  1.14022E+04 0.00290  1.02942E+04 0.00230  9.75809E+03 0.00360  1.44621E+04 0.00385  3.58553E+03 0.00725  4.52918E+03 0.00496  4.07883E+03 0.00473  2.38226E+03 0.00912  4.05195E+03 0.00577  2.79901E+03 0.00734  2.31559E+03 0.00797  4.31013E+02 0.01536  4.25017E+02 0.01292  4.26976E+02 0.01402  4.53676E+02 0.01338  4.35904E+02 0.01377  4.49454E+02 0.01296  4.66999E+02 0.01814  4.27851E+02 0.01396  8.25463E+02 0.01180  1.34249E+03 0.00933  1.65514E+03 0.00732  4.36363E+03 0.00540  4.53052E+03 0.00535  4.69119E+03 0.00639  2.89143E+03 0.00601  2.03980E+03 0.00777  1.50269E+03 0.00976  1.68645E+03 0.00746  2.93723E+03 0.00525  3.70963E+03 0.00503  6.48201E+03 0.00337  8.92128E+03 0.00355  1.18941E+04 0.00365  6.98455E+03 0.00333  4.74128E+03 0.00391  3.31749E+03 0.00539  2.87357E+03 0.00487  2.75311E+03 0.00403  2.22025E+03 0.00507  1.46011E+03 0.00601  1.32909E+03 0.00490  1.13683E+03 0.00563  9.24878E+02 0.00668  6.93401E+02 0.00844  4.29090E+02 0.00953  1.29012E+02 0.01312 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.29036E+00 0.00105 ];

% Flux spectra in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  1.75505E+01 0.00083  2.00161E+00 0.00121 ];
INF_FISS_FLX              (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  4.24914E-01 0.00018  6.48813E-01 0.00019 ];
INF_CAPT                  (idx, [1:   4]) = [  1.94816E-02 0.00105  6.24097E-02 0.00045 ];
INF_ABS                   (idx, [1:   4]) = [  2.76254E-02 0.00084  2.44857E-01 0.00048 ];
INF_FISS                  (idx, [1:   4]) = [  8.14378E-03 0.00085  1.82447E-01 0.00050 ];
INF_NSF                   (idx, [1:   4]) = [  2.07778E-02 0.00086  4.44569E-01 0.00050 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.55137E+00 9.6E-05  2.43670E+00 0.0E+00 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.03690E+02 9.6E-06  2.02270E+02 0.0E+00 ];
INF_INVV                  (idx, [1:   4]) = [  5.12562E-08 0.00167  2.22250E-06 0.00039 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  3.97310E-01 0.00018  4.04097E-01 0.00065 ];
INF_SCATT1                (idx, [1:   4]) = [  4.37730E-02 0.00186  8.24245E-03 0.03129 ];
INF_SCATT2                (idx, [1:   4]) = [  2.27886E-02 0.00302  4.88221E-04 0.43137 ];
INF_SCATT3                (idx, [1:   4]) = [  1.20883E-02 0.00561 -1.13527E-04 1.00000 ];
INF_SCATT4                (idx, [1:   4]) = [  7.70230E-03 0.00777 -1.64315E-04 0.90939 ];
INF_SCATT5                (idx, [1:   4]) = [  3.96304E-03 0.01343  7.98256E-05 1.00000 ];
INF_SCATT6                (idx, [1:   4]) = [  1.99495E-03 0.02294  2.95650E-04 0.43555 ];
INF_SCATT7                (idx, [1:   4]) = [  8.69871E-04 0.04089  3.66898E-05 1.00000 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  3.97427E-01 0.00018  4.04097E-01 0.00065 ];
INF_SCATTP1               (idx, [1:   4]) = [  4.37742E-02 0.00186  8.24245E-03 0.03129 ];
INF_SCATTP2               (idx, [1:   4]) = [  2.27888E-02 0.00298  4.88221E-04 0.43137 ];
INF_SCATTP3               (idx, [1:   4]) = [  1.20890E-02 0.00561 -1.13527E-04 1.00000 ];
INF_SCATTP4               (idx, [1:   4]) = [  7.70245E-03 0.00780 -1.64315E-04 0.90939 ];
INF_SCATTP5               (idx, [1:   4]) = [  3.96243E-03 0.01347  7.98256E-05 1.00000 ];
INF_SCATTP6               (idx, [1:   4]) = [  1.99344E-03 0.02288  2.95650E-04 0.43555 ];
INF_SCATTP7               (idx, [1:   4]) = [  8.68673E-04 0.04097  3.66898E-05 1.00000 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  3.09997E-01 0.00045  6.13891E-01 0.00050 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.07528E+00 0.00045  5.42988E-01 0.00050 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  2.75078E-02 0.00082  2.44857E-01 0.00048 ];
INF_REMXS                 (idx, [1:   4]) = [  2.83522E-02 0.00104  2.46885E-01 0.00106 ];

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

% Fission spectra:

INF_CHIT                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_CHIP                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_CHID                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Scattering matrixes:

INF_S0                    (idx, [1:   8]) = [  3.96562E-01 0.00018  7.47379E-04 0.00730  2.16978E-03 0.01672  4.01928E-01 0.00065 ];
INF_S1                    (idx, [1:   8]) = [  4.39514E-02 0.00186 -1.78325E-04 0.01792 -1.98441E-04 0.10423  8.44089E-03 0.03083 ];
INF_S2                    (idx, [1:   8]) = [  2.28063E-02 0.00304 -1.77115E-05 0.14795 -9.88292E-05 0.16445  5.87050E-04 0.36638 ];
INF_S3                    (idx, [1:   8]) = [  1.20907E-02 0.00558 -2.44910E-06 1.00000 -4.47268E-05 0.29244 -6.88006E-05 1.00000 ];
INF_S4                    (idx, [1:   8]) = [  7.70735E-03 0.00780 -5.05003E-06 0.42286 -3.91520E-06 1.00000 -1.60400E-04 0.94252 ];
INF_S5                    (idx, [1:   8]) = [  3.96284E-03 0.01345  2.04201E-07 1.00000 -1.62151E-05 0.56973  9.60408E-05 1.00000 ];
INF_S6                    (idx, [1:   8]) = [  1.99678E-03 0.02274 -1.82456E-06 0.75508 -1.01754E-05 0.94057  3.05825E-04 0.41880 ];
INF_S7                    (idx, [1:   8]) = [  8.70126E-04 0.04029 -2.55047E-07 1.00000 -8.35458E-06 0.80780  4.50444E-05 1.00000 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  3.96680E-01 0.00018  7.47379E-04 0.00730  2.16978E-03 0.01672  4.01928E-01 0.00065 ];
INF_SP1                   (idx, [1:   8]) = [  4.39526E-02 0.00185 -1.78325E-04 0.01792 -1.98441E-04 0.10423  8.44089E-03 0.03083 ];
INF_SP2                   (idx, [1:   8]) = [  2.28065E-02 0.00301 -1.77115E-05 0.14795 -9.88292E-05 0.16445  5.87050E-04 0.36638 ];
INF_SP3                   (idx, [1:   8]) = [  1.20915E-02 0.00557 -2.44910E-06 1.00000 -4.47268E-05 0.29244 -6.88006E-05 1.00000 ];
INF_SP4                   (idx, [1:   8]) = [  7.70751E-03 0.00784 -5.05003E-06 0.42286 -3.91520E-06 1.00000 -1.60400E-04 0.94252 ];
INF_SP5                   (idx, [1:   8]) = [  3.96223E-03 0.01348  2.04201E-07 1.00000 -1.62151E-05 0.56973  9.60408E-05 1.00000 ];
INF_SP6                   (idx, [1:   8]) = [  1.99527E-03 0.02269 -1.82456E-06 0.75508 -1.01754E-05 0.94057  3.05825E-04 0.41880 ];
INF_SP7                   (idx, [1:   8]) = [  8.68928E-04 0.04037 -2.55047E-07 1.00000 -8.35458E-06 0.80780  4.50444E-05 1.00000 ];

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

CMM_TRANSPXS              (idx, [1:   4]) = [  1.35149E-01 0.00106  1.46293E-02 0.00131 ];
CMM_TRANSPXS_X            (idx, [1:   4]) = [  1.35680E-01 0.00201  1.46992E-02 0.00235 ];
CMM_TRANSPXS_Y            (idx, [1:   4]) = [  1.35357E-01 0.00226  1.46215E-02 0.00208 ];
CMM_TRANSPXS_Z            (idx, [1:   4]) = [  1.34445E-01 0.00175  1.45706E-02 0.00191 ];
CMM_DIFFCOEF              (idx, [1:   4]) = [  2.46648E+00 0.00107  2.27863E+01 0.00131 ];
CMM_DIFFCOEF_X            (idx, [1:   4]) = [  2.45700E+00 0.00202  2.26799E+01 0.00235 ];
CMM_DIFFCOEF_Y            (idx, [1:   4]) = [  2.46292E+00 0.00228  2.27998E+01 0.00209 ];
CMM_DIFFCOEF_Z            (idx, [1:   4]) = [  2.47951E+00 0.00177  2.28792E+01 0.00191 ];

% Delayed neutron parameters (Meulekamp method):

BETA_EFF                  (idx, [1:  14]) = [  7.21176E-03 0.01807  1.78149E-04 0.11070  1.16382E-03 0.04606  1.10271E-03 0.04694  3.34073E-03 0.02623  1.07192E-03 0.04544  3.54435E-04 0.08201 ];
LAMBDA                    (idx, [1:  14]) = [  8.05282E-01 0.04198  1.24908E-02 5.8E-06  3.15850E-02 0.00071  1.10577E-01 0.00089  3.21582E-01 0.00074  1.34253E+00 0.00049  8.98758E+00 0.00391 ];

% G = 2;
% 
% 
% for idx = 1:2 % idx = 1 for moderator, idx = 2 for fuel
%     if idx == 2 %fuel
%         
%         TOT_TR_F = INF_TOT(idx,[1,3]);
%         ABS_F = INF_ABS(idx,[1,3]);
%         CAP_F = INF_CAPT(idx,[1,3]);
%         FIS_F = INF_FISS(idx,[1,3]);
%         NU_F = INF_NUBAR(idx,[1,3]);
%         CHI_F = INF_CHIT(idx,[1,3]);
%        
%     else
%         
%         TOT_TR_M = INF_TOT(idx,[1,3]);
%         ABS_M = INF_ABS(idx,[1,3]);
%         CAP_M = INF_CAPT(idx,[1,3]);
%         FIS_M = INF_FISS(idx,[1,3]);
%         NU_M = INF_NUBAR(idx,[1,3]);
%         CHI_M = INF_CHIT(idx,[1,3]);
%         
%     end
% end
% 
% for idx = 1:2
%     if idx == 2
%         SCAT_TR_F = reshape(INF_S0(idx,1:2:end), G, G);
%     else
%         SCAT_TR_M = reshape(INF_S0(idx,1:2:end), G, G);
%     end
% end
clearvars idx