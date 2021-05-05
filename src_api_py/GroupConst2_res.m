
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
INPUT_FILE_NAME           (idx, [1: 11])  = 'GroupConst2' ;
WORKING_DIRECTORY         (idx, [1: 50])  = '/home/huaiqian/Serpent2.1.29/src/GroupConstforpin2' ;
HOSTNAME                  (idx, [1:  8])  = 'huaiqian' ;
CPU_TYPE                  (idx, [1: 40])  = 'Intel(R) Core(TM) i5-3570K CPU @ 3.40GHz' ;
CPU_MHZ                   (idx, 1)        = 28.0 ;
START_DATE                (idx, [1: 24])  = 'Fri Nov  3 13:12:18 2017' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Fri Nov  3 13:13:52 2017' ;

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
ST_FRAC                   (idx, [1:   4]) = [  8.03392E-03 0.00302  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.91966E-01 2.4E-05  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  8.31643E-01 9.8E-05  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  8.32013E-01 9.8E-05  0.00000E+00 0.0E+00 ];
AVG_TRACKING_LOOPS        (idx, [1:   8]) = [  2.38005E+00 0.00037  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  2.81559E+01 0.00056  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  2.81559E+01 0.00056  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  5.68484E+00 0.00075  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  1.98994E-01 0.00346  0.00000E+00 0.0E+00 ];
LOST_PARTICLES            (idx, 1)        = 0 ;

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 500 ;
SOURCE_POPULATION         (idx, 1)        = 1000536 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  2.00107E+03 0.00143 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  2.00107E+03 0.00143 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  1.57209E+00 ;
RUNNING_TIME              (idx, 1)        =  1.57380E+00 ;
INIT_TIME                 (idx, [1:  2])  = [  1.30000E-02  1.30000E-02 ];
PROCESS_TIME              (idx, [1:  2])  = [  9.99989E-05  9.99989E-05 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  1.56070E+00  1.56070E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  1.57347E+00  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 0.99891 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  9.99031E-01 0.00011 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  9.85682E-01 ;

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

NORM_COEF                 (idx, [1:   4]) = [  4.99192E-04 0.00083  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  7.24138E-01 0.00209 ];
U235_FISS                 (idx, [1:   4]) = [  4.36100E-01 0.00121  9.10007E-01 0.00043 ];
U238_FISS                 (idx, [1:   4]) = [  4.31496E-02 0.00476  8.99926E-02 0.00439 ];
U235_CAPT                 (idx, [1:   4]) = [  9.88106E-02 0.00305  1.89601E-01 0.00281 ];
U238_CAPT                 (idx, [1:   4]) = [  3.87099E-01 0.00160  7.42690E-01 0.00080 ];

% Neutron balance (particles/weight):

BALA_SRC_NEUTRON_SRC        (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_FISS       (idx, [1:  2])  = [ 1000536 1.00000E+06 ];
BALA_SRC_NEUTRON_NXN        (idx, [1:  2])  = [ 0 2.06700E+03 ];
BALA_SRC_NEUTRON_VR         (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_TOT        (idx, [1:  2])  = [ 1000536 1.00207E+06 ];

BALA_LOSS_NEUTRON_CAPT       (idx, [1:  2])  = [ 521148 5.22008E+05 ];
BALA_LOSS_NEUTRON_FISS       (idx, [1:  2])  = [ 479388 4.80059E+05 ];
BALA_LOSS_NEUTRON_LEAK       (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_CUT        (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_TOT        (idx, [1:  2])  = [ 1000536 1.00207E+06 ];

BALA_NEUTRON_DIFF            (idx, [1:  2])  = [ 0 2.79397E-09 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.55427E-11 0.00054 ];
TOT_POWDENS               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_GENRATE               (idx, [1:   2]) = [  1.18233E+00 0.00053 ];
TOT_FISSRATE              (idx, [1:   2]) = [  4.78594E-01 0.00054 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  5.21406E-01 0.00049 ];
TOT_ABSRATE               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.98384E-01 0.00083 ];
TOT_FLUX                  (idx, [1:   2]) = [  5.80910E+01 0.00069 ];
TOT_PHOTON_PRODRATE       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  2.81613E+01 0.00053 ];
INI_FMASS                 (idx, 1)        =  0.00000E+00 ;
TOT_FMASS                 (idx, 1)        =  0.00000E+00 ;

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.47042E+00 3.7E-05 ];
FISSE                     (idx, [1:   2]) = [  2.02697E+02 4.0E-06 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.18601E+00 0.00103  1.17744E+00 0.00104  8.53846E-03 0.01788 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.18480E+00 0.00053 ];
COL_KEFF                  (idx, [1:   2]) = [  1.18474E+00 0.00113 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.18480E+00 0.00053 ];
ABS_KINF                  (idx, [1:   2]) = [  1.18480E+00 0.00053 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% ALF (Average lethargy of neutrons causing fission):
% Based on E0 = 2.000000E+01 MeV

ANA_ALF                   (idx, [1:   2]) = [  1.68270E+01 0.00046 ];
IMP_ALF                   (idx, [1:   2]) = [  1.68217E+01 0.00024 ];

% EALF (Energy corresponding to average lethargy of neutrons causing fission):

ANA_EALF                  (idx, [1:   2]) = [  9.99308E-07 0.00786 ];
IMP_EALF                  (idx, [1:   2]) = [  9.93644E-07 0.00403 ];

% AFGE (Average energy of neutrons causing fission):

ANA_AFGE                  (idx, [1:   2]) = [  3.00087E-01 0.00485 ];
IMP_AFGE                  (idx, [1:   2]) = [  2.99660E-01 0.00240 ];

% Forward-weighted delayed neutron parameters:

FWD_ANA_BETA_ZERO         (idx, [1:  14]) = [  6.38379E-03 0.01187  1.73455E-04 0.06884  9.90309E-04 0.02847  9.86894E-04 0.02938  2.89753E-03 0.01663  1.00089E-03 0.02974  3.34712E-04 0.05061 ];
FWD_ANA_LAMBDA            (idx, [1:  14]) = [  8.40244E-01 0.02770  4.27185E-03 0.06209  2.90826E-02 0.01304  9.94622E-02 0.01477  3.22034E-01 0.00058  1.20482E+00 0.01526  4.84643E+00 0.04165 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  14]) = [  7.35252E-03 0.01841  1.95279E-04 0.11415  1.11351E-03 0.04629  1.15433E-03 0.04855  3.32480E-03 0.02586  1.20145E-03 0.04549  3.63148E-04 0.07473 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  14]) = [  8.11588E-01 0.03819  1.24908E-02 5.5E-06  3.15414E-02 0.00075  1.10283E-01 0.00078  3.21679E-01 0.00075  1.34456E+00 0.00046  9.01234E+00 0.00387 ];

% Adjoint weighted time constants using Nauchi's method:

ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  2.53659E-05 0.00239  2.53439E-05 0.00239  2.84668E-05 0.02853 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  3.00674E-05 0.00213  3.00413E-05 0.00213  3.37408E-05 0.02855 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  14]) = [  7.20878E-03 0.01811  1.75547E-04 0.11110  1.13098E-03 0.04114  1.14229E-03 0.04409  3.28764E-03 0.02647  1.13147E-03 0.04582  3.40859E-04 0.08080 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  14]) = [  7.83409E-01 0.04441  1.24910E-02 1.1E-05  3.15614E-02 0.00088  1.10280E-01 0.00097  3.21881E-01 0.00087  1.34379E+00 0.00058  8.99423E+00 0.00542 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  2.52630E-05 0.00520  2.52506E-05 0.00522  1.88159E-05 0.05417 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  2.99444E-05 0.00507  2.99295E-05 0.00509  2.23045E-05 0.05436 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  14]) = [  6.80661E-03 0.05390  9.64256E-05 0.40158  1.02084E-03 0.13491  9.66084E-04 0.12850  3.36041E-03 0.07854  1.07800E-03 0.13645  2.84853E-04 0.22163 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  14]) = [  8.08853E-01 0.10323  1.24910E-02 2.7E-05  3.15688E-02 0.00199  1.09825E-01 0.00152  3.22256E-01 0.00197  1.34310E+00 0.00126  9.00676E+00 0.01259 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  14]) = [  6.87261E-03 0.05154  9.62772E-05 0.35651  1.07070E-03 0.13562  9.48877E-04 0.12753  3.38250E-03 0.07365  1.07073E-03 0.13212  3.03512E-04 0.21462 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  14]) = [  8.17243E-01 0.10270  1.24910E-02 2.7E-05  3.15671E-02 0.00200  1.09842E-01 0.00154  3.22204E-01 0.00196  1.34306E+00 0.00126  9.00676E+00 0.01259 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -2.73832E+02 0.05521 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  2.53912E-05 0.00148 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  3.00982E-05 0.00105 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  7.14438E-03 0.01054 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -2.82070E+02 0.01091 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  3.75810E-07 0.00122 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  4.23233E-06 0.00097  4.23198E-06 0.00098  4.27771E-06 0.01246 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.54110E-05 0.00136  3.54081E-05 0.00136  3.55596E-05 0.01699 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.40888E-01 0.00095  5.40005E-01 0.00097  7.29140E-01 0.02107 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.04821E+01 0.02819 ];
ANA_MEAN_NCOL             (idx, [1:   4]) = [  2.81559E+01 0.00056  3.19056E+01 0.00076 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  2])  = '11' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  1.00000E-11  5.00000E-09  1.00000E-08  1.50000E-08  2.00000E-08  2.50000E-08  3.00000E-08  3.50000E-08  4.20000E-08  5.00000E-08  5.80000E-08  6.70000E-08  8.00000E-08  1.00000E-07  1.40000E-07  1.80000E-07  2.20000E-07  2.50000E-07  2.80000E-07  3.00000E-07  3.20000E-07  3.50000E-07  4.00000E-07  5.00000E-07  6.25000E-07  7.80000E-07  8.50000E-07  9.10000E-07  9.50000E-07  9.72000E-07  9.96000E-07  1.02000E-06  1.04500E-06  1.07100E-06  1.09700E-06  1.12300E-06  1.15000E-06  1.30000E-06  1.50000E-06  1.85500E-06  2.10000E-06  2.60000E-06  3.30000E-06  4.00000E-06  9.87700E-06  1.59680E-05  2.77000E-05  4.80520E-05  7.55014E-05  1.48728E-04  3.67262E-04  9.06898E-04  1.42510E-03  2.23945E-03  3.51910E-03  5.50000E-03  9.11800E-03  1.50300E-02  2.47800E-02  4.08500E-02  6.74300E-02  1.11000E-01  1.83000E-01  3.02500E-01  5.00000E-01  8.21000E-01  1.35300E+00  2.23100E+00  3.67900E+00  6.06550E+00  2.00000E+01 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Micro-group spectrum:

