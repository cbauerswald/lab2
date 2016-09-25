import matplotlib.pyplot as plt

distances_middle = [36.238530850357733, 35.781240485063506, 36.026305470959869, 36.360155901702853, 36.491900359549959, 36.879671622642491, 36.34524789060805, 36.313504237113534, 36.519512272630095, 37.369298177263602, 46.219114831168156, 74.614720361379284, 81.287206357497269, 83.575895149317148, 79.903803386899654, 84.611228671182516, 85.794081592461225, 85.7687165073404, 88.911207483827184, 85.823565786409546, 77.385634871903562, 40.903243349522427, 37.204489146669459, 37.027693351788798, 37.888272195703564, 44.933903677981561, 62.269946013676417, 101.36717780282575, 102.33659404448525, 103.34262061206221, 105.06703128885397, 100.83259494163477, 70.474435883024341, 49.713876923526186, 44.99786051770522, 42.990445421606864, 43.079762487443702, 43.57196971645908, 47.961425410138759, 72.947986560596036, 120.32797574417131, 126.59445756965195, 128.0772462150403, 135.20756376921824, 155.50149935383286, 187.39919165544447]
distances_right = [35.18063976029373, 35.05227173011798, 35.907364707708496, 36.378042193780686, 36.979801542903488, 40.797878272150768, 38.231269710807283, 36.848137875675718, 36.563425673137999, 36.36775772871863, 36.267956827519185, 36.409346331696497, 36.424156063895339, 36.392208773877599, 36.427658973560028, 36.59208244103354, 36.624900540440251, 36.549834024764834, 36.64097681512294, 36.749679584661465, 36.777660217261882, 36.721062897326419, 36.858888541346289, 37.007652848029238, 37.078141670975356, 37.090617096731876, 37.248939060266252, 37.471011424760206, 37.707176370522291, 37.78615950818994, 37.999943927268134, 38.663665780459098, 38.927608967564368, 39.030062737963362, 39.553317438415547, 40.577812575200539, 40.940849815849106, 41.536435116007738, 46.604522987334832, 61.270939437177901, 117.65269203246712, 119.80045920293561, 123.98621698188273, 130.98203757176131, 140.30568957919689, 165.68675213500507]
distances_left = [35.758144193665487, 36.312360593062408, 36.34496347715708, 36.102614117403789, 36.460600197389454, 36.395346577735722, 36.226047629681261, 36.166090797294771, 36.242218829516105, 36.189609855699132, 36.287742707203165, 36.133108127168271, 36.321024673904049, 36.340485457994589, 36.361630787840454, 36.332662082029799, 36.470068234617429, 36.549834024764834, 36.559527550056146, 36.543934601218098, 36.719882292770194, 36.889546936991223, 36.982821371805244, 45.265494043978549, 91.466082097012702, 97.511003075014202, 95.134220976507265, 60.218265305221735, 38.320501162088192, 37.748277181565527, 37.875581743097598, 37.77906071824458, 38.807295670375595, 39.030062737963362, 39.482654429806587, 39.770854722135141, 40.759836560475549, 43.197116335630596, 50.031485153765118, 68.470695231545022, 121.0060091676134, 126.59445756965195, 128.0772462150403, 128.91593790603696, 135.31399902160135, 163.23236450239227]

plt.plot(distances_middle, 'bo')
plt.show()