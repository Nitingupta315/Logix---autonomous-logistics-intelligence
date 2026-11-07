# CORRECTIONS log — LOGIX SIMULATED datasets

⚠️ All data in the LOGIX folder is SIMULATED / FICTIONAL. Shared change log requested by Admin (project owner) on 2026-11-07. Original files are kept unchanged; corrections go into new `_v2` files. Each agent appends its own section; please don't edit other agents' sections.

---

## Logix Source — suppliers (2026-11-07)
**New files:** `suppliers_simulated_v2.csv`, `README_suppliers_simulated_v2.md`
**Unchanged:** `suppliers_simulated.csv`, `README_suppliers_simulated.md`

| # | Change | Why |
|---|---|---|
| S-1 | Lead time redefined as order → **ready to ship at the supplier** (transit excluded). Column renamed `Lead time (days)` → `Supplier lead time to ready-to-ship (days)`. Values unchanged. | Admin point 1. The v1 README said "order to delivery at plant" while the logistics data added transit on top, which counted transport twice. Delivered time = lead time + transit. |
| S-2 | Added `Earliest ready-to-ship date (if ordered 2026-11-07)`. | Makes the dispatch date explicit for logistics and planning; matches the "Earliest dispatch date" already in logistics_simulated.csv. |
| S-3 | `Available quantity` renamed `Max order quantity (units)`. | Admin point 2. Makes clear it is a hard cap that recovery options must respect. |
| S-4 | Added `Covers 24,000-unit PO alone` flag (COMP-ES-204 rows). | Admin point 2. S016 (9,000) and S017 (20,000) cannot cover the PO alone, so a split order is needed. |
| S-5 | Added `Data label` = SIMULATED column; README clarifies unit price is ex works (no freight). | Labelling consistency with the logistics file; avoids double-counting transport in total recovery cost (Admin point 4). |

No supplier, price, quantity or lead-time figure was changed.

## Logix Route — logistics_simulated_v2.csv (+ README_logistics_simulated_v2.md)
Original `logistics_simulated.csv` and its README are unchanged.
- **Lead-time definition (Admin point 1):** adopted "supplier lead time = order → ready-to-ship; delivered = lead time + transit". v1 already worked this way (dispatch = 2026-11-07 + lead time, delivery = dispatch + transit), so no dates changed. *Why:* the double-count came from the supplier README wording ("order to delivery at the plant"), not from the route dates. Columns were renamed and "Delivered lead time" added so the definition is explicit.
- **Deadline (Admin point 3):** the "before stock-out 2026-11-14" flag was replaced by "Meets deadline (planned / worst case)" against **end of 2026-11-12**. *Why:* a delivery on 11-14 is not safe, and stock drops below safety stock during 11-13. This will be regenerated if Logix Stock confirms a different date.
- **Worst-case delivery date added:** planned date + expected delay, rounded up. *Why:* so the deadline check covers the risk.
- **Cost split (Admin point 4):** added component unit price, purchase cost (qty × price) and total landed cost. *Why:* so Logix Command can show both parts.
- **Quantity (Admin point 2):** unchanged. Rows are capped at supplier availability (S016 9,000, S017 20,000, others 24,000). The README notes the second-leg deadline for a split order (end of 11-16 after 9,000 units land on 11-10).

## Logix Command — recovery-plan logic (2026-11-07)
**New files:** `command_work/plan_calc_simulated.py` (reads the three `_v2` files), `command_work/plan_options_simulated.txt` (its output). No original changed.

| # | Change | Why |
|---|---|---|
| C-1 | Every option checks each leg's quantity against the supplier's `Max order quantity` (S016 ≤ 9,000, S017 ≤ 20,000). Split orders are modelled explicitly (fast partial + later leg). | Admin point 2. No single fast supplier covers the 24,000-unit at-risk PO. |
| C-2 | Deadline = received by **end of 2026-11-12** for the first leg (Logix Stock). Each later leg's deadline is recomputed from the stock already received (last day closing ≥ safety stock 2,270); e.g. after 9,000 units land on 11-10 → end of 11-16. Checked on **planned and worst-case** dates. | Admin point 3. 11-14 is a line stop; 11-13 eats safety stock. Same rule as Logix Stock's split-order table. |
| C-3 | Total recovery cost = component purchase (qty × ex-works unit price) + transport, shown separately per leg and per option, plus the premium vs. the original PO price (€14.20). | Admin point 4. |
| C-4 | Assumption: a part-load leg (e.g. 15,000 units) is charged the full booking quote from logistics_v2 (conservative). The at-risk PO is treated as replaced, not additional. | Avoids under-stating cost; avoids double-counting stock. |

All figures SIMULATED. Nothing ordered or booked; any action needs explicit human approval.

## Logix Stock — inventory (Admin correction #3: conservative stock-out deadline)
- **Files:** new `inventory_simulated_v2.csv` + `README_inventory_simulated_v2.md`. `inventory_simulated.csv` and its README are unchanged.
- **Change:** added columns *Stock at end of 2026-11-12*, *Safety stock breach*, *Stock-out (no replenishment)*, *Latest safe delivery (received at plant)*, *Deadline rule*. No v1 values changed.
- **Latest safe delivery for COMP-ES-204: received at SIM-PLANT-01 by 2026-11-12 23:59.**
- **Why:** v1 only gave the stock-out (during 11-14), so plans treated an 11-14 arrival as acceptable. Stock ends 11-12 at 3,600 units (above the 2,270 safety stock) but crosses safety stock during 11-13, so 11-12 is the last day a delivery keeps the buffer intact.
- **Split orders:** next safe deadline after a partial delivery = end of day before stock would cross safety stock again (9,000 units received by 11-12 → 11-16; 20,000 → 11-20; 24,000 → 11-22; 29,000 → 11-24). Table in the v2 README.
