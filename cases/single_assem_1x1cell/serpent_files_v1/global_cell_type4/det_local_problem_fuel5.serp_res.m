
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
INPUT_FILE_NAME           (idx, [1:145])  = '/home/hirepan/Documents/chalmers/Project/codes/Shynt/repo/cases/single_assem_1x1cell/serpent_files/global_cell_type4/det_local_problem_fuel5.serp' ;
WORKING_DIRECTORY         (idx, [1: 84])  = '/home/hirepan/Documents/chalmers/Project/codes/Shynt/repo/cases/single_assem_1x1cell' ;
HOSTNAME                  (idx, [1:  4])  = 'thor' ;
CPU_TYPE                  (idx, [1: 40])  = 'Intel(R) Core(TM) i9-10900 CPU @ 2.80GHz' ;
CPU_MHZ                   (idx, 1)        = 236.0 ;
START_DATE                (idx, [1: 24])  = 'Thu Mar 10 11:45:12 2022' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Mar 10 11:45:40 2022' ;

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
OMP_HISTORY_PROFILE       (idx, [1:  18]) = [  1.14512E+00  9.63956E-01  1.00329E+00  9.58790E-01  9.61536E-01  1.09223E+00  9.65820E-01  9.68321E-01  1.01099E+00  1.03051E+00  9.65182E-01  9.63989E-01  9.97128E-01  9.71722E-01  1.05245E+00  9.63351E-01  1.03030E+00  9.55307E-01  ];
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
ST_FRAC                   (idx, [1:   4]) = [  2.25681E-03 0.00288  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.97743E-01 6.5E-06  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  8.34993E-01 8.7E-05  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  8.37431E-01 0.00011  0.00000E+00 0.0E+00 ];
AVG_TRACKING_LOOPS        (idx, [1:   8]) = [  4.89078E+00 0.00086  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  2.54955E+01 0.00051  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  2.54955E+01 0.00051  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  4.94941E+00 0.00076  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  4.24315E+01 0.00049  0.00000E+00 0.0E+00 ];
LOST_PARTICLES            (idx, 1)        = 0 ;

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 500 ;
SIMULATED_HISTORIES       (idx, 1)        = 1000418 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  2.00084E+03 0.00143 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  2.00084E+03 0.00143 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  8.19687E+00 ;
RUNNING_TIME              (idx, 1)        =  4.72033E-01 ;
INIT_TIME                 (idx, [1:  2])  = [  1.22500E-02  1.22500E-02 ];
PROCESS_TIME              (idx, [1:  2])  = [  1.16666E-04  1.16666E-04 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  4.59600E-01  4.59600E-01  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  4.71933E-01  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 17.36503 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  1.78273E+01 0.00174 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  9.41071E-01 ;

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

NORM_COEF                 (idx, [1:   4]) = [  4.99295E-04 0.00080  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  5.79071E-01 0.00219 ];
U235_FISS                 (idx, [1:   4]) = [  4.74345E-01 0.00122  9.19246E-01 0.00040 ];
U238_FISS                 (idx, [1:   4]) = [  4.16916E-02 0.00491  8.07541E-02 0.00456 ];
U235_CAPT                 (idx, [1:   4]) = [  1.16825E-01 0.00287  2.41164E-01 0.00255 ];
U238_CAPT                 (idx, [1:   4]) = [  3.42109E-01 0.00171  7.06168E-01 0.00094 ];

% Neutron balance (particles/weight):

BALA_SRC_NEUTRON_SRC     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_FISS    (idx, [1:  2])  = [ 1000418 1.00000E+06 ];
BALA_SRC_NEUTRON_NXN     (idx, [1:  2])  = [ 0 1.89812E+03 ];
BALA_SRC_NEUTRON_VR      (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_TOT     (idx, [1:  2])  = [ 1000418 1.00190E+06 ];

BALA_LOSS_NEUTRON_CAPT    (idx, [1:  2])  = [ 484329 4.85114E+05 ];
BALA_LOSS_NEUTRON_FISS    (idx, [1:  2])  = [ 516089 5.16785E+05 ];
BALA_LOSS_NEUTRON_LEAK    (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_CUT     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_ERR     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_TOT     (idx, [1:  2])  = [ 1000418 1.00190E+06 ];

BALA_NEUTRON_DIFF         (idx, [1:  2])  = [ 0 3.49246E-10 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.67514E-11 0.00056 ];
TOT_POWDENS               (idx, [1:   2]) = [  3.08793E-15 0.00056 ];
TOT_GENRATE               (idx, [1:   2]) = [  1.27425E+00 0.00056 ];
TOT_FISSRATE              (idx, [1:   2]) = [  5.16136E-01 0.00056 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  4.83864E-01 0.00060 ];
TOT_ABSRATE               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.98590E-01 0.00080 ];
TOT_FLUX                  (idx, [1:   2]) = [  5.47565E+01 0.00067 ];
TOT_PHOTON_PRODRATE       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  2.55024E+01 0.00053 ];
INI_FMASS                 (idx, 1)        =  5.42481E-03 ;
TOT_FMASS                 (idx, 1)        =  5.42481E-03 ;

% Six-factor formula:

SIX_FF_ETA                (idx, [1:   2]) = [  1.83907E+00 0.00087 ];
SIX_FF_F                  (idx, [1:   2]) = [  9.63733E-01 0.00028 ];
SIX_FF_P                  (idx, [1:   2]) = [  5.00014E-01 0.00101 ];
SIX_FF_EPSILON            (idx, [1:   2]) = [  1.44033E+00 0.00093 ];
SIX_FF_LF                 (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
SIX_FF_LT                 (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
SIX_FF_KINF               (idx, [1:   2]) = [  1.27589E+00 0.00101 ];
SIX_FF_KEFF               (idx, [1:   2]) = [  1.27589E+00 0.00101 ];

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.46883E+00 3.4E-05 ];
FISSE                     (idx, [1:   2]) = [  2.02571E+02 2.8E-06 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.27585E+00 0.00103  1.26679E+00 0.00101  9.10787E-03 0.01576 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.27672E+00 0.00056 ];
COL_KEFF                  (idx, [1:   2]) = [  1.27652E+00 0.00108 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.27672E+00 0.00056 ];
ABS_KINF                  (idx, [1:   2]) = [  1.27672E+00 0.00056 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% ALF (Average lethargy of neutrons causing fission):
% Based on E0 = 2.000000E+01 MeV

ANA_ALF                   (idx, [1:   2]) = [  1.64535E+01 0.00045 ];
IMP_ALF                   (idx, [1:   2]) = [  1.64541E+01 0.00024 ];

% EALF (Energy corresponding to average lethargy of neutrons causing fission):

ANA_EALF                  (idx, [1:   2]) = [  1.44957E-06 0.00741 ];
IMP_EALF                  (idx, [1:   2]) = [  1.43507E-06 0.00405 ];

% AFGE (Average energy of neutrons causing fission):

ANA_AFGE                  (idx, [1:   2]) = [  2.77006E-01 0.00490 ];
IMP_AFGE                  (idx, [1:   2]) = [  2.76225E-01 0.00232 ];

% Forward-weighted delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
FWD_ANA_BETA_ZERO         (idx, [1:  18]) = [  5.90447E-03 0.01149  1.68918E-04 0.07224  8.23491E-04 0.03136  4.94582E-04 0.04193  1.09035E-03 0.02602  1.90044E-03 0.02014  6.81969E-04 0.03457  5.47748E-04 0.03677  1.96980E-04 0.06424 ];
FWD_ANA_LAMBDA            (idx, [1:  18]) = [  4.75950E-01 0.01833  4.11401E-03 0.06379  2.42177E-02 0.01836  2.99372E-02 0.02903  1.25592E-01 0.01090  2.89543E-01 0.00450  5.47853E-01 0.02083  1.26205E+00 0.02433  1.38629E+00 0.05599 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  18]) = [  7.20220E-03 0.01822  2.11474E-04 0.10538  1.02718E-03 0.04511  6.29991E-04 0.06334  1.38146E-03 0.04033  2.24448E-03 0.03208  8.31332E-04 0.04902  6.47396E-04 0.05600  2.28892E-04 0.10143 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  18]) = [  4.65535E-01 0.02716  1.24667E-02 0.0E+00  2.82917E-02 0.0E+00  4.25244E-02 6.0E-09  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 4.9E-09  3.55460E+00 0.0E+00 ];

% Adjoint weighted time constants using Nauchi's method:

IFP_CHAIN_LENGTH          (idx, 1)        = 15 ;
ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  1.60027E-05 0.00241  1.59894E-05 0.00241  1.77958E-05 0.02405 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  2.04047E-05 0.00211  2.03877E-05 0.00211  2.26959E-05 0.02396 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  18]) = [  7.13338E-03 0.01592  2.05301E-04 0.09696  9.76963E-04 0.04528  6.35473E-04 0.05854  1.31657E-03 0.03883  2.27570E-03 0.02864  8.72957E-04 0.04932  6.41884E-04 0.05507  2.08531E-04 0.09652 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  18]) = [  4.55015E-01 0.02590  1.24667E-02 0.0E+00  2.82917E-02 3.7E-09  4.25244E-02 8.1E-09  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 5.5E-09  3.55460E+00 5.1E-09 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  1.60278E-05 0.00493  1.60202E-05 0.00496  1.31318E-05 0.05540 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  2.04360E-05 0.00478  2.04261E-05 0.00480  1.67520E-05 0.05562 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  18]) = [  7.34956E-03 0.04785  2.18290E-04 0.27683  8.30437E-04 0.13561  6.53131E-04 0.15224  1.29143E-03 0.11370  2.51160E-03 0.08153  8.70272E-04 0.14199  7.10306E-04 0.15283  2.64090E-04 0.25995 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  18]) = [  4.55815E-01 0.06743  1.24667E-02 0.0E+00  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 3.7E-09  2.92467E-01 5.9E-09  6.66488E-01 4.6E-09  1.63478E+00 0.0E+00  3.55460E+00 2.7E-09 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  18]) = [  7.26809E-03 0.04572  2.08789E-04 0.26310  8.45131E-04 0.13276  6.65329E-04 0.14779  1.31945E-03 0.11027  2.51060E-03 0.07826  8.52350E-04 0.13429  6.19708E-04 0.14537  2.46734E-04 0.25384 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  18]) = [  4.53988E-01 0.06689  1.24667E-02 3.8E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 3.7E-09  2.92467E-01 6.0E-09  6.66488E-01 4.8E-09  1.63478E+00 0.0E+00  3.55460E+00 2.7E-09 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -4.66955E+02 0.04887 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  1.60486E-05 0.00146 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  2.04648E-05 0.00102 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  7.27001E-03 0.00994 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -4.53556E+02 0.01011 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  2.71188E-07 0.00129 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  4.12583E-06 0.00100  4.12589E-06 0.00100  4.14669E-06 0.01277 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  2.46027E-05 0.00141  2.46044E-05 0.00141  2.43891E-05 0.01673 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.00668E-01 0.00101  4.99638E-01 0.00103  7.19728E-01 0.01992 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.20278E+01 0.02723 ];
ANA_MEAN_NCOL             (idx, [1:   4]) = [  2.54955E+01 0.00051  2.83273E+01 0.00069 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  1])  = '0' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  2.00000E+01  6.06550E+00  3.67900E+00  2.23100E+00  1.35300E+00  8.21000E-01  5.00000E-01  3.02500E-01  1.83000E-01  1.11000E-01  6.74300E-02  4.08500E-02  2.47800E-02  1.50300E-02  9.11800E-03  5.50000E-03  3.51910E-03  2.23945E-03  1.42510E-03  9.06898E-04  3.67262E-04  1.48728E-04  7.55014E-05  4.80520E-05  2.77000E-05  1.59680E-05  9.87700E-06  4.00000E-06  3.30000E-06  2.60000E-06  2.10000E-06  1.85500E-06  1.50000E-06  1.30000E-06  1.15000E-06  1.12300E-06  1.09700E-06  1.07100E-06  1.04500E-06  1.02000E-06  9.96000E-07  9.72000E-07  9.50000E-07  9.10000E-07  8.50000E-07  7.80000E-07  6.25000E-07  5.00000E-07  4.00000E-07  3.50000E-07  3.20000E-07  3.00000E-07  2.80000E-07  2.50000E-07  2.20000E-07  1.80000E-07  1.40000E-07  1.00000E-07  8.00000E-08  6.70000E-08  5.80000E-08  5.00000E-08  4.20000E-08  3.50000E-08  3.00000E-08  2.50000E-08  2.00000E-08  1.50000E-08  1.00000E-08  5.00000E-09  1.00000E-11 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Micro-group spectrum:

