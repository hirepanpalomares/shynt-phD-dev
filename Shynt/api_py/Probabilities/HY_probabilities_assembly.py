

def get_HY_probabilities():
        probabilities_hy = {
            1: {
                "regions": {49:{"regions":{},"surfaces":{}},50:{"regions":{},"surfaces":{}}},
                "surfaces": {9:{"regions":{},"surfaces":{}},10:{"regions":{},"surfaces":{}},11:{"regions":{},"surfaces":{}},12:{"regions":{},"surfaces":{}}}
            },
            3: {
                "regions": {55:{"regions":{},"surfaces":{}},56:{"regions":{},"surfaces":{}}},
                "surfaces": {21:{"regions":{},"surfaces":{}},22:{"regions":{},"surfaces":{}},23:{"regions":{},"surfaces":{}},24:{"regions":{},"surfaces":{}}}
            },
            4: {
                "regions": {58:{"regions":{},"surfaces":{}},59:{"regions":{},"surfaces":{}}},
                "surfaces": {27:{"regions":{},"surfaces":{}},28:{"regions":{},"surfaces":{}},29:{"regions":{},"surfaces":{}},30:{"regions":{},"surfaces":{}}}
            },
            14: {
                "regions": {88:{"regions":{},"surfaces":{}},89:{"regions":{},"surfaces":{}}},
                "surfaces": {87:{"regions":{},"surfaces":{}},88:{"regions":{},"surfaces":{}},89:{"regions":{},"surfaces":{}},90:{"regions":{},"surfaces":{}}}
            }
        }


        probabilities_hy[1]["regions"][49]["regions"][49] = np.array([0.206934607638399,0.251669063386091])
        probabilities_hy[1]["regions"][49]["regions"][50] = np.array([0.127014326022925,0.269044452759082])
        probabilities_hy[1]["regions"][50]["regions"][49] = np.array([0.0817570594188428,0.0824679367610927])
        probabilities_hy[1]["regions"][50]["regions"][50] = np.array([0.228429319859206,0.383812896062468])
        probabilities_hy[1]["regions"][49]["surfaces"][9] = np.array([0.166542803421598,0.119792995568699])
        probabilities_hy[1]["regions"][49]["surfaces"][10] = np.array([0.166608450941485,0.120055357456803])
        probabilities_hy[1]["regions"][49]["surfaces"][11] = np.array([0.166435042398389,0.119565795583124])
        probabilities_hy[1]["regions"][49]["surfaces"][12] = np.array([0.166464769577205,0.119872335246201])
        probabilities_hy[1]["regions"][50]["surfaces"][9] = np.array([0.172338782286969,0.133546866893756])
        probabilities_hy[1]["regions"][50]["surfaces"][10] = np.array([0.172777560984723,0.133324753933553])
        probabilities_hy[1]["regions"][50]["surfaces"][11] = np.array([0.172478911464482,0.133523704679041])
        probabilities_hy[1]["regions"][50]["surfaces"][12] = np.array([0.172218365985777,0.133323841670089])

        probabilities_hy[1]["surfaces"][9]["regions"][49] = np.array([0.125599917885510,0.126102871924956])
        probabilities_hy[1]["surfaces"][10]["regions"][49] = np.array([0.125377032448647,0.125676846573072])
        probabilities_hy[1]["surfaces"][11]["regions"][49] = np.array([0.125609472951010,0.125867446516094])
        probabilities_hy[1]["surfaces"][12]["regions"][49] = np.array([0.125585325019308,0.125573451383002])
        probabilities_hy[1]["surfaces"][9]["regions"][50] = np.array([0.238833932776019,0.499137292328557])
        probabilities_hy[1]["surfaces"][10]["regions"][50] = np.array([0.238807270554751,0.499325664916995])
        probabilities_hy[1]["surfaces"][11]["regions"][50] = np.array([0.238943455836014,0.498758683878580])
        probabilities_hy[1]["surfaces"][12]["regions"][50] = np.array([0.238934933938744,0.499450566701203])



        probabilities_hy[1]["surfaces"][9]["surfaces"][9]   = np.array([0,0])
        probabilities_hy[1]["surfaces"][9]["surfaces"][10]  = np.array([0.216308435293886,0.107125186794419])
        probabilities_hy[1]["surfaces"][9]["surfaces"][11]  = np.array([0.209634559417402,0.133813871133826])
        probabilities_hy[1]["surfaces"][9]["surfaces"][12]  = np.array([0.209620044229850,0.133820149937840])
        probabilities_hy[1]["surfaces"][10]["surfaces"][9]  = np.array([0.216632368987707,0.107614210010799])
        probabilities_hy[1]["surfaces"][10]["surfaces"][10] = np.array([0,0])
        probabilities_hy[1]["surfaces"][10]["surfaces"][11] = np.array([0.209391478962938,0.133716754150237])
        probabilities_hy[1]["surfaces"][10]["surfaces"][12] = np.array([0.209789774589569,0.133665268603863])
        probabilities_hy[1]["surfaces"][11]["surfaces"][9]  = np.array([0.209284511924110,0.134318813658243])
        probabilities_hy[1]["surfaces"][11]["surfaces"][10] = np.array([0.209629672625958,0.133966124244573])
        probabilities_hy[1]["surfaces"][11]["surfaces"][11] = np.array([0,0])
        probabilities_hy[1]["surfaces"][11]["surfaces"][12] = np.array([0.216528740588411,0.107091441947448])
        probabilities_hy[1]["surfaces"][12]["surfaces"][9]  = np.array([0.209562166000612,0.133614015258548])
        probabilities_hy[1]["surfaces"][12]["surfaces"][10] = np.array([0.209350687047432,0.133935512228815])
        probabilities_hy[1]["surfaces"][12]["surfaces"][11] = np.array([0.216564814670834,0.107427710275973])
        probabilities_hy[1]["surfaces"][12]["surfaces"][12] = np.array([0,0])


        # ---------------------------------------------

        probabilities_hy[3]["regions"][55]["regions"][55] = np.array([0.206987754370148,0.260540170676173])
        probabilities_hy[3]["regions"][55]["regions"][56] = np.array([0.126551872707213,0.262516771073638])
        probabilities_hy[3]["regions"][56]["regions"][55] = np.array([0.0822112705067555,0.0859917347315646])
        probabilities_hy[3]["regions"][56]["regions"][56] = np.array([0.228150473066375,0.379987161703321])
        
        probabilities_hy[3]["regions"][55]["surfaces"][21] = np.array([0.166677043615561,0.119129051735880])
        probabilities_hy[3]["regions"][55]["surfaces"][22] = np.array([0.166609800986723,0.119255605640872])
        probabilities_hy[3]["regions"][55]["surfaces"][23] = np.array([0.166573689204570,0.119503350997256])
        probabilities_hy[3]["regions"][55]["surfaces"][24] = np.array([0.166598593881917,0.119055049876181])
        probabilities_hy[3]["regions"][56]["surfaces"][21] = np.array([0.172471268148911,0.133581584132113])
        probabilities_hy[3]["regions"][56]["surfaces"][22] = np.array([0.172447638228543,0.133519834220893])
        probabilities_hy[3]["regions"][56]["surfaces"][23] = np.array([0.172416431061570,0.133378496345021])
        probabilities_hy[3]["regions"][56]["surfaces"][24] = np.array([0.172302918987846,0.133541188867087])

        probabilities_hy[3]["surfaces"][21]["regions"][55] = np.array([0.125740429208915,0.131124092130689])
        probabilities_hy[3]["surfaces"][22]["regions"][55] = np.array([0.126000578094396,0.131376585676518])
        probabilities_hy[3]["surfaces"][23]["regions"][55] = np.array([0.125878518246469,0.130712572545304])
        probabilities_hy[3]["surfaces"][24]["regions"][55] = np.array([0.125793798248947,0.131090363454485])
        probabilities_hy[3]["surfaces"][21]["regions"][56] = np.array([0.238214704642319,0.495388283025713])
        probabilities_hy[3]["surfaces"][22]["regions"][56] = np.array([0.238005845640448,0.494492620541037])
        probabilities_hy[3]["surfaces"][23]["regions"][56] = np.array([0.238529180995626,0.494957361127561])
        probabilities_hy[3]["surfaces"][24]["regions"][56] = np.array([0.238268903984335,0.494522618650661])

        probabilities_hy[3]["surfaces"][21]["surfaces"][21] = np.array([0,0])
        probabilities_hy[3]["surfaces"][21]["surfaces"][22] = np.array([0.216620679003327,0.105562342210278])
        probabilities_hy[3]["surfaces"][21]["surfaces"][23] = np.array([0.209666175482244,0.134074436028993])
        probabilities_hy[3]["surfaces"][21]["surfaces"][24] = np.array([0.209755924477264,0.133847885154995])
        probabilities_hy[3]["surfaces"][22]["surfaces"][21] = np.array([0.216542265065672,0.105690292290261])
        probabilities_hy[3]["surfaces"][22]["surfaces"][22] = np.array([0,0])
        probabilities_hy[3]["surfaces"][22]["surfaces"][23] = np.array([0.209863918248687,0.134566081888668])
        probabilities_hy[3]["surfaces"][22]["surfaces"][24] = np.array([0.209583218984036,0.133873679065738])
        probabilities_hy[3]["surfaces"][23]["surfaces"][21] = np.array([0.209885521351541,0.134503434798058])
        probabilities_hy[3]["surfaces"][23]["surfaces"][22] = np.array([0.209403484023906,0.134058539618619])
        probabilities_hy[3]["surfaces"][23]["surfaces"][23] = np.array([0,0])
        probabilities_hy[3]["surfaces"][23]["surfaces"][24] = np.array([0.216300165269941,0.105767351652256])
        probabilities_hy[3]["surfaces"][24]["surfaces"][21] = np.array([0.209745400040916,0.134462598643992])
        probabilities_hy[3]["surfaces"][24]["surfaces"][22] = np.array([0.210003214856814,0.134224741580527])
        probabilities_hy[3]["surfaces"][24]["surfaces"][23] = np.array([0.216185551514949,0.105700418658071])
        probabilities_hy[3]["surfaces"][24]["surfaces"][24] = np.array([0,0])


        # ---------------------------------------------

        probabilities_hy[4]["regions"][58]["regions"][58] = np.array([0.207164370152850,0.275121239408503])
        probabilities_hy[4]["regions"][58]["regions"][59] = np.array([0.125992018673293,0.253056751977260])
        probabilities_hy[4]["regions"][59]["regions"][58] = np.array([0.0825646630739309,0.0916310096598090])
        probabilities_hy[4]["regions"][59]["regions"][59] = np.array([0.227459649489463,0.374039403520436])
        
        probabilities_hy[4]["regions"][58]["surfaces"][27] = np.array([0.166544938885124,0.118113764334458])
        probabilities_hy[4]["regions"][58]["surfaces"][28] = np.array([0.166726903094647,0.118229579160926])
        probabilities_hy[4]["regions"][58]["surfaces"][29] = np.array([0.166813492959868,0.117982625063739])
        probabilities_hy[4]["regions"][58]["surfaces"][30] = np.array([0.166757021308636,0.117496175669665])
        probabilities_hy[4]["regions"][59]["surfaces"][27] = np.array([0.172325158762388,0.133719188926552])
        probabilities_hy[4]["regions"][59]["surfaces"][28] = np.array([0.172552754587544,0.133324876909015])
        probabilities_hy[4]["regions"][59]["surfaces"][29] = np.array([0.172640180626949,0.133523545681478])
        probabilities_hy[4]["regions"][59]["surfaces"][30] = np.array([0.172457593459724,0.133761975302710])

        probabilities_hy[4]["surfaces"][27]["regions"][58] = np.array([0.126208780188658,0.139301330227313])
        probabilities_hy[4]["surfaces"][28]["regions"][58] = np.array([0.126267462052254,0.138789368169178])
        probabilities_hy[4]["surfaces"][29]["regions"][58] = np.array([0.126223669076224,0.138397519883375])
        probabilities_hy[4]["surfaces"][30]["regions"][58] = np.array([0.126176340637394,0.139407711208410])
        probabilities_hy[4]["surfaces"][27]["regions"][59] = np.array([0.236887839269644,0.488101907059726])
        probabilities_hy[4]["surfaces"][28]["regions"][59] = np.array([0.237130102656815,0.488100627303887])
        probabilities_hy[4]["surfaces"][29]["regions"][59] = np.array([0.237048627727544,0.487299551586057])
        probabilities_hy[4]["surfaces"][30]["regions"][59] = np.array([0.236961995027544,0.487961166842173])




        probabilities_hy[4]["surfaces"][27]["surfaces"][27] = np.array([0,0])
        probabilities_hy[4]["surfaces"][27]["surfaces"][28] = np.array([0.216310355002557,0.103445279495641])
        probabilities_hy[4]["surfaces"][27]["surfaces"][29] = np.array([0.210266060277034,0.134784658476386])
        probabilities_hy[4]["surfaces"][27]["surfaces"][30] = np.array([0.210323815004258,0.134369597973691])
        probabilities_hy[4]["surfaces"][28]["surfaces"][27] = np.array([0.216542046459085,0.103082935301780])
        probabilities_hy[4]["surfaces"][28]["surfaces"][28] = np.array([0,0])
        probabilities_hy[4]["surfaces"][28]["surfaces"][29] = np.array([0.209955128326268,0.134920224314262])
        probabilities_hy[4]["surfaces"][28]["surfaces"][30] = np.array([0.210102110879439,0.135109616503913])
        probabilities_hy[4]["surfaces"][29]["surfaces"][27] = np.array([0.209763745812659,0.135167278699415])
        probabilities_hy[4]["surfaces"][29]["surfaces"][28] = np.array([0.210300019310044,0.134800059050396])
        probabilities_hy[4]["surfaces"][29]["surfaces"][29] = np.array([0,0])
        probabilities_hy[4]["surfaces"][29]["surfaces"][30] = np.array([0.216660789696832,0.104336513443192])
        probabilities_hy[4]["surfaces"][30]["surfaces"][27] = np.array([0.210025932755347,0.134844538047996])
        probabilities_hy[4]["surfaces"][30]["surfaces"][28] = np.array([0.210130881178445,0.134347577084373])
        probabilities_hy[4]["surfaces"][30]["surfaces"][29] = np.array([0.216701701948577,0.103443625413364])
        probabilities_hy[4]["surfaces"][30]["surfaces"][30] = np.array([0,0])

        # ---------------------------------------------

        probabilities_hy[14]["regions"][88]["regions"][88] = np.array([0.207248349211150,0.280150733569062])
        probabilities_hy[14]["regions"][88]["regions"][89] = np.array([0.125774484601038,0.249640049055650])
        probabilities_hy[14]["regions"][89]["regions"][88] = np.array([0.0827234634480299,0.0932733806467048])
        probabilities_hy[14]["regions"][89]["regions"][89] = np.array([0.227347196866900,0.371684644127079])
        probabilities_hy[14]["regions"][88]["surfaces"][87] = np.array([0.166890972327234,0.117385667155372])
        probabilities_hy[14]["regions"][88]["surfaces"][88] = np.array([0.166667926810827,0.117406131371497])
        probabilities_hy[14]["regions"][88]["surfaces"][89] = np.array([0.166649024648420,0.117518538387215])
        probabilities_hy[14]["regions"][88]["surfaces"][90] = np.array([0.166768738343667,0.117899611326067])
        probabilities_hy[14]["regions"][89]["surfaces"][87] = np.array([0.172449129978554,0.133543496721579])
        probabilities_hy[14]["regions"][89]["surfaces"][88] = np.array([0.172444891871899,0.133968250282147])
        probabilities_hy[14]["regions"][89]["surfaces"][89] = np.array([0.172530927330568,0.133683146035615])
        probabilities_hy[14]["regions"][89]["surfaces"][90] = np.array([0.172504390504050,0.133847082186875])

        probabilities_hy[14]["surfaces"][87]["regions"][88] = np.array([0.126463894976390,0.141445752100174])
        probabilities_hy[14]["surfaces"][88]["regions"][88] = np.array([0.126194127162374,0.141217020432454])
        probabilities_hy[14]["surfaces"][89]["regions"][88] = np.array([0.126312841338748,0.142055602859349])
        probabilities_hy[14]["surfaces"][90]["regions"][88] = np.array([0.126152922843666,0.141902565523794])
        probabilities_hy[14]["surfaces"][87]["regions"][89] = np.array([0.236666266680982,0.486088326200666])
        probabilities_hy[14]["surfaces"][88]["regions"][89] = np.array([0.236756331228800,0.486107915096211])
        probabilities_hy[14]["surfaces"][89]["regions"][89] = np.array([0.236598357678260,0.484594364468030])
        probabilities_hy[14]["surfaces"][90]["regions"][89] = np.array([0.236721908692722,0.485598622218703])




        probabilities_hy[14]["surfaces"][87]["surfaces"][87] = np.array([0,0])
        probabilities_hy[14]["surfaces"][87]["surfaces"][88] = np.array([0.216771189241648,0.102558844507846])
        probabilities_hy[14]["surfaces"][87]["surfaces"][89] = np.array([0.209966169631824,0.135064986527183])
        probabilities_hy[14]["surfaces"][87]["surfaces"][90] = np.array([0.210129321687434,0.134848034553812])
        probabilities_hy[14]["surfaces"][88]["surfaces"][87] = np.array([0.216666263230513,0.102864511009720])
        probabilities_hy[14]["surfaces"][88]["surfaces"][88] = np.array([0,0])
        probabilities_hy[14]["surfaces"][88]["surfaces"][89] = np.array([0.210364239700012,0.134899821463995])
        probabilities_hy[14]["surfaces"][88]["surfaces"][90] = np.array([0.210014828909744,0.134907756397540])
        probabilities_hy[14]["surfaces"][89]["surfaces"][87] = np.array([0.210416813634703,0.134996336706204])
        probabilities_hy[14]["surfaces"][89]["surfaces"][88] = np.array([0.209983016636957,0.135370586721055])
        probabilities_hy[14]["surfaces"][89]["surfaces"][89] = np.array([0,0])
        probabilities_hy[14]["surfaces"][89]["surfaces"][90] = np.array([0.216684759089995,0.102983109245361])
        probabilities_hy[14]["surfaces"][90]["surfaces"][87] = np.array([0.210220476752022,0.134835497664106])
        probabilities_hy[14]["surfaces"][90]["surfaces"][88] = np.array([0.210323660714286,0.134724641697680])
        probabilities_hy[14]["surfaces"][90]["surfaces"][89] = np.array([0.216577872304582,0.102936693324887])
        probabilities_hy[14]["surfaces"][90]["surfaces"][90] = np.array([0,0])




        return probabilities_hy