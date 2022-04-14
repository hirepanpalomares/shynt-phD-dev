
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
INPUT_FILE_NAME           (idx, [1:135])  = '/home/hirepan/Documents/chalmers/Project/codes/Shynt/repo/cases/single_assem_1x1cell/serpent_files/global_cell_type4/XS_generation.serp' ;
WORKING_DIRECTORY         (idx, [1: 84])  = '/home/hirepan/Documents/chalmers/Project/codes/Shynt/repo/cases/single_assem_1x1cell' ;
HOSTNAME                  (idx, [1:  4])  = 'thor' ;
CPU_TYPE                  (idx, [1: 40])  = 'Intel(R) Core(TM) i9-10900 CPU @ 2.80GHz' ;
CPU_MHZ                   (idx, 1)        = 236.0 ;
START_DATE                (idx, [1: 24])  = 'Thu Mar 10 12:01:22 2022' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Mar 10 12:01:31 2022' ;

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
OMP_HISTORY_PROFILE       (idx, [1:  18]) = [  9.71495E-01  1.03589E+00  1.00679E+00  1.00185E+00  1.02946E+00  9.88480E-01  9.76268E-01  1.00439E+00  1.00437E+00  9.81434E-01  1.00040E+00  9.67228E-01  1.06126E+00  9.86813E-01  9.76906E-01  1.00890E+00  1.00417E+00  9.93891E-01  ];
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
ST_FRAC                   (idx, [1:   4]) = [  8.63771E-03 0.00297  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.91362E-01 2.6E-05  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  8.36758E-01 0.00011  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  8.37144E-01 0.00011  0.00000E+00 0.0E+00 ];
AVG_TRACKING_LOOPS        (idx, [1:   8]) = [  2.32303E+00 0.00036  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  2.54950E+01 0.00053  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  2.54950E+01 0.00053  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  4.95967E+00 0.00073  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  1.92772E-01 0.00329  0.00000E+00 0.0E+00 ];
LOST_PARTICLES            (idx, 1)        = 0 ;

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 500 ;
SIMULATED_HISTORIES       (idx, 1)        = 1000425 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  2.00085E+03 0.00142 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  2.00085E+03 0.00142 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.31233E+00 ;
RUNNING_TIME              (idx, 1)        =  1.43500E-01 ;
INIT_TIME                 (idx, [1:  2])  = [  1.16500E-02  1.16500E-02 ];
PROCESS_TIME              (idx, [1:  2])  = [  1.16666E-04  1.16666E-04 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  1.31667E-01  1.31667E-01  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  1.43400E-01  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 16.11382 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  1.75380E+01 0.00452 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  7.62602E-01 ;

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

NORM_COEF                 (idx, [1:   4]) = [  4.98701E-04 0.00084  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  5.77644E-01 0.00210 ];
U235_FISS                 (idx, [1:   4]) = [  4.75060E-01 0.00120  9.20037E-01 0.00041 ];
U238_FISS                 (idx, [1:   4]) = [  4.13165E-02 0.00509  7.99631E-02 0.00468 ];
U235_CAPT                 (idx, [1:   4]) = [  1.16254E-01 0.00280  2.40720E-01 0.00247 ];
U238_CAPT                 (idx, [1:   4]) = [  3.41366E-01 0.00166  7.06815E-01 0.00090 ];

% Neutron balance (particles/weight):

BALA_SRC_NEUTRON_SRC     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_FISS    (idx, [1:  2])  = [ 1000425 1.00000E+06 ];
BALA_SRC_NEUTRON_NXN     (idx, [1:  2])  = [ 0 1.94096E+03 ];
BALA_SRC_NEUTRON_VR      (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_TOT     (idx, [1:  2])  = [ 1000425 1.00194E+06 ];

BALA_LOSS_NEUTRON_CAPT    (idx, [1:  2])  = [ 483465 4.84198E+05 ];
BALA_LOSS_NEUTRON_FISS    (idx, [1:  2])  = [ 516960 5.17743E+05 ];
BALA_LOSS_NEUTRON_LEAK    (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_CUT     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_ERR     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_TOT     (idx, [1:  2])  = [ 1000425 1.00194E+06 ];

BALA_NEUTRON_DIFF         (idx, [1:  2])  = [ 0 1.04774E-09 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.67472E-11 0.00054 ];
TOT_POWDENS               (idx, [1:   2]) = [  3.08714E-15 0.00054 ];
TOT_GENRATE               (idx, [1:   2]) = [  1.27388E+00 0.00053 ];
TOT_FISSRATE              (idx, [1:   2]) = [  5.16005E-01 0.00054 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  4.83995E-01 0.00058 ];
TOT_ABSRATE               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.97402E-01 0.00084 ];
TOT_FLUX                  (idx, [1:   2]) = [  5.46874E+01 0.00069 ];
TOT_PHOTON_PRODRATE       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  2.54719E+01 0.00056 ];
INI_FMASS                 (idx, 1)        =  5.42481E-03 ;
TOT_FMASS                 (idx, 1)        =  5.42481E-03 ;

% Six-factor formula:

SIX_FF_ETA                (idx, [1:   2]) = [  1.84328E+00 0.00084 ];
SIX_FF_F                  (idx, [1:   2]) = [  9.64160E-01 0.00026 ];
SIX_FF_P                  (idx, [1:   2]) = [  4.99888E-01 0.00097 ];
SIX_FF_EPSILON            (idx, [1:   2]) = [  1.43920E+00 0.00092 ];
SIX_FF_LF                 (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
SIX_FF_LT                 (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
SIX_FF_KINF               (idx, [1:   2]) = [  1.27808E+00 0.00097 ];
SIX_FF_KEFF               (idx, [1:   2]) = [  1.27808E+00 0.00097 ];

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.46875E+00 3.3E-05 ];
FISSE                     (idx, [1:   2]) = [  2.02571E+02 2.8E-06 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.27782E+00 0.00099  1.26896E+00 0.00098  9.12644E-03 0.01749 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.27638E+00 0.00054 ];
COL_KEFF                  (idx, [1:   2]) = [  1.27772E+00 0.00111 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.27638E+00 0.00054 ];
ABS_KINF                  (idx, [1:   2]) = [  1.27638E+00 0.00054 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% ALF (Average lethargy of neutrons causing fission):
% Based on E0 = 2.000000E+01 MeV

ANA_ALF                   (idx, [1:   2]) = [  1.64579E+01 0.00046 ];
IMP_ALF                   (idx, [1:   2]) = [  1.64550E+01 0.00025 ];

% EALF (Energy corresponding to average lethargy of neutrons causing fission):

ANA_EALF                  (idx, [1:   2]) = [  1.44461E-06 0.00775 ];
IMP_EALF                  (idx, [1:   2]) = [  1.43401E-06 0.00410 ];

% AFGE (Average energy of neutrons causing fission):

ANA_AFGE                  (idx, [1:   2]) = [  2.74176E-01 0.00510 ];
IMP_AFGE                  (idx, [1:   2]) = [  2.75567E-01 0.00231 ];

% Forward-weighted delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
FWD_ANA_BETA_ZERO         (idx, [1:  18]) = [  5.93398E-03 0.01232  1.68253E-04 0.06789  7.80619E-04 0.03243  5.31754E-04 0.04103  1.11146E-03 0.02773  1.91368E-03 0.02105  6.67422E-04 0.03448  5.48591E-04 0.03711  2.12197E-04 0.06261 ];
FWD_ANA_LAMBDA            (idx, [1:  18]) = [  4.84618E-01 0.02012  4.38828E-03 0.06074  2.39914E-02 0.01895  3.07877E-02 0.02764  1.27188E-01 0.00960  2.89543E-01 0.00450  5.41188E-01 0.02154  1.22609E+00 0.02585  1.45028E+00 0.05392 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  18]) = [  7.22398E-03 0.01727  2.11360E-04 0.10004  9.76808E-04 0.04821  6.57168E-04 0.05930  1.38335E-03 0.03979  2.31439E-03 0.03082  7.79064E-04 0.05078  6.58284E-04 0.05770  2.43554E-04 0.10067 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  18]) = [  4.75482E-01 0.03076  1.24667E-02 0.0E+00  2.82917E-02 0.0E+00  4.25244E-02 5.8E-09  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 4.9E-09  3.55460E+00 0.0E+00 ];

% Adjoint weighted time constants using Nauchi's method:

IFP_CHAIN_LENGTH          (idx, 1)        = 15 ;
ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  1.60288E-05 0.00224  1.60168E-05 0.00225  1.75073E-05 0.02331 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  2.04713E-05 0.00199  2.04559E-05 0.00199  2.23692E-05 0.02326 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  18]) = [  7.15524E-03 0.01754  2.05617E-04 0.09471  9.46736E-04 0.04805  6.57096E-04 0.05457  1.29106E-03 0.04019  2.27560E-03 0.03001  8.50618E-04 0.05001  6.59441E-04 0.05263  2.69070E-04 0.08846 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  18]) = [  5.00191E-01 0.03139  1.24667E-02 0.0E+00  2.82917E-02 4.3E-09  4.25244E-02 8.1E-09  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 5.5E-09  3.55460E+00 4.9E-09 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  1.59703E-05 0.00489  1.59572E-05 0.00490  1.29607E-05 0.05133 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  2.03987E-05 0.00482  2.03821E-05 0.00483  1.65458E-05 0.05124 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  18]) = [  6.56899E-03 0.04877  2.06107E-04 0.27151  6.73193E-04 0.16734  5.83900E-04 0.16270  1.36961E-03 0.10786  2.24696E-03 0.08833  6.77781E-04 0.14109  6.15014E-04 0.17351  1.96436E-04 0.28246 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  18]) = [  4.82244E-01 0.06804  1.24667E-02 4.7E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 4.0E-09  2.92467E-01 5.8E-09  6.66488E-01 5.1E-09  1.63478E+00 0.0E+00  3.55460E+00 4.7E-09 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  18]) = [  6.61312E-03 0.04664  2.05346E-04 0.25390  6.42944E-04 0.15190  5.55052E-04 0.15528  1.41583E-03 0.10407  2.23547E-03 0.08667  7.18539E-04 0.13505  6.35583E-04 0.16927  2.04350E-04 0.25779 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  18]) = [  4.85784E-01 0.06717  1.24667E-02 4.7E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 4.0E-09  2.92467E-01 5.8E-09  6.66488E-01 5.1E-09  1.63478E+00 0.0E+00  3.55460E+00 6.0E-09 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -4.17112E+02 0.04968 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  1.60307E-05 0.00133 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  2.04745E-05 0.00090 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  6.91522E-03 0.00925 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -4.31690E+02 0.00931 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  2.71066E-07 0.00129 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  4.13167E-06 0.00104  4.13142E-06 0.00104  4.15554E-06 0.01252 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  2.46121E-05 0.00137  2.46125E-05 0.00138  2.44517E-05 0.01688 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.00486E-01 0.00097  4.99488E-01 0.00097  7.25060E-01 0.02136 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.18651E+01 0.02548 ];
ANA_MEAN_NCOL             (idx, [1:   4]) = [  2.54950E+01 0.00053  2.83575E+01 0.00069 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  7])  = 'u4gcu_1' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  2.00000E+01  6.06550E+00  3.67900E+00  2.23100E+00  1.35300E+00  8.21000E-01  5.00000E-01  3.02500E-01  1.83000E-01  1.11000E-01  6.74300E-02  4.08500E-02  2.47800E-02  1.50300E-02  9.11800E-03  5.50000E-03  3.51910E-03  2.23945E-03  1.42510E-03  9.06898E-04  3.67262E-04  1.48728E-04  7.55014E-05  4.80520E-05  2.77000E-05  1.59680E-05  9.87700E-06  4.00000E-06  3.30000E-06  2.60000E-06  2.10000E-06  1.85500E-06  1.50000E-06  1.30000E-06  1.15000E-06  1.12300E-06  1.09700E-06  1.07100E-06  1.04500E-06  1.02000E-06  9.96000E-07  9.72000E-07  9.50000E-07  9.10000E-07  8.50000E-07  7.80000E-07  6.25000E-07  5.00000E-07  4.00000E-07  3.50000E-07  3.20000E-07  3.00000E-07  2.80000E-07  2.50000E-07  2.20000E-07  1.80000E-07  1.40000E-07  1.00000E-07  8.00000E-08  6.70000E-08  5.80000E-08  5.00000E-08  4.20000E-08  3.50000E-08  3.00000E-08  2.50000E-08  2.00000E-08  1.50000E-08  1.00000E-08  5.00000E-09  1.00000E-11 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Micro-group spectrum:

INF_MICRO_FLX             (idx, [1: 140]) = [  6.06082E+03 0.00687  2.53461E+04 0.00425  5.35370E+04 0.00302  5.64137E+04 0.00202  5.41629E+04 0.00197  6.51377E+04 0.00158  4.39053E+04 0.00197  4.06312E+04 0.00224  3.06703E+04 0.00272  2.48217E+04 0.00255  2.14126E+04 0.00285  1.89439E+04 0.00327  1.75319E+04 0.00418  1.65749E+04 0.00257  1.60848E+04 0.00397  1.38077E+04 0.00390  1.35571E+04 0.00349  1.32607E+04 0.00359  1.29008E+04 0.00383  2.46757E+04 0.00297  2.33811E+04 0.00280  1.62049E+04 0.00290  1.02459E+04 0.00394  1.11412E+04 0.00351  1.00726E+04 0.00465  9.67978E+03 0.00469  1.41848E+04 0.00260  3.42009E+03 0.00751  4.34796E+03 0.00690  4.02807E+03 0.00512  2.30657E+03 0.00871  4.00845E+03 0.00673  2.72435E+03 0.00584  2.28022E+03 0.00579  4.26034E+02 0.01087  4.18003E+02 0.01385  4.33292E+02 0.01334  4.42892E+02 0.01349  4.41138E+02 0.01592  4.26282E+02 0.01221  4.58826E+02 0.01734  4.27338E+02 0.01282  8.02154E+02 0.01275  1.28618E+03 0.00997  1.62508E+03 0.00925  4.30772E+03 0.00672  4.34179E+03 0.00588  4.49970E+03 0.00477  2.78292E+03 0.00575  1.88766E+03 0.00615  1.40319E+03 0.00654  1.56055E+03 0.00748  2.73124E+03 0.00574  3.36219E+03 0.00539  5.83187E+03 0.00409  7.97807E+03 0.00408  1.04755E+04 0.00262  6.12120E+03 0.00364  4.10051E+03 0.00337  2.85428E+03 0.00478  2.48258E+03 0.00419  2.34415E+03 0.00495  1.91648E+03 0.00495  1.24444E+03 0.00812  1.11869E+03 0.00562  9.56891E+02 0.00645  7.89255E+02 0.00707  5.86496E+02 0.00725  3.51634E+02 0.00795  1.03199E+02 0.00964 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.30774E+00 0.00109 ];

