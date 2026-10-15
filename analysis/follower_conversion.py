import math
# date, new_followers, reach_1d, reach_nonfoll
F=[("09-15",4,1900,1412),("09-16",7,1985,1424),("09-17",4,2594,2036),("09-18",6,2776,2231),
("09-19",5,4203,3684),("09-20",44,20645,19925),("09-21",102,28881,28255),("09-22",19,9657,8939),
("09-23",14,7169,6573),("09-24",13,4434,3720),("09-25",7,4219,3532),("09-26",21,6984,6398),
("09-27",13,5625,5109),("09-28",16,4417,3690),("09-29",10,4408,3708),("09-30",15,7951,7179),
("10-01",60,37261,36600),("10-02",29,8291,7773),("10-03",17,4714,4120),("10-04",12,6039,5342),
("10-05",12,5729,4816),("10-06",13,7223,6497),("10-07",27,16297,15606),("10-08",14,6015,5267),
("10-09",7,5462,4764),("10-10",7,3847,3324),("10-11",5,3428,2892),("10-12",11,4902,4340),
("10-13",12,5787,5231),("10-14",0,3860,3334)]
def corr(a,b):
    ma,mb=sum(a)/len(a),sum(b)/len(b)
    return sum((x-ma)*(y-mb) for x,y in zip(a,b))/((sum((x-ma)**2 for x in a)**.5)*(sum((y-mb)**2 for y in b)**.5))
def q(xs,p):
    xs=sorted(xs);n=len(xs);k=(n-1)*p;f=int(k);c=min(f+1,n-1)
    return xs[f]+(k-f)*(xs[c]-xs[f])
nf=[x[1] for x in F]; rc=[x[2] for x in F]; nfr=[x[3] for x in F]
# 10-14 follower_count_1d = 0 is almost certainly incomplete (current day); exclude
Fc=[x for x in F if x[0]!="10-14"]
print("=== FOLLOWER CONVERSION  09-15..10-14 (30d) ===")
print("  new followers TOTAL  %d  (excl 10-14 incomplete: %d over 29d)"%(sum(nf),sum(x[1] for x in Fc)))
print("  per day  MED %.0f  p25 %.0f  p75 %.0f"%(q(nf,.5),q(nf,.25),q(nf,.75)))
print("  corr(new_followers, reach_1d)          r = %+.3f"%corr(nf,rc))
print("  corr(new_followers, reach_nonfollower) r = %+.3f"%corr(nf,nfr))
cv=[1000*x[1]/x[3] for x in Fc]
print("  CVR per 1,000 non-follower reach: MED %.2f  p25 %.2f  p75 %.2f"%(q(cv,.5),q(cv,.25),q(cv,.75)))
print("  非フォロワーリーチ比率 MED %.1f%%"%(q([100*x[3]/x[2] for x in F],.5)))
print("\n=== 大当たり日のCVR ===")
for d,n,r,nr in sorted(Fc,key=lambda x:-x[2])[:5]:
    print("  %s  reach %6d  non-foll %6d  new %3d  -> %.2f / 1k"%(d,r,nr,n,1000*n/nr))
print("\n=== 平常日(reach<6000)のCVR ===")
sm=[x for x in Fc if x[2]<6000]
print("  n=%d  new/day MED %.0f  CVR MED %.2f / 1k"%(len(sm),q([x[1] for x in sm],.5),q([1000*x[1]/x[3] for x in sm],.5)))
