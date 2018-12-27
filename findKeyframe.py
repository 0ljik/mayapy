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
    
#file -import -type "STEP_ATF"  -ignoreVersion -ra true -mergeNamespacesOnClash false -namespace "DRJ_0001__L_type_Single_Nut" -options "ts=0;ec=0;cd=0.0015;icl=0.01;mcl=100.0;s=3;adp=1;smp=8;ant=0.0;leg=0;en=0;nt=15.0;st=0.0;gar=21.5;mel=11.314646;"  -pr  -importFrameRate true  -importTimeRange "override" "C:/Users/oljak/OneDrive/Documents/JOINT/[DRJ-0001] L-type_Single Nut.stp";
#file -import -type "STEP_ATF"  -ignoreVersion -ra true -mergeNamespacesOnClash false -namespace "DRJ_0002__L_type_Double_Nut" -options "ts=0;ec=0;cd=0.0015;icl=0.01;mcl=100.0;s=3;adp=1;smp=8;ant=0.0;leg=0;en=0;nt=15.0;st=0.0;gar=21.5;mel=11.314646;"  -pr  -importTimeRange "combine" "C:/Users/oljak/OneDrive/Documents/JOINT/[DRJ-0002] L-type_Double Nut.stp";#
#file -import -type "STEP_ATF"  -ignoreVersion -ra true -mergeNamespacesOnClash false -namespace "DRJ_0003__L_type_Hole_only" -options "ts=0;ec=0;cd=0.0015;icl=0.01;mcl=100.0;s=3;adp=1;smp=8;ant=0.0;leg=0;en=0;nt=15.0;st=0.0;gar=21.5;mel=11.314646;"  -pr  -importTimeRange "combine" "C:/Users/oljak/OneDrive/Documents/JOINT/[DRJ-0003] L-type_Hole only.stp";
#file -import -type "STEP_ATF"  -ignoreVersion -ra true -mergeNamespacesOnClash false -namespace "DRJ_0004__I_type_10_9mm_Hole_only" -options "ts=0;ec=0;cd=0.0015;icl=0.01;mcl=100.0;s=3;adp=1;smp=8;ant=0.0;leg=0;en=0;nt=15.0;st=0.0;gar=21.5;mel=11.314646;"  -pr  -importTimeRange "combine" "C:/Users/oljak/OneDrive/Documents/JOINT/[DRJ-0004] I-type_10.9mm Hole only.stp";
#file -import -type "STEP_ATF"  -ignoreVersion -ra true -mergeNamespacesOnClash false -namespace "DRJ_0006__I_type_12_5mm_Double_Nut" -options "ts=0;ec=0;cd=0.0015;icl=0.01;mcl=100.0;s=3;adp=1;smp=8;ant=0.0;leg=0;en=0;nt=15.0;st=0.0;gar=21.5;mel=11.314646;"  -pr  -importTimeRange "combine" "C:/Users/oljak/OneDrive/Documents/JOINT/[DRJ-0006] I-type_12.5mm Double Nut.stp";
#file -import -type "STEP_ATF"  -ignoreVersion -ra true -mergeNamespacesOnClash false -namespace "DRJ_0007__I_type_16mm_hole_only" -options "ts=0;ec=0;cd=0.0015;icl=0.01;mcl=100.0;s=3;adp=1;smp=8;ant=0.0;leg=0;en=0;nt=15.0;st=0.0;gar=21.5;mel=11.314646;"  -pr  -importTimeRange "combine" "C:/Users/oljak/OneDrive/Documents/JOINT/[DRJ-0007] I-type_16mm hole only.stp";
### file -import -type "STEP_ATF"  -ignoreVersion -ra true -mergeNamespacesOnClash false -namespace "DRJ_0008__V_type_12mm_Single_Nut" -options "ts=0;ec=0;cd=0.0015;icl=0.01;mcl=100.0;s=3;adp=1;smp=8;ant=0.0;leg=0;en=0;nt=15.0;st=0.0;gar=21.5;mel=11.314646;"  -pr  -importTimeRange "combine" "C:/Users/oljak/OneDrive/Documents/JOINT/[DRJ-0008] V-type_12mm Single Nut.stp";
#file -import -type "STEP_ATF"  -ignoreVersion -ra true -mergeNamespacesOnClash false -namespace "DRJ_0009__V_type_12mm_Double_Nut" -options "ts=0;ec=0;cd=0.0015;icl=0.01;mcl=100.0;s=3;adp=1;smp=8;ant=0.0;leg=0;en=0;nt=15.0;st=0.0;gar=21.5;mel=11.314646;"  -pr  -importTimeRange "combine" "C:/Users/oljak/OneDrive/Documents/JOINT/[DRJ-0009] V-type_12mm Double Nut.stp";
### file -import -type "STEP_ATF"  -ignoreVersion -ra true -mergeNamespacesOnClash false -namespace "DRJ_0010__Harness_Clamp" -options "ts=0;ec=0;cd=0.0015;icl=0.01;mcl=100.0;s=3;adp=1;smp=8;ant=0.0;leg=0;en=0;nt=15.0;st=0.0;gar=21.5;mel=11.314646;"  -pr  -importTimeRange "combine" "C:/Users/oljak/OneDrive/Documents/JOINT/[DRJ-0010] Harness Clamp.stp";
#file -import -type "STEP_ATF"  -ignoreVersion -ra true -mergeNamespacesOnClash false -namespace "DRJ_0011__Bushing_Set_female" -options "ts=0;ec=0;cd=0.0015;icl=0.01;mcl=100.0;s=3;adp=1;smp=8;ant=0.0;leg=0;en=0;nt=15.0;st=0.0;gar=21.5;mel=11.314646;"  -pr  -importTimeRange "combine" "C:/Users/oljak/OneDrive/Documents/JOINT/[DRJ-0011] Bushing Set_female.stp";
#file -import -type "STEP_ATF"  -ignoreVersion -ra true -mergeNamespacesOnClash false -namespace "DRJ_0011__Bushing_Set_male" -options "ts=0;ec=0;cd=0.0015;icl=0.01;mcl=100.0;s=3;adp=1;smp=8;ant=0.0;leg=0;en=0;nt=15.0;st=0.0;gar=21.5;mel=11.314646;"  -pr  -importTimeRange "combine" "C:/Users/oljak/OneDrive/Documents/JOINT/[DRJ-0011] Bushing Set_male.stp";
#file -import -type "STEP_ATF"  -ignoreVersion -ra true -mergeNamespacesOnClash false -namespace "HerkuleX__DRS_010X" -options "ts=0;ec=0;cd=0.0015;icl=0.01;mcl=100.0;s=3;adp=1;smp=8;ant=0.0;leg=0;en=0;nt=15.0;st=0.0;gar=21.5;mel=11.314646;"  -pr  -importTimeRange "combine" "C:/Users/oljak/OneDrive/Documents/JOINT/[HerkuleX] DRS-010X.stp";
#select -r HerkuleX__DRS_010X;
#duplicate -rr;
#move -r 2.602818 0 0 HerkuleX__DRS_010X.scalePivot HerkuleX__DRS_010X.rotatePivot ;
#move -r 2.602818 0 0 HerkuleX__DRS_010X1.scalePivot HerkuleX__DRS_010X1.rotatePivot ;
 
importpath='C:/workspace/maya/herkulex/'
filename='[HerkuleX] DRS-010X.stp'
filepath=importpath+filename
cmds.file(filepath, i=True)
for i in range(19):
    cmds.select('HerkuleX__DRS_010X', r=True)
    cmds.duplicate(rr=True)
    cmds.move(2.602818, 0, 0, 'HerkuleX__DRS_010X'+str(i+1)+'.scalePivot', 'HerkuleX__DRS_010X'+str(i+1)+'.rotatePivot', r=True)