INF_MICRO_FLX             (idx, [1: 140]) = [  1.14060E+04 0.00989  4.64389E+04 0.00378  9.70860E+04 0.00223  1.00939E+05 0.00202  9.55682E+04 0.00158  1.13933E+05 0.00136  7.73546E+04 0.00162  7.18436E+04 0.00125  5.52417E+04 0.00141  4.54780E+04 0.00140  3.92161E+04 0.00128  3.50744E+04 0.00119  3.24963E+04 0.00164  3.07475E+04 0.00155  2.99567E+04 0.00169  2.57542E+04 0.00176  2.54490E+04 0.00187  2.50606E+04 0.00141  2.45811E+04 0.00118  4.75172E+04 0.00105  4.54100E+04 0.00151  3.21925E+04 0.00142  2.05595E+04 0.00206  2.32295E+04 0.00176  2.14542E+04 0.00222  1.94756E+04 0.00173  3.08104E+04 0.00150  6.97824E+03 0.00352  8.73742E+03 0.00299  7.90219E+03 0.00391  4.61540E+03 0.00451  7.98697E+03 0.00396  5.43693E+03 0.00355  4.64838E+03 0.00311  8.81348E+02 0.00949  8.64905E+02 0.00802  8.96947E+02 0.00833  9.24856E+02 0.00926  9.17976E+02 0.00900  8.94686E+02 0.00842  9.21126E+02 0.00967  8.74374E+02 0.01041  1.64058E+03 0.00601  2.62741E+03 0.00551  3.36828E+03 0.00535  8.79288E+03 0.00280  9.25578E+03 0.00288  9.81815E+03 0.00353  6.39488E+03 0.00338  4.56984E+03 0.00377  3.45448E+03 0.00538  3.93441E+03 0.00455  7.11093E+03 0.00297  8.99940E+03 0.00294  1.63411E+04 0.00250  2.33372E+04 0.00281  3.26335E+04 0.00242  1.99291E+04 0.00268  1.39694E+04 0.00269  9.90195E+03 0.00275  8.78069E+03 0.00257  8.55739E+03 0.00282  7.08149E+03 0.00380  4.74338E+03 0.00330  4.37071E+03 0.00408  3.86513E+03 0.00345  3.25716E+03 0.00438  2.56596E+03 0.00426  1.71814E+03 0.00429  6.32260E+02 0.00549 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];

