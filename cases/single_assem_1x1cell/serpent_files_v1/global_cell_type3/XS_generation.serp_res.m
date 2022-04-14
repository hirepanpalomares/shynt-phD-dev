
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
INPUT_FILE_NAME           (idx, [1:135])  = '/home/hirepan/Documents/chalmers/Project/codes/Shynt/repo/cases/single_assem_1x1cell/serpent_files/global_cell_type3/XS_generation.serp' ;
WORKING_DIRECTORY         (idx, [1: 84])  = '/home/hirepan/Documents/chalmers/Project/codes/Shynt/repo/cases/single_assem_1x1cell' ;
HOSTNAME                  (idx, [1:  4])  = 'thor' ;
CPU_TYPE                  (idx, [1: 40])  = 'Intel(R) Core(TM) i9-10900 CPU @ 2.80GHz' ;
CPU_MHZ                   (idx, 1)        = 236.0 ;
START_DATE                (idx, [1: 24])  = 'Thu Mar 10 11:53:34 2022' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Mar 10 11:53:43 2022' ;

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
OMP_HISTORY_PROFILE       (idx, [1:  18]) = [  9.98663E-01  1.00842E+00  1.05559E+00  9.74777E-01  1.01483E+00  1.02835E+00  9.74155E-01  1.00643E+00  9.98042E-01  9.67485E-01  9.70918E-01  9.60945E-01  1.02315E+00  9.89148E-01  9.94559E-01  9.88853E-01  1.00165E+00  1.04402E+00  ];
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

