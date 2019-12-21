# how to make keybind

## keybind
keyname		scancode	
cap		00 3A
win_left	E0 5B

Alt_left	00 38
Ctrl_left	00 1D


## example
"Scancode Map" = hex:
00,00,00,00,00,00,00,00, # fixed info don't change 
03,00,00,00, #bind个数，02为1个，03为2个，以此类推
3a,00,5b,e0, #一个bind，（逆序
#format: function key scan code, physical key scan code
#function capslock on phy key ctrl left
3a,00,1d,00,
#function left ctrl on phy key capslock
1d,00,3a,00,
#function win 
#5b,e0,3a,00,
#38,00,1d,00,
#1d,00,38,00,
00,00,00,00 # 结束
