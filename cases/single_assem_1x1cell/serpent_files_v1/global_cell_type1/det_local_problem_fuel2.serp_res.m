
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
INPUT_FILE_NAME           (idx, [1:145])  = '/home/hirepan/Documents/chalmers/Project/codes/Shynt/repo/cases/single_assem_1x1cell/serpent_files/global_cell_type1/det_local_problem_fuel2.serp' ;
WORKING_DIRECTORY         (idx, [1: 84])  = '/home/hirepan/Documents/chalmers/Project/codes/Shynt/repo/cases/single_assem_1x1cell' ;
HOSTNAME                  (idx, [1:  4])  = 'thor' ;
CPU_TYPE                  (idx, [1: 40])  = 'Intel(R) Core(TM) i9-10900 CPU @ 2.80GHz' ;
CPU_MHZ                   (idx, 1)        = 236.0 ;
START_DATE                (idx, [1: 24])  = 'Thu Mar 10 11:42:17 2022' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Mar 10 11:42:41 2022' ;

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
OMP_HISTORY_PROFILE       (idx, [1:  18]) = [  9.99200E-01  9.49973E-01  9.86104E-01  9.56284E-01  9.55319E-01  9.73777E-01  9.53341E-01  9.46344E-01  1.04092E+00  1.15210E+00  1.25485E+00  9.53390E-01  9.48420E-01  9.46834E-01  9.47063E-01  9.48093E-01  1.13192E+00  9.56071E-01  ];
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
ST_FRAC                   (idx, [1:   4]) = [  2.18004E-03 0.00301  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.97820E-01 6.6E-06  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  8.26458E-01 8.3E-05  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  8.31961E-01 0.00010  0.00000E+00 0.0E+00 ];
AVG_TRACKING_LOOPS        (idx, [1:   8]) = [  4.89599E+00 0.00095  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  2.82369E+01 0.00057  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  2.82369E+01 0.00057  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  5.70336E+00 0.00079  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  4.49714E+01 0.00053  0.00000E+00 0.0E+00 ];
LOST_PARTICLES            (idx, 1)        = 0 ;

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 500 ;
SIMULATED_HISTORIES       (idx, 1)        = 1000486 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  2.00097E+03 0.00153 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  2.00097E+03 0.00153 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  7.08841E+00 ;
RUNNING_TIME              (idx, 1)        =  4.05917E-01 ;
INIT_TIME                 (idx, [1:  2])  = [  1.16333E-02  1.16333E-02 ];
PROCESS_TIME              (idx, [1:  2])  = [  1.00001E-04  1.16666E-04 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  3.94100E-01  3.94100E-01  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  4.05833E-01  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 17.46272 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  1.79583E+01 0.00180 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  9.49456E-01 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 64024.21 ;
ALLOC_MEMSIZE             (idx, 1)        = 390.08;
MEMSIZE                   (idx, 1)        = 203.14;
XS_MEMSIZE                (idx, 1)        = 74.10;
MAT_MEMSIZE               (idx, 1)        = 6.90;
RES_MEMSIZE               (idx, 1)        = 1.55;
IFC_MEMSIZE               (idx, 1)        = 0.00;
MISC_MEMSIZE              (idx, 1)        = 120.59;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 186.94;

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

NORM_COEF                 (idx, [1:   4]) = [  4.99008E-04 0.00082  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  7.24531E-01 0.00210 ];
U235_FISS                 (idx, [1:   4]) = [  4.36437E-01 0.00123  9.12166E-01 0.00045 ];
U238_FISS                 (idx, [1:   4]) = [  4.20458E-02 0.00501  8.78335E-02 0.00469 ];
U235_CAPT                 (idx, [1:   4]) = [  9.86774E-02 0.00305  1.89227E-01 0.00281 ];
U238_CAPT                 (idx, [1:   4]) = [  3.87438E-01 0.00157  7.42891E-01 0.00079 ];

% Neutron balance (particles/weight):

BALA_SRC_NEUTRON_SRC     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_FISS    (idx, [1:  2])  = [ 1000486 1.00000E+06 ];
BALA_SRC_NEUTRON_NXN     (idx, [1:  2])  = [ 0 1.99994E+03 ];
BALA_SRC_NEUTRON_VR      (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_TOT     (idx, [1:  2])  = [ 1000486 1.00200E+06 ];

BALA_LOSS_NEUTRON_CAPT    (idx, [1:  2])  = [ 521708 5.22531E+05 ];
BALA_LOSS_NEUTRON_FISS    (idx, [1:  2])  = [ 478778 4.79469E+05 ];
BALA_LOSS_NEUTRON_LEAK    (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_CUT     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_ERR     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_TOT     (idx, [1:  2])  = [ 1000486 1.00200E+06 ];

BALA_NEUTRON_DIFF         (idx, [1:  2])  = [ 0 -5.82077E-10 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.55264E-11 0.00052 ];
TOT_POWDENS               (idx, [1:   2]) = [  2.86210E-15 0.00052 ];
TOT_GENRATE               (idx, [1:   2]) = [  1.18184E+00 0.00052 ];
TOT_FISSRATE              (idx, [1:   2]) = [  4.78324E-01 0.00052 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  5.21676E-01 0.00048 ];
TOT_ABSRATE               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.98017E-01 0.00082 ];
TOT_FLUX                  (idx, [1:   2]) = [  5.79995E+01 0.00065 ];
TOT_PHOTON_PRODRATE       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  2.82314E+01 0.00052 ];
INI_FMASS                 (idx, 1)        =  5.42481E-03 ;
TOT_FMASS                 (idx, 1)        =  5.42481E-03 ;

% Six-factor formula:

SIX_FF_ETA                (idx, [1:   2]) = [  1.72368E+00 0.00086 ];
SIX_FF_F                  (idx, [1:   2]) = [  9.49042E-01 0.00032 ];
SIX_FF_P                  (idx, [1:   2]) = [  5.41714E-01 0.00088 ];
SIX_FF_EPSILON            (idx, [1:   2]) = [  1.33728E+00 0.00086 ];
SIX_FF_LF                 (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
SIX_FF_LT                 (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
SIX_FF_KINF               (idx, [1:   2]) = [  1.18468E+00 0.00105 ];
SIX_FF_KEFF               (idx, [1:   2]) = [  1.18468E+00 0.00105 ];

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.47080E+00 3.7E-05 ];
FISSE                     (idx, [1:   2]) = [  2.02599E+02 3.3E-06 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.18451E+00 0.00107  1.17621E+00 0.00106  8.46803E-03 0.01623 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.18418E+00 0.00052 ];
COL_KEFF                  (idx, [1:   2]) = [  1.18465E+00 0.00108 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.18418E+00 0.00052 ];
ABS_KINF                  (idx, [1:   2]) = [  1.18418E+00 0.00052 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% ALF (Average lethargy of neutrons causing fission):
% Based on E0 = 2.000000E+01 MeV

ANA_ALF                   (idx, [1:   2]) = [  1.68578E+01 0.00047 ];
IMP_ALF                   (idx, [1:   2]) = [  1.68607E+01 0.00024 ];

% EALF (Energy corresponding to average lethargy of neutrons causing fission):

ANA_EALF                  (idx, [1:   2]) = [  9.69963E-07 0.00812 ];
IMP_EALF                  (idx, [1:   2]) = [  9.55791E-07 0.00415 ];

% AFGE (Average energy of neutrons causing fission):

ANA_AFGE                  (idx, [1:   2]) = [  2.90398E-01 0.00517 ];
IMP_AFGE                  (idx, [1:   2]) = [  2.90153E-01 0.00246 ];

% Forward-weighted delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
FWD_ANA_BETA_ZERO         (idx, [1:  18]) = [  6.52645E-03 0.01147  1.90041E-04 0.06892  9.18030E-04 0.03217  5.46433E-04 0.03841  1.21015E-03 0.02504  2.11660E-03 0.02030  7.15021E-04 0.03670  5.83013E-04 0.03637  2.47158E-04 0.06034 ];
FWD_ANA_LAMBDA            (idx, [1:  18]) = [  4.82783E-01 0.01919  4.46308E-03 0.05995  2.45572E-02 0.01746  3.02774E-02 0.02847  1.27720E-01 0.00914  2.91297E-01 0.00284  5.34523E-01 0.02224  1.25224E+00 0.02474  1.54270E+00 0.05112 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  18]) = [  7.30577E-03 0.01795  2.29566E-04 0.10440  1.01114E-03 0.04916  6.42791E-04 0.06306  1.32243E-03 0.03840  2.36933E-03 0.03092  8.10930E-04 0.05523  6.41079E-04 0.05614  2.78493E-04 0.09674 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  18]) = [  4.86019E-01 0.03004  1.24667E-02 0.0E+00  2.82917E-02 0.0E+00  4.25244E-02 5.9E-09  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 4.9E-09  3.55460E+00 0.0E+00 ];

% Adjoint weighted time constants using Nauchi's method:

IFP_CHAIN_LENGTH          (idx, 1)        = 15 ;
ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  2.54298E-05 0.00243  2.54103E-05 0.00244  2.74062E-05 0.02380 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  3.01014E-05 0.00207  3.00784E-05 0.00209  3.24402E-05 0.02374 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  18]) = [  7.14522E-03 0.01650  1.84621E-04 0.10624  1.04050E-03 0.04685  6.44239E-04 0.05804  1.32105E-03 0.03860  2.30400E-03 0.03057  7.22112E-04 0.05430  6.33574E-04 0.05548  2.95128E-04 0.08454 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  18]) = [  4.91713E-01 0.03233  1.24667E-02 0.0E+00  2.82917E-02 4.3E-09  4.25244E-02 8.2E-09  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 5.5E-09  3.55460E+00 4.8E-09 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  2.54576E-05 0.00502  2.54551E-05 0.00505  1.83089E-05 0.05993 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  3.01323E-05 0.00484  3.01287E-05 0.00487  2.17038E-05 0.06009 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  18]) = [  6.98090E-03 0.05008  2.05421E-04 0.27980  8.65251E-04 0.14400  5.33497E-04 0.17971  1.38376E-03 0.12069  2.40134E-03 0.08602  7.88342E-04 0.14924  5.83126E-04 0.18024  2.20168E-04 0.27932 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  18]) = [  4.73202E-01 0.07749  1.24667E-02 3.8E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 3.2E-09  2.92467E-01 5.6E-09  6.66488E-01 3.3E-09  1.63478E+00 0.0E+00  3.55460E+00 3.8E-09 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  18]) = [  6.86978E-03 0.04893  1.91473E-04 0.28022  8.53105E-04 0.13831  4.96475E-04 0.18045  1.32843E-03 0.11718  2.44041E-03 0.08170  7.59081E-04 0.15128  5.80307E-04 0.17000  2.20496E-04 0.27687 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  18]) = [  4.79178E-01 0.07735  1.24667E-02 6.1E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 3.2E-09  2.92467E-01 5.7E-09  6.66488E-01 3.3E-09  1.63478E+00 1.9E-09  3.55460E+00 2.7E-09 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -2.77302E+02 0.05141 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  2.54393E-05 0.00146 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  3.01162E-05 0.00102 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  7.12098E-03 0.00995 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -2.80485E+02 0.01028 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  3.77204E-07 0.00114 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  4.23946E-06 0.00098  4.23988E-06 0.00099  4.20998E-06 0.01194 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.53993E-05 0.00135  3.54001E-05 0.00135  3.50995E-05 0.01584 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.42229E-01 0.00087  5.41381E-01 0.00088  7.20792E-01 0.02055 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.21299E+01 0.02788 ];
ANA_MEAN_NCOL             (idx, [1:   4]) = [  2.82369E+01 0.00057  3.20166E+01 0.00080 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  1])  = '0' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  2.00000E+01  6.06550E+00  3.67900E+00  2.23100E+00  1.35300E+00  8.21000E-01  5.00000E-01  3.02500E-01  1.83000E-01  1.11000E-01  6.74300E-02  4.08500E-02  2.47800E-02  1.50300E-02  9.11800E-03  5.50000E-03  3.51910E-03  2.23945E-03  1.42510E-03  9.06898E-04  3.67262E-04  1.48728E-04  7.55014E-05  4.80520E-05  2.77000E-05  1.59680E-05  9.87700E-06  4.00000E-06  3.30000E-06  2.60000E-06  2.10000E-06  1.85500E-06  1.50000E-06  1.30000E-06  1.15000E-06  1.12300E-06  1.09700E-06  1.07100E-06  1.04500E-06  1.02000E-06  9.96000E-07  9.72000E-07  9.50000E-07  9.10000E-07  8.50000E-07  7.80000E-07  6.25000E-07  5.00000E-07  4.00000E-07  3.50000E-07  3.20000E-07  3.00000E-07  2.80000E-07  2.50000E-07  2.20000E-07  1.80000E-07  1.40000E-07  1.00000E-07  8.00000E-08  6.70000E-08  5.80000E-08  5.00000E-08  4.20000E-08  3.50000E-08  3.00000E-08  2.50000E-08  2.00000E-08  1.50000E-08  1.00000E-08  5.00000E-09  1.00000E-11 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Micro-group spectrum:

INF_MICRO_FLX             (idx, [1: 140]) = [  1.70663E+04 0.00820  6.98306E+04 0.00386  1.48438E+05 0.00218  1.56643E+05 0.00138  1.49802E+05 0.00166  1.80491E+05 0.00166  1.22025E+05 0.00176  1.13220E+05 0.00180  8.61973E+04 0.00146  7.01515E+04 0.00165  6.07350E+04 0.00171  5.42902E+04 0.00152  5.02223E+04 0.00181  4.76055E+04 0.00160  4.62288E+04 0.00212  3.96749E+04 0.00159  3.92466E+04 0.00211  3.85908E+04 0.00162  3.74553E+04 0.00186  7.26367E+04 0.00131  6.92170E+04 0.00111  4.88086E+04 0.00186  3.12707E+04 0.00186  3.49341E+04 0.00189  3.22469E+04 0.00183  2.96864E+04 0.00179  4.59901E+04 0.00165  1.06398E+04 0.00270  1.34223E+04 0.00291  1.22608E+04 0.00370  7.12015E+03 0.00411  1.23775E+04 0.00329  8.37428E+03 0.00359  7.13179E+03 0.00416  1.32285E+03 0.00667  1.33984E+03 0.00784  1.37877E+03 0.00725  1.40595E+03 0.00792  1.39538E+03 0.00774  1.38890E+03 0.00847  1.42763E+03 0.00736  1.36301E+03 0.00612  2.55134E+03 0.00536  4.05836E+03 0.00605  5.12785E+03 0.00553  1.36075E+04 0.00410  1.42080E+04 0.00252  1.51017E+04 0.00262  9.77404E+03 0.00277  6.96828E+03 0.00234  5.27311E+03 0.00447  5.97162E+03 0.00382  1.08155E+04 0.00323  1.37865E+04 0.00255  2.49147E+04 0.00225  3.55511E+04 0.00199  4.93512E+04 0.00195  3.01258E+04 0.00211  2.09736E+04 0.00263  1.48117E+04 0.00294  1.30813E+04 0.00255  1.26897E+04 0.00268  1.04593E+04 0.00296  6.96311E+03 0.00292  6.38912E+03 0.00318  5.61507E+03 0.00318  4.69703E+03 0.00256  3.67439E+03 0.00255  2.42663E+03 0.00441  8.43330E+02 0.00396 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.18469E+00 0.00108 ];

