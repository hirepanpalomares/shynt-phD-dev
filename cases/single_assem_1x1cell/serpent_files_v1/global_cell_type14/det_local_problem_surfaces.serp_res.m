
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
INPUT_FILE_NAME           (idx, [1:149])  = '/home/hirepan/Documents/chalmers/Project/codes/Shynt/repo/cases/single_assem_1x1cell/serpent_files/global_cell_type14/det_local_problem_surfaces.serp' ;
WORKING_DIRECTORY         (idx, [1: 84])  = '/home/hirepan/Documents/chalmers/Project/codes/Shynt/repo/cases/single_assem_1x1cell' ;
HOSTNAME                  (idx, [1:  4])  = 'thor' ;
CPU_TYPE                  (idx, [1: 40])  = 'Intel(R) Core(TM) i9-10900 CPU @ 2.80GHz' ;
CPU_MHZ                   (idx, 1)        = 236.0 ;
START_DATE                (idx, [1: 24])  = 'Thu Mar 10 11:47:29 2022' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Mar 10 11:48:05 2022' ;

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
OMP_HISTORY_PROFILE       (idx, [1:  18]) = [  9.50893E-01  1.07464E+00  9.82737E-01  9.64494E-01  1.00577E+00  9.67093E-01  1.01046E+00  1.03014E+00  1.05637E+00  1.03247E+00  1.01362E+00  9.53933E-01  9.64559E-01  9.73256E-01  1.04749E+00  1.05377E+00  9.63300E-01  9.55012E-01  ];
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
ST_FRAC                   (idx, [1:   4]) = [  3.64726E-03 0.00293  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.96353E-01 1.1E-05  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  8.37685E-01 0.00011  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  8.38072E-01 0.00011  0.00000E+00 0.0E+00 ];
AVG_TRACKING_LOOPS        (idx, [1:   8]) = [  3.41423E+00 0.00072  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  2.50480E+01 0.00054  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  2.50480E+01 0.00054  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  4.83969E+00 0.00079  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  4.20809E+01 0.00056  0.00000E+00 0.0E+00 ];
LOST_PARTICLES            (idx, 1)        = 0 ;

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 500 ;
SIMULATED_HISTORIES       (idx, 1)        = 1000538 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  2.00108E+03 0.00144 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  2.00108E+03 0.00144 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  1.06065E+01 ;
RUNNING_TIME              (idx, 1)        =  6.04017E-01 ;
INIT_TIME                 (idx, [1:  2])  = [  1.21500E-02  1.21500E-02 ];
PROCESS_TIME              (idx, [1:  2])  = [  1.66667E-04  1.66667E-04 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  5.91700E-01  5.91700E-01  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  6.03983E-01  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 17.55998 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  1.79051E+01 0.00141 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  9.56486E-01 ;

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

NORM_COEF                 (idx, [1:   4]) = [  4.99648E-04 0.00079  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  5.57186E-01 0.00217 ];
U235_FISS                 (idx, [1:   4]) = [  4.81509E-01 0.00110  9.20613E-01 0.00039 ];
U238_FISS                 (idx, [1:   4]) = [  4.15472E-02 0.00492  7.93869E-02 0.00453 ];
U235_CAPT                 (idx, [1:   4]) = [  1.19316E-01 0.00280  2.49574E-01 0.00243 ];
U238_CAPT                 (idx, [1:   4]) = [  3.34578E-01 0.00175  6.99818E-01 0.00094 ];

% Neutron balance (particles/weight):

BALA_SRC_NEUTRON_SRC     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_FISS    (idx, [1:  2])  = [ 1000538 1.00000E+06 ];
BALA_SRC_NEUTRON_NXN     (idx, [1:  2])  = [ 0 1.84980E+03 ];
BALA_SRC_NEUTRON_VR      (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_TOT     (idx, [1:  2])  = [ 1000538 1.00185E+06 ];

BALA_LOSS_NEUTRON_CAPT    (idx, [1:  2])  = [ 477695 4.78383E+05 ];
BALA_LOSS_NEUTRON_FISS    (idx, [1:  2])  = [ 522843 5.23467E+05 ];
BALA_LOSS_NEUTRON_LEAK    (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_CUT     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_ERR     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_TOT     (idx, [1:  2])  = [ 1000538 1.00185E+06 ];

BALA_NEUTRON_DIFF         (idx, [1:  2])  = [ 0 6.98492E-10 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.69437E-11 0.00053 ];
TOT_POWDENS               (idx, [1:   2]) = [  3.12337E-15 0.00053 ];
TOT_GENRATE               (idx, [1:   2]) = [  1.28877E+00 0.00052 ];
TOT_FISSRATE              (idx, [1:   2]) = [  5.22067E-01 0.00053 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  4.77933E-01 0.00058 ];
TOT_ABSRATE               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.99297E-01 0.00079 ];
TOT_FLUX                  (idx, [1:   2]) = [  5.42181E+01 0.00066 ];
TOT_PHOTON_PRODRATE       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  2.50708E+01 0.00051 ];
INI_FMASS                 (idx, 1)        =  5.42481E-03 ;
TOT_FMASS                 (idx, 1)        =  5.42481E-03 ;

% Six-factor formula:

SIX_FF_ETA                (idx, [1:   2]) = [  1.85869E+00 0.00080 ];
SIX_FF_F                  (idx, [1:   2]) = [  9.66009E-01 0.00026 ];
SIX_FF_P                  (idx, [1:   2]) = [  4.91181E-01 0.00105 ];
SIX_FF_EPSILON            (idx, [1:   2]) = [  1.46589E+00 0.00100 ];
SIX_FF_LF                 (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
SIX_FF_LT                 (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
SIX_FF_KINF               (idx, [1:   2]) = [  1.29221E+00 0.00098 ];
SIX_FF_KEFF               (idx, [1:   2]) = [  1.29221E+00 0.00098 ];

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.46859E+00 3.4E-05 ];
FISSE                     (idx, [1:   2]) = [  2.02568E+02 2.8E-06 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.29236E+00 0.00099  1.28288E+00 0.00100  9.33192E-03 0.01574 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.29127E+00 0.00052 ];
COL_KEFF                  (idx, [1:   2]) = [  1.29017E+00 0.00109 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.29127E+00 0.00052 ];
ABS_KINF                  (idx, [1:   2]) = [  1.29127E+00 0.00052 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% ALF (Average lethargy of neutrons causing fission):
% Based on E0 = 2.000000E+01 MeV

ANA_ALF                   (idx, [1:   2]) = [  1.63586E+01 0.00047 ];
IMP_ALF                   (idx, [1:   2]) = [  1.63541E+01 0.00025 ];

% EALF (Energy corresponding to average lethargy of neutrons causing fission):

ANA_EALF                  (idx, [1:   2]) = [  1.59599E-06 0.00777 ];
IMP_EALF                  (idx, [1:   2]) = [  1.58608E-06 0.00411 ];

% AFGE (Average energy of neutrons causing fission):

ANA_AFGE                  (idx, [1:   2]) = [  2.74488E-01 0.00487 ];
IMP_AFGE                  (idx, [1:   2]) = [  2.74838E-01 0.00235 ];

% Forward-weighted delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
FWD_ANA_BETA_ZERO         (idx, [1:  18]) = [  5.88212E-03 0.01156  1.66752E-04 0.07003  8.40452E-04 0.03033  4.98882E-04 0.03882  1.07474E-03 0.02675  1.87227E-03 0.02032  6.71653E-04 0.03383  5.54497E-04 0.03900  2.02871E-04 0.06110 ];
FWD_ANA_LAMBDA            (idx, [1:  18]) = [  4.78296E-01 0.01838  4.23868E-03 0.06237  2.50664E-02 0.01606  3.11279E-02 0.02709  1.22931E-01 0.01284  2.90712E-01 0.00348  5.58517E-01 0.01968  1.23589E+00 0.02543  1.45028E+00 0.05392 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  18]) = [  7.14826E-03 0.01657  1.80608E-04 0.10435  1.03806E-03 0.04454  6.43488E-04 0.05856  1.31044E-03 0.04099  2.25554E-03 0.02948  7.85950E-04 0.04847  6.73670E-04 0.05739  2.60506E-04 0.08712 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  18]) = [  4.76809E-01 0.02639  1.24667E-02 0.0E+00  2.82917E-02 0.0E+00  4.25244E-02 5.7E-09  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 4.9E-09  3.55460E+00 0.0E+00 ];

% Adjoint weighted time constants using Nauchi's method:

IFP_CHAIN_LENGTH          (idx, 1)        = 15 ;
ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  1.47052E-05 0.00231  1.46979E-05 0.00231  1.56191E-05 0.02397 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  1.89949E-05 0.00208  1.89855E-05 0.00209  2.01709E-05 0.02391 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  18]) = [  7.22432E-03 0.01585  1.93907E-04 0.10332  1.02504E-03 0.04187  6.37005E-04 0.05257  1.26311E-03 0.03996  2.35690E-03 0.02826  8.09019E-04 0.04901  6.79189E-04 0.05286  2.60156E-04 0.08407 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  18]) = [  4.84752E-01 0.02682  1.24667E-02 0.0E+00  2.82917E-02 1.5E-09  4.25244E-02 8.1E-09  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 5.5E-09  3.55460E+00 4.9E-09 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  1.47651E-05 0.00495  1.47457E-05 0.00497  1.23012E-05 0.04787 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  1.90741E-05 0.00488  1.90489E-05 0.00489  1.59065E-05 0.04787 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  18]) = [  7.69744E-03 0.04893  1.89082E-04 0.30096  1.09802E-03 0.12612  8.00415E-04 0.14467  1.13044E-03 0.11309  2.62099E-03 0.08968  6.96193E-04 0.14005  8.67052E-04 0.13919  2.95249E-04 0.26338 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  18]) = [  4.99780E-01 0.06557  1.24667E-02 5.4E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 3.2E-09  2.92467E-01 5.8E-09  6.66488E-01 5.5E-09  1.63478E+00 0.0E+00  3.55460E+00 6.0E-09 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  18]) = [  7.78415E-03 0.04695  2.10324E-04 0.27667  1.11784E-03 0.12346  7.83096E-04 0.14186  1.14924E-03 0.10873  2.69306E-03 0.08448  7.06411E-04 0.14251  8.11519E-04 0.13887  3.12667E-04 0.26266 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  18]) = [  5.01134E-01 0.06567  1.24667E-02 3.8E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 3.2E-09  2.92467E-01 5.8E-09  6.66488E-01 5.5E-09  1.63478E+00 0.0E+00  3.55460E+00 3.8E-09 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -5.29397E+02 0.04862 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  1.47367E-05 0.00131 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  1.90361E-05 0.00091 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  7.10043E-03 0.00862 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -4.82488E+02 0.00884 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  2.54964E-07 0.00127 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  4.10743E-06 0.00109  4.10742E-06 0.00109  4.10033E-06 0.01307 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  2.30366E-05 0.00143  2.30420E-05 0.00144  2.24079E-05 0.01680 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  4.91880E-01 0.00105  4.90837E-01 0.00106  7.17850E-01 0.02133 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.23062E+01 0.02512 ];
ANA_MEAN_NCOL             (idx, [1:   4]) = [  2.50480E+01 0.00054  2.77332E+01 0.00075 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  1])  = '0' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  2.00000E+01  6.06550E+00  3.67900E+00  2.23100E+00  1.35300E+00  8.21000E-01  5.00000E-01  3.02500E-01  1.83000E-01  1.11000E-01  6.74300E-02  4.08500E-02  2.47800E-02  1.50300E-02  9.11800E-03  5.50000E-03  3.51910E-03  2.23945E-03  1.42510E-03  9.06898E-04  3.67262E-04  1.48728E-04  7.55014E-05  4.80520E-05  2.77000E-05  1.59680E-05  9.87700E-06  4.00000E-06  3.30000E-06  2.60000E-06  2.10000E-06  1.85500E-06  1.50000E-06  1.30000E-06  1.15000E-06  1.12300E-06  1.09700E-06  1.07100E-06  1.04500E-06  1.02000E-06  9.96000E-07  9.72000E-07  9.50000E-07  9.10000E-07  8.50000E-07  7.80000E-07  6.25000E-07  5.00000E-07  4.00000E-07  3.50000E-07  3.20000E-07  3.00000E-07  2.80000E-07  2.50000E-07  2.20000E-07  1.80000E-07  1.40000E-07  1.00000E-07  8.00000E-08  6.70000E-08  5.80000E-08  5.00000E-08  4.20000E-08  3.50000E-08  3.00000E-08  2.50000E-08  2.00000E-08  1.50000E-08  1.00000E-08  5.00000E-09  1.00000E-11 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Micro-group spectrum:

INF_MICRO_FLX             (idx, [1: 140]) = [  1.68585E+04 0.00732  7.04647E+04 0.00332  1.48282E+05 0.00238  1.56718E+05 0.00178  1.49406E+05 0.00166  1.80370E+05 0.00119  1.21390E+05 0.00145  1.12580E+05 0.00111  8.54686E+04 0.00149  6.98876E+04 0.00155  6.03688E+04 0.00156  5.38230E+04 0.00147  4.97918E+04 0.00123  4.71407E+04 0.00170  4.58987E+04 0.00157  3.92527E+04 0.00178  3.86883E+04 0.00179  3.79401E+04 0.00196  3.69993E+04 0.00220  7.09979E+04 0.00146  6.73020E+04 0.00164  4.70667E+04 0.00162  2.97564E+04 0.00233  3.29949E+04 0.00199  3.01066E+04 0.00154  2.74488E+04 0.00223  4.21564E+04 0.00179  9.82295E+03 0.00379  1.24035E+04 0.00324  1.13017E+04 0.00351  6.45087E+03 0.00407  1.14184E+04 0.00298  7.69029E+03 0.00453  6.37785E+03 0.00435  1.19317E+03 0.00794  1.18758E+03 0.00675  1.21493E+03 0.00725  1.25366E+03 0.00728  1.26921E+03 0.00659  1.22368E+03 0.00915  1.27441E+03 0.00828  1.19101E+03 0.00878  2.26433E+03 0.00686  3.60178E+03 0.00550  4.57083E+03 0.00428  1.20467E+04 0.00305  1.24007E+04 0.00342  1.27560E+04 0.00366  7.80581E+03 0.00330  5.38555E+03 0.00440  3.91993E+03 0.00475  4.38845E+03 0.00382  7.68090E+03 0.00392  9.42327E+03 0.00269  1.62941E+04 0.00258  2.20701E+04 0.00315  2.90105E+04 0.00288  1.71139E+04 0.00244  1.16424E+04 0.00223  8.12446E+03 0.00283  7.10075E+03 0.00270  6.79928E+03 0.00278  5.59459E+03 0.00313  3.70473E+03 0.00386  3.36540E+03 0.00451  2.94611E+03 0.00345  2.44462E+03 0.00316  1.89637E+03 0.00432  1.25875E+03 0.00588  4.37444E+02 0.00860 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.29016E+00 0.00111 ];

