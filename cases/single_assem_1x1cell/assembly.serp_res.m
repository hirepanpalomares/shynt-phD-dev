
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
TITLE                     (idx, [1: 16])  = 'Single+fuel+cell' ;
CONFIDENTIAL_DATA         (idx, 1)        = 0 ;
INPUT_FILE_NAME           (idx, [1: 13])  = 'assembly.serp' ;
WORKING_DIRECTORY         (idx, [1: 84])  = '/home/hirepan/Documents/chalmers/Project/codes/Shynt/repo/cases/single_assem_1x1cell' ;
HOSTNAME                  (idx, [1:  4])  = 'thor' ;
CPU_TYPE                  (idx, [1: 40])  = 'Intel(R) Core(TM) i9-10900 CPU @ 2.80GHz' ;
CPU_MHZ                   (idx, 1)        = 236.0 ;
START_DATE                (idx, [1: 24])  = 'Wed May 11 13:26:44 2022' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Wed May 11 13:33:05 2022' ;

% Run parameters:

POP                       (idx, 1)        = 100000 ;
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
OMP_THREADS               (idx, 1)        = 15 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:  15]) = [  1.15816E+00  1.07874E+00  1.22896E+00  9.37656E-01  8.99181E-01  1.09435E+00  1.09310E+00  9.73143E-01  9.37447E-01  9.55659E-01  9.91086E-01  9.42685E-01  9.10736E-01  8.63065E-01  9.36032E-01  ];
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

