
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
INPUT_FILE_NAME           (idx, [1: 11])  = 'GroupConst3' ;
WORKING_DIRECTORY         (idx, [1: 50])  = '/home/huaiqian/Serpent2.1.29/src/GroupConstforpin3' ;
HOSTNAME                  (idx, [1:  8])  = 'huaiqian' ;
CPU_TYPE                  (idx, [1: 40])  = 'Intel(R) Core(TM) i5-3570K CPU @ 3.40GHz' ;
CPU_MHZ                   (idx, 1)        = 28.0 ;
START_DATE                (idx, [1: 24])  = 'Fri Nov  3 13:15:26 2017' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Fri Nov  3 13:16:58 2017' ;

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
ST_FRAC                   (idx, [1:   4]) = [  8.33167E-03 0.00281  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.91668E-01 2.4E-05  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  8.34448E-01 0.00010  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  8.34825E-01 0.00010  0.00000E+00 0.0E+00 ];
AVG_TRACKING_LOOPS        (idx, [1:   8]) = [  2.35623E+00 0.00039  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  2.68926E+01 0.00055  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  2.68926E+01 0.00055  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  5.32090E+00 0.00075  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  1.96719E-01 0.00314  0.00000E+00 0.0E+00 ];
LOST_PARTICLES            (idx, 1)        = 0 ;

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 500 ;
SOURCE_POPULATION         (idx, 1)        = 1000474 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  2.00095E+03 0.00155 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  2.00095E+03 0.00155 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  1.52547E+00 ;
RUNNING_TIME              (idx, 1)        =  1.52683E+00 ;
INIT_TIME                 (idx, [1:  2])  = [  1.29333E-02  1.29333E-02 ];
PROCESS_TIME              (idx, [1:  2])  = [  8.33335E-05  8.33335E-05 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  1.51382E+00  1.51382E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  1.52653E+00  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 0.99911 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  9.99233E-01 0.00012 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  9.84827E-01 ;

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

NORM_COEF                 (idx, [1:   4]) = [  4.99431E-04 0.00082  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  6.54826E-01 0.00231 ];
U235_FISS                 (idx, [1:   4]) = [  4.54910E-01 0.00123  9.14091E-01 0.00044 ];
U238_FISS                 (idx, [1:   4]) = [  4.27722E-02 0.00502  8.59090E-02 0.00471 ];
U235_CAPT                 (idx, [1:   4]) = [  1.05884E-01 0.00314  2.10431E-01 0.00290 ];
U238_CAPT                 (idx, [1:   4]) = [  3.66941E-01 0.00179  7.29067E-01 0.00090 ];

% Neutron balance (particles/weight):

BALA_SRC_NEUTRON_SRC        (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_FISS       (idx, [1:  2])  = [ 1000474 1.00000E+06 ];
BALA_SRC_NEUTRON_NXN        (idx, [1:  2])  = [ 0 2.09641E+03 ];
BALA_SRC_NEUTRON_VR         (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_TOT        (idx, [1:  2])  = [ 1000474 1.00210E+06 ];

BALA_LOSS_NEUTRON_CAPT       (idx, [1:  2])  = [ 502963 5.03803E+05 ];
BALA_LOSS_NEUTRON_FISS       (idx, [1:  2])  = [ 497511 4.98293E+05 ];
BALA_LOSS_NEUTRON_LEAK       (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_CUT        (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_TOT        (idx, [1:  2])  = [ 1000474 1.00210E+06 ];

BALA_NEUTRON_DIFF            (idx, [1:  2])  = [ 0 1.16415E-09 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.61344E-11 0.00052 ];
TOT_POWDENS               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_GENRATE               (idx, [1:   2]) = [  1.22694E+00 0.00052 ];
TOT_FISSRATE              (idx, [1:   2]) = [  4.96861E-01 0.00052 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  5.03139E-01 0.00051 ];
TOT_ABSRATE               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.98862E-01 0.00082 ];
TOT_FLUX                  (idx, [1:   2]) = [  5.66527E+01 0.00066 ];
TOT_PHOTON_PRODRATE       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  2.69110E+01 0.00052 ];
INI_FMASS                 (idx, 1)        =  0.00000E+00 ;
TOT_FMASS                 (idx, 1)        =  0.00000E+00 ;

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.46938E+00 3.4E-05 ];
FISSE                     (idx, [1:   2]) = [  2.02679E+02 3.8E-06 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.23026E+00 0.00110  1.22187E+00 0.00109  8.59132E-03 0.01642 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.22950E+00 0.00052 ];
COL_KEFF                  (idx, [1:   2]) = [  1.22882E+00 0.00108 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.22950E+00 0.00052 ];
ABS_KINF                  (idx, [1:   2]) = [  1.22950E+00 0.00052 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% ALF (Average lethargy of neutrons causing fission):
% Based on E0 = 2.000000E+01 MeV

ANA_ALF                   (idx, [1:   2]) = [  1.66756E+01 0.00048 ];
IMP_ALF                   (idx, [1:   2]) = [  1.66722E+01 0.00023 ];

% EALF (Energy corresponding to average lethargy of neutrons causing fission):

ANA_EALF                  (idx, [1:   2]) = [  1.16399E-06 0.00814 ];
IMP_EALF                  (idx, [1:   2]) = [  1.15347E-06 0.00390 ];

% AFGE (Average energy of neutrons causing fission):

ANA_AFGE                  (idx, [1:   2]) = [  2.90610E-01 0.00509 ];
IMP_AFGE                  (idx, [1:   2]) = [  2.90873E-01 0.00234 ];

% Forward-weighted delayed neutron parameters:

FWD_ANA_BETA_ZERO         (idx, [1:  14]) = [  5.97768E-03 0.01238  1.72509E-04 0.07238  8.76309E-04 0.03107  9.63366E-04 0.03074  2.71979E-03 0.01772  9.46617E-04 0.02882  2.99092E-04 0.05050 ];
FWD_ANA_LAMBDA            (idx, [1:  14]) = [  8.36652E-01 0.02659  4.17190E-03 0.06321  2.78063E-02 0.01654  9.72965E-02 0.01655  3.22008E-01 0.00062  1.22568E+00 0.01391  4.72775E+00 0.04284 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  14]) = [  6.92330E-03 0.01768  1.76769E-04 0.10670  9.87245E-04 0.04655  1.10433E-03 0.04441  3.20635E-03 0.02684  1.09282E-03 0.04528  3.55792E-04 0.07916 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  14]) = [  8.45328E-01 0.04079  1.24907E-02 4.0E-06  3.15793E-02 0.00072  1.10443E-01 0.00084  3.21860E-01 0.00081  1.34421E+00 0.00045  9.01802E+00 0.00395 ];

% Adjoint weighted time constants using Nauchi's method:

ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  2.06811E-05 0.00220  2.06636E-05 0.00220  2.32319E-05 0.02509 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  2.54276E-05 0.00190  2.54063E-05 0.00191  2.85379E-05 0.02501 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  14]) = [  6.99654E-03 0.01663  1.80700E-04 0.10677  1.05695E-03 0.04453  1.14267E-03 0.04184  3.14381E-03 0.02484  1.14815E-03 0.04301  3.24256E-04 0.08000 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  14]) = [  8.04535E-01 0.04181  1.24906E-02 4.0E-06  3.15568E-02 0.00092  1.10447E-01 0.00101  3.22001E-01 0.00090  1.34434E+00 0.00054  9.03755E+00 0.00562 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  2.06785E-05 0.00517  2.06818E-05 0.00524  1.48589E-05 0.05534 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  2.54236E-05 0.00503  2.54276E-05 0.00510  1.82794E-05 0.05540 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  14]) = [  6.70533E-03 0.05287  3.19829E-04 0.26266  1.22569E-03 0.11919  9.13730E-04 0.12789  2.82448E-03 0.07283  1.11526E-03 0.13374  3.06337E-04 0.26395 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  14]) = [  6.70795E-01 0.10044  1.24907E-02 1.1E-05  3.14445E-02 0.00216  1.10679E-01 0.00249  3.21782E-01 0.00190  1.34176E+00 0.00126  9.27851E+00 0.01541 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  14]) = [  6.72357E-03 0.05079  3.24551E-04 0.25524  1.24546E-03 0.11649  8.89896E-04 0.12162  2.84186E-03 0.07089  1.12952E-03 0.12480  2.92288E-04 0.25582 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  14]) = [  6.64120E-01 0.09746  1.24907E-02 1.1E-05  3.14486E-02 0.00215  1.10695E-01 0.00250  3.21848E-01 0.00190  1.34176E+00 0.00125  9.27851E+00 0.01541 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -3.30825E+02 0.05392 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  2.07179E-05 0.00143 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  2.54724E-05 0.00085 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  6.88445E-03 0.00951 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -3.32498E+02 0.00954 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  3.25855E-07 0.00119 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  4.18802E-06 0.00106  4.18817E-06 0.00106  4.18026E-06 0.01286 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.01811E-05 0.00131  3.01798E-05 0.00132  3.04416E-05 0.01621 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.24452E-01 0.00093  5.23606E-01 0.00095  7.26846E-01 0.02273 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  9.85654E+00 0.03156 ];
ANA_MEAN_NCOL             (idx, [1:   4]) = [  2.68926E+01 0.00055  3.02142E+01 0.00073 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  2])  = '11' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  1.00000E-11  5.00000E-09  1.00000E-08  1.50000E-08  2.00000E-08  2.50000E-08  3.00000E-08  3.50000E-08  4.20000E-08  5.00000E-08  5.80000E-08  6.70000E-08  8.00000E-08  1.00000E-07  1.40000E-07  1.80000E-07  2.20000E-07  2.50000E-07  2.80000E-07  3.00000E-07  3.20000E-07  3.50000E-07  4.00000E-07  5.00000E-07  6.25000E-07  7.80000E-07  8.50000E-07  9.10000E-07  9.50000E-07  9.72000E-07  9.96000E-07  1.02000E-06  1.04500E-06  1.07100E-06  1.09700E-06  1.12300E-06  1.15000E-06  1.30000E-06  1.50000E-06  1.85500E-06  2.10000E-06  2.60000E-06  3.30000E-06  4.00000E-06  9.87700E-06  1.59680E-05  2.77000E-05  4.80520E-05  7.55014E-05  1.48728E-04  3.67262E-04  9.06898E-04  1.42510E-03  2.23945E-03  3.51910E-03  5.50000E-03  9.11800E-03  1.50300E-02  2.47800E-02  4.08500E-02  6.74300E-02  1.11000E-01  1.83000E-01  3.02500E-01  5.00000E-01  8.21000E-01  1.35300E+00  2.23100E+00  3.67900E+00  6.06550E+00  2.00000E+01 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Micro-group spectrum:

INF_MICRO_FLX             (idx, [1: 140]) = [  1.12328E+04 0.00745  4.69775E+04 0.00322  9.69302E+04 0.00241  1.00778E+05 0.00151  9.57839E+04 0.00165  1.14042E+05 0.00155  7.75732E+04 0.00120  7.17991E+04 0.00156  5.55107E+04 0.00163  4.52672E+04 0.00155  3.91487E+04 0.00182  3.50311E+04 0.00179  3.24174E+04 0.00119  3.07814E+04 0.00182  2.99685E+04 0.00146  2.57169E+04 0.00153  2.54218E+04 0.00111  2.49733E+04 0.00111  2.43694E+04 0.00170  4.70727E+04 0.00124  4.50638E+04 0.00114  3.18573E+04 0.00144  2.01916E+04 0.00189  2.28985E+04 0.00221  2.11099E+04 0.00235  1.89571E+04 0.00210  2.98831E+04 0.00131  6.76143E+03 0.00320  8.50789E+03 0.00228  7.71943E+03 0.00358  4.44917E+03 0.00356  7.80645E+03 0.00242  5.27852E+03 0.00367  4.47647E+03 0.00416  8.51886E+02 0.00707  8.45625E+02 0.00708  8.67617E+02 0.00814  8.85489E+02 0.00884  8.67986E+02 0.01013  8.74372E+02 0.00725  8.86377E+02 0.00777  8.23457E+02 0.00875  1.59219E+03 0.00579  2.53913E+03 0.00526  3.23844E+03 0.00411  8.50956E+03 0.00229  8.90511E+03 0.00277  9.32626E+03 0.00254  5.93978E+03 0.00357  4.18487E+03 0.00377  3.11830E+03 0.00475  3.53164E+03 0.00477  6.28179E+03 0.00438  7.95426E+03 0.00288  1.41064E+04 0.00291  1.98274E+04 0.00222  2.71791E+04 0.00205  1.63989E+04 0.00214  1.13739E+04 0.00258  7.98037E+03 0.00306  7.08770E+03 0.00286  6.87375E+03 0.00312  5.69110E+03 0.00254  3.80527E+03 0.00395  3.50038E+03 0.00425  3.09431E+03 0.00334  2.61653E+03 0.00295  2.06162E+03 0.00443  1.38590E+03 0.00491  5.13200E+02 0.00649 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];