INF_MICRO_FLX             (idx, [1: 140]) = [  1.69767E+04 0.00989  7.06771E+04 0.00315  1.48778E+05 0.00190  1.56286E+05 0.00149  1.49614E+05 0.00157  1.80287E+05 0.00111  1.21509E+05 0.00152  1.13088E+05 0.00149  8.57005E+04 0.00150  6.99255E+04 0.00174  6.03829E+04 0.00172  5.40139E+04 0.00162  4.97429E+04 0.00187  4.72323E+04 0.00166  4.58598E+04 0.00128  3.93336E+04 0.00187  3.88722E+04 0.00231  3.81936E+04 0.00202  3.70825E+04 0.00218  7.14301E+04 0.00134  6.76610E+04 0.00133  4.74913E+04 0.00164  2.99847E+04 0.00170  3.34533E+04 0.00198  3.04561E+04 0.00209  2.78861E+04 0.00188  4.29943E+04 0.00186  9.97025E+03 0.00286  1.25439E+04 0.00263  1.14961E+04 0.00320  6.58705E+03 0.00453  1.14631E+04 0.00292  7.82646E+03 0.00352  6.53631E+03 0.00334  1.20878E+03 0.00649  1.21610E+03 0.00590  1.23866E+03 0.00681  1.27954E+03 0.01018  1.27478E+03 0.00638  1.25773E+03 0.00652  1.33518E+03 0.00755  1.22139E+03 0.00839  2.29208E+03 0.00666  3.70020E+03 0.00563  4.71592E+03 0.00361  1.22729E+04 0.00341  1.27016E+04 0.00264  1.30746E+04 0.00309  8.14646E+03 0.00274  5.58654E+03 0.00345  4.12044E+03 0.00520  4.62918E+03 0.00393  8.13704E+03 0.00330  1.00147E+04 0.00341  1.74157E+04 0.00272  2.38307E+04 0.00290  3.16731E+04 0.00255  1.87179E+04 0.00302  1.28094E+04 0.00298  8.94401E+03 0.00296  7.85737E+03 0.00331  7.52800E+03 0.00302  6.18068E+03 0.00327  4.09727E+03 0.00384  3.74192E+03 0.00358  3.29177E+03 0.00380  2.71432E+03 0.00340  2.11830E+03 0.00341  1.39384E+03 0.00558  4.82873E+02 0.00663 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.27651E+00 0.00130 ];

