
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
START_DATE                (idx, [1: 24])  = 'Mon Dec 13 14:04:05 2021' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Mon Dec 13 14:05:20 2021' ;

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
OMP_HISTORY_PROFILE       (idx, [1:  18]) = [  1.04805E+00  1.07611E+00  1.00839E+00  9.83748E-01  9.56133E-01  9.75655E-01  1.02900E+00  9.83568E-01  9.72091E-01  9.94914E-01  1.06438E+00  1.03602E+00  1.02083E+00  9.82015E-01  9.62297E-01  9.64063E-01  9.76799E-01  9.65943E-01  ];
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
ST_FRAC                   (idx, [1:   4]) = [  2.14287E-03 0.00273  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.97857E-01 5.9E-06  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  8.23371E-01 8.2E-05  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  8.29723E-01 0.00010  0.00000E+00 0.0E+00 ];
AVG_TRACKING_LOOPS        (idx, [1:   8]) = [  4.89660E+00 0.00092  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  2.92108E+01 0.00062  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  2.92108E+01 0.00062  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  5.99476E+00 0.00080  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  4.58424E+01 0.00055  0.00000E+00 0.0E+00 ];
LOST_PARTICLES            (idx, 1)        = 0 ;

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 500 ;
SIMULATED_HISTORIES       (idx, 1)        = 1000630 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  2.00126E+03 0.00154 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  2.00126E+03 0.00154 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.22284E+01 ;
RUNNING_TIME              (idx, 1)        =  1.25050E+00 ;
INIT_TIME                 (idx, [1:  2])  = [  1.15500E-02  1.15500E-02 ];
PROCESS_TIME              (idx, [1:  2])  = [  1.16666E-04  1.16666E-04 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  1.23877E+00  1.23877E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  1.25042E+00  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 17.77565 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  1.79365E+01 0.00066 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  9.80474E-01 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 64027.77 ;
ALLOC_MEMSIZE             (idx, 1)        = 390.16;
MEMSIZE                   (idx, 1)        = 203.25;
XS_MEMSIZE                (idx, 1)        = 74.10;
MAT_MEMSIZE               (idx, 1)        = 6.90;
RES_MEMSIZE               (idx, 1)        = 1.61;
IFC_MEMSIZE               (idx, 1)        = 0.00;
MISC_MEMSIZE              (idx, 1)        = 120.64;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 186.91;

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

NORM_COEF                 (idx, [1:   4]) = [  4.99951E-04 0.00086  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  7.89040E-01 0.00217 ];
U235_FISS                 (idx, [1:   4]) = [  4.21574E-01 0.00128  9.09115E-01 0.00045 ];
U238_FISS                 (idx, [1:   4]) = [  4.21572E-02 0.00476  9.08849E-02 0.00447 ];
U235_CAPT                 (idx, [1:   4]) = [  9.29088E-02 0.00317  1.72672E-01 0.00296 ];
U238_CAPT                 (idx, [1:   4]) = [  4.05647E-01 0.00167  7.53725E-01 0.00075 ];

% Neutron balance (particles/weight):

BALA_SRC_NEUTRON_SRC     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_FISS    (idx, [1:  2])  = [ 1000630 1.00000E+06 ];
BALA_SRC_NEUTRON_NXN     (idx, [1:  2])  = [ 0 1.99721E+03 ];
BALA_SRC_NEUTRON_VR      (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_TOT     (idx, [1:  2])  = [ 1000630 1.00200E+06 ];

BALA_LOSS_NEUTRON_CAPT    (idx, [1:  2])  = [ 537391 5.38170E+05 ];
BALA_LOSS_NEUTRON_FISS    (idx, [1:  2])  = [ 463239 4.63827E+05 ];
BALA_LOSS_NEUTRON_LEAK    (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_CUT     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_ERR     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_TOT     (idx, [1:  2])  = [ 1000630 1.00200E+06 ];

BALA_NEUTRON_DIFF         (idx, [1:  2])  = [ 0 2.67755E-09 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.50319E-11 0.00056 ];
TOT_POWDENS               (idx, [1:   2]) = [  2.77096E-15 0.00056 ];
TOT_GENRATE               (idx, [1:   2]) = [  1.14467E+00 0.00055 ];
TOT_FISSRATE              (idx, [1:   2]) = [  4.63062E-01 0.00056 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  5.36938E-01 0.00048 ];
TOT_ABSRATE               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.99903E-01 0.00086 ];
TOT_FLUX                  (idx, [1:   2]) = [  5.92144E+01 0.00065 ];
TOT_PHOTON_PRODRATE       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  2.92585E+01 0.00051 ];
INI_FMASS                 (idx, 1)        =  5.42481E-03 ;
TOT_FMASS                 (idx, 1)        =  5.42481E-03 ;

% Six-factor formula:

SIX_FF_ETA                (idx, [1:   2]) = [  1.67921E+00 0.00096 ];
SIX_FF_F                  (idx, [1:   2]) = [  9.42335E-01 0.00034 ];
SIX_FF_P                  (idx, [1:   2]) = [  5.50371E-01 0.00095 ];
SIX_FF_EPSILON            (idx, [1:   2]) = [  1.31690E+00 0.00080 ];
SIX_FF_LF                 (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
SIX_FF_LT                 (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
SIX_FF_KINF               (idx, [1:   2]) = [  1.14649E+00 0.00110 ];
SIX_FF_KEFF               (idx, [1:   2]) = [  1.14649E+00 0.00110 ];

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.47198E+00 3.8E-05 ];
FISSE                     (idx, [1:   2]) = [  2.02612E+02 3.3E-06 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.14626E+00 0.00113  1.13826E+00 0.00110  8.22980E-03 0.01651 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.14693E+00 0.00055 ];
COL_KEFF                  (idx, [1:   2]) = [  1.14531E+00 0.00117 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.14693E+00 0.00055 ];
ABS_KINF                  (idx, [1:   2]) = [  1.14693E+00 0.00055 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% ALF (Average lethargy of neutrons causing fission):
% Based on E0 = 2.000000E+01 MeV

ANA_ALF                   (idx, [1:   2]) = [  1.69358E+01 0.00046 ];
IMP_ALF                   (idx, [1:   2]) = [  1.69337E+01 0.00024 ];

% EALF (Energy corresponding to average lethargy of neutrons causing fission):

ANA_EALF                  (idx, [1:   2]) = [  8.96704E-07 0.00801 ];
IMP_EALF                  (idx, [1:   2]) = [  8.88333E-07 0.00406 ];

% AFGE (Average energy of neutrons causing fission):

ANA_AFGE                  (idx, [1:   2]) = [  2.98114E-01 0.00488 ];
IMP_AFGE                  (idx, [1:   2]) = [  2.99306E-01 0.00241 ];

% Forward-weighted delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
FWD_ANA_BETA_ZERO         (idx, [1:  18]) = [  6.73833E-03 0.01135  1.66680E-04 0.06992  9.26366E-04 0.02906  5.58073E-04 0.04017  1.26687E-03 0.02472  2.17051E-03 0.01927  7.72027E-04 0.03404  6.32005E-04 0.03769  2.45796E-04 0.06016 ];
FWD_ANA_LAMBDA            (idx, [1:  18]) = [  4.83354E-01 0.01673  4.06414E-03 0.06437  2.50664E-02 0.01606  2.97671E-02 0.02931  1.26390E-01 0.01027  2.89543E-01 0.00450  5.53185E-01 0.02026  1.24243E+00 0.02516  1.53559E+00 0.05133 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  18]) = [  7.31060E-03 0.01672  1.88626E-04 0.10262  1.07096E-03 0.04599  6.37110E-04 0.06510  1.33890E-03 0.03975  2.29288E-03 0.02800  8.15884E-04 0.05069  6.93635E-04 0.05554  2.72608E-04 0.08939 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  18]) = [  4.80358E-01 0.02565  1.24667E-02 0.0E+00  2.82917E-02 0.0E+00  4.25244E-02 6.0E-09  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 4.9E-09  3.55460E+00 0.0E+00 ];

% Adjoint weighted time constants using Nauchi's method:

IFP_CHAIN_LENGTH          (idx, 1)        = 15 ;
ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  2.95113E-05 0.00235  2.94826E-05 0.00236  3.39910E-05 0.02575 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  3.38070E-05 0.00209  3.37740E-05 0.00210  3.89205E-05 0.02562 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  18]) = [  7.16545E-03 0.01657  1.88577E-04 0.10342  9.96941E-04 0.04516  5.93535E-04 0.05786  1.32834E-03 0.03928  2.29623E-03 0.03000  7.59210E-04 0.05569  7.19148E-04 0.05398  2.83478E-04 0.08769 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  18]) = [  5.02536E-01 0.02977  1.24667E-02 0.0E+00  2.82917E-02 4.2E-09  4.25244E-02 8.2E-09  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 5.5E-09  3.55460E+00 4.9E-09 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  2.94938E-05 0.00517  2.94606E-05 0.00519  2.25743E-05 0.05877 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  3.37846E-05 0.00502  3.37466E-05 0.00505  2.58408E-05 0.05873 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  18]) = [  6.65114E-03 0.05418  1.41574E-04 0.30459  1.32191E-03 0.13315  4.54710E-04 0.20864  1.15481E-03 0.13007  2.01702E-03 0.09437  7.67416E-04 0.16798  4.38605E-04 0.18829  3.55097E-04 0.23477 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  18]) = [  5.33724E-01 0.07776  1.24667E-02 5.5E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 4.0E-09  2.92467E-01 5.1E-09  6.66488E-01 5.0E-09  1.63478E+00 0.0E+00  3.55460E+00 4.7E-09 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  18]) = [  6.71670E-03 0.05175  1.33370E-04 0.30610  1.29052E-03 0.12925  4.65768E-04 0.19230  1.18820E-03 0.12662  2.03831E-03 0.09014  7.83194E-04 0.16144  4.65490E-04 0.18141  3.51841E-04 0.21942 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  18]) = [  5.32029E-01 0.07681  1.24667E-02 0.0E+00  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 4.0E-09  2.92467E-01 5.2E-09  6.66488E-01 5.0E-09  1.63478E+00 0.0E+00  3.55460E+00 5.4E-09 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -2.26450E+02 0.05368 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  2.96037E-05 0.00152 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  3.39117E-05 0.00101 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  6.98828E-03 0.00992 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -2.36294E+02 0.00999 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  4.15274E-07 0.00119 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  4.27184E-06 0.00097  4.27136E-06 0.00097  4.35689E-06 0.01232 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.96548E-05 0.00128  3.96577E-05 0.00129  3.96194E-05 0.01538 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.50874E-01 0.00095  5.50090E-01 0.00095  7.16810E-01 0.02027 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.12952E+01 0.02487 ];
ANA_MEAN_NCOL             (idx, [1:   4]) = [  2.92108E+01 0.00062  3.33203E+01 0.00080 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  1])  = '0' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  2.00000E+01  6.06550E+00  3.67900E+00  2.23100E+00  1.35300E+00  8.21000E-01  5.00000E-01  3.02500E-01  1.83000E-01  1.11000E-01  6.74300E-02  4.08500E-02  2.47800E-02  1.50300E-02  9.11800E-03  5.50000E-03  3.51910E-03  2.23945E-03  1.42510E-03  9.06898E-04  3.67262E-04  1.48728E-04  7.55014E-05  4.80520E-05  2.77000E-05  1.59680E-05  9.87700E-06  4.00000E-06  3.30000E-06  2.60000E-06  2.10000E-06  1.85500E-06  1.50000E-06  1.30000E-06  1.15000E-06  1.12300E-06  1.09700E-06  1.07100E-06  1.04500E-06  1.02000E-06  9.96000E-07  9.72000E-07  9.50000E-07  9.10000E-07  8.50000E-07  7.80000E-07  6.25000E-07  5.00000E-07  4.00000E-07  3.50000E-07  3.20000E-07  3.00000E-07  2.80000E-07  2.50000E-07  2.20000E-07  1.80000E-07  1.40000E-07  1.00000E-07  8.00000E-08  6.70000E-08  5.80000E-08  5.00000E-08  4.20000E-08  3.50000E-08  3.00000E-08  2.50000E-08  2.00000E-08  1.50000E-08  1.00000E-08  5.00000E-09  1.00000E-11 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Micro-group spectrum:

INF_MICRO_FLX             (idx, [1: 140]) = [  1.68247E+04 0.00736  7.04705E+04 0.00295  1.47993E+05 0.00182  1.56159E+05 0.00131  1.49577E+05 0.00177  1.80506E+05 0.00156  1.22237E+05 0.00182  1.13606E+05 0.00125  8.62262E+04 0.00192  7.03476E+04 0.00163  6.08533E+04 0.00143  5.41824E+04 0.00113  5.02958E+04 0.00218  4.76042E+04 0.00161  4.62158E+04 0.00147  3.96312E+04 0.00158  3.91260E+04 0.00163  3.86150E+04 0.00197  3.75033E+04 0.00146  7.28733E+04 0.00150  6.96771E+04 0.00151  4.90716E+04 0.00180  3.14724E+04 0.00157  3.55168E+04 0.00182  3.26181E+04 0.00196  3.02011E+04 0.00213  4.66195E+04 0.00159  1.08968E+04 0.00307  1.36856E+04 0.00356  1.24373E+04 0.00336  7.25413E+03 0.00394  1.25230E+04 0.00373  8.51550E+03 0.00404  7.19701E+03 0.00421  1.35710E+03 0.00716  1.37470E+03 0.00669  1.41341E+03 0.00673  1.42698E+03 0.00862  1.43807E+03 0.00824  1.40057E+03 0.00615  1.46284E+03 0.00845  1.37744E+03 0.00777  2.58139E+03 0.00743  4.14582E+03 0.00574  5.26368E+03 0.00375  1.38717E+04 0.00314  1.45697E+04 0.00340  1.56313E+04 0.00227  1.01523E+04 0.00296  7.35373E+03 0.00444  5.60400E+03 0.00440  6.41409E+03 0.00446  1.16412E+04 0.00377  1.51082E+04 0.00234  2.74949E+04 0.00264  3.97787E+04 0.00183  5.61149E+04 0.00172  3.46194E+04 0.00202  2.41472E+04 0.00206  1.70643E+04 0.00231  1.50844E+04 0.00252  1.47050E+04 0.00272  1.21508E+04 0.00261  8.15104E+03 0.00285  7.48264E+03 0.00327  6.56790E+03 0.00303  5.52049E+03 0.00307  4.29886E+03 0.00383  2.85060E+03 0.00400  9.87025E+02 0.00462 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.14532E+00 0.00115 ];