% Flux spectra in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  1.74285E+01 0.00081  1.79090E+00 0.00111 ];
INF_FISS_FLX              (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  4.28695E-01 0.00019  6.75633E-01 0.00025 ];
INF_CAPT                  (idx, [1:   4]) = [  1.97231E-02 0.00117  6.54637E-02 0.00055 ];
INF_ABS                   (idx, [1:   4]) = [  2.84990E-02 0.00089  2.68301E-01 0.00059 ];
INF_FISS                  (idx, [1:   4]) = [  8.77589E-03 0.00066  2.02837E-01 0.00061 ];
INF_NSF                   (idx, [1:   4]) = [  2.23433E-02 0.00067  4.94152E-01 0.00061 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.54598E+00 9.2E-05  2.43620E+00 0.0E+00 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.03285E+02 6.4E-06  2.02270E+02 0.0E+00 ];
INF_INVV                  (idx, [1:   4]) = [  5.06818E-08 0.00142  2.18498E-06 0.00051 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  4.00251E-01 0.00020  4.07205E-01 0.00080 ];
INF_SCATT1                (idx, [1:   4]) = [  4.35574E-02 0.00237  8.18217E-03 0.03501 ];
INF_SCATT2                (idx, [1:   4]) = [  2.30620E-02 0.00296  6.33169E-04 0.28421 ];
INF_SCATT3                (idx, [1:   4]) = [  1.19271E-02 0.00697  5.35882E-05 1.00000 ];
INF_SCATT4                (idx, [1:   4]) = [  7.60242E-03 0.00554 -8.84852E-05 1.00000 ];
INF_SCATT5                (idx, [1:   4]) = [  3.92752E-03 0.01220  7.51563E-05 1.00000 ];
INF_SCATT6                (idx, [1:   4]) = [  2.09414E-03 0.01960 -1.32479E-04 0.93879 ];
INF_SCATT7                (idx, [1:   4]) = [  8.70913E-04 0.03818 -4.43667E-05 1.00000 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  4.00362E-01 0.00020  4.07205E-01 0.00080 ];
INF_SCATTP1               (idx, [1:   4]) = [  4.35584E-02 0.00237  8.18217E-03 0.03501 ];
INF_SCATTP2               (idx, [1:   4]) = [  2.30625E-02 0.00296  6.33169E-04 0.28421 ];
INF_SCATTP3               (idx, [1:   4]) = [  1.19267E-02 0.00699  5.35882E-05 1.00000 ];
INF_SCATTP4               (idx, [1:   4]) = [  7.60177E-03 0.00555 -8.84852E-05 1.00000 ];
INF_SCATTP5               (idx, [1:   4]) = [  3.92742E-03 0.01221  7.51563E-05 1.00000 ];
INF_SCATTP6               (idx, [1:   4]) = [  2.09460E-03 0.01954 -1.32479E-04 0.93879 ];
INF_SCATTP7               (idx, [1:   4]) = [  8.71237E-04 0.03841 -4.43667E-05 1.00000 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  3.13911E-01 0.00067  6.37319E-01 0.00058 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.06188E+00 0.00067  5.23029E-01 0.00058 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  2.83879E-02 0.00091  2.68301E-01 0.00059 ];
INF_REMXS                 (idx, [1:   4]) = [  2.91874E-02 0.00118  2.70701E-01 0.00114 ];

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

