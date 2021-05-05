
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
INPUT_FILE_NAME           (idx, [1: 11])  = 'GroupConst5' ;
WORKING_DIRECTORY         (idx, [1: 50])  = '/home/huaiqian/Serpent2.1.29/src/GroupConstforpin5' ;
HOSTNAME                  (idx, [1:  8])  = 'huaiqian' ;
CPU_TYPE                  (idx, [1: 40])  = 'Intel(R) Core(TM) i5-3570K CPU @ 3.40GHz' ;
CPU_MHZ                   (idx, 1)        = 28.0 ;
START_DATE                (idx, [1: 24])  = 'Fri Nov  3 13:26:14 2017' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Fri Nov  3 13:27:42 2017' ;

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
ST_FRAC                   (idx, [1:   4]) = [  8.68791E-03 0.00306  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.91312E-01 2.7E-05  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  8.37289E-01 0.00011  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  8.37675E-01 0.00011  0.00000E+00 0.0E+00 ];
AVG_TRACKING_LOOPS        (idx, [1:   8]) = [  2.32592E+00 0.00039  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  2.54158E+01 0.00053  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  2.54158E+01 0.00053  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  4.92504E+00 0.00076  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  1.93176E-01 0.00348  0.00000E+00 0.0E+00 ];
LOST_PARTICLES            (idx, 1)        = 0 ;

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 500 ;
SOURCE_POPULATION         (idx, 1)        = 1000511 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  2.00102E+03 0.00137 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  2.00102E+03 0.00137 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  1.47388E+00 ;
RUNNING_TIME              (idx, 1)        =  1.47515E+00 ;
INIT_TIME                 (idx, [1:  2])  = [  1.31500E-02  1.31500E-02 ];
PROCESS_TIME              (idx, [1:  2])  = [  8.33332E-05  8.33332E-05 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  1.46190E+00  1.46190E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  1.47483E+00  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 0.99914 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  9.99324E-01 0.00013 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  9.84759E-01 ;

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

NORM_COEF                 (idx, [1:   4]) = [  4.99405E-04 0.00085  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  5.80807E-01 0.00229 ];
U235_FISS                 (idx, [1:   4]) = [  4.73577E-01 0.00115  9.17269E-01 0.00044 ];
U238_FISS                 (idx, [1:   4]) = [  4.27345E-02 0.00513  8.27310E-02 0.00483 ];
U235_CAPT                 (idx, [1:   4]) = [  1.16549E-01 0.00274  2.40607E-01 0.00261 ];
U238_CAPT                 (idx, [1:   4]) = [  3.42545E-01 0.00187  7.06832E-01 0.00094 ];

% Neutron balance (particles/weight):

BALA_SRC_NEUTRON_SRC        (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_FISS       (idx, [1:  2])  = [ 1000511 1.00000E+06 ];
BALA_SRC_NEUTRON_NXN        (idx, [1:  2])  = [ 0 2.06195E+03 ];
BALA_SRC_NEUTRON_VR         (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_TOT        (idx, [1:  2])  = [ 1000511 1.00206E+06 ];

BALA_LOSS_NEUTRON_CAPT       (idx, [1:  2])  = [ 484323 4.85095E+05 ];
BALA_LOSS_NEUTRON_FISS       (idx, [1:  2])  = [ 516188 5.16967E+05 ];
BALA_LOSS_NEUTRON_LEAK       (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_CUT        (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_TOT        (idx, [1:  2])  = [ 1000511 1.00206E+06 ];

BALA_NEUTRON_DIFF            (idx, [1:  2])  = [ 0 4.65661E-10 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.67666E-11 0.00050 ];
TOT_POWDENS               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_GENRATE               (idx, [1:   2]) = [  1.27475E+00 0.00049 ];
TOT_FISSRATE              (idx, [1:   2]) = [  5.16371E-01 0.00050 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  4.83629E-01 0.00053 ];
TOT_ABSRATE               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.98810E-01 0.00085 ];
TOT_FLUX                  (idx, [1:   2]) = [  5.48317E+01 0.00069 ];
TOT_PHOTON_PRODRATE       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  2.54319E+01 0.00055 ];
INI_FMASS                 (idx, 1)        =  0.00000E+00 ;
TOT_FMASS                 (idx, 1)        =  0.00000E+00 ;

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.46867E+00 3.5E-05 ];
FISSE                     (idx, [1:   2]) = [  2.02662E+02 3.7E-06 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.27659E+00 0.00097  1.26718E+00 0.00095  9.13162E-03 0.01687 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.27744E+00 0.00049 ];
COL_KEFF                  (idx, [1:   2]) = [  1.27680E+00 0.00109 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.27744E+00 0.00049 ];
ABS_KINF                  (idx, [1:   2]) = [  1.27744E+00 0.00049 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% ALF (Average lethargy of neutrons causing fission):
% Based on E0 = 2.000000E+01 MeV

ANA_ALF                   (idx, [1:   2]) = [  1.64025E+01 0.00049 ];
IMP_ALF                   (idx, [1:   2]) = [  1.64115E+01 0.00025 ];

% EALF (Energy corresponding to average lethargy of neutrons causing fission):

ANA_EALF                  (idx, [1:   2]) = [  1.52919E-06 0.00812 ];
IMP_EALF                  (idx, [1:   2]) = [  1.49758E-06 0.00406 ];

% AFGE (Average energy of neutrons causing fission):

ANA_AFGE                  (idx, [1:   2]) = [  2.86699E-01 0.00504 ];
IMP_AFGE                  (idx, [1:   2]) = [  2.85116E-01 0.00241 ];

% Forward-weighted delayed neutron parameters:

FWD_ANA_BETA_ZERO         (idx, [1:  14]) = [  5.84648E-03 0.01189  1.59713E-04 0.06887  9.07896E-04 0.02893  8.88332E-04 0.02937  2.68347E-03 0.01745  9.04972E-04 0.03152  3.02093E-04 0.05376 ];
FWD_ANA_LAMBDA            (idx, [1:  14]) = [  8.21466E-01 0.02786  4.19688E-03 0.06293  2.83376E-02 0.01526  1.00017E-01 0.01444  3.21724E-01 0.00058  1.19292E+00 0.01590  4.59502E+00 0.04330 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  14]) = [  6.98639E-03 0.01670  1.85895E-04 0.10325  1.06036E-03 0.04619  1.11452E-03 0.04302  3.19728E-03 0.02418  1.07402E-03 0.04594  3.54312E-04 0.07486 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  14]) = [  8.16286E-01 0.03851  1.24907E-02 4.8E-06  3.16316E-02 0.00062  1.10360E-01 0.00083  3.21749E-01 0.00079  1.34327E+00 0.00047  8.86643E+00 0.00332 ];

% Adjoint weighted time constants using Nauchi's method:

ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  1.59275E-05 0.00217  1.59131E-05 0.00217  1.79401E-05 0.02522 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  2.03236E-05 0.00195  2.03053E-05 0.00195  2.28840E-05 0.02511 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  14]) = [  7.17597E-03 0.01695  1.84646E-04 0.09948  1.07486E-03 0.04332  1.14726E-03 0.04211  3.29804E-03 0.02297  1.11000E-03 0.04382  3.61165E-04 0.07559 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  14]) = [  8.03722E-01 0.04062  1.24908E-02 7.9E-06  3.16125E-02 0.00078  1.10315E-01 0.00095  3.21573E-01 0.00083  1.34262E+00 0.00057  8.85927E+00 0.00431 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  1.59836E-05 0.00526  1.59611E-05 0.00529  1.34413E-05 0.05634 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  2.03948E-05 0.00517  2.03660E-05 0.00521  1.71646E-05 0.05632 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  14]) = [  6.89438E-03 0.05110  2.15663E-04 0.28666  1.13263E-03 0.12850  1.20755E-03 0.12198  2.95702E-03 0.07505  9.71485E-04 0.15061  4.10024E-04 0.20731 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  14]) = [  8.42937E-01 0.11008  1.24906E-02 0.0E+00  3.16486E-02 0.00155  1.10260E-01 0.00201  3.21694E-01 0.00187  1.34164E+00 0.00147  8.77985E+00 0.00782 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  14]) = [  6.79785E-03 0.04910  2.15337E-04 0.26682  1.17420E-03 0.12308  1.13097E-03 0.11975  2.93706E-03 0.07232  9.24460E-04 0.14422  4.15823E-04 0.20297 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  14]) = [  8.71419E-01 0.10986  1.24906E-02 0.0E+00  3.16482E-02 0.00154  1.10222E-01 0.00196  3.21586E-01 0.00184  1.34170E+00 0.00147  8.77790E+00 0.00773 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -4.39128E+02 0.05255 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  1.59355E-05 0.00144 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  2.03331E-05 0.00102 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  6.85141E-03 0.00943 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -4.30404E+02 0.00955 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  2.69770E-07 0.00121 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  4.12043E-06 0.00101  4.12080E-06 0.00102  4.08783E-06 0.01369 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  2.46111E-05 0.00137  2.46103E-05 0.00137  2.47137E-05 0.01634 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  4.99262E-01 0.00103  4.98330E-01 0.00104  7.04724E-01 0.01996 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.00016E+01 0.02751 ];
ANA_MEAN_NCOL             (idx, [1:   4]) = [  2.54158E+01 0.00053  2.82043E+01 0.00070 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  2])  = '11' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  1.00000E-11  5.00000E-09  1.00000E-08  1.50000E-08  2.00000E-08  2.50000E-08  3.00000E-08  3.50000E-08  4.20000E-08  5.00000E-08  5.80000E-08  6.70000E-08  8.00000E-08  1.00000E-07  1.40000E-07  1.80000E-07  2.20000E-07  2.50000E-07  2.80000E-07  3.00000E-07  3.20000E-07  3.50000E-07  4.00000E-07  5.00000E-07  6.25000E-07  7.80000E-07  8.50000E-07  9.10000E-07  9.50000E-07  9.72000E-07  9.96000E-07  1.02000E-06  1.04500E-06  1.07100E-06  1.09700E-06  1.12300E-06  1.15000E-06  1.30000E-06  1.50000E-06  1.85500E-06  2.10000E-06  2.60000E-06  3.30000E-06  4.00000E-06  9.87700E-06  1.59680E-05  2.77000E-05  4.80520E-05  7.55014E-05  1.48728E-04  3.67262E-04  9.06898E-04  1.42510E-03  2.23945E-03  3.51910E-03  5.50000E-03  9.11800E-03  1.50300E-02  2.47800E-02  4.08500E-02  6.74300E-02  1.11000E-01  1.83000E-01  3.02500E-01  5.00000E-01  8.21000E-01  1.35300E+00  2.23100E+00  3.67900E+00  6.06550E+00  2.00000E+01 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Micro-group spectrum:

INF_MICRO_FLX             (idx, [1: 140]) = [  1.13507E+04 0.00846  4.62457E+04 0.00447  9.71656E+04 0.00238  1.00910E+05 0.00203  9.54906E+04 0.00173  1.13643E+05 0.00131  7.71677E+04 0.00164  7.17134E+04 0.00143  5.50979E+04 0.00119  4.51150E+04 0.00175  3.90364E+04 0.00118  3.48934E+04 0.00158  3.23078E+04 0.00206  3.06223E+04 0.00171  2.98148E+04 0.00155  2.56008E+04 0.00184  2.52102E+04 0.00200  2.49366E+04 0.00172  2.42738E+04 0.00157  4.67481E+04 0.00111  4.43866E+04 0.00124  3.13763E+04 0.00121  1.97943E+04 0.00206  2.22417E+04 0.00208  2.03733E+04 0.00153  1.82176E+04 0.00233  2.87517E+04 0.00161  6.49036E+03 0.00306  8.10479E+03 0.00303  7.40973E+03 0.00345  4.25949E+03 0.00327  7.41638E+03 0.00263  5.05952E+03 0.00300  4.24366E+03 0.00315  7.85246E+02 0.01003  7.86490E+02 0.00870  8.14706E+02 0.00625  8.32774E+02 0.01021  8.26996E+02 0.00757  8.12543E+02 0.01133  8.43446E+02 0.00908  7.92940E+02 0.00667  1.50816E+03 0.00741  2.40526E+03 0.00436  3.05780E+03 0.00343  8.04200E+03 0.00230  8.32431E+03 0.00350  8.61728E+03 0.00229  5.34620E+03 0.00500  3.71602E+03 0.00404  2.73053E+03 0.00490  3.05224E+03 0.00437  5.35504E+03 0.00424  6.65561E+03 0.00376  1.15056E+04 0.00285  1.57837E+04 0.00240  2.11461E+04 0.00250  1.25874E+04 0.00302  8.67002E+03 0.00330  6.04460E+03 0.00404  5.34969E+03 0.00303  5.13630E+03 0.00323  4.23349E+03 0.00369  2.81643E+03 0.00382  2.59945E+03 0.00416  2.30169E+03 0.00414  1.92329E+03 0.00568  1.52385E+03 0.00315  1.03508E+03 0.00569  3.80373E+02 0.00564 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];