% Flux spectra in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  5.01359E+01 0.00063  9.08622E+00 0.00081 ];
INF_FISS_FLX              (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  4.14261E-01 0.00018  9.34951E-01 0.00018 ];
INF_CAPT                  (idx, [1:   4]) = [  6.86374E-03 0.00109  2.12378E-02 0.00048 ];
INF_ABS                   (idx, [1:   4]) = [  8.98324E-03 0.00090  6.05285E-02 0.00058 ];
INF_FISS                  (idx, [1:   4]) = [  2.11950E-03 0.00081  3.92907E-02 0.00064 ];
INF_NSF                   (idx, [1:   4]) = [  5.49388E-03 0.00082  9.57200E-02 0.00064 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.59207E+00 9.8E-05  2.43620E+00 0.0E+00 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.03760E+02 7.3E-06  2.02270E+02 0.0E+00 ];
INF_INVV                  (idx, [1:   4]) = [  5.57124E-08 0.00092  2.39954E-06 0.00026 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  4.05254E-01 0.00020  8.74385E-01 0.00022 ];
INF_SCATT1                (idx, [1:   4]) = [  1.69192E-01 0.00033  2.22118E-01 0.00081 ];
INF_SCATT2                (idx, [1:   4]) = [  6.69854E-02 0.00073  5.50183E-02 0.00288 ];
INF_SCATT3                (idx, [1:   4]) = [  6.08770E-03 0.00658  1.66482E-02 0.00611 ];
INF_SCATT4                (idx, [1:   4]) = [ -6.22684E-03 0.00554 -3.97408E-03 0.01860 ];
INF_SCATT5                (idx, [1:   4]) = [  6.29266E-04 0.03961  3.17841E-03 0.02994 ];
INF_SCATT6                (idx, [1:   4]) = [  3.74767E-03 0.00725 -8.48114E-03 0.01005 ];
INF_SCATT7                (idx, [1:   4]) = [  6.25589E-04 0.03883 -2.33949E-04 0.38925 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  4.05294E-01 0.00020  8.74385E-01 0.00022 ];
INF_SCATTP1               (idx, [1:   4]) = [  1.69193E-01 0.00033  2.22118E-01 0.00081 ];
INF_SCATTP2               (idx, [1:   4]) = [  6.69863E-02 0.00073  5.50183E-02 0.00288 ];
INF_SCATTP3               (idx, [1:   4]) = [  6.08820E-03 0.00658  1.66482E-02 0.00611 ];
INF_SCATTP4               (idx, [1:   4]) = [ -6.22679E-03 0.00555 -3.97408E-03 0.01860 ];
INF_SCATTP5               (idx, [1:   4]) = [  6.29043E-04 0.03958  3.17841E-03 0.02994 ];
INF_SCATTP6               (idx, [1:   4]) = [  3.74773E-03 0.00725 -8.48114E-03 0.01005 ];
INF_SCATTP7               (idx, [1:   4]) = [  6.25748E-04 0.03891 -2.33949E-04 0.38925 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  1.85578E-01 0.00056  6.37829E-01 0.00044 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.79620E+00 0.00056  5.22609E-01 0.00044 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  8.94341E-03 0.00087  6.05285E-02 0.00058 ];
INF_REMXS                 (idx, [1:   4]) = [  2.02159E-02 0.00055  6.18493E-02 0.00096 ];

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

