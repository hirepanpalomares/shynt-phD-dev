import numpy as np

d_tl_br_fast = [
  1.1462610371251978, 
  1.1881609295606355, 
  1.1278642579552787,
  1.1464904657506367
]

d_tr_bl_fast = [
  1.0871895928053532,
  1.158400822582762,
  1.1583333804462206,
  1.2059585642361763
]

d_tl_br_thermal = [
  0.2137139248363373,
  0.21406054967270235,
  0.1846571964556739,
  0.21382060341646633
]

d_tr_bl_fast = [
  0.1777978199752981,
  0.19932416816133292,
  0.19933016199450113,
  0.24985610830137456
]


fuel_scores_cross = {
  4: {
    'regions': {
        4: np.array([0.23919, 0.04257]),
        5: np.array([0.0703033, 0.0133524]), 
        6: np.array([0.0394318 , 0.00740159]), 
        7: np.array([0.0703403, 0.0133532]), 
        8: np.array([0.0532227, 0.0173513]), 
        9: np.array([0.0319633, 0.0102496]), 
        10: np.array([0.0532098, 0.0173482]), 
        11: np.array([0.119549 , 0.0405516]), 
      }, 
      'surfaces': {
        3: np.array([0.430778 , 0.0488801]), 
        4: np.array([0.244036 , 0.0263478]), 
        5: np.array([0.243964 , 0.0263993]), 
        6: np.array([0.430763 , 0.0488799])
      }
    }, 
  5: {
    'regions': {
        4: np.array([0.0702965, 0.0133506]), 
        6: np.array([0.0703099, 0.0133485]), 
        7: np.array([0.0394392 , 0.00740497]), 
        8: np.array([0.0319547, 0.0102618]), 
        9: np.array([0.0532312, 0.0173622]), 
        10: np.array([0.119577 , 0.0405364]), 
        11: np.array([0.0532007, 0.0173504]), 
        5: np.array([0.23912 , 0.042572])
      }, 
      'surfaces': {
        3: np.array([0.243986 , 0.0263594]), 
        4: np.array([0.243963 , 0.0263571]), 
        5: np.array([0.430676 , 0.0488794]), 
        6: np.array([0.430866 , 0.0488995])
      }
    }, 
  6: {
    'regions': { 
      4: np.array([0.0394484 , 0.00742481]), 
      5: np.array([0.070314 , 0.0133466]), 
      7: np.array([0.0703245, 0.0133493]), 
      8: np.array([0.0532094, 0.0173486]), 
      9: np.array([0.119528, 0.040557]), 
      10: np.array([0.0531966, 0.0173571]), 
      11: np.array([0.0319455, 0.0102568]), 
      6: np.array([0.23918 , 0.042557])
    }, 
      'surfaces': {
        3: np.array([0.243983 , 0.0263716]), 
        4: np.array([0.430829 , 0.0489058]), 
        5: np.array([0.430788 , 0.0488838]), 
        6: np.array([0.244059 , 0.0263435])
      }
    }, 
  7: {
    'regions': {   
      4: np.array([0.0702947, 0.013333 ]), 
      5: np.array([0.0394313 , 0.00741875]), 
      6: np.array([0.0702973, 0.0133428]), 
      8: np.array([0.119587 , 0.0405508]), 
      9: np.array([0.053215 , 0.0173705]), 
      10: np.array([0.0319756, 0.0102686]), 
      11: np.array([0.0532268, 0.0173699]), 
      7: np.array([0.23923 , 0.042589])
    }, 
    'surfaces': {
      3: np.array([0.430699 , 0.0488591]), 
      4: np.array([0.430777 , 0.0488795]), 
      5: np.array([0.24406  , 0.0263665]), 
      6: np.array([0.243967 , 0.0263564])
    }
  }
}