MIN_MACROXS               (idx, [1:   4]) = [  5.00000E-02 4.7E-09  0.00000E+00 0.0E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  8.34161E-03 0.00279  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.91658E-01 2.3E-05  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  8.33741E-01 0.00011  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  8.34121E-01 0.00011  0.00000E+00 0.0E+00 ];
AVG_TRACKING_LOOPS        (idx, [1:   8]) = [  2.35551E+00 0.00040  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  2.69198E+01 0.00055  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  2.69198E+01 0.00055  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  5.35346E+00 0.00076  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  1.97198E-01 0.00311  0.00000E+00 0.0E+00 ];
LOST_PARTICLES            (idx, 1)        = 0 ;

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 500 ;
SIMULATED_HISTORIES       (idx, 1)        = 1000593 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  2.00119E+03 0.00145 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  2.00119E+03 0.00145 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.40336E+00 ;
RUNNING_TIME              (idx, 1)        =  1.48150E-01 ;
INIT_TIME                 (idx, [1:  2])  = [  1.19000E-02  1.19000E-02 ];
PROCESS_TIME              (idx, [1:  2])  = [  1.00001E-04  1.00001E-04 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  1.36100E-01  1.36100E-01  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  1.48050E-01  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 16.22249 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  1.77082E+01 0.00561 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  7.73990E-01 ;

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

NORM_COEF                 (idx, [1:   4]) = [  4.99787E-04 0.00082  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  6.55338E-01 0.00201 ];
U235_FISS                 (idx, [1:   4]) = [  4.54820E-01 0.00121  9.15823E-01 0.00044 ];
U238_FISS                 (idx, [1:   4]) = [  4.18232E-02 0.00509  8.41765E-02 0.00478 ];
U235_CAPT                 (idx, [1:   4]) = [  1.06303E-01 0.00312  2.10544E-01 0.00274 ];
U238_CAPT                 (idx, [1:   4]) = [  3.67507E-01 0.00157  7.27984E-01 0.00087 ];

% Neutron balance (particles/weight):

BALA_SRC_NEUTRON_SRC     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_FISS    (idx, [1:  2])  = [ 1000593 1.00000E+06 ];
BALA_SRC_NEUTRON_NXN     (idx, [1:  2])  = [ 0 1.91611E+03 ];
BALA_SRC_NEUTRON_VR      (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_TOT     (idx, [1:  2])  = [ 1000593 1.00192E+06 ];

BALA_LOSS_NEUTRON_CAPT    (idx, [1:  2])  = [ 504326 5.05033E+05 ];
BALA_LOSS_NEUTRON_FISS    (idx, [1:  2])  = [ 496267 4.96883E+05 ];
BALA_LOSS_NEUTRON_LEAK    (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_CUT     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_ERR     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_TOT     (idx, [1:  2])  = [ 1000593 1.00192E+06 ];

BALA_NEUTRON_DIFF         (idx, [1:  2])  = [ 0 -1.04774E-09 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.61083E-11 0.00053 ];
TOT_POWDENS               (idx, [1:   2]) = [  2.96937E-15 0.00053 ];
TOT_GENRATE               (idx, [1:   2]) = [  1.22569E+00 0.00052 ];
TOT_FISSRATE              (idx, [1:   2]) = [  4.96283E-01 0.00053 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  5.03717E-01 0.00052 ];
TOT_ABSRATE               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.99574E-01 0.00082 ];
TOT_FLUX                  (idx, [1:   2]) = [  5.65290E+01 0.00067 ];
TOT_PHOTON_PRODRATE       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  2.69545E+01 0.00053 ];
INI_FMASS                 (idx, 1)        =  5.42481E-03 ;
TOT_FMASS                 (idx, 1)        =  5.42481E-03 ;

% Six-factor formula:

SIX_FF_ETA                (idx, [1:   2]) = [  1.78163E+00 0.00087 ];
SIX_FF_F                  (idx, [1:   2]) = [  9.55739E-01 0.00029 ];
SIX_FF_P                  (idx, [1:   2]) = [  5.24457E-01 0.00096 ];
SIX_FF_EPSILON            (idx, [1:   2]) = [  1.37474E+00 0.00088 ];
SIX_FF_LF                 (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
SIX_FF_LT                 (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
SIX_FF_KINF               (idx, [1:   2]) = [  1.22721E+00 0.00098 ];
SIX_FF_KEFF               (idx, [1:   2]) = [  1.22721E+00 0.00098 ];

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.46974E+00 3.4E-05 ];
FISSE                     (idx, [1:   2]) = [  2.02586E+02 2.9E-06 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.22698E+00 0.00102  1.21848E+00 0.00100  8.72621E-03 0.01541 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.22808E+00 0.00053 ];
COL_KEFF                  (idx, [1:   2]) = [  1.22670E+00 0.00110 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.22808E+00 0.00053 ];
ABS_KINF                  (idx, [1:   2]) = [  1.22808E+00 0.00053 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% ALF (Average lethargy of neutrons causing fission):
% Based on E0 = 2.000000E+01 MeV

ANA_ALF                   (idx, [1:   2]) = [  1.67128E+01 0.00047 ];
IMP_ALF                   (idx, [1:   2]) = [  1.67055E+01 0.00023 ];

% EALF (Energy corresponding to average lethargy of neutrons causing fission):

ANA_EALF                  (idx, [1:   2]) = [  1.12093E-06 0.00802 ];
IMP_EALF                  (idx, [1:   2]) = [  1.11579E-06 0.00393 ];

% AFGE (Average energy of neutrons causing fission):

ANA_AFGE                  (idx, [1:   2]) = [  2.82914E-01 0.00522 ];
IMP_AFGE                  (idx, [1:   2]) = [  2.82417E-01 0.00231 ];

% Forward-weighted delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
FWD_ANA_BETA_ZERO         (idx, [1:  18]) = [  6.14629E-03 0.01139  1.61685E-04 0.07150  9.00953E-04 0.03044  4.97308E-04 0.03977  1.15062E-03 0.02607  1.92799E-03 0.01903  6.93948E-04 0.03518  5.65561E-04 0.03838  2.48234E-04 0.05710 ];
FWD_ANA_LAMBDA            (idx, [1:  18]) = [  4.93121E-01 0.01869  4.01428E-03 0.06496  2.53494E-02 0.01525  2.98521E-02 0.02917  1.25858E-01 0.01070  2.90712E-01 0.00348  5.57184E-01 0.01983  1.22936E+00 0.02571  1.62801E+00 0.04870 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  18]) = [  7.22833E-03 0.01621  1.90071E-04 0.11232  1.09700E-03 0.04547  6.16621E-04 0.06158  1.32561E-03 0.04193  2.20892E-03 0.03013  8.11032E-04 0.05365  6.64455E-04 0.05749  3.14607E-04 0.08699 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  18]) = [  5.04836E-01 0.02937  1.24667E-02 0.0E+00  2.82917E-02 0.0E+00  4.25244E-02 6.0E-09  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 4.9E-09  3.55460E+00 0.0E+00 ];

% Adjoint weighted time constants using Nauchi's method:

IFP_CHAIN_LENGTH          (idx, 1)        = 15 ;
ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  2.07760E-05 0.00238  2.07561E-05 0.00239  2.37254E-05 0.02386 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  2.54762E-05 0.00205  2.54519E-05 0.00207  2.90834E-05 0.02388 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  18]) = [  7.14600E-03 0.01553  1.85291E-04 0.10876  1.02514E-03 0.04300  6.27096E-04 0.05636  1.32204E-03 0.03697  2.15559E-03 0.02996  8.55387E-04 0.04655  6.52691E-04 0.05439  3.22763E-04 0.07746 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  18]) = [  5.14783E-01 0.02811  1.24667E-02 0.0E+00  2.82917E-02 2.6E-09  4.25244E-02 8.1E-09  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 5.5E-09  3.55460E+00 4.6E-09 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  2.09049E-05 0.00497  2.08921E-05 0.00500  1.68649E-05 0.05556 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  2.56406E-05 0.00493  2.56250E-05 0.00495  2.06620E-05 0.05540 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  18]) = [  7.28707E-03 0.04731  1.10613E-04 0.38052  1.27976E-03 0.12997  6.76923E-04 0.16482  1.09021E-03 0.12372  2.05457E-03 0.09107  8.33433E-04 0.14951  9.27479E-04 0.17432  3.14077E-04 0.22831 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  18]) = [  5.36213E-01 0.06570  1.24667E-02 2.7E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 3.5E-09  2.92467E-01 5.0E-09  6.66488E-01 4.6E-09  1.63478E+00 0.0E+00  3.55460E+00 7.1E-09 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  18]) = [  7.32819E-03 0.04554  1.11014E-04 0.33599  1.23447E-03 0.12595  6.88807E-04 0.15852  1.14651E-03 0.12361  2.05331E-03 0.08899  8.58028E-04 0.14874  8.97515E-04 0.16398  3.38541E-04 0.21300 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  18]) = [  5.37558E-01 0.06493  1.24667E-02 4.7E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 3.2E-09  2.92467E-01 4.9E-09  6.66488E-01 4.6E-09  1.63478E+00 0.0E+00  3.55460E+00 6.5E-09 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -3.51963E+02 0.04704 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  2.08640E-05 0.00142 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  2.55871E-05 0.00105 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  7.06845E-03 0.00875 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -3.39355E+02 0.00900 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  3.26797E-07 0.00120 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  4.19112E-06 0.00100  4.19116E-06 0.00100  4.21402E-06 0.01320 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.01428E-05 0.00137  3.01404E-05 0.00137  3.06214E-05 0.01601 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.25039E-01 0.00096  5.24157E-01 0.00097  7.19462E-01 0.02301 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.18408E+01 0.02567 ];
ANA_MEAN_NCOL             (idx, [1:   4]) = [  2.69198E+01 0.00055  3.02959E+01 0.00076 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  7])  = 'u4gcu_1' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  2.00000E+01  6.06550E+00  3.67900E+00  2.23100E+00  1.35300E+00  8.21000E-01  5.00000E-01  3.02500E-01  1.83000E-01  1.11000E-01  6.74300E-02  4.08500E-02  2.47800E-02  1.50300E-02  9.11800E-03  5.50000E-03  3.51910E-03  2.23945E-03  1.42510E-03  9.06898E-04  3.67262E-04  1.48728E-04  7.55014E-05  4.80520E-05  2.77000E-05  1.59680E-05  9.87700E-06  4.00000E-06  3.30000E-06  2.60000E-06  2.10000E-06  1.85500E-06  1.50000E-06  1.30000E-06  1.15000E-06  1.12300E-06  1.09700E-06  1.07100E-06  1.04500E-06  1.02000E-06  9.96000E-07  9.72000E-07  9.50000E-07  9.10000E-07  8.50000E-07  7.80000E-07  6.25000E-07  5.00000E-07  4.00000E-07  3.50000E-07  3.20000E-07  3.00000E-07  2.80000E-07  2.50000E-07  2.20000E-07  1.80000E-07  1.40000E-07  1.00000E-07  8.00000E-08  6.70000E-08  5.80000E-08  5.00000E-08  4.20000E-08  3.50000E-08  3.00000E-08  2.50000E-08  2.00000E-08  1.50000E-08  1.00000E-08  5.00000E-09  1.00000E-11 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Micro-group spectrum:

INF_MICRO_FLX             (idx, [1: 140]) = [  6.06599E+03 0.00770  2.51891E+04 0.00528  5.35249E+04 0.00291  5.65487E+04 0.00214  5.42332E+04 0.00215  6.54517E+04 0.00213  4.38600E+04 0.00213  4.07453E+04 0.00237  3.07770E+04 0.00293  2.48385E+04 0.00281  2.15095E+04 0.00274  1.90488E+04 0.00238  1.75361E+04 0.00268  1.65320E+04 0.00254  1.61598E+04 0.00348  1.38130E+04 0.00368  1.36531E+04 0.00387  1.33120E+04 0.00455  1.29455E+04 0.00270  2.48773E+04 0.00272  2.36883E+04 0.00201  1.65367E+04 0.00252  1.05672E+04 0.00390  1.14724E+04 0.00423  1.04643E+04 0.00415  9.99451E+03 0.00382  1.47597E+04 0.00280  3.64632E+03 0.00687  4.58201E+03 0.00773  4.18050E+03 0.00775  2.39141E+03 0.00654  4.22397E+03 0.00577  2.83493E+03 0.00707  2.40385E+03 0.00862  4.45527E+02 0.01205  4.45561E+02 0.01510  4.46844E+02 0.01508  4.79179E+02 0.01700  4.63877E+02 0.01426  4.63416E+02 0.01379  4.78679E+02 0.01791  4.41594E+02 0.01453  8.31687E+02 0.01436  1.35046E+03 0.00752  1.70796E+03 0.00773  4.51942E+03 0.00530  4.71035E+03 0.00491  4.89155E+03 0.00358  3.11205E+03 0.00499  2.16134E+03 0.00668  1.60265E+03 0.00655  1.80404E+03 0.00835  3.24780E+03 0.00468  4.07870E+03 0.00427  7.24320E+03 0.00427  1.01853E+04 0.00416  1.36837E+04 0.00242  8.12428E+03 0.00305  5.58715E+03 0.00387  3.86308E+03 0.00484  3.39427E+03 0.00408  3.26746E+03 0.00416  2.62913E+03 0.00508  1.74018E+03 0.00450  1.57227E+03 0.00476  1.36712E+03 0.00719  1.10935E+03 0.00640  8.37440E+02 0.00670  5.11615E+02 0.00832  1.54848E+02 0.01253 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.26275E+00 0.00104 ];

% Flux spectra in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  1.76035E+01 0.00084  2.27097E+00 0.00090 ];
INF_FISS_FLX              (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  4.27369E-01 0.00016  6.27203E-01 0.00019 ];
INF_CAPT                  (idx, [1:   4]) = [  1.93731E-02 0.00119  5.92193E-02 0.00044 ];
INF_ABS                   (idx, [1:   4]) = [  2.67801E-02 0.00096  2.20423E-01 0.00049 ];
INF_FISS                  (idx, [1:   4]) = [  7.40699E-03 0.00077  1.61204E-01 0.00052 ];
INF_NSF                   (idx, [1:   4]) = [  1.89904E-02 0.00078  3.92725E-01 0.00052 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.56385E+00 0.00011  2.43620E+00 3.8E-09 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.03472E+02 7.0E-06  2.02270E+02 0.0E+00 ];
INF_INVV                  (idx, [1:   4]) = [  5.23276E-08 0.00125  2.26126E-06 0.00046 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  4.00560E-01 0.00016  4.06576E-01 0.00060 ];
INF_SCATT1                (idx, [1:   4]) = [  4.34168E-02 0.00185  7.98929E-03 0.03242 ];
INF_SCATT2                (idx, [1:   4]) = [  2.29493E-02 0.00337  5.96119E-04 0.24293 ];
INF_SCATT3                (idx, [1:   4]) = [  1.19191E-02 0.00540 -3.58472E-05 1.00000 ];
INF_SCATT4                (idx, [1:   4]) = [  7.71216E-03 0.00691  2.32224E-05 1.00000 ];
INF_SCATT5                (idx, [1:   4]) = [  4.01743E-03 0.01128  1.41440E-04 0.86049 ];
INF_SCATT6                (idx, [1:   4]) = [  1.98677E-03 0.02358  2.97954E-06 1.00000 ];
INF_SCATT7                (idx, [1:   4]) = [  7.35904E-04 0.04920  6.78782E-05 1.00000 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  4.00669E-01 0.00017  4.06576E-01 0.00060 ];
INF_SCATTP1               (idx, [1:   4]) = [  4.34199E-02 0.00185  7.98929E-03 0.03242 ];
INF_SCATTP2               (idx, [1:   4]) = [  2.29495E-02 0.00338  5.96119E-04 0.24293 ];
INF_SCATTP3               (idx, [1:   4]) = [  1.19188E-02 0.00542 -3.58472E-05 1.00000 ];
INF_SCATTP4               (idx, [1:   4]) = [  7.71242E-03 0.00694  2.32224E-05 1.00000 ];
INF_SCATTP5               (idx, [1:   4]) = [  4.01704E-03 0.01129  1.41440E-04 0.86049 ];
INF_SCATTP6               (idx, [1:   4]) = [  1.98669E-03 0.02356  2.97954E-06 1.00000 ];
INF_SCATTP7               (idx, [1:   4]) = [  7.34823E-04 0.04932  6.78782E-05 1.00000 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  3.14084E-01 0.00049  5.96571E-01 0.00048 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.06129E+00 0.00049  5.58751E-01 0.00048 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  2.66713E-02 0.00095  2.20423E-01 0.00049 ];
INF_REMXS                 (idx, [1:   4]) = [  2.75801E-02 0.00134  2.22578E-01 0.00119 ];

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

