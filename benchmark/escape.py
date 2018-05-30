input_domains = {'M' : 3, 'V' : 4, 'H' : 5}

# input: [name, arity, dimension0, dimension1, ...]
input_relations = {'MmethArg': ['M', 'V'], 'MmethRet': ['M', 'V'], 
                   'VH': ['V', 'H'], 'HFH': ['H', 'H']}
input_tuples = [['MmethArg', 0, 0], ['MmethArg', 1, 3], ['MmethArg', 2, 2], ['MmethRet', 0, 1], ['MmethRet', 2, 1], ['VH', 1, 1], ['VH', 0, 0], ['VH', 2, 2], ['VH', 3, 3], ['HFH', 0, 1], ['HFH', 1, 2], ['HFH', 2, 3], ['HFH', 0, 2]]

# output
output_relations = {'rMH': ['M', 'H'], 'rRH': ['M', 'H'], 'rHH' :['H', 'H']}
output_tuples = [['rMH', 0, 0], ['rMH', 0, 1], ['rMH', 0, 2], ['rMH', 0, 3], ['rMH', 1, 3], ['rMH', 2, 2], ['rMH', 2, 3], ['rRH', 0, 1], ['rRH', 0, 2], ['rRH', 0, 3], ['rRH', 2, 1], ['rRH', 2, 2], ['rRH', 2, 3], ['rHH', 0, 1], ['rHH', 1, 2], ['rHH', 2, 3], ['rHH', 0, 2], ['rHH', 1, 3], ['rHH', 0, 3]]

# rules
true_rules = [
['rHH(x0H,x2H)', 'HFH(x0H,x2H)'],
['rHH(x0H,x3H)', 'HFH(x0H,x2H)', 'rHH(x2H,x3H)'],
['rMH(x2M,x1H)', 'MmethArg(x2M,x0V)', 'VH(x0V,x1H)'],
['rMH(x0M,x2H)', 'rHH(x1H,x2H)', 'rMH(x0M,x1H)'],
['rRH(x0M,x2H)', 'rHH(x1H,x2H)', 'rRH(x0M,x1H)'],
['rRH(x2M,x1H)', 'MmethRet(x2M,x0V)', 'VH(x0V,x1H)'],
]

rules = [['rHH(x0H,x2H)', 'HFH(x0H,x2H)'], ['rHH(x3H,x2H)', 'HFH(x0H,x2H)', 'rHH(x3H,x0H)'], ['rHH(x0H,x3H)', 'HFH(x0H,x2H)', 'rHH(x2H,x3H)'], ['rHH(x2H,x1H)', 'rHH(x0H,x1H)', 'rHH(x2H,x0H)'], ['rMH(x0M,x1H)', 'rRH(x0M,x1H)'], ['rMH(x2M,x1H)', 'MmethArg(x2M,x0V)', 'VH(x0V,x1H)'], ['rMH(x2M,x1H)', 'MmethRet(x2M,x0V)', 'VH(x0V,x1H)'], ['rMH(x2M,x1H)', 'rMH(x0M,x1H)', 'rRH(x2M,x1H)'], ['rMH(x2M,x1H)', 'rHH(x0H,x1H)', 'rRH(x2M,x1H)'], ['rMH(x2M,x1H)', 'VH(x0V,x1H)', 'rRH(x2M,x1H)'], ['rMH(x3M,x2H)', 'HFH(x0H,x2H)', 'rRH(x3M,x0H)'], ['rMH(x3M,x2H)', 'HFH(x0H,x2H)', 'rMH(x3M,x0H)'], ['rMH(x0M,x1H)', 'rHH(x1H,x2H)', 'rRH(x0M,x1H)'], ['rMH(x0M,x2H)', 'rHH(x1H,x2H)', 'rRH(x0M,x1H)'], ['rMH(x0M,x2H)', 'rHH(x1H,x2H)', 'rMH(x0M,x1H)'], ['rRH(x0M,x1H)', 'rMH(x0M,x1H)'], ['rRH(x2M,x1H)', 'MmethArg(x2M,x0V)', 'VH(x0V,x1H)'], ['rRH(x2M,x1H)', 'MmethRet(x2M,x0V)', 'VH(x0V,x1H)'], ['rRH(x2M,x1H)', 'rMH(x2M,x1H)', 'rRH(x0M,x1H)'], ['rRH(x2M,x1H)', 'rHH(x0H,x1H)', 'rMH(x2M,x1H)'], ['rRH(x2M,x1H)', 'VH(x0V,x1H)', 'rMH(x2M,x1H)'], ['rRH(x3M,x2H)', 'HFH(x0H,x2H)', 'rRH(x3M,x0H)'], ['rRH(x3M,x2H)', 'HFH(x0H,x2H)', 'rMH(x3M,x0H)'], ['rRH(x0M,x1H)', 'rHH(x1H,x2H)', 'rMH(x0M,x1H)'], ['rRH(x0M,x2H)', 'rHH(x1H,x2H)', 'rRH(x0M,x1H)'], ['rRH(x0M,x2H)', 'rHH(x1H,x2H)', 'rMH(x0M,x1H)']]