MIN_MACROXS               (idx, [1:   4]) = [  5.00000E-02 1.1E-09  0.00000E+00 0.0E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  8.62239E-03 0.00040  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.91378E-01 3.5E-06  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  8.35920E-01 1.6E-05  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  8.36308E-01 1.6E-05  0.00000E+00 0.0E+00 ];
AVG_TRACKING_LOOPS        (idx, [1:   8]) = [  2.32925E+00 5.4E-05  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  2.56798E+01 7.3E-05  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  2.56798E+01 7.3E-05  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  5.02636E+00 0.00011  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  1.93952E-01 0.00047  0.00000E+00 0.0E+00 ];
LOST_PARTICLES            (idx, 1)        = 0 ;

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 500 ;
SIMULATED_HISTORIES       (idx, 1)        = 50000462 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  1.00001E+05 0.00020 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  1.00001E+05 0.00020 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  8.72261E+01 ;
RUNNING_TIME              (idx, 1)        =  6.34790E+00 ;
INIT_TIME                 (idx, [1:  2])  = [  1.65500E-02  1.65500E-02 ];
PROCESS_TIME              (idx, [1:  2])  = [  1.16670E-04  1.16670E-04 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  6.33123E+00  6.33123E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  6.34768E+00  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 13.74094 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  1.38008E+01 0.00019 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  8.90785E-01 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 64024.21 ;
ALLOC_MEMSIZE             (idx, 1)        = 920.62;
MEMSIZE                   (idx, 1)        = 757.50;
XS_MEMSIZE                (idx, 1)        = 68.06;
MAT_MEMSIZE               (idx, 1)        = 20.07;
RES_MEMSIZE               (idx, 1)        = 1.43;
IFC_MEMSIZE               (idx, 1)        = 0.00;
MISC_MEMSIZE              (idx, 1)        = 667.94;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 163.11;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 2 ;
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

NORM_COEF                 (idx, [1:   4]) = [  9.98422E-06 0.00011  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  5.87976E-01 0.00032 ];
U235_FISS                 (idx, [1:   4]) = [  4.72109E-01 0.00016  9.19242E-01 5.9E-05 ];
U238_FISS                 (idx, [1:   4]) = [  4.14765E-02 0.00071  8.07579E-02 0.00067 ];
U235_CAPT                 (idx, [1:   4]) = [  1.15133E-01 0.00042  2.36520E-01 0.00039 ];
U238_CAPT                 (idx, [1:   4]) = [  3.45310E-01 0.00025  7.09373E-01 0.00014 ];

% Neutron balance (particles/weight):

BALA_SRC_NEUTRON_SRC     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_FISS    (idx, [1:  2])  = [ 50000462 5.00000E+07 ];
BALA_SRC_NEUTRON_NXN     (idx, [1:  2])  = [ 0 9.74029E+04 ];
BALA_SRC_NEUTRON_VR      (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_TOT     (idx, [1:  2])  = [ 50000462 5.00974E+07 ];

BALA_LOSS_NEUTRON_CAPT    (idx, [1:  2])  = [ 24328543 2.43775E+07 ];
BALA_LOSS_NEUTRON_FISS    (idx, [1:  2])  = [ 25671919 2.57199E+07 ];
BALA_LOSS_NEUTRON_LEAK    (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_CUT     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_ERR     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_TOT     (idx, [1:  2])  = [ 50000462 5.00974E+07 ];

BALA_NEUTRON_DIFF         (idx, [1:  2])  = [ 0 3.32296E-06 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.66605E-11 7.5E-05 ];
TOT_POWDENS               (idx, [1:   2]) = [  3.07117E-17 7.5E-05 ];
TOT_GENRATE               (idx, [1:   2]) = [  1.26736E+00 7.4E-05 ];
TOT_FISSRATE              (idx, [1:   2]) = [  5.13331E-01 7.6E-05 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  4.86669E-01 8.0E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.98422E-01 0.00011 ];
TOT_FLUX                  (idx, [1:   2]) = [  5.49603E+01 9.6E-05 ];
TOT_PHOTON_PRODRATE       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  2.56877E+01 7.6E-05 ];
INI_FMASS                 (idx, 1)        =  5.42481E-01 ;
TOT_FMASS                 (idx, 1)        =  5.42481E-01 ;

% Six-factor formula:

SIX_FF_ETA                (idx, [1:   2]) = [  1.83324E+00 0.00011 ];
SIX_FF_F                  (idx, [1:   2]) = [  9.62433E-01 3.9E-05 ];
SIX_FF_P                  (idx, [1:   2]) = [  5.02455E-01 0.00014 ];
SIX_FF_EPSILON            (idx, [1:   2]) = [  1.43258E+00 0.00013 ];
SIX_FF_LF                 (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
SIX_FF_LT                 (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
SIX_FF_KINF               (idx, [1:   2]) = [  1.26999E+00 0.00013 ];
SIX_FF_KEFF               (idx, [1:   2]) = [  1.26999E+00 0.00013 ];

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.46890E+00 5.0E-06 ];
FISSE                     (idx, [1:   2]) = [  2.02573E+02 4.2E-07 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.26997E+00 0.00014  1.26091E+00 0.00014  9.08680E-03 0.00228 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.26984E+00 7.4E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.26938E+00 0.00015 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.26984E+00 7.4E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.26984E+00 7.4E-05 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% ALF (Average lethargy of neutrons causing fission):
% Based on E0 = 2.000000E+01 MeV

ANA_ALF                   (idx, [1:   2]) = [  1.64800E+01 6.4E-05 ];
IMP_ALF                   (idx, [1:   2]) = [  1.64794E+01 3.5E-05 ];

% EALF (Energy corresponding to average lethargy of neutrons causing fission):

ANA_EALF                  (idx, [1:   2]) = [  1.39304E-06 0.00106 ];
IMP_EALF                  (idx, [1:   2]) = [  1.39367E-06 0.00058 ];

% AFGE (Average energy of neutrons causing fission):

ANA_AFGE                  (idx, [1:   2]) = [  2.76681E-01 0.00070 ];
IMP_AFGE                  (idx, [1:   2]) = [  2.76736E-01 0.00034 ];

% Forward-weighted delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 8 ;
FWD_ANA_BETA_ZERO         (idx, [1:  18]) = [  5.95627E-03 0.00162  1.73160E-04 0.00958  8.47653E-04 0.00430  4.90258E-04 0.00570  1.10756E-03 0.00374  1.89767E-03 0.00276  6.74618E-04 0.00470  5.43489E-04 0.00557  2.21870E-04 0.00824 ];
FWD_ANA_LAMBDA            (idx, [1:  18]) = [  4.82924E-01 0.00265  1.24667E-02 0.0E+00  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 6.3E-09  3.55460E+00 0.0E+00 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  18]) = [  7.24452E-03 0.00232  2.10738E-04 0.01442  1.03068E-03 0.00634  5.95109E-04 0.00899  1.34275E-03 0.00539  2.30147E-03 0.00431  8.25359E-04 0.00701  6.62578E-04 0.00826  2.75826E-04 0.01289 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  18]) = [  4.86292E-01 0.00382  1.24667E-02 0.0E+00  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 6.3E-09  3.55460E+00 0.0E+00 ];

% Adjoint weighted time constants using Nauchi's method:

IFP_CHAIN_LENGTH          (idx, 1)        = 15 ;
ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  1.66211E-05 0.00032  1.66078E-05 0.00032  1.84626E-05 0.00315 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  2.11082E-05 0.00029  2.10913E-05 0.00029  2.34468E-05 0.00314 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  18]) = [  7.15404E-03 0.00229  2.06172E-04 0.01401  1.01894E-03 0.00632  5.87882E-04 0.00804  1.32623E-03 0.00541  2.27889E-03 0.00401  8.14244E-04 0.00650  6.50657E-04 0.00797  2.71031E-04 0.01212 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  18]) = [  4.84888E-01 0.00372  1.24667E-02 0.0E+00  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 6.3E-09  3.55460E+00 0.0E+00 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  1.66173E-05 0.00071  1.66036E-05 0.00072  1.85018E-05 0.00753 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  2.11033E-05 0.00069  2.10859E-05 0.00069  2.34974E-05 0.00754 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  18]) = [  7.12369E-03 0.00705  2.16198E-04 0.04026  9.91992E-04 0.01761  5.81766E-04 0.02559  1.30089E-03 0.01617  2.28377E-03 0.01227  8.07812E-04 0.02034  6.73413E-04 0.02232  2.67852E-04 0.03563 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  18]) = [  4.88388E-01 0.01015  1.24667E-02 0.0E+00  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 6.3E-09  3.55460E+00 0.0E+00 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  18]) = [  7.11886E-03 0.00680  2.16039E-04 0.03887  9.88394E-04 0.01725  5.82460E-04 0.02421  1.30812E-03 0.01542  2.27637E-03 0.01197  8.11432E-04 0.01928  6.71144E-04 0.02153  2.64905E-04 0.03407 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  18]) = [  4.86671E-01 0.00974  1.24667E-02 0.0E+00  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 6.3E-09  3.55460E+00 0.0E+00 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -4.29177E+02 0.00712 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  1.66492E-05 0.00019 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  2.11439E-05 0.00013 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  7.14396E-03 0.00127 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -4.29096E+02 0.00129 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  2.79044E-07 0.00017 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  4.13282E-06 0.00016  4.13296E-06 0.00016  4.11491E-06 0.00161 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  2.54438E-05 0.00020  2.54439E-05 0.00020  2.54283E-05 0.00222 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  5.03089E-01 0.00014  5.02085E-01 0.00014  6.71564E-01 0.00268 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.19884E+01 0.00370 ];
ANA_MEAN_NCOL             (idx, [1:   4]) = [  2.56798E+01 7.3E-05  2.85887E+01 9.7E-05 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  1])  = '0' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  2.00000E+01  6.06550E+00  3.67900E+00  2.23100E+00  1.35300E+00  8.21000E-01  5.00000E-01  3.02500E-01  1.83000E-01  1.11000E-01  6.74300E-02  4.08500E-02  2.47800E-02  1.50300E-02  9.11800E-03  5.50000E-03  3.51910E-03  2.23945E-03  1.42510E-03  9.06898E-04  3.67262E-04  1.48728E-04  7.55014E-05  4.80520E-05  2.77000E-05  1.59680E-05  9.87700E-06  4.00000E-06  3.30000E-06  2.60000E-06  2.10000E-06  1.85500E-06  1.50000E-06  1.30000E-06  1.15000E-06  1.12300E-06  1.09700E-06  1.07100E-06  1.04500E-06  1.02000E-06  9.96000E-07  9.72000E-07  9.50000E-07  9.10000E-07  8.50000E-07  7.80000E-07  6.25000E-07  5.00000E-07  4.00000E-07  3.50000E-07  3.20000E-07  3.00000E-07  2.80000E-07  2.50000E-07  2.20000E-07  1.80000E-07  1.40000E-07  1.00000E-07  8.00000E-08  6.70000E-08  5.80000E-08  5.00000E-08  4.20000E-08  3.50000E-08  3.00000E-08  2.50000E-08  2.00000E-08  1.50000E-08  1.00000E-08  5.00000E-09  1.00000E-11 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Micro-group spectrum:

INF_MICRO_FLX             (idx, [1: 140]) = [  8.41187E+05 0.00101  3.51400E+06 0.00044  7.41462E+06 0.00030  7.83164E+06 0.00023  7.47831E+06 0.00023  9.00627E+06 0.00025  6.08115E+06 0.00017  5.65180E+06 0.00026  4.29271E+06 0.00021  3.49512E+06 0.00022  3.02324E+06 0.00014  2.69850E+06 0.00030  2.49498E+06 0.00025  2.36188E+06 0.00023  2.29404E+06 0.00023  1.96815E+06 0.00026  1.94346E+06 0.00029  1.90939E+06 0.00023  1.85678E+06 0.00017  3.57658E+06 0.00016  3.39133E+06 0.00022  2.37664E+06 0.00020  1.50339E+06 0.00029  1.67654E+06 0.00023  1.53052E+06 0.00031  1.39987E+06 0.00027  2.15534E+06 0.00026  5.01546E+05 0.00045  6.30455E+05 0.00041  5.74988E+05 0.00047  3.30780E+05 0.00054  5.78482E+05 0.00054  3.91732E+05 0.00055  3.27794E+05 0.00062  6.13265E+04 0.00125  6.08879E+04 0.00096  6.25084E+04 0.00109  6.46056E+04 0.00096  6.41513E+04 0.00137  6.31497E+04 0.00147  6.55218E+04 0.00102  6.16102E+04 0.00115  1.16384E+05 0.00096  1.85843E+05 0.00083  2.36182E+05 0.00060  6.18734E+05 0.00039  6.40376E+05 0.00044  6.63428E+05 0.00040  4.12736E+05 0.00054  2.86392E+05 0.00060  2.11115E+05 0.00054  2.36227E+05 0.00063  4.14767E+05 0.00037  5.15224E+05 0.00033  8.96975E+05 0.00042  1.23224E+06 0.00035  1.64489E+06 0.00031  9.76485E+05 0.00038  6.69194E+05 0.00043  4.67096E+05 0.00042  4.09629E+05 0.00041  3.94684E+05 0.00039  3.23412E+05 0.00053  2.14931E+05 0.00055  1.96301E+05 0.00051  1.71632E+05 0.00050  1.42962E+05 0.00061  1.11165E+05 0.00061  7.31247E+04 0.00074  2.54891E+04 0.00074 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.26937E+00 0.00011 ];

