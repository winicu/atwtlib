# win.icu 2019~2023
import math
import re


def info_atwt(bool):
    if bool:
        print("By win.icu")
    else:
        print("0.33e304")
#########
# ALIAS
#########


def swap(list, n1, n2):
    temp = list[n1]
    list[n1] = list[n2]
    list[n2] = temp
    return list

#########
# MATH
#########


def rad_deg(num, convert_type: bool):
    if convert_type == 1:
        return math.degrees(num)
    else:
        return math.radians(num)

# 2.Rad&Deg


def rad(num):
    return math.radians(num)


def deg(num):
    return math.degrees(num)


def qbrt(x):
    if x < 0:
        x = abs(x)
        cube_root = pow(x, 1 / 3) * (-1)
    else:
        cube_root = pow(x, 1 / 3)
    return cube_root


def root(times, num):
    return num ** (1 / float(times))


def eng(num):
    return num / 1000


def lcm(a, b):
    if a == b:
        return a
    elif max(a, b) % min(a, b) == 0:
        return max(a, b)
    elif max(a, b) % min(a, b) != 0:
        return a * b


def atwt(a):
    table_atwt = [1.008, 4.002602, 6.94, 9.0121831, 10.81, 12.011, 14.007, 15.999, 18.998403163, 20.1797, 22.98976928, 24.305,
                  26.9815375, 28.085, 30.973761998, 32.06, 35, 45, 39.948, 39.0983, 40.078, 44.955908, 47.867, 50.9415, 51.9961,
                  54.938044, 55.845, 58.933194, 58.6934, 63.546, 65.38, 69.723, 72.630, 74.921595, 78.971, 79.904, 83.798, 85.4678,
                  87.62, 88.90584, 91.224, 92.90637, 95.95, 97, 101.07, 102.90550, 106.42, 107.8682, 112.414, 114.818, 118.710,
                  121.760, 127.60, 126.90447, 131.293, 132.90545196, 137.327, 138.90547, 140.116, 140.90766, 144.212, 145,
                  150.36, 151.964, 157.25, 158.92535, 162.5, 164.93033, 167.259, 168.93422, 173.054, 174.9668, 178.49, 180.94788,
                  183.84, 186.207, 190.23, 192.217, 195.084, 196.966569, 200.592, 204.38, 207.2, 208.98040, 209, 210, 222, 223,
                  226, 227, 232.0377, 231.03588, 238.02891, 237, 244, 243, 247, 247, 251, 252, 257, 258, 259, 262, 267, 270, 271, 270,
                  277, 276, 281, 282, 285, 285, 289, 289, 293, 294, 295, 316, 320, 320, 321, 325, 330, 332, 334, 335]
    return table_atwt[a - 1]


