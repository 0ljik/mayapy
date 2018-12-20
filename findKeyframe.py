import maya.cmds as cmds
selection = cmds.ls(selection = True)
print "Using the range of animated keyframes on the selection"
keys=[]
keys.append(cmds.findKeyframe(selection, which = 'last'))
keys.append(cmds.findKeyframe(selection, which = 'first'))
i=2
time = keys[1]
while time!=endTime:
    keys.append(cmds.findKeyframe(selection, time=(time,keys[0])))
    time=keys[i]
    i+=1
    
for i in range(len(keys)):
    print(keys[i])
