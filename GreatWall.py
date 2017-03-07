# Build a "Great Wall"
# Jason Shorey and Brian Shorey, 2017_03_06

from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()

height = 5	# Set height of wall
length = 100	# Set length of wall

air = 0
stone = 1
water = 8
water_stationary = 9
wood = 17

x, y, z = mc.player.getPos()

xstart = x+1
xend = x+101

for xw in range (int(xstart), int(xend)):	# Range for the length of the wall
	for yw in range (1, 255):		# Range for the height of the wall
		block = mc.getBlock(xw, yw, z)	# Get the block type
		if block == water:		# Don't build a wall on water
			break			# Not sure why this isn't working
		elif block == water_stationary:	# This also doesn't seem to work
			break
		elif block == air:		# If we're above ground, build the wall!
			mc.setBlocks(xw, yw, z, xw, yw+height, z, stone)
			break
		elif block == wood:		# Build the wall through a tree!
                        mc.setBlocks(xw, yw, z, xw, yw+height, z, stone)
                        break