% Flux spectra in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  4.93041E+01 9.1E-05  5.65630E+00 0.00018 ];
INF_FISS_FLX              (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  4.12678E-01 3.1E-05  9.44261E-01 4.6E-05 ];
INF_CAPT                  (idx, [1:   4]) = [  7.06464E-03 0.00017  2.44605E-02 8.7E-05 ];
INF_ABS                   (idx, [1:   4]) = [  1.01113E-02 0.00013  8.86582E-02 0.00011 ];
INF_FISS                  (idx, [1:   4]) = [  3.04667E-03 0.00013  6.41977E-02 0.00012 ];
INF_NSF                   (idx, [1:   4]) = [  7.76277E-03 0.00013  1.56399E-01 0.00012 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.54796E+00 1.4E-05  2.43620E+00 0.0E+00 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.03305E+02 1.1E-06  2.02270E+02 3.8E-09 ];
INF_INVV                  (idx, [1:   4]) = [  5.23005E-08 0.00016  2.25550E-06 6.0E-05 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  4.02563E-01 3.3E-05  8.55570E-01 6.1E-05 ];
INF_SCATT1                (idx, [1:   4]) = [  1.68032E-01 4.9E-05  2.25550E-01 0.00013 ];
INF_SCATT2                (idx, [1:   4]) = [  6.65788E-02 7.7E-05  5.78856E-02 0.00039 ];
INF_SCATT3                (idx, [1:   4]) = [  6.02568E-03 0.00093  1.76289E-02 0.00097 ];
INF_SCATT4                (idx, [1:   4]) = [ -6.16049E-03 0.00070 -3.35168E-03 0.00508 ];
INF_SCATT5                (idx, [1:   4]) = [  7.05863E-04 0.00686  2.98219E-03 0.00574 ];
INF_SCATT6                (idx, [1:   4]) = [  3.76734E-03 0.00090 -7.99673E-03 0.00258 ];
INF_SCATT7                (idx, [1:   4]) = [  6.10507E-04 0.00546 -4.21442E-04 0.04087 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  4.02602E-01 3.3E-05  8.55570E-01 6.1E-05 ];
INF_SCATTP1               (idx, [1:   4]) = [  1.68032E-01 4.9E-05  2.25550E-01 0.00013 ];
INF_SCATTP2               (idx, [1:   4]) = [  6.65790E-02 7.7E-05  5.78856E-02 0.00039 ];
INF_SCATTP3               (idx, [1:   4]) = [  6.02565E-03 0.00093  1.76289E-02 0.00097 ];
INF_SCATTP4               (idx, [1:   4]) = [ -6.16052E-03 0.00070 -3.35168E-03 0.00508 ];
INF_SCATTP5               (idx, [1:   4]) = [  7.05877E-04 0.00689  2.98219E-03 0.00574 ];
INF_SCATTP6               (idx, [1:   4]) = [  3.76727E-03 0.00091 -7.99673E-03 0.00258 ];
INF_SCATTP7               (idx, [1:   4]) = [  6.10532E-04 0.00547 -4.21442E-04 0.04087 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  1.84546E-01 8.5E-05  6.41030E-01 6.4E-05 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.80623E+00 8.5E-05  5.19996E-01 6.4E-05 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  1.00719E-02 0.00013  8.86582E-02 0.00011 ];
INF_REMXS                 (idx, [1:   4]) = [  2.04981E-02 5.8E-05  9.05069E-02 0.00018 ];

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