% Flux spectra in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  3.21767E+01 0.00079  4.56315E+00 0.00109 ];
INF_FISS_FLX              (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  4.04496E-01 0.00028  1.09407E+00 0.00019 ];
INF_CAPT                  (idx, [1:   4]) = [  1.57910E-04 0.00122  5.07557E-03 0.00034 ];
INF_ABS                   (idx, [1:   4]) = [  1.57910E-04 0.00122  5.07557E-03 0.00034 ];
INF_FISS                  (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_NSF                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_NUBAR                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_KAPPA                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_INVV                  (idx, [1:   4]) = [  5.44229E-08 0.00088  2.33740E-06 0.00034 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  4.04341E-01 0.00028  1.08899E+00 0.00020 ];
INF_SCATT1                (idx, [1:   4]) = [  2.36514E-01 0.00040  3.31202E-01 0.00088 ];
INF_SCATT2                (idx, [1:   4]) = [  9.05349E-02 0.00064  8.44832E-02 0.00222 ];
INF_SCATT3                (idx, [1:   4]) = [  2.89628E-03 0.01569  2.54574E-02 0.00730 ];
INF_SCATT4                (idx, [1:   4]) = [ -1.37357E-02 0.00281 -5.48406E-03 0.03073 ];
INF_SCATT5                (idx, [1:   4]) = [ -1.19176E-03 0.03192  4.89076E-03 0.03265 ];
INF_SCATT6                (idx, [1:   4]) = [  4.66599E-03 0.00678 -1.20634E-02 0.00847 ];
INF_SCATT7                (idx, [1:   4]) = [  4.72335E-04 0.07854 -5.50418E-04 0.19839 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  4.04341E-01 0.00028  1.08899E+00 0.00020 ];
INF_SCATTP1               (idx, [1:   4]) = [  2.36514E-01 0.00040  3.31202E-01 0.00088 ];
INF_SCATTP2               (idx, [1:   4]) = [  9.05349E-02 0.00064  8.44832E-02 0.00222 ];
INF_SCATTP3               (idx, [1:   4]) = [  2.89628E-03 0.01569  2.54574E-02 0.00730 ];
INF_SCATTP4               (idx, [1:   4]) = [ -1.37357E-02 0.00281 -5.48406E-03 0.03073 ];
INF_SCATTP5               (idx, [1:   4]) = [ -1.19176E-03 0.03192  4.89076E-03 0.03265 ];
INF_SCATTP6               (idx, [1:   4]) = [  4.66599E-03 0.00678 -1.20634E-02 0.00847 ];
INF_SCATTP7               (idx, [1:   4]) = [  4.72335E-04 0.07854 -5.50418E-04 0.19839 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  1.05991E-01 0.00106  6.52842E-01 0.00056 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  3.14500E+00 0.00105  5.10592E-01 0.00056 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  1.57910E-04 0.00122  5.07557E-03 0.00034 ];
INF_REMXS                 (idx, [1:   4]) = [  1.63310E-02 0.00082  6.48329E-03 0.00666 ];

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

INF_S0                    (idx, [1:   8]) = [  3.88165E-01 0.00028  1.61756E-02 0.00079  1.40294E-03 0.01207  1.08758E+00 0.00020 ];
INF_S1                    (idx, [1:   8]) = [  2.31686E-01 0.00041  4.82726E-03 0.00198  8.85738E-04 0.01061  3.30316E-01 0.00088 ];
INF_S2                    (idx, [1:   8]) = [  9.19811E-02 0.00067 -1.44619E-03 0.00668  4.65439E-04 0.01483  8.40178E-02 0.00224 ];
INF_S3                    (idx, [1:   8]) = [  4.58048E-03 0.00994 -1.68419E-03 0.00439  1.61732E-04 0.03508  2.52957E-02 0.00740 ];
INF_S4                    (idx, [1:   8]) = [ -1.31945E-02 0.00289 -5.41227E-04 0.01268 -2.94737E-06 1.00000 -5.48111E-03 0.03081 ];
INF_S5                    (idx, [1:   8]) = [ -1.21576E-03 0.03051  2.39974E-05 0.28041 -6.32466E-05 0.08510  4.95401E-03 0.03178 ];
INF_S6                    (idx, [1:   8]) = [  4.80297E-03 0.00609 -1.36983E-04 0.03909 -7.48500E-05 0.05669 -1.19886E-02 0.00844 ];
INF_S7                    (idx, [1:   8]) = [  6.32381E-04 0.05549 -1.60046E-04 0.03057 -7.11646E-05 0.06568 -4.79254E-04 0.22308 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  3.88165E-01 0.00028  1.61756E-02 0.00079  1.40294E-03 0.01207  1.08758E+00 0.00020 ];
INF_SP1                   (idx, [1:   8]) = [  2.31686E-01 0.00041  4.82726E-03 0.00198  8.85738E-04 0.01061  3.30316E-01 0.00088 ];
INF_SP2                   (idx, [1:   8]) = [  9.19811E-02 0.00067 -1.44619E-03 0.00668  4.65439E-04 0.01483  8.40178E-02 0.00224 ];
INF_SP3                   (idx, [1:   8]) = [  4.58048E-03 0.00994 -1.68419E-03 0.00439  1.61732E-04 0.03508  2.52957E-02 0.00740 ];
INF_SP4                   (idx, [1:   8]) = [ -1.31945E-02 0.00289 -5.41227E-04 0.01268 -2.94737E-06 1.00000 -5.48111E-03 0.03081 ];
INF_SP5                   (idx, [1:   8]) = [ -1.21576E-03 0.03051  2.39974E-05 0.28041 -6.32466E-05 0.08510  4.95401E-03 0.03178 ];
INF_SP6                   (idx, [1:   8]) = [  4.80297E-03 0.00609 -1.36983E-04 0.03909 -7.48500E-05 0.05669 -1.19886E-02 0.00844 ];
INF_SP7                   (idx, [1:   8]) = [  6.32381E-04 0.05549 -1.60046E-04 0.03057 -7.11646E-05 0.06568 -4.79254E-04 0.22308 ];

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

CMM_TRANSPXS              (idx, [1:   4]) = [  2.20547E-01 0.00210 -3.31648E-02 0.00269 ];
CMM_TRANSPXS_X            (idx, [1:   4]) = [  2.21662E-01 0.00314 -3.33121E-02 0.00325 ];
CMM_TRANSPXS_Y            (idx, [1:   4]) = [  2.19740E-01 0.00309 -3.30347E-02 0.00352 ];
CMM_TRANSPXS_Z            (idx, [1:   4]) = [  2.20353E-01 0.00368 -3.31654E-02 0.00447 ];
CMM_DIFFCOEF              (idx, [1:   4]) = [  1.51155E+00 0.00211 -1.00526E+01 0.00272 ];
CMM_DIFFCOEF_X            (idx, [1:   4]) = [  1.50415E+00 0.00315 -1.00089E+01 0.00327 ];
CMM_DIFFCOEF_Y            (idx, [1:   4]) = [  1.51730E+00 0.00311 -1.00934E+01 0.00355 ];
CMM_DIFFCOEF_Z            (idx, [1:   4]) = [  1.51322E+00 0.00367 -1.00554E+01 0.00445 ];

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
INPUT_FILE_NAME           (idx, [1: 11])  = 'GroupConst3' ;
WORKING_DIRECTORY         (idx, [1: 50])  = '/home/huaiqian/Serpent2.1.29/src/GroupConstforpin3' ;
HOSTNAME                  (idx, [1:  8])  = 'huaiqian' ;
CPU_TYPE                  (idx, [1: 40])  = 'Intel(R) Core(TM) i5-3570K CPU @ 3.40GHz' ;
CPU_MHZ                   (idx, 1)        = 28.0 ;
START_DATE                (idx, [1: 24])  = 'Fri Nov  3 13:15:26 2017' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Fri Nov  3 13:16:58 2017' ;

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
ST_FRAC                   (idx, [1:   4]) = [  8.33167E-03 0.00281  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.91668E-01 2.4E-05  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  8.34448E-01 0.00010  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  8.34825E-01 0.00010  0.00000E+00 0.0E+00 ];
AVG_TRACKING_LOOPS        (idx, [1:   8]) = [  2.35623E+00 0.00039  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  2.68926E+01 0.00055  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  2.68926E+01 0.00055  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  5.32090E+00 0.00075  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  1.96719E-01 0.00314  0.00000E+00 0.0E+00 ];
LOST_PARTICLES            (idx, 1)        = 0 ;

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 500 ;
SOURCE_POPULATION         (idx, 1)        = 1000474 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  2.00095E+03 0.00155 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  2.00095E+03 0.00155 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  1.52548E+00 ;
RUNNING_TIME              (idx, 1)        =  1.52683E+00 ;
INIT_TIME                 (idx, [1:  2])  = [  1.29333E-02  1.29333E-02 ];
PROCESS_TIME              (idx, [1:  2])  = [  8.33335E-05  8.33335E-05 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  1.51382E+00  1.51382E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  1.52653E+00  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 0.99912 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  9.99233E-01 0.00012 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  9.84827E-01 ;

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

NORM_COEF                 (idx, [1:   4]) = [  4.99431E-04 0.00082  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  6.54826E-01 0.00231 ];
U235_FISS                 (idx, [1:   4]) = [  4.54910E-01 0.00123  9.14091E-01 0.00044 ];
U238_FISS                 (idx, [1:   4]) = [  4.27722E-02 0.00502  8.59090E-02 0.00471 ];
U235_CAPT                 (idx, [1:   4]) = [  1.05884E-01 0.00314  2.10431E-01 0.00290 ];
U238_CAPT                 (idx, [1:   4]) = [  3.66941E-01 0.00179  7.29067E-01 0.00090 ];

% Neutron balance (particles/weight):

BALA_SRC_NEUTRON_SRC        (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_FISS       (idx, [1:  2])  = [ 1000474 1.00000E+06 ];
BALA_SRC_NEUTRON_NXN        (idx, [1:  2])  = [ 0 2.09641E+03 ];
BALA_SRC_NEUTRON_VR         (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_TOT        (idx, [1:  2])  = [ 1000474 1.00210E+06 ];

BALA_LOSS_NEUTRON_CAPT       (idx, [1:  2])  = [ 502963 5.03803E+05 ];
BALA_LOSS_NEUTRON_FISS       (idx, [1:  2])  = [ 497511 4.98293E+05 ];
BALA_LOSS_NEUTRON_LEAK       (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_CUT        (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_TOT        (idx, [1:  2])  = [ 1000474 1.00210E+06 ];

BALA_NEUTRON_DIFF            (idx, [1:  2])  = [ 0 1.16415E-09 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.61344E-11 0.00052 ];
TOT_POWDENS               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_GENRATE               (idx, [1:   2]) = [  1.22694E+00 0.00052 ];
TOT_FISSRATE              (idx, [1:   2]) = [  4.96861E-01 0.00052 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  5.03139E-01 0.00051 ];
TOT_ABSRATE               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.98862E-01 0.00082 ];
TOT_FLUX                  (idx, [1:   2]) = [  5.66527E+01 0.00066 ];
TOT_PHOTON_PRODRATE       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  2.69110E+01 0.00052 ];
INI_FMASS                 (idx, 1)        =  0.00000E+00 ;
TOT_FMASS                 (idx, 1)        =  0.00000E+00 ;

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.46938E+00 3.4E-05 ];
FISSE                     (idx, [1:   2]) = [  2.02679E+02 3.8E-06 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.23026E+00 0.00110  1.22187E+00 0.00109  8.59132E-03 0.01642 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.22950E+00 0.00052 ];
COL_KEFF                  (idx, [1:   2]) = [  1.22882E+00 0.00108 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.22950E+00 0.00052 ];
ABS_KINF                  (idx, [1:   2]) = [  1.22950E+00 0.00052 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% ALF (Average lethargy of neutrons causing fission):
% Based on E0 = 2.000000E+01 MeV

ANA_ALF                   (idx, [1:   2]) = [  1.66756E+01 0.00048 ];
IMP_ALF                   (idx, [1:   2]) = [  1.66722E+01 0.00023 ];

% EALF (Energy corresponding to average lethargy of neutrons causing fission):

ANA_EALF                  (idx, [1:   2]) = [  1.16399E-06 0.00814 ];
IMP_EALF                  (idx, [1:   2]) = [  1.15347E-06 0.00390 ];

% AFGE (Average energy of neutrons causing fission):

ANA_AFGE                  (idx, [1:   2]) = [  2.90610E-01 0.00509 ];
IMP_AFGE                  (idx, [1:   2]) = [  2.90873E-01 0.00234 ];

% Forward-weighted delayed neutron parameters:

FWD_ANA_BETA_ZERO         (idx, [1:  14]) = [  5.97768E-03 0.01238  1.72509E-04 0.07238  8.76309E-04 0.03107  9.63366E-04 0.03074  2.71979E-03 0.01772  9.46617E-04 0.02882  2.99092E-04 0.05050 ];
FWD_ANA_LAMBDA            (idx, [1:  14]) = [  8.36652E-01 0.02659  4.17190E-03 0.06321  2.78063E-02 0.01654  9.72965E-02 0.01655  3.22008E-01 0.00062  1.22568E+00 0.01391  4.72775E+00 0.04284 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  14]) = [  6.92330E-03 0.01768  1.76769E-04 0.10670  9.87245E-04 0.04655  1.10433E-03 0.04441  3.20635E-03 0.02684  1.09282E-03 0.04528  3.55792E-04 0.07916 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  14]) = [  8.45328E-01 0.04079  1.24907E-02 4.0E-06  3.15793E-02 0.00072  1.10443E-01 0.00084  3.21860E-01 0.00081  1.34421E+00 0.00045  9.01802E+00 0.00395 ];

% Adjoint weighted time constants using Nauchi's method:

ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  2.06811E-05 0.00220  2.06636E-05 0.00220  2.32319E-05 0.02509 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  2.54276E-05 0.00190  2.54063E-05 0.00191  2.85379E-05 0.02501 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  14]) = [  6.99654E-03 0.01663  1.80700E-04 0.10677  1.05695E-03 0.04453  1.14267E-03 0.04184  3.14381E-03 0.02484  1.14815E-03 0.04301  3.24256E-04 0.08000 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  14]) = [  8.04535E-01 0.04181  1.24906E-02 4.0E-06  3.15568E-02 0.00092  1.10447E-01 0.00101  3.22001E-01 0.00090  1.34434E+00 0.00054  9.03755E+00 0.00562 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  2.06785E-05 0.00517  2.06818E-05 0.00524  1.48589E-05 0.05534 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  2.54236E-05 0.00503  2.54276E-05 0.00510  1.82794E-05 0.05540 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  14]) = [  6.70533E-03 0.05287  3.19829E-04 0.26266  1.22569E-03 0.11919  9.13730E-04 0.12789  2.82448E-03 0.07283  1.11526E-03 0.13374  3.06337E-04 0.26395 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  14]) = [  6.70795E-01 0.10044  1.24907E-02 1.1E-05  3.14445E-02 0.00216  1.10679E-01 0.00249  3.21782E-01 0.00190  1.34176E+00 0.00126  9.27851E+00 0.01541 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  14]) = [  6.72357E-03 0.05079  3.24551E-04 0.25524  1.24546E-03 0.11649  8.89896E-04 0.12162  2.84186E-03 0.07089  1.12952E-03 0.12480  2.92288E-04 0.25582 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  14]) = [  6.64120E-01 0.09746  1.24907E-02 1.1E-05  3.14486E-02 0.00215  1.10695E-01 0.00250  3.21848E-01 0.00190  1.34176E+00 0.00125  9.27851E+00 0.01541 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -3.30825E+02 0.05392 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  2.07179E-05 0.00143 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  2.54724E-05 0.00085 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  6.88445E-03 0.00951 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -3.32498E+02 0.00954 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  3.25855E-07 0.00119 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  4.18802E-06 0.00106  4.18817E-06 0.00106  4.18026E-06 0.01286 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.01811E-05 0.00131  3.01798E-05 0.00132  3.04416E-05 0.01621 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.24452E-01 0.00093  5.23606E-01 0.00095  7.26846E-01 0.02273 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  9.85654E+00 0.03156 ];
ANA_MEAN_NCOL             (idx, [1:   4]) = [  2.68926E+01 0.00055  3.02142E+01 0.00073 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  2])  = '12' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  1.00000E-11  5.00000E-09  1.00000E-08  1.50000E-08  2.00000E-08  2.50000E-08  3.00000E-08  3.50000E-08  4.20000E-08  5.00000E-08  5.80000E-08  6.70000E-08  8.00000E-08  1.00000E-07  1.40000E-07  1.80000E-07  2.20000E-07  2.50000E-07  2.80000E-07  3.00000E-07  3.20000E-07  3.50000E-07  4.00000E-07  5.00000E-07  6.25000E-07  7.80000E-07  8.50000E-07  9.10000E-07  9.50000E-07  9.72000E-07  9.96000E-07  1.02000E-06  1.04500E-06  1.07100E-06  1.09700E-06  1.12300E-06  1.15000E-06  1.30000E-06  1.50000E-06  1.85500E-06  2.10000E-06  2.60000E-06  3.30000E-06  4.00000E-06  9.87700E-06  1.59680E-05  2.77000E-05  4.80520E-05  7.55014E-05  1.48728E-04  3.67262E-04  9.06898E-04  1.42510E-03  2.23945E-03  3.51910E-03  5.50000E-03  9.11800E-03  1.50300E-02  2.47800E-02  4.08500E-02  6.74300E-02  1.11000E-01  1.83000E-01  3.02500E-01  5.00000E-01  8.21000E-01  1.35300E+00  2.23100E+00  3.67900E+00  6.06550E+00  2.00000E+01 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Micro-group spectrum:

INF_MICRO_FLX             (idx, [1: 140]) = [  6.24779E+03 0.00758  2.61987E+04 0.00476  5.45411E+04 0.00299  5.70372E+04 0.00262  5.43663E+04 0.00220  6.49140E+04 0.00196  4.36751E+04 0.00211  4.04914E+04 0.00203  3.09648E+04 0.00290  2.48589E+04 0.00331  2.13721E+04 0.00259  1.89922E+04 0.00247  1.76198E+04 0.00300  1.67542E+04 0.00275  1.61396E+04 0.00311  1.37964E+04 0.00254  1.36021E+04 0.00276  1.33639E+04 0.00428  1.30299E+04 0.00345  2.49745E+04 0.00310  2.36671E+04 0.00238  1.66494E+04 0.00264  1.05342E+04 0.00330  1.15587E+04 0.00279  1.05746E+04 0.00400  1.00643E+04 0.00424  1.47568E+04 0.00307  3.61552E+03 0.00844  4.54688E+03 0.00545  4.14404E+03 0.00600  2.40757E+03 0.00697  4.19232E+03 0.00484  2.82356E+03 0.00760  2.34619E+03 0.00842  4.42844E+02 0.01814  4.44683E+02 0.01533  4.52968E+02 0.01470  4.69622E+02 0.01232  4.58855E+02 0.01495  4.65749E+02 0.01532  4.67459E+02 0.01295  4.60119E+02 0.01044  8.38179E+02 0.01077  1.34488E+03 0.00991  1.74385E+03 0.00782  4.53594E+03 0.00543  4.70998E+03 0.00542  4.88361E+03 0.00502  3.08108E+03 0.00543  2.14623E+03 0.00710  1.62559E+03 0.00822  1.81661E+03 0.00732  3.22971E+03 0.00581  4.07982E+03 0.00436  7.24286E+03 0.00345  1.01171E+04 0.00311  1.36271E+04 0.00293  8.14944E+03 0.00404  5.51480E+03 0.00313  3.86596E+03 0.00411  3.40896E+03 0.00525  3.24221E+03 0.00353  2.65615E+03 0.00543  1.74596E+03 0.00672  1.59306E+03 0.00604  1.36629E+03 0.00582  1.10723E+03 0.00589  8.34515E+02 0.00721  5.17389E+02 0.00942  1.56399E+02 0.00910 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.26450E+00 0.00095 ];

