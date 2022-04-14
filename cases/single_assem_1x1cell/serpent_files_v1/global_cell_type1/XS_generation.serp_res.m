
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
INPUT_FILE_NAME           (idx, [1:135])  = '/home/hirepan/Documents/chalmers/Project/codes/Shynt/repo/cases/single_assem_1x1cell/serpent_files/global_cell_type1/XS_generation.serp' ;
WORKING_DIRECTORY         (idx, [1: 84])  = '/home/hirepan/Documents/chalmers/Project/codes/Shynt/repo/cases/single_assem_1x1cell' ;
HOSTNAME                  (idx, [1:  4])  = 'thor' ;
CPU_TYPE                  (idx, [1: 40])  = 'Intel(R) Core(TM) i9-10900 CPU @ 2.80GHz' ;
CPU_MHZ                   (idx, 1)        = 236.0 ;
START_DATE                (idx, [1: 24])  = 'Thu Mar 10 11:48:05 2022' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Mar 10 11:48:16 2022' ;

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
OMP_HISTORY_PROFILE       (idx, [1:  18]) = [  9.71080E-01  9.89865E-01  1.01372E+00  1.00808E+00  9.90600E-01  1.00075E+00  1.00719E+00  9.68595E-01  1.02335E+00  1.01798E+00  1.00083E+00  1.00647E+00  9.77440E-01  9.94786E-01  1.03211E+00  1.00584E+00  1.00366E+00  9.87641E-01  ];
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
ST_FRAC                   (idx, [1:   4]) = [  8.03144E-03 0.00293  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.91969E-01 2.4E-05  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  8.31084E-01 9.7E-05  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  8.31455E-01 9.7E-05  0.00000E+00 0.0E+00 ];
AVG_TRACKING_LOOPS        (idx, [1:   8]) = [  2.38074E+00 0.00039  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  2.82207E+01 0.00058  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  2.82207E+01 0.00058  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  5.72069E+00 0.00077  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  1.99542E-01 0.00326  0.00000E+00 0.0E+00 ];
LOST_PARTICLES            (idx, 1)        = 0 ;

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 500 ;
SIMULATED_HISTORIES       (idx, 1)        = 1000567 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  2.00113E+03 0.00149 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  2.00113E+03 0.00149 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  3.05163E+00 ;
RUNNING_TIME              (idx, 1)        =  1.85083E-01 ;
INIT_TIME                 (idx, [1:  2])  = [  1.20000E-02  1.20000E-02 ];
PROCESS_TIME              (idx, [1:  2])  = [  1.16666E-04  1.16666E-04 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  1.72917E-01  1.72917E-01  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  1.84983E-01  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 16.48788 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  1.76992E+01 0.00452 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  8.22708E-01 ;

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

NORM_COEF                 (idx, [1:   4]) = [  4.99684E-04 0.00082  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  7.26312E-01 0.00207 ];
U235_FISS                 (idx, [1:   4]) = [  4.37257E-01 0.00118  9.12387E-01 0.00044 ];
U238_FISS                 (idx, [1:   4]) = [  4.20104E-02 0.00492  8.76129E-02 0.00456 ];
U235_CAPT                 (idx, [1:   4]) = [  9.82385E-02 0.00311  1.88181E-01 0.00285 ];
U238_CAPT                 (idx, [1:   4]) = [  3.88684E-01 0.00159  7.44512E-01 0.00083 ];

% Neutron balance (particles/weight):

BALA_SRC_NEUTRON_SRC     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_FISS    (idx, [1:  2])  = [ 1000567 1.00000E+06 ];
BALA_SRC_NEUTRON_NXN     (idx, [1:  2])  = [ 0 1.96877E+03 ];
BALA_SRC_NEUTRON_VR      (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_TOT     (idx, [1:  2])  = [ 1000567 1.00197E+06 ];

BALA_LOSS_NEUTRON_CAPT    (idx, [1:  2])  = [ 521576 5.22360E+05 ];
BALA_LOSS_NEUTRON_FISS    (idx, [1:  2])  = [ 478991 4.79609E+05 ];
BALA_LOSS_NEUTRON_LEAK    (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_CUT     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_ERR     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_TOT     (idx, [1:  2])  = [ 1000567 1.00197E+06 ];

BALA_NEUTRON_DIFF         (idx, [1:  2])  = [ 0 -1.04774E-09 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.55124E-11 0.00055 ];
TOT_POWDENS               (idx, [1:   2]) = [  2.85953E-15 0.00055 ];
TOT_GENRATE               (idx, [1:   2]) = [  1.18079E+00 0.00054 ];
TOT_FISSRATE              (idx, [1:   2]) = [  4.77893E-01 0.00055 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  5.22107E-01 0.00050 ];
TOT_ABSRATE               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.99369E-01 0.00082 ];
TOT_FLUX                  (idx, [1:   2]) = [  5.80501E+01 0.00065 ];
TOT_PHOTON_PRODRATE       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  2.82522E+01 0.00051 ];
INI_FMASS                 (idx, 1)        =  5.42481E-03 ;
TOT_FMASS                 (idx, 1)        =  5.42481E-03 ;

% Six-factor formula:

SIX_FF_ETA                (idx, [1:   2]) = [  1.72520E+00 0.00089 ];
SIX_FF_F                  (idx, [1:   2]) = [  9.49173E-01 0.00031 ];
SIX_FF_P                  (idx, [1:   2]) = [  5.41403E-01 0.00092 ];
SIX_FF_EPSILON            (idx, [1:   2]) = [  1.33692E+00 0.00083 ];
SIX_FF_LF                 (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
SIX_FF_LT                 (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
SIX_FF_KINF               (idx, [1:   2]) = [  1.18485E+00 0.00103 ];
SIX_FF_KEFF               (idx, [1:   2]) = [  1.18485E+00 0.00103 ];

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.47082E+00 3.5E-05 ];
FISSE                     (idx, [1:   2]) = [  2.02600E+02 3.0E-06 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.18492E+00 0.00104  1.17606E+00 0.00104  8.79039E-03 0.01698 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.18308E+00 0.00055 ];
COL_KEFF                  (idx, [1:   2]) = [  1.18201E+00 0.00111 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.18308E+00 0.00055 ];
ABS_KINF                  (idx, [1:   2]) = [  1.18308E+00 0.00055 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% ALF (Average lethargy of neutrons causing fission):
% Based on E0 = 2.000000E+01 MeV

ANA_ALF                   (idx, [1:   2]) = [  1.68623E+01 0.00046 ];
IMP_ALF                   (idx, [1:   2]) = [  1.68572E+01 0.00023 ];

% EALF (Energy corresponding to average lethargy of neutrons causing fission):

ANA_EALF                  (idx, [1:   2]) = [  9.64569E-07 0.00792 ];
IMP_EALF                  (idx, [1:   2]) = [  9.58570E-07 0.00384 ];

% AFGE (Average energy of neutrons causing fission):

ANA_AFGE                  (idx, [1:   2]) = [  2.87715E-01 0.00504 ];
IMP_AFGE                  (idx, [1:   2]) = [  2.90487E-01 0.00232 ];

% Forward-weighted delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
FWD_ANA_BETA_ZERO         (idx, [1:  18]) = [  6.68122E-03 0.01137  1.90005E-04 0.06459  9.96050E-04 0.02928  5.42166E-04 0.03930  1.21686E-03 0.02818  2.10645E-03 0.02085  7.29006E-04 0.03346  6.54989E-04 0.03392  2.45698E-04 0.05781 ];
FWD_ANA_LAMBDA            (idx, [1:  18]) = [  4.86359E-01 0.01760  4.63761E-03 0.05816  2.56889E-02 0.01425  3.12129E-02 0.02695  1.24793E-01 0.01151  2.89543E-01 0.00450  5.59850E-01 0.01954  1.32090E+00 0.02182  1.57113E+00 0.05030 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  18]) = [  7.55444E-03 0.01669  2.30208E-04 0.09947  1.10556E-03 0.04419  5.64378E-04 0.05971  1.32564E-03 0.04364  2.44331E-03 0.03102  8.03816E-04 0.05212  7.91714E-04 0.05627  2.89812E-04 0.09168 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  18]) = [  4.92823E-01 0.02578  1.24667E-02 0.0E+00  2.82917E-02 0.0E+00  4.25244E-02 5.7E-09  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 5.3E-09  3.55460E+00 0.0E+00 ];

% Adjoint weighted time constants using Nauchi's method:

IFP_CHAIN_LENGTH          (idx, 1)        = 15 ;
ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  2.53694E-05 0.00239  2.53433E-05 0.00239  2.89435E-05 0.02300 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  3.00435E-05 0.00212  3.00128E-05 0.00213  3.42632E-05 0.02290 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  18]) = [  7.40377E-03 0.01697  1.98024E-04 0.09897  1.08352E-03 0.04443  5.77174E-04 0.05871  1.36039E-03 0.03889  2.29523E-03 0.03166  8.42009E-04 0.04715  7.52638E-04 0.04946  2.94793E-04 0.08054 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  18]) = [  5.12213E-01 0.02932  1.24667E-02 0.0E+00  2.82917E-02 3.6E-09  4.25244E-02 8.2E-09  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 5.4E-09  3.55460E+00 4.8E-09 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  2.54854E-05 0.00513  2.54674E-05 0.00518  1.94520E-05 0.05425 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  3.01838E-05 0.00507  3.01626E-05 0.00512  2.29833E-05 0.05409 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  18]) = [  6.81794E-03 0.05381  1.57905E-04 0.33712  9.86338E-04 0.13172  4.10468E-04 0.19336  1.18557E-03 0.11977  2.33325E-03 0.09646  7.79753E-04 0.14279  7.59195E-04 0.16378  2.05459E-04 0.25978 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  18]) = [  5.30974E-01 0.06832  1.24667E-02 3.9E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 3.5E-09  2.92467E-01 5.3E-09  6.66488E-01 5.1E-09  1.63478E+00 0.0E+00  3.55460E+00 3.8E-09 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  18]) = [  6.83986E-03 0.05110  1.55014E-04 0.34108  1.00176E-03 0.12335  3.86747E-04 0.19768  1.18043E-03 0.11343  2.37345E-03 0.09213  7.41320E-04 0.14339  7.76845E-04 0.15349  2.24290E-04 0.24835 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  18]) = [  5.34122E-01 0.06772  1.24667E-02 3.9E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 3.2E-09  2.92467E-01 5.3E-09  6.66488E-01 5.1E-09  1.63478E+00 0.0E+00  3.55460E+00 6.0E-09 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -2.72932E+02 0.05476 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  2.54348E-05 0.00154 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  3.01214E-05 0.00111 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  7.37196E-03 0.01019 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -2.90211E+02 0.01030 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  3.76458E-07 0.00118 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  4.23960E-06 0.00102  4.23894E-06 0.00103  4.33632E-06 0.01177 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.53373E-05 0.00129  3.53348E-05 0.00129  3.60477E-05 0.01602 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.41905E-01 0.00092  5.41026E-01 0.00093  7.13035E-01 0.01845 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.19355E+01 0.02484 ];
ANA_MEAN_NCOL             (idx, [1:   4]) = [  2.82207E+01 0.00058  3.19840E+01 0.00077 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  7])  = 'u4gcu_1' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  2.00000E+01  6.06550E+00  3.67900E+00  2.23100E+00  1.35300E+00  8.21000E-01  5.00000E-01  3.02500E-01  1.83000E-01  1.11000E-01  6.74300E-02  4.08500E-02  2.47800E-02  1.50300E-02  9.11800E-03  5.50000E-03  3.51910E-03  2.23945E-03  1.42510E-03  9.06898E-04  3.67262E-04  1.48728E-04  7.55014E-05  4.80520E-05  2.77000E-05  1.59680E-05  9.87700E-06  4.00000E-06  3.30000E-06  2.60000E-06  2.10000E-06  1.85500E-06  1.50000E-06  1.30000E-06  1.15000E-06  1.12300E-06  1.09700E-06  1.07100E-06  1.04500E-06  1.02000E-06  9.96000E-07  9.72000E-07  9.50000E-07  9.10000E-07  8.50000E-07  7.80000E-07  6.25000E-07  5.00000E-07  4.00000E-07  3.50000E-07  3.20000E-07  3.00000E-07  2.80000E-07  2.50000E-07  2.20000E-07  1.80000E-07  1.40000E-07  1.00000E-07  8.00000E-08  6.70000E-08  5.80000E-08  5.00000E-08  4.20000E-08  3.50000E-08  3.00000E-08  2.50000E-08  2.00000E-08  1.50000E-08  1.00000E-08  5.00000E-09  1.00000E-11 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Micro-group spectrum:

INF_MICRO_FLX             (idx, [1: 140]) = [  6.03251E+03 0.00633  2.51912E+04 0.00379  5.35612E+04 0.00301  5.65484E+04 0.00195  5.42987E+04 0.00188  6.56639E+04 0.00176  4.40401E+04 0.00202  4.10295E+04 0.00281  3.06030E+04 0.00284  2.48604E+04 0.00198  2.14736E+04 0.00221  1.91179E+04 0.00302  1.76856E+04 0.00325  1.67102E+04 0.00379  1.61990E+04 0.00312  1.38888E+04 0.00303  1.36444E+04 0.00298  1.34361E+04 0.00325  1.30381E+04 0.00295  2.52607E+04 0.00256  2.38273E+04 0.00256  1.67286E+04 0.00250  1.06350E+04 0.00267  1.18100E+04 0.00335  1.06697E+04 0.00396  1.03260E+04 0.00419  1.51834E+04 0.00300  3.72539E+03 0.00591  4.69817E+03 0.00564  4.27434E+03 0.00556  2.47109E+03 0.00657  4.34819E+03 0.00649  2.96704E+03 0.00547  2.49568E+03 0.00638  4.64506E+02 0.01551  4.63179E+02 0.01577  4.71776E+02 0.01489  4.82395E+02 0.02051  4.82982E+02 0.01204  4.66210E+02 0.01714  4.97272E+02 0.01147  4.65157E+02 0.01686  8.85073E+02 0.01074  1.41300E+03 0.00731  1.79569E+03 0.00858  4.70047E+03 0.00616  4.93897E+03 0.00515  5.19461E+03 0.00546  3.33647E+03 0.00622  2.38152E+03 0.00815  1.78029E+03 0.00998  2.05299E+03 0.00671  3.70299E+03 0.00617  4.69184E+03 0.00453  8.49024E+03 0.00405  1.20229E+04 0.00339  1.65954E+04 0.00257  1.00069E+04 0.00297  6.95292E+03 0.00345  4.86725E+03 0.00382  4.27484E+03 0.00411  4.10216E+03 0.00425  3.37339E+03 0.00484  2.23441E+03 0.00542  2.01823E+03 0.00413  1.75729E+03 0.00603  1.44809E+03 0.00587  1.10244E+03 0.00699  6.89168E+02 0.00886  2.11210E+02 0.01279 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.22203E+00 0.00108 ];

