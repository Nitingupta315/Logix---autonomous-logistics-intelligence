# SIMULATED supplier dataset v2 — LOGIX (not real data)

**File:** `suppliers_simulated_v2.csv` (corrected copy of `suppliers_simulated.csv`, which is kept unchanged)
**Status:** ⚠️ SIMULATED / FICTIONAL. Created by Logix Source (LOGIX – Autonomous Logistics Intelligence) for the SupplyChain AI demo. All supplier names, IDs, prices, quantities, lead times and scores are invented. No real supplier has been contacted and no order has been placed. Changes from v1 are logged in `CORRECTIONS_simulated.md`.

## Lead-time definition (agreed LOGIX standard)
- **Supplier lead time** = order placement → goods **ready to ship at the supplier's dock**. It does **not** include transport.
- **Delivered time** = supplier lead time + transit time (transit comes from `logistics_simulated*.csv`).
- The v1 README described lead time as "order to delivery at the German plant". That was wrong: the logistics data adds transit on top, so transport would have been counted twice. The numbers themselves are unchanged; only the definition is corrected.

## Columns
| Column | Meaning |
|---|---|
| Data label | Always `SIMULATED` |
| Supplier ID | Fictional ID (`SIM-` prefix) |
| Supplier name | Fictional German/European automotive supplier |
| Component ID | `COMP-` ID; joins with the inventory and logistics files |
| Component | Component type |
| Component availability | `Available`, `Limited` or `Disrupted` |
| Max order quantity (units) | Hard cap on what can be ordered from this supplier now (was "Available quantity") |
| Unit price (€) | Per unit, EUR, ex works: excludes freight, duties and expediting |
| Supplier lead time to ready-to-ship (days) | See definition above |
| Earliest ready-to-ship date (if ordered 2026-11-07) | 2026-11-07 (inventory snapshot date) + lead time. Assumes the order is placed today |
| Reliability score | 0–1, simulated on-time-in-full history |
| Location | City, country |
| Covers 24,000-unit PO alone | COMP-ES-204 only: whether max quantity ≥ the 24,000-unit at-risk PO. `n/a` for other components |

## Component ID mapping (unchanged from v1)
COMP-BC-201 brake caliper · COMP-WH-202 wiring harness · COMP-MC-203 MCU · COMP-ES-204 Automotive Electronic Sensors · COMP-BM-205 battery cell module · COMP-SF-206 seat frame

## COMP-ES-204: quantity constraints and split orders
| Supplier | Max qty | Unit € | Ready to ship | Alone covers 24k? |
|---|---|---|---|---|
| SIM-S016 Amberg DE | 9,000 | 19.80 | 2026-11-10 | No |
| SIM-S017 Innsbruck AT | 20,000 | 16.90 | 2026-11-12 | No |
| SIM-S018 Wrocław PL | 35,000 | 14.60 | 2026-11-14 | Yes |
| SIM-S019 Enschede NL | 28,000 | 15.30 | 2026-11-16 | Yes |
| SIM-S020 Arad RO | 60,000 | 12.40 | 2026-11-22 | Yes |

- No single fast supplier can cover 24,000 units. SIM-S016 + SIM-S017 together can supply up to 29,000.
- Example split (simulated, purchase cost only): 9,000 × €19.80 from S016 + 15,000 × €16.90 from S017 = €178,200 + €253,500 = **€431,700**. Transport is added separately from the logistics data.
- SIM-S018 to S020 only become ready to ship on or after 2026-11-14, so they cannot meet a deadline earlier than that. They are only useful as a larger follow-up delivery.