INF_S0                    (idx, [1:   8]) = [  3.99789E-01 0.00017  7.71582E-04 0.00791  1.95180E-03 0.01404  4.04624E-01 0.00061 ];
INF_S1                    (idx, [1:   8]) = [  4.36000E-02 0.00186 -1.83215E-04 0.01826 -1.69151E-04 0.09009  8.15844E-03 0.03168 ];
INF_S2                    (idx, [1:   8]) = [  2.29646E-02 0.00337 -1.53242E-05 0.19038 -7.27829E-05 0.20207  6.68902E-04 0.21223 ];
INF_S3                    (idx, [1:   8]) = [  1.19278E-02 0.00536 -8.71983E-06 0.19811 -2.87378E-05 0.36838 -7.10933E-06 1.00000 ];
INF_S4                    (idx, [1:   8]) = [  7.71660E-03 0.00689 -4.43629E-06 0.49220 -1.53205E-06 1.00000  2.47544E-05 1.00000 ];
INF_S5                    (idx, [1:   8]) = [  4.01726E-03 0.01127  1.64805E-07 1.00000 -2.53801E-05 0.30928  1.66820E-04 0.72261 ];
INF_S6                    (idx, [1:   8]) = [  1.98858E-03 0.02357 -1.80387E-06 0.71238 -4.04069E-06 1.00000  7.02023E-06 1.00000 ];
INF_S7                    (idx, [1:   8]) = [  7.33814E-04 0.04830  2.08961E-06 0.79382  4.43389E-06 1.00000  6.34443E-05 1.00000 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  3.99897E-01 0.00017  7.71582E-04 0.00791  1.95180E-03 0.01404  4.04624E-01 0.00061 ];
INF_SP1                   (idx, [1:   8]) = [  4.36032E-02 0.00186 -1.83215E-04 0.01826 -1.69151E-04 0.09009  8.15844E-03 0.03168 ];
INF_SP2                   (idx, [1:   8]) = [  2.29648E-02 0.00338 -1.53242E-05 0.19038 -7.27829E-05 0.20207  6.68902E-04 0.21223 ];
INF_SP3                   (idx, [1:   8]) = [  1.19275E-02 0.00537 -8.71983E-06 0.19811 -2.87378E-05 0.36838 -7.10933E-06 1.00000 ];
INF_SP4                   (idx, [1:   8]) = [  7.71686E-03 0.00692 -4.43629E-06 0.49220 -1.53205E-06 1.00000  2.47544E-05 1.00000 ];
INF_SP5                   (idx, [1:   8]) = [  4.01687E-03 0.01129  1.64805E-07 1.00000 -2.53801E-05 0.30928  1.66820E-04 0.72261 ];
INF_SP6                   (idx, [1:   8]) = [  1.98849E-03 0.02355 -1.80387E-06 0.71238 -4.04069E-06 1.00000  7.02023E-06 1.00000 ];
INF_SP7                   (idx, [1:   8]) = [  7.32733E-04 0.04843  2.08961E-06 0.79382  4.43389E-06 1.00000  6.34443E-05 1.00000 ];

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

CMM_TRANSPXS              (idx, [1:   4]) = [  2.58616E-01 0.00207  8.43259E-01 0.01130 ];
CMM_TRANSPXS_X            (idx, [1:   4]) = [  2.58949E-01 0.00369  8.72157E-01 0.01886 ];
CMM_TRANSPXS_Y            (idx, [1:   4]) = [  2.57930E-01 0.00376  8.47857E-01 0.01644 ];
CMM_TRANSPXS_Z            (idx, [1:   4]) = [  2.59143E-01 0.00346  8.22022E-01 0.01643 ];
CMM_DIFFCOEF              (idx, [1:   4]) = [  1.28904E+00 0.00206  3.96504E-01 0.01131 ];
CMM_DIFFCOEF_X            (idx, [1:   4]) = [  1.28768E+00 0.00374  3.85467E-01 0.01893 ];
CMM_DIFFCOEF_Y            (idx, [1:   4]) = [  1.29279E+00 0.00383  3.95744E-01 0.01668 ];
CMM_DIFFCOEF_Z            (idx, [1:   4]) = [  1.28666E+00 0.00344  4.08301E-01 0.01752 ];

% Delayed neutron parameters (Meulekamp method):