% Flux spectra in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  1.77146E+01 0.00086  2.70391E+00 0.00112 ];
INF_FISS_FLX              (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  4.26674E-01 0.00023  5.95918E-01 0.00019 ];
INF_CAPT                  (idx, [1:   4]) = [  1.91677E-02 0.00124  5.53120E-02 0.00050 ];
INF_ABS                   (idx, [1:   4]) = [  2.56875E-02 0.00094  1.89409E-01 0.00055 ];
INF_FISS                  (idx, [1:   4]) = [  6.51980E-03 0.00083  1.34097E-01 0.00057 ];
INF_NSF                   (idx, [1:   4]) = [  1.68175E-02 0.00086  3.26688E-01 0.00057 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.57944E+00 0.00010  2.43620E+00 2.7E-09 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.03634E+02 8.3E-06  2.02270E+02 3.8E-09 ];
INF_INVV                  (idx, [1:   4]) = [  5.35213E-08 0.00146  2.32072E-06 0.00049 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  4.00986E-01 0.00026  4.05984E-01 0.00063 ];
INF_SCATT1                (idx, [1:   4]) = [  4.32833E-02 0.00217  8.22010E-03 0.02557 ];
INF_SCATT2                (idx, [1:   4]) = [  2.29187E-02 0.00358  4.80927E-04 0.34838 ];
INF_SCATT3                (idx, [1:   4]) = [  1.17803E-02 0.00586 -3.96699E-05 1.00000 ];
INF_SCATT4                (idx, [1:   4]) = [  7.44667E-03 0.00715 -5.10234E-05 1.00000 ];
INF_SCATT5                (idx, [1:   4]) = [  3.90344E-03 0.01343  9.53560E-05 1.00000 ];
INF_SCATT6                (idx, [1:   4]) = [  1.94938E-03 0.02043 -1.47905E-05 1.00000 ];
INF_SCATT7                (idx, [1:   4]) = [  8.24576E-04 0.05778 -3.81349E-05 1.00000 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  4.01097E-01 0.00026  4.05984E-01 0.00063 ];
INF_SCATTP1               (idx, [1:   4]) = [  4.32837E-02 0.00218  8.22010E-03 0.02557 ];
INF_SCATTP2               (idx, [1:   4]) = [  2.29193E-02 0.00358  4.80927E-04 0.34838 ];
INF_SCATTP3               (idx, [1:   4]) = [  1.17815E-02 0.00589 -3.96699E-05 1.00000 ];
INF_SCATTP4               (idx, [1:   4]) = [  7.44655E-03 0.00715 -5.10234E-05 1.00000 ];
INF_SCATTP5               (idx, [1:   4]) = [  3.90357E-03 0.01338  9.53560E-05 1.00000 ];
INF_SCATTP6               (idx, [1:   4]) = [  1.94945E-03 0.02045 -1.47905E-05 1.00000 ];
INF_SCATTP7               (idx, [1:   4]) = [  8.23772E-04 0.05810 -3.81349E-05 1.00000 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  3.14080E-01 0.00060  5.69411E-01 0.00042 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.06131E+00 0.00060  5.85403E-01 0.00042 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  2.55764E-02 0.00092  1.89409E-01 0.00055 ];
INF_REMXS                 (idx, [1:   4]) = [  2.64821E-02 0.00136  1.91676E-01 0.00136 ];

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

