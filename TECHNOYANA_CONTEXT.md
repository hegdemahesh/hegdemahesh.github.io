# Technoyana Ecosystem & Product Architecture Context

> **Official Entity**: Technoyana Digital Transformation Services Private Limited (Est. 2021)  
> **Founder & CTO**: Maheshchandra Hegde  
> **Core Focus**: Enterprise Product Engineering, Spatial AI & High-Reliability Sports SaaS Studio  
> **Primary Website**: [technoyana.in](https://technoyana.in/)

---

## 1. Company Overview & Divisions

Technoyana acts as both an enterprise product engineering incubator and the core powerhouse behind specialized technology ventures:

### Flagship Divisions:
1. **Twitan ([twitan.com](https://twitan.com)) — Sports SaaS Studio**
   - High-reliability operational software for tournament directors, sports clubs, academies, and live match scoring.
   - **Shutlify (Badminton OS)**: Operational operating system for badminton tournaments — automated bracket generators (single/double elimination, round-robin, league stages), live court arbitration/scoring, multi-court schedule engines, and venue-ready offline-first PWAs.
   - **Twicket**: High-fidelity live scoring and statistical engine for cricket tournaments.

2. **Srushtilabs ([srushtilabs.com](https://srushtilabs.com)) — Spatial AI & 3D Tech**
   - **Voxelforge AI**: AI-assisted generative 3D asset workflows producing game-ready, low-poly modular assets for Unreal Engine, Unity, and WebGL.
   - **ayam3d**: Exploratory R&D in generative 3D mesh synthesis, automated retopology, and PBR textures.

---

## 2. Brand Identity & Design System Tokens

When building or styling products powered by **Technoyana**, adhere to the following design tokens:

### Brand Colors:
- **Primary Brand Blue**: `#0070ba` (Technoyana Deep Wing Blue)
- **Secondary Brand Cyan**: `#38bdf8` (Technoyana Bright Facet Cyan)
- **Primary Action Blue**: `#0284c7` / Hover: `#0369a1`
- **Dark Neutral (Headings & Shell)**: `#0f172a` / `#090d16`
- **Light Neutral (Surface & Cards)**: `#ffffff` / `#f8fafc` / `#f1f5f9`
- **Line / Border Subtle**: `#e2e8f0` / `#cbd5e1`
- **Accent Emerald (Live State / Active Status)**: `#059669` / Light: `#ecfdf5`

### Typography:
- **Headings**: `Sora`, -apple-system, BlinkMacSystemFont, sans-serif
- **Body**: `Instrument Sans`, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif
- **Tech / Badges / Numbers**: `Space Grotesk`, monospace, sans-serif

### Official Vector Logo Component:
Available in the workspace at [`src/TechnoyanaLogo.jsx`](file:///c:/Users/Mahesh/Documents/GitHub/hegdemahesh.github.io/src/TechnoyanaLogo.jsx):
- ViewBox: `0 0 342.44016 66.925781`
- Features the geometric blue wing (`#0070ba`) with cyan facet (`#38bdf8`) alongside the customized geometric typographic wordmark.
- Can be rendered with custom height and text colors (`#0f172a` for light mode, `#ffffff` for dark mode).

---

## 3. "Powered by Technoyana" Branding Guidelines

For sub-products, client applications, and sponsored tournament engines (such as **HBL Sirsi**):

1. **Header / Topbar Badge**:
   - Accompany product branding with:
     ```html
     <span class="powered-by">Powered by <strong>Technoyana</strong></span>
     ```
   - Or include the `TechnoyanaLogo` component at a compact height (`18px` – `22px`).

2. **Footer Attribution**:
   - Standard format:
     ```html
     <footer>
       <p>© 2026 HBL Sirsi. Engineered & Powered by Technoyana Digital Transformation Services Pvt. Ltd.</p>
       <a href="https://technoyana.in" target="_blank" rel="noopener noreferrer">technoyana.in</a>
       ·
       <a href="https://twitan.com" target="_blank" rel="noopener noreferrer">twitan.com (Sports OS)</a>
     </footer>
     ```

---

## 4. Project Context: HBL Sirsi (Badminton Tournament Management)

### Tournament Context:
- **Event**: **HBL Sirsi** (Badminton Tournament held in Sirsi, Uttara Kannada, Karnataka).
- **Domain**: Badminton Tournament Operations, Player Management, Match Scheduling & Live Court Scoring.
- **Platform Base**: Powered by **Technoyana** & **Twitan's Shutlify** architectural patterns.

### Core Tournament Management Workflows:
1. **Fixture & Bracket Generation**:
   - Knockout brackets (Round of 64, 32, 16, Quarter-Finals, Semi-Finals, Finals).
   - Round-robin group stages leading into knockout brackets.
   - Seeded player placements and automatic bye calculations.
2. **Court Management & Scheduling**:
   - Multi-court allocation (e.g., Court 1, Court 2, Court 3).
   - Match queue management (Live on Court, On Deck / Next Up, Completed).
   - Estimated start times and match duration tracking.
3. **Umpire / Referee Live Scoring Interface**:
   - Large, high-visibility touch-friendly tap targets for rapid score logging courtside.
   - Badminton rules engine (BWF rally point system: 21 points, deuce to 30, service over, side changes at 11 and game intervals).
   - Undo last point / fault corrections.
   - Real-time sync to public spectator dashboards.
4. **Spectator & Player Views**:
   - Mobile-first live scoreboard.
   - Player profiles, match histories, and tournament leaderboard.
5. **Critical Venue Resilience Requirement (Offline-First)**:
   - Badminton courts often suffer from spotty or fluctuating indoor Wi-Fi / mobile networks.
   - Match scoring must never fail or lose state during network drops.
   - Utilize local state persistence (IndexedDB / LocalStorage) with automatic synchronization when back online.

---

## 5. Architectural Standards for HBL Sirsi & Technoyana Apps

1. **Frontend**: React / Vite / TypeScript or JavaScript with clean semantic HTML.
2. **Performance**: Fast initial load, lightweight bundles, zero layout shift (CLS).
3. **Accessibility (WCAG 2.1 AA)**: High-contrast score readouts, visible focus states, and aria-labels for court status.
4. **State Management**: Robust local fallback with optimistic UI updates.