INF_S0                    (idx, [1:   8]) = [  3.99507E-01 0.00021  7.43976E-04 0.00871  2.27338E-03 0.01834  4.04932E-01 0.00080 ];
INF_S1                    (idx, [1:   8]) = [  4.37264E-02 0.00237 -1.68919E-04 0.02598 -2.30602E-04 0.05945  8.41277E-03 0.03364 ];
INF_S2                    (idx, [1:   8]) = [  2.30800E-02 0.00291 -1.79527E-05 0.15332 -9.64206E-05 0.18220  7.29590E-04 0.24418 ];
INF_S3                    (idx, [1:   8]) = [  1.19313E-02 0.00695 -4.25895E-06 0.38863 -2.28191E-05 0.51492  7.64072E-05 1.00000 ];
INF_S4                    (idx, [1:   8]) = [  7.60606E-03 0.00546 -3.63315E-06 0.44707 -1.67728E-05 0.55958 -7.17124E-05 1.00000 ];
INF_S5                    (idx, [1:   8]) = [  3.93017E-03 0.01223 -2.64500E-06 0.63592 -1.29007E-06 1.00000  7.64463E-05 1.00000 ];
INF_S6                    (idx, [1:   8]) = [  2.09123E-03 0.01976  2.90912E-06 0.57280  3.04119E-06 1.00000 -1.35520E-04 0.93441 ];
INF_S7                    (idx, [1:   8]) = [  8.71829E-04 0.03831 -9.16688E-07 1.00000 -1.24550E-05 0.67993 -3.19117E-05 1.00000 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  3.99618E-01 0.00020  7.43976E-04 0.00871  2.27338E-03 0.01834  4.04932E-01 0.00080 ];
INF_SP1                   (idx, [1:   8]) = [  4.37273E-02 0.00237 -1.68919E-04 0.02598 -2.30602E-04 0.05945  8.41277E-03 0.03364 ];
INF_SP2                   (idx, [1:   8]) = [  2.30804E-02 0.00292 -1.79527E-05 0.15332 -9.64206E-05 0.18220  7.29590E-04 0.24418 ];
INF_SP3                   (idx, [1:   8]) = [  1.19309E-02 0.00696 -4.25895E-06 0.38863 -2.28191E-05 0.51492  7.64072E-05 1.00000 ];
INF_SP4                   (idx, [1:   8]) = [  7.60540E-03 0.00547 -3.63315E-06 0.44707 -1.67728E-05 0.55958 -7.17124E-05 1.00000 ];
INF_SP5                   (idx, [1:   8]) = [  3.93007E-03 0.01225 -2.64500E-06 0.63592 -1.29007E-06 1.00000  7.64463E-05 1.00000 ];
INF_SP6                   (idx, [1:   8]) = [  2.09169E-03 0.01970  2.90912E-06 0.57280  3.04119E-06 1.00000 -1.35520E-04 0.93441 ];
INF_SP7                   (idx, [1:   8]) = [  8.72154E-04 0.03854 -9.16688E-07 1.00000 -1.24550E-05 0.67993 -3.19117E-05 1.00000 ];

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

CMM_TRANSPXS              (idx, [1:   4]) = [  2.57991E-01 0.00293  7.47598E-01 0.01018 ];
CMM_TRANSPXS_X            (idx, [1:   4]) = [  2.57563E-01 0.00397  7.49619E-01 0.02204 ];
CMM_TRANSPXS_Y            (idx, [1:   4]) = [  2.56496E-01 0.00355  7.59177E-01 0.01966 ];
CMM_TRANSPXS_Z            (idx, [1:   4]) = [  2.60030E-01 0.00346  7.50085E-01 0.01818 ];
CMM_DIFFCOEF              (idx, [1:   4]) = [  1.29230E+00 0.00288  4.46987E-01 0.01022 ];
CMM_DIFFCOEF_X            (idx, [1:   4]) = [  1.29466E+00 0.00393  4.49756E-01 0.02148 ];
CMM_DIFFCOEF_Y            (idx, [1:   4]) = [  1.29996E+00 0.00357  4.43167E-01 0.01970 ];
CMM_DIFFCOEF_Z            (idx, [1:   4]) = [  1.28227E+00 0.00342  4.48038E-01 0.01876 ];

% Delayed neutron parameters (Meulekamp method):

