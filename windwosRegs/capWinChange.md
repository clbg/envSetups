# how to make keybind

## keybind
keyname		scancode	
cap		00 3A
win_left	E0 5B



## example
"Scancode Map" = hex:
00,00,00,00,00,00,00,00, # fixed info don't change 
03,00,00,00, #bind个数，02为1个，03为2个，以此类推
3a,00,5b,e0, #一个bind，（逆序
5b,e0,3a,00,
00,00,00,00 # 结束
