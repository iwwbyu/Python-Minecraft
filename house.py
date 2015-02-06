#builds a house!
import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
mc.player.setTilePos(0,0,0)


#hole in the ground
mc.setBlocks(-10,0,-10, 10,40,10, 0)

#floor
mc.setBlocks(-5,-1,-5, 5,-1,5, 4)

#walls
mc.setBlocks(-5,3,-5, -5,0,5, 45)
mc.setBlocks(5,3,5, -5,0,5, 45)
mc.setBlocks(5,3,5, 5,0,-5, 45)
mc.setBlocks(-5,3,-5, 5,0,-5, 45)

#windows
mc.setBlocks(-5,1,-5, -5,1,5, 20)
mc.setBlocks(5,1,5, -5,1,5, 20)
mc.setBlocks(5,1,5, 5,1,-5, 20)
mc.setBlocks(-5,1,-5, 5,1,-5, 20)
#chests
mc.setBlock(4,0,4, 54)
mc.setBlock(-4,0,4, 54)
mc.setBlock(4,0,-4, 54)
mc.setBlock(-4,0,-4, 54)

#stairs
for x in range(1,11):
	mc.setBlock(x-10,x-1,-6, 5)
	mc.setBlock(x-10,x-1,+6, 5)
	mc.setBlock(-x+10,x-1,-6, 5)
	mc.setBlock(-x+10,x-1,+6, 5)

#bridges
for x in range(1,8):
	mc.setBlock(x-7,x+2,-5, 5)
	mc.setBlock(x-7,x+2,-4, 5)
	mc.setBlock(x-7,x+2,-3, 5)
	mc.setBlock(x-7,x+2,-2, 5)
	mc.setBlock(x-7,x+2,-1, 5)
	mc.setBlock(x-7,x+2,0, 5)
	mc.setBlock(x-7,x+2,1, 5)
	mc.setBlock(x-7,x+2,2, 5)
	mc.setBlock(x-7,x+2,3, 5)
	mc.setBlock(x-7,x+2,4, 5)
	mc.setBlock(x-7,x+2,5, 5)
	mc.setBlock(1,x+8,-x-3, 5)
	mc.setBlock(-1,x+8,-x-3, 5)
	mc.setBlock(1,x+8,x+3, 5)
	mc.setBlock(-1,x+8,x+3, 5)


for x in range(1,7):
	mc.setBlock(-x+7,x+2,-6, 5)
	mc.setBlock(-x+7,x+2,-5, 5)
	mc.setBlock(-x+7,x+2,-4, 5)
	mc.setBlock(-x+7,x+2,-3, 5)
	mc.setBlock(-x+7,x+2,-2, 5)
	mc.setBlock(-x+7,x+2,-1, 5)
	mc.setBlock(-x+7,x+2,0, 5)
	mc.setBlock(-x+7,x+2,1, 5)
	mc.setBlock(-x+7,x+2,2, 5)
	mc.setBlock(-x+7,x+2,3, 5)
	mc.setBlock(-x+7,x+2,4, 5)
	mc.setBlock(-x+7,x+2,5, 5)
	mc.setBlock(-x+7,x+2,6, 5)

#roof
for x in range(1,6):
	mc.setBlock(0,x+9,-x-5, 5)
	mc.setBlock(0,x+9,x+5, 5)
	mc.setBlock(0,x+9,-x-10, 5)

#gables
mc.setBlocks(-5,4,5, 5,4,5, 5)
mc.setBlocks(-5,4,-5, 5,4,-5, 5)
mc.setBlocks(-4,5,5, 4,5,5, 5)
mc.setBlocks(-4,5,-5, 4,5,-5, 5)
mc.setBlocks(-3,6,5, 3,6,5, 5)
mc.setBlocks(-3,6,-5, 3,6,-5, 5)
mc.setBlocks(-2,7,5, 2,7,5, 5)
mc.setBlocks(-2,7,-5, 2,7,-5, 5)
mc.setBlocks(0,8,5, 0,8,-5, 5)



mc.setBlocks(-4,1,-4, 4,4,4, 0)
mc.setBlocks(-4,2,-4, -4,2,4, 50)
mc.setBlocks(4,2,4, -4,2,4, 50)
mc.setBlocks(4,2,4, 4,2,-4, 50)
mc.setBlocks(-4,2,-4, 4,2,-4, 50)
mc.setBlocks(-5,0,0, -5,1,0, 64)
mc.setBlocks(5,0,0, 5,1,0, 64)
mc.setBlocks(0,0,5, 0,1,5, 64)
mc.setBlocks(0,0,-5, 0,1,-5, 64)
mc.setBlocks(2,0,2, 2,0,1, 26)
#mc.setBlocks(9,1,9, 9,15,9, 65)