coolant_scores_cross = {
  8: {
    'regions': {
      4: np.array([0.0512718, 0.0293162]), 
      5: np.array([0.0299006, 0.0172919]), 
      6: np.array([0.0512978, 0.0293271]), 
      7: np.array([0.125008, 0.068932]), 
      8: np.array([0.518267, 0.53761 ]), 
      9: np.array([0.0829771, 0.0658807]), 
      10: np.array([0.0373621, 0.0303513]), 
      11: np.array([0.082996 , 0.0659243])
    }, 
    'surfaces': {
      3: np.array([0.861213, 0.40349 ]), 
      4: np.array([0.228492 , 0.0789344]), 
      5: np.array([0.228458 , 0.0788802]), 
      6: np.array([0.861385, 0.403521])
    }
  }, 
  9: {
    'regions': {    
      4: np.array([0.0298986, 0.0172776]), 
      5: np.array([0.0512856, 0.0293479]), 
      6: np.array([0.124946 , 0.0689462]), 
      7: np.array([0.0512998, 0.0293039]), 
      8: np.array([0.0829937, 0.065893 ]), 
      9: np.array([0.518368, 0.537515]), 
      10: np.array([0.0830004, 0.0659412]), 
      11: np.array([0.0373885, 0.0303166])
    }, 
    'surfaces': {
      3: np.array([0.861213, 0.40349 ]), 
      4: np.array([0.228492 , 0.0789344]), 
      5: np.array([0.228458 , 0.0788802]), 
      6: np.array([0.861385, 0.403521])
    }
  }, 
  10: {
    'regions': {    
      4: np.array([0.0512866, 0.0293362]), 
      5: np.array([0.125015 , 0.0689427]), 
      6: np.array([0.051331 , 0.0293075]), 
      7: np.array([0.0299126, 0.017291 ]), 
      8: np.array([0.0373717, 0.0303713]), 
      9: np.array([0.082958 , 0.0658854]), 
      10: np.array([0.518343, 0.537473]), 
      11: np.array([0.0830025, 0.0659213])
    }, 
    'surfaces': {
      3: np.array([0.861213, 0.40349 ]), 
      4: np.array([0.228492 , 0.0789344]), 
      5: np.array([0.228458 , 0.0788802]), 
      6: np.array([0.861385, 0.403521])
    }
  }, 
  11: {
    'regions': {    
      4: np.array([0.125002 , 0.0689138]), 
      5: np.array([0.051327 , 0.0293306]), 
      6: np.array([0.0299077, 0.0172946]), 
      7: np.array([0.0513243, 0.029338 ]), 
      8: np.array([0.0829499, 0.0658874]), 
      9: np.array([0.0373644, 0.0303073]), 
      10: np.array([0.083044 , 0.0659047]), 
      11: np.array([0.518268, 0.537542])
    }, 
    'surfaces': {
      3: np.array([0.861213, 0.40349 ]), 
      4: np.array([0.228492 , 0.0789344]), 
      5: np.array([0.228458 , 0.0788802]), 
      6: np.array([0.861385, 0.403521])
    }
  }
}


surface_scores_cross = {
  3: {
   'regions': {
      4: np.array([0.391189, 0.071044]), 
      5: np.array([0.215552 , 0.0381572]), 
      6: np.array([0.215513, 0.038143]), 
      7: np.array([0.391237 , 0.0709955]), 
      8: np.array([0.909029, 0.375907]), 
      9: np.array([0.248868 , 0.0725619]), 
      10: np.array([0.248918 , 0.0725688]), 
      11: np.array([0.908976, 0.37583 ])
    }, 
    'surfaces': {
      3: np.array([0., 0.]), 
      4: np.array([2.02783 , 0.238407]), 
      5: np.array([2.09112 , 0.192513]), 
      6: np.array([2.02786 , 0.238398])
    }
  }, 
  4: {
    'regions': {
      4: np.array([0.215569 , 0.0381619]), 
      5: np.array([0.215575 , 0.0381501]), 
      6: np.array([0.391299 , 0.0710633]), 
      7: np.array([0.391128 , 0.0710539]), 
      8: np.array([0.90889 , 0.375803]), 
      9: np.array([0.908676, 0.375871]), 
      10: np.array([0.248927 , 0.0725893]), 
      11: np.array([0.248845 , 0.0725711])
    }, 
    'surfaces': {
      3: np.array([2.02789, 0.23838]), 
      4: np.array([0., 0.]), 
      5: np.array([2.02783 , 0.238433]), 
      6: np.array([2.09105 , 0.192497])
    }
  }, 
  5: {
    'regions': {
      4: np.array([0.215597 , 0.0381365]), 
      5: np.array([0.391287 , 0.0710475]), 
      6: np.array([0.39129  , 0.0710291]), 
      7: np.array([0.215541 , 0.0381428]), 
      8: np.array([0.248833 , 0.0725878]), 
      9: np.array([0.908838, 0.375759]), 
      10: np.array([0.908777, 0.375843]), 
      11: np.array([0.248873 , 0.0725982])
    }, 
    'surfaces': {
      3: np.array([2.09114 , 0.192504]), 
      4: np.array([2.02793 , 0.238374]), 
      5: np.array([0., 0.]), 
      6: np.array([2.02788 , 0.238403])
    }
  }, 
  6: {
    'regions': {
      4: np.array([0.39124  , 0.0710486]), 
      5: np.array([0.391261 , 0.0710487]), 
      6: np.array([0.215521 , 0.0381357]), 
      7: np.array([0.215609 , 0.0381449]), 
      8: np.array([0.248903, 0.07263 ]), 
      9: np.array([0.248841 , 0.0725702]), 
      10: np.array([0.908913, 0.375754]), 
      11: np.array([0.90895 , 0.375843])
    }, 
    'surfaces': {
      3: np.array([2.02787 , 0.238327]), 
      4: np.array([2.09083 , 0.192507]), 
      5: np.array([2.02796 , 0.238357]), 
      6: np.array([0., 0.])
    }
  }
}