INF_S0                    (idx, [1:   8]) = [  3.92180E-01 3.1E-05  1.03832E-02 0.00016  1.81590E-03 0.00155  8.53754E-01 6.2E-05 ];
INF_S1                    (idx, [1:   8]) = [  1.65077E-01 4.7E-05  2.95412E-03 0.00037  6.08750E-04 0.00242  2.24941E-01 0.00013 ];
INF_S2                    (idx, [1:   8]) = [  6.74956E-02 7.6E-05 -9.16848E-04 0.00106  3.33902E-04 0.00355  5.75517E-02 0.00039 ];
INF_S3                    (idx, [1:   8]) = [  7.08526E-03 0.00077 -1.05957E-03 0.00063  1.20541E-04 0.00912  1.75084E-02 0.00098 ];
INF_S4                    (idx, [1:   8]) = [ -5.82009E-03 0.00080 -3.40404E-04 0.00218 -7.23898E-07 1.00000 -3.35096E-03 0.00510 ];
INF_S5                    (idx, [1:   8]) = [  6.89535E-04 0.00716  1.63283E-05 0.02878 -5.07163E-05 0.01948  3.03290E-03 0.00565 ];
INF_S6                    (idx, [1:   8]) = [  3.84880E-03 0.00089 -8.14665E-05 0.00645 -6.42063E-05 0.01228 -7.93253E-03 0.00259 ];
INF_S7                    (idx, [1:   8]) = [  7.07766E-04 0.00474 -9.72590E-05 0.00619 -5.77474E-05 0.01276 -3.63695E-04 0.04740 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  3.92219E-01 3.1E-05  1.03832E-02 0.00016  1.81590E-03 0.00155  8.53754E-01 6.2E-05 ];
INF_SP1                   (idx, [1:   8]) = [  1.65078E-01 4.7E-05  2.95412E-03 0.00037  6.08750E-04 0.00242  2.24941E-01 0.00013 ];
INF_SP2                   (idx, [1:   8]) = [  6.74958E-02 7.6E-05 -9.16848E-04 0.00106  3.33902E-04 0.00355  5.75517E-02 0.00039 ];
INF_SP3                   (idx, [1:   8]) = [  7.08522E-03 0.00077 -1.05957E-03 0.00063  1.20541E-04 0.00912  1.75084E-02 0.00098 ];
INF_SP4                   (idx, [1:   8]) = [ -5.82012E-03 0.00080 -3.40404E-04 0.00218 -7.23898E-07 1.00000 -3.35096E-03 0.00510 ];
INF_SP5                   (idx, [1:   8]) = [  6.89549E-04 0.00719  1.63283E-05 0.02878 -5.07163E-05 0.01948  3.03290E-03 0.00565 ];
INF_SP6                   (idx, [1:   8]) = [  3.84873E-03 0.00089 -8.14665E-05 0.00645 -6.42063E-05 0.01228 -7.93253E-03 0.00259 ];
INF_SP7                   (idx, [1:   8]) = [  7.07791E-04 0.00474 -9.72590E-05 0.00619 -5.77474E-05 0.01276 -3.63695E-04 0.04740 ];

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

