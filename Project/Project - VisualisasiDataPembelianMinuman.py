#Roni Merdiansah
#2010631250097
#2C Sistem Informasi

#Import Library
import numpy as np
import matplotlib.pyplot as plt

#Membuat Data
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei']
jm = ['Air Mineral','Teh','Kopi','Isotonik','Soda']
airmineral = [41,54,37,58,53]
teh = [32,27,15,22,23]
kopi = [21,19,26,30,24]
isotonik = [11,14,9,14,12]
soda = [9,7,12,8,8]

n1 = [53,23,24,12,8]
n2 = [58,22,30,14,8]
n3 = [37,15,26,9,12]
n4 = [54,27,19,14,7]
n5 = [41,32,21,11,9]

colors = ('lightblue','sandybrown','saddlebrown','deepskyblue','lightgray')*5

x = np.array(range(5))
y = np.array(range(5))
xpos, ypos = np.meshgrid(x,y)
z = np.array([[n5],
              [n4],
              [n3],
              [n2],
              [n1]])

xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros_like(xpos)

dx = 0.5 * np.ones_like(zpos)
dy = dx.copy()
dz = z.flatten()

x2 = np.arange(len(bulan))
width = 0.25

#Mengatur Opsi Yang Akan Tampil
fig = plt.figure(figsize=(13,5))
ax3 = fig.add_subplot(131)
ax2 = fig.add_subplot(132)
ax = fig.add_subplot(133,projection='3d')

ax.bar3d(xpos,ypos,zpos,dx,dy,dz,color=(np.array(colors)),shade=True)
labels=['Air Mineral','Teh','Kopi','Isotonik','Soda']

ax.set_title('3D Bar Penjualan Jenis Minuman\nJanuari-Mei', size=12)

ax.set_xticklabels(np.array(jm),size=8,color='k')
ax.set_xticks(range(5))
ax.set_xlabel('Jenis Minuman',labelpad=12,color='g')

ax.set_yticklabels(np.array(bulan),size=8,color='c')
ax.set_yticks(range(5))
ax.set_ylabel('Bulan',labelpad=8,color='b')

ax.set_zlabel('Jumlah Terjual/Buah',size=8,color='r')

am = ax2.bar(x2 + width/2, airmineral, width, label='Air Mineral', color='lightblue')
th = ax2.bar(x2 - width/2, teh, width, label='Teh', color='sandybrown')
kp = ax2.bar(x2 + width/4, kopi, width, label='Kopi', color='saddlebrown')
ist = ax2.bar(x2 - width/4, isotonik, width, label='Isotonik', color='deepskyblue')
sd = ax2.bar(x2 + width/6, soda, width, label='Soda', color='lightgray')

ax2.set_title('Grafik Bar Penjualan Jenis Minuman\nJanuari-Mei', size=12)
ax2.set_ylabel('Jumlah Terjual/Buah',size=8,color='r')
ax2.set_xticks(x2)
ax2.grid(linestyle='--',linewidth=0.5, axis='y')
ax2.set_xticklabels(bulan, size=8,color='c')
ax2.legend(fontsize=6.5)

ax3.plot(airmineral,color='lightblue',marker='o',linestyle='--')
ax3.plot(teh,color='sandybrown',marker='H',linestyle=':')
ax3.plot(kopi,color='saddlebrown',marker='>',linestyle='-')
ax3.plot(isotonik,color='deepskyblue',marker='*',linestyle=':')
ax3.plot(soda,color='lightgray',marker='|',linestyle='--')

ax3.set_title('Grafik Line Penjualan Jenis Minuman\nJanuari-Mei', size=12)
ax3.set_ylabel('Jumlah Terjual/Buah',size=8,color='r')
ax3.set_xticks(x2)
ax3.grid(linestyle='--',linewidth=0.5, axis='y')
ax3.set_xticklabels(bulan, size=8,color='c')

#Perintah Menampilkan
plt.show()