BETA_EFF                  (idx, [1:  18]) = [  7.22833E-03 0.01621  1.90071E-04 0.11232  1.09700E-03 0.04547  6.16621E-04 0.06158  1.32561E-03 0.04193  2.20892E-03 0.03013  8.11032E-04 0.05365  6.64455E-04 0.05749  3.14607E-04 0.08699 ];
LAMBDA                    (idx, [1:  18]) = [  5.04836E-01 0.02937  1.24667E-02 0.0E+00  2.82917E-02 0.0E+00  4.25244E-02 6.0E-09  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 4.9E-09  3.55460E+00 0.0E+00 ];


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
INPUT_FILE_NAME           (idx, [1:135])  = '/home/hirepan/Documents/chalmers/Project/codes/Shynt/repo/cases/single_assem_1x1cell/serpent_files/global_cell_type3/XS_generation.serp' ;
WORKING_DIRECTORY         (idx, [1: 84])  = '/home/hirepan/Documents/chalmers/Project/codes/Shynt/repo/cases/single_assem_1x1cell' ;
HOSTNAME                  (idx, [1:  4])  = 'thor' ;
CPU_TYPE                  (idx, [1: 40])  = 'Intel(R) Core(TM) i9-10900 CPU @ 2.80GHz' ;
CPU_MHZ                   (idx, 1)        = 236.0 ;
START_DATE                (idx, [1: 24])  = 'Thu Mar 10 11:53:34 2022' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Mar 10 11:53:43 2022' ;

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
OMP_HISTORY_PROFILE       (idx, [1:  18]) = [  9.98663E-01  1.00842E+00  1.05559E+00  9.74777E-01  1.01483E+00  1.02835E+00  9.74155E-01  1.00643E+00  9.98042E-01  9.67485E-01  9.70918E-01  9.60945E-01  1.02315E+00  9.89148E-01  9.94559E-01  9.88853E-01  1.00165E+00  1.04402E+00  ];
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

