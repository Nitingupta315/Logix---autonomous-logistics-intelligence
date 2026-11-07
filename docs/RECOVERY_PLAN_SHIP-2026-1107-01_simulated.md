# SIMULATED recovery plan: COMP-ES-204 / SHIP-2026-1107-01 (Logix Command, 2026-11-07)
Status: RECOMMENDATION ONLY. Awaiting Admin approval. Nothing ordered or booked.
Inputs: suppliers_simulated_v2.csv, inventory_simulated_v2.csv, logistics_simulated_v2.csv, inventory_scenarios_SHIP-2026-1107-01_simulated.csv, plus specialist reports from Logix Source, Logix Stock and Logix Route.

Deadlines: first delivery received by end of 11-12; once 9,000 units are in, the next is due by end of 11-16 (Logix Stock).

| Option | Legs | Components € | Transport € | Total € | Planned / worst | Slack (leg 1 / leg 2) | Notes |
|---|---|---|---|---|---|---|---|
| G Admin proposal | S016 9k RT-02 + S017 15k RT-04 | 431,700 | 2,990 | 434,690 | 11-11 & 11-12 / 11-12 & 11-13 | 0 d / 3 d | Leg 1 zero slack |
| **A Recommended** | S016 9k RT-01 + S017 15k RT-04 | 431,700 | 3,380 | **435,080** | 11-10 & 11-12 / 11-11 & 11-13 | 1 d / 3 d | Van is an independent path to 11-12 |
| B | S016 9k RT-01 + S017 15k RT-03 | 431,700 | 1,960 | 433,660 | 11-10 & 11-13 / 11-11 & 11-14 | 1 d / 2 d | No fallback by 11-12 if S016 fails |
| C | S016 9k RT-01 + S018 15k RT-05 | 397,200 | 2,730 | 399,930 | 11-10 & 11-15 / 11-11 & 11-16 | 1 d / 0 d | S018 reliability 0.78 |
| Not feasible | S019 (11-17), S020 (11-23+), S018 air (11-14), S017 only (4k short) | | | | | | |

Assumptions: the new order replaces the at-risk PO; the van leg is priced at 4 vans; probabilities treat suppliers and routes as independent and are indicative only; longer-slip rates are a Logix Route assumption; 4 sensors per vehicle (Logix Stock).
