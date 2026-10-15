import math,json
# date, views, reach, saved, shares, skip, avg_watch_ms, likes, comments
R=[("09-01",2144,1796,29,4,.461,34760,37,0),("09-02",17649,14856,245,8,.358,33735,135,0),
("09-03",1551,1284,13,1,.394,26374,20,0),("09-04",4923,4010,47,3,.359,30253,40,0),
("09-05",11753,10051,86,3,.402,34686,92,3),("09-06",1576,1337,7,0,.417,27059,18,2),
("09-07",11325,9685,39,4,.383,40999,64,7),("09-08",1457,1121,19,1,.397,25259,20,0),
("09-09",1161,945,16,1,.535,21462,15,0),("09-10",1182,948,14,3,.547,19260,23,0),
("09-11",1458,1191,14,1,.455,21450,15,0),("09-12",1460,1231,12,0,.441,20849,18,0),
("09-13",2708,2294,22,2,.381,32764,27,0),("09-14",2315,1860,23,0,.381,27937,27,2),
("09-15",2040,1657,27,1,.437,32966,18,0),("09-16",4994,4165,46,0,.302,39210,39,0),
("09-17",2454,2017,15,0,.379,26046,34,0),("09-18",1946,1531,28,0,.312,35022,27,2),
("09-19",12997,11315,62,0,.383,39681,67,0),("09-20",60643,53241,519,21,.268,41002,510,35),
("09-21",2266,1833,17,0,.478,28226,19,0),("09-22",11301,9946,64,7,.463,34508,74,0),
("09-23",1109,904,14,0,.455,22268,17,0),("09-24",3217,2670,28,5,.363,31390,34,0),
("09-25",7889,6673,66,2,.465,37696,49,5),("09-26",2520,1995,18,1,.362,44369,29,0),
("09-27",1668,1358,11,1,.455,28257,24,0),("09-28",2094,1641,62,1,.462,26848,26,0),
("09-29",2903,2518,19,0,.430,36551,19,0),("09-30",54697,50786,315,9,.265,32140,268,15),
("10-01",6287,5373,70,8,.373,36179,54,0),("10-02",2938,2457,45,3,.398,32269,40,2),
("10-03",3832,3063,61,0,.386,41771,48,0),("10-04",4915,4243,46,1,.415,39881,39,0),
("10-05",3919,3365,23,0,.387,26970,28,0),("10-06",18864,19114,135,3,.553,28198,116,15),
("10-07",3336,2792,33,1,.484,27417,38,6),("10-08",4735,4142,46,0,.338,32311,39,0),
("10-09",1155,951,12,0,.488,20490,12,0),("10-10",802,682,6,0,.592,16182,6,0),
("10-11",2564,2199,13,0,.420,23189,26,0),("10-12",7461,6026,93,2,.370,39062,49,2),
("10-13",1789,1464,14,1,.443,22040,10,0),("10-14",1134,872,12,1,.490,26093,8,0)]
K=["date","views","reach","saved","shares","skip","watch","likes","comments"]
D=[dict(zip(K,r)) for r in R]
for d in D:
    d["svr"]=d["saved"]/d["reach"]; d["watch_s"]=d["watch"]/1000.0
    d["eng"]=(d["likes"]+d["comments"]+d["saved"]+d["shares"])/d["reach"]
def q(xs,p):
    xs=sorted(xs);n=len(xs);k=(n-1)*p;f=int(k);c=min(f+1,n-1)
    return xs[f]+(k-f)*(xs[c]-xs[f])
def corr(a,b):
    ma,mb=sum(a)/len(a),sum(b)/len(b)
    na=sum((x-ma)**2 for x in a)**.5; nb=sum((y-mb)**2 for y in b)**.5
    return sum((x-ma)*(y-mb) for x,y in zip(a,b))/(na*nb)
n=len(D)
print("=== NEW BASELINE  2026-09-01 .. 2026-10-14   n=%d reels (44 days, 1/day) ==="%n)
for f,lab,mul,fmt in [("views","views",1,"%.0f"),("reach","reach",1,"%.0f"),("saved","saves",1,"%.0f"),
                      ("svr","save_rate_pct",100,"%.2f"),("skip","skip_pct",100,"%.1f"),
                      ("watch_s","watch_sec",1,"%.1f"),("eng","eng_rate_pct",100,"%.2f")]:
    xs=[d[f]*mul for d in D]
    print(("  %-14s p25 "+fmt+"  MED "+fmt+"  p75 "+fmt)%(lab,q(xs,.25),q(xs,.5),q(xs,.75)))
print("  TOTAL views %d / reach %d / saves %d"%(sum(d["views"] for d in D),sum(d["reach"] for d in D),sum(d["saved"] for d in D)))

print("\n=== PREDICTOR TEST vs log(views) ===")
lv=[math.log(d["views"]) for d in D]
for f,lab in [("skip","skip_rate"),("watch_s","avg_watch_sec"),("svr","save_rate"),("saved","save_count")]:
    print("  %-14s r = %+.3f"%(lab,corr([d[f] for d in D],lv)))

print("\n=== 1万再生 %d / %d ==="%(sum(1 for d in D if d["views"]>=10000),n))
for d in sorted((d for d in D if d["views"]>=10000),key=lambda x:-x["views"]):
    print("  %s  %6d views  skip %.1f%%  watch %.1fs  save %.2f%%"%(d["date"],d["views"],d["skip"]*100,d["watch_s"],d["svr"]*100))

print("\n=== GATE COMPARISON (which single threshold best separates 1万再生?) ===")
def gate(f,thr,le=True):
    sel=[d for d in D if (d[f]<=thr if le else d[f]>=thr)]
    oth=[d for d in D if d not in sel]
    if not sel or not oth: return None
    h=sum(1 for d in sel if d["views"]>=10000); ho=sum(1 for d in oth if d["views"]>=10000)
    return (len(sel),h,100*h/len(sel),len(oth),ho,100*ho/len(oth))
for f,thr,le,lab in [("skip",.344,True,"skip<=34.4% (OLD RULE)"),("skip",.40,True,"skip<=40%"),
                     ("watch_s",32,False,"watch>=32s"),("watch_s",33.7,False,"watch>=33.7s(MED)"),
                     ("watch_s",36,False,"watch>=36s"),("saved",46,False,"saves>=46(p75)")]:
    g=gate(f,thr,le)
    print("  %-24s in: n=%2d hit=%d (%.0f%%)   out: n=%2d hit=%d (%.0f%%)"%((lab,)+g))

print("\n=== REACH-BAND DILUTION ===")
for lo,hi,lbl in [(0,2000,"<2,000"),(2000,5000,"2,000-5,000"),(5000,15000,"5,000-15,000"),(15000,10**9,"15,000+")]:
    v=[d for d in D if lo<=d["reach"]<hi]
    if v: print("  %-14s n=%2d  save_rate MED %.2f%%  save_cnt MED %3.0f  skip MED %.1f%%  watch MED %.1fs"%(
        lbl,len(v),q([d["svr"] for d in v],.5)*100,q([d["saved"] for d in v],.5),
        q([d["skip"] for d in v],.5)*100,q([d["watch_s"] for d in v],.5)))
