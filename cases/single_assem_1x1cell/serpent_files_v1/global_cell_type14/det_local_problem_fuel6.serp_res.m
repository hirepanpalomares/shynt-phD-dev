
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
INPUT_FILE_NAME           (idx, [1:146])  = '/home/hirepan/Documents/chalmers/Project/codes/Shynt/repo/cases/single_assem_1x1cell/serpent_files/global_cell_type14/det_local_problem_fuel6.serp' ;
WORKING_DIRECTORY         (idx, [1: 84])  = '/home/hirepan/Documents/chalmers/Project/codes/Shynt/repo/cases/single_assem_1x1cell' ;
HOSTNAME                  (idx, [1:  4])  = 'thor' ;
CPU_TYPE                  (idx, [1: 40])  = 'Intel(R) Core(TM) i9-10900 CPU @ 2.80GHz' ;
CPU_MHZ                   (idx, 1)        = 236.0 ;
START_DATE                (idx, [1: 24])  = 'Thu Mar 10 11:46:39 2022' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Mar 10 11:47:06 2022' ;

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
OMP_HISTORY_PROFILE       (idx, [1:  18]) = [  9.57326E-01  1.23219E+00  9.56721E-01  9.64078E-01  9.39654E-01  1.09089E+00  1.22710E+00  9.42793E-01  1.06360E+00  9.56558E-01  9.45997E-01  9.55920E-01  9.59615E-01  1.02358E+00  9.53533E-01  9.49675E-01  9.52046E-01  9.28717E-01  ];
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