% Flux spectra in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  4.99107E+01 0.00094  8.09539E+00 0.00075 ];
INF_FISS_FLX              (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  4.13930E-01 0.00023  9.35929E-01 0.00018 ];
INF_CAPT                  (idx, [1:   4]) = [  6.89516E-03 0.00108  2.19475E-02 0.00059 ];
INF_ABS                   (idx, [1:   4]) = [  9.20797E-03 0.00084  6.67970E-02 0.00072 ];
INF_FISS                  (idx, [1:   4]) = [  2.31280E-03 0.00096  4.48495E-02 0.00078 ];
INF_NSF                   (idx, [1:   4]) = [  5.96595E-03 0.00093  1.09262E-01 0.00078 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.57953E+00 0.00012  2.43620E+00 2.7E-09 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.03633E+02 9.4E-06  2.02270E+02 5.4E-09 ];
INF_INVV                  (idx, [1:   4]) = [  5.50395E-08 0.00095  2.36360E-06 0.00024 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  4.04727E-01 0.00023  8.69145E-01 0.00023 ];
INF_SCATT1                (idx, [1:   4]) = [  1.68989E-01 0.00041  2.22681E-01 0.00074 ];
INF_SCATT2                (idx, [1:   4]) = [  6.69221E-02 0.00077  5.58904E-02 0.00236 ];
INF_SCATT3                (idx, [1:   4]) = [  6.08701E-03 0.00643  1.70319E-02 0.00820 ];
INF_SCATT4                (idx, [1:   4]) = [ -6.24345E-03 0.00687 -3.83284E-03 0.02595 ];
INF_SCATT5                (idx, [1:   4]) = [  6.31117E-04 0.05315  3.18800E-03 0.01725 ];
INF_SCATT6                (idx, [1:   4]) = [  3.75026E-03 0.00596 -8.24719E-03 0.00796 ];
INF_SCATT7                (idx, [1:   4]) = [  6.11923E-04 0.03116 -1.59442E-04 0.58372 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  4.04767E-01 0.00023  8.69145E-01 0.00023 ];
INF_SCATTP1               (idx, [1:   4]) = [  1.68990E-01 0.00041  2.22681E-01 0.00074 ];
INF_SCATTP2               (idx, [1:   4]) = [  6.69221E-02 0.00077  5.58904E-02 0.00236 ];
INF_SCATTP3               (idx, [1:   4]) = [  6.08729E-03 0.00642  1.70319E-02 0.00820 ];
INF_SCATTP4               (idx, [1:   4]) = [ -6.24338E-03 0.00688 -3.83284E-03 0.02595 ];
INF_SCATTP5               (idx, [1:   4]) = [  6.31171E-04 0.05319  3.18800E-03 0.01725 ];
INF_SCATTP6               (idx, [1:   4]) = [  3.75062E-03 0.00594 -8.24719E-03 0.00796 ];
INF_SCATTP7               (idx, [1:   4]) = [  6.11652E-04 0.03113 -1.59442E-04 0.58372 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  1.85276E-01 0.00051  6.37595E-01 0.00028 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.79912E+00 0.00051  5.22799E-01 0.00028 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  9.16798E-03 0.00083  6.67970E-02 0.00072 ];
INF_REMXS                 (idx, [1:   4]) = [  2.02621E-02 0.00057  6.81812E-02 0.00081 ];

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