% Flux spectra in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  4.92890E+01 0.00073  5.47232E+00 0.00129 ];
INF_FISS_FLX              (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  4.12498E-01 0.00018  9.45582E-01 0.00029 ];
INF_CAPT                  (idx, [1:   4]) = [  7.07159E-03 0.00107  2.47483E-02 0.00064 ];
INF_ABS                   (idx, [1:   4]) = [  1.01749E-02 0.00085  9.11480E-02 0.00076 ];
INF_FISS                  (idx, [1:   4]) = [  3.10334E-03 0.00073  6.63997E-02 0.00081 ];
INF_NSF                   (idx, [1:   4]) = [  7.90202E-03 0.00073  1.61763E-01 0.00081 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.54629E+00 9.8E-05  2.43620E+00 2.7E-09 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.03287E+02 7.5E-06  2.02270E+02 0.0E+00 ];
INF_INVV                  (idx, [1:   4]) = [  5.21107E-08 0.00081  2.24451E-06 0.00037 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  4.02329E-01 0.00018  8.54339E-01 0.00040 ];
INF_SCATT1                (idx, [1:   4]) = [  1.67896E-01 0.00034  2.25905E-01 0.00109 ];
INF_SCATT2                (idx, [1:   4]) = [  6.65013E-02 0.00059  5.83122E-02 0.00315 ];
INF_SCATT3                (idx, [1:   4]) = [  6.02758E-03 0.00559  1.79326E-02 0.01075 ];
INF_SCATT4                (idx, [1:   4]) = [ -6.14805E-03 0.00612 -3.22287E-03 0.03770 ];
INF_SCATT5                (idx, [1:   4]) = [  7.36775E-04 0.02762  3.03610E-03 0.03550 ];
INF_SCATT6                (idx, [1:   4]) = [  3.80181E-03 0.00685 -8.09105E-03 0.01355 ];
INF_SCATT7                (idx, [1:   4]) = [  6.54116E-04 0.03808 -5.32002E-04 0.21038 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  4.02368E-01 0.00018  8.54339E-01 0.00040 ];
INF_SCATTP1               (idx, [1:   4]) = [  1.67897E-01 0.00034  2.25905E-01 0.00109 ];
INF_SCATTP2               (idx, [1:   4]) = [  6.65019E-02 0.00059  5.83122E-02 0.00315 ];
INF_SCATTP3               (idx, [1:   4]) = [  6.02700E-03 0.00559  1.79326E-02 0.01075 ];
INF_SCATTP4               (idx, [1:   4]) = [ -6.14781E-03 0.00614 -3.22287E-03 0.03770 ];
INF_SCATTP5               (idx, [1:   4]) = [  7.37242E-04 0.02763  3.03610E-03 0.03550 ];
INF_SCATTP6               (idx, [1:   4]) = [  3.80163E-03 0.00685 -8.09105E-03 0.01355 ];
INF_SCATTP7               (idx, [1:   4]) = [  6.53977E-04 0.03813 -5.32002E-04 0.21038 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  1.84335E-01 0.00053  6.41456E-01 0.00049 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.80832E+00 0.00053  5.19654E-01 0.00049 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  1.01365E-02 0.00084  9.11480E-02 0.00076 ];
INF_REMXS                 (idx, [1:   4]) = [  2.05052E-02 0.00043  9.31056E-02 0.00118 ];

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

