import numpy as np

import matplotlib.pyplot as plt
from matplotlib import rcParams

import math


fig = plt.figure()
ax = fig.add_subplot(111)

n_groups = 20

# LG_means = (112427,112463,115484,249047,292129,291911,292036,305604,1538640,1517094,1543786,1500005,0)
# LG_std = (34,52,8416,198,982,1315,1296,5930,58042,64173,47997,14164,0)

# NEXUS_means = (32895,34104,119369,136401,129656,137275,135536,134109,136562,1892541,1899921,1909015,1893890)
# NEXUS_std = (2611,2980,2638,9133,7001,10101,7504,7543,8082,487175,516802,543551,515123)

# S6_means = (56925,62425,136266,139787,147391,168195,178416,535820,2787158,2794804,2781716,2908874,2849658)
# S6_std = (153,852,4725,3706,3596,3959,26734,24083,15511,12325,16802,26809,16441)


sec1=[0.09067039487144501, 0.06455386578751465, 0.05474647350362183, 0.050819672131147464, 0.05024141980947405, 0.04897159647404503, 0.044220756681707774, 0.04312805872756942, 0.042549167927382725, 0.04130031459224015, 0.03711379050489827, 0.0362116991643453, 0.03422982885085579, 0.03415243648479793, 0.033993115318416534, 0.033817511354948815, 0.0333464103570027, 0.03334262097148699, 0.03314407381121376, 0.03313373253493024]
fig, ax = plt.subplots(figsize=(20,8))

index = np.arange(n_groups)
bar_width = 0.8

opacity = 1
error_config = {'ecolor':'black',    # error-bars colour
                'linewidth':2}

rects1 = plt.bar(index+ 1.5*bar_width, sec1, bar_width,
                 alpha=opacity,
                 color='grey',
                 edgecolor='black',
                 hatch = '//')
                 #hatch = '//',
                 #yerr=existstd,
                 #error_kw=error_config)



FONTSIZE = 36

# ax.set_yscale('log')
# ax.set_ylim(0,1e9)
ax.set_ylabel('Absolute Ratio Change',fontsize=FONTSIZE)
ax.set_xlabel('Round',fontsize=FONTSIZE)
ax.set_xlim(-0.2*bar_width,len(index)+1.5*bar_width)
xTickMarks = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
ax.set_xticks(index + 2*bar_width)
xtickNames = ax.set_xticklabels(xTickMarks, color="black", ha='center', va='top', y=-0.01, rotation='horizontal')
# fig.autofmt_xdate()
#plt.setp(xtickNames, rotation=15)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')



# ax.legend((rects5[0],rects1[0],rects2[0],rects3[0],rects4[0]), ('baseline',r'$\epsilon$=0.05',r'$\epsilon$=0.5',r'$\epsilon$=5',r'$\epsilon$=50'), loc = "upper right",fontsize=24)

#rcParams.update({'font.size': FONTSIZE})
plt.tick_params(labelsize=FONTSIZE)

#ax.legend((rects1[0], rects2[0], rects3[0]), ('LG (C=1M W=8)', 'Nexus 6 (C=2M W=8)', 'S6 (C=2M W=16)'), loc = 2)

# rects = ax.patches
# labels = ('1773021', '294848', '152746')

# count = -1
# yheight = [-20,-20,-20]
# for rect in rects:
#   height = rect.get_height()
#   count = count + 1
#   ax.text(rect.get_x() + rect.get_width()/2, height + 50000, label, fontsize=15, ha='center', va='bottom')
#   xlabel = ax.text(rect.get_x()+rect.get_width(), -50000, xTickMarks[count], fontsize=16, ha='center', va='top')
    #plt.setp(xlabel, rotation=30)

# rcParams.update({'font.size': 28})
plt.tight_layout()
# rcParams['ps.useafm'] = True
# rcParams['pdf.use14corefonts'] = True
# rcParams['text.usetex']=True
# fig.set_tight_layout(True)
#plt.style.use('classic')
#plt.rcParams['hatch.color'] = 'b'
# plt.show()
plt.savefig("abs_change.eps", format='eps', dpi=600)
# plt.savefig("accuracy.pdf")