INF_S0                    (idx, [1:   8]) = [  3.93668E-01 0.00023  1.10589E-02 0.00089  1.39749E-03 0.00945  8.67748E-01 0.00023 ];
INF_S1                    (idx, [1:   8]) = [  1.65827E-01 0.00042  3.16294E-03 0.00216  4.63843E-04 0.01562  2.22217E-01 0.00075 ];
INF_S2                    (idx, [1:   8]) = [  6.78743E-02 0.00078 -9.52192E-04 0.00511  2.56376E-04 0.02118  5.56341E-02 0.00234 ];
INF_S3                    (idx, [1:   8]) = [  7.21000E-03 0.00554 -1.12299E-03 0.00457  8.84704E-05 0.06496  1.69434E-02 0.00813 ];
INF_S4                    (idx, [1:   8]) = [ -5.87788E-03 0.00730 -3.65568E-04 0.00989 -6.26258E-06 0.66942 -3.82657E-03 0.02607 ];
INF_S5                    (idx, [1:   8]) = [  6.24187E-04 0.05159  6.92953E-06 0.58598 -4.38101E-05 0.10663  3.23181E-03 0.01652 ];
INF_S6                    (idx, [1:   8]) = [  3.84159E-03 0.00564 -9.13265E-05 0.03541 -4.85578E-05 0.08262 -8.19864E-03 0.00797 ];
INF_S7                    (idx, [1:   8]) = [  7.16949E-04 0.02573 -1.05025E-04 0.03435 -4.26944E-05 0.09291 -1.16748E-04 0.79648 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  3.93708E-01 0.00023  1.10589E-02 0.00089  1.39749E-03 0.00945  8.67748E-01 0.00023 ];
INF_SP1                   (idx, [1:   8]) = [  1.65828E-01 0.00042  3.16294E-03 0.00216  4.63843E-04 0.01562  2.22217E-01 0.00075 ];
INF_SP2                   (idx, [1:   8]) = [  6.78743E-02 0.00078 -9.52192E-04 0.00511  2.56376E-04 0.02118  5.56341E-02 0.00234 ];
INF_SP3                   (idx, [1:   8]) = [  7.21028E-03 0.00553 -1.12299E-03 0.00457  8.84704E-05 0.06496  1.69434E-02 0.00813 ];
INF_SP4                   (idx, [1:   8]) = [ -5.87781E-03 0.00731 -3.65568E-04 0.00989 -6.26258E-06 0.66942 -3.82657E-03 0.02607 ];
INF_SP5                   (idx, [1:   8]) = [  6.24241E-04 0.05163  6.92953E-06 0.58598 -4.38101E-05 0.10663  3.23181E-03 0.01652 ];
INF_SP6                   (idx, [1:   8]) = [  3.84194E-03 0.00562 -9.13265E-05 0.03541 -4.85578E-05 0.08262 -8.19864E-03 0.00797 ];
INF_SP7                   (idx, [1:   8]) = [  7.16678E-04 0.02571 -1.05025E-04 0.03435 -4.26944E-05 0.09291 -1.16748E-04 0.79648 ];

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