MIN_MACROXS               (idx, [1:   4]) = [  5.00000E-02 9.3E-10  0.00000E+00 0.0E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  2.25932E-03 0.00287  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.97741E-01 6.5E-06  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  8.36404E-01 8.8E-05  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  8.38291E-01 0.00011  0.00000E+00 0.0E+00 ];
AVG_TRACKING_LOOPS        (idx, [1:   8]) = [  4.89225E+00 0.00095  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  2.50754E+01 0.00051  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  2.50754E+01 0.00051  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  4.83716E+00 0.00077  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  4.20448E+01 0.00051  0.00000E+00 0.0E+00 ];
LOST_PARTICLES            (idx, 1)        = 0 ;

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 500 ;
SIMULATED_HISTORIES       (idx, 1)        = 1000426 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  2.00085E+03 0.00142 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  2.00085E+03 0.00142 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  7.96973E+00 ;
RUNNING_TIME              (idx, 1)        =  4.54883E-01 ;
INIT_TIME                 (idx, [1:  2])  = [  1.18167E-02  1.18167E-02 ];
PROCESS_TIME              (idx, [1:  2])  = [  1.16666E-04  1.16666E-04 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  4.42900E-01  4.42900E-01  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  4.54800E-01  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 17.52037 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  1.79670E+01 0.00150 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  9.51013E-01 ;

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

NORM_COEF                 (idx, [1:   4]) = [  4.98990E-04 0.00080  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  5.55567E-01 0.00215 ];
U235_FISS                 (idx, [1:   4]) = [  4.80582E-01 0.00116  9.20465E-01 0.00042 ];
U238_FISS                 (idx, [1:   4]) = [  4.15506E-02 0.00522  7.95353E-02 0.00487 ];
U235_CAPT                 (idx, [1:   4]) = [  1.20008E-01 0.00289  2.51183E-01 0.00256 ];
U238_CAPT                 (idx, [1:   4]) = [  3.33481E-01 0.00170  6.97974E-01 0.00097 ];

% Neutron balance (particles/weight):

BALA_SRC_NEUTRON_SRC     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_FISS    (idx, [1:  2])  = [ 1000426 1.00000E+06 ];
BALA_SRC_NEUTRON_NXN     (idx, [1:  2])  = [ 0 1.94920E+03 ];
BALA_SRC_NEUTRON_VR      (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_TOT     (idx, [1:  2])  = [ 1000426 1.00195E+06 ];

BALA_LOSS_NEUTRON_CAPT    (idx, [1:  2])  = [ 477964 4.78728E+05 ];
BALA_LOSS_NEUTRON_FISS    (idx, [1:  2])  = [ 522462 5.23221E+05 ];
BALA_LOSS_NEUTRON_LEAK    (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_CUT     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_ERR     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_TOT     (idx, [1:  2])  = [ 1000426 1.00195E+06 ];

BALA_NEUTRON_DIFF         (idx, [1:  2])  = [ 0 4.19095E-09 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.69349E-11 0.00050 ];
TOT_POWDENS               (idx, [1:   2]) = [  3.12174E-15 0.00050 ];
TOT_GENRATE               (idx, [1:   2]) = [  1.28805E+00 0.00050 ];
TOT_FISSRATE              (idx, [1:   2]) = [  5.21797E-01 0.00050 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  4.78203E-01 0.00055 ];
TOT_ABSRATE               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.97981E-01 0.00080 ];
TOT_FLUX                  (idx, [1:   2]) = [  5.42007E+01 0.00066 ];
TOT_PHOTON_PRODRATE       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  2.50683E+01 0.00054 ];
INI_FMASS                 (idx, 1)        =  5.42481E-03 ;
TOT_FMASS                 (idx, 1)        =  5.42481E-03 ;

% Six-factor formula:

SIX_FF_ETA                (idx, [1:   2]) = [  1.85666E+00 0.00086 ];
SIX_FF_F                  (idx, [1:   2]) = [  9.65737E-01 0.00027 ];
SIX_FF_P                  (idx, [1:   2]) = [  4.91082E-01 0.00094 ];
SIX_FF_EPSILON            (idx, [1:   2]) = [  1.46749E+00 0.00092 ];
SIX_FF_LF                 (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
SIX_FF_LT                 (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
SIX_FF_KINF               (idx, [1:   2]) = [  1.29166E+00 0.00099 ];
SIX_FF_KEFF               (idx, [1:   2]) = [  1.29166E+00 0.00099 ];

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.46848E+00 3.1E-05 ];
FISSE                     (idx, [1:   2]) = [  2.02567E+02 2.5E-06 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.29210E+00 0.00103  1.28230E+00 0.00099  9.36421E-03 0.01622 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.29052E+00 0.00050 ];
COL_KEFF                  (idx, [1:   2]) = [  1.29113E+00 0.00105 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.29052E+00 0.00050 ];
ABS_KINF                  (idx, [1:   2]) = [  1.29052E+00 0.00050 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% ALF (Average lethargy of neutrons causing fission):
% Based on E0 = 2.000000E+01 MeV

ANA_ALF                   (idx, [1:   2]) = [  1.63527E+01 0.00047 ];
IMP_ALF                   (idx, [1:   2]) = [  1.63564E+01 0.00022 ];

% EALF (Energy corresponding to average lethargy of neutrons causing fission):

ANA_EALF                  (idx, [1:   2]) = [  1.60494E-06 0.00771 ];
IMP_EALF                  (idx, [1:   2]) = [  1.58126E-06 0.00367 ];

% AFGE (Average energy of neutrons causing fission):

ANA_AFGE                  (idx, [1:   2]) = [  2.75466E-01 0.00505 ];
IMP_AFGE                  (idx, [1:   2]) = [  2.74021E-01 0.00212 ];

% Forward-weighted delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
FWD_ANA_BETA_ZERO         (idx, [1:  18]) = [  5.83035E-03 0.01169  1.75921E-04 0.06578  8.44610E-04 0.02954  4.66134E-04 0.04340  1.08791E-03 0.02560  1.86594E-03 0.01930  6.45188E-04 0.03323  5.36214E-04 0.03842  2.08433E-04 0.06424 ];
FWD_ANA_LAMBDA            (idx, [1:  18]) = [  4.75369E-01 0.01919  4.63761E-03 0.05816  2.51796E-02 0.01574  2.87465E-02 0.03099  1.25059E-01 0.01131  2.90127E-01 0.00402  5.51852E-01 0.02040  1.20647E+00 0.02667  1.46450E+00 0.05348 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  18]) = [  7.25365E-03 0.01676  2.27425E-04 0.09612  1.08378E-03 0.04749  5.89632E-04 0.06587  1.35364E-03 0.03763  2.34743E-03 0.02843  7.10293E-04 0.05314  6.81839E-04 0.05832  2.59610E-04 0.08996 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  18]) = [  4.68664E-01 0.02737  1.24667E-02 0.0E+00  2.82917E-02 0.0E+00  4.25244E-02 6.3E-09  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 5.0E-09  3.55460E+00 0.0E+00 ];

% Adjoint weighted time constants using Nauchi's method:

IFP_CHAIN_LENGTH          (idx, 1)        = 15 ;
ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  1.47254E-05 0.00223  1.47102E-05 0.00225  1.68411E-05 0.02501 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  1.90169E-05 0.00199  1.89974E-05 0.00201  2.17419E-05 0.02491 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  18]) = [  7.21641E-03 0.01647  2.19027E-04 0.09925  1.07508E-03 0.04331  5.96458E-04 0.05764  1.35638E-03 0.03585  2.29450E-03 0.02791  7.52564E-04 0.04917  6.88009E-04 0.05114  2.34393E-04 0.08968 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  18]) = [  4.60974E-01 0.02702  1.24667E-02 0.0E+00  2.82917E-02 2.5E-09  4.25244E-02 8.2E-09  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 5.4E-09  3.55460E+00 5.1E-09 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  1.45974E-05 0.00502  1.45801E-05 0.00504  1.31783E-05 0.05332 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  1.88539E-05 0.00497  1.88318E-05 0.00500  1.69733E-05 0.05312 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  18]) = [  7.61315E-03 0.05123  1.91754E-04 0.24988  1.10299E-03 0.11892  5.91838E-04 0.19156  1.53575E-03 0.10932  2.47560E-03 0.08670  7.57021E-04 0.16270  7.50993E-04 0.16043  2.07204E-04 0.24570 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  18]) = [  4.41458E-01 0.06570  1.24667E-02 3.8E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 4.0E-09  2.92467E-01 6.1E-09  6.66488E-01 5.5E-09  1.63478E+00 0.0E+00  3.55460E+00 5.4E-09 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  18]) = [  7.60299E-03 0.04823  2.07393E-04 0.23369  1.10332E-03 0.11573  5.38597E-04 0.17126  1.47873E-03 0.10450  2.55332E-03 0.08345  7.72549E-04 0.15545  7.31480E-04 0.15022  2.17600E-04 0.22415 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  18]) = [  4.41507E-01 0.06447  1.24667E-02 3.8E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 4.2E-09  2.92467E-01 6.1E-09  6.66488E-01 5.0E-09  1.63478E+00 0.0E+00  3.55460E+00 4.7E-09 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -5.27896E+02 0.05216 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  1.46900E-05 0.00139 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  1.89708E-05 0.00092 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  7.35290E-03 0.00999 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -5.01359E+02 0.01023 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  2.55079E-07 0.00117 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  4.09658E-06 0.00101  4.09683E-06 0.00102  4.05549E-06 0.01235 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  2.30645E-05 0.00134  2.30622E-05 0.00134  2.35806E-05 0.01716 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  4.91740E-01 0.00094  4.90673E-01 0.00094  7.25147E-01 0.02251 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.20397E+01 0.02629 ];
ANA_MEAN_NCOL             (idx, [1:   4]) = [  2.50754E+01 0.00051  2.77647E+01 0.00071 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  1])  = '0' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  2.00000E+01  6.06550E+00  3.67900E+00  2.23100E+00  1.35300E+00  8.21000E-01  5.00000E-01  3.02500E-01  1.83000E-01  1.11000E-01  6.74300E-02  4.08500E-02  2.47800E-02  1.50300E-02  9.11800E-03  5.50000E-03  3.51910E-03  2.23945E-03  1.42510E-03  9.06898E-04  3.67262E-04  1.48728E-04  7.55014E-05  4.80520E-05  2.77000E-05  1.59680E-05  9.87700E-06  4.00000E-06  3.30000E-06  2.60000E-06  2.10000E-06  1.85500E-06  1.50000E-06  1.30000E-06  1.15000E-06  1.12300E-06  1.09700E-06  1.07100E-06  1.04500E-06  1.02000E-06  9.96000E-07  9.72000E-07  9.50000E-07  9.10000E-07  8.50000E-07  7.80000E-07  6.25000E-07  5.00000E-07  4.00000E-07  3.50000E-07  3.20000E-07  3.00000E-07  2.80000E-07  2.50000E-07  2.20000E-07  1.80000E-07  1.40000E-07  1.00000E-07  8.00000E-08  6.70000E-08  5.80000E-08  5.00000E-08  4.20000E-08  3.50000E-08  3.00000E-08  2.50000E-08  2.00000E-08  1.50000E-08  1.00000E-08  5.00000E-09  1.00000E-11 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Micro-group spectrum:

INF_MICRO_FLX             (idx, [1: 140]) = [  1.67579E+04 0.00632  7.03134E+04 0.00347  1.48561E+05 0.00185  1.57170E+05 0.00154  1.49565E+05 0.00145  1.79881E+05 0.00134  1.21506E+05 0.00148  1.13055E+05 0.00138  8.56606E+04 0.00162  6.99246E+04 0.00129  6.05560E+04 0.00169  5.38735E+04 0.00221  4.98629E+04 0.00145  4.72989E+04 0.00150  4.57716E+04 0.00185  3.93321E+04 0.00183  3.88057E+04 0.00162  3.81265E+04 0.00185  3.69703E+04 0.00190  7.11244E+04 0.00105  6.74728E+04 0.00167  4.70507E+04 0.00139  2.96643E+04 0.00225  3.30173E+04 0.00176  3.01988E+04 0.00220  2.73834E+04 0.00222  4.21727E+04 0.00153  9.82277E+03 0.00310  1.23413E+04 0.00337  1.12499E+04 0.00213  6.45022E+03 0.00422  1.13545E+04 0.00317  7.63462E+03 0.00399  6.38219E+03 0.00417  1.20813E+03 0.00999  1.18214E+03 0.00954  1.21928E+03 0.00895  1.26587E+03 0.00672  1.24970E+03 0.00704  1.22041E+03 0.00910  1.25197E+03 0.00815  1.17755E+03 0.00816  2.27332E+03 0.00587  3.61953E+03 0.00620  4.56684E+03 0.00557  1.20258E+04 0.00350  1.23602E+04 0.00338  1.27893E+04 0.00321  7.82765E+03 0.00332  5.39137E+03 0.00368  3.95886E+03 0.00472  4.44111E+03 0.00290  7.70252E+03 0.00313  9.44475E+03 0.00343  1.63268E+04 0.00314  2.21176E+04 0.00245  2.92237E+04 0.00271  1.71269E+04 0.00351  1.16851E+04 0.00318  8.12345E+03 0.00390  7.07430E+03 0.00270  6.82854E+03 0.00330  5.59474E+03 0.00269  3.69298E+03 0.00390  3.37991E+03 0.00407  2.95050E+03 0.00250  2.45517E+03 0.00375  1.89925E+03 0.00469  1.24668E+03 0.00469  4.32435E+02 0.00716 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.29113E+00 0.00105 ];