def mcwt(str):
    table_name = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K",
                  "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn",
                  "Ga",
                  "Ge",
                  "As",
                  "Se",
                  "Br",
                  "Kr",
                  "Rb",
                  "Sr",
                  "Y",
                  "Zr",
                  "Nb",
                  "Mo",
                  "Tc",
                  "Ru",
                  "Rh",
                  "Pd",
                  "Ag",
                  "Cd",
                  "In",
                  "Sn",
                  "Sb",
                  "Te",
                  "I",
                  "Xe",
                  "Cs",
                  "Ba",
                  "La",
                  "Ce",
                  "Pr",
                  "Nd",
                  "Pm",
                  "Sm",
                  "Eu",
                  "Gd",
                  "Tb",
                  "Dy",
                  "Ho",
                  "Er",
                  "Tm",
                  "Yb",
                  "Lu",
                  "Hf",
                  "Ta",
                  "W",
                  "Re",
                  "Os",
                  "Ir",
                  "Pt",
                  "Au",
                  "Hg",
                  "Tl",
                  "Pb",
                  "Bi",
                  "Po",
                  "At",
                  "Rn",
                  "Fr",
                  "Ra",
                  "Ac",
                  "Th",
                  "Pa",
                  "U",
                  "Np",
                  "Pu",
                  "Am",
                  "Cm",
                  "Bk",
                  "Cf",
                  "Es",
                  "Fm",
                  "Md",
                  "No",
                  "Lr",
                  "Rf",
                  "Db",
                  "Sg",
                  "Bh",
                  "Hs",
                  "Mt",
                  "Ds",
                  "Rg",
                  "Cn",
                  "Nh",
                  "Fl",
                  "Mc",
                  "Lv",
                  "Ts",
                  "Og",
                  ]
    dic = {'H': '1.01', 'He': '4.0', 'Li': '6.94', 'Be': '9.01', 'B': '10.81', 'C': '12.01', 'N': '14.01', 'O': '16.0',
           'F': '19.0', 'Ne': '20.18', 'Na': '22.99', 'Mg': '24.31', 'Al': '26.98', 'Si': '28.09', 'P': '30.97',
           'S': '32.07', 'Cl': '35.45', 'Ar': '39.95', 'K': '39.1', 'Ca': '40.08', 'Sc': '44.96', 'Ti': '47.87',
           'V': '50.94', 'Cr': '52.0', 'Mn': '54.94', 'Fe': '55.85', 'Co': '58.93', 'Ni': '58.69', 'Cu': '63.55',
           'Zn': '65.39', 'Ga': '69.72', 'Ge': '72.64', 'As': '74.92', 'Se': '78.96', 'Br': '79.9', 'Kr': '83.8',
           'Rb': '85.47', 'Sr': '87.62', 'Y': '88.91', 'Zr': '91.22', 'Nb': '92.91', 'Mo': '95.94', 'Tc': '97.91',
           'Ru': '101.07', 'Rh': '102.91', 'Pd': '106.42', 'Ag': '107.87', 'Cd': '112.41', 'In': '114.82',
           'Sn': '118.71', 'Sb': '121.76', 'Te': '127.6', 'I': '126.9', 'Xe': '131.29', 'Cs': '132.91', 'Ba': '137.33',
           'La': '138.91', 'Ce': '140.12', 'Pr': '140.91', 'Nd': '144.24', 'Pm': '145.0', 'Sm': '150.36',
           'Eu': '151.96', 'Gd': '157.25', 'Tb': '158.93', 'Dy': '162.5', 'Ho': '164.93', 'Er': '167.26',
           'Tm': '168.93', 'Yb': '173.04', 'Lu': '174.97', 'Hf': '178.49', 'Ta': '180.95', 'W': '183.84',
           'Re': '186.21', 'Os': '190.23', 'Ir': '192.22', 'Pt': '195.08', 'Au': '196.97', 'Hg': '200.59',
           'Tl': '204.38', 'Pb': '207.2', 'Bi': '208.98', 'Po': '208.98', 'At': '209.99', 'Rn': '222.02', 'Fr': '223.0',
           'Ra': '226.0', 'Ac': '227.0', 'Th': '232.04', 'Pa': '231.04', 'U': '238.03', 'Np': '238.85', 'Pu': '242.88',
           'Am': '244.86', 'Cm': '246.91', 'Bk': '248.93', 'Cf': '252.96', 'Es': '253.97', 'Fm': '259.0',
           'Md': '260.01', 'No': '261.02', 'Lr': '264.04', 'Rf': '269.08', 'Db': '270.09', 'Sg': '273.11',
           'Bh': '274.12', 'Hs': '272.11', 'Mt': '278.15', 'Ds': '283.19', 'Rg': '282.18', 'Cn': '287.22',
           'Nh': '286.22', 'Fl': '291.2', 'Mc': '290.19', 'Lv': '295.23', 'Ts': '293.21', 'Og': '299.26'}
    div = re.compile(r"([A-Z][a-z]+[\d+]*)|([A-Z]\d*)|(\(.*\)\d+)")
    ele = div.findall(str)
    div_Xx_X = re.compile(r"(\D+)|(\d+)")
    div_XX = re.compile(r"([A-Z][a-z]?\d*)|(\d+)")
    form1 = []
    form2 = []
    form3 = []
    for q in ele:
        Xx_ = div_Xx_X.findall(q[0])
        if len(Xx_) == 2:
            form1.append(float(dic[Xx_[0][0]]) * int(Xx_[1][1]))
        elif len(Xx_) == 1:
            form1.append(float(dic[Xx_[0][0]]))
        X_ = div_Xx_X.findall(q[1])
        if len(X_) == 2:
            form2.append(float(dic[X_[0][0]]) * int(X_[1][1]))
        elif len(X_) == 1:
            form2.append(float(dic[X_[0][0]]))
        XX_ = div_XX.findall(q[2])
        len_XX = len(XX_)
        if len(XX_) != 0:
            for p in range(len_XX - 1):
                XX_X = div_Xx_X.findall(XX_[p][0])
                if len(XX_X) == 2:
                    form3.append(
                        float(dic[XX_X[0][0]]) * int(XX_X[1][1]) * int(XX_[len(XX_) - 1][1]))
                elif len(XX_X) == 1:
                    form3.append(float(dic[XX_X[0][0]])
                                 * int(XX_[len(XX_) - 1][1]))
    return sum(form1) + sum(form2) + sum(form3)
