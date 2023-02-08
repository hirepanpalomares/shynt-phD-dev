
import numpy as np


fuel_regions_cross = [4,5,6,7]
cool_region = 2
fuel_region_2r = 1
surfaces = [3,4,5,6]

def fuel_scores():
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

  # pin_cross_fuel = {
  #   4: {
  #     'regions': {
  #       5: np.array([0.0741275, 0.01332990]), 
  #       7: np.array([0.0742435, 0.01330240]), 
  #       6: np.array([0.0525849, 0.00741579]), 
  #       2: np.array([0.3008140, 0.08557860]), 
  #       4: np.array([0.2562000, 0.04264300])
  #     },
  #     'surfaces': {
  #       3: np.array([0.567115 , 0.0490694]), 
  #       4: np.array([0.567472 , 0.0488614]), 
  #       5: np.array([0.405170  , 0.0264219]), 
  #       6: np.array([0.405157 , 0.0263659])
  #     }
  #   },
  #   5: {
  #     'regions': {
  #       4: np.array([0.0743179, 0.0133251]), 
  #       7: np.array([0.0527244 , 0.00741846]), 
  #       6: np.array([0.0741388, 0.0133073]), 
  #       2: np.array([0.300809 , 0.0855392]), 
  #       5: np.array([0.25631 , 0.042608])
  #     }, 
  #     'surfaces': {
  #       3: np.array([0.405005, 0.026398]), 
  #       4: np.array([0.56709  , 0.0488257]), 
  #       5: np.array([0.567315 , 0.0489074]), 
  #       6: np.array([0.40516  , 0.0263201])
  #     }
  #   }, 
  #   7: {
  #     'regions': {  
  #       4: np.array([0.0741871, 0.0133815]), 
  #       5: np.array([0.0525673 , 0.00742428]), 
  #       6: np.array([0.0742463, 0.0133326]), 
  #       2: np.array([0.300829 , 0.0855434]), 
  #       7: np.array([0.25618 , 0.042451])
  #     }, 
  #     'surfaces': {
  #       3: np.array([0.566822 , 0.0488216]), 
  #       4: np.array([0.405422 , 0.0263152]), 
  #       5: np.array([0.404957 , 0.0264353]), 
  #       6: np.array([0.567359 , 0.0488131])
  #     }
  #   }, 
  #   6: {
  #     'regions': {    
  #       4: np.array([0.0527596, 0.00744856]), 
  #       5: np.array([0.0741827, 0.01336610]), 
  #       7: np.array([0.0741764, 0.01331130]), 
  #       2: np.array([0.3006330, 0.08541040]), 
  #       6: np.array([0.2564100, 0.04257500])
  #     }, 
  #     'surfaces': {
  #       3: np.array([0.405301 , 0.0264173]), 
  #       4: np.array([0.405485 , 0.0263726]), 
  #       5: np.array([0.567359 , 0.0489296]), 
  #       6: np.array([0.566899 , 0.0487834])
  #     }
  #   }
  # }

  pin_cross_fuel = {
    4: {
      'regions': {
        5: np.array([0.0832094, 0.0150921]), 
        7: np.array([0.0831026, 0.0150332]), 
        6: np.array([0.0774778, 0.0107356]), 
        2: np.array([0.391922, 0.119255]), 
        4: np.array([0.23917 , 0.042493])
      }, 
      'surfaces': {
        3: np.array([0.539229 , 0.0553104]), 
        4: np.array([0.539234 , 0.0553665]), 
        5: np.array([0.547897 , 0.0413907]), 
        6: np.array([0.547878 , 0.0415391])
      }
    }, 
    5: {
      'regions': {
        4: np.array([0.0831771, 0.0150466]), 
        7: np.array([0.0775665, 0.0107084]), 
        6: np.array([0.0831802, 0.0150714]), 
        2: np.array([0.392258, 0.118934]), 
        5: np.array([0.23925 , 0.042434])
      }, 
      'surfaces': {
        3: np.array([0.547877 , 0.0414492]), 
        4: np.array([0.539737, 0.055514]), 
        5: np.array([0.539528 , 0.0553315]), 
        6: np.array([0.547675 , 0.0414725])
      }
    },
    7: {
      'regions': {
        4: np.array([0.0830005, 0.0150426]), 
        5: np.array([0.0774039, 0.010808 ]), 
        6: np.array([0.0830573, 0.0150761]), 
        2: np.array([0.391527, 0.119275]), 
        7: np.array([0.2392  , 0.042594])
      }, 
      'surfaces': {
        3: np.array([0.539446 , 0.0555074]), 
        4: np.array([0.547389 , 0.0414215]), 
        5: np.array([0.547958 , 0.0414864]), 
        6: np.array([0.539554 , 0.0555486])
      }
    }, 
    6: {
      'regions': {
        4: np.array([0.0774384, 0.0107489]), 
        5: np.array([0.0830957, 0.0150561]), 
        7: np.array([0.0831176, 0.0150863]), 
        2: np.array([0.391744, 0.119235]), 
        6: np.array([0.23919 , 0.042555])
      }, 
      'surfaces': {
        3: np.array([0.547751 , 0.0414628]), 
        4: np.array([0.547677 , 0.0415005]), 
        5: np.array([0.538821 , 0.0554305]), 
        6: np.array([0.538807 , 0.0554125])
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