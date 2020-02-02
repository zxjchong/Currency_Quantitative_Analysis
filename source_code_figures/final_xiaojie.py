import sys
import math
import string
import csv
import xlrd
import numbers
import random
import numpy as np
import time
from sys import argv
import os 
import matplotlib.pyplot as plt
from matplotlib import rcParams
from scipy import interpolate
from mpl_toolkits.mplot3d import Axes3D
# def partition(rate_list):
from sklearn.preprocessing import StandardScaler
from sklearn import decomposition
from sklearn.decomposition import PCA

date_list = []
rate_list = []
abs_change = []
currency_rate = {}
with open('dollar-yen-exchange-rate-historical-chart.csv', 'rt') as f:
     reader = csv.reader(f)
     for row in reader:
        if len(row)>1:
            if row[0]!='':
                if row[0][0]!='d':
                    if row[0][4] == '-':
                        currency_rate[row[0]] = row[1]
                        date_list.append(row[0])
                        rate_list.append(row[1])
        # print row

date_index = 1
date_index_list = []
date_index_list.append(0)
for i in range(1,len(rate_list)):
    abs_change.append(abs(float(rate_list[i])/float(rate_list[i-1])-1))
    if abs(float(rate_list[i])/float(rate_list[i-1])-1) >0.025:
        # print "\Xhline{0.5pt}"
        # print "\\textbf{"+date_list[i]+"} & "+str(float(rate_list[i])/float(rate_list[i-1])-1)+" & "+str(i-date_index)+" \\\\"
        date_index = i
        date_index_list.append(i)
        # print str(i) + "  " +date_list[i]+" "+ str(float(rate_list[i])/float(rate_list[i-1])-1)
abs_change.sort()

top_20 = abs_change[-20:] 
top_20.reverse()
print (top_20)
# print len(top_20)

# print date_index_list
# print date_list[date_index_list[-3]]


# here we use -4:-3
# y = []
# for i in range(date_index_list[-4],date_index_list[-3]):
#     y.append(float(rate_list[i]))
# x=list(range(1,len(y)+1))

# plt.figure()
# ax = plt.subplot(111)
# ax.plot(x,y,label = "Raw Data")
# plt.xlabel("Date(day)")
# plt.ylabel("Exchange Rate(Yen per USD)")
# # plt.show()
# plt.savefig("Rawdata.eps", format='eps', dpi=600)


# plt.figure()
# ax = plt.subplot(111)
# ax.plot(x,y,label = "Raw Data")
# # trend5 = np.polyfit(x,y,1)
# # trendpoly5 = np.poly1d(trend5)
# # ax.plot(x,trendpoly5(x),label = "N = 1")
# # trend5 = np.polyfit(x,y,2)
# # trendpoly5 = np.poly1d(trend5)
# # ax.plot(x,trendpoly5(x),label = "N = 2")
# # trend5 = np.polyfit(x,y,3)
# # trendpoly5 = np.poly1d(trend5)
# # ax.plot(x,trendpoly5(x),label = "N = 3")
# trend5 = np.polyfit(x,y,4)
# trendpoly5 = np.poly1d(trend5)
# ax.plot(x,trendpoly5(x),label = "N = 4")

# trend5 = np.polyfit(x,y,5)
# trendpoly5 = np.poly1d(trend5)
# ax.plot(x,trendpoly5(x),label = "N = 5")
# trend6 = np.polyfit(x,y,6)
# trendpoly6 = np.poly1d(trend6)
# ax.plot(x,trendpoly6(x),label = "N = 6")
# ax.legend()
# plt.xlabel("Date(day)")
# plt.ylabel("Exchange Rate(Yen per USD)")
# # plt.show()
# plt.savefig("polydata.eps", format='eps', dpi=600)
# print trendpoly6

# tck = interpolate.splrep(x, y)

# xx = np.linspace(x[0], x[-1], 10*(x[-1]-x[0]))
# yy = interpolate.splev(xx, tck)
# d1 = np.diff(yy) / np.diff(xx)
# d2 = np.diff(d1) / np.diff(xx[1:])