INF_S0                    (idx, [1:   8]) = [  3.94045E-01 0.00019  1.12090E-02 0.00096  1.28333E-03 0.01166  8.73102E-01 0.00023 ];
INF_S1                    (idx, [1:   8]) = [  1.65994E-01 0.00032  3.19805E-03 0.00261  4.37734E-04 0.01640  2.21680E-01 0.00081 ];
INF_S2                    (idx, [1:   8]) = [  6.79518E-02 0.00069 -9.66436E-04 0.00534  2.35003E-04 0.02666  5.47833E-02 0.00286 ];
INF_S3                    (idx, [1:   8]) = [  7.22834E-03 0.00543 -1.14064E-03 0.00438  8.41639E-05 0.05983  1.65641E-02 0.00614 ];
INF_S4                    (idx, [1:   8]) = [ -5.85146E-03 0.00618 -3.75383E-04 0.01306 -3.41998E-06 1.00000 -3.97066E-03 0.01871 ];
INF_S5                    (idx, [1:   8]) = [  6.18991E-04 0.03854  1.02752E-05 0.36254 -3.81509E-05 0.08551  3.21656E-03 0.02972 ];
INF_S6                    (idx, [1:   8]) = [  3.83989E-03 0.00683 -9.22190E-05 0.03285 -4.54617E-05 0.07717 -8.43568E-03 0.01012 ];
INF_S7                    (idx, [1:   8]) = [  7.31100E-04 0.03227 -1.05512E-04 0.03680 -4.32373E-05 0.05023 -1.90712E-04 0.47431 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  3.94085E-01 0.00019  1.12090E-02 0.00096  1.28333E-03 0.01166  8.73102E-01 0.00023 ];
INF_SP1                   (idx, [1:   8]) = [  1.65995E-01 0.00032  3.19805E-03 0.00261  4.37734E-04 0.01640  2.21680E-01 0.00081 ];
INF_SP2                   (idx, [1:   8]) = [  6.79527E-02 0.00069 -9.66436E-04 0.00534  2.35003E-04 0.02666  5.47833E-02 0.00286 ];
INF_SP3                   (idx, [1:   8]) = [  7.22884E-03 0.00543 -1.14064E-03 0.00438  8.41639E-05 0.05983  1.65641E-02 0.00614 ];
INF_SP4                   (idx, [1:   8]) = [ -5.85141E-03 0.00619 -3.75383E-04 0.01306 -3.41998E-06 1.00000 -3.97066E-03 0.01871 ];
INF_SP5                   (idx, [1:   8]) = [  6.18768E-04 0.03853  1.02752E-05 0.36254 -3.81509E-05 0.08551  3.21656E-03 0.02972 ];
INF_SP6                   (idx, [1:   8]) = [  3.83995E-03 0.00684 -9.22190E-05 0.03285 -4.54617E-05 0.07717 -8.43568E-03 0.01012 ];
INF_SP7                   (idx, [1:   8]) = [  7.31260E-04 0.03235 -1.05512E-04 0.03680 -4.32373E-05 0.05023 -1.90712E-04 0.47431 ];

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