INF_S0                    (idx, [1:   8]) = [  4.00192E-01 0.00026  7.93999E-04 0.00794  1.74231E-03 0.01536  4.04242E-01 0.00065 ];
INF_S1                    (idx, [1:   8]) = [  4.34685E-02 0.00215 -1.85270E-04 0.02110 -1.50082E-04 0.08848  8.37019E-03 0.02523 ];
INF_S2                    (idx, [1:   8]) = [  2.29401E-02 0.00354 -2.14247E-05 0.13669 -7.56458E-05 0.14374  5.56573E-04 0.29841 ];
INF_S3                    (idx, [1:   8]) = [  1.17821E-02 0.00587 -1.77981E-06 1.00000 -2.37532E-05 0.24114 -1.59167E-05 1.00000 ];
INF_S4                    (idx, [1:   8]) = [  7.45002E-03 0.00722 -3.34398E-06 0.54630 -2.50037E-05 0.30630 -2.60197E-05 1.00000 ];
INF_S5                    (idx, [1:   8]) = [  3.90761E-03 0.01324 -4.17610E-06 0.36956 -1.31969E-05 0.51758  1.08553E-04 0.90216 ];
INF_S6                    (idx, [1:   8]) = [  1.95031E-03 0.02044 -9.26737E-07 1.00000 -1.70609E-05 0.36304  2.27039E-06 1.00000 ];
INF_S7                    (idx, [1:   8]) = [  8.23446E-04 0.05848  1.13039E-06 1.00000  2.56891E-06 1.00000 -4.07038E-05 1.00000 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  4.00303E-01 0.00026  7.93999E-04 0.00794  1.74231E-03 0.01536  4.04242E-01 0.00065 ];
INF_SP1                   (idx, [1:   8]) = [  4.34690E-02 0.00216 -1.85270E-04 0.02110 -1.50082E-04 0.08848  8.37019E-03 0.02523 ];
INF_SP2                   (idx, [1:   8]) = [  2.29407E-02 0.00354 -2.14247E-05 0.13669 -7.56458E-05 0.14374  5.56573E-04 0.29841 ];
INF_SP3                   (idx, [1:   8]) = [  1.17833E-02 0.00590 -1.77981E-06 1.00000 -2.37532E-05 0.24114 -1.59167E-05 1.00000 ];
INF_SP4                   (idx, [1:   8]) = [  7.44990E-03 0.00721 -3.34398E-06 0.54630 -2.50037E-05 0.30630 -2.60197E-05 1.00000 ];
INF_SP5                   (idx, [1:   8]) = [  3.90775E-03 0.01320 -4.17610E-06 0.36956 -1.31969E-05 0.51758  1.08553E-04 0.90216 ];
INF_SP6                   (idx, [1:   8]) = [  1.95037E-03 0.02047 -9.26737E-07 1.00000 -1.70609E-05 0.36304  2.27039E-06 1.00000 ];
INF_SP7                   (idx, [1:   8]) = [  8.22642E-04 0.05879  1.13039E-06 1.00000  2.56891E-06 1.00000 -4.07038E-05 1.00000 ];

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

CMM_TRANSPXS              (idx, [1:   4]) = [  2.60805E-01 0.00324  8.98297E-01 0.00908 ];
CMM_TRANSPXS_X            (idx, [1:   4]) = [  2.60202E-01 0.00390  9.24992E-01 0.01558 ];
CMM_TRANSPXS_Y            (idx, [1:   4]) = [  2.59644E-01 0.00417  9.15212E-01 0.02047 ];
CMM_TRANSPXS_Z            (idx, [1:   4]) = [  2.62708E-01 0.00424  8.72044E-01 0.01894 ];
CMM_DIFFCOEF              (idx, [1:   4]) = [  1.27841E+00 0.00322  3.71816E-01 0.00918 ];
CMM_DIFFCOEF_X            (idx, [1:   4]) = [  1.28152E+00 0.00390  3.62420E-01 0.01525 ];
CMM_DIFFCOEF_Y            (idx, [1:   4]) = [  1.28434E+00 0.00414  3.67632E-01 0.01910 ];
CMM_DIFFCOEF_Z            (idx, [1:   4]) = [  1.26938E+00 0.00420  3.85396E-01 0.01814 ];

% Delayed neutron parameters (Meulekamp method):