% Flux spectra in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  1.76535E+01 0.00088  2.26533E+00 0.00079 ];
INF_FISS_FLX              (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  4.24477E-01 0.00023  6.24309E-01 0.00019 ];
INF_CAPT                  (idx, [1:   4]) = [  1.93026E-02 0.00135  5.92738E-02 0.00044 ];
INF_ABS                   (idx, [1:   4]) = [  2.67525E-02 0.00102  2.20635E-01 0.00050 ];
INF_FISS                  (idx, [1:   4]) = [  7.44983E-03 0.00065  1.61361E-01 0.00052 ];
INF_NSF                   (idx, [1:   4]) = [  1.90728E-02 0.00069  3.93189E-01 0.00052 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.56016E+00 9.8E-05  2.43670E+00 0.0E+00 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.03816E+02 1.1E-05  2.02270E+02 0.0E+00 ];
INF_INVV                  (idx, [1:   4]) = [  5.21321E-08 0.00146  2.26297E-06 0.00046 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  3.97703E-01 0.00021  4.03536E-01 0.00055 ];
INF_SCATT1                (idx, [1:   4]) = [  4.38009E-02 0.00204  8.07880E-03 0.02712 ];
INF_SCATT2                (idx, [1:   4]) = [  2.27751E-02 0.00367  3.92493E-04 0.46351 ];
INF_SCATT3                (idx, [1:   4]) = [  1.21080E-02 0.00501 -2.69891E-04 0.68524 ];
INF_SCATT4                (idx, [1:   4]) = [  7.65314E-03 0.00644 -8.22024E-06 1.00000 ];
INF_SCATT5                (idx, [1:   4]) = [  3.96798E-03 0.01125  7.75632E-06 1.00000 ];
INF_SCATT6                (idx, [1:   4]) = [  1.95573E-03 0.02596  7.46708E-06 1.00000 ];
INF_SCATT7                (idx, [1:   4]) = [  7.69633E-04 0.05383  5.22305E-05 1.00000 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  3.97822E-01 0.00021  4.03536E-01 0.00055 ];
INF_SCATTP1               (idx, [1:   4]) = [  4.38023E-02 0.00204  8.07880E-03 0.02712 ];
INF_SCATTP2               (idx, [1:   4]) = [  2.27748E-02 0.00366  3.92493E-04 0.46351 ];
INF_SCATTP3               (idx, [1:   4]) = [  1.21077E-02 0.00501 -2.69891E-04 0.68524 ];
INF_SCATTP4               (idx, [1:   4]) = [  7.65190E-03 0.00647 -8.22024E-06 1.00000 ];
INF_SCATTP5               (idx, [1:   4]) = [  3.96793E-03 0.01123  7.75632E-06 1.00000 ];
INF_SCATTP6               (idx, [1:   4]) = [  1.95576E-03 0.02589  7.46708E-06 1.00000 ];
INF_SCATTP7               (idx, [1:   4]) = [  7.69346E-04 0.05393  5.22305E-05 1.00000 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  3.10508E-01 0.00066  5.93307E-01 0.00045 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.07352E+00 0.00066  5.61826E-01 0.00045 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  2.66338E-02 0.00103  2.20635E-01 0.00050 ];
INF_REMXS                 (idx, [1:   4]) = [  2.75545E-02 0.00116  2.22785E-01 0.00095 ];

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