% Flux spectra in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  4.91146E+01 0.00066  5.09143E+00 0.00129 ];
INF_FISS_FLX              (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  4.12244E-01 0.00015  9.47623E-01 0.00028 ];
INF_CAPT                  (idx, [1:   4]) = [  7.11165E-03 0.00090  2.53445E-02 0.00086 ];
INF_ABS                   (idx, [1:   4]) = [  1.03907E-02 0.00071  9.62368E-02 0.00101 ];
INF_FISS                  (idx, [1:   4]) = [  3.27907E-03 0.00087  7.08923E-02 0.00107 ];
INF_NSF                   (idx, [1:   4]) = [  8.33145E-03 0.00085  1.72708E-01 0.00107 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.54080E+00 8.9E-05  2.43620E+00 0.0E+00 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.03233E+02 6.6E-06  2.02270E+02 3.8E-09 ];
INF_INVV                  (idx, [1:   4]) = [  5.13934E-08 0.00068  2.22005E-06 0.00034 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  4.01863E-01 0.00016  8.51363E-01 0.00042 ];
INF_SCATT1                (idx, [1:   4]) = [  1.67708E-01 0.00038  2.26763E-01 0.00099 ];
INF_SCATT2                (idx, [1:   4]) = [  6.64591E-02 0.00063  5.86968E-02 0.00364 ];
INF_SCATT3                (idx, [1:   4]) = [  5.98960E-03 0.00592  1.80348E-02 0.00796 ];
INF_SCATT4                (idx, [1:   4]) = [ -6.17420E-03 0.00598 -3.25452E-03 0.03266 ];
INF_SCATT5                (idx, [1:   4]) = [  7.09708E-04 0.03805  2.92986E-03 0.04197 ];
INF_SCATT6                (idx, [1:   4]) = [  3.72853E-03 0.00874 -7.76788E-03 0.01718 ];
INF_SCATT7                (idx, [1:   4]) = [  5.71634E-04 0.05070 -3.07824E-04 0.32627 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  4.01903E-01 0.00015  8.51363E-01 0.00042 ];
INF_SCATTP1               (idx, [1:   4]) = [  1.67708E-01 0.00038  2.26763E-01 0.00099 ];
INF_SCATTP2               (idx, [1:   4]) = [  6.64590E-02 0.00064  5.86968E-02 0.00364 ];
INF_SCATTP3               (idx, [1:   4]) = [  5.98907E-03 0.00591  1.80348E-02 0.00796 ];
INF_SCATTP4               (idx, [1:   4]) = [ -6.17407E-03 0.00598 -3.25452E-03 0.03266 ];
INF_SCATTP5               (idx, [1:   4]) = [  7.09448E-04 0.03817  2.92986E-03 0.04197 ];
INF_SCATTP6               (idx, [1:   4]) = [  3.72870E-03 0.00872 -7.76788E-03 0.01718 ];
INF_SCATTP7               (idx, [1:   4]) = [  5.71792E-04 0.05064 -3.07824E-04 0.32627 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  1.84231E-01 0.00062  6.42142E-01 0.00040 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.80934E+00 0.00062  5.19098E-01 0.00040 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  1.03511E-02 0.00073  9.62368E-02 0.00101 ];
INF_REMXS                 (idx, [1:   4]) = [  2.05620E-02 0.00047  9.82187E-02 0.00150 ];

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

