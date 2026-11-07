# SIMULATED logistics dataset v2 — LOGIX (not real data)

**File:** `logistics_simulated_v2.csv` (supersedes `logistics_simulated.csv` for the demo; the original is kept unchanged)
**Status:** ⚠️ SIMULATED / FICTIONAL. Created by Logix Route (Logistics Intelligence Agent, LOGIX – Autonomous Logistics Intelligence). All carriers (SIM-CAR-…), routes, costs, risks and emissions are invented. No carrier contacted, nothing booked, no live GPS/tracking used. Any real booking needs explicit human approval.

## What changed vs v1 (see CORRECTIONS_simulated.md)
1. **Lead-time definition (Admin point 1).** Supplier lead time = order → ready-to-ship at the supplier. Delivered lead time = supplier lead time + transit. v1 already computed dates this way (dispatch = 2026-11-07 + lead time; delivery = dispatch + transit), so **no delivery date changed**. v2 renames the columns to make the definition explicit and adds "Delivered lead time - order to plant (days)".
2. **Conservative deadline (Admin point 3).** The stock-out flag ("before 2026-11-14") is replaced by **latest safe delivery date = end of 2026-11-12**. Stock falls below safety stock (2,270) during 11-13 and runs out during 11-14, per inventory_simulated.csv. If Logix Stock states a different date, the two "Meets deadline" columns will be regenerated.
3. **Worst-case date.** New column: planned delivery + expected delay if disrupted (rounded up to whole days). "Meets deadline (worst case)" uses it.
4. **Cost split (Admin point 4).** Added component unit price (from suppliers_simulated.csv), component purchase cost (qty × price), and total landed cost (purchase + transport).
5. **Quantity (Admin point 2).** Shipment quantity is still min(available, 24,000): SIM-S016 can ship 9,000 and SIM-S017 20,000. No row covers 24,000 on its own before the deadline.

## Deadline results (single shipment, deadline end of 11-12)
- **Safe even in worst case:** SIM-RT-01 Amberg FTL (11-10, worst 11-11) and SIM-RT-02 Amberg LTL (11-11, worst 11-12). Both only 9,000 units.
- **On time if nothing goes wrong:** SIM-RT-04 Innsbruck express vans (11-12, worst 11-13).
- **Late:** every other route, including SIM-RT-03 Innsbruck FTL (11-13).

## Split-order note (for Logix Command)
If 9,000 units from Amberg arrive on 11-10 (counted at end of day), stock on the evening of 11-10 is 8,400 + 9,000 = 17,400. It then falls below safety stock during 11-17, so the **second delivery's latest safe date moves to end of 2026-11-16**. Against that date:
- SIM-RT-03 Innsbruck FTL (worst 11-14) and SIM-RT-04 vans (worst 11-13) both meet it with margin.
- SIM-RT-05 Wrocław FTL (worst 11-16) meets it with zero margin, and the supplier's reliability is 0.78.