# plt.figure()
# ax = plt.subplot(111)
# ax.plot(x,y,'ko:',label = "Raw Data")
# trend6 = np.polyfit(x,y,6)
# trendpoly6 = np.poly1d(trend6)
# ax.plot(x,trendpoly6(x),label = "Polyfit with N = 6",lw=1.5)
# ax.plot(x,interpolate.splev(x, tck),label = "SPLINE",lw=1.5)
# ax.legend()
# plt.xlabel("Date(day)")
# plt.ylabel("Exchange Rate(Yen per USD)")
# # plt.show()
# plt.savefig("Spline.eps", format='eps', dpi=600)
# print trendpoly6


#This part is for spline after this part we will go to pca part.

# plt.figure()
# ax = plt.subplot(221)
# ax.plot(x,y,'ko:',label = "Raw Data",lw=0.5)
# ax.legend()
# plt.title("Raw data")
# ax = plt.subplot(222)
# ax.plot(xx,interpolate.splev(xx, tck),label = "SPLINE",lw=1)
# ax.legend()
# plt.title("Spline output")
# ax = plt.subplot(223)
# ax.plot(xx[1:],d1,label = "First derivative",lw=1)
# ax.legend()
# plt.title("Spline first derivative")
# ax = plt.subplot(224)
# ax.plot(xx[1:-1],d2,label = "Second derivative",lw=1)
# ax.legend()
# plt.title("Spline second derivative")
# # plt.show()

# # plt.gca().xaxis.set_major_locator(plt.NullLocator())
# # plt.gca().yaxis.set_major_locator(plt.NullLocator())
# # plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, hspace = 0, wspace = 0)
# plt.savefig("Spline12.eps", format='eps', dpi=600,bbox_inches='tight')
# plt.savefig("Spline12.eps", format='eps', dpi=600)

# begin to pca part
# final_x = xx[1:-1]
# final_y = interpolate.splev(xx[1:-1], tck)
# matrix = []
# for i in range(len(final_x)):
#     one_date = []
#     one_date.append(final_y[i])
#     one_date.append(d1[i])
#     one_date.append(d2[i])
#     matrix.append(one_date)
# print (matrix)
# print (len(matrix))
# X_std = StandardScaler().fit_transform(matrix)


# pca = decomposition.PCA()
# pca
# PCA(copy=True, iterated_power='auto', n_components=None, random_state=None, svd_solver='auto', tol=0.0, whiten=False)
# pca_output = pca.fit_transform(X_std)
# print (pca.explained_variance_ratio_)

# change parameter after this 

# max_ratio=0
# print ("hello")
# # d_x=list(range(3,21))
# # d_y=[300,275,250,225,200,175,150,125,100,75,50,20,10,9,8,7,6,5,3,2,1]
# # d_z=[]
# window_list = [300,275,250,225,200,175,150,125,100,75,50,20,10,9,8,7,6,5,3,2,1]
# # list(range(1,301))
# # window_list[:] = window_list[::-1]
# # print (window_list)
# d_x =[]
# d_y=[]
# d_z=[]

# for start_date in range(3,41):
#     for time_window in window_list:
#         tmp_z = []
#         d_x.append(start_date)
#         d_y.append(time_window)
#         print ("#########")
#         print ("time window: " + str(time_window))
#         print ("start_date: " + date_list[date_index_list[-3]-1-start_date])
#         print ("Period_length: " + str(start_date))
#         y = []
#         for i in range(date_index_list[-3]-1-start_date,date_index_list[-3]):
#             y.append(float(rate_list[i]))
#         x=list(range(1,len(y)+1))

#         tck = interpolate.splrep(x, y)

#         xx = np.linspace(x[0], x[-1], time_window*(x[-1]-x[0]))
#         yy = interpolate.splev(xx, tck)
#         d1 = np.diff(yy) / np.diff(xx)
#         d2 = np.diff(d1) / np.diff(xx[1:])

