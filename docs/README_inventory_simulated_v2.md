# SIMULATED inventory dataset v2 — LOGIX (not real data)

**File:** `inventory_simulated_v2.csv` (supersedes nothing; `inventory_simulated.csv` is kept unchanged)
**Status:** ⚠️ SIMULATED / FICTIONAL. Created by Logix Stock. Not an ERP extract; no real inventory read or modified.

v2 = v1 columns unchanged + five new columns that fix the **latest safe delivery date** for COMP-ES-204 (Admin correction #3). See `CORRECTIONS_simulated.md`.

## Daily projection, no replenishment (2,400 units/day, 7-day production)
| Date | Start of day | End of day | vs safety stock (2,270) |
|---|---|---|---|
| 11-07 | 18,000 | 15,600 | above |
| 11-08 | 15,600 | 13,200 | above |
| 11-09 | 13,200 | 10,800 | above |
| 11-10 | 10,800 | 8,400 | above |
| 11-11 | 8,400 | 6,000 | above |
| 11-12 | 6,000 | **3,600** | above — last safe day |
| 11-13 | 3,600 | 1,200 | **breached** after (3,600 − 2,270) ÷ 2,400 ≈ 0.55 day |
| 11-14 | 1,200 | 0 | **stock-out** after 0.5 day |

## Latest safe delivery: received at the plant by 2026-11-12 23:59
- Delivery on 11-14 is too late (stock-out that day). Delivery on 11-13 means consuming safety stock before the goods are booked in, leaving no buffer for demand variability or a late truck.
- "Delivered" = received at SIM-PLANT-01 and available to production. Transport ETAs must therefore be ≤ 2026-11-12.

## Deadline for a second (split) delivery
Each 2,400 units received moves the next safe deadline out by one day. Rule: next deadline = end of day before stock would cross safety stock.
| Received by end of 11-12 | Stock end 11-12 | Next safety-stock breach | Next latest safe delivery |
|---|---|---|---|
| 9,000 (e.g. SIM-S016 max) | 12,600 | during 11-17 | 2026-11-16 23:59 |
| 20,000 (e.g. SIM-S017 max) | 23,600 | during 11-21 | 2026-11-20 23:59 |
| 24,000 (full at-risk PO qty) | 27,600 | during 11-23 | 2026-11-22 23:59 |
| 29,000 (S016 + S017) | 32,600 | during 11-25 | 2026-11-24 23:59 |
