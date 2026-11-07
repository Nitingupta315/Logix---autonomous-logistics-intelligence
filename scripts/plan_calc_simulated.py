"""SIMULATED recovery-plan calculator - Logix Command (LOGIX). Simulated data only; no real orders.
Reads the v2 files. Rules (Admin corrections 2-4):
 - Quantity per supplier <= Max order quantity (suppliers_simulated_v2.csv); split orders allowed.
 - Deadline rule (Logix Stock): each delivery must be received by the end of the last day whose
   closing stock is still >= safety stock, given all earlier legs. First leg: end of 2026-11-12.
   Checked on both planned and worst-case delivery dates (logistics_simulated_v2.csv).
 - Total recovery cost = component purchase (qty x ex-works unit price) + transport (full booking quote).
"""
import csv, datetime as dt, os
B=os.path.dirname(os.path.abspath(__file__))+'/..'
P=lambda s: dt.date.fromisoformat(s[:10])
sup={r['Supplier ID']:r for r in csv.DictReader(open(B+'/suppliers_simulated_v2.csv',encoding='utf-8'))}
rt={r['Route ID']:r for r in csv.DictReader(open(B+'/logistics_simulated_v2.csv',encoding='utf-8'))}
inv=next(csv.DictReader(open(B+'/inventory_simulated_v2.csv',encoding='utf-8')))
START=P(inv['Snapshot date']); ON=int(inv['On-hand stock (units)']); USE=int(inv['Avg daily consumption (units/day)'])
SS=int(inv['Safety stock (units)']); PO=int(inv['Open PO quantity (units)']); BASE=float(inv['Unit cost (€)'])

def safe_until(legs):  # last day closing >= SS, given legs as (qty, date) received before day's use
    s=ON; d=START
    while True:
        s+=sum(q for q,dd in legs if dd==d); s-=USE
        if s<SS: return d-dt.timedelta(1)
        d+=dt.timedelta(1)

# Re-priced by Logix Route at actual split quantity (incident test): 15,000 units by van = 4 vans x €650
TRANSPORT_OVERRIDE={('SIM-RT-04',15000):2600.0}
OPTIONS={
 'G (Admin proposal)':[('SIM-RT-02',9000),('SIM-RT-04',15000)],  # (route, qty)
 'A':[('SIM-RT-01',9000),('SIM-RT-04',15000)],
 'B':[('SIM-RT-01',9000),('SIM-RT-03',15000)],
 'C':[('SIM-RT-01',9000),('SIM-RT-05',15000)],
 'D':[('SIM-RT-01',9000),('SIM-RT-08',15000)],
 'E':[('SIM-RT-04',20000)],
 'F':[('SIM-RT-01',9000),('SIM-RT-04',20000)],
}
def evaluate(legs):
    out=[]; comp=tr=qty=0; ok_p=ok_w=True; prev_p=[]; prev_w=[]
    for r,q in sorted(legs,key=lambda x:P(rt[x[0]]['Planned delivery date'])):
        R=rt[r]; S=sup[R['Supplier ID']]; cap=int(S['Max order quantity (units)'])
        assert q<=cap, f"{r}: {q} > cap {cap}"
        price=float(S['Unit price (€)']); t=TRANSPORT_OVERRIDE.get((r,q),float(R['Transport cost (€)']))
        pd,wd=P(R['Planned delivery date']),P(R['Worst-case delivery date'])
        dl_p,dl_w=safe_until(prev_p),safe_until(prev_w)
        ok_p&=pd<=dl_p; ok_w&=wd<=dl_w
        prev_p.append((q,pd)); prev_w.append((q,wd))
        comp+=q*price; tr+=t; qty+=q
        out.append(dict(route=r,supplier=R['Supplier ID'],mode=R['Transport mode'],qty=q,price=price,
            comp=q*price,transport=t,planned=pd,worst=wd,deadline=dl_w,rel=S['Reliability score'],risk=R['Delay risk']))
    return dict(legs=out,qty=qty,comp=comp,transport=tr,total=comp+tr,premium=comp-qty*BASE,
                ok_planned=ok_p,ok_worst=ok_w,covers_po=qty>=PO,cover_until=safe_until(prev_w))
if __name__=='__main__':
    print(f"SIMULATED | deadline first leg: end of {safe_until([])} | PO {PO:,} @ €{BASE}")
    for k,legs in OPTIONS.items():
        e=evaluate(legs)
        print(f"\nOption {k}: {e['qty']:,} u | component €{e['comp']:,.0f} + transport €{e['transport']:,.0f} = €{e['total']:,.0f} "
              f"| premium vs PO price €{e['premium']:,.0f} | deadline planned {'OK' if e['ok_planned'] else 'MISS'} / worst {'OK' if e['ok_worst'] else 'MISS'} "
              f"| covers PO {'yes' if e['covers_po'] else 'NO'} | worst-case cover to end {e['cover_until']}")
        for l in e['legs']:
            print(f"   {l['supplier']} {l['qty']:,}u {l['route']} {l['mode']}: planned {l['planned']} / worst {l['worst']} (leg deadline {l['deadline']}) "
                  f"| {l['qty']:,}×€{l['price']:.2f}=€{l['comp']:,.0f} + €{l['transport']:,.0f} | rel {l['rel']} risk {l['risk']}")