CMM_TRANSPXS              (idx, [1:   4]) = [  1.91616E-01 0.00149  5.93494E-01 0.00547 ];
CMM_TRANSPXS_X            (idx, [1:   4]) = [  1.92124E-01 0.00190  5.93357E-01 0.01089 ];
CMM_TRANSPXS_Y            (idx, [1:   4]) = [  1.91676E-01 0.00231  5.98350E-01 0.00612 ];
CMM_TRANSPXS_Z            (idx, [1:   4]) = [  1.91084E-01 0.00226  5.90720E-01 0.00823 ];
CMM_DIFFCOEF              (idx, [1:   4]) = [  1.73969E+00 0.00149  5.62050E-01 0.00548 ];
CMM_DIFFCOEF_X            (idx, [1:   4]) = [  1.73514E+00 0.00190  5.63357E-01 0.01076 ];
CMM_DIFFCOEF_Y            (idx, [1:   4]) = [  1.73927E+00 0.00233  5.57586E-01 0.00610 ];
CMM_DIFFCOEF_Z            (idx, [1:   4]) = [  1.74465E+00 0.00226  5.65206E-01 0.00828 ];

% Delayed neutron parameters (Meulekamp method):

BETA_EFF                  (idx, [1:  18]) = [  7.30577E-03 0.01795  2.29566E-04 0.10440  1.01114E-03 0.04916  6.42791E-04 0.06306  1.32243E-03 0.03840  2.36933E-03 0.03092  8.10930E-04 0.05523  6.41079E-04 0.05614  2.78493E-04 0.09674 ];
LAMBDA                    (idx, [1:  18]) = [  4.86019E-01 0.03004  1.24667E-02 0.0E+00  2.82917E-02 0.0E+00  4.25244E-02 5.9E-09  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 4.9E-09  3.55460E+00 0.0E+00 ];

