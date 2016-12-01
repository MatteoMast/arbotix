#!/usr/bin/env python

MX_TORQUE_CONTROL_EN = 70 # (0X46)	Torque Control Mode Enable	Torque control mode on/off	RW	0 (0X00)
MX_TORQUE_CONTROL_L = 71 #(0X47)	Goal Torque(L)	Lowest byte of goal torque value	RW	0 (0X00)
MX_TORQUE_CONTROL_H = 72 #(0X48)	Goal Torque(H)	Highest byte of goal torque value	RW	0 (0X00)
MX_GOAL_ACCELARATION = 73