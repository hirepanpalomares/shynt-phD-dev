from Shynt.api_py.materials import Isotope, Material


u235_03 = Isotope("92235.03c")
u238_03 = Isotope("92238.03c")
pu238_03 = Isotope("94238.03c")
pu239_03 = Isotope("94239.03c")
pu240_03 = Isotope("94240.03c")
pu241_03 = Isotope("94241.03c")
pu242_03 = Isotope("94242.03c")
am241_03 = Isotope("95241.03c")

helium_03 = Isotope("He-4.03c")
na = Isotope("Na-23.03c")
oxygen_03 = Isotope("8016.03c")

carbon_nat = Isotope("C-nat.03c")
si_28 = Isotope("Si-28.03c")
si_29 = Isotope("Si-29.03c")
si_30 = Isotope("Si-30.03c")
p_31 = Isotope("P-31.03c")
ti_46 = Isotope("Ti-46.03c")
ti_47 = Isotope("Ti-47.03c")
ti_48 = Isotope("Ti-48.03c")
ti_49 = Isotope("Ti-49.03c")
ti_50 = Isotope("Ti-50.03c")
cr_50 = Isotope("Cr-50.03c")
cr_52 = Isotope("Cr-52.03c")
cr_53 = Isotope("Cr-53.03c")
cr_54 = Isotope("Cr-54.03c")
mn_55 = Isotope("Mn-55.03c")
fe_54 = Isotope("Fe-54.03c")
fe_56 = Isotope("Fe-56.03c")
fe_57 = Isotope("Fe-57.03c")
fe_58 = Isotope("Fe-58.03c")
ni_58 = Isotope("Ni-58.03c")
ni_60 = Isotope("Ni-60.03c")
ni_61 = Isotope("Ni-61.03c")
ni_62 = Isotope("Ni-62.03c")
ni_64 = Isotope("Ni-64.03c")
mo_92 = Isotope("Mo-92.03c")
mo_94 = Isotope("Mo-94.03c")
mo_95 = Isotope("Mo-95.03c")
mo_96 = Isotope("Mo-96.03c")
mo_97 = Isotope("Mo-97.03c")
mo_98 = Isotope("Mo-98.03c")
mo_100 = Isotope("Mo-100.03c")

composition_inner_fuel = {
    "fractions": [
        (u235_03, 1.01116e-04), (u238_03, 1.98680e-02), (pu238_03, 1.78056e-05),
        (pu239_03, 2.45592e-03), (pu240_03, 7.32245e-04), (pu241_03, 1.96866e-04),
        (pu242_03, 6.83261e-05), (am241_03, 4.81830e-05), (oxygen_03, 4.65070e-02),
    ],
    "type": "atom_density"
}

inner_fuel = Material("inner_fuel", composition=composition_inner_fuel, options="sum tmp 453")

helium_gas = Material("helium_gas", composition={"fractions":[(helium_03, 1.0E-05)],"type":"atom_density"}, options="sum tmp 453")

na_coolant = Material("na_coolant", composition={"fractions":[(na, 2.37718e-02)],"type":"atom_density"}, options="sum tmp 453")

composition_cladding = {
    "fractions": [
        (carbon_nat, 1.97913e-04), (si_28, 9.39458e-04), (si_29, 4.60789e-05), (si_30, 2.93992e-05),
        (p_31, 4.60060e-05), (ti_46, 3.41106e-05), (ti_47, 3.01070e-05), (ti_48, 2.92121e-04),
        (ti_49, 2.09995e-05), (ti_50, 1.97055e-05), (cr_50, 6.61142e-04), (cr_52, 1.22599e-02),
        (cr_53, 1.36391e-03), (cr_54, 3.33224e-04), (mn_55, 1.46981e-03), (fe_54, 3.33120e-03),
        (fe_56, 5.04275e-02), (fe_57, 1.14412e-03), (fe_58, 1.49639e-04), (ni_58, 7.81396e-03),
        (ni_60, 2.90969e-03), (ni_61, 1.24406e-04), (ni_62, 3.90285e-04), (ni_64, 9.62720e-05),
        (mo_92, 1.87735e-04), (mo_94, 1.15707e-04), (mo_95, 1.98193e-04), (mo_96, 2.06406e-04),
        (mo_97, 1.17638e-04), (mo_98, 2.95822e-04), (mo_100, 1.16718e-04)
    ],
    "type": "atom_density"
}

cladding = Material("cladding", composition=composition_cladding, options="sum tmp 453")