INF_S0                    (idx, [1:   8]) = [  3.91682E-01 0.00015  1.01814E-02 0.00052  1.95788E-03 0.01040  8.49405E-01 0.00043 ];
INF_S1                    (idx, [1:   8]) = [  1.64810E-01 0.00037  2.89810E-03 0.00248  6.63138E-04 0.02416  2.26100E-01 0.00096 ];
INF_S2                    (idx, [1:   8]) = [  6.73601E-02 0.00064 -9.00987E-04 0.00700  3.54346E-04 0.02754  5.83425E-02 0.00362 ];
INF_S3                    (idx, [1:   8]) = [  7.03076E-03 0.00496 -1.04116E-03 0.00354  1.21109E-04 0.07113  1.79137E-02 0.00812 ];
INF_S4                    (idx, [1:   8]) = [ -5.83649E-03 0.00614 -3.37709E-04 0.01372 -8.14158E-06 0.89192 -3.24638E-03 0.03259 ];
INF_S5                    (idx, [1:   8]) = [  6.89820E-04 0.03923  1.98888E-05 0.24047 -5.73085E-05 0.10905  2.98717E-03 0.04175 ];
INF_S6                    (idx, [1:   8]) = [  3.80637E-03 0.00848 -7.78417E-05 0.04388 -7.48460E-05 0.08444 -7.69304E-03 0.01770 ];
INF_S7                    (idx, [1:   8]) = [  6.71525E-04 0.04320 -9.98902E-05 0.04099 -5.52864E-05 0.09939 -2.52538E-04 0.39950 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  3.91721E-01 0.00015  1.01814E-02 0.00052  1.95788E-03 0.01040  8.49405E-01 0.00043 ];
INF_SP1                   (idx, [1:   8]) = [  1.64810E-01 0.00037  2.89810E-03 0.00248  6.63138E-04 0.02416  2.26100E-01 0.00096 ];
INF_SP2                   (idx, [1:   8]) = [  6.73600E-02 0.00064 -9.00987E-04 0.00700  3.54346E-04 0.02754  5.83425E-02 0.00362 ];
INF_SP3                   (idx, [1:   8]) = [  7.03023E-03 0.00494 -1.04116E-03 0.00354  1.21109E-04 0.07113  1.79137E-02 0.00812 ];
INF_SP4                   (idx, [1:   8]) = [ -5.83636E-03 0.00615 -3.37709E-04 0.01372 -8.14158E-06 0.89192 -3.24638E-03 0.03259 ];
INF_SP5                   (idx, [1:   8]) = [  6.89559E-04 0.03937  1.98888E-05 0.24047 -5.73085E-05 0.10905  2.98717E-03 0.04175 ];
INF_SP6                   (idx, [1:   8]) = [  3.80654E-03 0.00847 -7.78417E-05 0.04388 -7.48460E-05 0.08444 -7.69304E-03 0.01770 ];
INF_SP7                   (idx, [1:   8]) = [  6.71682E-04 0.04316 -9.98902E-05 0.04099 -5.52864E-05 0.09939 -2.52538E-04 0.39950 ];

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

