import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
mc.player.setTilePos(0,0,0)
mc.setBlock(1,0,1, 103)
	
for x in range(1,103):
	mc.setBlock(1,x, x*-1, x)