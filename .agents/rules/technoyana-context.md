---
description: Context, brand system, and architectural guidelines for Technoyana, Twitan (Shutlify), and HBL Sirsi Badminton Tournament Management
---

# Technoyana & HBL Sirsi Context

## Entity & Leadership
- **Company**: Technoyana Digital Transformation Services Private Limited (Est. 2021)
- **Founder & CTO**: Maheshchandra Hegde
- **Core Website**: https://technoyana.in/
- **Sports SaaS Division**: Twitan (https://twitan.com), developer of **Shutlify (Badminton OS)** and **Twicket**.

## Brand System
- **Colors**:
  - Primary Blue: `#0070ba`
  - Secondary Cyan: `#38bdf8`
  - Dark Neutral: `#0f172a` / `#090d16`
  - Accent Emerald (Live/Active): `#059669`
- **Typography**: `Sora` (Headings), `Instrument Sans` (Body), `Space Grotesk` (Tech/Metrics).
- **Logo Component**: `TechnoyanaLogo.jsx` with SVG paths, customizable height and color.
- **Attribution**: "Powered by Technoyana" badge or footer attribution with link to `https://technoyana.in/`.

## Target Project: HBL Sirsi (Badminton Tournament Management)
- **Purpose**: Operational software for the HBL Sirsi badminton tournament held in Sirsi, Karnataka.
- **Powered by**: Technoyana / Twitan Shutlify architecture.
- **Key Modules**:
  1. Automated bracket & fixture generators (single/double elimination, round-robin).
  2. Multi-court scheduling, match queues, and real-time court allocation.
  3. Umpire/referee court scoring interface (BWF 21-point rules, service indicators, undo point).
  4. Public spectator live scoreboard and player leaderboard.
  5. Venue-ready offline-first PWA resilience (local caching for spotty stadium Wi-Fi).