INF_S0                    (idx, [1:   8]) = [  3.91993E-01 0.00018  1.03369E-02 0.00098  1.86184E-03 0.01226  8.52477E-01 0.00040 ];
INF_S1                    (idx, [1:   8]) = [  1.64950E-01 0.00034  2.94557E-03 0.00179  6.08418E-04 0.02260  2.25297E-01 0.00111 ];
INF_S2                    (idx, [1:   8]) = [  6.74162E-02 0.00059 -9.14825E-04 0.00654  3.40182E-04 0.03071  5.79720E-02 0.00325 ];
INF_S3                    (idx, [1:   8]) = [  7.08473E-03 0.00478 -1.05715E-03 0.00431  1.27624E-04 0.05118  1.78050E-02 0.01089 ];
INF_S4                    (idx, [1:   8]) = [ -5.80653E-03 0.00629 -3.41523E-04 0.00952  7.38443E-06 0.91462 -3.23026E-03 0.03786 ];
INF_S5                    (idx, [1:   8]) = [  7.25737E-04 0.02687  1.10383E-05 0.40944 -5.92549E-05 0.11593  3.09535E-03 0.03508 ];
INF_S6                    (idx, [1:   8]) = [  3.88160E-03 0.00677 -7.97890E-05 0.04480 -6.46594E-05 0.09810 -8.02639E-03 0.01370 ];
INF_S7                    (idx, [1:   8]) = [  7.50261E-04 0.03211 -9.61450E-05 0.03643 -6.09678E-05 0.08282 -4.71034E-04 0.23790 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  3.92031E-01 0.00018  1.03369E-02 0.00098  1.86184E-03 0.01226  8.52477E-01 0.00040 ];
INF_SP1                   (idx, [1:   8]) = [  1.64951E-01 0.00034  2.94557E-03 0.00179  6.08418E-04 0.02260  2.25297E-01 0.00111 ];
INF_SP2                   (idx, [1:   8]) = [  6.74167E-02 0.00059 -9.14825E-04 0.00654  3.40182E-04 0.03071  5.79720E-02 0.00325 ];
INF_SP3                   (idx, [1:   8]) = [  7.08415E-03 0.00478 -1.05715E-03 0.00431  1.27624E-04 0.05118  1.78050E-02 0.01089 ];
INF_SP4                   (idx, [1:   8]) = [ -5.80628E-03 0.00630 -3.41523E-04 0.00952  7.38443E-06 0.91462 -3.23026E-03 0.03786 ];
INF_SP5                   (idx, [1:   8]) = [  7.26204E-04 0.02688  1.10383E-05 0.40944 -5.92549E-05 0.11593  3.09535E-03 0.03508 ];
INF_SP6                   (idx, [1:   8]) = [  3.88142E-03 0.00677 -7.97890E-05 0.04480 -6.46594E-05 0.09810 -8.02639E-03 0.01370 ];
INF_SP7                   (idx, [1:   8]) = [  7.50122E-04 0.03215 -9.61450E-05 0.03643 -6.09678E-05 0.08282 -4.71034E-04 0.23790 ];

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