INF_S0                    (idx, [1:   8]) = [  3.96923E-01 0.00022  7.80682E-04 0.00821  2.01105E-03 0.01740  4.01525E-01 0.00056 ];
INF_S1                    (idx, [1:   8]) = [  4.39865E-02 0.00206 -1.85656E-04 0.01792 -1.74569E-04 0.10613  8.25337E-03 0.02686 ];
INF_S2                    (idx, [1:   8]) = [  2.27941E-02 0.00359 -1.89191E-05 0.19291 -6.79434E-05 0.18167  4.60436E-04 0.39880 ];
INF_S3                    (idx, [1:   8]) = [  1.21096E-02 0.00495 -1.57459E-06 1.00000 -5.11481E-05 0.27037 -2.18743E-04 0.84647 ];
INF_S4                    (idx, [1:   8]) = [  7.65308E-03 0.00647  5.43299E-08 1.00000 -1.83600E-05 0.56556  1.01398E-05 1.00000 ];
INF_S5                    (idx, [1:   8]) = [  3.97068E-03 0.01109 -2.69665E-06 0.65101 -1.46469E-05 0.55701  2.24032E-05 1.00000 ];
INF_S6                    (idx, [1:   8]) = [  1.95830E-03 0.02586 -2.56366E-06 0.66919  3.11275E-06 1.00000  4.35434E-06 1.00000 ];
INF_S7                    (idx, [1:   8]) = [  7.69356E-04 0.05433  2.77720E-07 1.00000  8.55377E-07 1.00000  5.13751E-05 1.00000 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  3.97041E-01 0.00022  7.80682E-04 0.00821  2.01105E-03 0.01740  4.01525E-01 0.00056 ];
INF_SP1                   (idx, [1:   8]) = [  4.39880E-02 0.00205 -1.85656E-04 0.01792 -1.74569E-04 0.10613  8.25337E-03 0.02686 ];
INF_SP2                   (idx, [1:   8]) = [  2.27938E-02 0.00358 -1.89191E-05 0.19291 -6.79434E-05 0.18167  4.60436E-04 0.39880 ];
INF_SP3                   (idx, [1:   8]) = [  1.21093E-02 0.00495 -1.57459E-06 1.00000 -5.11481E-05 0.27037 -2.18743E-04 0.84647 ];
INF_SP4                   (idx, [1:   8]) = [  7.65185E-03 0.00650  5.43299E-08 1.00000 -1.83600E-05 0.56556  1.01398E-05 1.00000 ];
INF_SP5                   (idx, [1:   8]) = [  3.97063E-03 0.01107 -2.69665E-06 0.65101 -1.46469E-05 0.55701  2.24032E-05 1.00000 ];
INF_SP6                   (idx, [1:   8]) = [  1.95832E-03 0.02579 -2.56366E-06 0.66919  3.11275E-06 1.00000  4.35434E-06 1.00000 ];
INF_SP7                   (idx, [1:   8]) = [  7.69069E-04 0.05444  2.77720E-07 1.00000  8.55377E-07 1.00000  5.13751E-05 1.00000 ];

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

