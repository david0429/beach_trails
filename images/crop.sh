#!/usr/bin/env bash

convert full.jpg -crop 304x304+0+0 00.jpg
convert full.jpg -crop 304x304+304+0 01.jpg
convert full.jpg -crop 304x304+608+0 02.jpg
convert full.jpg -crop 304x304+912+0 03.jpg
convert full.jpg -crop 304x304+1216+0 04.jpg
convert full.jpg -crop 304x304+1520+0 05.jpg

convert full.jpg -crop 304x304+0+304 10.jpg
convert full.jpg -crop 304x304+304+304 11.jpg
convert full.jpg -crop 304x304+608+304 12.jpg
convert full.jpg -crop 304x304+912+304 13.jpg
convert full.jpg -crop 304x304+1216+304 14.jpg
convert full.jpg -crop 304x304+1520+304 15.jpg

convert full.jpg -crop 304x304+0+608 20.jpg
convert full.jpg -crop 304x304+304+608 21.jpg
convert full.jpg -crop 304x304+608+608 22.jpg
convert full.jpg -crop 304x304+912+608 23.jpg
convert full.jpg -crop 304x304+1216+608 24.jpg
convert full.jpg -crop 304x304+1520+608 25.jpg

convert full.jpg -crop 304x304+0+912 30.jpg
convert full.jpg -crop 304x304+304+912 31.jpg
convert full.jpg -crop 304x304+608+912 32.jpg
convert full.jpg -crop 304x304+912+912 33.jpg
convert full.jpg -crop 304x304+1216+912 34.jpg
convert full.jpg -crop 304x304+1520+912 35.jpg

convert full.jpg -crop 304x304+0+1216 40.jpg
convert full.jpg -crop 304x304+304+1216 41.jpg
convert full.jpg -crop 304x304+608+1216 42.jpg
convert full.jpg -crop 304x304+912+1216 43.jpg
convert full.jpg -crop 304x304+1216+1216 44.jpg
convert full.jpg -crop 304x304+1520+1216 45.jpg

convert full.jpg -crop 304x304+0+1520 50.jpg
convert full.jpg -crop 304x304+304+1520 51.jpg
convert full.jpg -crop 304x304+608+1520 52.jpg
convert full.jpg -crop 304x304+912+1520 53.jpg
convert full.jpg -crop 304x304+1216+1520 54.jpg
convert full.jpg -crop 304x304+1520+1520 55.jpg