CMM_TRANSPXS              (idx, [1:   4]) = [  1.91565E-01 0.00131  5.90361E-01 0.00455 ];
CMM_TRANSPXS_X            (idx, [1:   4]) = [  1.92172E-01 0.00237  5.91141E-01 0.00683 ];
CMM_TRANSPXS_Y            (idx, [1:   4]) = [  1.91449E-01 0.00146  5.89045E-01 0.00861 ];
CMM_TRANSPXS_Z            (idx, [1:   4]) = [  1.91098E-01 0.00149  5.92887E-01 0.00911 ];
CMM_DIFFCOEF              (idx, [1:   4]) = [  1.74013E+00 0.00131  5.64909E-01 0.00458 ];
CMM_DIFFCOEF_X            (idx, [1:   4]) = [  1.73479E+00 0.00237  5.64513E-01 0.00684 ];
CMM_DIFFCOEF_Y            (idx, [1:   4]) = [  1.74120E+00 0.00146  5.66894E-01 0.00861 ];
CMM_DIFFCOEF_Z            (idx, [1:   4]) = [  1.74440E+00 0.00149  5.63319E-01 0.00893 ];

% Delayed neutron parameters (Meulekamp method):

BETA_EFF                  (idx, [1:  18]) = [  7.31060E-03 0.01672  1.88626E-04 0.10262  1.07096E-03 0.04599  6.37110E-04 0.06510  1.33890E-03 0.03975  2.29288E-03 0.02800  8.15884E-04 0.05069  6.93635E-04 0.05554  2.72608E-04 0.08939 ];
LAMBDA                    (idx, [1:  18]) = [  4.80358E-01 0.02565  1.24667E-02 0.0E+00  2.82917E-02 0.0E+00  4.25244E-02 6.0E-09  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 4.9E-09  3.55460E+00 0.0E+00 ];

