
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
INPUT_FILE_NAME           (idx, [1: 11])  = 'GroupConst6' ;
WORKING_DIRECTORY         (idx, [1: 50])  = '/home/huaiqian/Serpent2.1.29/src/GroupConstforpin6' ;
HOSTNAME                  (idx, [1:  8])  = 'huaiqian' ;
CPU_TYPE                  (idx, [1: 40])  = 'Intel(R) Core(TM) i5-3570K CPU @ 3.40GHz' ;
CPU_MHZ                   (idx, 1)        = 28.0 ;
START_DATE                (idx, [1: 24])  = 'Fri Nov  3 13:29:03 2017' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Fri Nov  3 13:30:31 2017' ;

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
ST_FRAC                   (idx, [1:   4]) = [  8.77334E-03 0.00285  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.91227E-01 2.5E-05  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  8.38425E-01 0.00011  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  8.38813E-01 0.00011  0.00000E+00 0.0E+00 ];
AVG_TRACKING_LOOPS        (idx, [1:   8]) = [  2.31363E+00 0.00038  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  2.50111E+01 0.00055  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  2.50111E+01 0.00055  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  4.80615E+00 0.00076  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  1.91665E-01 0.00325  0.00000E+00 0.0E+00 ];
LOST_PARTICLES            (idx, 1)        = 0 ;

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 500 ;
SOURCE_POPULATION         (idx, 1)        = 1000501 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  2.00100E+03 0.00148 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  2.00100E+03 0.00148 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  1.47291E+00 ;
RUNNING_TIME              (idx, 1)        =  1.47350E+00 ;
INIT_TIME                 (idx, [1:  2])  = [  1.29167E-02  1.29167E-02 ];
PROCESS_TIME              (idx, [1:  2])  = [  9.99991E-05  9.99991E-05 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  1.46048E+00  1.46048E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  1.47318E+00  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 0.99960 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  9.99688E-01 0.00011 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  9.84775E-01 ;

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

NORM_COEF                 (idx, [1:   4]) = [  4.99208E-04 0.00079  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  5.57189E-01 0.00216 ];
U235_FISS                 (idx, [1:   4]) = [  4.80358E-01 0.00119  9.19097E-01 0.00042 ];
U238_FISS                 (idx, [1:   4]) = [  4.23098E-02 0.00515  8.09028E-02 0.00477 ];
U235_CAPT                 (idx, [1:   4]) = [  1.19652E-01 0.00280  2.50411E-01 0.00243 ];
U238_CAPT                 (idx, [1:   4]) = [  3.34145E-01 0.00172  6.99291E-01 0.00095 ];

% Neutron balance (particles/weight):

BALA_SRC_NEUTRON_SRC        (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_FISS       (idx, [1:  2])  = [ 1000501 1.00000E+06 ];
BALA_SRC_NEUTRON_NXN        (idx, [1:  2])  = [ 0 2.07981E+03 ];
BALA_SRC_NEUTRON_VR         (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_TOT        (idx, [1:  2])  = [ 1000501 1.00208E+06 ];

BALA_LOSS_NEUTRON_CAPT       (idx, [1:  2])  = [ 477745 4.78561E+05 ];
BALA_LOSS_NEUTRON_FISS       (idx, [1:  2])  = [ 522756 5.23518E+05 ];
BALA_LOSS_NEUTRON_LEAK       (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_CUT        (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_TOT        (idx, [1:  2])  = [ 1000501 1.00208E+06 ];

BALA_NEUTRON_DIFF            (idx, [1:  2])  = [ 0 -1.16415E-10 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.69745E-11 0.00049 ];
TOT_POWDENS               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_GENRATE               (idx, [1:   2]) = [  1.29045E+00 0.00048 ];
TOT_FISSRATE              (idx, [1:   2]) = [  5.22791E-01 0.00049 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  4.77209E-01 0.00053 ];
TOT_ABSRATE               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.98416E-01 0.00079 ];
TOT_FLUX                  (idx, [1:   2]) = [  5.43024E+01 0.00063 ];
TOT_PHOTON_PRODRATE       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  2.50177E+01 0.00052 ];
INI_FMASS                 (idx, 1)        =  0.00000E+00 ;
TOT_FMASS                 (idx, 1)        =  0.00000E+00 ;

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.46839E+00 3.2E-05 ];
FISSE                     (idx, [1:   2]) = [  2.02655E+02 3.3E-06 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.29277E+00 0.00104  1.28332E+00 0.00100  8.95614E-03 0.01630 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.29318E+00 0.00048 ];
COL_KEFF                  (idx, [1:   2]) = [  1.29296E+00 0.00102 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.29318E+00 0.00048 ];
ABS_KINF                  (idx, [1:   2]) = [  1.29318E+00 0.00048 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% ALF (Average lethargy of neutrons causing fission):
% Based on E0 = 2.000000E+01 MeV

ANA_ALF                   (idx, [1:   2]) = [  1.63259E+01 0.00048 ];
IMP_ALF                   (idx, [1:   2]) = [  1.63274E+01 0.00022 ];

% EALF (Energy corresponding to average lethargy of neutrons causing fission):

ANA_EALF                  (idx, [1:   2]) = [  1.64997E-06 0.00792 ];
IMP_EALF                  (idx, [1:   2]) = [  1.62766E-06 0.00366 ];

% AFGE (Average energy of neutrons causing fission):

ANA_AFGE                  (idx, [1:   2]) = [  2.83010E-01 0.00523 ];
IMP_AFGE                  (idx, [1:   2]) = [  2.82715E-01 0.00223 ];

% Forward-weighted delayed neutron parameters:

FWD_ANA_BETA_ZERO         (idx, [1:  14]) = [  5.73545E-03 0.01187  1.50676E-04 0.06976  9.10148E-04 0.02983  9.22603E-04 0.02905  2.60900E-03 0.01767  8.66057E-04 0.02940  2.76967E-04 0.05451 ];
FWD_ANA_LAMBDA            (idx, [1:  14]) = [  7.98876E-01 0.02885  4.19695E-03 0.06293  2.83613E-02 0.01510  1.02113E-01 0.01267  3.21358E-01 0.00053  1.22240E+00 0.01408  4.46852E+00 0.04510 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  14]) = [  7.16588E-03 0.01749  1.85503E-04 0.11219  1.08987E-03 0.04445  1.17765E-03 0.04171  3.25603E-03 0.02553  1.08934E-03 0.04567  3.67477E-04 0.08305 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  14]) = [  8.02662E-01 0.04028  1.24909E-02 6.6E-06  3.15865E-02 0.00070  1.10326E-01 0.00082  3.21310E-01 0.00073  1.34306E+00 0.00047  8.97418E+00 0.00391 ];

% Adjoint weighted time constants using Nauchi's method:

ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  1.46411E-05 0.00230  1.46288E-05 0.00231  1.62043E-05 0.02235 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  1.89159E-05 0.00198  1.89002E-05 0.00200  2.09204E-05 0.02219 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  14]) = [  6.89507E-03 0.01671  1.86965E-04 0.10008  1.03914E-03 0.04380  1.15450E-03 0.04040  3.11654E-03 0.02510  1.03957E-03 0.04114  3.58351E-04 0.07617 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  14]) = [  8.29018E-01 0.04337  1.24910E-02 1.0E-05  3.15725E-02 0.00088  1.10402E-01 0.00100  3.21206E-01 0.00081  1.34340E+00 0.00057  8.92299E+00 0.00471 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  1.45413E-05 0.00497  1.45284E-05 0.00501  1.26641E-05 0.04855 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  1.87918E-05 0.00493  1.87751E-05 0.00497  1.63929E-05 0.04857 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  14]) = [  6.90316E-03 0.04802  1.93374E-04 0.27754  1.01261E-03 0.11781  1.16445E-03 0.11273  3.27710E-03 0.07317  9.44895E-04 0.12925  3.10719E-04 0.21565 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  14]) = [  8.28901E-01 0.10565  1.24909E-02 2.0E-05  3.16269E-02 0.00153  1.10479E-01 0.00210  3.21237E-01 0.00173  1.34418E+00 0.00122  9.01723E+00 0.01122 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  14]) = [  6.78730E-03 0.04596  1.82574E-04 0.27114  1.06669E-03 0.11610  1.14678E-03 0.10970  3.13205E-03 0.07132  9.53734E-04 0.12016  3.05468E-04 0.20492 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  14]) = [  8.29984E-01 0.10381  1.24909E-02 2.0E-05  3.16298E-02 0.00152  1.10479E-01 0.00210  3.21190E-01 0.00171  1.34417E+00 0.00122  9.01999E+00 0.01121 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -4.79833E+02 0.04837 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  1.46395E-05 0.00137 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  1.89154E-05 0.00090 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  6.89019E-03 0.00950 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -4.70910E+02 0.00948 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  2.54358E-07 0.00124 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  4.10671E-06 0.00108  4.10656E-06 0.00108  4.12223E-06 0.01363 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  2.30630E-05 0.00140  2.30636E-05 0.00140  2.31802E-05 0.01579 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  4.91652E-01 0.00099  4.90590E-01 0.00100  7.23903E-01 0.02047 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  9.80974E+00 0.02712 ];
ANA_MEAN_NCOL             (idx, [1:   4]) = [  2.50111E+01 0.00055  2.76613E+01 0.00073 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  2])  = '11' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  1.00000E-11  5.00000E-09  1.00000E-08  1.50000E-08  2.00000E-08  2.50000E-08  3.00000E-08  3.50000E-08  4.20000E-08  5.00000E-08  5.80000E-08  6.70000E-08  8.00000E-08  1.00000E-07  1.40000E-07  1.80000E-07  2.20000E-07  2.50000E-07  2.80000E-07  3.00000E-07  3.20000E-07  3.50000E-07  4.00000E-07  5.00000E-07  6.25000E-07  7.80000E-07  8.50000E-07  9.10000E-07  9.50000E-07  9.72000E-07  9.96000E-07  1.02000E-06  1.04500E-06  1.07100E-06  1.09700E-06  1.12300E-06  1.15000E-06  1.30000E-06  1.50000E-06  1.85500E-06  2.10000E-06  2.60000E-06  3.30000E-06  4.00000E-06  9.87700E-06  1.59680E-05  2.77000E-05  4.80520E-05  7.55014E-05  1.48728E-04  3.67262E-04  9.06898E-04  1.42510E-03  2.23945E-03  3.51910E-03  5.50000E-03  9.11800E-03  1.50300E-02  2.47800E-02  4.08500E-02  6.74300E-02  1.11000E-01  1.83000E-01  3.02500E-01  5.00000E-01  8.21000E-01  1.35300E+00  2.23100E+00  3.67900E+00  6.06550E+00  2.00000E+01 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Micro-group spectrum:

INF_MICRO_FLX             (idx, [1: 140]) = [  1.13014E+04 0.00988  4.62982E+04 0.00397  9.68016E+04 0.00263  1.01072E+05 0.00214  9.55578E+04 0.00121  1.13965E+05 0.00153  7.70621E+04 0.00158  7.14901E+04 0.00115  5.50882E+04 0.00142  4.50484E+04 0.00147  3.90207E+04 0.00174  3.48538E+04 0.00156  3.23261E+04 0.00140  3.06402E+04 0.00146  2.97408E+04 0.00148  2.55127E+04 0.00144  2.51841E+04 0.00225  2.47566E+04 0.00151  2.41911E+04 0.00145  4.65012E+04 0.00156  4.41916E+04 0.00141  3.10639E+04 0.00186  1.96941E+04 0.00205  2.20891E+04 0.00173  2.01829E+04 0.00141  1.79634E+04 0.00161  2.84320E+04 0.00161  6.41683E+03 0.00301  8.05495E+03 0.00233  7.32908E+03 0.00304  4.22329E+03 0.00432  7.31891E+03 0.00358  5.01780E+03 0.00419  4.16811E+03 0.00450  7.82136E+02 0.00731  7.78149E+02 0.00993  7.88841E+02 0.00919  8.24803E+02 0.00927  8.26992E+02 0.00975  7.96797E+02 0.00877  8.38534E+02 0.00719  7.76375E+02 0.00798  1.46888E+03 0.00791  2.35652E+03 0.00692  3.01144E+03 0.00479  7.91321E+03 0.00303  8.09080E+03 0.00294  8.38354E+03 0.00293  5.20810E+03 0.00404  3.59835E+03 0.00457  2.61723E+03 0.00324  2.94200E+03 0.00424  5.10857E+03 0.00435  6.28803E+03 0.00299  1.07922E+04 0.00266  1.47325E+04 0.00246  1.95765E+04 0.00226  1.15636E+04 0.00314  7.95819E+03 0.00365  5.56255E+03 0.00336  4.88219E+03 0.00378  4.70108E+03 0.00271  3.87869E+03 0.00362  2.57667E+03 0.00400  2.36205E+03 0.00460  2.07708E+03 0.00469  1.74420E+03 0.00487  1.37831E+03 0.00518  9.28320E+02 0.00460  3.42226E+02 0.00705 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];