% Flux spectra in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  3.23022E+01 0.00091  5.37169E+00 0.00132 ];
INF_FISS_FLX              (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  4.05884E-01 0.00031  1.10727E+00 0.00024 ];
INF_CAPT                  (idx, [1:   4]) = [  1.60334E-04 0.00152  5.18238E-03 0.00041 ];
INF_ABS                   (idx, [1:   4]) = [  1.60334E-04 0.00152  5.18238E-03 0.00041 ];
INF_FISS                  (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_NSF                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_NUBAR                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_KAPPA                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_INVV                  (idx, [1:   4]) = [  5.56370E-08 0.00103  2.38662E-06 0.00041 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  4.05723E-01 0.00031  1.10211E+00 0.00025 ];
INF_SCATT1                (idx, [1:   4]) = [  2.37270E-01 0.00036  3.30454E-01 0.00083 ];
INF_SCATT2                (idx, [1:   4]) = [  9.08640E-02 0.00052  8.34292E-02 0.00237 ];
INF_SCATT3                (idx, [1:   4]) = [  2.96885E-03 0.01270  2.53886E-02 0.00649 ];
INF_SCATT4                (idx, [1:   4]) = [ -1.37267E-02 0.00269 -5.63799E-03 0.02246 ];
INF_SCATT5                (idx, [1:   4]) = [ -1.13816E-03 0.03126  4.63580E-03 0.03702 ];
INF_SCATT6                (idx, [1:   4]) = [  4.67010E-03 0.00943 -1.24902E-02 0.01285 ];
INF_SCATT7                (idx, [1:   4]) = [  4.58007E-04 0.08796 -2.07497E-04 0.60667 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  4.05723E-01 0.00031  1.10211E+00 0.00025 ];
INF_SCATTP1               (idx, [1:   4]) = [  2.37270E-01 0.00036  3.30454E-01 0.00083 ];
INF_SCATTP2               (idx, [1:   4]) = [  9.08640E-02 0.00052  8.34292E-02 0.00237 ];
INF_SCATTP3               (idx, [1:   4]) = [  2.96885E-03 0.01270  2.53886E-02 0.00649 ];
INF_SCATTP4               (idx, [1:   4]) = [ -1.37267E-02 0.00269 -5.63799E-03 0.02246 ];
INF_SCATTP5               (idx, [1:   4]) = [ -1.13816E-03 0.03126  4.63580E-03 0.03702 ];
INF_SCATTP6               (idx, [1:   4]) = [  4.67010E-03 0.00943 -1.24902E-02 0.01285 ];
INF_SCATTP7               (idx, [1:   4]) = [  4.58007E-04 0.08796 -2.07497E-04 0.60667 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  1.06267E-01 0.00081  6.65184E-01 0.00059 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  3.13681E+00 0.00082  5.01119E-01 0.00059 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  1.60334E-04 0.00152  5.18238E-03 0.00041 ];
INF_REMXS                 (idx, [1:   4]) = [  1.67723E-02 0.00095  6.38692E-03 0.00685 ];

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

INF_S0                    (idx, [1:   8]) = [  3.89112E-01 0.00030  1.66113E-02 0.00100  1.22214E-03 0.01231  1.10088E+00 0.00025 ];
INF_S1                    (idx, [1:   8]) = [  2.32301E-01 0.00036  4.96814E-03 0.00222  7.82864E-04 0.01466  3.29672E-01 0.00083 ];
INF_S2                    (idx, [1:   8]) = [  9.23298E-02 0.00049 -1.46580E-03 0.00605  4.18837E-04 0.01549  8.30104E-02 0.00241 ];
INF_S3                    (idx, [1:   8]) = [  4.70003E-03 0.00751 -1.73118E-03 0.00420  1.56624E-04 0.03493  2.52320E-02 0.00655 ];
INF_S4                    (idx, [1:   8]) = [ -1.31675E-02 0.00281 -5.59163E-04 0.01080  2.82965E-06 1.00000 -5.64082E-03 0.02268 ];
INF_S5                    (idx, [1:   8]) = [ -1.16458E-03 0.02931  2.64185E-05 0.21106 -5.51118E-05 0.09737  4.69091E-03 0.03635 ];
INF_S6                    (idx, [1:   8]) = [  4.80631E-03 0.00895 -1.36212E-04 0.04467 -6.92795E-05 0.07104 -1.24210E-02 0.01298 ];
INF_S7                    (idx, [1:   8]) = [  6.22361E-04 0.06387 -1.64354E-04 0.02476 -6.68784E-05 0.07102 -1.40619E-04 0.90749 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  3.89112E-01 0.00030  1.66113E-02 0.00100  1.22214E-03 0.01231  1.10088E+00 0.00025 ];
INF_SP1                   (idx, [1:   8]) = [  2.32301E-01 0.00036  4.96814E-03 0.00222  7.82864E-04 0.01466  3.29672E-01 0.00083 ];
INF_SP2                   (idx, [1:   8]) = [  9.23298E-02 0.00049 -1.46580E-03 0.00605  4.18837E-04 0.01549  8.30104E-02 0.00241 ];
INF_SP3                   (idx, [1:   8]) = [  4.70003E-03 0.00751 -1.73118E-03 0.00420  1.56624E-04 0.03493  2.52320E-02 0.00655 ];
INF_SP4                   (idx, [1:   8]) = [ -1.31675E-02 0.00281 -5.59163E-04 0.01080  2.82965E-06 1.00000 -5.64082E-03 0.02268 ];
INF_SP5                   (idx, [1:   8]) = [ -1.16458E-03 0.02931  2.64185E-05 0.21106 -5.51118E-05 0.09737  4.69091E-03 0.03635 ];
INF_SP6                   (idx, [1:   8]) = [  4.80631E-03 0.00895 -1.36212E-04 0.04467 -6.92795E-05 0.07104 -1.24210E-02 0.01298 ];
INF_SP7                   (idx, [1:   8]) = [  6.22361E-04 0.06387 -1.64354E-04 0.02476 -6.68784E-05 0.07102 -1.40619E-04 0.90749 ];

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

CMM_TRANSPXS              (idx, [1:   4]) = [  2.14378E-01 0.00210 -3.81583E-02 0.00268 ];
CMM_TRANSPXS_X            (idx, [1:   4]) = [  2.14612E-01 0.00284 -3.82144E-02 0.00355 ];
CMM_TRANSPXS_Y            (idx, [1:   4]) = [  2.15373E-01 0.00316 -3.83140E-02 0.00310 ];
CMM_TRANSPXS_Z            (idx, [1:   4]) = [  2.13227E-01 0.00283 -3.79613E-02 0.00370 ];
CMM_DIFFCOEF              (idx, [1:   4]) = [  1.55505E+00 0.00209 -8.73706E+00 0.00270 ];
CMM_DIFFCOEF_X            (idx, [1:   4]) = [  1.55349E+00 0.00282 -8.72535E+00 0.00357 ];
CMM_DIFFCOEF_Y            (idx, [1:   4]) = [  1.54807E+00 0.00317 -8.70206E+00 0.00311 ];
CMM_DIFFCOEF_Z            (idx, [1:   4]) = [  1.56358E+00 0.00282 -8.78375E+00 0.00369 ];

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
INPUT_FILE_NAME           (idx, [1: 11])  = 'GroupConst2' ;
WORKING_DIRECTORY         (idx, [1: 50])  = '/home/huaiqian/Serpent2.1.29/src/GroupConstforpin2' ;
HOSTNAME                  (idx, [1:  8])  = 'huaiqian' ;
CPU_TYPE                  (idx, [1: 40])  = 'Intel(R) Core(TM) i5-3570K CPU @ 3.40GHz' ;
CPU_MHZ                   (idx, 1)        = 28.0 ;
START_DATE                (idx, [1: 24])  = 'Fri Nov  3 13:12:18 2017' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Fri Nov  3 13:13:52 2017' ;

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
ST_FRAC                   (idx, [1:   4]) = [  8.03392E-03 0.00302  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.91966E-01 2.4E-05  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  8.31643E-01 9.8E-05  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  8.32013E-01 9.8E-05  0.00000E+00 0.0E+00 ];
AVG_TRACKING_LOOPS        (idx, [1:   8]) = [  2.38005E+00 0.00037  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  2.81559E+01 0.00056  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  2.81559E+01 0.00056  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  5.68484E+00 0.00075  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  1.98994E-01 0.00346  0.00000E+00 0.0E+00 ];
LOST_PARTICLES            (idx, 1)        = 0 ;

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 500 ;
SOURCE_POPULATION         (idx, 1)        = 1000536 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  2.00107E+03 0.00143 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  2.00107E+03 0.00143 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  1.57210E+00 ;
RUNNING_TIME              (idx, 1)        =  1.57380E+00 ;
INIT_TIME                 (idx, [1:  2])  = [  1.30000E-02  1.30000E-02 ];
PROCESS_TIME              (idx, [1:  2])  = [  9.99989E-05  9.99989E-05 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  1.56070E+00  1.56070E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  1.57347E+00  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 0.99892 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  9.99031E-01 0.00011 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  9.85682E-01 ;

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

NORM_COEF                 (idx, [1:   4]) = [  4.99192E-04 0.00083  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  7.24138E-01 0.00209 ];
U235_FISS                 (idx, [1:   4]) = [  4.36100E-01 0.00121  9.10007E-01 0.00043 ];
U238_FISS                 (idx, [1:   4]) = [  4.31496E-02 0.00476  8.99926E-02 0.00439 ];
U235_CAPT                 (idx, [1:   4]) = [  9.88106E-02 0.00305  1.89601E-01 0.00281 ];
U238_CAPT                 (idx, [1:   4]) = [  3.87099E-01 0.00160  7.42690E-01 0.00080 ];

% Neutron balance (particles/weight):

BALA_SRC_NEUTRON_SRC        (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_FISS       (idx, [1:  2])  = [ 1000536 1.00000E+06 ];
BALA_SRC_NEUTRON_NXN        (idx, [1:  2])  = [ 0 2.06700E+03 ];
BALA_SRC_NEUTRON_VR         (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_TOT        (idx, [1:  2])  = [ 1000536 1.00207E+06 ];

BALA_LOSS_NEUTRON_CAPT       (idx, [1:  2])  = [ 521148 5.22008E+05 ];
BALA_LOSS_NEUTRON_FISS       (idx, [1:  2])  = [ 479388 4.80059E+05 ];
BALA_LOSS_NEUTRON_LEAK       (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_CUT        (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_TOT        (idx, [1:  2])  = [ 1000536 1.00207E+06 ];

BALA_NEUTRON_DIFF            (idx, [1:  2])  = [ 0 2.79397E-09 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.55427E-11 0.00054 ];
TOT_POWDENS               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_GENRATE               (idx, [1:   2]) = [  1.18233E+00 0.00053 ];
TOT_FISSRATE              (idx, [1:   2]) = [  4.78594E-01 0.00054 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  5.21406E-01 0.00049 ];
TOT_ABSRATE               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.98384E-01 0.00083 ];
TOT_FLUX                  (idx, [1:   2]) = [  5.80910E+01 0.00069 ];
TOT_PHOTON_PRODRATE       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  2.81613E+01 0.00053 ];
INI_FMASS                 (idx, 1)        =  0.00000E+00 ;
TOT_FMASS                 (idx, 1)        =  0.00000E+00 ;

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.47042E+00 3.7E-05 ];
FISSE                     (idx, [1:   2]) = [  2.02697E+02 4.0E-06 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.18601E+00 0.00103  1.17744E+00 0.00104  8.53846E-03 0.01788 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.18480E+00 0.00053 ];
COL_KEFF                  (idx, [1:   2]) = [  1.18474E+00 0.00113 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.18480E+00 0.00053 ];
ABS_KINF                  (idx, [1:   2]) = [  1.18480E+00 0.00053 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% ALF (Average lethargy of neutrons causing fission):
% Based on E0 = 2.000000E+01 MeV

ANA_ALF                   (idx, [1:   2]) = [  1.68270E+01 0.00046 ];
IMP_ALF                   (idx, [1:   2]) = [  1.68217E+01 0.00024 ];

% EALF (Energy corresponding to average lethargy of neutrons causing fission):

ANA_EALF                  (idx, [1:   2]) = [  9.99308E-07 0.00786 ];
IMP_EALF                  (idx, [1:   2]) = [  9.93644E-07 0.00403 ];

% AFGE (Average energy of neutrons causing fission):

ANA_AFGE                  (idx, [1:   2]) = [  3.00087E-01 0.00485 ];
IMP_AFGE                  (idx, [1:   2]) = [  2.99660E-01 0.00240 ];

% Forward-weighted delayed neutron parameters:

FWD_ANA_BETA_ZERO         (idx, [1:  14]) = [  6.38379E-03 0.01187  1.73455E-04 0.06884  9.90309E-04 0.02847  9.86894E-04 0.02938  2.89753E-03 0.01663  1.00089E-03 0.02974  3.34712E-04 0.05061 ];
FWD_ANA_LAMBDA            (idx, [1:  14]) = [  8.40244E-01 0.02770  4.27185E-03 0.06209  2.90826E-02 0.01304  9.94622E-02 0.01477  3.22034E-01 0.00058  1.20482E+00 0.01526  4.84643E+00 0.04165 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  14]) = [  7.35252E-03 0.01841  1.95279E-04 0.11415  1.11351E-03 0.04629  1.15433E-03 0.04855  3.32480E-03 0.02586  1.20145E-03 0.04549  3.63148E-04 0.07473 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  14]) = [  8.11588E-01 0.03819  1.24908E-02 5.5E-06  3.15414E-02 0.00075  1.10283E-01 0.00078  3.21679E-01 0.00075  1.34456E+00 0.00046  9.01234E+00 0.00387 ];

% Adjoint weighted time constants using Nauchi's method:

ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  2.53659E-05 0.00239  2.53439E-05 0.00239  2.84668E-05 0.02853 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  3.00674E-05 0.00213  3.00413E-05 0.00213  3.37408E-05 0.02855 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  14]) = [  7.20878E-03 0.01811  1.75547E-04 0.11110  1.13098E-03 0.04114  1.14229E-03 0.04409  3.28764E-03 0.02647  1.13147E-03 0.04582  3.40859E-04 0.08080 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  14]) = [  7.83409E-01 0.04441  1.24910E-02 1.1E-05  3.15614E-02 0.00088  1.10280E-01 0.00097  3.21881E-01 0.00087  1.34379E+00 0.00058  8.99423E+00 0.00542 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  2.52630E-05 0.00520  2.52506E-05 0.00522  1.88159E-05 0.05417 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  2.99444E-05 0.00507  2.99295E-05 0.00509  2.23045E-05 0.05436 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  14]) = [  6.80661E-03 0.05390  9.64256E-05 0.40158  1.02084E-03 0.13491  9.66084E-04 0.12850  3.36041E-03 0.07854  1.07800E-03 0.13645  2.84853E-04 0.22163 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  14]) = [  8.08853E-01 0.10323  1.24910E-02 2.7E-05  3.15688E-02 0.00199  1.09825E-01 0.00152  3.22256E-01 0.00197  1.34310E+00 0.00126  9.00676E+00 0.01259 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  14]) = [  6.87261E-03 0.05154  9.62772E-05 0.35651  1.07070E-03 0.13562  9.48877E-04 0.12753  3.38250E-03 0.07365  1.07073E-03 0.13212  3.03512E-04 0.21462 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  14]) = [  8.17243E-01 0.10270  1.24910E-02 2.7E-05  3.15671E-02 0.00200  1.09842E-01 0.00154  3.22204E-01 0.00196  1.34306E+00 0.00126  9.00676E+00 0.01259 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -2.73832E+02 0.05521 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  2.53912E-05 0.00148 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  3.00982E-05 0.00105 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  7.14438E-03 0.01054 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -2.82070E+02 0.01091 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  3.75810E-07 0.00122 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  4.23233E-06 0.00097  4.23198E-06 0.00098  4.27771E-06 0.01246 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.54110E-05 0.00136  3.54081E-05 0.00136  3.55596E-05 0.01699 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.40888E-01 0.00095  5.40005E-01 0.00097  7.29140E-01 0.02107 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.04821E+01 0.02819 ];
ANA_MEAN_NCOL             (idx, [1:   4]) = [  2.81559E+01 0.00056  3.19056E+01 0.00076 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  2])  = '12' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  1.00000E-11  5.00000E-09  1.00000E-08  1.50000E-08  2.00000E-08  2.50000E-08  3.00000E-08  3.50000E-08  4.20000E-08  5.00000E-08  5.80000E-08  6.70000E-08  8.00000E-08  1.00000E-07  1.40000E-07  1.80000E-07  2.20000E-07  2.50000E-07  2.80000E-07  3.00000E-07  3.20000E-07  3.50000E-07  4.00000E-07  5.00000E-07  6.25000E-07  7.80000E-07  8.50000E-07  9.10000E-07  9.50000E-07  9.72000E-07  9.96000E-07  1.02000E-06  1.04500E-06  1.07100E-06  1.09700E-06  1.12300E-06  1.15000E-06  1.30000E-06  1.50000E-06  1.85500E-06  2.10000E-06  2.60000E-06  3.30000E-06  4.00000E-06  9.87700E-06  1.59680E-05  2.77000E-05  4.80520E-05  7.55014E-05  1.48728E-04  3.67262E-04  9.06898E-04  1.42510E-03  2.23945E-03  3.51910E-03  5.50000E-03  9.11800E-03  1.50300E-02  2.47800E-02  4.08500E-02  6.74300E-02  1.11000E-01  1.83000E-01  3.02500E-01  5.00000E-01  8.21000E-01  1.35300E+00  2.23100E+00  3.67900E+00  6.06550E+00  2.00000E+01 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Micro-group spectrum:

INF_MICRO_FLX             (idx, [1: 140]) = [  6.32320E+03 0.00879  2.62108E+04 0.00385  5.47405E+04 0.00243  5.68868E+04 0.00253  5.42798E+04 0.00165  6.47917E+04 0.00206  4.36163E+04 0.00233  4.04238E+04 0.00233  3.07974E+04 0.00244  2.49673E+04 0.00285  2.13357E+04 0.00313  1.91245E+04 0.00210  1.76471E+04 0.00274  1.66199E+04 0.00360  1.61248E+04 0.00267  1.38917E+04 0.00320  1.35801E+04 0.00445  1.33698E+04 0.00386  1.29720E+04 0.00454  2.52538E+04 0.00228  2.38827E+04 0.00321  1.68522E+04 0.00341  1.06883E+04 0.00342  1.17818E+04 0.00312  1.07483E+04 0.00406  1.03243E+04 0.00467  1.52125E+04 0.00313  3.73735E+03 0.00450  4.71653E+03 0.00424  4.24114E+03 0.00562  2.49930E+03 0.00701  4.33933E+03 0.00572  2.90935E+03 0.00688  2.46641E+03 0.00735  4.52228E+02 0.01430  4.65637E+02 0.01660  4.71163E+02 0.01389  4.87393E+02 0.01290  4.83445E+02 0.01803  4.64109E+02 0.01130  4.92735E+02 0.01585  4.66927E+02 0.01893  8.83304E+02 0.01284  1.40979E+03 0.00909  1.79438E+03 0.00741  4.72147E+03 0.00639  4.89590E+03 0.00507  5.19011E+03 0.00542  3.36149E+03 0.00663  2.36794E+03 0.00689  1.80105E+03 0.00652  2.04896E+03 0.00844  3.68889E+03 0.00517  4.71336E+03 0.00483  8.49169E+03 0.00395  1.20972E+04 0.00364  1.65819E+04 0.00307  1.00682E+04 0.00266  6.93134E+03 0.00401  4.88787E+03 0.00355  4.28833E+03 0.00295  4.11714E+03 0.00361  3.34927E+03 0.00500  2.21826E+03 0.00469  2.01558E+03 0.00559  1.73959E+03 0.00616  1.45285E+03 0.00542  1.09734E+03 0.00613  6.77324E+02 0.00848  2.14601E+02 0.01096 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.22516E+00 0.00118 ];