CMM_TRANSPXS              (idx, [1:   4]) = [  1.90160E-01 0.00142  5.88830E-01 0.00570 ];
CMM_TRANSPXS_X            (idx, [1:   4]) = [  1.90754E-01 0.00208  5.83908E-01 0.01301 ];
CMM_TRANSPXS_Y            (idx, [1:   4]) = [  1.90021E-01 0.00225  5.89092E-01 0.01223 ];
CMM_TRANSPXS_Z            (idx, [1:   4]) = [  1.89742E-01 0.00200  5.97667E-01 0.00787 ];
CMM_DIFFCOEF              (idx, [1:   4]) = [  1.75299E+00 0.00142  5.66543E-01 0.00580 ];
CMM_DIFFCOEF_X            (idx, [1:   4]) = [  1.74763E+00 0.00208  5.73134E-01 0.01272 ];
CMM_DIFFCOEF_Y            (idx, [1:   4]) = [  1.75440E+00 0.00223  5.67950E-01 0.01267 ];
CMM_DIFFCOEF_Z            (idx, [1:   4]) = [  1.75694E+00 0.00199  5.58544E-01 0.00778 ];

% Delayed neutron parameters (Meulekamp method):

BETA_EFF                  (idx, [1:  18]) = [  7.20220E-03 0.01822  2.11474E-04 0.10538  1.02718E-03 0.04511  6.29991E-04 0.06334  1.38146E-03 0.04033  2.24448E-03 0.03208  8.31332E-04 0.04902  6.47396E-04 0.05600  2.28892E-04 0.10143 ];
LAMBDA                    (idx, [1:  18]) = [  4.65535E-01 0.02716  1.24667E-02 0.0E+00  2.82917E-02 0.0E+00  4.25244E-02 6.0E-09  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 4.9E-09  3.55460E+00 0.0E+00 ];