MIN_MACROXS               (idx, [1:   4]) = [  5.00000E-02 4.7E-09  0.00000E+00 0.0E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  8.34161E-03 0.00279  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.91658E-01 2.3E-05  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  8.33741E-01 0.00011  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  8.34121E-01 0.00011  0.00000E+00 0.0E+00 ];
AVG_TRACKING_LOOPS        (idx, [1:   8]) = [  2.35551E+00 0.00040  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  2.69198E+01 0.00055  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  2.69198E+01 0.00055  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  5.35346E+00 0.00076  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  1.97198E-01 0.00311  0.00000E+00 0.0E+00 ];
LOST_PARTICLES            (idx, 1)        = 0 ;

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 500 ;
SIMULATED_HISTORIES       (idx, 1)        = 1000593 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  2.00119E+03 0.00145 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  2.00119E+03 0.00145 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.40337E+00 ;
RUNNING_TIME              (idx, 1)        =  1.48167E-01 ;
INIT_TIME                 (idx, [1:  2])  = [  1.19000E-02  1.19000E-02 ];
PROCESS_TIME              (idx, [1:  2])  = [  1.00001E-04  1.00001E-04 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  1.36100E-01  1.36100E-01  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  1.48050E-01  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 16.22072 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  1.77082E+01 0.00561 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  7.73903E-01 ;

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

NORM_COEF                 (idx, [1:   4]) = [  4.99787E-04 0.00082  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  6.55338E-01 0.00201 ];
U235_FISS                 (idx, [1:   4]) = [  4.54820E-01 0.00121  9.15823E-01 0.00044 ];
U238_FISS                 (idx, [1:   4]) = [  4.18232E-02 0.00509  8.41765E-02 0.00478 ];
U235_CAPT                 (idx, [1:   4]) = [  1.06303E-01 0.00312  2.10544E-01 0.00274 ];
U238_CAPT                 (idx, [1:   4]) = [  3.67507E-01 0.00157  7.27984E-01 0.00087 ];

% Neutron balance (particles/weight):

BALA_SRC_NEUTRON_SRC     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_FISS    (idx, [1:  2])  = [ 1000593 1.00000E+06 ];
BALA_SRC_NEUTRON_NXN     (idx, [1:  2])  = [ 0 1.91611E+03 ];
BALA_SRC_NEUTRON_VR      (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_TOT     (idx, [1:  2])  = [ 1000593 1.00192E+06 ];

BALA_LOSS_NEUTRON_CAPT    (idx, [1:  2])  = [ 504326 5.05033E+05 ];
BALA_LOSS_NEUTRON_FISS    (idx, [1:  2])  = [ 496267 4.96883E+05 ];
BALA_LOSS_NEUTRON_LEAK    (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_CUT     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_ERR     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_TOT     (idx, [1:  2])  = [ 1000593 1.00192E+06 ];

BALA_NEUTRON_DIFF         (idx, [1:  2])  = [ 0 -1.04774E-09 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.61083E-11 0.00053 ];
TOT_POWDENS               (idx, [1:   2]) = [  2.96937E-15 0.00053 ];
TOT_GENRATE               (idx, [1:   2]) = [  1.22569E+00 0.00052 ];
TOT_FISSRATE              (idx, [1:   2]) = [  4.96283E-01 0.00053 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  5.03717E-01 0.00052 ];
TOT_ABSRATE               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.99574E-01 0.00082 ];
TOT_FLUX                  (idx, [1:   2]) = [  5.65290E+01 0.00067 ];
TOT_PHOTON_PRODRATE       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  2.69545E+01 0.00053 ];
INI_FMASS                 (idx, 1)        =  5.42481E-03 ;
TOT_FMASS                 (idx, 1)        =  5.42481E-03 ;

% Six-factor formula:

SIX_FF_ETA                (idx, [1:   2]) = [  1.78163E+00 0.00087 ];
SIX_FF_F                  (idx, [1:   2]) = [  9.55739E-01 0.00029 ];
SIX_FF_P                  (idx, [1:   2]) = [  5.24457E-01 0.00096 ];
SIX_FF_EPSILON            (idx, [1:   2]) = [  1.37474E+00 0.00088 ];
SIX_FF_LF                 (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
SIX_FF_LT                 (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
SIX_FF_KINF               (idx, [1:   2]) = [  1.22721E+00 0.00098 ];
SIX_FF_KEFF               (idx, [1:   2]) = [  1.22721E+00 0.00098 ];

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.46974E+00 3.4E-05 ];
FISSE                     (idx, [1:   2]) = [  2.02586E+02 2.9E-06 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.22698E+00 0.00102  1.21848E+00 0.00100  8.72621E-03 0.01541 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.22808E+00 0.00053 ];
COL_KEFF                  (idx, [1:   2]) = [  1.22670E+00 0.00110 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.22808E+00 0.00053 ];
ABS_KINF                  (idx, [1:   2]) = [  1.22808E+00 0.00053 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% ALF (Average lethargy of neutrons causing fission):
% Based on E0 = 2.000000E+01 MeV

ANA_ALF                   (idx, [1:   2]) = [  1.67128E+01 0.00047 ];
IMP_ALF                   (idx, [1:   2]) = [  1.67055E+01 0.00023 ];

% EALF (Energy corresponding to average lethargy of neutrons causing fission):

ANA_EALF                  (idx, [1:   2]) = [  1.12093E-06 0.00802 ];
IMP_EALF                  (idx, [1:   2]) = [  1.11579E-06 0.00393 ];

% AFGE (Average energy of neutrons causing fission):

ANA_AFGE                  (idx, [1:   2]) = [  2.82914E-01 0.00522 ];
IMP_AFGE                  (idx, [1:   2]) = [  2.82417E-01 0.00231 ];

% Forward-weighted delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
FWD_ANA_BETA_ZERO         (idx, [1:  18]) = [  6.14629E-03 0.01139  1.61685E-04 0.07150  9.00953E-04 0.03044  4.97308E-04 0.03977  1.15062E-03 0.02607  1.92799E-03 0.01903  6.93948E-04 0.03518  5.65561E-04 0.03838  2.48234E-04 0.05710 ];
FWD_ANA_LAMBDA            (idx, [1:  18]) = [  4.93121E-01 0.01869  4.01428E-03 0.06496  2.53494E-02 0.01525  2.98521E-02 0.02917  1.25858E-01 0.01070  2.90712E-01 0.00348  5.57184E-01 0.01983  1.22936E+00 0.02571  1.62801E+00 0.04870 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  18]) = [  7.22833E-03 0.01621  1.90071E-04 0.11232  1.09700E-03 0.04547  6.16621E-04 0.06158  1.32561E-03 0.04193  2.20892E-03 0.03013  8.11032E-04 0.05365  6.64455E-04 0.05749  3.14607E-04 0.08699 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  18]) = [  5.04836E-01 0.02937  1.24667E-02 0.0E+00  2.82917E-02 0.0E+00  4.25244E-02 6.0E-09  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 4.9E-09  3.55460E+00 0.0E+00 ];

% Adjoint weighted time constants using Nauchi's method:

IFP_CHAIN_LENGTH          (idx, 1)        = 15 ;
ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  2.07760E-05 0.00238  2.07561E-05 0.00239  2.37254E-05 0.02386 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  2.54762E-05 0.00205  2.54519E-05 0.00207  2.90834E-05 0.02388 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  18]) = [  7.14600E-03 0.01553  1.85291E-04 0.10876  1.02514E-03 0.04300  6.27096E-04 0.05636  1.32204E-03 0.03697  2.15559E-03 0.02996  8.55387E-04 0.04655  6.52691E-04 0.05439  3.22763E-04 0.07746 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  18]) = [  5.14783E-01 0.02811  1.24667E-02 0.0E+00  2.82917E-02 2.6E-09  4.25244E-02 8.1E-09  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 5.5E-09  3.55460E+00 4.6E-09 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  2.09049E-05 0.00497  2.08921E-05 0.00500  1.68649E-05 0.05556 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  2.56406E-05 0.00493  2.56250E-05 0.00495  2.06620E-05 0.05540 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  18]) = [  7.28707E-03 0.04731  1.10613E-04 0.38052  1.27976E-03 0.12997  6.76923E-04 0.16482  1.09021E-03 0.12372  2.05457E-03 0.09107  8.33433E-04 0.14951  9.27479E-04 0.17432  3.14077E-04 0.22831 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  18]) = [  5.36213E-01 0.06570  1.24667E-02 2.7E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 3.5E-09  2.92467E-01 5.0E-09  6.66488E-01 4.6E-09  1.63478E+00 0.0E+00  3.55460E+00 7.1E-09 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  18]) = [  7.32819E-03 0.04554  1.11014E-04 0.33599  1.23447E-03 0.12595  6.88807E-04 0.15852  1.14651E-03 0.12361  2.05331E-03 0.08899  8.58028E-04 0.14874  8.97515E-04 0.16398  3.38541E-04 0.21300 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  18]) = [  5.37558E-01 0.06493  1.24667E-02 4.7E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 3.2E-09  2.92467E-01 4.9E-09  6.66488E-01 4.6E-09  1.63478E+00 0.0E+00  3.55460E+00 6.5E-09 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -3.51963E+02 0.04704 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  2.08640E-05 0.00142 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  2.55871E-05 0.00105 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  7.06845E-03 0.00875 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -3.39355E+02 0.00900 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  3.26797E-07 0.00120 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  4.19112E-06 0.00100  4.19116E-06 0.00100  4.21402E-06 0.01320 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.01428E-05 0.00137  3.01404E-05 0.00137  3.06214E-05 0.01601 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.25039E-01 0.00096  5.24157E-01 0.00097  7.19462E-01 0.02301 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.18408E+01 0.02567 ];
ANA_MEAN_NCOL             (idx, [1:   4]) = [  2.69198E+01 0.00055  3.02959E+01 0.00076 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  7])  = 'u4gcu_2' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  2.00000E+01  6.06550E+00  3.67900E+00  2.23100E+00  1.35300E+00  8.21000E-01  5.00000E-01  3.02500E-01  1.83000E-01  1.11000E-01  6.74300E-02  4.08500E-02  2.47800E-02  1.50300E-02  9.11800E-03  5.50000E-03  3.51910E-03  2.23945E-03  1.42510E-03  9.06898E-04  3.67262E-04  1.48728E-04  7.55014E-05  4.80520E-05  2.77000E-05  1.59680E-05  9.87700E-06  4.00000E-06  3.30000E-06  2.60000E-06  2.10000E-06  1.85500E-06  1.50000E-06  1.30000E-06  1.15000E-06  1.12300E-06  1.09700E-06  1.07100E-06  1.04500E-06  1.02000E-06  9.96000E-07  9.72000E-07  9.50000E-07  9.10000E-07  8.50000E-07  7.80000E-07  6.25000E-07  5.00000E-07  4.00000E-07  3.50000E-07  3.20000E-07  3.00000E-07  2.80000E-07  2.50000E-07  2.20000E-07  1.80000E-07  1.40000E-07  1.00000E-07  8.00000E-08  6.70000E-08  5.80000E-08  5.00000E-08  4.20000E-08  3.50000E-08  3.00000E-08  2.50000E-08  2.00000E-08  1.50000E-08  1.00000E-08  5.00000E-09  1.00000E-11 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Micro-group spectrum:

INF_MICRO_FLX             (idx, [1: 140]) = [  1.07344E+04 0.01094  4.50545E+04 0.00456  9.48003E+04 0.00282  1.00258E+05 0.00187  9.56590E+04 0.00167  1.14641E+05 0.00172  7.79627E+04 0.00133  7.22643E+04 0.00143  5.53458E+04 0.00160  4.51838E+04 0.00146  3.91359E+04 0.00152  3.51048E+04 0.00165  3.24732E+04 0.00198  3.06871E+04 0.00165  2.99281E+04 0.00174  2.56781E+04 0.00185  2.54415E+04 0.00164  2.49856E+04 0.00117  2.43832E+04 0.00159  4.70318E+04 0.00120  4.50219E+04 0.00143  3.17314E+04 0.00139  2.02228E+04 0.00173  2.28202E+04 0.00196  2.10472E+04 0.00193  1.89251E+04 0.00198  2.99073E+04 0.00175  6.80108E+03 0.00341  8.52347E+03 0.00268  7.73260E+03 0.00341  4.49101E+03 0.00356  7.81927E+03 0.00284  5.29847E+03 0.00302  4.49076E+03 0.00260  8.43415E+02 0.00910  8.45317E+02 0.00776  8.70369E+02 0.00859  8.81857E+02 0.00672  8.97133E+02 0.00569  8.75503E+02 0.00878  9.05356E+02 0.00663  8.55252E+02 0.00812  1.60004E+03 0.00547  2.56460E+03 0.00544  3.23736E+03 0.00503  8.50999E+03 0.00288  8.85648E+03 0.00276  9.27600E+03 0.00292  5.94522E+03 0.00433  4.20851E+03 0.00392  3.13629E+03 0.00524  3.52725E+03 0.00484  6.31810E+03 0.00307  7.96703E+03 0.00331  1.40747E+04 0.00253  1.97594E+04 0.00219  2.71012E+04 0.00206  1.64088E+04 0.00268  1.13623E+04 0.00226  8.00734E+03 0.00206  7.09044E+03 0.00260  6.90527E+03 0.00254  5.65483E+03 0.00280  3.82644E+03 0.00233  3.51138E+03 0.00300  3.10018E+03 0.00393  2.60269E+03 0.00456  2.04780E+03 0.00388  1.38847E+03 0.00470  5.05853E+02 0.00648 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];