% Flux spectra in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  4.91382E+01 0.00066  5.08542E+00 0.00119 ];
INF_FISS_FLX              (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  4.12198E-01 0.00022  9.47824E-01 0.00028 ];
INF_CAPT                  (idx, [1:   4]) = [  7.10358E-03 0.00117  2.53638E-02 0.00045 ];
INF_ABS                   (idx, [1:   4]) = [  1.03879E-02 0.00088  9.63276E-02 0.00053 ];
INF_FISS                  (idx, [1:   4]) = [  3.28430E-03 0.00072  7.09638E-02 0.00056 ];
INF_NSF                   (idx, [1:   4]) = [  8.34524E-03 0.00071  1.72882E-01 0.00056 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.54095E+00 0.00010  2.43620E+00 0.0E+00 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.03233E+02 7.3E-06  2.02270E+02 0.0E+00 ];
INF_INVV                  (idx, [1:   4]) = [  5.14991E-08 0.00064  2.22113E-06 0.00040 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  4.01813E-01 0.00022  8.51304E-01 0.00040 ];
INF_SCATT1                (idx, [1:   4]) = [  1.67655E-01 0.00028  2.26663E-01 0.00103 ];
INF_SCATT2                (idx, [1:   4]) = [  6.64255E-02 0.00058  5.83620E-02 0.00311 ];
INF_SCATT3                (idx, [1:   4]) = [  6.01216E-03 0.00710  1.75827E-02 0.01101 ];
INF_SCATT4                (idx, [1:   4]) = [ -6.17346E-03 0.00510 -3.27925E-03 0.04241 ];
INF_SCATT5                (idx, [1:   4]) = [  7.32393E-04 0.03415  2.90197E-03 0.04722 ];
INF_SCATT6                (idx, [1:   4]) = [  3.77770E-03 0.00629 -7.73671E-03 0.01682 ];
INF_SCATT7                (idx, [1:   4]) = [  5.93979E-04 0.03329 -2.53003E-04 0.39388 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  4.01851E-01 0.00022  8.51304E-01 0.00040 ];
INF_SCATTP1               (idx, [1:   4]) = [  1.67656E-01 0.00028  2.26663E-01 0.00103 ];
INF_SCATTP2               (idx, [1:   4]) = [  6.64257E-02 0.00058  5.83620E-02 0.00311 ];
INF_SCATTP3               (idx, [1:   4]) = [  6.01230E-03 0.00709  1.75827E-02 0.01101 ];
INF_SCATTP4               (idx, [1:   4]) = [ -6.17337E-03 0.00509 -3.27925E-03 0.04241 ];
INF_SCATTP5               (idx, [1:   4]) = [  7.32453E-04 0.03419  2.90197E-03 0.04722 ];
INF_SCATTP6               (idx, [1:   4]) = [  3.77768E-03 0.00628 -7.73671E-03 0.01682 ];
INF_SCATTP7               (idx, [1:   4]) = [  5.93769E-04 0.03342 -2.53003E-04 0.39388 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  1.84384E-01 0.00067  6.42591E-01 0.00050 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.80784E+00 0.00067  5.18736E-01 0.00050 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  1.03503E-02 0.00091  9.63276E-02 0.00053 ];
INF_REMXS                 (idx, [1:   4]) = [  2.05772E-02 0.00055  9.84815E-02 0.00127 ];

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