CMM_TRANSPXS              (idx, [1:   4]) = [  1.90589E-01 0.00019  5.84071E-01 0.00086 ];
CMM_TRANSPXS_X            (idx, [1:   4]) = [  1.90882E-01 0.00032  5.84342E-01 0.00139 ];
CMM_TRANSPXS_Y            (idx, [1:   4]) = [  1.90877E-01 0.00031  5.83851E-01 0.00177 ];
CMM_TRANSPXS_Z            (idx, [1:   4]) = [  1.90011E-01 0.00028  5.84100E-01 0.00167 ];
CMM_DIFFCOEF              (idx, [1:   4]) = [  1.74897E+00 0.00018  5.70717E-01 0.00085 ];
CMM_DIFFCOEF_X            (idx, [1:   4]) = [  1.74628E+00 0.00032  5.70469E-01 0.00139 ];
CMM_DIFFCOEF_Y            (idx, [1:   4]) = [  1.74633E+00 0.00031  5.70965E-01 0.00177 ];
CMM_DIFFCOEF_Z            (idx, [1:   4]) = [  1.75428E+00 0.00028  5.70717E-01 0.00166 ];

% Delayed neutron parameters (Meulekamp method):

BETA_EFF                  (idx, [1:  18]) = [  7.24452E-03 0.00232  2.10738E-04 0.01442  1.03068E-03 0.00634  5.95109E-04 0.00899  1.34275E-03 0.00539  2.30147E-03 0.00431  8.25359E-04 0.00701  6.62578E-04 0.00826  2.75826E-04 0.01289 ];
LAMBDA                    (idx, [1:  18]) = [  4.86292E-01 0.00382  1.24667E-02 0.0E+00  2.82917E-02 0.0E+00  4.25244E-02 0.0E+00  1.33042E-01 0.0E+00  2.92467E-01 0.0E+00  6.66488E-01 0.0E+00  1.63478E+00 6.3E-09  3.55460E+00 0.0E+00 ];