% Flux spectra in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  3.18864E+01 0.00078  3.66641E+00 0.00133 ];
INF_FISS_FLX              (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  4.02742E-01 0.00025  1.07642E+00 0.00028 ];
INF_CAPT                  (idx, [1:   4]) = [  1.54333E-04 0.00148  4.93252E-03 0.00050 ];
INF_ABS                   (idx, [1:   4]) = [  1.54333E-04 0.00148  4.93252E-03 0.00050 ];
INF_FISS                  (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_NSF                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_NUBAR                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_KAPPA                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_INVV                  (idx, [1:   4]) = [  5.27034E-08 0.00080  2.27148E-06 0.00050 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  4.02588E-01 0.00025  1.07143E+00 0.00029 ];
INF_SCATT1                (idx, [1:   4]) = [  2.35500E-01 0.00031  3.31922E-01 0.00082 ];
INF_SCATT2                (idx, [1:   4]) = [  9.01579E-02 0.00067  8.62492E-02 0.00307 ];
INF_SCATT3                (idx, [1:   4]) = [  2.78364E-03 0.01714  2.62598E-02 0.00846 ];
INF_SCATT4                (idx, [1:   4]) = [ -1.37985E-02 0.00310 -5.23374E-03 0.03775 ];
INF_SCATT5                (idx, [1:   4]) = [ -1.21451E-03 0.03604  4.35626E-03 0.03358 ];
INF_SCATT6                (idx, [1:   4]) = [  4.62299E-03 0.00898 -1.17609E-02 0.01445 ];
INF_SCATT7                (idx, [1:   4]) = [  4.10837E-04 0.09710 -7.27073E-04 0.27306 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  4.02588E-01 0.00025  1.07143E+00 0.00029 ];
INF_SCATTP1               (idx, [1:   4]) = [  2.35500E-01 0.00031  3.31922E-01 0.00082 ];
INF_SCATTP2               (idx, [1:   4]) = [  9.01579E-02 0.00067  8.62492E-02 0.00307 ];
INF_SCATTP3               (idx, [1:   4]) = [  2.78364E-03 0.01714  2.62598E-02 0.00846 ];
INF_SCATTP4               (idx, [1:   4]) = [ -1.37985E-02 0.00310 -5.23374E-03 0.03775 ];
INF_SCATTP5               (idx, [1:   4]) = [ -1.21451E-03 0.03604  4.35626E-03 0.03358 ];
INF_SCATTP6               (idx, [1:   4]) = [  4.62299E-03 0.00898 -1.17609E-02 0.01445 ];
INF_SCATTP7               (idx, [1:   4]) = [  4.10837E-04 0.09710 -7.27073E-04 0.27306 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  1.05428E-01 0.00072  6.37224E-01 0.00063 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  3.16175E+00 0.00072  5.23108E-01 0.00063 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  1.54333E-04 0.00148  4.93252E-03 0.00050 ];
INF_REMXS                 (idx, [1:   4]) = [  1.56940E-02 0.00082  6.62011E-03 0.00635 ];

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

INF_S0                    (idx, [1:   8]) = [  3.87048E-01 0.00025  1.55398E-02 0.00089  1.62979E-03 0.01109  1.06980E+00 0.00029 ];
INF_S1                    (idx, [1:   8]) = [  2.30871E-01 0.00032  4.62932E-03 0.00178  1.04846E-03 0.01569  3.30873E-01 0.00082 ];
INF_S2                    (idx, [1:   8]) = [  9.15504E-02 0.00064 -1.39254E-03 0.00588  5.79109E-04 0.02421  8.56701E-02 0.00307 ];
INF_S3                    (idx, [1:   8]) = [  4.40357E-03 0.01056 -1.61993E-03 0.00435  2.23360E-04 0.05306  2.60365E-02 0.00843 ];
INF_S4                    (idx, [1:   8]) = [ -1.32771E-02 0.00299 -5.21366E-04 0.01547  1.14564E-05 0.81251 -5.24520E-03 0.03775 ];
INF_S5                    (idx, [1:   8]) = [ -1.23685E-03 0.03513  2.23341E-05 0.25134 -7.59018E-05 0.09182  4.43216E-03 0.03339 ];
INF_S6                    (idx, [1:   8]) = [  4.75411E-03 0.00893 -1.31122E-04 0.03903 -1.11833E-04 0.05443 -1.16491E-02 0.01447 ];
INF_S7                    (idx, [1:   8]) = [  5.61227E-04 0.06899 -1.50390E-04 0.04397 -1.03423E-04 0.04122 -6.23650E-04 0.31989 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  3.87048E-01 0.00025  1.55398E-02 0.00089  1.62979E-03 0.01109  1.06980E+00 0.00029 ];
INF_SP1                   (idx, [1:   8]) = [  2.30871E-01 0.00032  4.62932E-03 0.00178  1.04846E-03 0.01569  3.30873E-01 0.00082 ];
INF_SP2                   (idx, [1:   8]) = [  9.15504E-02 0.00064 -1.39254E-03 0.00588  5.79109E-04 0.02421  8.56701E-02 0.00307 ];
INF_SP3                   (idx, [1:   8]) = [  4.40357E-03 0.01056 -1.61993E-03 0.00435  2.23360E-04 0.05306  2.60365E-02 0.00843 ];
INF_SP4                   (idx, [1:   8]) = [ -1.32771E-02 0.00299 -5.21366E-04 0.01547  1.14564E-05 0.81251 -5.24520E-03 0.03775 ];
INF_SP5                   (idx, [1:   8]) = [ -1.23685E-03 0.03513  2.23341E-05 0.25134 -7.59018E-05 0.09182  4.43216E-03 0.03339 ];
INF_SP6                   (idx, [1:   8]) = [  4.75411E-03 0.00893 -1.31122E-04 0.03903 -1.11833E-04 0.05443 -1.16491E-02 0.01447 ];
INF_SP7                   (idx, [1:   8]) = [  5.61227E-04 0.06899 -1.50390E-04 0.04397 -1.03423E-04 0.04122 -6.23650E-04 0.31989 ];

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

CMM_TRANSPXS              (idx, [1:   4]) = [  2.30427E-01 0.00172 -2.78392E-02 0.00241 ];
CMM_TRANSPXS_X            (idx, [1:   4]) = [  2.30386E-01 0.00204 -2.78326E-02 0.00285 ];
CMM_TRANSPXS_Y            (idx, [1:   4]) = [  2.30790E-01 0.00333 -2.78686E-02 0.00381 ];
CMM_TRANSPXS_Z            (idx, [1:   4]) = [  2.30199E-01 0.00321 -2.78284E-02 0.00353 ];
CMM_DIFFCOEF              (idx, [1:   4]) = [  1.44669E+00 0.00173 -1.19752E+01 0.00241 ];
CMM_DIFFCOEF_X            (idx, [1:   4]) = [  1.44699E+00 0.00204 -1.19787E+01 0.00283 ];
CMM_DIFFCOEF_Y            (idx, [1:   4]) = [  1.44470E+00 0.00334 -1.19651E+01 0.00381 ];
CMM_DIFFCOEF_Z            (idx, [1:   4]) = [  1.44838E+00 0.00321 -1.19818E+01 0.00355 ];

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
INPUT_FILE_NAME           (idx, [1: 11])  = 'GroupConst5' ;
WORKING_DIRECTORY         (idx, [1: 50])  = '/home/huaiqian/Serpent2.1.29/src/GroupConstforpin5' ;
HOSTNAME                  (idx, [1:  8])  = 'huaiqian' ;
CPU_TYPE                  (idx, [1: 40])  = 'Intel(R) Core(TM) i5-3570K CPU @ 3.40GHz' ;
CPU_MHZ                   (idx, 1)        = 28.0 ;
START_DATE                (idx, [1: 24])  = 'Fri Nov  3 13:26:14 2017' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Fri Nov  3 13:27:42 2017' ;

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
ST_FRAC                   (idx, [1:   4]) = [  8.68791E-03 0.00306  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  9.91312E-01 2.7E-05  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  8.37289E-01 0.00011  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  8.37675E-01 0.00011  0.00000E+00 0.0E+00 ];
AVG_TRACKING_LOOPS        (idx, [1:   8]) = [  2.32592E+00 0.00039  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  2.54158E+01 0.00053  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  2.54158E+01 0.00053  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  4.92504E+00 0.00076  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  1.93176E-01 0.00348  0.00000E+00 0.0E+00 ];
LOST_PARTICLES            (idx, 1)        = 0 ;

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 500 ;
SOURCE_POPULATION         (idx, 1)        = 1000511 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  2.00102E+03 0.00137 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  2.00102E+03 0.00137 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  1.47389E+00 ;
RUNNING_TIME              (idx, 1)        =  1.47515E+00 ;
INIT_TIME                 (idx, [1:  2])  = [  1.31500E-02  1.31500E-02 ];
PROCESS_TIME              (idx, [1:  2])  = [  8.33332E-05  8.33332E-05 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  1.46190E+00  1.46190E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  1.47483E+00  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 0.99915 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  9.99324E-01 0.00013 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  9.84759E-01 ;

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

NORM_COEF                 (idx, [1:   4]) = [  4.99405E-04 0.00085  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  5.80807E-01 0.00229 ];
U235_FISS                 (idx, [1:   4]) = [  4.73577E-01 0.00115  9.17269E-01 0.00044 ];
U238_FISS                 (idx, [1:   4]) = [  4.27345E-02 0.00513  8.27310E-02 0.00483 ];
U235_CAPT                 (idx, [1:   4]) = [  1.16549E-01 0.00274  2.40607E-01 0.00261 ];
U238_CAPT                 (idx, [1:   4]) = [  3.42545E-01 0.00187  7.06832E-01 0.00094 ];

% Neutron balance (particles/weight):

BALA_SRC_NEUTRON_SRC        (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_FISS       (idx, [1:  2])  = [ 1000511 1.00000E+06 ];
BALA_SRC_NEUTRON_NXN        (idx, [1:  2])  = [ 0 2.06195E+03 ];
BALA_SRC_NEUTRON_VR         (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_TOT        (idx, [1:  2])  = [ 1000511 1.00206E+06 ];

BALA_LOSS_NEUTRON_CAPT       (idx, [1:  2])  = [ 484323 4.85095E+05 ];
BALA_LOSS_NEUTRON_FISS       (idx, [1:  2])  = [ 516188 5.16967E+05 ];
BALA_LOSS_NEUTRON_LEAK       (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_CUT        (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_TOT        (idx, [1:  2])  = [ 1000511 1.00206E+06 ];

BALA_NEUTRON_DIFF            (idx, [1:  2])  = [ 0 4.65661E-10 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.67666E-11 0.00050 ];
TOT_POWDENS               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_GENRATE               (idx, [1:   2]) = [  1.27475E+00 0.00049 ];
TOT_FISSRATE              (idx, [1:   2]) = [  5.16371E-01 0.00050 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  4.83629E-01 0.00053 ];
TOT_ABSRATE               (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.98810E-01 0.00085 ];
TOT_FLUX                  (idx, [1:   2]) = [  5.48317E+01 0.00069 ];
TOT_PHOTON_PRODRATE       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  2.54319E+01 0.00055 ];
INI_FMASS                 (idx, 1)        =  0.00000E+00 ;
TOT_FMASS                 (idx, 1)        =  0.00000E+00 ;

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.46867E+00 3.5E-05 ];
FISSE                     (idx, [1:   2]) = [  2.02662E+02 3.7E-06 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.27659E+00 0.00097  1.26718E+00 0.00095  9.13162E-03 0.01687 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.27744E+00 0.00049 ];
COL_KEFF                  (idx, [1:   2]) = [  1.27680E+00 0.00109 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.27744E+00 0.00049 ];
ABS_KINF                  (idx, [1:   2]) = [  1.27744E+00 0.00049 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% ALF (Average lethargy of neutrons causing fission):
% Based on E0 = 2.000000E+01 MeV

ANA_ALF                   (idx, [1:   2]) = [  1.64025E+01 0.00049 ];
IMP_ALF                   (idx, [1:   2]) = [  1.64115E+01 0.00025 ];

% EALF (Energy corresponding to average lethargy of neutrons causing fission):

ANA_EALF                  (idx, [1:   2]) = [  1.52919E-06 0.00812 ];
IMP_EALF                  (idx, [1:   2]) = [  1.49758E-06 0.00406 ];

% AFGE (Average energy of neutrons causing fission):

ANA_AFGE                  (idx, [1:   2]) = [  2.86699E-01 0.00504 ];
IMP_AFGE                  (idx, [1:   2]) = [  2.85116E-01 0.00241 ];

% Forward-weighted delayed neutron parameters:

FWD_ANA_BETA_ZERO         (idx, [1:  14]) = [  5.84648E-03 0.01189  1.59713E-04 0.06887  9.07896E-04 0.02893  8.88332E-04 0.02937  2.68347E-03 0.01745  9.04972E-04 0.03152  3.02093E-04 0.05376 ];
FWD_ANA_LAMBDA            (idx, [1:  14]) = [  8.21466E-01 0.02786  4.19688E-03 0.06293  2.83376E-02 0.01526  1.00017E-01 0.01444  3.21724E-01 0.00058  1.19292E+00 0.01590  4.59502E+00 0.04330 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  14]) = [  6.98639E-03 0.01670  1.85895E-04 0.10325  1.06036E-03 0.04619  1.11452E-03 0.04302  3.19728E-03 0.02418  1.07402E-03 0.04594  3.54312E-04 0.07486 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  14]) = [  8.16286E-01 0.03851  1.24907E-02 4.8E-06  3.16316E-02 0.00062  1.10360E-01 0.00083  3.21749E-01 0.00079  1.34327E+00 0.00047  8.86643E+00 0.00332 ];

% Adjoint weighted time constants using Nauchi's method:

ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  1.59275E-05 0.00217  1.59131E-05 0.00217  1.79401E-05 0.02522 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  2.03236E-05 0.00195  2.03053E-05 0.00195  2.28840E-05 0.02511 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  14]) = [  7.17597E-03 0.01695  1.84646E-04 0.09948  1.07486E-03 0.04332  1.14726E-03 0.04211  3.29804E-03 0.02297  1.11000E-03 0.04382  3.61165E-04 0.07559 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  14]) = [  8.03722E-01 0.04062  1.24908E-02 7.9E-06  3.16125E-02 0.00078  1.10315E-01 0.00095  3.21573E-01 0.00083  1.34262E+00 0.00057  8.85927E+00 0.00431 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  1.59836E-05 0.00526  1.59611E-05 0.00529  1.34413E-05 0.05634 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  2.03948E-05 0.00517  2.03660E-05 0.00521  1.71646E-05 0.05632 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  14]) = [  6.89438E-03 0.05110  2.15663E-04 0.28666  1.13263E-03 0.12850  1.20755E-03 0.12198  2.95702E-03 0.07505  9.71485E-04 0.15061  4.10024E-04 0.20731 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  14]) = [  8.42937E-01 0.11008  1.24906E-02 0.0E+00  3.16486E-02 0.00155  1.10260E-01 0.00201  3.21694E-01 0.00187  1.34164E+00 0.00147  8.77985E+00 0.00782 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  14]) = [  6.79785E-03 0.04910  2.15337E-04 0.26682  1.17420E-03 0.12308  1.13097E-03 0.11975  2.93706E-03 0.07232  9.24460E-04 0.14422  4.15823E-04 0.20297 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  14]) = [  8.71419E-01 0.10986  1.24906E-02 0.0E+00  3.16482E-02 0.00154  1.10222E-01 0.00196  3.21586E-01 0.00184  1.34170E+00 0.00147  8.77790E+00 0.00773 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -4.39128E+02 0.05255 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  1.59355E-05 0.00144 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  2.03331E-05 0.00102 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  6.85141E-03 0.00943 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -4.30404E+02 0.00955 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  2.69770E-07 0.00121 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  4.12043E-06 0.00101  4.12080E-06 0.00102  4.08783E-06 0.01369 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  2.46111E-05 0.00137  2.46103E-05 0.00137  2.47137E-05 0.01634 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  4.99262E-01 0.00103  4.98330E-01 0.00104  7.04724E-01 0.01996 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.00016E+01 0.02751 ];
ANA_MEAN_NCOL             (idx, [1:   4]) = [  2.54158E+01 0.00053  2.82043E+01 0.00070 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  2])  = '12' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  1.00000E-11  5.00000E-09  1.00000E-08  1.50000E-08  2.00000E-08  2.50000E-08  3.00000E-08  3.50000E-08  4.20000E-08  5.00000E-08  5.80000E-08  6.70000E-08  8.00000E-08  1.00000E-07  1.40000E-07  1.80000E-07  2.20000E-07  2.50000E-07  2.80000E-07  3.00000E-07  3.20000E-07  3.50000E-07  4.00000E-07  5.00000E-07  6.25000E-07  7.80000E-07  8.50000E-07  9.10000E-07  9.50000E-07  9.72000E-07  9.96000E-07  1.02000E-06  1.04500E-06  1.07100E-06  1.09700E-06  1.12300E-06  1.15000E-06  1.30000E-06  1.50000E-06  1.85500E-06  2.10000E-06  2.60000E-06  3.30000E-06  4.00000E-06  9.87700E-06  1.59680E-05  2.77000E-05  4.80520E-05  7.55014E-05  1.48728E-04  3.67262E-04  9.06898E-04  1.42510E-03  2.23945E-03  3.51910E-03  5.50000E-03  9.11800E-03  1.50300E-02  2.47800E-02  4.08500E-02  6.74300E-02  1.11000E-01  1.83000E-01  3.02500E-01  5.00000E-01  8.21000E-01  1.35300E+00  2.23100E+00  3.67900E+00  6.06550E+00  2.00000E+01 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Micro-group spectrum:

INF_MICRO_FLX             (idx, [1: 140]) = [  6.36002E+03 0.01073  2.62570E+04 0.00367  5.47797E+04 0.00293  5.70821E+04 0.00205  5.42856E+04 0.00199  6.46799E+04 0.00213  4.34471E+04 0.00220  4.03393E+04 0.00232  3.05512E+04 0.00190  2.48525E+04 0.00234  2.13518E+04 0.00227  1.89779E+04 0.00286  1.75615E+04 0.00285  1.65264E+04 0.00299  1.60220E+04 0.00381  1.37658E+04 0.00353  1.34365E+04 0.00252  1.32989E+04 0.00362  1.29181E+04 0.00377  2.48305E+04 0.00216  2.33362E+04 0.00303  1.63013E+04 0.00249  1.02381E+04 0.00269  1.11738E+04 0.00313  1.01482E+04 0.00375  9.62271E+03 0.00463  1.41098E+04 0.00345  3.48569E+03 0.00515  4.38897E+03 0.00682  3.97543E+03 0.00422  2.25446E+03 0.00757  3.99501E+03 0.00655  2.72037E+03 0.00686  2.25615E+03 0.00783  4.18401E+02 0.01224  4.08605E+02 0.01502  4.25467E+02 0.01415  4.32081E+02 0.01563  4.36867E+02 0.01624  4.31259E+02 0.01381  4.45721E+02 0.01424  4.21316E+02 0.01333  7.94585E+02 0.01134  1.25392E+03 0.00897  1.61728E+03 0.00678  4.27010E+03 0.00406  4.39457E+03 0.00519  4.51131E+03 0.00472  2.76877E+03 0.00800  1.89897E+03 0.00778  1.36881E+03 0.00712  1.54361E+03 0.00687  2.70007E+03 0.00528  3.37248E+03 0.00603  5.83089E+03 0.00373  7.93148E+03 0.00252  1.04452E+04 0.00299  6.08513E+03 0.00403  4.12656E+03 0.00409  2.82769E+03 0.00504  2.46513E+03 0.00369  2.35936E+03 0.00534  1.89308E+03 0.00481  1.21918E+03 0.00522  1.13123E+03 0.00628  9.42043E+02 0.00773  7.85442E+02 0.00720  5.74465E+02 0.00830  3.53628E+02 0.00950  1.03583E+02 0.01129 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.30719E+00 0.00106 ];

