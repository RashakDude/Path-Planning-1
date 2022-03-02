import matplotlib.pyplot as plt
import matplotlib.patches as patches

from matplotlib.font_manager import FontProperties

fontP = FontProperties()
fontP.set_size('x-small')

x_range = (0,50)
y_range = (0,30)

obs_boundary = [
    [0, 0, 1, 30],
    [0, 30, 50, 1],
    [1, 0, 50, 1],
    [50, 1, 1, 30]
]

obs_rectangle = [
    [20, 0, 1, 15, 0],
    [10, 15, 11, 1, 0],
    [30, 15, 1, 15, 0],
    [40, 0, 1, 16, 0]
]

fig, ax = plt.subplots()

for (ox, oy, w, h) in obs_boundary:
    ax.add_patch(
        patches.Rectangle(
            (ox, oy), w, h,
            edgecolor='black',
            facecolor='black',
            fill=True
        )
    )

for (ox, oy, w, h, a) in obs_rectangle:
    ax.add_patch(
        patches.Rectangle(
            (ox, oy), w, h,
            angle = a,
            edgecolor='black',
            facecolor='black',
            fill=True
        )
    )

rrt_path = [(45, 25), (44.34116007291925, 24.858314572286428), (44.44023921902489, 24.36822955638921), (44.10865764298231, 23.993992120489064), (43.77707606693973, 23.61975468458892), (43.44549449089714, 23.245517248688774), (43.11391291485456, 22.87127981278863), (42.78233133881197, 22.497042376888484), (42.36657584861527, 22.774796535041517), (41.87978404245286, 22.88896193020635), (41.46566104628284, 22.608779589500937), (41.05153805011282, 22.328597248795525), (40.575114123035924, 22.48032147793718), (40.14061964395024, 22.232905739464346), (39.70612516486455, 21.98549000099151), (39.27163068577887, 21.738074262518676), (38.83713620669318, 21.49065852404584), (38.402641727607495, 21.243242785573006), (37.96814724852181, 20.99582704710017), (37.593714913158365, 20.664465573427876), (37.2249868366723, 20.32676806735049), (36.79644048676817, 20.06918696170832), (36.36789413686404, 19.811605856066148), (35.93934778695991, 19.554024750423977), (35.510801437055775, 19.296443644781807), (35.082255087151644, 19.038862539139636), (34.85550805292969, 18.59323289193071), (34.38419045227146, 18.426320581690366), (34.24866454206527, 17.94503820338966), (33.85434085014027, 17.790441863403284), (33.59648091865666, 17.362063227456918), (33.41113454308239, 16.89768544906794), (33.26736170831905, 16.41880198518125), (32.951566271418116, 16.03115105711252), (32.615284553634055, 15.661131319417084), (32.58536881796306, 15.16202707303236), (32.144927788586955, 14.925359162993592), (31.962853331404865, 14.459688794554879), (31.807683321260864, 13.984375983921806), (31.648394046040018, 13.762036400383245), (31.260056850158367, 14.076987543093948), (30.81914560454962, 13.841196802190609), (30.33568133173082, 13.968720513349705), (29.84891308340027, 14.08298631058233), (29.48742911357474, 14.42842710081877), (29.275798413182947, 14.881430905054096), (28.994375973398817, 15.294712177780006), (28.606667139772657, 15.610436520091845), (28.21657758793174, 15.923214622817328), (28.020014012367444, 16.38295668176058), (27.687166469198445, 16.756068612696005), (27.684515038485028, 17.256061582561752), (27.9915125115748, 17.650716560379713), (28.31383690743777, 18.032955992976053), (28.689213124297638, 18.363247827292273), (28.40780336045818, 18.776537731373924), (27.984977200699653, 19.043404811816337), (27.552394669923736, 19.29414841406274), (27.193185527715706, 19.64195409566408), (26.869646566076597, 20.023166031864257), (26.55081050658432, 20.408319984417567), (26.324459626171844, 20.854150982595684), (26.16737659101268, 21.32883500388267), (26.087010377723185, 21.82233401275858), (25.94842842318499, 22.302745338474757), (25.688521331451252, 22.729885015473407), (25.892466221177358, 23.18640060332842), (25.947985823939405, 23.68330861665598), (25.50678819836908, 23.9185630644165), (25.095398266463864, 24.202743155075613), (24.745022904198468, 24.55944626063736), (24.24514113216527, 24.548573634967784), (23.74525936013207, 24.53770100929821), (23.262960947767386, 24.669565490605738), (22.97610533473868, 25.079094314101624), (22.546319261686694, 24.823587109877256), (22.075411420166642, 24.655522227183322), (21.593529307806676, 24.522144456218673), (21.09363347372939, 24.511938816984618), (20.597790241856917, 24.44759995309769), (20.10251221935786, 24.37904573784128), (19.679789819281623, 24.112014330561564), (19.185313779147233, 24.03789654772228), (18.689193792697548, 24.10006534250844), (18.189486014618105, 24.08297334066826), (18.07189788060553, 23.596996972169297), (17.572972163472333, 23.62975561657236), (17.07583945269614, 23.576285364316426), (16.577933660564906, 23.53057079156148), (16.093984408385314, 23.656241477542004), (15.664306500040269, 23.400552418174524), (15.562656929928997, 22.91099408161371), (15.422213392137246, 22.4311236692183), (15.398228774772747, 21.93169926239593), (14.901038881434145, 21.98463516667601), (14.40669031605689, 21.90967186959371), (14.015823120156575, 21.597866104462554), (13.551511389994976, 21.412354333314894), (13.075474343325922, 21.25942058884166), (12.579095523545023, 21.19935339918772), (12.5382135528544, 20.701027537454205), (12.187818413756744, 20.344343858970404), (12.098985887869123, 19.852298350562467), (11.681995092014978, 19.57640221761942), (11.24032382734547, 19.342038197417434), (11.326193420960916, 18.849466971205104), (10.977259439227387, 18.49135375392377), (10.491519409178045, 18.37279312298895), (10.154551116171408, 18.003398524343822), (9.81824401486117, 17.633401857320585), (9.738947256841062, 17.13972987698597), (9.4487054830371, 16.732593888968292), (9.388347766548435, 16.23625031233989), (9.239797088890374, 15.758827338272523), (9.031184858896113, 15.304425602473877), (8.867727930597376, 14.831898531724336), (8.388224203147145, 14.973588952576751), (8.301269571161448, 14.481208112193789), (8.020449169664108, 14.067517524794374), (8.054555259591462, 13.568682106414858), (8.124261667113366, 13.073564931646713), (7.972042437243644, 12.597298928180301), (8.01991311351695, 12.09959580547246), (8.12589482718196, 11.610957005980822), (8.252458962494424, 11.127240643168266), (8.402638659777931, 10.650327591843567), (8.648364529484981, 10.21487518691656), (8.64232748534538, 9.714911634146905), (8.867577971155093, 9.268523665399439), (9.158248968373824, 8.861694006480786), (9.083051725986586, 8.367380973335436), (8.6440333271659, 8.128084409430056), (8.168485757941003, 7.973635358269838), (7.704421655790687, 7.787505003154342), (7.325728215332076, 7.461021805801674), (7.1407832163501554, 6.9964840276268765), (7.030215311256369, 6.508862516244153), (6.618509341747944, 6.225140478553867), (6.124791808887067, 6.3041531215027575), (5.6512806227329255, 6.143569322236149), (5.273902814045665, 5.815566289459924), (5.378556958426797, 5.3266414383183065), (5, 5)]
rrt_star_path = [[45, 25], [45.0, 25.0], [45.0, 25.0], [45.0, 25.0], [43.98393254145679, 24.349282086878056], [43.28399668714935, 24.033241351179502], [42.6238346360189, 23.520675302350007], [42.100803275654215, 22.782696043454457], [41.57879723432688, 21.986030697156796], [41.031470727385994, 21.723604700854168], [40.041032612229856, 21.303158055680132], [39.532869103123694, 20.942578492922557], [39.30315158093605, 19.98511759102449], [39.031026469783484, 19.24545707342018], [38.394131738288635, 18.768529172887753], [37.563694642039074, 18.165709016070053], [37.392798727929936, 17.789519692649524], [36.57818056056726, 17.43819587187761], [36.23132572877337, 16.92903983405209], [35.81182057286093, 16.281034382620852], [35.310121395421845, 15.924518553179826], [34.52176139370379, 15.601754049319359], [34.09361694878528, 15.316762935933019], [33.4510739931381, 14.499072590185891], [32.93009866975919, 13.932378545240816], [32.47541226894678, 13.795284465072966], [31.99349506316178, 13.456651875209298], [31.242421465340282, 13.366409729104266], [30.274683692269342, 13.37181541897576], [29.336478301058698, 13.349812787047265], [29.102925513926706, 14.692223618821844], [27.49277256750505, 15.492656904031735], [26.67441010143376, 15.930379718637248], [26.2366256632611, 16.665493435714218], [25.885771798483344, 17.426930886099335], [25.153088988963606, 18.11290476866289], [24.197154324545433, 18.328054390221524], [23.48874744214533, 19.046549607529716], [22.41852090135376, 19.36265954009213], [22.030720427903518, 19.367107855582503], [21.042114137946548, 19.096505371585152], [20.76176461973475, 18.899850261033308], [19.92269571249295, 18.626971135437522], [18.520962079040768, 18.45020222569999], [18.001760721187175, 17.837904508696425], [17.027410180264187, 17.73918571038006], [16.05979855212702, 17.635840265656615], [15.308219706347263, 17.754440778821802], [14.075514953508836, 17.694690095805466], [12.340812568048223, 17.2732107237876], [11.386462640640639, 17.181107958092582], [10.173380115083479, 16.875785494501052], [9.500819554949857, 17.206066530868164], [9.38409552077066, 16.268052145598162], [8.349850479528843, 15.84720897030139], [7.434277826617216, 15.57043972123779], [7.237228659973397, 14.027688000672764], [6.851553797872669, 12.350758095747503], [6.193268007265473, 11.297928469853016], [5, 5]]
bi_rrt_path = [(45, 25), (44.28336655920307, 24.644420878661936), (43.566733118406134, 24.288841757323873), (42.8500996776092, 23.93326263598581), (42.13346623681227, 23.577683514647745), (41.416832796015335, 23.22210439330968), (40.7001993552184, 22.866525271971618), (39.98356591442147, 22.510946150633554), (39.266932473624536, 22.15536702929549), (38.5502990328276, 21.799787907957427), (37.83366559203067, 21.444208786619363), (37.11703215123374, 21.0886296652813), (36.400398710436804, 20.733050543943236), (35.68376526963987, 20.377471422605172), (34.96713182884294, 20.02189230126711), (34.250498388046005, 19.666313179929045), (33.53386494724907, 19.31073405859098), (32.81723150645214, 18.955154937252917), (32.166726386398814, 18.489490799934607), (32.38934822802241, 17.721090178102404), (32.48203844158235, 16.926477993253584), (31.723782152732955, 16.671434074642793), (31.933322749439075, 15.899363651473998), (32.011591171290874, 15.103201573665196), (31.574374336770116, 14.4332452768729), (30.908827257481136, 13.989345417388906), (30.243280178192155, 13.545445557904912), (29.577733098903174, 13.10154569842092), (28.912186019614193, 12.657645838936928), (28.39209681297124, 13.26551689198478), (27.835264963299284, 13.839919443503232), (27.339567637188992, 14.467839948732284), (26.893392557356755, 15.131863892680615), (26.36266595191406, 15.318135058905577), (26.36266595191406, 15.318135058905577), (26.505061804739015, 15.68242432872169), (26.796311436601723, 16.427524088445068), (27.087561068464435, 17.172623848168445), (27.378810700327143, 17.917723607891823), (27.670060332189852, 18.6628233676152), (27.961309964052564, 19.407923127338577), (28.252559595915272, 20.153022887061955), (28.54380922777798, 20.898122646785332), (28.83505885964069, 21.64322240650871), (29.126308491503398, 22.388322166232086), (28.525188416220182, 22.916199666312835), (28.417796244995383, 23.70895872274778), (27.617932631428836, 23.694187138801976), (26.81806901786229, 23.679415554856174), (26.018205404295742, 23.66464397091037), (25.218341790729195, 23.649872386964567), (24.418478177162648, 23.635100803018762), (23.6186145635961, 23.62032921907296), (22.818750950029553, 23.605557635127155), (22.018887336463006, 23.590786051181354), (21.21902372289646, 23.57601446723555), (20.419160109329912, 23.561242883289747), (19.619296495763365, 23.546471299343942), (18.819432882196818, 23.53169971539814), (18.01956926863027, 23.516928131452335), (17.219705655063724, 23.502156547506534), (16.419842041497176, 23.48738496356073), (15.619978427930631, 23.472613379614923), (14.89278254080256, 23.806059239904144), (14.098921927688767, 23.707138428410342), (13.321144841138366, 23.519887784520474), (13.22222746062433, 23.004708172461655), (12.896604591276274, 22.273975836405874), (12.193500770987015, 21.892341170927686), (11.394013514976702, 21.863703303040893), (10.637312872496302, 21.604080234594058), (10.699041850462086, 20.8064653317247), (10.423570160137427, 20.055389205203774), (9.93874745007958, 19.419034791522087), (10.01985659294722, 18.62315709555161), (9.820046682427057, 17.848511370295267), (9.491611409320642, 17.119038772194752), (9.483854994563512, 16.31907637430963), (9.466090870578116, 15.519273626190426), (9.420195304568384, 14.72059121307452), (9.486466011071762, 13.92334081736465), (10.129106910679008, 13.446882346821843), (10.10577495986876, 12.647222656658966), (9.832433516017167, 11.895368644850073), (9.071879202059597, 11.64726153991245), (8.938625384791893, 10.858437465619843), (9.592713064067263, 10.397819068440398), (9.525858945848018, 9.600617383245787), (10.214724961601704, 9.193845195971823), (10.414823320617474, 8.419273929580411), (10.127093168102292, 7.672808016538435), (10.324694625430645, 6.897596004207801), (10.215637381775748, 6.105064290264191), (9.421346482572208, 6.200468522048901), (8.646531464414894, 6.399620945177222), (7.893869978524488, 6.128510842714688), (7.106390162632458, 5.987530207297425), (6.309330166707927, 5.919007489190312), (5.645226166573557, 5.472951576769538), (5, 5)]
fmt_path = [(45, 25), (43.632228997183375, 23.605653658460405), (41.81776774815491, 21.681717927613164), (40.29857065825683, 20.536745564237368), (38.61476180062054, 19.23423422098155), (37.044308539671775, 18.05889467335328), (35.78630411086014, 17.420390428504344), (33.512155135692105, 15.118039822756204), (32.5130767082812, 14.519087395821943), (29.54888728175347, 13.41663272354512), (27.36963090187704, 14.233491816926474), (24.606173906747483, 15.430834137816968), (22.06491180517578, 16.814800897778397), (20.961550506257343, 17.16940506829677), (18.94377605552568, 17.972772682719945), (16.03743899150262, 18.45804672729771), (14.251391040234052, 18.7427983495212), (12.224172782821105, 18.491933512498996), (9.411045969643247, 16.783148857040366), (8.165242450538132, 13.728786414158924), (7.334165713925523, 10.806759525608733), (6.401408691063015, 8.605834419352718), (5.703322595103285, 7.412721008211125), (5, 5)]