BETA_EFF                  (idx, [1:  18]) = [  7.55444E-03 0.01669  2.30208E-04 0.09947  1.10556E-03 0.04419  5.64378E-04 0.05971  1.32564E-03 0.04364  2.44331E-03 0.03102  8.03816E-04 0.05212  7.91714E-04 0.05627  2.89812E-04 0.09168 ];
LAMBDA                    (idx, [1:  18]) = [  4.92823E-01 0.02578  1.24667E-02 0.0E+00  2.82917E-02 0.0E+00  4.25244E-02 5.7E-09  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 5.3E-09  3.55460E+00 0.0E+00 ];


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
INPUT_FILE_NAME           (idx, [1:135])  = '/home/hirepan/Documents/chalmers/Project/codes/Shynt/repo/cases/single_assem_1x1cell/serpent_files/global_cell_type1/XS_generation.serp' ;
WORKING_DIRECTORY         (idx, [1: 84])  = '/home/hirepan/Documents/chalmers/Project/codes/Shynt/repo/cases/single_assem_1x1cell' ;
HOSTNAME                  (idx, [1:  4])  = 'thor' ;
CPU_TYPE                  (idx, [1: 40])  = 'Intel(R) Core(TM) i9-10900 CPU @ 2.80GHz' ;
CPU_MHZ                   (idx, 1)        = 236.0 ;
START_DATE                (idx, [1: 24])  = 'Thu Mar 10 11:48:05 2022' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Mar 10 11:48:16 2022' ;

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
OMP_HISTORY_PROFILE       (idx, [1:  18]) = [  9.71080E-01  9.89865E-01  1.01372E+00  1.00808E+00  9.90600E-01  1.00075E+00  1.00719E+00  9.68595E-01  1.02335E+00  1.01798E+00  1.00083E+00  1.00647E+00  9.77440E-01  9.94786E-01  1.03211E+00  1.00584E+00  1.00366E+00  9.87641E-01  ];
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
ST_FRAC                   (idx, [1:   4]) = [  8.03144E-03 0.00293  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.91969E-01 2.4E-05  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  8.31084E-01 9.7E-05  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  8.31455E-01 9.7E-05  0.00000E+00 0.0E+00 ];
AVG_TRACKING_LOOPS        (idx, [1:   8]) = [  2.38074E+00 0.00039  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  2.82207E+01 0.00058  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  2.82207E+01 0.00058  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  5.72069E+00 0.00077  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  1.99542E-01 0.00326  0.00000E+00 0.0E+00 ];
LOST_PARTICLES            (idx, 1)        = 0 ;

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 500 ;
SIMULATED_HISTORIES       (idx, 1)        = 1000567 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  2.00113E+03 0.00149 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  2.00113E+03 0.00149 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  3.05164E+00 ;
RUNNING_TIME              (idx, 1)        =  1.85100E-01 ;
INIT_TIME                 (idx, [1:  2])  = [  1.20000E-02  1.20000E-02 ];
PROCESS_TIME              (idx, [1:  2])  = [  1.16666E-04  1.16666E-04 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  1.72917E-01  1.72917E-01  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  1.84983E-01  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 16.48645 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  1.76992E+01 0.00452 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  8.22708E-01 ;

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

NORM_COEF                 (idx, [1:   4]) = [  4.99684E-04 0.00082  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  7.26312E-01 0.00207 ];
U235_FISS                 (idx, [1:   4]) = [  4.37257E-01 0.00118  9.12387E-01 0.00044 ];
U238_FISS                 (idx, [1:   4]) = [  4.20104E-02 0.00492  8.76129E-02 0.00456 ];
U235_CAPT                 (idx, [1:   4]) = [  9.82385E-02 0.00311  1.88181E-01 0.00285 ];
U238_CAPT                 (idx, [1:   4]) = [  3.88684E-01 0.00159  7.44512E-01 0.00083 ];

% Neutron balance (particles/weight):

BALA_SRC_NEUTRON_SRC     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_FISS    (idx, [1:  2])  = [ 1000567 1.00000E+06 ];
BALA_SRC_NEUTRON_NXN     (idx, [1:  2])  = [ 0 1.96877E+03 ];
BALA_SRC_NEUTRON_VR      (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_TOT     (idx, [1:  2])  = [ 1000567 1.00197E+06 ];

BALA_LOSS_NEUTRON_CAPT    (idx, [1:  2])  = [ 521576 5.22360E+05 ];
BALA_LOSS_NEUTRON_FISS    (idx, [1:  2])  = [ 478991 4.79609E+05 ];
BALA_LOSS_NEUTRON_LEAK    (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_CUT     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_ERR     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_TOT     (idx, [1:  2])  = [ 1000567 1.00197E+06 ];

BALA_NEUTRON_DIFF         (idx, [1:  2])  = [ 0 -1.04774E-09 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.55124E-11 0.00055 ];
TOT_POWDENS               (idx, [1:   2]) = [  2.85953E-15 0.00055 ];
TOT_GENRATE               (idx, [1:   2]) = [  1.18079E+00 0.00054 ];
TOT_FISSRATE              (idx, [1:   2]) = [  4.77893E-01 0.00055 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  5.22107E-01 0.00050 ];
TOT_ABSRATE               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.99369E-01 0.00082 ];
TOT_FLUX                  (idx, [1:   2]) = [  5.80501E+01 0.00065 ];
TOT_PHOTON_PRODRATE       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  2.82522E+01 0.00051 ];
INI_FMASS                 (idx, 1)        =  5.42481E-03 ;
TOT_FMASS                 (idx, 1)        =  5.42481E-03 ;

% Six-factor formula:

SIX_FF_ETA                (idx, [1:   2]) = [  1.72520E+00 0.00089 ];
SIX_FF_F                  (idx, [1:   2]) = [  9.49173E-01 0.00031 ];
SIX_FF_P                  (idx, [1:   2]) = [  5.41403E-01 0.00092 ];
SIX_FF_EPSILON            (idx, [1:   2]) = [  1.33692E+00 0.00083 ];
SIX_FF_LF                 (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
SIX_FF_LT                 (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
SIX_FF_KINF               (idx, [1:   2]) = [  1.18485E+00 0.00103 ];
SIX_FF_KEFF               (idx, [1:   2]) = [  1.18485E+00 0.00103 ];

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.47082E+00 3.5E-05 ];
FISSE                     (idx, [1:   2]) = [  2.02600E+02 3.0E-06 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.18492E+00 0.00104  1.17606E+00 0.00104  8.79039E-03 0.01698 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.18308E+00 0.00055 ];
COL_KEFF                  (idx, [1:   2]) = [  1.18201E+00 0.00111 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.18308E+00 0.00055 ];
ABS_KINF                  (idx, [1:   2]) = [  1.18308E+00 0.00055 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% ALF (Average lethargy of neutrons causing fission):
% Based on E0 = 2.000000E+01 MeV

ANA_ALF                   (idx, [1:   2]) = [  1.68623E+01 0.00046 ];
IMP_ALF                   (idx, [1:   2]) = [  1.68572E+01 0.00023 ];

% EALF (Energy corresponding to average lethargy of neutrons causing fission):

ANA_EALF                  (idx, [1:   2]) = [  9.64569E-07 0.00792 ];
IMP_EALF                  (idx, [1:   2]) = [  9.58570E-07 0.00384 ];

% AFGE (Average energy of neutrons causing fission):

ANA_AFGE                  (idx, [1:   2]) = [  2.87715E-01 0.00504 ];
IMP_AFGE                  (idx, [1:   2]) = [  2.90487E-01 0.00232 ];

% Forward-weighted delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
FWD_ANA_BETA_ZERO         (idx, [1:  18]) = [  6.68122E-03 0.01137  1.90005E-04 0.06459  9.96050E-04 0.02928  5.42166E-04 0.03930  1.21686E-03 0.02818  2.10645E-03 0.02085  7.29006E-04 0.03346  6.54989E-04 0.03392  2.45698E-04 0.05781 ];
FWD_ANA_LAMBDA            (idx, [1:  18]) = [  4.86359E-01 0.01760  4.63761E-03 0.05816  2.56889E-02 0.01425  3.12129E-02 0.02695  1.24793E-01 0.01151  2.89543E-01 0.00450  5.59850E-01 0.01954  1.32090E+00 0.02182  1.57113E+00 0.05030 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  18]) = [  7.55444E-03 0.01669  2.30208E-04 0.09947  1.10556E-03 0.04419  5.64378E-04 0.05971  1.32564E-03 0.04364  2.44331E-03 0.03102  8.03816E-04 0.05212  7.91714E-04 0.05627  2.89812E-04 0.09168 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  18]) = [  4.92823E-01 0.02578  1.24667E-02 0.0E+00  2.82917E-02 0.0E+00  4.25244E-02 5.7E-09  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 5.3E-09  3.55460E+00 0.0E+00 ];

% Adjoint weighted time constants using Nauchi's method:

IFP_CHAIN_LENGTH          (idx, 1)        = 15 ;
ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  2.53694E-05 0.00239  2.53433E-05 0.00239  2.89435E-05 0.02300 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  3.00435E-05 0.00212  3.00128E-05 0.00213  3.42632E-05 0.02290 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  18]) = [  7.40377E-03 0.01697  1.98024E-04 0.09897  1.08352E-03 0.04443  5.77174E-04 0.05871  1.36039E-03 0.03889  2.29523E-03 0.03166  8.42009E-04 0.04715  7.52638E-04 0.04946  2.94793E-04 0.08054 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  18]) = [  5.12213E-01 0.02932  1.24667E-02 0.0E+00  2.82917E-02 3.6E-09  4.25244E-02 8.2E-09  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 5.4E-09  3.55460E+00 4.8E-09 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  2.54854E-05 0.00513  2.54674E-05 0.00518  1.94520E-05 0.05425 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  3.01838E-05 0.00507  3.01626E-05 0.00512  2.29833E-05 0.05409 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  18]) = [  6.81794E-03 0.05381  1.57905E-04 0.33712  9.86338E-04 0.13172  4.10468E-04 0.19336  1.18557E-03 0.11977  2.33325E-03 0.09646  7.79753E-04 0.14279  7.59195E-04 0.16378  2.05459E-04 0.25978 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  18]) = [  5.30974E-01 0.06832  1.24667E-02 3.9E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 3.5E-09  2.92467E-01 5.3E-09  6.66488E-01 5.1E-09  1.63478E+00 0.0E+00  3.55460E+00 3.8E-09 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  18]) = [  6.83986E-03 0.05110  1.55014E-04 0.34108  1.00176E-03 0.12335  3.86747E-04 0.19768  1.18043E-03 0.11343  2.37345E-03 0.09213  7.41320E-04 0.14339  7.76845E-04 0.15349  2.24290E-04 0.24835 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  18]) = [  5.34122E-01 0.06772  1.24667E-02 3.9E-09  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 3.2E-09  2.92467E-01 5.3E-09  6.66488E-01 5.1E-09  1.63478E+00 0.0E+00  3.55460E+00 6.0E-09 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -2.72932E+02 0.05476 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  2.54348E-05 0.00154 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  3.01214E-05 0.00111 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  7.37196E-03 0.01019 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -2.90211E+02 0.01030 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  3.76458E-07 0.00118 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  4.23960E-06 0.00102  4.23894E-06 0.00103  4.33632E-06 0.01177 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  3.53373E-05 0.00129  3.53348E-05 0.00129  3.60477E-05 0.01602 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.41905E-01 0.00092  5.41026E-01 0.00093  7.13035E-01 0.01845 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.19355E+01 0.02484 ];
ANA_MEAN_NCOL             (idx, [1:   4]) = [  2.82207E+01 0.00058  3.19840E+01 0.00077 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  7])  = 'u4gcu_2' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  2.00000E+01  6.06550E+00  3.67900E+00  2.23100E+00  1.35300E+00  8.21000E-01  5.00000E-01  3.02500E-01  1.83000E-01  1.11000E-01  6.74300E-02  4.08500E-02  2.47800E-02  1.50300E-02  9.11800E-03  5.50000E-03  3.51910E-03  2.23945E-03  1.42510E-03  9.06898E-04  3.67262E-04  1.48728E-04  7.55014E-05  4.80520E-05  2.77000E-05  1.59680E-05  9.87700E-06  4.00000E-06  3.30000E-06  2.60000E-06  2.10000E-06  1.85500E-06  1.50000E-06  1.30000E-06  1.15000E-06  1.12300E-06  1.09700E-06  1.07100E-06  1.04500E-06  1.02000E-06  9.96000E-07  9.72000E-07  9.50000E-07  9.10000E-07  8.50000E-07  7.80000E-07  6.25000E-07  5.00000E-07  4.00000E-07  3.50000E-07  3.20000E-07  3.00000E-07  2.80000E-07  2.50000E-07  2.20000E-07  1.80000E-07  1.40000E-07  1.00000E-07  8.00000E-08  6.70000E-08  5.80000E-08  5.00000E-08  4.20000E-08  3.50000E-08  3.00000E-08  2.50000E-08  2.00000E-08  1.50000E-08  1.00000E-08  5.00000E-09  1.00000E-11 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Micro-group spectrum:

INF_MICRO_FLX             (idx, [1: 140]) = [  1.07221E+04 0.00841  4.49764E+04 0.00372  9.48083E+04 0.00260  9.95033E+04 0.00222  9.55073E+04 0.00183  1.15107E+05 0.00175  7.80717E+04 0.00150  7.26388E+04 0.00185  5.53565E+04 0.00161  4.53135E+04 0.00179  3.91996E+04 0.00123  3.50713E+04 0.00131  3.25794E+04 0.00124  3.08898E+04 0.00169  3.00109E+04 0.00182  2.58302E+04 0.00188  2.55450E+04 0.00161  2.51770E+04 0.00170  2.45148E+04 0.00154  4.74106E+04 0.00144  4.53628E+04 0.00137  3.21721E+04 0.00154  2.05106E+04 0.00187  2.32827E+04 0.00217  2.14981E+04 0.00182  1.93965E+04 0.00190  3.07506E+04 0.00141  6.96549E+03 0.00316  8.73101E+03 0.00305  7.95147E+03 0.00318  4.62928E+03 0.00371  8.03345E+03 0.00357  5.45878E+03 0.00445  4.62232E+03 0.00379  8.84937E+02 0.00863  8.78245E+02 0.00654  9.02707E+02 0.00864  9.26861E+02 0.00786  9.17132E+02 0.00696  8.96536E+02 0.00873  9.39503E+02 0.00856  8.76116E+02 0.00994  1.66201E+03 0.00531  2.63126E+03 0.00481  3.38575E+03 0.00465  8.85302E+03 0.00321  9.25219E+03 0.00278  9.79860E+03 0.00242  6.37764E+03 0.00435  4.56681E+03 0.00411  3.43343E+03 0.00415  3.92420E+03 0.00265  7.12766E+03 0.00352  9.07457E+03 0.00297  1.63150E+04 0.00234  2.33149E+04 0.00215  3.25858E+04 0.00175  1.99406E+04 0.00221  1.39867E+04 0.00248  9.88418E+03 0.00238  8.77003E+03 0.00254  8.52065E+03 0.00239  7.07478E+03 0.00267  4.76279E+03 0.00316  4.36909E+03 0.00300  3.85560E+03 0.00236  3.25431E+03 0.00369  2.57712E+03 0.00287  1.74267E+03 0.00387  6.30472E+02 0.00484 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];