% Flux spectra in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  1.74963E+01 0.00088  1.78865E+00 0.00094 ];
INF_FISS_FLX              (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  4.25534E-01 0.00019  6.72199E-01 0.00023 ];
INF_CAPT                  (idx, [1:   4]) = [  1.96502E-02 0.00087  6.53893E-02 0.00051 ];
INF_ABS                   (idx, [1:   4]) = [  2.84658E-02 0.00063  2.67968E-01 0.00056 ];
INF_FISS                  (idx, [1:   4]) = [  8.81556E-03 0.00078  2.02579E-01 0.00058 ];
INF_NSF                   (idx, [1:   4]) = [  2.24243E-02 0.00075  4.93624E-01 0.00058 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.54372E+00 9.9E-05  2.43670E+00 2.7E-09 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.03582E+02 8.1E-06  2.02270E+02 0.0E+00 ];
INF_INVV                  (idx, [1:   4]) = [  5.03330E-08 0.00121  2.18304E-06 0.00049 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  3.97072E-01 0.00020  4.04020E-01 0.00071 ];
INF_SCATT1                (idx, [1:   4]) = [  4.39369E-02 0.00200  7.52590E-03 0.02870 ];
INF_SCATT2                (idx, [1:   4]) = [  2.28176E-02 0.00375  4.96873E-04 0.50314 ];
INF_SCATT3                (idx, [1:   4]) = [  1.21869E-02 0.00433 -1.23725E-04 1.00000 ];
INF_SCATT4                (idx, [1:   4]) = [  7.70094E-03 0.00729  1.00198E-05 1.00000 ];
INF_SCATT5                (idx, [1:   4]) = [  3.97551E-03 0.01298  2.32402E-04 0.57147 ];
INF_SCATT6                (idx, [1:   4]) = [  1.95783E-03 0.02655 -8.86677E-05 1.00000 ];
INF_SCATT7                (idx, [1:   4]) = [  8.34910E-04 0.03774 -3.27007E-05 1.00000 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  3.97190E-01 0.00020  4.04020E-01 0.00071 ];
INF_SCATTP1               (idx, [1:   4]) = [  4.39397E-02 0.00200  7.52590E-03 0.02870 ];
INF_SCATTP2               (idx, [1:   4]) = [  2.28161E-02 0.00375  4.96873E-04 0.50314 ];
INF_SCATTP3               (idx, [1:   4]) = [  1.21865E-02 0.00436 -1.23725E-04 1.00000 ];
INF_SCATTP4               (idx, [1:   4]) = [  7.69964E-03 0.00730  1.00198E-05 1.00000 ];
INF_SCATTP5               (idx, [1:   4]) = [  3.97438E-03 0.01300  2.32402E-04 0.57147 ];
INF_SCATTP6               (idx, [1:   4]) = [  1.95764E-03 0.02657 -8.86677E-05 1.00000 ];
INF_SCATTP7               (idx, [1:   4]) = [  8.32981E-04 0.03797 -3.27007E-05 1.00000 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  3.10278E-01 0.00050  6.34355E-01 0.00047 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.07431E+00 0.00050  5.25471E-01 0.00047 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  2.83481E-02 0.00062  2.67968E-01 0.00056 ];
INF_REMXS                 (idx, [1:   4]) = [  2.91853E-02 0.00099  2.70538E-01 0.00107 ];

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