#         final_x = xx[1:-1]
#         final_y = interpolate.splev(xx[1:-1], tck)
#         matrix = []
#         for i in range(len(final_x)):
#             one_date = []
#             one_date.append(final_y[i])
#             one_date.append(d1[i])
#             one_date.append(d2[i])
#             matrix.append(one_date)
#         # print (matrix)
#         # print (len(matrix))
#         X_std = StandardScaler().fit_transform(matrix)


#         pca = decomposition.PCA()
#         PCA(copy=True, iterated_power='auto', n_components=None, random_state=None, svd_solver='auto', tol=0.0, whiten=False)
#         pca_output = pca.fit_transform(X_std)
#         print (pca.explained_variance_ratio_)
#         if pca.explained_variance_ratio_[0]>max_ratio:
#             max_ratio = pca.explained_variance_ratio_[0]
#         tmp_z.append(pca.explained_variance_ratio_[0])
#         d_z.append(pca.explained_variance_ratio_[0]) 

# # d_z = np.array(d_z)

# fig = plt.figure()
# ax = Axes3D(fig)
# ax.scatter(d_x, d_y, d_z)
# # plt.show()
# ax.set_zlabel('Fraction of variance') 
# ax.set_ylabel('Time window size')
# ax.set_xlabel('Start Date')
# plt.savefig("pca1.eps", format='eps', dpi=600)
# print (max_ratio)

#begin analysis the terrible week
# print ("start_date: " + date_list[date_index_list[-42]])
# print ("start_date: " + date_list[date_index_list[-41]])
# print ("start_date: " + date_list[date_index_list[-42]+55])
# print ("start_date: " + date_list[date_index_list[-42]+54])

# max_ratio=0
# print ("hello")
# # d_x=list(range(3,21))
# # d_y=[300,275,250,225,200,175,150,125,100,75,50,20,10,9,8,7,6,5,3,2,1]
# # d_z=[]
# # window_list = [300,275,250,225,200,175,150,125,100,75,50,20,10]
# window_list = [300,275,250,225,200,175,150,125,100,75,50,20,10,9,8]
# # list(range(1,301))
# # window_list[:] = window_list[::-1]
# # print (window_list)
# d_x =[]
# d_y=[]
# d_z=[]

# for start_date in range(10,40):
#     for time_window in window_list:
#         tmp_z = []
#         d_x.append(start_date)
#         d_y.append(time_window)
#         print ("#########")
#         print ("time window: " + str(time_window))
#         print ("start_date: " + date_list[date_index_list[-3]-1-start_date])
#         print ("Period_length: " + str(start_date))
#         y = []
#         for i in range(date_index_list[-42]+54-start_date,date_index_list[-42]+54):
#             y.append(float(rate_list[i]))
#         x=list(range(1,len(y)+1))

#         tck = interpolate.splrep(x, y)

#         xx = np.linspace(x[0], x[-1], time_window*(x[-1]-x[0]))
#         yy = interpolate.splev(xx, tck)
#         d1 = np.diff(yy) / np.diff(xx)
#         d2 = np.diff(d1) / np.diff(xx[1:])

#         final_x = xx[1:-1]
#         final_y = interpolate.splev(xx[1:-1], tck)
#         matrix = []
#         for i in range(len(final_x)):
#             one_date = []
#             one_date.append(final_y[i])
#             one_date.append(d1[i])
#             one_date.append(d2[i])
#             matrix.append(one_date)
#         # print (matrix)
#         # print (len(matrix))
#         X_std = StandardScaler().fit_transform(matrix)


#         pca = decomposition.PCA()
#         PCA(copy=True, iterated_power='auto', n_components=None, random_state=None, svd_solver='auto', tol=0.0, whiten=False)
#         pca_output = pca.fit_transform(X_std)
#         print (pca.explained_variance_ratio_)
#         if pca.explained_variance_ratio_[0]>max_ratio:
#             max_ratio = pca.explained_variance_ratio_[0]
#         tmp_z.append(pca.explained_variance_ratio_[0])
#         d_z.append(pca.explained_variance_ratio_[0]) 
#         # d_z.append(pca.explained_variance_[0]) 

# # d_z = np.array(d_z)