pin_2r_fuel = {
  1: {
    'regions': {
      2: np.array([1.03225 , 0.341866]), 
      1: np.array([1.67643, 0.30696])
    }, 
    'surfaces': {
      3: np.array([1.34976 , 0.150415]), 
      4: np.array([1.34984 , 0.150528]), 
      5: np.array([1.35026 , 0.150426]), 
      6: np.array([1.34941 , 0.150518])
    }
  }
}

pin_2r_coolant = {
  2: {
    'regions': {
      1: np.array([1.03024, 0.579666]), 
      2: np.array([2.88664, 2.79913])
    }, 
    'surfaces': {
      3: np.array([2.17911, 0.964563]), 
      4: np.array([2.17981, 0.964423]), 
      5: np.array([2.17920, 0.964796]), 
      6: np.array([2.17946, 0.964897])}
    }
}

pin_2r_surfaces = {
  3: {
    'regions': {
      1: np.array([1.21359, 0.21846]), 
      2: np.array([2.31547 , 0.897233])
    }, 
    'surfaces': {
      3: np.array([0., 0.]), 
      4: np.array([2.02811 , 0.238031]), 
      5: np.array([2.09131 , 0.192502]), 
      6: np.array([2.02822 , 0.238468])}
    }, 
  4: {
    'regions': {
      1: np.array([1.2132  , 0.218299]), 
      2: np.array([2.31614 , 0.897232])
    }, 
    'surfaces': {
      3: np.array([2.02798 , 0.238452]), 
      4: np.array([0., 0.]), 
      5: np.array([2.02827 , 0.238348]), 
      6: np.array([2.09093 , 0.192301])}
    }, 
  5: {
    'regions': {
      1: np.array([1.2134 , 0.21848]), 
      2: np.array([2.31512, 0.89661])
    }, 
    'surfaces': {
      3: np.array([2.09195 , 0.192602]), 
      4: np.array([2.02804 , 0.238427]), 
      5: np.array([0., 0.]), 
      6: np.array([2.02798 , 0.238254])}
    }, 
  6: {
    'regions': {
      1: np.array([1.21338 , 0.218355]), 
      2: np.array([2.31549 , 0.896841])
    }, 
    'surfaces': {
      3: np.array([2.02825 , 0.238166]), 
      4: np.array([2.09139 , 0.192372]), 
      5: np.array([2.02794 , 0.238464]), 
      6: np.array([0., 0.])
    }
  }
}


fuel_regions_cross = [4,5,6,7]
coolant_regions_cross = [8,9,10,11]

cool_region_2r = 2
fuel_region_2r = 1
surfaces = [3,4,5,6]