% Flux spectra in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  1.77201E+01 0.00121  2.70294E+00 0.00087 ];
INF_FISS_FLX              (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  4.23544E-01 0.00023  5.92681E-01 0.00015 ];
INF_CAPT                  (idx, [1:   4]) = [  1.91355E-02 0.00117  5.52901E-02 0.00041 ];
INF_ABS                   (idx, [1:   4]) = [  2.57118E-02 0.00091  1.89312E-01 0.00045 ];
INF_FISS                  (idx, [1:   4]) = [  6.57631E-03 0.00068  1.34022E-01 0.00047 ];
INF_NSF                   (idx, [1:   4]) = [  1.69353E-02 0.00071  3.26572E-01 0.00047 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.57519E+00 0.00013  2.43670E+00 0.0E+00 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.04025E+02 1.3E-05  2.02270E+02 2.7E-09 ];
INF_INVV                  (idx, [1:   4]) = [  5.34359E-08 0.00140  2.31969E-06 0.00043 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  3.97825E-01 0.00025  4.03343E-01 0.00054 ];
INF_SCATT1                (idx, [1:   4]) = [  4.35225E-02 0.00196  7.91963E-03 0.03063 ];
INF_SCATT2                (idx, [1:   4]) = [  2.24901E-02 0.00361  5.47637E-04 0.38546 ];
INF_SCATT3                (idx, [1:   4]) = [  1.19725E-02 0.00582 -1.25052E-05 1.00000 ];
INF_SCATT4                (idx, [1:   4]) = [  7.62336E-03 0.00640  6.37509E-05 1.00000 ];
INF_SCATT5                (idx, [1:   4]) = [  3.88662E-03 0.01173  5.65840E-05 1.00000 ];
INF_SCATT6                (idx, [1:   4]) = [  1.92967E-03 0.02225 -2.00207E-05 1.00000 ];
INF_SCATT7                (idx, [1:   4]) = [  8.60057E-04 0.04783 -2.84109E-05 1.00000 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  3.97941E-01 0.00025  4.03343E-01 0.00054 ];
INF_SCATTP1               (idx, [1:   4]) = [  4.35248E-02 0.00194  7.91963E-03 0.03063 ];
INF_SCATTP2               (idx, [1:   4]) = [  2.24925E-02 0.00363  5.47637E-04 0.38546 ];
INF_SCATTP3               (idx, [1:   4]) = [  1.19729E-02 0.00581 -1.25052E-05 1.00000 ];
INF_SCATTP4               (idx, [1:   4]) = [  7.62287E-03 0.00641  6.37509E-05 1.00000 ];
INF_SCATTP5               (idx, [1:   4]) = [  3.88667E-03 0.01173  5.65840E-05 1.00000 ];
INF_SCATTP6               (idx, [1:   4]) = [  1.92999E-03 0.02226 -2.00207E-05 1.00000 ];
INF_SCATTP7               (idx, [1:   4]) = [  8.60000E-04 0.04776 -2.84109E-05 1.00000 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  3.10657E-01 0.00061  5.66593E-01 0.00045 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.07300E+00 0.00061  5.88314E-01 0.00045 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  2.55953E-02 0.00092  1.89312E-01 0.00045 ];
INF_REMXS                 (idx, [1:   4]) = [  2.65198E-02 0.00132  1.91074E-01 0.00109 ];

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