CMM_TRANSPXS              (idx, [1:   4]) = [  1.39040E-01 0.00205  1.61034E-02 0.00158 ];
CMM_TRANSPXS_X            (idx, [1:   4]) = [  1.39552E-01 0.00237  1.61615E-02 0.00212 ];
CMM_TRANSPXS_Y            (idx, [1:   4]) = [  1.38641E-01 0.00260  1.60557E-02 0.00219 ];
CMM_TRANSPXS_Z            (idx, [1:   4]) = [  1.38961E-01 0.00308  1.60974E-02 0.00291 ];
CMM_DIFFCOEF              (idx, [1:   4]) = [  2.39762E+00 0.00203  2.07007E+01 0.00157 ];
CMM_DIFFCOEF_X            (idx, [1:   4]) = [  2.38891E+00 0.00234  2.06274E+01 0.00211 ];
CMM_DIFFCOEF_Y            (idx, [1:   4]) = [  2.40468E+00 0.00258  2.07634E+01 0.00218 ];
CMM_DIFFCOEF_Z            (idx, [1:   4]) = [  2.39929E+00 0.00305  2.07114E+01 0.00288 ];

% Delayed neutron parameters (Meulekamp method):

BETA_EFF                  (idx, [1:  14]) = [  6.92330E-03 0.01768  1.76769E-04 0.10670  9.87245E-04 0.04655  1.10433E-03 0.04441  3.20635E-03 0.02684  1.09282E-03 0.04528  3.55792E-04 0.07916 ];
LAMBDA                    (idx, [1:  14]) = [  8.45328E-01 0.04079  1.24907E-02 4.0E-06  3.15793E-02 0.00072  1.10443E-01 0.00084  3.21860E-01 0.00081  1.34421E+00 0.00045  9.01802E+00 0.00395 ];

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