def fuel_scores():
  

  fuel_to_coolant_cross = np.zeros(2)
  fuel_to_s3_cross = np.zeros(2)
  fuel_to_s4_cross = np.zeros(2)
  fuel_to_s5_cross = np.zeros(2)
  fuel_to_s6_cross = np.zeros(2)

  fuel_to_fuel = np.zeros(2)

  for fr in fuel_regions_cross:
    for cr in coolant_regions_cross:
      fuel_to_coolant_cross += fuel_scores_cross[fr]['regions'][cr]
    for fr_p in fuel_regions_cross:
      fuel_to_fuel += fuel_scores_cross[fr]['regions'][fr_p]
    fuel_to_s3_cross += fuel_scores_cross[fr]['surfaces'][3]
    fuel_to_s4_cross += fuel_scores_cross[fr]['surfaces'][4]
    fuel_to_s5_cross += fuel_scores_cross[fr]['surfaces'][5]
    fuel_to_s6_cross += fuel_scores_cross[fr]['surfaces'][6]

  print("fuel_to_coolant ---------------------------------")
  print(fuel_to_coolant_cross)
  print(pin_2r_fuel[fuel_region_2r]['regions'][cool_region_2r])
  print("fuel_to_fuel ---------------------------------")
  print(fuel_to_fuel)
  print(pin_2r_fuel[fuel_region_2r]['regions'][fuel_region_2r])
  print("fuel_to_s3 ---------------------------------")
  print(fuel_to_s3_cross)
  print(pin_2r_fuel[fuel_region_2r]['surfaces'][3])
  print("fuel_to_s4 ---------------------------------")
  print(fuel_to_s4_cross)
  print(pin_2r_fuel[fuel_region_2r]['surfaces'][4])
  print("fuel_to_s5 ---------------------------------")
  print(fuel_to_s5_cross)
  print(pin_2r_fuel[fuel_region_2r]['surfaces'][5])
  print("fuel_to_s6 ---------------------------------")
  print(fuel_to_s6_cross)
  print(pin_2r_fuel[fuel_region_2r]['surfaces'][6])

def coolant_scores():

  coolant_to_fuel_cross = np.zeros(2)
  coolant_to_s3_cross = np.zeros(2)
  coolant_to_s4_cross = np.zeros(2)
  coolant_to_s5_cross = np.zeros(2)
  coolant_to_s6_cross = np.zeros(2)
  coolant_to_coolant = np.zeros(2)


  for cr in coolant_regions_cross:
    for fr in fuel_regions_cross:
      coolant_to_fuel_cross += coolant_scores_cross[cr]['regions'][fr]
    for cr_p in coolant_regions_cross:
      coolant_to_coolant += coolant_scores_cross[cr]['regions'][cr_p]
    coolant_to_s3_cross += coolant_scores_cross[cr]['surfaces'][3]
    coolant_to_s4_cross += coolant_scores_cross[cr]['surfaces'][4]
    coolant_to_s5_cross += coolant_scores_cross[cr]['surfaces'][5]
    coolant_to_s6_cross += coolant_scores_cross[cr]['surfaces'][6]

  print("coolant_to_fuel ---------------------------------")
  print(coolant_to_fuel_cross)
  print(pin_2r_coolant[cool_region_2r]['regions'][fuel_region_2r])
  
  print("coolant_to_coolant ---------------------------------")
  print(coolant_to_coolant)
  print(pin_2r_coolant[cool_region_2r]['regions'][cool_region_2r])
  
  print("coolant_to_s3 ---------------------------------")
  print(coolant_to_s3_cross)
  print(pin_2r_coolant[cool_region_2r]['surfaces'][3])
  print("coolant_to_s4 ---------------------------------")
  print(coolant_to_s4_cross)
  print(pin_2r_coolant[cool_region_2r]['surfaces'][4])
  print("coolant_to_s5 ---------------------------------")
  print(coolant_to_s5_cross)
  print(pin_2r_coolant[cool_region_2r]['surfaces'][5])
  print("coolant_to_s6 ---------------------------------")
  print(coolant_to_s6_cross)
  print(pin_2r_coolant[cool_region_2r]['surfaces'][6])


def surface_scores():
 
  for s in surfaces:
    surf_to_fuel = np.zeros(2)
    for fr in fuel_regions_cross:
      surf_to_fuel += surface_scores_cross[s]['regions'][fr]
    print(f"surface_{s}_to_fuel -----------------------------")
    print(surf_to_fuel)
    print(pin_2r_surfaces[s]['regions'][fuel_region_2r])
    surf_to_coolant = np.zeros(2)
    for cr in coolant_regions_cross:
      surf_to_coolant += surface_scores_cross[s]['regions'][cr]

    print(f"surface_{s}_to_coolant --------------------------")
    print(surf_to_coolant)
    print(pin_2r_surfaces[s]['regions'][cool_region_2r])
    for sp in surfaces:
      print(f"surface_{s}_to_surface{sp} --------------------------")
      print(surface_scores_cross[s]['surfaces'][sp])
      print(pin_2r_surfaces[s]['surfaces'][sp])
    print("**************************************************")




if __name__=='__main__':
  # fuel_scores()
  coolant_scores()
  # surface_scores()