INF_S0                    (idx, [1:   8]) = [  3.96349E-01 0.00020  7.23516E-04 0.00672  2.35948E-03 0.01647  4.01660E-01 0.00072 ];
INF_S1                    (idx, [1:   8]) = [  4.41054E-02 0.00197 -1.68485E-04 0.02072 -1.93912E-04 0.09418  7.71981E-03 0.02816 ];
INF_S2                    (idx, [1:   8]) = [  2.28409E-02 0.00377 -2.32594E-05 0.11793 -9.41698E-05 0.15330  5.91043E-04 0.42105 ];
INF_S3                    (idx, [1:   8]) = [  1.21882E-02 0.00437 -1.27434E-06 1.00000 -5.19550E-05 0.28083 -7.17695E-05 1.00000 ];
INF_S4                    (idx, [1:   8]) = [  7.70311E-03 0.00734 -2.17044E-06 1.00000 -1.88187E-05 0.50444  2.88385E-05 1.00000 ];
INF_S5                    (idx, [1:   8]) = [  3.97399E-03 0.01294  1.51476E-06 1.00000 -1.11357E-06 1.00000  2.33515E-04 0.56921 ];
INF_S6                    (idx, [1:   8]) = [  1.95932E-03 0.02645 -1.48585E-06 1.00000  5.78042E-06 1.00000 -9.44482E-05 1.00000 ];
INF_S7                    (idx, [1:   8]) = [  8.35928E-04 0.03791 -1.01853E-06 1.00000 -1.06204E-05 0.73005 -2.20803E-05 1.00000 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  3.96467E-01 0.00020  7.23516E-04 0.00672  2.35948E-03 0.01647  4.01660E-01 0.00072 ];
INF_SP1                   (idx, [1:   8]) = [  4.41082E-02 0.00197 -1.68485E-04 0.02072 -1.93912E-04 0.09418  7.71981E-03 0.02816 ];
INF_SP2                   (idx, [1:   8]) = [  2.28393E-02 0.00376 -2.32594E-05 0.11793 -9.41698E-05 0.15330  5.91043E-04 0.42105 ];
INF_SP3                   (idx, [1:   8]) = [  1.21878E-02 0.00440 -1.27434E-06 1.00000 -5.19550E-05 0.28083 -7.17695E-05 1.00000 ];
INF_SP4                   (idx, [1:   8]) = [  7.70181E-03 0.00735 -2.17044E-06 1.00000 -1.88187E-05 0.50444  2.88385E-05 1.00000 ];
INF_SP5                   (idx, [1:   8]) = [  3.97287E-03 0.01296  1.51476E-06 1.00000 -1.11357E-06 1.00000  2.33515E-04 0.56921 ];
INF_SP6                   (idx, [1:   8]) = [  1.95913E-03 0.02647 -1.48585E-06 1.00000  5.78042E-06 1.00000 -9.44482E-05 1.00000 ];
INF_SP7                   (idx, [1:   8]) = [  8.34000E-04 0.03812 -1.01853E-06 1.00000 -1.06204E-05 0.73005 -2.20803E-05 1.00000 ];

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