INF_S0                    (idx, [1:   8]) = [  3.91621E-01 0.00022  1.01919E-02 0.00099  1.96154E-03 0.00851  8.49342E-01 0.00040 ];
INF_S1                    (idx, [1:   8]) = [  1.64773E-01 0.00027  2.88238E-03 0.00221  6.56408E-04 0.01309  2.26006E-01 0.00104 ];
INF_S2                    (idx, [1:   8]) = [  6.73321E-02 0.00058 -9.06637E-04 0.00621  3.73864E-04 0.02271  5.79881E-02 0.00316 ];
INF_S3                    (idx, [1:   8]) = [  7.05244E-03 0.00600 -1.04028E-03 0.00452  1.40934E-04 0.05602  1.74417E-02 0.01116 ];
INF_S4                    (idx, [1:   8]) = [ -5.84214E-03 0.00540 -3.31319E-04 0.01160  9.97629E-07 1.00000 -3.28025E-03 0.04223 ];
INF_S5                    (idx, [1:   8]) = [  7.08276E-04 0.03425  2.41169E-05 0.17651 -5.08140E-05 0.08880  2.95279E-03 0.04572 ];
INF_S6                    (idx, [1:   8]) = [  3.85118E-03 0.00605 -7.34811E-05 0.04412 -7.95589E-05 0.06055 -7.65715E-03 0.01722 ];
INF_S7                    (idx, [1:   8]) = [  6.88813E-04 0.02883 -9.48334E-05 0.02987 -6.54565E-05 0.10147 -1.87547E-04 0.53329 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  3.91659E-01 0.00022  1.01919E-02 0.00099  1.96154E-03 0.00851  8.49342E-01 0.00040 ];
INF_SP1                   (idx, [1:   8]) = [  1.64774E-01 0.00027  2.88238E-03 0.00221  6.56408E-04 0.01309  2.26006E-01 0.00104 ];
INF_SP2                   (idx, [1:   8]) = [  6.73323E-02 0.00058 -9.06637E-04 0.00621  3.73864E-04 0.02271  5.79881E-02 0.00316 ];
INF_SP3                   (idx, [1:   8]) = [  7.05257E-03 0.00599 -1.04028E-03 0.00452  1.40934E-04 0.05602  1.74417E-02 0.01116 ];
INF_SP4                   (idx, [1:   8]) = [ -5.84205E-03 0.00539 -3.31319E-04 0.01160  9.97629E-07 1.00000 -3.28025E-03 0.04223 ];
INF_SP5                   (idx, [1:   8]) = [  7.08336E-04 0.03427  2.41169E-05 0.17651 -5.08140E-05 0.08880  2.95279E-03 0.04572 ];
INF_SP6                   (idx, [1:   8]) = [  3.85116E-03 0.00604 -7.34811E-05 0.04412 -7.95589E-05 0.06055 -7.65715E-03 0.01722 ];
INF_SP7                   (idx, [1:   8]) = [  6.88602E-04 0.02893 -9.48334E-05 0.02987 -6.54565E-05 0.10147 -1.87547E-04 0.53329 ];

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