% Flux spectra in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  3.17925E+01 0.00099  3.42678E+00 0.00125 ];
INF_FISS_FLX              (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  4.02127E-01 0.00031  1.07045E+00 0.00021 ];
INF_CAPT                  (idx, [1:   4]) = [  1.53297E-04 0.00170  4.88409E-03 0.00037 ];
INF_ABS                   (idx, [1:   4]) = [  1.53297E-04 0.00170  4.88409E-03 0.00037 ];
INF_FISS                  (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_NSF                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_NUBAR                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_KAPPA                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_INVV                  (idx, [1:   4]) = [  5.22477E-08 0.00113  2.24917E-06 0.00037 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  4.01975E-01 0.00031  1.06551E+00 0.00022 ];
INF_SCATT1                (idx, [1:   4]) = [  2.35111E-01 0.00043  3.32504E-01 0.00080 ];
INF_SCATT2                (idx, [1:   4]) = [  8.99450E-02 0.00073  8.68475E-02 0.00234 ];
INF_SCATT3                (idx, [1:   4]) = [  2.73338E-03 0.01967  2.63787E-02 0.00644 ];
INF_SCATT4                (idx, [1:   4]) = [ -1.37448E-02 0.00228 -4.93093E-03 0.03878 ];
INF_SCATT5                (idx, [1:   4]) = [ -1.11640E-03 0.02576  4.05085E-03 0.04305 ];
INF_SCATT6                (idx, [1:   4]) = [  4.68906E-03 0.00675 -1.16438E-02 0.01334 ];
INF_SCATT7                (idx, [1:   4]) = [  4.43549E-04 0.08049 -5.67702E-04 0.22141 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  4.01975E-01 0.00031  1.06551E+00 0.00022 ];
INF_SCATTP1               (idx, [1:   4]) = [  2.35111E-01 0.00043  3.32504E-01 0.00080 ];
INF_SCATTP2               (idx, [1:   4]) = [  8.99450E-02 0.00073  8.68475E-02 0.00234 ];
INF_SCATTP3               (idx, [1:   4]) = [  2.73338E-03 0.01967  2.63787E-02 0.00644 ];
INF_SCATTP4               (idx, [1:   4]) = [ -1.37448E-02 0.00228 -4.93093E-03 0.03878 ];
INF_SCATTP5               (idx, [1:   4]) = [ -1.11640E-03 0.02576  4.05085E-03 0.04305 ];
INF_SCATTP6               (idx, [1:   4]) = [  4.68906E-03 0.00675 -1.16438E-02 0.01334 ];
INF_SCATTP7               (idx, [1:   4]) = [  4.43549E-04 0.08049 -5.67702E-04 0.22141 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  1.05435E-01 0.00062  6.32805E-01 0.00056 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  3.16153E+00 0.00062  5.26759E-01 0.00056 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  1.53297E-04 0.00170  4.88409E-03 0.00037 ];
INF_REMXS                 (idx, [1:   4]) = [  1.54903E-02 0.00113  6.63639E-03 0.00542 ];

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

INF_S0                    (idx, [1:   8]) = [  3.86637E-01 0.00031  1.53379E-02 0.00115  1.69250E-03 0.00931  1.06381E+00 0.00022 ];
INF_S1                    (idx, [1:   8]) = [  2.30549E-01 0.00043  4.56176E-03 0.00218  1.07864E-03 0.01344  3.31425E-01 0.00080 ];
INF_S2                    (idx, [1:   8]) = [  9.13421E-02 0.00070 -1.39709E-03 0.00537  5.84028E-04 0.02241  8.62635E-02 0.00235 ];
INF_S3                    (idx, [1:   8]) = [  4.34335E-03 0.01217 -1.60997E-03 0.00422  2.15057E-04 0.04486  2.61636E-02 0.00657 ];
INF_S4                    (idx, [1:   8]) = [ -1.32348E-02 0.00229 -5.10080E-04 0.01309  1.48526E-05 0.51888 -4.94578E-03 0.03913 ];
INF_S5                    (idx, [1:   8]) = [ -1.14020E-03 0.02548  2.37998E-05 0.25696 -6.98533E-05 0.09111  4.12070E-03 0.04248 ];
INF_S6                    (idx, [1:   8]) = [  4.81344E-03 0.00602 -1.24388E-04 0.05434 -1.02046E-04 0.07933 -1.15417E-02 0.01355 ];
INF_S7                    (idx, [1:   8]) = [  5.86589E-04 0.05663 -1.43040E-04 0.03507 -9.19445E-05 0.07262 -4.75757E-04 0.26476 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  3.86637E-01 0.00031  1.53379E-02 0.00115  1.69250E-03 0.00931  1.06381E+00 0.00022 ];
INF_SP1                   (idx, [1:   8]) = [  2.30549E-01 0.00043  4.56176E-03 0.00218  1.07864E-03 0.01344  3.31425E-01 0.00080 ];
INF_SP2                   (idx, [1:   8]) = [  9.13421E-02 0.00070 -1.39709E-03 0.00537  5.84028E-04 0.02241  8.62635E-02 0.00235 ];
INF_SP3                   (idx, [1:   8]) = [  4.34335E-03 0.01217 -1.60997E-03 0.00422  2.15057E-04 0.04486  2.61636E-02 0.00657 ];
INF_SP4                   (idx, [1:   8]) = [ -1.32348E-02 0.00229 -5.10080E-04 0.01309  1.48526E-05 0.51888 -4.94578E-03 0.03913 ];
INF_SP5                   (idx, [1:   8]) = [ -1.14020E-03 0.02548  2.37998E-05 0.25696 -6.98533E-05 0.09111  4.12070E-03 0.04248 ];
INF_SP6                   (idx, [1:   8]) = [  4.81344E-03 0.00602 -1.24388E-04 0.05434 -1.02046E-04 0.07933 -1.15417E-02 0.01355 ];
INF_SP7                   (idx, [1:   8]) = [  5.86589E-04 0.05663 -1.43040E-04 0.03507 -9.19445E-05 0.07262 -4.75757E-04 0.26476 ];

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

CMM_TRANSPXS              (idx, [1:   4]) = [  2.34236E-01 0.00130 -2.64603E-02 0.00258 ];
CMM_TRANSPXS_X            (idx, [1:   4]) = [  2.34669E-01 0.00229 -2.65150E-02 0.00355 ];
CMM_TRANSPXS_Y            (idx, [1:   4]) = [  2.34627E-01 0.00260 -2.65137E-02 0.00310 ];
CMM_TRANSPXS_Z            (idx, [1:   4]) = [  2.33492E-01 0.00258 -2.63619E-02 0.00351 ];
CMM_DIFFCOEF              (idx, [1:   4]) = [  1.42312E+00 0.00130 -1.25995E+01 0.00257 ];
CMM_DIFFCOEF_X            (idx, [1:   4]) = [  1.42062E+00 0.00231 -1.25753E+01 0.00355 ];
CMM_DIFFCOEF_Y            (idx, [1:   4]) = [  1.42093E+00 0.00263 -1.25750E+01 0.00311 ];
CMM_DIFFCOEF_Z            (idx, [1:   4]) = [  1.42783E+00 0.00256 -1.26482E+01 0.00351 ];

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
INPUT_FILE_NAME           (idx, [1: 11])  = 'GroupConst6' ;
WORKING_DIRECTORY         (idx, [1: 50])  = '/home/huaiqian/Serpent2.1.29/src/GroupConstforpin6' ;
HOSTNAME                  (idx, [1:  8])  = 'huaiqian' ;
CPU_TYPE                  (idx, [1: 40])  = 'Intel(R) Core(TM) i5-3570K CPU @ 3.40GHz' ;
CPU_MHZ                   (idx, 1)        = 28.0 ;
START_DATE                (idx, [1: 24])  = 'Fri Nov  3 13:29:03 2017' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Fri Nov  3 13:30:31 2017' ;

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
ST_FRAC                   (idx, [1:   4]) = [  8.77334E-03 0.00285  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.91227E-01 2.5E-05  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  8.38425E-01 0.00011  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  8.38813E-01 0.00011  0.00000E+00 0.0E+00 ];
AVG_TRACKING_LOOPS        (idx, [1:   8]) = [  2.31363E+00 0.00038  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  2.50111E+01 0.00055  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  2.50111E+01 0.00055  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  4.80615E+00 0.00076  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  1.91665E-01 0.00325  0.00000E+00 0.0E+00 ];
LOST_PARTICLES            (idx, 1)        = 0 ;

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 500 ;
SOURCE_POPULATION         (idx, 1)        = 1000501 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  2.00100E+03 0.00148 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  2.00100E+03 0.00148 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  1.47292E+00 ;
RUNNING_TIME              (idx, 1)        =  1.47350E+00 ;
INIT_TIME                 (idx, [1:  2])  = [  1.29167E-02  1.29167E-02 ];
PROCESS_TIME              (idx, [1:  2])  = [  9.99991E-05  9.99991E-05 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  1.46048E+00  1.46048E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  1.47318E+00  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 0.99961 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  9.99688E-01 0.00011 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  9.84775E-01 ;

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

NORM_COEF                 (idx, [1:   4]) = [  4.99208E-04 0.00079  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  5.57189E-01 0.00216 ];
U235_FISS                 (idx, [1:   4]) = [  4.80358E-01 0.00119  9.19097E-01 0.00042 ];
U238_FISS                 (idx, [1:   4]) = [  4.23098E-02 0.00515  8.09028E-02 0.00477 ];
U235_CAPT                 (idx, [1:   4]) = [  1.19652E-01 0.00280  2.50411E-01 0.00243 ];
U238_CAPT                 (idx, [1:   4]) = [  3.34145E-01 0.00172  6.99291E-01 0.00095 ];

% Neutron balance (particles/weight):

BALA_SRC_NEUTRON_SRC        (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_FISS       (idx, [1:  2])  = [ 1000501 1.00000E+06 ];
BALA_SRC_NEUTRON_NXN        (idx, [1:  2])  = [ 0 2.07981E+03 ];
BALA_SRC_NEUTRON_VR         (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_TOT        (idx, [1:  2])  = [ 1000501 1.00208E+06 ];

BALA_LOSS_NEUTRON_CAPT       (idx, [1:  2])  = [ 477745 4.78561E+05 ];
BALA_LOSS_NEUTRON_FISS       (idx, [1:  2])  = [ 522756 5.23518E+05 ];
BALA_LOSS_NEUTRON_LEAK       (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_CUT        (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_TOT        (idx, [1:  2])  = [ 1000501 1.00208E+06 ];

BALA_NEUTRON_DIFF            (idx, [1:  2])  = [ 0 -1.16415E-10 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.69745E-11 0.00049 ];
TOT_POWDENS               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_GENRATE               (idx, [1:   2]) = [  1.29045E+00 0.00048 ];
TOT_FISSRATE              (idx, [1:   2]) = [  5.22791E-01 0.00049 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  4.77209E-01 0.00053 ];
TOT_ABSRATE               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.98416E-01 0.00079 ];
TOT_FLUX                  (idx, [1:   2]) = [  5.43024E+01 0.00063 ];
TOT_PHOTON_PRODRATE       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  2.50177E+01 0.00052 ];
INI_FMASS                 (idx, 1)        =  0.00000E+00 ;
TOT_FMASS                 (idx, 1)        =  0.00000E+00 ;

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.46839E+00 3.2E-05 ];
FISSE                     (idx, [1:   2]) = [  2.02655E+02 3.3E-06 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.29277E+00 0.00104  1.28332E+00 0.00100  8.95614E-03 0.01630 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.29318E+00 0.00048 ];
COL_KEFF                  (idx, [1:   2]) = [  1.29296E+00 0.00102 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.29318E+00 0.00048 ];
ABS_KINF                  (idx, [1:   2]) = [  1.29318E+00 0.00048 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% ALF (Average lethargy of neutrons causing fission):
% Based on E0 = 2.000000E+01 MeV

ANA_ALF                   (idx, [1:   2]) = [  1.63259E+01 0.00048 ];
IMP_ALF                   (idx, [1:   2]) = [  1.63274E+01 0.00022 ];

% EALF (Energy corresponding to average lethargy of neutrons causing fission):

ANA_EALF                  (idx, [1:   2]) = [  1.64997E-06 0.00792 ];
IMP_EALF                  (idx, [1:   2]) = [  1.62766E-06 0.00366 ];

% AFGE (Average energy of neutrons causing fission):

ANA_AFGE                  (idx, [1:   2]) = [  2.83010E-01 0.00523 ];
IMP_AFGE                  (idx, [1:   2]) = [  2.82715E-01 0.00223 ];

% Forward-weighted delayed neutron parameters:

FWD_ANA_BETA_ZERO         (idx, [1:  14]) = [  5.73545E-03 0.01187  1.50676E-04 0.06976  9.10148E-04 0.02983  9.22603E-04 0.02905  2.60900E-03 0.01767  8.66057E-04 0.02940  2.76967E-04 0.05451 ];
FWD_ANA_LAMBDA            (idx, [1:  14]) = [  7.98876E-01 0.02885  4.19695E-03 0.06293  2.83613E-02 0.01510  1.02113E-01 0.01267  3.21358E-01 0.00053  1.22240E+00 0.01408  4.46852E+00 0.04510 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  14]) = [  7.16588E-03 0.01749  1.85503E-04 0.11219  1.08987E-03 0.04445  1.17765E-03 0.04171  3.25603E-03 0.02553  1.08934E-03 0.04567  3.67477E-04 0.08305 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  14]) = [  8.02662E-01 0.04028  1.24909E-02 6.6E-06  3.15865E-02 0.00070  1.10326E-01 0.00082  3.21310E-01 0.00073  1.34306E+00 0.00047  8.97418E+00 0.00391 ];

% Adjoint weighted time constants using Nauchi's method:

ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  1.46411E-05 0.00230  1.46288E-05 0.00231  1.62043E-05 0.02235 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  1.89159E-05 0.00198  1.89002E-05 0.00200  2.09204E-05 0.02219 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  14]) = [  6.89507E-03 0.01671  1.86965E-04 0.10008  1.03914E-03 0.04380  1.15450E-03 0.04040  3.11654E-03 0.02510  1.03957E-03 0.04114  3.58351E-04 0.07617 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  14]) = [  8.29018E-01 0.04337  1.24910E-02 1.0E-05  3.15725E-02 0.00088  1.10402E-01 0.00100  3.21206E-01 0.00081  1.34340E+00 0.00057  8.92299E+00 0.00471 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  1.45413E-05 0.00497  1.45284E-05 0.00501  1.26641E-05 0.04855 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  1.87918E-05 0.00493  1.87751E-05 0.00497  1.63929E-05 0.04857 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  14]) = [  6.90316E-03 0.04802  1.93374E-04 0.27754  1.01261E-03 0.11781  1.16445E-03 0.11273  3.27710E-03 0.07317  9.44895E-04 0.12925  3.10719E-04 0.21565 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  14]) = [  8.28901E-01 0.10565  1.24909E-02 2.0E-05  3.16269E-02 0.00153  1.10479E-01 0.00210  3.21237E-01 0.00173  1.34418E+00 0.00122  9.01723E+00 0.01122 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  14]) = [  6.78730E-03 0.04596  1.82574E-04 0.27114  1.06669E-03 0.11610  1.14678E-03 0.10970  3.13205E-03 0.07132  9.53734E-04 0.12016  3.05468E-04 0.20492 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  14]) = [  8.29984E-01 0.10381  1.24909E-02 2.0E-05  3.16298E-02 0.00152  1.10479E-01 0.00210  3.21190E-01 0.00171  1.34417E+00 0.00122  9.01999E+00 0.01121 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -4.79833E+02 0.04837 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  1.46395E-05 0.00137 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  1.89154E-05 0.00090 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  6.89019E-03 0.00950 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -4.70910E+02 0.00948 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  2.54358E-07 0.00124 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  4.10671E-06 0.00108  4.10656E-06 0.00108  4.12223E-06 0.01363 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  2.30630E-05 0.00140  2.30636E-05 0.00140  2.31802E-05 0.01579 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  4.91652E-01 0.00099  4.90590E-01 0.00100  7.23903E-01 0.02047 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  9.80974E+00 0.02712 ];
ANA_MEAN_NCOL             (idx, [1:   4]) = [  2.50111E+01 0.00055  2.76613E+01 0.00073 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  2])  = '12' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  1.00000E-11  5.00000E-09  1.00000E-08  1.50000E-08  2.00000E-08  2.50000E-08  3.00000E-08  3.50000E-08  4.20000E-08  5.00000E-08  5.80000E-08  6.70000E-08  8.00000E-08  1.00000E-07  1.40000E-07  1.80000E-07  2.20000E-07  2.50000E-07  2.80000E-07  3.00000E-07  3.20000E-07  3.50000E-07  4.00000E-07  5.00000E-07  6.25000E-07  7.80000E-07  8.50000E-07  9.10000E-07  9.50000E-07  9.72000E-07  9.96000E-07  1.02000E-06  1.04500E-06  1.07100E-06  1.09700E-06  1.12300E-06  1.15000E-06  1.30000E-06  1.50000E-06  1.85500E-06  2.10000E-06  2.60000E-06  3.30000E-06  4.00000E-06  9.87700E-06  1.59680E-05  2.77000E-05  4.80520E-05  7.55014E-05  1.48728E-04  3.67262E-04  9.06898E-04  1.42510E-03  2.23945E-03  3.51910E-03  5.50000E-03  9.11800E-03  1.50300E-02  2.47800E-02  4.08500E-02  6.74300E-02  1.11000E-01  1.83000E-01  3.02500E-01  5.00000E-01  8.21000E-01  1.35300E+00  2.23100E+00  3.67900E+00  6.06550E+00  2.00000E+01 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Micro-group spectrum:

INF_MICRO_FLX             (idx, [1: 140]) = [  6.39596E+03 0.00983  2.61140E+04 0.00424  5.46602E+04 0.00268  5.69724E+04 0.00251  5.42555E+04 0.00201  6.49389E+04 0.00233  4.33881E+04 0.00251  4.02949E+04 0.00229  3.05336E+04 0.00229  2.46911E+04 0.00233  2.12983E+04 0.00255  1.89941E+04 0.00290  1.75241E+04 0.00269  1.65777E+04 0.00264  1.60144E+04 0.00333  1.36857E+04 0.00307  1.34174E+04 0.00321  1.32041E+04 0.00294  1.28562E+04 0.00352  2.46270E+04 0.00311  2.32538E+04 0.00235  1.61381E+04 0.00354  1.01816E+04 0.00401  1.10834E+04 0.00388  9.96437E+03 0.00321  9.42216E+03 0.00401  1.39122E+04 0.00248  3.43052E+03 0.00725  4.33810E+03 0.00728  3.95803E+03 0.00681  2.31395E+03 0.01185  3.96716E+03 0.00662  2.65843E+03 0.00618  2.23662E+03 0.00735  4.03200E+02 0.01426  4.08603E+02 0.01268  4.12662E+02 0.01237  4.28537E+02 0.01355  4.35379E+02 0.01448  4.23940E+02 0.01681  4.43363E+02 0.01110  4.15389E+02 0.01414  7.89987E+02 0.01559  1.24256E+03 0.00824  1.57788E+03 0.01092  4.15095E+03 0.00591  4.25532E+03 0.00619  4.34582E+03 0.00551  2.64813E+03 0.00717  1.83208E+03 0.00531  1.34281E+03 0.00617  1.49093E+03 0.00628  2.52642E+03 0.00773  3.13533E+03 0.00432  5.42053E+03 0.00508  7.27835E+03 0.00452  9.51788E+03 0.00296  5.54657E+03 0.00430  3.75505E+03 0.00534  2.60012E+03 0.00486  2.24317E+03 0.00469  2.12545E+03 0.00522  1.70263E+03 0.00469  1.11395E+03 0.00808  1.00724E+03 0.00625  8.55749E+02 0.00752  6.88156E+02 0.01016  5.09093E+02 0.00674  3.10044E+02 0.00956  8.74810E+01 0.01308 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.32180E+00 0.00138 ];