rule_weights = {
'253':
[(1,0.99), (2,0.0837434932828377), (3,0.01), (4,0.99), (5,0.01), (6,0.99), (7,0.01), (8,0.019128406553835964), (9,0.01), (10,0.01), (11,1.0), (12,0.4771660070157512), (13,0.014981750252239086), (14,0.9500277708569375), (15,0.99), (16,0.01), (17,0.01), (18,0.99), (19,0.01), (20,0.01), (21,0.01), (22,0.3425844219127545), (23,0.99), (24,0.01), (25,0.9793613261560401), (26,0.6888092232518052)],
'253_soup_50':
[(1,0.99), (3,0.99), (4,0.5065556501910546), (6,0.99), (9,0.01), (11,0.13714232271992144), (12,0.99), (13,0.01), (14,0.99), (17,0.01), (18,0.99), (21,0.01), (22,0.99)],
'253_soup_75':
[(1,0.99), (2,0.947298810629008), (4,0.17063565778560197), (5,0.01), (6,0.6899382395362095), (7,0.01), (8,0.013173981667328853), (10,0.01), (11,1.0), (12,0.4771660070157512), (13,0.01), (14,0.7341031345026698), (16,0.5970232478175928), (17,0.3627765454142803), (18,0.99), (20,0.13714232271992144), (21,0.8418680625061747), (24,0.99), (25,0.05554837565002524), (26,0.019128406553835964)],
'34':
[(1,0.99), (2,0.01), (3,0.99), (4,0.018838172746085124), (5,0.01), (6,0.99), (7,0.01), (8,0.01), (9,0.01), (10,0.01), (11,0.99), (12,0.68752384348049), (13,0.01), (14,0.7282803491116691), (15,0.99), (16,0.01), (17,0.01), (18,0.99), (19,0.01), (20,0.01), (21,0.01), (22,0.99), (23,0.1459576960664185), (24,0.01), (25,0.6179190543130938), (26,0.5322546210937495)],
'34_soup_50':
[(1,0.99), (3,0.7039881700829288), (4,0.99), (6,0.99), (9,0.01), (11,0.99), (12,0.99), (13,0.01), (14,0.751149605122621), (17,0.01), (18,0.99), (21,0.01), (22,0.99)],
'34_soup_75':
[(1,0.99), (2,0.99), (4,0.018838172746085124), (5,0.01), (6,0.99), (7,0.01), (8,0.01), (10,0.01), (11,0.99), (12,0.99), (13,0.02152196582079323), (14,0.7282803491116691), (16,0.01), (17,0.01), (18,0.99), (20,0.01), (21,0.01), (24,0.01), (25,0.99), (26,0.99)],
'3519':
[(1,0.99), (2,0.24313236697774365), (3,0.99), (4,0.22170382451228476), (5,0.01), (6,0.99), (7,0.01), (8,0.01), (9,0.01), (10,0.01), (11,0.99), (12,0.99), (13,0.01), (14,0.99), (15,0.09429644153223216), (16,0.01), (17,0.01), (18,0.99), (19,0.01), (20,0.01), (21,0.01), (22,0.99), (23,0.99), (24,0.01), (25,0.06199906885670947), (26,0.36584643578588405)],
'3519_soup_50':
[(1,0.99), (3,0.99), (4,0.05667837063701642), (6,0.99), (9,0.01), (11,0.99), (12,0.99), (13,0.01), (14,0.99), (17,0.01), (18,0.99), (21,0.01), (22,0.99)],
'3519_soup_75':
[(1,0.99), (2,0.7811579863533903), (4,0.22170382451228476), (5,0.99), (6,0.7733464064898561), (7,0.943576263078186), (8,0.6773407819905691), (10,0.09972516141427246), (11,0.99), (12,0.21344799540312287), (13,0.01), (14,0.99), (16,0.01), (17,0.01), (18,0.01), (20,0.99), (21,0.012171461220090031), (24,0.016339780218264738), (25,0.99), (26,0.4999966111688567)],
'42':
[(1,0.99), (2,0.99), (3,0.7499061812554475), (4,0.27707849007413665), (5,0.01), (6,0.01), (7,0.49977281524066264), (8,0.99), (9,0.17221793768785243), (10,0.99), (11,0.99), (12,0.43649097442328655), (13,0.01), (14,0.8324471004187546), (15,0.20976756886633208), (16,0.01), (17,0.746049175327422), (18,0.01), (19,0.17737847790937833), (20,0.36878291341130565), (21,0.5874273817862956), (22,0.35791991947712865), (23,0.99), (24,0.99), (25,0.03141823882658079), (26,0.5800248845020607)],
'42_soup_50':
[(1,0.99), (3,0.010130152958615982), (4,0.99), (6,0.99), (9,0.01), (11,0.99), (12,0.989894638404846), (13,0.01), (14,0.99), (17,0.01), (18,0.99), (21,0.01), (22,0.99)],
'42_soup_75':
[(1,0.99), (2,0.99), (4,0.27707849007413665), (5,0.9307982862993378), (6,0.99), (7,0.23785332292257527), (8,0.38656687435934867), (10,0.6832234717598454), (11,0.99), (12,0.4415001698680282), (13,0.7829017787900358), (14,0.7275636800328681), (16,0.01), (17,0.01), (18,0.7349124971554912), (20,0.01), (21,0.01), (24,0.01), (25,0.5874273817862956), (26,0.99)],
'481':
[(1,0.99), (2,0.008001751436242044), (3,0.99), (4,0.03606595997520412), (5,0.33178160039312465), (6,0.21126684493196268), (7,0.4999747487500632), (8,0.05579901844176394), (9,0.7653214815092081), (10,0.99), (11,0.19770954278431951), (12,0.3847017026926254), (13,0.1371889246589284), (14,0.7566776218890333), (15,0.7041099919485491), (16,0.99), (17,0.8677877586367141), (18,0.22268661109769805), (19,0.17849467529707497), (20,0.35120495789343364), (21,0.4660482099727825), (22,0.99), (23,0.6284158186160698), (24,0.3470963999584301), (25,0.8580135606297231), (26,0.4752976285730792)],
'481_soup_50':
[(1,0.99), (3,0.3683848362446426), (4,0.99), (6,0.99), (9,0.019102275274603044), (11,0.99), (12,0.99), (13,0.01), (14,0.7566776218890333), (17,0.01), (18,0.99), (21,0.01), (22,0.99)],
'481_soup_75':
[(1,0.99), (2,0.99), (4,0.03606595997520412), (5,0.99), (6,0.21126684493196268), (7,0.4297904241039558), (8,0.33178160039312465), (10,0.5812946959167776), (11,0.19770954278431951), (12,0.4829223037633394), (13,0.1371889246589284), (14,0.99), (16,0.99), (17,0.8989316540800546), (18,0.5050249987374376), (20,0.35120495789343364), (21,0.17849467529707497), (24,0.3470963999584301), (25,0.4660482099727825), (26,0.05579901844176394)],
'499':
[(1,0.99), (2,0.99), (3,0.17271010931872688), (4,0.9550252683388301), (5,0.99), (6,0.09908869512330998), (7,0.9291804529785139), (8,0.48698976898317814), (9,0.35201645279022564), (10,0.529495556242733), (11,1.0), (12,0.44952568414836525), (13,0.21219559441882296), (14,0.7582900937887228), (15,0.7068735730833172), (16,0.20203656380101287), (17,0.49997474875006315), (18,0.4987777773983262), (19,0.9324026457758108), (20,0.9379237281923711), (21,0.99), (22,0.3835214116349055), (23,0.11953330546139973), (24,0.6833051796855019), (25,0.1776403917490872), (26,0.8171896373015943)],
'499_soup_50':
[(1,0.99), (3,0.13540172909418635), (4,0.99), (6,0.722026342212896), (9,0.01), (11,0.99), (12,0.99), (13,0.01), (14,0.7582900937887228), (17,0.4151785853884916), (18,0.99), (21,0.8535351471425356), (22,0.17271010931872688)],
'499_soup_75':
[(1,0.99), (2,0.39282464497526887), (4,0.7890484710640308), (5,0.17271010931872688), (6,0.7733464064898561), (7,0.9415902636228138), (8,0.6333627218471601), (10,0.01), (11,1.0), (12,0.44952568414836525), (13,0.21219559441882296), (14,0.7582900937887228), (16,0.012846457546581133), (17,0.01), (18,0.01), (20,0.99), (21,0.012879612594477273), (24,0.012568713707048249), (25,0.99), (26,0.5453470231834557)],
'591':
[(1,0.99), (2,0.4532330290421628), (3,0.48252862615483466), (4,0.99), (5,0.6883426104066226), (6,0.99), (7,0.09199977675109006), (8,0.6746477568572683), (9,0.2780214924307508), (10,0.9016058915066514), (11,0.018307553466073934), (12,0.4593596145290272), (13,0.4951982319039603), (14,0.6783835404120788), (15,0.12547838150880675), (16,0.01), (17,0.01), (18,0.7023680679153208), (19,0.6831852665492281), (20,0.01), (21,0.01), (22,0.99), (23,0.11526630133679805), (24,0.01), (25,0.7828002920173303), (26,0.99)],
'591_soup_50':
[(1,0.99), (3,0.99), (4,0.40200384209360096), (6,0.99), (9,0.01), (11,0.99), (12,0.99), (13,0.01), (14,0.6907738853926814), (17,0.01), (18,0.99), (21,0.01), (22,0.99)],
'591_soup_75':
[(1,0.99), (2,0.2780214924307508), (4,0.99), (5,0.24559762781994654), (6,0.99), (7,0.01), (8,0.1337973423094002), (10,0.27077089014280015), (11,0.018307553466073934), (12,0.99), (13,0.1775353441513018), (14,0.99), (16,0.01), (17,0.01), (18,0.6646163809289676), (20,0.01), (21,0.01), (24,0.01), (25,0.12169560465851914), (26,0.99)],
'6012':
[(1,0.99), (2,0.5478342986830887), (3,0.4781408077217032), (4,0.99), (5,0.01), (6,0.99), (7,0.01), (8,0.01), (9,0.01), (10,0.01), (11,0.3638630197297024), (12,0.99), (13,0.01), (14,0.99), (15,0.1893791092311754), (16,0.01), (17,0.01), (18,0.99), (19,0.01), (20,0.01), (21,0.01), (22,0.10634935068738993), (23,0.28693452450641665), (24,0.01), (25,0.99), (26,0.99)],
'6012_soup_50':
[(1,0.99), (3,0.99), (4,0.14724131610415359), (6,0.99), (9,0.01), (11,0.99), (12,0.99), (13,0.01), (14,0.99), (17,0.01), (18,0.99), (21,0.01), (22,0.99)],
'6012_soup_75':
[(1,0.99), (2,0.19730098508437166), (4,0.99), (5,0.01), (6,0.99), (7,0.01), (8,0.01), (10,0.01), (11,0.3466827886649182), (12,0.99), (13,0.01), (14,0.9749873427701053), (16,0.01), (17,0.01), (18,0.99), (20,0.01), (21,0.01), (24,0.01), (25,0.99), (26,0.99)],
'68':
[(1,0.99), (2,0.5281857114042451), (3,0.17356763549842225), (4,0.99), (5,0.99), (6,0.09033585265365318), (7,0.01), (8,0.7739812826850769), (9,0.19439300045398433), (10,0.7695553612824789), (11,0.5859387097174721), (12,1.0), (13,0.657890637688276), (14,0.7248762417678801), (15,0.8718282719421057), (16,0.99), (17,0.8647980239636625), (18,0.5050249987374373), (19,0.2541985221444316), (20,0.7242516544150118), (21,0.4909393094647877), (22,0.4518906337536538), (23,0.7758207611804138), (24,0.7718676770847227), (25,0.832040206829189), (26,0.3435381834196539)],
'68_soup_50':
[(1,0.99), (3,0.99), (4,0.41764209803369623), (6,0.99), (9,0.01), (11,0.8010234839292698), (12,0.99), (13,0.01), (14,0.7248762417678801), (17,0.6118611102438946), (18,0.99), (21,0.6766545071486478), (22,0.17356763549842225)],
'68_soup_75':
[(1,0.99), (2,0.19439300045398433), (4,0.99), (5,0.17356763549842225), (6,0.09033585265365318), (7,0.01), (8,0.8882920445095155), (10,0.99), (11,0.5859387097174721), (12,1.0), (13,0.99), (14,0.7248762417678801), (16,0.99), (17,0.8647980239636625), (18,0.5050249987374373), (20,0.7242516544150118), (21,0.2541985221444316), (24,0.7718676770847227), (25,0.4909393094647877), (26,0.7739812826850769)],
'991':
[(1,0.99), (2,0.45999216068977866), (3,0.99), (4,0.8368042177698709), (5,0.3901453524329872), (6,0.16529137708695774), (7,0.5743026555641344), (8,0.034442368967490866), (9,0.3156874016885185), (10,0.99), (11,0.13016201116094972), (12,0.011003588929841324), (13,0.16201319327434915), (14,0.7142160704801332), (15,0.9646690618027512), (16,0.6808353093150417), (17,0.49997474875006315), (18,0.9497274092941764), (19,0.9922513533492915), (20,0.567610961443864), (21,0.7415366136487759), (22,0.5246411525920076), (23,0.99), (24,0.8269318274091104), (25,0.10784069381395212), (26,0.13880756371642133)],
'991_soup_50':
[(1,0.99), (3,0.99), (4,0.2830352528782333), (6,0.99), (9,0.01), (11,0.99), (12,0.99), (13,0.03614423703835986), (14,0.99), (17,0.01), (18,0.99), (21,0.01), (22,0.99)],
'991_soup_75':
[(1,0.99), (2,0.3156874016885185), (4,0.99), (5,0.7207581079151253), (6,0.7572593377261274), (7,0.8860144581382723), (8,0.3901453524329872), (10,0.6540715085600388), (11,0.13598072964925248), (12,0.011003588929841324), (13,0.16201319327434915), (14,0.99), (16,0.6956550982375209), (17,0.01), (18,0.31982208547657365), (20,0.567610961443864), (21,1.0), (24,0.8269318274091104), (25,0.99), (26,0.034442368967490866)]
}
# for ZAATAR
base = 1
chain = None
nc = 6
nl = 2
bound = 20