INF_S0                    (idx, [1:   8]) = [  3.97024E-01 0.00025  8.00780E-04 0.00772  1.73639E-03 0.01177  4.01607E-01 0.00055 ];
INF_S1                    (idx, [1:   8]) = [  4.37084E-02 0.00193 -1.85860E-04 0.01664 -1.43368E-04 0.10284  8.06300E-03 0.03009 ];
INF_S2                    (idx, [1:   8]) = [  2.25099E-02 0.00360 -1.98158E-05 0.16676 -8.39430E-05 0.12729  6.31580E-04 0.33757 ];
INF_S3                    (idx, [1:   8]) = [  1.19792E-02 0.00580 -6.77895E-06 0.40782 -3.20918E-05 0.34487  1.95866E-05 1.00000 ];
INF_S4                    (idx, [1:   8]) = [  7.62450E-03 0.00646 -1.13371E-06 1.00000 -6.52753E-06 1.00000  7.02785E-05 1.00000 ];
INF_S5                    (idx, [1:   8]) = [  3.89062E-03 0.01160 -4.00241E-06 0.59702 -7.41313E-06 1.00000  6.39971E-05 1.00000 ];
INF_S6                    (idx, [1:   8]) = [  1.93011E-03 0.02192 -4.35413E-07 1.00000 -1.18846E-05 0.49515 -8.13614E-06 1.00000 ];
INF_S7                    (idx, [1:   8]) = [  8.57701E-04 0.04713  2.35624E-06 0.81176 -4.27780E-06 1.00000 -2.41331E-05 1.00000 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  3.97141E-01 0.00025  8.00780E-04 0.00772  1.73639E-03 0.01177  4.01607E-01 0.00055 ];
INF_SP1                   (idx, [1:   8]) = [  4.37106E-02 0.00192 -1.85860E-04 0.01664 -1.43368E-04 0.10284  8.06300E-03 0.03009 ];
INF_SP2                   (idx, [1:   8]) = [  2.25124E-02 0.00362 -1.98158E-05 0.16676 -8.39430E-05 0.12729  6.31580E-04 0.33757 ];
INF_SP3                   (idx, [1:   8]) = [  1.19797E-02 0.00579 -6.77895E-06 0.40782 -3.20918E-05 0.34487  1.95866E-05 1.00000 ];
INF_SP4                   (idx, [1:   8]) = [  7.62400E-03 0.00647 -1.13371E-06 1.00000 -6.52753E-06 1.00000  7.02785E-05 1.00000 ];
INF_SP5                   (idx, [1:   8]) = [  3.89067E-03 0.01160 -4.00241E-06 0.59702 -7.41313E-06 1.00000  6.39971E-05 1.00000 ];
INF_SP6                   (idx, [1:   8]) = [  1.93042E-03 0.02193 -4.35413E-07 1.00000 -1.18846E-05 0.49515 -8.13614E-06 1.00000 ];
INF_SP7                   (idx, [1:   8]) = [  8.57644E-04 0.04706  2.35624E-06 0.81176 -4.27780E-06 1.00000 -2.41331E-05 1.00000 ];

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