% Flux spectra in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  1.74332E+01 0.00100  1.65576E+00 0.00116 ];
INF_FISS_FLX              (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  4.25973E-01 0.00017  6.90119E-01 0.00026 ];
INF_CAPT                  (idx, [1:   4]) = [  1.97058E-02 0.00107  6.77526E-02 0.00056 ];
INF_ABS                   (idx, [1:   4]) = [  2.90096E-02 0.00079  2.85644E-01 0.00061 ];
INF_FISS                  (idx, [1:   4]) = [  9.30380E-03 0.00075  2.17891E-01 0.00062 ];
INF_NSF                   (idx, [1:   4]) = [  2.36208E-02 0.00075  5.30936E-01 0.00062 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.53884E+00 7.9E-05  2.43670E+00 0.0E+00 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.03510E+02 8.0E-06  2.02270E+02 2.7E-09 ];
INF_INVV                  (idx, [1:   4]) = [  4.98697E-08 0.00159  2.16007E-06 0.00053 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  3.96982E-01 0.00015  4.04254E-01 0.00095 ];
INF_SCATT1                (idx, [1:   4]) = [  4.40817E-02 0.00289  7.67916E-03 0.04288 ];
INF_SCATT2                (idx, [1:   4]) = [  2.30212E-02 0.00310  5.12670E-04 0.51784 ];
INF_SCATT3                (idx, [1:   4]) = [  1.21652E-02 0.00596 -8.52020E-05 1.00000 ];
INF_SCATT4                (idx, [1:   4]) = [  7.69776E-03 0.00779  4.40051E-05 1.00000 ];
INF_SCATT5                (idx, [1:   4]) = [  3.96229E-03 0.01361  1.05460E-04 1.00000 ];
INF_SCATT6                (idx, [1:   4]) = [  1.93882E-03 0.02352 -1.45358E-04 0.85313 ];
INF_SCATT7                (idx, [1:   4]) = [  8.48556E-04 0.04948  1.59883E-04 0.44267 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  3.97101E-01 0.00015  4.04254E-01 0.00095 ];
INF_SCATTP1               (idx, [1:   4]) = [  4.40823E-02 0.00288  7.67916E-03 0.04288 ];
INF_SCATTP2               (idx, [1:   4]) = [  2.30236E-02 0.00309  5.12670E-04 0.51784 ];
INF_SCATTP3               (idx, [1:   4]) = [  1.21666E-02 0.00595 -8.52020E-05 1.00000 ];
INF_SCATTP4               (idx, [1:   4]) = [  7.69849E-03 0.00778  4.40051E-05 1.00000 ];
INF_SCATTP5               (idx, [1:   4]) = [  3.96197E-03 0.01364  1.05460E-04 1.00000 ];
INF_SCATTP6               (idx, [1:   4]) = [  1.93878E-03 0.02349 -1.45358E-04 0.85313 ];
INF_SCATTP7               (idx, [1:   4]) = [  8.49187E-04 0.04955  1.59883E-04 0.44267 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  3.10182E-01 0.00061  6.49490E-01 0.00065 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.07465E+00 0.00061  5.13229E-01 0.00065 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  2.88905E-02 0.00077  2.85644E-01 0.00061 ];
INF_REMXS                 (idx, [1:   4]) = [  2.97039E-02 0.00132  2.88285E-01 0.00147 ];

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