# fig = plt.figure()
# ax = Axes3D(fig)
# ax.scatter(d_x, d_y, d_z)

# ax.set_zlabel('Fraction of variance') 
# ax.set_ylabel('Time window size')
# ax.set_xlabel('Start Date')
# # plt.show()
# plt.savefig("pca_before.eps", format='eps', dpi=600)
# print (max_ratio)

#after that week
print ("start_date: " + date_list[date_index_list[-42]])
print ("start_date: " + date_list[date_index_list[-41]])
print ("start_date: " + date_list[date_index_list[-42]+55])
print ("start_date: " + date_list[date_index_list[-42]+54])

max_ratio=0
print ("hello")
# d_x=list(range(3,21))
# d_y=[300,275,250,225,200,175,150,125,100,75,50,20,10,9,8,7,6,5,3,2,1]
# d_z=[]
window_list = [300,275,250,225,200,175,150,125,100,75,50,20,10,9,8,7,6,5,3,2,1]
# list(range(1,301))
# window_list[:] = window_list[::-1]
# print (window_list)
d_x =[]
d_y=[]
d_z=[]

for start_date in range(10,40):
    for time_window in window_list:
        tmp_z = []
        d_x.append(start_date)
        d_y.append(time_window)
        print ("#########")
        print ("time window: " + str(time_window))
        print ("start_date: " + date_list[date_index_list[-3]-1-start_date])
        print ("Period_length: " + str(start_date))
        y = []
        for i in range(date_index_list[-42]+54,date_index_list[-42]+54+start_date):
            y.append(float(rate_list[i]))
        x=list(range(1,len(y)+1))

        tck = interpolate.splrep(x, y)

        xx = np.linspace(x[0], x[-1], time_window*(x[-1]-x[0]))
        yy = interpolate.splev(xx, tck)
        d1 = np.diff(yy) / np.diff(xx)
        d2 = np.diff(d1) / np.diff(xx[1:])

        final_x = xx[1:-1]
        final_y = interpolate.splev(xx[1:-1], tck)
        matrix = []
        for i in range(len(final_x)):
            one_date = []
            one_date.append(final_y[i])
            one_date.append(d1[i])
            one_date.append(d2[i])
            matrix.append(one_date)
        # print (matrix)
        # print (len(matrix))
        X_std = StandardScaler().fit_transform(matrix)


        pca = decomposition.PCA()
        PCA(copy=True, iterated_power='auto', n_components=None, random_state=None, svd_solver='auto', tol=0.0, whiten=False)
        pca_output = pca.fit_transform(X_std)
        print (pca.explained_variance_ratio_)
        if pca.explained_variance_ratio_[0]>max_ratio:
            max_ratio = pca.explained_variance_ratio_[0]
        tmp_z.append(pca.explained_variance_ratio_[0])
        d_z.append(pca.explained_variance_ratio_[0]) 
        # pca.explained_variance_
        # d_z.append(pca.explained_variance_[0]) 
# d_z = np.array(d_z)

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(d_x, d_y, d_z)

ax.set_zlabel('Fraction of variance') 
ax.set_ylabel('Time window size')
ax.set_xlabel('End Date')
# plt.show()
plt.savefig("pca_after.eps", format='eps', dpi=600)
print (max_ratio)


#just be kind

# print ("start_date: " + date_list[date_index_list[-42]])
# print ("start_date: " + date_list[date_index_list[-41]])
# print ("start_date: " + date_list[date_index_list[-42]+55])
# print ("start_date: " + date_list[date_index_list[-42]+54])
# y= []
# for i in range(date_index_list[-42]+54-30,date_index_list[-42]+54+30):
#     y.append(float(rate_list[i]))
# x=list(range(1,len(y)+1))

# plt.figure()
# ax = plt.subplot(111)
# ax.plot(x,y)
# ax.scatter(x[30],y[30], c = 'r',label = "Catastrophe")
# plt.xlabel("Date(day)")
# plt.ylabel("Exchange Rate(Yen per USD)")
# ax.legend()
# # plt.show()
# plt.savefig("1997.eps", format='eps', dpi=600)