BETA_EFF                  (idx, [1:  18]) = [  7.22398E-03 0.01727  2.11360E-04 0.10004  9.76808E-04 0.04821  6.57168E-04 0.05930  1.38335E-03 0.03979  2.31439E-03 0.03082  7.79064E-04 0.05078  6.58284E-04 0.05770  2.43554E-04 0.10067 ];
LAMBDA                    (idx, [1:  18]) = [  4.75482E-01 0.03076  1.24667E-02 0.0E+00  2.82917E-02 0.0E+00  4.25244E-02 5.8E-09  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 4.9E-09  3.55460E+00 0.0E+00 ];


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
INPUT_FILE_NAME           (idx, [1:135])  = '/home/hirepan/Documents/chalmers/Project/codes/Shynt/repo/cases/single_assem_1x1cell/serpent_files/global_cell_type4/XS_generation.serp' ;
WORKING_DIRECTORY         (idx, [1: 84])  = '/home/hirepan/Documents/chalmers/Project/codes/Shynt/repo/cases/single_assem_1x1cell' ;
HOSTNAME                  (idx, [1:  4])  = 'thor' ;
CPU_TYPE                  (idx, [1: 40])  = 'Intel(R) Core(TM) i9-10900 CPU @ 2.80GHz' ;
CPU_MHZ                   (idx, 1)        = 236.0 ;
START_DATE                (idx, [1: 24])  = 'Thu Mar 10 12:01:22 2022' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Mar 10 12:01:31 2022' ;

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
OMP_HISTORY_PROFILE       (idx, [1:  18]) = [  9.71495E-01  1.03589E+00  1.00679E+00  1.00185E+00  1.02946E+00  9.88480E-01  9.76268E-01  1.00439E+00  1.00437E+00  9.81434E-01  1.00040E+00  9.67228E-01  1.06126E+00  9.86813E-01  9.76906E-01  1.00890E+00  1.00417E+00  9.93891E-01  ];
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
ST_FRAC                   (idx, [1:   4]) = [  8.63771E-03 0.00297  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.91362E-01 2.6E-05  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  8.36758E-01 0.00011  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  8.37144E-01 0.00011  0.00000E+00 0.0E+00 ];
AVG_TRACKING_LOOPS        (idx, [1:   8]) = [  2.32303E+00 0.00036  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  2.54950E+01 0.00053  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  2.54950E+01 0.00053  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  4.95967E+00 0.00073  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  1.92772E-01 0.00329  0.00000E+00 0.0E+00 ];
LOST_PARTICLES            (idx, 1)        = 0 ;

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 500 ;
SIMULATED_HISTORIES       (idx, 1)        = 1000425 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  2.00085E+03 0.00142 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  2.00085E+03 0.00142 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.31235E+00 ;
RUNNING_TIME              (idx, 1)        =  1.43500E-01 ;
INIT_TIME                 (idx, [1:  2])  = [  1.16500E-02  1.16500E-02 ];
PROCESS_TIME              (idx, [1:  2])  = [  1.16666E-04  1.16666E-04 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  1.31667E-01  1.31667E-01  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  1.43400E-01  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 16.11392 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  1.75380E+01 0.00452 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  7.62602E-01 ;

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

NORM_COEF                 (idx, [1:   4]) = [  4.98701E-04 0.00084  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  5.77644E-01 0.00210 ];
U235_FISS                 (idx, [1:   4]) = [  4.75060E-01 0.00120  9.20037E-01 0.00041 ];
U238_FISS                 (idx, [1:   4]) = [  4.13165E-02 0.00509  7.99631E-02 0.00468 ];
U235_CAPT                 (idx, [1:   4]) = [  1.16254E-01 0.00280  2.40720E-01 0.00247 ];
U238_CAPT                 (idx, [1:   4]) = [  3.41366E-01 0.00166  7.06815E-01 0.00090 ];

% Neutron balance (particles/weight):

BALA_SRC_NEUTRON_SRC     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_FISS    (idx, [1:  2])  = [ 1000425 1.00000E+06 ];
BALA_SRC_NEUTRON_NXN     (idx, [1:  2])  = [ 0 1.94096E+03 ];
BALA_SRC_NEUTRON_VR      (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_TOT     (idx, [1:  2])  = [ 1000425 1.00194E+06 ];

BALA_LOSS_NEUTRON_CAPT    (idx, [1:  2])  = [ 483465 4.84198E+05 ];
BALA_LOSS_NEUTRON_FISS    (idx, [1:  2])  = [ 516960 5.17743E+05 ];
BALA_LOSS_NEUTRON_LEAK    (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_CUT     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_ERR     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_TOT     (idx, [1:  2])  = [ 1000425 1.00194E+06 ];

BALA_NEUTRON_DIFF         (idx, [1:  2])  = [ 0 1.04774E-09 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.67472E-11 0.00054 ];
TOT_POWDENS               (idx, [1:   2]) = [  3.08714E-15 0.00054 ];
TOT_GENRATE               (idx, [1:   2]) = [  1.27388E+00 0.00053 ];
TOT_FISSRATE              (idx, [1:   2]) = [  5.16005E-01 0.00054 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  4.83995E-01 0.00058 ];
TOT_ABSRATE               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.97402E-01 0.00084 ];
TOT_FLUX                  (idx, [1:   2]) = [  5.46874E+01 0.00069 ];
TOT_PHOTON_PRODRATE       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  2.54719E+01 0.00056 ];
INI_FMASS                 (idx, 1)        =  5.42481E-03 ;
TOT_FMASS                 (idx, 1)        =  5.42481E-03 ;

% Six-factor formula:

SIX_FF_ETA                (idx, [1:   2]) = [  1.84328E+00 0.00084 ];
SIX_FF_F                  (idx, [1:   2]) = [  9.64160E-01 0.00026 ];
SIX_FF_P                  (idx, [1:   2]) = [  4.99888E-01 0.00097 ];
SIX_FF_EPSILON            (idx, [1:   2]) = [  1.43920E+00 0.00092 ];
SIX_FF_LF                 (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
SIX_FF_LT                 (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
SIX_FF_KINF               (idx, [1:   2]) = [  1.27808E+00 0.00097 ];
SIX_FF_KEFF               (idx, [1:   2]) = [  1.27808E+00 0.00097 ];

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.46875E+00 3.3E-05 ];
FISSE                     (idx, [1:   2]) = [  2.02571E+02 2.8E-06 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.27782E+00 0.00099  1.26896E+00 0.00098  9.12644E-03 0.01749 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.27638E+00 0.00054 ];
COL_KEFF                  (idx, [1:   2]) = [  1.27772E+00 0.00111 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.27638E+00 0.00054 ];
ABS_KINF                  (idx, [1:   2]) = [  1.27638E+00 0.00054 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% ALF (Average lethargy of neutrons causing fission):
% Based on E0 = 2.000000E+01 MeV

ANA_ALF                   (idx, [1:   2]) = [  1.64579E+01 0.00046 ];
IMP_ALF                   (idx, [1:   2]) = [  1.64550E+01 0.00025 ];

% EALF (Energy corresponding to average lethargy of neutrons causing fission):

ANA_EALF                  (idx, [1:   2]) = [  1.44461E-06 0.00775 ];
IMP_EALF                  (idx, [1:   2]) = [  1.43401E-06 0.00410 ];

% AFGE (Average energy of neutrons causing fission):

ANA_AFGE                  (idx, [1:   2]) = [  2.74176E-01 0.00510 ];
IMP_AFGE                  (idx, [1:   2]) = [  2.75567E-01 0.00231 ];

% Forward-weighted delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
FWD_ANA_BETA_ZERO         (idx, [1:  18]) = [  5.93398E-03 0.01232  1.68253E-04 0.06789  7.80619E-04 0.03243  5.31754E-04 0.04103  1.11146E-03 0.02773  1.91368E-03 0.02105  6.67422E-04 0.03448  5.48591E-04 0.03711  2.12197E-04 0.06261 ];
FWD_ANA_LAMBDA            (idx, [1:  18]) = [  4.84618E-01 0.02012  4.38828E-03 0.06074  2.39914E-02 0.01895  3.07877E-02 0.02764  1.27188E-01 0.00960  2.89543E-01 0.00450  5.41188E-01 0.02154  1.22609E+00 0.02585  1.45028E+00 0.05392 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  18]) = [  7.22398E-03 0.01727  2.11360E-04 0.10004  9.76808E-04 0.04821  6.57168E-04 0.05930  1.38335E-03 0.03979  2.31439E-03 0.03082  7.79064E-04 0.05078  6.58284E-04 0.05770  2.43554E-04 0.10067 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  18]) = [  4.75482E-01 0.03076  1.24667E-02 0.0E+00  2.82917E-02 0.0E+00  4.25244E-02 5.8E-09  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 4.9E-09  3.55460E+00 0.0E+00 ];

% Adjoint weighted time constants using Nauchi's method:

IFP_CHAIN_LENGTH          (idx, 1)        = 15 ;
ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  1.60288E-05 0.00224  1.60168E-05 0.00225  1.75073E-05 0.02331 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  2.04713E-05 0.00199  2.04559E-05 0.00199  2.23692E-05 0.02326 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  18]) = [  7.15524E-03 0.01754  2.05617E-04 0.09471  9.46736E-04 0.04805  6.57096E-04 0.05457  1.29106E-03 0.04019  2.27560E-03 0.03001  8.50618E-04 0.05001  6.59441E-04 0.05263  2.69070E-04 0.08846 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  18]) = [  5.00191E-01 0.03139  1.24667E-02 0.0E+00  2.82917E-02 4.3E-09  4.25244E-02 8.1E-09  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 5.5E-09  3.55460E+00 4.9E-09 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  1.59703E-05 0.00489  1.59572E-05 0.00490  1.29607E-05 0.05133 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  2.03987E-05 0.00482  2.03821E-05 0.00483  1.65458E-05 0.05124 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  18]) = [  6.56899E-03 0.04877  2.06107E-04 0.27151  6.73193E-04 0.16734  5.83900E-04 0.16270  1.36961E-03 0.10786  2.24696E-03 0.08833  6.77781E-04 0.14109  6.15014E-04 0.17351  1.96436E-04 0.28246 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  18]) = [  4.82244E-01 0.06804  1.24667E-02 4.7E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 4.0E-09  2.92467E-01 5.8E-09  6.66488E-01 5.1E-09  1.63478E+00 0.0E+00  3.55460E+00 4.7E-09 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  18]) = [  6.61312E-03 0.04664  2.05346E-04 0.25390  6.42944E-04 0.15190  5.55052E-04 0.15528  1.41583E-03 0.10407  2.23547E-03 0.08667  7.18539E-04 0.13505  6.35583E-04 0.16927  2.04350E-04 0.25779 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  18]) = [  4.85784E-01 0.06717  1.24667E-02 4.7E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 4.0E-09  2.92467E-01 5.8E-09  6.66488E-01 5.1E-09  1.63478E+00 0.0E+00  3.55460E+00 6.0E-09 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -4.17112E+02 0.04968 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  1.60307E-05 0.00133 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  2.04745E-05 0.00090 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  6.91522E-03 0.00925 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -4.31690E+02 0.00931 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  2.71066E-07 0.00129 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  4.13167E-06 0.00104  4.13142E-06 0.00104  4.15554E-06 0.01252 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  2.46121E-05 0.00137  2.46125E-05 0.00138  2.44517E-05 0.01688 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.00486E-01 0.00097  4.99488E-01 0.00097  7.25060E-01 0.02136 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.18651E+01 0.02548 ];
ANA_MEAN_NCOL             (idx, [1:   4]) = [  2.54950E+01 0.00053  2.83575E+01 0.00069 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  7])  = 'u4gcu_2' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  2.00000E+01  6.06550E+00  3.67900E+00  2.23100E+00  1.35300E+00  8.21000E-01  5.00000E-01  3.02500E-01  1.83000E-01  1.11000E-01  6.74300E-02  4.08500E-02  2.47800E-02  1.50300E-02  9.11800E-03  5.50000E-03  3.51910E-03  2.23945E-03  1.42510E-03  9.06898E-04  3.67262E-04  1.48728E-04  7.55014E-05  4.80520E-05  2.77000E-05  1.59680E-05  9.87700E-06  4.00000E-06  3.30000E-06  2.60000E-06  2.10000E-06  1.85500E-06  1.50000E-06  1.30000E-06  1.15000E-06  1.12300E-06  1.09700E-06  1.07100E-06  1.04500E-06  1.02000E-06  9.96000E-07  9.72000E-07  9.50000E-07  9.10000E-07  8.50000E-07  7.80000E-07  6.25000E-07  5.00000E-07  4.00000E-07  3.50000E-07  3.20000E-07  3.00000E-07  2.80000E-07  2.50000E-07  2.20000E-07  1.80000E-07  1.40000E-07  1.00000E-07  8.00000E-08  6.70000E-08  5.80000E-08  5.00000E-08  4.20000E-08  3.50000E-08  3.00000E-08  2.50000E-08  2.00000E-08  1.50000E-08  1.00000E-08  5.00000E-09  1.00000E-11 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Micro-group spectrum:

INF_MICRO_FLX             (idx, [1: 140]) = [  1.09700E+04 0.01052  4.50289E+04 0.00445  9.47663E+04 0.00243  1.00206E+05 0.00210  9.55062E+04 0.00200  1.14587E+05 0.00109  7.79305E+04 0.00136  7.22347E+04 0.00129  5.52399E+04 0.00153  4.51466E+04 0.00125  3.91187E+04 0.00137  3.49195E+04 0.00147  3.23926E+04 0.00140  3.06506E+04 0.00160  2.98125E+04 0.00146  2.56497E+04 0.00161  2.53290E+04 0.00214  2.49464E+04 0.00175  2.43056E+04 0.00164  4.66471E+04 0.00123  4.44817E+04 0.00108  3.11776E+04 0.00114  1.97349E+04 0.00189  2.22352E+04 0.00166  2.04052E+04 0.00199  1.82506E+04 0.00249  2.87972E+04 0.00160  6.49706E+03 0.00333  8.17823E+03 0.00300  7.45255E+03 0.00398  4.28163E+03 0.00430  7.47963E+03 0.00316  5.04863E+03 0.00331  4.28310E+03 0.00445  8.13137E+02 0.00913  7.91593E+02 0.00866  8.14837E+02 0.00925  8.38578E+02 0.00755  8.36004E+02 0.00808  8.13281E+02 0.00927  8.55690E+02 0.01051  7.89205E+02 0.01017  1.53712E+03 0.00654  2.41189E+03 0.00647  3.08043E+03 0.00518  8.02306E+03 0.00278  8.33242E+03 0.00367  8.59501E+03 0.00358  5.34803E+03 0.00256  3.72490E+03 0.00496  2.75726E+03 0.00428  3.08029E+03 0.00320  5.39346E+03 0.00358  6.69405E+03 0.00371  1.15599E+04 0.00297  1.58725E+04 0.00308  2.11514E+04 0.00237  1.26533E+04 0.00308  8.66837E+03 0.00285  6.08409E+03 0.00338  5.36701E+03 0.00369  5.17399E+03 0.00337  4.25131E+03 0.00317  2.85282E+03 0.00513  2.61827E+03 0.00435  2.30520E+03 0.00310  1.93594E+03 0.00414  1.52411E+03 0.00561  1.03053E+03 0.00509  3.77421E+02 0.00785 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];