INF_S0                    (idx, [1:   8]) = [  3.96269E-01 0.00015  7.13284E-04 0.00563  2.42011E-03 0.01474  4.01834E-01 0.00096 ];
INF_S1                    (idx, [1:   8]) = [  4.42460E-02 0.00286 -1.64285E-04 0.01964 -2.48276E-04 0.06828  7.92744E-03 0.04172 ];
INF_S2                    (idx, [1:   8]) = [  2.30441E-02 0.00311 -2.29104E-05 0.12292 -8.77611E-05 0.18956  6.00431E-04 0.43545 ];
INF_S3                    (idx, [1:   8]) = [  1.21688E-02 0.00592 -3.63474E-06 0.62630 -4.01816E-05 0.36720 -4.50204E-05 1.00000 ];
INF_S4                    (idx, [1:   8]) = [  7.69845E-03 0.00774 -6.86685E-07 1.00000 -1.64293E-05 0.63349  6.04344E-05 1.00000 ];
INF_S5                    (idx, [1:   8]) = [  3.96230E-03 0.01365 -1.21504E-08 1.00000 -3.15876E-05 0.34279  1.37048E-04 1.00000 ];
INF_S6                    (idx, [1:   8]) = [  1.94201E-03 0.02333 -3.18781E-06 0.55445 -8.22270E-06 1.00000 -1.37135E-04 0.93505 ];
INF_S7                    (idx, [1:   8]) = [  8.47329E-04 0.04995  1.22621E-06 1.00000 -4.83559E-06 1.00000  1.64719E-04 0.41051 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  3.96388E-01 0.00015  7.13284E-04 0.00563  2.42011E-03 0.01474  4.01834E-01 0.00096 ];
INF_SP1                   (idx, [1:   8]) = [  4.42466E-02 0.00285 -1.64285E-04 0.01964 -2.48276E-04 0.06828  7.92744E-03 0.04172 ];
INF_SP2                   (idx, [1:   8]) = [  2.30465E-02 0.00310 -2.29104E-05 0.12292 -8.77611E-05 0.18956  6.00431E-04 0.43545 ];
INF_SP3                   (idx, [1:   8]) = [  1.21702E-02 0.00590 -3.63474E-06 0.62630 -4.01816E-05 0.36720 -4.50204E-05 1.00000 ];
INF_SP4                   (idx, [1:   8]) = [  7.69918E-03 0.00774 -6.86685E-07 1.00000 -1.64293E-05 0.63349  6.04344E-05 1.00000 ];
INF_SP5                   (idx, [1:   8]) = [  3.96198E-03 0.01369 -1.21504E-08 1.00000 -3.15876E-05 0.34279  1.37048E-04 1.00000 ];
INF_SP6                   (idx, [1:   8]) = [  1.94196E-03 0.02331 -3.18781E-06 0.55445 -8.22270E-06 1.00000 -1.37135E-04 0.93505 ];
INF_SP7                   (idx, [1:   8]) = [  8.47961E-04 0.05001  1.22621E-06 1.00000 -4.83559E-06 1.00000  1.64719E-04 0.41051 ];

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