CMM_TRANSPXS              (idx, [1:   4]) = [  1.90300E-01 0.00144  5.78572E-01 0.00696 ];
CMM_TRANSPXS_X            (idx, [1:   4]) = [  1.90166E-01 0.00214  5.82828E-01 0.01092 ];
CMM_TRANSPXS_Y            (idx, [1:   4]) = [  1.90646E-01 0.00197  5.77597E-01 0.01165 ];
CMM_TRANSPXS_Z            (idx, [1:   4]) = [  1.90123E-01 0.00230  5.78349E-01 0.01080 ];
CMM_DIFFCOEF              (idx, [1:   4]) = [  1.75171E+00 0.00144  5.76803E-01 0.00697 ];
CMM_DIFFCOEF_X            (idx, [1:   4]) = [  1.75305E+00 0.00215  5.73554E-01 0.01086 ];
CMM_DIFFCOEF_Y            (idx, [1:   4]) = [  1.74861E+00 0.00198  5.78946E-01 0.01140 ];
CMM_DIFFCOEF_Z            (idx, [1:   4]) = [  1.75348E+00 0.00231  5.77908E-01 0.01041 ];

% Delayed neutron parameters (Meulekamp method):

BETA_EFF                  (idx, [1:  18]) = [  7.14826E-03 0.01657  1.80608E-04 0.10435  1.03806E-03 0.04454  6.43488E-04 0.05856  1.31044E-03 0.04099  2.25554E-03 0.02948  7.85950E-04 0.04847  6.73670E-04 0.05739  2.60506E-04 0.08712 ];
LAMBDA                    (idx, [1:  18]) = [  4.76809E-01 0.02639  1.24667E-02 0.0E+00  2.82917E-02 0.0E+00  4.25244E-02 5.7E-09  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 4.9E-09  3.55460E+00 0.0E+00 ];