CMM_TRANSPXS              (idx, [1:   4]) = [  1.90056E-01 0.00145  5.79014E-01 0.00544 ];
CMM_TRANSPXS_X            (idx, [1:   4]) = [  1.90123E-01 0.00199  5.80505E-01 0.01106 ];
CMM_TRANSPXS_Y            (idx, [1:   4]) = [  1.90320E-01 0.00256  5.79184E-01 0.01174 ];
CMM_TRANSPXS_Z            (idx, [1:   4]) = [  1.89765E-01 0.00203  5.81085E-01 0.00996 ];
CMM_DIFFCOEF              (idx, [1:   4]) = [  1.75395E+00 0.00145  5.76102E-01 0.00546 ];
CMM_DIFFCOEF_X            (idx, [1:   4]) = [  1.75342E+00 0.00199  5.75900E-01 0.01107 ];
CMM_DIFFCOEF_Y            (idx, [1:   4]) = [  1.75172E+00 0.00255  5.77422E-01 0.01170 ];
CMM_DIFFCOEF_Z            (idx, [1:   4]) = [  1.75673E+00 0.00202  5.74983E-01 0.00979 ];

% Delayed neutron parameters (Meulekamp method):

BETA_EFF                  (idx, [1:  18]) = [  7.25365E-03 0.01676  2.27425E-04 0.09612  1.08378E-03 0.04749  5.89632E-04 0.06587  1.35364E-03 0.03763  2.34743E-03 0.02843  7.10293E-04 0.05314  6.81839E-04 0.05832  2.59610E-04 0.08996 ];
LAMBDA                    (idx, [1:  18]) = [  4.68664E-01 0.02737  1.24667E-02 0.0E+00  2.82917E-02 0.0E+00  4.25244E-02 6.3E-09  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 5.0E-09  3.55460E+00 0.0E+00 ];