x1 = [0] * len(rrt_path)
y1 = [0] * len(rrt_path)
for i in range(len(rrt_path)):
    x1[i] = rrt_path[i][0]
    y1[i] = rrt_path[i][1]

x2 = [0] * len(rrt_star_path)
y2 = [0] * len(rrt_star_path)
for i in range(len(rrt_star_path)):
    x2[i] = rrt_star_path[i][0]
    y2[i] = rrt_star_path[i][1]

x3 = [0] * len(bi_rrt_path)
y3 = [0] * len(bi_rrt_path)
for i in range(len(bi_rrt_path)):
    x3[i] = bi_rrt_path[i][0]
    y3[i] = bi_rrt_path[i][1]

x4 = [0] * len(fmt_path)
y4 = [0] * len(fmt_path)
for i in range(len(fmt_path)):
    x4[i] = fmt_path[i][0]
    y4[i] = fmt_path[i][1]

plt.plot(x1,y1,'-')
plt.plot(x2,y2,'--')
plt.plot(x3,y3,'-.')
plt.plot(x4,y4,':')

plt.plot(5,5, "or")
plt.plot(45,25, "og")
plt.legend(["RRT", "RRT*", "Bi-RRT", "FMT"], loc='upper left', prop=fontP)
plt.xlabel("Normalised X")
plt.ylabel("Normalised Y")
plt.show()