% Flux spectra in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  3.20981E+01 0.00082  4.56253E+00 0.00112 ];
INF_FISS_FLX              (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  4.05622E-01 0.00034  1.09409E+00 0.00024 ];
INF_CAPT                  (idx, [1:   4]) = [  1.61322E-04 0.00157  5.07465E-03 0.00041 ];
INF_ABS                   (idx, [1:   4]) = [  1.61322E-04 0.00157  5.07465E-03 0.00041 ];
INF_FISS                  (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_NSF                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_NUBAR                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_KAPPA                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_INVV                  (idx, [1:   4]) = [  5.46968E-08 0.00094  2.33741E-06 0.00041 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  4.05456E-01 0.00034  1.08900E+00 0.00024 ];
INF_SCATT1                (idx, [1:   4]) = [  2.37124E-01 0.00038  3.31444E-01 0.00088 ];
INF_SCATT2                (idx, [1:   4]) = [  9.06850E-02 0.00063  8.47688E-02 0.00220 ];
INF_SCATT3                (idx, [1:   4]) = [  2.79043E-03 0.01489  2.57964E-02 0.00743 ];
INF_SCATT4                (idx, [1:   4]) = [ -1.38587E-02 0.00215 -5.60969E-03 0.03506 ];
INF_SCATT5                (idx, [1:   4]) = [ -1.19261E-03 0.02734  4.74743E-03 0.03736 ];
INF_SCATT6                (idx, [1:   4]) = [  4.67889E-03 0.00771 -1.22560E-02 0.01056 ];
INF_SCATT7                (idx, [1:   4]) = [  4.16447E-04 0.08121 -5.79553E-04 0.31276 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  4.05456E-01 0.00034  1.08900E+00 0.00024 ];
INF_SCATTP1               (idx, [1:   4]) = [  2.37124E-01 0.00038  3.31444E-01 0.00088 ];
INF_SCATTP2               (idx, [1:   4]) = [  9.06850E-02 0.00063  8.47688E-02 0.00220 ];
INF_SCATTP3               (idx, [1:   4]) = [  2.79043E-03 0.01489  2.57964E-02 0.00743 ];
INF_SCATTP4               (idx, [1:   4]) = [ -1.38587E-02 0.00215 -5.60969E-03 0.03506 ];
INF_SCATTP5               (idx, [1:   4]) = [ -1.19261E-03 0.02734  4.74743E-03 0.03736 ];
INF_SCATTP6               (idx, [1:   4]) = [  4.67889E-03 0.00771 -1.22560E-02 0.01056 ];
INF_SCATTP7               (idx, [1:   4]) = [  4.16447E-04 0.08121 -5.79553E-04 0.31276 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  1.06844E-01 0.00100  6.52890E-01 0.00064 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  3.11989E+00 0.00101  5.10556E-01 0.00064 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  1.61322E-04 0.00157  5.07465E-03 0.00041 ];
INF_REMXS                 (idx, [1:   4]) = [  1.64114E-02 0.00086  6.47976E-03 0.00697 ];

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

INF_S0                    (idx, [1:   8]) = [  3.89210E-01 0.00034  1.62453E-02 0.00089  1.39402E-03 0.01285  1.08761E+00 0.00024 ];
INF_S1                    (idx, [1:   8]) = [  2.32277E-01 0.00039  4.84694E-03 0.00188  8.75629E-04 0.01402  3.30568E-01 0.00089 ];
INF_S2                    (idx, [1:   8]) = [  9.21242E-02 0.00061 -1.43920E-03 0.00614  4.69319E-04 0.01662  8.42995E-02 0.00218 ];
INF_S3                    (idx, [1:   8]) = [  4.48715E-03 0.00880 -1.69672E-03 0.00382  1.64022E-04 0.03764  2.56324E-02 0.00742 ];
INF_S4                    (idx, [1:   8]) = [ -1.33035E-02 0.00218 -5.55187E-04 0.01132 -2.72863E-06 1.00000 -5.60696E-03 0.03473 ];
INF_S5                    (idx, [1:   8]) = [ -1.21581E-03 0.02541  2.32052E-05 0.25897 -6.62104E-05 0.07435  4.81364E-03 0.03698 ];
INF_S6                    (idx, [1:   8]) = [  4.80257E-03 0.00765 -1.23676E-04 0.04282 -8.83471E-05 0.04549 -1.21677E-02 0.01058 ];
INF_S7                    (idx, [1:   8]) = [  5.70269E-04 0.05968 -1.53823E-04 0.04151 -8.25761E-05 0.04930 -4.96977E-04 0.36336 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  3.89210E-01 0.00034  1.62453E-02 0.00089  1.39402E-03 0.01285  1.08761E+00 0.00024 ];
INF_SP1                   (idx, [1:   8]) = [  2.32277E-01 0.00039  4.84694E-03 0.00188  8.75629E-04 0.01402  3.30568E-01 0.00089 ];
INF_SP2                   (idx, [1:   8]) = [  9.21242E-02 0.00061 -1.43920E-03 0.00614  4.69319E-04 0.01662  8.42995E-02 0.00218 ];
INF_SP3                   (idx, [1:   8]) = [  4.48715E-03 0.00880 -1.69672E-03 0.00382  1.64022E-04 0.03764  2.56324E-02 0.00742 ];
INF_SP4                   (idx, [1:   8]) = [ -1.33035E-02 0.00218 -5.55187E-04 0.01132 -2.72863E-06 1.00000 -5.60696E-03 0.03473 ];
INF_SP5                   (idx, [1:   8]) = [ -1.21581E-03 0.02541  2.32052E-05 0.25897 -6.62104E-05 0.07435  4.81364E-03 0.03698 ];
INF_SP6                   (idx, [1:   8]) = [  4.80257E-03 0.00765 -1.23676E-04 0.04282 -8.83471E-05 0.04549 -1.21677E-02 0.01058 ];
INF_SP7                   (idx, [1:   8]) = [  5.70269E-04 0.05968 -1.53823E-04 0.04151 -8.25761E-05 0.04930 -4.96977E-04 0.36336 ];

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

CMM_TRANSPXS              (idx, [1:   4]) = [  1.23285E-01 0.00100  3.91531E-01 0.00590 ];
CMM_TRANSPXS_X            (idx, [1:   4]) = [  1.23446E-01 0.00193  3.92191E-01 0.01027 ];
CMM_TRANSPXS_Y            (idx, [1:   4]) = [  1.23078E-01 0.00168  3.93194E-01 0.00892 ];
CMM_TRANSPXS_Z            (idx, [1:   4]) = [  1.23351E-01 0.00156  3.90732E-01 0.00933 ];
CMM_DIFFCOEF              (idx, [1:   4]) = [  2.70382E+00 0.00100  8.52063E-01 0.00584 ];
CMM_DIFFCOEF_X            (idx, [1:   4]) = [  2.70047E+00 0.00193  8.51938E-01 0.00962 ];
CMM_DIFFCOEF_Y            (idx, [1:   4]) = [  2.70850E+00 0.00168  8.49368E-01 0.00888 ];
CMM_DIFFCOEF_Z            (idx, [1:   4]) = [  2.70248E+00 0.00156  8.54883E-01 0.00934 ];

% Delayed neutron parameters (Meulekamp method):

BETA_EFF                  (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
LAMBDA                    (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