CMM_TRANSPXS              (idx, [1:   4]) = [  1.29743E-01 0.00139  1.27347E-02 0.00150 ];
CMM_TRANSPXS_X            (idx, [1:   4]) = [  1.30078E-01 0.00161  1.27616E-02 0.00167 ];
CMM_TRANSPXS_Y            (idx, [1:   4]) = [  1.29912E-01 0.00175  1.27579E-02 0.00203 ];
CMM_TRANSPXS_Z            (idx, [1:   4]) = [  1.29260E-01 0.00249  1.26868E-02 0.00252 ];
CMM_DIFFCOEF              (idx, [1:   4]) = [  2.56930E+00 0.00139  2.61767E+01 0.00150 ];
CMM_DIFFCOEF_X            (idx, [1:   4]) = [  2.56272E+00 0.00162  2.61218E+01 0.00167 ];
CMM_DIFFCOEF_Y            (idx, [1:   4]) = [  2.56603E+00 0.00175  2.61302E+01 0.00202 ];
CMM_DIFFCOEF_Z            (idx, [1:   4]) = [  2.57916E+00 0.00249  2.62781E+01 0.00251 ];

% Delayed neutron parameters (Meulekamp method):

BETA_EFF                  (idx, [1:  14]) = [  7.16588E-03 0.01749  1.85503E-04 0.11219  1.08987E-03 0.04445  1.17765E-03 0.04171  3.25603E-03 0.02553  1.08934E-03 0.04567  3.67477E-04 0.08305 ];
LAMBDA                    (idx, [1:  14]) = [  8.02662E-01 0.04028  1.24909E-02 6.6E-06  3.15865E-02 0.00070  1.10326E-01 0.00082  3.21310E-01 0.00073  1.34306E+00 0.00047  8.97418E+00 0.00391 ];

% G = 2;


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