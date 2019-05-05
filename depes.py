#python2.7
# - *- coding: utf- 8 - *-
#CreatedCyXNot404
#recode ga bakal bikin lu pro!

blue='\033[94m'
green='\033[92m'
purple='\033[95m'
cyan='\033[96m'
red='\033[91m'
white='\033[97m'
yellow='\033[93m'

import os,sys,time

mes ="""       <[+==============================================+]>
         |		ScDefaceCreator : V1		|
         +—————————————————————————————————————-—-——————|
	 |		Author    : CyXNot404		|
	 |		Developer : LuckyArd		|
	 |		Github    : LuckyArd110		|
	 |		Facebook  : lucky.ardhika	|
	 |		Instagram : @chg.official	|
	 |		FreeFire  : SAVAGE2025L		|
	 |		Youtube   : LuckyArd110		|
       <[+==============================================+]>"""

os.system('clear')
print "\033[92m "
print mes
time.sleep(2)
print
print "SELAMAT DATANG DI TOOLS SAYA :) ISI LENGKAP DATA DI BAWAH :)"
print
print "==========================================================="
print
a = raw_input('Title 				   : ')
c = raw_input('Hacked By? 			   : ')
d = raw_input('Apa Warna Font UntUk Hacked By ..? : ')
e = raw_input('Masukkan Isi/Pesan scrip 	   : ')
f = raw_input('Apa Warna Untuk Isi/Pesan? 	   : ')
g = raw_input('Thanks To ? 			   : ')
h = raw_input('Link Gambar 			   : ')
print
print "================================================================"
print "\033[96mScrip Deface Sedang di Buat..."
time.sleep(2)
fo = open('scriptv1.html','w')
teks1 ="""<html>
<font color="lime"><b><strong>
<marquee scrollamount="9" direction="left">0101010101010101010101010101010101010101010100101010101010100110101010101010101010101010101001010101</marquee>
<marquee scrollamount="9" direction="right">0101010100101010110101010101010101010101010100101010101010101010101010101010101010101010101001010101</marquee>
<marquee scrollamount="9" direction="left">0101010101010101010101010101010101010101010100101010101001101010101010101010101010101010101001010101</marquee>
<marquee scrollamount="9" direction="right">0101010101010101010101010010101011010101010100101010101010101010101010101010101010101010101001010101</marquee>
<marquee scrollamount="9" direction="left">0101010101010101010101010101010101010101010100101010011010101010101010101010101010101010101001010101</marquee>
<marquee scrollamount="9" direction="right">0101010101010101010101010101010101010010101010101010101010101010101010101010101010101010101001010101</marquee>
</font>
</strong></b></font>
<head>
<title>"""

title = a

teks2 ="""</title>

<style>
body{
    background-color:#000000;
 
</style>

<body bgcolor=black><table width=100% height=100%><td align=center><span style='font: 60px calibri;size:60px; color:"""
colord = d

tek =""";text-shadow: 0px 0px 70px;'>
<b>"""
hacked = c
teks4 ="""<b style='font: 82px calibri;size: 90px'></b>
<br>
<br>"""

teks5 ='''<center>
<img src="'''
img = h
teks0 ='''" height="500" width="500"> 
</center>
<br>
<center>
<font color="'''

colors = f

teks6 ='''" size="7" face='Iceland'><b>'''

isi = e

teks7 ='''</b></font>
</center>
<center>
<br>
<font size="5" color="blue"/>
Tanks to :
<br>'''

thanks = g

teks8 ='''</font>
</center>
<br>
<br>
<font size="5" color="lime">
<marquee scrollamount="5" direction="left" behavior="alternate">010101010101010101010101010101010101001010101010101010101010101010101010101010101001010101</marquee>
<marquee scrollamount="5" direction="right" behavior="alternate">010101010101010101010101010101010101001010101010101010101010101010101010101010101001010101</marquee>
<marquee scrollamount="5" direction="left" behavior="alternate">010101010101010101010101010101010101001010101010101010101010101010101010101010101001010101</marquee>
<marquee scrollamount="5" direction="right" behavior="alternate">010101010101010101010101010101010101001010101010101010101010101010101010101010101001010101</marquee>
<marquee scrollamount="5" direction="left" behavior="alternate">010101010101010101010101010101010101001010101010101010101010101010101010101010101001010101</marquee>
</font>
<br>
<br>
<br>
<font size="2" color="yellow"/>
developer by CyXNot404
</font>
'''
fo.write(teks1)
fo.write(title)
fo.write(teks2)
fo.write(colord)
fo.write(tek)
fo.write(hacked)
fo.write(teks4)
fo.write(teks5)
fo.write(img)
fo.write(teks0)
fo.write(colors)
fo.write(teks6)
fo.write(isi)
fo.write(teks7)
fo.write(thanks)
fo.write(teks8)
fo.close()

os.system('mv scriptv1.html /sdcard')
print "==============================================================]>"
print "              Done! Disimpan di internal luar folder "
print "                    dengan nama scriptv1.html"
print "==============================================================]>"
