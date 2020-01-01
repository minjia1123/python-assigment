def parse(filename):
    f=open(filename,"r")
    line_of_f=f.readlines()
    inf_of_single=[]
    inf_of_long=[]
    for line in line_of_f:
        linf=line.split('"')
        if len(linf)!=5:continue
        time_of_beat=int(linf[1])
        type_of_beat=linf[-2]
        if type_of_beat.isdigit(): inf_of_single.append((time_of_beat,int(type_of_beat)))
        else:
            tmp_1=type_of_beat.split("$")
            for i in tmp_1:
                if i.isdigit():inf_of_single.append((time_of_beat,int(i)))
                else:
                    tmp2=i.split("_")
                    inf_of_long.append((time_of_beat,int(tmp2[0]),int(tmp2[1])))
    f.close()

    #for i in inf_of_single:print(i)
    #print("")
    #for i in inf_of_long:print(i)
    return inf_of_single, inf_of_long

#parse("flowerdance.xml")