% Flux spectra in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  3.17996E+01 0.00091  3.67413E+00 0.00148 ];
INF_FISS_FLX              (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  4.03759E-01 0.00032  1.07648E+00 0.00026 ];
INF_CAPT                  (idx, [1:   4]) = [  1.58026E-04 0.00129  4.93197E-03 0.00045 ];
INF_ABS                   (idx, [1:   4]) = [  1.58026E-04 0.00129  4.93197E-03 0.00045 ];
INF_FISS                  (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_NSF                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_NUBAR                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_KAPPA                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_INVV                  (idx, [1:   4]) = [  5.29306E-08 0.00101  2.27166E-06 0.00045 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  4.03601E-01 0.00032  1.07162E+00 0.00025 ];
INF_SCATT1                (idx, [1:   4]) = [  2.35999E-01 0.00040  3.31855E-01 0.00082 ];
INF_SCATT2                (idx, [1:   4]) = [  9.03371E-02 0.00069  8.63884E-02 0.00291 ];
INF_SCATT3                (idx, [1:   4]) = [  2.82956E-03 0.01619  2.61811E-02 0.00774 ];
INF_SCATT4                (idx, [1:   4]) = [ -1.36981E-02 0.00244 -4.79269E-03 0.03231 ];
INF_SCATT5                (idx, [1:   4]) = [ -1.08089E-03 0.03381  4.72000E-03 0.02667 ];
INF_SCATT6                (idx, [1:   4]) = [  4.71366E-03 0.00870 -1.17729E-02 0.01236 ];
INF_SCATT7                (idx, [1:   4]) = [  4.59916E-04 0.09153 -6.61516E-04 0.20397 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  4.03601E-01 0.00032  1.07162E+00 0.00025 ];
INF_SCATTP1               (idx, [1:   4]) = [  2.35999E-01 0.00040  3.31855E-01 0.00082 ];
INF_SCATTP2               (idx, [1:   4]) = [  9.03371E-02 0.00069  8.63884E-02 0.00291 ];
INF_SCATTP3               (idx, [1:   4]) = [  2.82956E-03 0.01619  2.61811E-02 0.00774 ];
INF_SCATTP4               (idx, [1:   4]) = [ -1.36981E-02 0.00244 -4.79269E-03 0.03231 ];
INF_SCATTP5               (idx, [1:   4]) = [ -1.08089E-03 0.03381  4.72000E-03 0.02667 ];
INF_SCATTP6               (idx, [1:   4]) = [  4.71366E-03 0.00870 -1.17729E-02 0.01236 ];
INF_SCATTP7               (idx, [1:   4]) = [  4.59916E-04 0.09153 -6.61516E-04 0.20397 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  1.06428E-01 0.00089  6.37887E-01 0.00044 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  3.13208E+00 0.00089  5.22561E-01 0.00044 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  1.58026E-04 0.00129  4.93197E-03 0.00045 ];
INF_REMXS                 (idx, [1:   4]) = [  1.57465E-02 0.00112  6.50240E-03 0.00535 ];

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

INF_S0                    (idx, [1:   8]) = [  3.88012E-01 0.00031  1.55889E-02 0.00110  1.63920E-03 0.01270  1.06998E+00 0.00025 ];
INF_S1                    (idx, [1:   8]) = [  2.31360E-01 0.00041  4.63955E-03 0.00264  1.03982E-03 0.01658  3.30815E-01 0.00081 ];
INF_S2                    (idx, [1:   8]) = [  9.17426E-02 0.00069 -1.40551E-03 0.00575  5.67729E-04 0.02059  8.58207E-02 0.00295 ];
INF_S3                    (idx, [1:   8]) = [  4.46020E-03 0.00962 -1.63064E-03 0.00486  2.18960E-04 0.03869  2.59622E-02 0.00772 ];
INF_S4                    (idx, [1:   8]) = [ -1.31690E-02 0.00242 -5.29025E-04 0.01163  2.89058E-05 0.28061 -4.82159E-03 0.03249 ];
INF_S5                    (idx, [1:   8]) = [ -1.09804E-03 0.03133  1.71465E-05 0.36182 -5.80674E-05 0.11929  4.77806E-03 0.02645 ];
INF_S6                    (idx, [1:   8]) = [  4.84389E-03 0.00807 -1.30229E-04 0.03960 -9.05150E-05 0.08423 -1.16824E-02 0.01265 ];
INF_S7                    (idx, [1:   8]) = [  6.06746E-04 0.06528 -1.46830E-04 0.03125 -8.42942E-05 0.07905 -5.77222E-04 0.23360 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  3.88012E-01 0.00031  1.55889E-02 0.00110  1.63920E-03 0.01270  1.06998E+00 0.00025 ];
INF_SP1                   (idx, [1:   8]) = [  2.31360E-01 0.00041  4.63955E-03 0.00264  1.03982E-03 0.01658  3.30815E-01 0.00081 ];
INF_SP2                   (idx, [1:   8]) = [  9.17426E-02 0.00069 -1.40551E-03 0.00575  5.67729E-04 0.02059  8.58207E-02 0.00295 ];
INF_SP3                   (idx, [1:   8]) = [  4.46020E-03 0.00962 -1.63064E-03 0.00486  2.18960E-04 0.03869  2.59622E-02 0.00772 ];
INF_SP4                   (idx, [1:   8]) = [ -1.31690E-02 0.00242 -5.29025E-04 0.01163  2.89058E-05 0.28061 -4.82159E-03 0.03249 ];
INF_SP5                   (idx, [1:   8]) = [ -1.09804E-03 0.03133  1.71465E-05 0.36182 -5.80674E-05 0.11929  4.77806E-03 0.02645 ];
INF_SP6                   (idx, [1:   8]) = [  4.84389E-03 0.00807 -1.30229E-04 0.03960 -9.05150E-05 0.08423 -1.16824E-02 0.01265 ];
INF_SP7                   (idx, [1:   8]) = [  6.06746E-04 0.06528 -1.46830E-04 0.03125 -8.42942E-05 0.07905 -5.77222E-04 0.23360 ];

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

CMM_TRANSPXS              (idx, [1:   4]) = [  1.22933E-01 0.00128  3.94218E-01 0.00577 ];
CMM_TRANSPXS_X            (idx, [1:   4]) = [  1.22925E-01 0.00199  3.93499E-01 0.01043 ];
CMM_TRANSPXS_Y            (idx, [1:   4]) = [  1.23259E-01 0.00162  3.91562E-01 0.01136 ];
CMM_TRANSPXS_Z            (idx, [1:   4]) = [  1.22628E-01 0.00157  4.00142E-01 0.01091 ];
CMM_DIFFCOEF              (idx, [1:   4]) = [  2.71162E+00 0.00128  8.46234E-01 0.00578 ];
CMM_DIFFCOEF_X            (idx, [1:   4]) = [  2.71194E+00 0.00201  8.49392E-01 0.01079 ];
CMM_DIFFCOEF_Y            (idx, [1:   4]) = [  2.70451E+00 0.00161  8.53923E-01 0.01135 ];
CMM_DIFFCOEF_Z            (idx, [1:   4]) = [  2.71840E+00 0.00157  8.35387E-01 0.01076 ];

% Delayed neutron parameters (Meulekamp method):

BETA_EFF                  (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
LAMBDA                    (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

