
import numpy as np


fuel_regions_cross = [4,5,6,7]
cool_region = 2
fuel_region_2r = 1
surfaces = [3,4,5,6]

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


def fuel_scores():
  pin_cross_fuel = {
    4: {
      'regions': {
        5: np.array([0.0702973, 0.0133067]), 
        7: np.array([0.0701908, 0.0133524]), 
        6: np.array([0.0393805 , 0.00739185]), 
        2: np.array([0.257929 , 0.0853058]), 
        4: np.array([0.23937 , 0.042601])
      }, 
      'surfaces': {  
        3: np.array([0.430668 , 0.0489348]), 
        4: np.array([0.24422 , 0.026355]), 
        5: np.array([0.244108 , 0.0263972]), 
        6: np.array([0.430721 , 0.0488902])}
      }, 
    5: {
      'regions': {    
        4: np.array([0.0703702, 0.0133134]), 
        7: np.array([0.0393968 , 0.00742688]), 
        6: np.array([0.0702892, 0.0133781]), 
        2: np.array([0.258122 , 0.0855177]), 
        5: np.array([0.23932 , 0.042604])
      }, 
      'surfaces': {  
        3: np.array([0.244158 , 0.0263605]), 
        4: np.array([0.243879 , 0.0262914]), 
        5: np.array([0.430968 , 0.0489165]), 
        6: np.array([0.430961 , 0.0488284])
      }
    }, 
    7: {
      'regions': {
        4: np.array([0.0702873, 0.0134151]), 
        5: np.array([0.0394215 , 0.00744878]), 
        6: np.array([0.0701672, 0.0133807]), 
        2: np.array([0.257933 , 0.0854667]), 
        7: np.array([0.23936 , 0.042602])
      }, 
      'surfaces': {  
        3: np.array([0.430608 , 0.0488196]), 
        4: np.array([0.430764 , 0.0488736]), 
        5: np.array([0.244105 , 0.0263607]), 
        6: np.array([0.243843 , 0.0263938])
      }
    }, 
    6: {
      'regions': {    
        4: np.array([0.0394504 , 0.00743613]), 
        5: np.array([0.0702596, 0.0134109]), 
        7: np.array([0.0702297, 0.0133523]), 
        2: np.array([0.257997 , 0.0854905]), 
        6: np.array([0.239   , 0.042663])
      }, 
      'surfaces': {  
        3: np.array([0.244261 , 0.0263922]), 
        4: np.array([0.431177 , 0.0489032]), 
        5: np.array([0.430736 , 0.0488238]), 
        6: np.array([0.243891 , 0.0264372])
      }
    }
  }

  

  fuel_to_coolant_cross = np.zeros(2)
  fuel_to_s3_cross = np.zeros(2)
  fuel_to_s4_cross = np.zeros(2)
  fuel_to_s5_cross = np.zeros(2)
  fuel_to_s6_cross = np.zeros(2)

  fuel_to_fuel = np.zeros(2)

  for fr in fuel_regions_cross:
    fuel_to_coolant_cross += pin_cross_fuel[fr]['regions'][cool_region]
    fuel_to_s3_cross += pin_cross_fuel[fr]['surfaces'][3]
    fuel_to_s4_cross += pin_cross_fuel[fr]['surfaces'][4]
    fuel_to_s5_cross += pin_cross_fuel[fr]['surfaces'][5]
    fuel_to_s6_cross += pin_cross_fuel[fr]['surfaces'][6]
    for fr_p in fuel_regions_cross:
      fuel_to_fuel += pin_cross_fuel[fr]['regions'][fr_p]

  print("fuel_to_coolant ---------------------------------")
  print(fuel_to_coolant_cross)
  print(pin_2r_fuel[fuel_region_2r]['regions'][cool_region])
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
  pin_cross_coolant = {
    2: {
      'regions': {
        4: np.array([0.257263, 0.144849]), 
        5: np.array([0.257388, 0.144847]), 
        7: np.array([0.257694, 0.144897]), 
        6: np.array([0.257747, 0.144721]), 
        2: np.array([2.886430, 2.799220])
      }, 
      'surfaces': {
        3: np.array([2.17967 , 0.964898]), 
        4: np.array([2.17953 , 0.964874]), 
        5: np.array([2.17933 , 0.964703]), 
        6: np.array([2.17914 , 0.965028])
      }
    }
  }

  coolant_to_fuel_cross = np.zeros(2)
  
  for fr in fuel_regions_cross:
    coolant_to_fuel_cross += pin_cross_coolant[cool_region]['regions'][fr]
  coolant_to_s3_cross = pin_cross_coolant[cool_region]['surfaces'][3]
  coolant_to_s4_cross = pin_cross_coolant[cool_region]['surfaces'][4]
  coolant_to_s5_cross = pin_cross_coolant[cool_region]['surfaces'][5]
  coolant_to_s6_cross = pin_cross_coolant[cool_region]['surfaces'][6]
  coolant_to_coolant = pin_cross_coolant[cool_region]['regions'][cool_region]

  print("coolant_to_fuel ---------------------------------")
  print(coolant_to_fuel_cross)
  print(pin_2r_coolant[cool_region]['regions'][fuel_region_2r])
  
  print("coolant_to_coolant ---------------------------------")
  print(coolant_to_coolant)
  print(pin_2r_coolant[cool_region]['regions'][cool_region])
  
  print("coolant_to_s3 ---------------------------------")
  print(coolant_to_s3_cross)
  print(pin_2r_coolant[cool_region]['surfaces'][3])
  print("coolant_to_s4 ---------------------------------")
  print(coolant_to_s4_cross)
  print(pin_2r_coolant[cool_region]['surfaces'][4])
  print("coolant_to_s5 ---------------------------------")
  print(coolant_to_s5_cross)
  print(pin_2r_coolant[cool_region]['surfaces'][5])
  print("coolant_to_s6 ---------------------------------")
  print(coolant_to_s6_cross)
  print(pin_2r_coolant[cool_region]['surfaces'][6])

