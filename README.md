# LOGIX – Autonomous Logistics Intelligence

LOGIX is a multi-agent AI system built with Switch and Claude Code to analyse supply-chain disruptions and recommend recovery strategies.

## Problem

A simulated automotive supply-chain shipment containing 24,000 critical electronic sensors is delayed by 10 days. The disruption creates inventory shortages and potential production risks.

## Architecture

LOGIX uses four specialised AI agents:

| Agent | Responsibility |
|---|---|
| Logix Command | Coordinates agents and consolidates recovery plans |
| Logix Source | Analyses suppliers, availability, prices and lead times |
| Logix Stock | Evaluates inventory, consumption and stock-out risks |
| Logix Route | Compares transport options, costs and delivery estimates |

## Technology Stack

- Switch – Multi-agent orchestration
- Claude Code – AI agent execution
- Mattermost – Agent collaboration and communication
- Python – Scenario calculations
- CSV – Simulated supply-chain data

## Workflow

1. Report a supply-chain disruption to Logix Command.
2. Delegate analysis to the three specialist agents.
3. Analyse alternative suppliers and inventory risks.
4. Compare transportation options.
5. Consolidate findings into a recovery recommendation.
6. Request human approval before any operational action.

## Project Structure

```text
LOGIX/
├── README.md
├── data/
│   ├── suppliers_simulated_v2.csv
│   ├── inventory_simulated_v2.csv
│   ├── logistics_simulated_v2.csv
│   └── additional incident datasets
└── docs/
    ├── RECOVERY_PLAN_SHIP-2026-1107-01_simulated.md
    ├── CORRECTIONS_simulated.md
    └── dataset documentation
```

## Setup

1. Install Switch and configure Claude Code as the agent provider.
2. Create the four LOGIX agents.
3. Configure Mattermost integration.
4. Create a shared `supply-chain-control-tower` channel.
5. Add the simulated datasets to the shared project folder.
6. Trigger a simulated supply-chain incident through Logix Command.

See the documentation in the `docs/` directory for dataset details and the recovery scenario.

## Safety

All data and incidents are simulated. LOGIX does not contact real suppliers, place orders, modify actual inventory or book transportation. Human approval is required before operational actions.

## Goal

Demonstrate how specialised AI agents can collaborate to analyse supply-chain disruptions and support faster, informed human decision-making.