% Flux spectra in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  3.22634E+01 0.00082  5.37500E+00 0.00092 ];
INF_FISS_FLX              (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  4.07119E-01 0.00032  1.10746E+00 0.00019 ];
INF_CAPT                  (idx, [1:   4]) = [  1.63677E-04 0.00138  5.18297E-03 0.00033 ];
INF_ABS                   (idx, [1:   4]) = [  1.63677E-04 0.00138  5.18297E-03 0.00033 ];
INF_FISS                  (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_NSF                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_NUBAR                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_KAPPA                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_INVV                  (idx, [1:   4]) = [  5.58642E-08 0.00099  2.38733E-06 0.00033 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  4.06957E-01 0.00032  1.10235E+00 0.00018 ];
INF_SCATT1                (idx, [1:   4]) = [  2.37975E-01 0.00035  3.30256E-01 0.00078 ];
INF_SCATT2                (idx, [1:   4]) = [  9.10550E-02 0.00078  8.32519E-02 0.00336 ];
INF_SCATT3                (idx, [1:   4]) = [  2.89269E-03 0.01405  2.48589E-02 0.00686 ];
INF_SCATT4                (idx, [1:   4]) = [ -1.38605E-02 0.00293 -5.85452E-03 0.02894 ];
INF_SCATT5                (idx, [1:   4]) = [ -1.24062E-03 0.03214  4.81318E-03 0.02994 ];
INF_SCATT6                (idx, [1:   4]) = [  4.63713E-03 0.00838 -1.28888E-02 0.00843 ];
INF_SCATT7                (idx, [1:   4]) = [  4.29415E-04 0.07625 -4.61541E-04 0.27275 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  4.06957E-01 0.00032  1.10235E+00 0.00018 ];
INF_SCATTP1               (idx, [1:   4]) = [  2.37975E-01 0.00035  3.30256E-01 0.00078 ];
INF_SCATTP2               (idx, [1:   4]) = [  9.10550E-02 0.00078  8.32519E-02 0.00336 ];
INF_SCATTP3               (idx, [1:   4]) = [  2.89269E-03 0.01405  2.48589E-02 0.00686 ];
INF_SCATTP4               (idx, [1:   4]) = [ -1.38605E-02 0.00293 -5.85452E-03 0.02894 ];
INF_SCATTP5               (idx, [1:   4]) = [ -1.24062E-03 0.03214  4.81318E-03 0.02994 ];
INF_SCATTP6               (idx, [1:   4]) = [  4.63713E-03 0.00838 -1.28888E-02 0.00843 ];
INF_SCATTP7               (idx, [1:   4]) = [  4.29415E-04 0.07625 -4.61541E-04 0.27275 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  1.07248E-01 0.00094  6.65358E-01 0.00054 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  3.10812E+00 0.00094  5.00987E-01 0.00054 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  1.63677E-04 0.00138  5.18297E-03 0.00033 ];
INF_REMXS                 (idx, [1:   4]) = [  1.68477E-02 0.00107  6.34957E-03 0.00436 ];

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

INF_S0                    (idx, [1:   8]) = [  3.90272E-01 0.00031  1.66855E-02 0.00107  1.23223E-03 0.01233  1.10111E+00 0.00019 ];
INF_S1                    (idx, [1:   8]) = [  2.32989E-01 0.00035  4.98649E-03 0.00197  7.86534E-04 0.01199  3.29470E-01 0.00077 ];
INF_S2                    (idx, [1:   8]) = [  9.25355E-02 0.00077 -1.48045E-03 0.00497  4.26414E-04 0.01634  8.28255E-02 0.00339 ];
INF_S3                    (idx, [1:   8]) = [  4.62033E-03 0.00914 -1.72764E-03 0.00424  1.50362E-04 0.04143  2.47085E-02 0.00686 ];
INF_S4                    (idx, [1:   8]) = [ -1.32964E-02 0.00316 -5.64104E-04 0.01201  8.41122E-06 0.71702 -5.86293E-03 0.02874 ];
INF_S5                    (idx, [1:   8]) = [ -1.25477E-03 0.03072  1.41535E-05 0.33486 -5.35267E-05 0.07911  4.86670E-03 0.02985 ];
INF_S6                    (idx, [1:   8]) = [  4.77418E-03 0.00791 -1.37042E-04 0.03803 -6.59863E-05 0.04805 -1.28228E-02 0.00856 ];
INF_S7                    (idx, [1:   8]) = [  5.91645E-04 0.05382 -1.62230E-04 0.03080 -5.94631E-05 0.06479 -4.02078E-04 0.31596 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  3.90272E-01 0.00031  1.66855E-02 0.00107  1.23223E-03 0.01233  1.10111E+00 0.00019 ];
INF_SP1                   (idx, [1:   8]) = [  2.32989E-01 0.00035  4.98649E-03 0.00197  7.86534E-04 0.01199  3.29470E-01 0.00077 ];
INF_SP2                   (idx, [1:   8]) = [  9.25355E-02 0.00077 -1.48045E-03 0.00497  4.26414E-04 0.01634  8.28255E-02 0.00339 ];
INF_SP3                   (idx, [1:   8]) = [  4.62033E-03 0.00914 -1.72764E-03 0.00424  1.50362E-04 0.04143  2.47085E-02 0.00686 ];
INF_SP4                   (idx, [1:   8]) = [ -1.32964E-02 0.00316 -5.64104E-04 0.01201  8.41122E-06 0.71702 -5.86293E-03 0.02874 ];
INF_SP5                   (idx, [1:   8]) = [ -1.25477E-03 0.03072  1.41535E-05 0.33486 -5.35267E-05 0.07911  4.86670E-03 0.02985 ];
INF_SP6                   (idx, [1:   8]) = [  4.77418E-03 0.00791 -1.37042E-04 0.03803 -6.59863E-05 0.04805 -1.28228E-02 0.00856 ];
INF_SP7                   (idx, [1:   8]) = [  5.91645E-04 0.05382 -1.62230E-04 0.03080 -5.94631E-05 0.06479 -4.02078E-04 0.31596 ];

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

CMM_TRANSPXS              (idx, [1:   4]) = [  1.23362E-01 0.00136  3.95964E-01 0.00430 ];
CMM_TRANSPXS_X            (idx, [1:   4]) = [  1.23443E-01 0.00252  3.94933E-01 0.00725 ];
CMM_TRANSPXS_Y            (idx, [1:   4]) = [  1.23589E-01 0.00162  3.95787E-01 0.00792 ];
CMM_TRANSPXS_Z            (idx, [1:   4]) = [  1.23076E-01 0.00188  3.98411E-01 0.00819 ];
CMM_DIFFCOEF              (idx, [1:   4]) = [  2.70219E+00 0.00136  8.42203E-01 0.00431 ];
CMM_DIFFCOEF_X            (idx, [1:   4]) = [  2.70072E+00 0.00251  8.45092E-01 0.00726 ];
CMM_DIFFCOEF_Y            (idx, [1:   4]) = [  2.69727E+00 0.00163  8.43495E-01 0.00805 ];
CMM_DIFFCOEF_Z            (idx, [1:   4]) = [  2.70858E+00 0.00188  8.38023E-01 0.00831 ];

% Delayed neutron parameters (Meulekamp method):

BETA_EFF                  (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
LAMBDA                    (idx, [1:  18]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