def surface_scores():
  
  pin_cross_surfaces = {
    3: {
      'regions': {
        4: np.array([0.391338 , 0.0709924]), 
        5: np.array([0.215473, 0.038123]), 
        7: np.array([0.391167 , 0.0710838]), 
        6: np.array([0.215656 , 0.0380994]), 
        2: np.array([2.31584 , 0.896692])
      },   
      'surfaces': {
        3: np.array([0., 0.]), 
        4: np.array([2.02748, 0.23834]), 
        5: np.array([2.09146 , 0.192205]), 
        6: np.array([2.02787 , 0.238273])
      }
    },
    4: {
      'regions': {
        4: np.array([0.391453 , 0.0710234]), 
        5: np.array([0.391198 , 0.0711059]), 
        7: np.array([0.215557 , 0.0380645]), 
        6: np.array([0.215494 , 0.0380473]), 
        2: np.array([2.31468 , 0.896737])
      }, 
      'surfaces': {
        3: np.array([2.02807 , 0.238302]), 
        4: np.array([0., 0.]), 
        5: np.array([2.02754 , 0.238098]), 
        6: np.array([2.09052 , 0.192431])
      }
    }, 
    5: {
      'regions': {
        4: np.array([0.215769 , 0.0380809]), 
        5: np.array([0.390965 , 0.0710159]), 
        7: np.array([0.21563  , 0.0380964]), 
        6: np.array([0.391322 , 0.0710865]), 
        2: np.array([2.31539 , 0.896384])
      }, 
      'surfaces': {
        3: np.array([2.09124 , 0.192305]), 
        4: np.array([2.02798 , 0.238262]), 
        5: np.array([0., 0.]), 
        6: np.array([2.02781 , 0.238127])
      }
    }, 
    6: {
      'regions': {
        4: np.array([0.215367 , 0.0380945]), 
        5: np.array([0.215524 , 0.0381413]), 
        7: np.array([0.391414 , 0.0710654]), 
        6: np.array([0.39092  , 0.0709774]), 
        2: np.array([2.31514 , 0.896432])
      }, 
      'surfaces': {
        3: np.array([2.02742 , 0.238266]), 
        4: np.array([2.09052 , 0.192487]), 
        5: np.array([2.02825 , 0.238281]), 
        6: np.array([0., 0.])
      }
    }
  }

  for s in surfaces:
    surf_to_fuel = np.zeros(2)
    for fr in fuel_regions_cross:
      surf_to_fuel += pin_cross_surfaces[s]['regions'][fr]
    print(f"surface_{s}_to_fuel -----------------------------")
    print(surf_to_fuel)
    print(pin_2r_surfaces[s]['regions'][fuel_region_2r])

    print(f"surface_{s}_to_coolant --------------------------")
    print(pin_cross_surfaces[s]['regions'][cool_region])
    print(pin_2r_surfaces[s]['regions'][cool_region])
    for sp in surfaces:
      print(f"surface_{s}_to_surface{sp} --------------------------")
      print(pin_cross_surfaces[s]['surfaces'][sp])
      print(pin_2r_surfaces[s]['surfaces'][sp])
    print("**************************************************")



if __name__=='__main__':
  fuel_scores()
  # coolant_scores()
  # surface_scores()