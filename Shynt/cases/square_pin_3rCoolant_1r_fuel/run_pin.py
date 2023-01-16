import Shynt

from pin_3c1f import model_universe

Shynt.run(model_universe, serp_dir="serpent_files", name_out="pin_3c1f")

raise SystemExit
# flx1_f = 5.17248
# flx2_f = 30.0545
# flx1_c1 = 5.4794
# flx2_c1 = 29.7986
# flx1_c2 = 5.59869
# flx2_c2 = 29.7022

flx1_f = 1.168151983818857
flx1_c1 = 1.1426489553641432
flx1_c2 = 1.159598173049235
flx2_f = 0.2001875376035711
flx2_c1 = 0.2075162814191603
flx2_c2 = 0.22335662719177163

s11_f = 0.400257
s11_c1 = 0.389698
s11_c2 = 0.391267
s12_c1 = 8.18255E-04
s12_f = 8.18255E-04
s12_c1 = 1.6854E-02
s12_c2 = 1.70095E-02
s22_f = 0.404682
s22_c1 = 1.10687
s22_c2 = 1.112040
s21_f = 1.59537E-03
s21_c1 = 1.1463E-03
s21_c2 = 1.12036E-03
nuf1_f = 1.5484E-02
nuf2_f = 0.285150


qf1 = s11_f*flx1_f + s21_f*flx2_f + (nuf1_f*flx1_f + nuf2_f*flx2_f)/1.1475
qf2 = s12_f*flx1_f + s22_f*flx2_f

qc1_1 = s11_c1*flx1_c1 + s21_c1*flx2_c1
qc1_2 = s12_c1*flx1_c1 + s22_c1*flx2_c1


qc2_1 = s11_c2*flx1_c2 + s21_c2*flx2_c2
qc2_2 = s12_c2*flx1_c2 + s22_c2*flx2_c2


print(f"qf1: {qf1}")
print(f"qc1_1: {qc1_1}")
print(f"qc2_1: {qc2_1}")

print(f"qf2: {qf2}")
print(f"qc1_2: {qc1_2}")
print(f"qc2_2: {qc2_2}")