CMM_TRANSPXS              (idx, [1:   4]) = [  1.31855E-01 0.00165  1.35046E-02 0.00166 ];
CMM_TRANSPXS_X            (idx, [1:   4]) = [  1.31691E-01 0.00222  1.34873E-02 0.00232 ];
CMM_TRANSPXS_Y            (idx, [1:   4]) = [  1.32233E-01 0.00226  1.35382E-02 0.00260 ];
CMM_TRANSPXS_Z            (idx, [1:   4]) = [  1.31662E-01 0.00211  1.34910E-02 0.00200 ];
CMM_DIFFCOEF              (idx, [1:   4]) = [  2.52820E+00 0.00165  2.46845E+01 0.00165 ];
CMM_DIFFCOEF_X            (idx, [1:   4]) = [  2.53148E+00 0.00222  2.47177E+01 0.00230 ];
CMM_DIFFCOEF_Y            (idx, [1:   4]) = [  2.52111E+00 0.00224  2.46257E+01 0.00258 ];
CMM_DIFFCOEF_Z            (idx, [1:   4]) = [  2.53201E+00 0.00212  2.47102E+01 0.00201 ];

% Delayed neutron parameters (Meulekamp method):

BETA_EFF                  (idx, [1:  14]) = [  6.98639E-03 0.01670  1.85895E-04 0.10325  1.06036E-03 0.04619  1.11452E-03 0.04302  3.19728E-03 0.02418  1.07402E-03 0.04594  3.54312E-04 0.07486 ];
LAMBDA                    (idx, [1:  14]) = [  8.16286E-01 0.03851  1.24907E-02 4.8E-06  3.16316E-02 0.00062  1.10360E-01 0.00083  3.21749E-01 0.00079  1.34327E+00 0.00047  8.86643E+00 0.00332 ];

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