CMM_TRANSPXS              (idx, [1:   4]) = [  1.44181E-01 0.00191  1.85208E-02 0.00165 ];
CMM_TRANSPXS_X            (idx, [1:   4]) = [  1.44381E-01 0.00258  1.85490E-02 0.00236 ];
CMM_TRANSPXS_Y            (idx, [1:   4]) = [  1.44614E-01 0.00241  1.85736E-02 0.00220 ];
CMM_TRANSPXS_Z            (idx, [1:   4]) = [  1.43573E-01 0.00199  1.84431E-02 0.00198 ];
CMM_DIFFCOEF              (idx, [1:   4]) = [  2.31210E+00 0.00190  1.79989E+01 0.00165 ];
CMM_DIFFCOEF_X            (idx, [1:   4]) = [  2.30908E+00 0.00257  1.79728E+01 0.00236 ];
CMM_DIFFCOEF_Y            (idx, [1:   4]) = [  2.30531E+00 0.00242  1.79487E+01 0.00221 ];
CMM_DIFFCOEF_Z            (idx, [1:   4]) = [  2.32192E+00 0.00198  1.80753E+01 0.00197 ];

% Delayed neutron parameters (Meulekamp method):

BETA_EFF                  (idx, [1:  14]) = [  7.35252E-03 0.01841  1.95279E-04 0.11415  1.11351E-03 0.04629  1.15433E-03 0.04855  3.32480E-03 0.02586  1.20145E-03 0.04549  3.63148E-04 0.07473 ];
LAMBDA                    (idx, [1:  14]) = [  8.11588E-01 0.03819  1.24908E-02 5.5E-06  3.15414E-02 0.00075  1.10283E-01 0.00078  3.21679E-01 0.00075  1.34456E+00 0.00046  9.01234E+00 0.00387 ];

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