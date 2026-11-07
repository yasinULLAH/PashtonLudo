# 🎲 Bannu Royale Ludo & Khyber Saanp Seedhi Pro
### Authentic Pashtun Cultural Rules, 2-Dice Mechanics, Multi-Mouse Hardware Lock & KPK Hujra Board Gaming Suite
**Developer:** Yasin Ullah — Bannu Software Solutions  
**Contact:** WhatsApp: `0336-1593533` | [LinkedIn Profile](https://www.linkedin.com/in/yasin-ullah-029229232/)  
**Edition:** v5.0 Master Production Suite (PWA Offline Enabled)

---

## 📌 Table of Contents / فہرست مضامین
1. [English Documentation](#-english-documentation)
   - [Project Overview](#1-project-overview)
   - [Core Architecture & Technology Stack](#2-core-architecture--technology-stack)
   - [Bannu Royale Ludo (`index.html`) — Deep Dive](#3-bannu-royale-ludo-indexhtml--deep-dive)
     - [All 26 Cultural & Tournament Rules Detailed](#all-26-cultural--tournament-rules-detailed)
     - [Multi-Mouse Hardware Lock (2 to 4 Mice)](#multi-mouse-hardware-lock-2-to-4-mice)
     - [7 Match Formats & 7 Cultural Drills](#7-match-formats--7-cultural-drills)
     - [Single-Click Preview vs Second-Click Execution](#single-click-preview-vs-second-click-execution)
     - [Crash Recovery & Unfinished Match Engine](#crash-recovery--unfinished-match-engine)
     - [HD Stats Picture Card & Referee Log](#hd-stats-picture-card--referee-log)
   - [Khyber Saanp Seedhi Pro (`snakes.html`) — Deep Dive](#4-khyber-saanp-seedhi-pro-snakeshtml--deep-dive)
     - [Authentic KPK Hujra Rules](#authentic-kpk-hujra-rules)
     - [Multi-Beads System (1 to 4 Beads Per Player)](#multi-beads-system-1-to-4-beads-per-player)
     - [Tactical Hazard & Takkar Radar](#tactical-hazard--takkar-radar)
     - [Manual On-Board Snake & Bite Editor](#manual-on-board-snake--bite-editor)
     - [Idle Auto-Roll, Remembered Automation & AFK Bot Takeover](#idle-auto-roll-remembered-automation--afk-bot-takeover)
     - [Hall of Fame & Players Directory CRUD (IndexedDB)](#hall-of-fame--players-directory-crud-indexeddb)
     - [AES-GCM 256-bit Encrypted Backup Vault](#aes-gcm-256-bit-encrypted-backup-vault)
     - [Dynamic DB-Backed User Theme Engine](#dynamic-db-backed-user-theme-engine)
   - [Multiplayer & Networking (WebRTC, QR Code & LAN Radar)](#5-multiplayer--networking-webrtc-qr-code--lan-radar)
   - [Audio Synthesizer & Procedural Sound Effects](#6-audio-synthesizer--procedural-sound-effects)
   - [Progressive Web App (PWA) Offline Engine](#7-progressive-web-app-pwa-offline-engine)
   - [Installation, Deployment & Browser Support](#8-installation-deployment--browser-support)
2. [اردو زبان میں مکمل دستاویزات (Urdu Documentation)](#-اردو-زبان-میں-مکمل-دستاویزات-urdu-documentation)
   - [ایپ کا تعارف اور پس منظر](#1-ایپ-کا-تعارف-اور-پس-منظر)
   - [بنوں رائل لڈو کے تمام 26 روایتی قوانین کی مکمل وضاحت](#2-بنوں-رائل-لڈو-کے-تمام-26-روایتی-قوانین-کی-مکمل-وضاحت)
   - [ملٹی ماؤس ہارڈویئر لاک (ایک لیپ ٹاپ پر 2 سے 4 ماؤس)](#3-ملٹی-ماؤس-ہارڈویئر-لاک-ایک-لیپ-ٹاپ-پر-2-سے-4-ماؤس)
   - [خیبر سانپ سیڑھی پرو کے روایتی قوانین و فیچرز](#4-خیبر-سانپ-سیڑھی-پرو-کے-روایتی-قوانین-و-فیچرز)
   - [کھلاڑیوں کا ریکارڈ، ہال آف فیم اور پرنٹ ایبل اسناد](#5-کھلاڑیوں-کا-ریکارڈ-ہال-آف-فیم-اور-پرنٹ-ایبل-اسناد)
   - [بغیر انٹرنیٹ اور وائی فائی ملٹی پلیئر کھیلنے کا طریقہ](#6-بغیر-انٹرنیٹ-اور-وائی-فائی-ملٹی-پلیئر-کھیلنے-کا-طریقہ)

---

# 🇬🇧 English Documentation

## 1. Project Overview
**Bannu Royale Ludo & Khyber Saanp Seedhi Pro** is a world-class cultural board gaming suite developed by **Yasin Ullah (Bannu Software Solutions)**. The suite preserves and digitalizes the centuries-old traditional Hujra board gaming rules of Khyber Pakhtunkhwa (KPK), Pakistan—specifically the historic 2-Dice tactical Ludo played in Bannu, Lakki Marwat, Peshawar, Mardan, and Swat, along with Pashtun Snake and Ladder (Khyber Saanp Seedhi).

The project is structured as a dual-game Progressive Web Application (PWA) that runs 100% client-side in any modern web browser with zero server latency, complete offline readiness, multi-pointer hardware support, WebRTC peer-to-peer networking, and bank-grade cryptographic data vaults.

---

## 2. Core Architecture & Technology Stack

| Layer | Technologies & Libraries | Architectural Purpose |
|---|---|---|
| **Render Engine** | HTML5 Canvas 2D API (`index.html`) & Dynamic CSS Grid 10x10 (`snakes.html`) | 60 FPS distraction-free hardware-accelerated board rendering, custom token geometry, breadcrumb hop trails, and realistic snake anatomy. |
| **Styling & Theme** | Tailwind CSS 3.4.17, Animate.css, CSS Custom Properties (`--main-bg`, `--accent-primary`) | Responsive layouts, mobile React Native Android app styling, tactile active-press feedback, and user-customizable UI theme engine. |
| **State & Database** | IndexedDB (`KhyberSaanpSeedhiDB_v1`), HTML5 LocalStorage | Persistent multi-store database for users, players, matches, custom presets, settings, and instant crash recovery snapshots. |
| **Cryptographic Security** | Web Crypto API (`SubtleCrypto`), PBKDF2 (SHA-256, 100k rounds), AES-GCM 256-bit | Authenticated client-side encryption of career vaults and exported JSON backups with random 16-byte salt and 12-byte IV. |
| **Multi-Touch & Hardware** | Pointer Events API (`pointerdown`, `pointermove`, `pointerup`), `event.pointerId` | Multi-touch drag-and-drop, gesture support, and Multi-Mouse hardware pointer lock (2 to 4 separate USB/wireless mice). |
| **Peer-to-Peer Networking** | PeerJS 1.5.2/1.5.4, Native `RTCPeerConnection`, `RTCDataChannel`, BroadcastChannel | Zero-server device-to-device multiplayer: Wi-Fi LAN Radar, PeerJS room codes, and serverless WebRTC SDP QR code handshakes. |
| **Vision & QR Scanning** | `QRCode.js`, `Html5Qrcode` (2.3.8), `jsQR` (1.4.0) | High-speed QR code generation and real-time camera/image scanner for zero-typing WebRTC room pairing. |
| **Audio Synthesis** | Web Audio API (`AudioContext`, `OscillatorNode`, `GainNode`) | Zero-asset procedural sound effects (hops, dice rattles, kills, victory fanfare) and a live traditional Pashtun Rabab background synth loop. |
| **Data Tables & Export** | jQuery 3.7.1, DataTables 1.13.8, PDFMake, JSZip, Buttons HTML5 | Searchable, paginated, responsive player directories and match archives with 1-click export to PDF, Excel, CSV, and Print. |
| **Offline PWA** | Workbox 7.0.0, Service Worker (`sw.js`), Web App Manifest (`manifest.json`) | Complete offline caching of all assets, standalone home-screen installation on Android/iOS/Windows, and offline fallback. |

---

## 3. Bannu Royale Ludo (`index.html`) — Deep Dive

Bannu Royale Ludo is a full simulation of the authentic Pashtun 2-Dice Ludo ruleset alongside international 1-Die Yalla rules. It operates on an adaptive full-bleed 15x15 board canvas that fills 100% of the screen without empty borders or page scrolling.

### All 26 Cultural & Tournament Rules Detailed

1. **Two-Dice Tactical Play vs 1-Die Classic (`diceCount: 2 | 1`)**
   - **Mechanism:** Players roll two 6-sided dice simultaneously.
   - **Effect:** Numbers can be split across two different beads or combined into a single sum hop on one bead. In 1-Die mode, classic single-die rolling applies.
2. **Must Use 1 Die When Only 1 Bead Remains on Board (`oneDieWhenOneBeadLeft: true`)**
   - **Mechanism:** As soon as 3 beads reach Home and only 1 bead remains on the board, rolling automatically switches from 2 Dice to 1 Die.
   - **Guardrail:** Even if disabled, the engine automatically switches to 1 Die once the bead enters the Home column or reaches the final square needing 1 step, ensuring no bead ever gets mathematically trapped.
3. **Close Game vs Open Game Capture Lock (`closeGameMode: true`)**
   - **Mechanism:** Capturing an enemy bead on Die 1 locks (🔒) that capturing bead on the kill square for the remainder of that turn if any other bead can legally move.
   - **Effect:** Prevents "hit-and-run" tactics. In Open Game, capturing beads can immediately run away on Die 2.
4. **Bonus Re-Roll on Kill / Capture (`bonusRollOnKill: true`)**
   - **Mechanism:** Capturing any opponent bead awards a bonus dice re-roll once the current dice are spent.
   - **Effect:** Rewards offensive strategies and momentum shifts.
5. **Mandatory Hand / Yard Spawn on 6 (`mandatoryYardSpawn: true`)**
   - **Mechanism:** If a player rolls a 6 while unplaced beads remain in the hand/yard, the engine forces spawning a bead onto the starting square before moving ground beads.
   - **Auto-Placement:** Includes single-click automatic placement of the pocket bead on 6.
6. **Blood Gate: 1 Kill Required for Home Entry + Outer Loop (`killRequiredForHome: true`)**
   - **Mechanism:** A player's Home column gate stays locked (🔒) until that player captures at least 1 enemy bead.
   - **Effect:** Reaching the Home gate with 0 kills forces the bead to bypass the gate and complete another full 52-square outer lap!
7. **Two Kills Required for Home Entry (`twoKillsForHome: false`)**
   - **Mechanism:** Upgrades the blood-gate threshold from 1 kill to 2 kills before Home unlocks.
8. **Strict Near-Home Remainder Rule (`strictHomeRemainder: true`)**
   - **Mechanism:** Near Home, a player cannot play one die into Home if the second die (the remainder) cannot be legally consumed by any bead on the board.
   - **Effect:** Prevents wasting leftover dice numbers. If both numbers cannot be legally consumed without overshooting, the move is withheld.
9. **Three Consecutive Sixes Penalty (`threeConsecutiveSixesPenalty: false`)**
   - **Mechanism:** Rolling three consecutive 6s (in 1-Die) or three consecutive 6+6s (in 2-Dice) cancels the turn and passes the dice to the next player.
10. **Single Six Re-Roll in 2-Dice Mode (`singleSixBonusInTwoDice: false`)**
    - **Mechanism:** In traditional 2-Dice Ludo, only Double Six (6+6) grants a bonus roll. Enabling this grants a re-roll even if only one die is a 6 (e.g., 6+2, 6+4).
11. **Stack Roll / Accumulate Sixes Before Moving (`stackRollBeforeMoving: false`)**
    - **Mechanism:** Queues bonus rolls into an on-screen Stack Bar before executing moves.
    - **Mid-Turn Kill Bonus Integration:** If you kill an enemy with Die 1, your remaining die stays stacked while you immediately roll your Kill Bonus re-roll, allowing all numbers to be planned together!
12. **Spawn on 1 as well as 6 (`spawnOnOneAndSix: false`)**
    - **Mechanism:** Allows bringing beads out of hand on either a 1 or a 6.
13. **Double-Six Spawns Two Beads (`doubleSixSpawnsTwoBeads: false`)**
    - **Mechanism:** Rolling 6+6 with 2+ beads in hand forces bringing two separate beads out onto the starting square simultaneously.
14. **First Bead Starts Already on Board (`firstBeadStartsOnBoard: false`)**
    - **Mechanism:** Players begin the match with 1, 2, 3, or 4 beads already deployed on their starting square, starting immediate action without waiting for a 6.
15. **Pair Blockade / Jora Wall Rule (`pairBlockadeRule: false`)**
    - **Mechanism:** Two beads of the same player (or 2v2 team) on the same square form a "🧱 JORA" wall. Rival beads cannot jump over this square until the blockade breaks.
16. **Kill All Stacked Enemies on One Square (`killAllStackedEnemies: false`)**
    - **Mechanism:** Landing on stacked opponent beads captures every enemy bead on that square simultaneously (+N kills). When OFF, the traditional popup allows selecting which single bead to capture.
17. **Mandatory Capture / Must Kill if Possible (`mandatoryCapture: false`)**
    - **Mechanism:** If any legal move captures an enemy bead, peaceful moves are disallowed and the player must execute the capture ("Phoonk" rule).
18. **Optional Outer Loop After Kill (`allowOptionalLoopAfterKill: false`)**
    - **Mechanism:** Players who have completed their kill requirement can choose between entering Home or looping around the outer board again to hunt more enemies.
19. **No-Kill Gate Wait Until All Ground Beads Gather (`waitAllGroundAtGateBeforeLoop: false`)**
    - **Mechanism:** A 0-kill bead reaching the Home gate must wait until all other active ground beads of that player arrive at the gate before beginning another lap.
20. **2v2 Opposite-Corner Teams & Safe Partner Stacking (`teamMode: true`)**
    - **Mechanism:** Red + Yellow (♦Team 1) compete against Green + Blue (★Team 2). Teammates never capture each other, can stack safely, and win when all 8 team beads reach Home.
21. **Teammate Assist Requires Rolling a 1-Die Six First (`teamAssistRequiresSix: true`)**
    - **Mechanism:** After completing all your beads in 2v2, you must roll 1 Die on your turn until you roll a 6. Once rolled, Partner Assist unlocks and you gain 2-Dice control of your partner's beads!
22. **Bonus Re-Roll on Bead Home Completion (`bonusRollOnHome: true`)**
    - **Mechanism:** Moving any bead into the final center Home triangle awards a bonus dice re-roll.
23. **Bonus Re-Roll on 6 / Double 6 (`doubleSixBonusRoll: true`)**
    - **Mechanism:** Master switch for whether 6 (1-Die) or 6+6 (2-Dice) grants another turn.
24. **Star / Stop Square Safe Immunity (`safeStopImmunity: true`)**
    - **Mechanism:** All 8 Stop squares (4 colored start squares + 4 yellow Star stops at 8, 21, 34, 47) provide 100% immunity from enemy capture.
25. **3-Timeouts Auto-Bot Takeover & One-Tap Reclaim (`threeTimeoutsBotTakeover: true`)**
    - **Mechanism:** If a human player misses their turn timer 3 consecutive times, the smart AI Bot automatically takes over their seat. A pulsing "👤 Reclaim Seat" button allows reclaiming control instantly with a single tap.
26. **Multi-Mouse Per-Player Hardware Lock for 2 to 4 Mice (`multiMouseLock: false`)**
    - **Mechanism:** Tracks physical hardware mouse pointers via `event.pointerId`. Locks each seat to a specific physical mouse so only that mouse can roll or move on that player's turn!

---

### Multi-Mouse Hardware Lock (2 to 4 Mice)
The application includes a native hardware calibration system allowing up to 4 players to plug in 2, 3, or 4 USB/wireless mice into a single laptop and play without interfering with each other's turns.

- **How It Works:** Modern operating systems and browsers assign a unique `event.pointerId` when independent pointer injection is active.
- **Windows Setup:** Plug in 2–4 mice, install a multi-cursor driver utility (**TeamPlayer4** or **MouseMux**), enable native pointer injection, open the Multi-Mouse Calibration modal in the app, and click each player's colored target box with their respective mouse.
- **Linux Setup:** Built-in via native XInput! Run `xinput create-master Player2` and `xinput reattach <device_id> <master_id>`. Each physical mouse generates an independent cursor and `pointerId`.
- **Enforcement:** If Green tries to click the dice or move a bead during Red's turn, the hardware pointer ID is rejected with a warning banner: `⛔ Mouse Locked! Only Red (Mouse ID #X) can play!`.

---

### 7 Match Formats & 7 Cultural Drills
- **Match Formats:**
  1. `2v2_ai`: 2v2 Teams vs AI (Red + Yellow vs Green + Blue)
  2. `1v1_ai`: 1v1 Duel vs AI
  3. `4p_ai`: 4-Player Free-For-All vs AI
  4. `pass_2p`: 2 Players on 1 Screen (1v1)
  5. `pass_3p`: 3 Players on 1 Screen
  6. `pass_4p_ffa`: 4 Players Free-For-All on 1 Screen
  7. `pass_play`: 4 Players (2v2 Teams) on 1 Screen
- **Cultural Drills (Instant Board State Loader):**
  1. `mandatory_spawn`: 1 bead on ground, 3 in hand, rolls 6+2.
  2. `blood_loop`: Step 49 before Home Gate with 0 kills, rolls 4+2.
  3. `close_game_kill`: Enemy at square 7, moves +3 to capture, locks capturer, moves +4 on Bead #2, earns kill bonus!
  4. `team_stack_capture`: Enemy lands on square with Green & Blue stacked; triggers single-capture choice modal.
  5. `home_remainder`: 1 bead needing 6 for Home, rolls 5+4 (remainder 4 cannot fit; verifies move withholding).
  6. `teammate_assist`: Red finished all beads; tests rolling 1-Die 6 to unlock partner assist.
  7. `home_split_two_beads`: Bead #1 at gate (needs 6) and Bead #2 on track; rolls 5+4, moves 5 into Home and 4 on Bead #2!

---

### Single-Click Preview vs Second-Click Execution
- **First Click / Tap:** Highlights the bead and draws connected hop trails, target rings, and tactical outcome badges (`⚡ SPAWN`, `⚔️ KILL!`, `★ SAFE`, `🏠 HOME PATH`, `🔄 LOOP`) on the board.
- **Second Click / Drag:** Clicking the selected bead again or tapping any highlighted destination circle executes the move immediately.
- **Auto-Placement on 6:** When a 6 is rolled and unplaced beads exist in the yard, the engine automatically places the pocket bead onto the start square without manual dragging!

---

### Crash Recovery & Unfinished Match Engine
Every move, dice roll, and turn state is saved into `localStorage` (`bannu_ludo_saved_match_v1`). If the browser closes, crashes, or refreshes mid-match, an alert banner appears on the Home screen:
> **🔄 Unfinished Match Saved** — Click *Resume Match* to restore the exact board state, turn, and dice pool seamlessly!

---

### HD Stats Picture Card & Referee Log
- **HD Stats Picture Card:** Generates a 600x380 canvas graphic displaying player name, rank, win rate, matches won, enemy kills, double sixes, and team wins. Downloadable as a high-resolution `.PNG` image.
- **Referee Log:** A slide-over modal recording timestamped, color-coded records of every dice roll, hop, capture, lock, and rule enforcement.
- **Crown Cheat System:** Tapping the center board crown (👑) 5 times within 1.8 seconds opens a secret authentication modal (Password: `yasin123`) allowing developers/testers to set upcoming dice rolls (e.g. `6,6`).

---

## 4. Khyber Saanp Seedhi Pro (`snakes.html`) — Deep Dive

Khyber Saanp Seedhi Pro (v4.0 Pro Edition) is an authentic KPK Hujra simulation of Snake and Ladder with rich Pashtun regulations, realistic anatomical SVG snakes, and full IndexedDB player management.

### Authentic KPK Hujra Rules
- **Chakka (6) Dakhila:** Beads wait in Hujra Camp (Square 0) and require rolling a **6 (Chakka)** to enter Square 1.
- **Teen Chakkay Barsi (3x6 Burn):** Rolling three consecutive 6s (6-6-6) cancels the turn and returns the bead to its turn-start position.
- **KPK Takkar (Knockback Cut):** Landing on an opponent's square knocks their bead back to Square 1! In multi-bead mode, cutting an enemy also awards a bonus roll.
- **Hujra Safe Zones:** Squares **1, 14, 27, 50, 75, and 92** are designated safe sanctuaries where beads cannot be cut.
- **Square 99 Kalamar (Giant Black Cobra):** The legendary Kalamar cobra bites at Square 99 and drops beads all the way down to Square 4!
- **Pura 100 Finish:** Players must land on Square 100 by exact count. Overshooting rolls are forfeited.

---

### Multi-Beads System (1 to 4 Beads Per Player)
Supports 1 Bead (Classic Default), 2 Beads (Jora Pair), 3 Beads (Toli), or 4 Beads (Full Hujra Ludo-Style):
- Each bead requires a 6 to enter from Camp.
- Friendly beads can stack safely on any square.
- Takkar cuts award a bonus re-roll.
- When multiple beads have legal moves, an interactive bottom selector allows choosing which bead to advance.
- All beads must reach Square 100 to claim victory.

---

### Tactical Hazard & Takkar Radar
When Radar Assist is enabled, target squares are highlighted with colored halos:
- **Green (`radar-good`):** Safe landing, ladder climb, or winning goal.
- **Red (`radar-danger`):** Snake bite square.
- **Amber (`radar-cut`):** Enemy bead available for Takkar knockback.
- **Blue (`radar-step`):** Standard neutral step.

---

### Manual On-Board Snake & Bite Editor
Allows customizing snake and ladder locations for any match:
- **Visual Board Clicker:** Select the Snake tool, click Square 97 (head), then click Square 12 (tail) to create a custom snake instantly!
- **Manual Coordinate Input:** Head (2–99) to Tail (1–98) inputs.
- **Snake Visual Scaler:** 4 size options:
  - Ultra-Slim (0.42) — Maximizes square number visibility.
  - Slim & Clear (0.55) — Recommended default.
  - Medium Classic (0.72)
  - Bold Cobra (0.90)
- **Anatomical SVG Rendering:** Procedural scales, snake eyes, fangs, split tongue, drop shadows, and linear gradients.

---

### Idle Auto-Roll, Remembered Automation & AFK Bot Takeover
- **Auto-Roll Dice (Remembered):** Automatically rolls on your turn and persists across sessions.
- **Idle Auto-Roll:** Configurable timer (5s, 8s, 10s, 15s, 30s) with an animated progress bar. If a player is idle, the dice rolls automatically.
- **AFK Bot Takeover:** After 3 consecutive idle timeouts, the AI bot assumes control of the player's seat.
- **Collapsible Top & Bottom Bars:** HUD bars are collapsed by default to maximize board size; floating handles allow instant access or re-expanding.
- **Immersive Mode (`Key I`):** Hides all top and bottom bars; clicking anywhere on the board rolls the dice!

---

### Hall of Fame & Players Directory CRUD (IndexedDB)
- **Database:** IndexedDB (`KhyberSaanpSeedhiDB_v1`) stores players, matches, presets, and settings.
- **Player Profiles:** Name, KPK District (Bannu, Peshawar, Mardan, Swat, Kohat, Charsadda, Abbottabad, D.I. Khan), Hujra Rank/Title, career matches, wins, Takkar cuts, and custom bead color.
- **Avatar Upload:** HTML5 Canvas auto-compresses uploaded images to under 100KB JPEG DataURLs.
- **Printable Match Certificates:** Official match records with winner details, turn counts, and verification IDs formatted for physical printing (`Ctrl + P`).

---

### AES-GCM 256-bit Encrypted Backup Vault
- **Encryption:** 256-bit AES-GCM encryption with PBKDF2 key derivation (SHA-256, 100,000 iterations).
- **Format:** Exported JSON file includes format header, salt, IV, and authenticated ciphertext.
- **Integrity:** Tamper detection rejects modified backup files, and restore operations prevent duplicate records.
- **Scheduling:** Daily, Weekly, or Custom auto-backup reminders.

---

### Dynamic DB-Backed User Theme Engine
Allows customizing CSS variables linked to the player profile:
- Font families: Inter Modern UI, Segoe Desktop Clean, Classic Hujra Serif, Tactical Monospace.
- Base font sizes: 13px, 14px, 15px, 16px.
- Color pickers: Header BG/Text, Sidebar BG/Text, Main BG/Text, Footer BG/Text.
- Stored directly in IndexedDB and localStorage.

---

## 5. Multiplayer & Networking (WebRTC, QR Code & LAN Radar)

| Networking Mode | Mechanism | Offline Capable? | Usage Scenario |
|---|---|:---:|---|
| **Same Wi-Fi / LAN Radar** | HTML5 `BroadcastChannel` & local PeerJS mesh | ✅ Yes | Automatic player discovery on same Wi-Fi or browser tabs; radar shows nearby nodes. |
| **PeerJS Room ID** | WebRTC signaling over PeerJS cloud / local relay | ⚠️ Initial signaling | Share 6-character room code (e.g. `KPK-9421`) to connect devices across the internet. |
| **Offline WebRTC QR Code** | Serverless SDP Offer/Answer encoded in QR codes | ✅ 100% Offline | Host generates Offer QR; guest scans with camera and generates Answer QR; host scans Answer QR to bind peer connection with zero internet! |
| **Camera QR Scanner** | `Html5Qrcode` / `jsQR` with camera stream & image upload | ✅ Yes | Scan room codes or SDP tokens using the device camera or by uploading a screenshot. |

---

## 6. Audio Synthesizer & Procedural Sound Effects
All audio in both games is procedurally generated using the browser's **Web Audio API** (`AudioContext`). No external audio files are required:
- **Dice Roll:** Triangle and sine waves simulating physical rolling dice.
- **Bead Hop:** Crisp sine wave tone on each board square.
- **Ladder Climb / Home:** Ascending arpeggio fanfare (E4 → G4 → B4 → E5).
- **Snake Bite / Capture:** Descending sawtooth frequency sweep.
- **Takkar Knockback Cut:** Punchy square wave with sub-bass impact.
- **Traditional Hujra Rabab Synth:** A continuous, ambient Pashtun musical scale synthesized using triangle oscillators.
- **Haptic Vibration:** Procedural vibration patterns on supported mobile devices.

---

## 7. Progressive Web App (PWA) Offline Engine
- **Service Worker (`sw.js`):** Built with Google Workbox 7.0.0. Precaches all assets (`index.html`, `snakes.html`, `manifest.json`, icons, scripts).
- **Cache Strategies:**
  - `StaleWhileRevalidate` for scripts and stylesheets.
  - `CacheFirst` for icons and images (30-day expiration).
- **Offline Fallback (`offline.html`):** Clean offline fallback page if an uncached resource is requested.
- **Auto-Update System (`pwa-register.js` & `version.json`):** Checks version timestamps and automatically triggers `skipWaiting()` and page reload when a new build is deployed.

---

## 8. Installation, Deployment & Browser Support

### Local / Static Hosting
Since both applications are entirely client-side, they can be served from any static file server:
```bash
# Using Python
python3 -m http.server 8080

# Using Node.js
npx serve .
```

### GitHub Pages Deployment
1. Push repository files to GitHub.
2. Go to **Settings** → **Pages**.
3. Set Source to `main` branch, `/ (root)` folder.
4. Access via `https://<username>.github.io/<repo>/index.html` (Ludo) or `snakes.html` (Snakes & Ladders).

### Browser Compatibility
- Google Chrome / Chromium 90+ (Desktop & Android)
- Mozilla Firefox 88+
- Apple Safari / WebKit 14+ (iOS & macOS)
- Microsoft Edge 90+
- Opera & Brave

---

# 🇵🇰 اردو زبان میں مکمل دستاویزات (Urdu Documentation)

## 1. ایپ کا تعارف اور پس منظر
**بنوں رائل لڈو اور خیبر سانپ سیڑھی پرو** پختونخوا کے روایتی اور ثقافتی کھیلوں کا ایک بے مثال اور جدید ترین سافٹ ویئر مجموعہ ہے جسے **یاسین اللہ (بنوں سافٹ ویئر سلوشنز)** نے تیار کیا ہے۔ یہ ایپ روایتی پختون حجرہ کلچر، بنوں اور لکی مروت کی 2 ڈائس والی تاریخی لڈو، اور خیبر پختونخوا کے سانپ سیڑھی کے تمام مستند اصولوں کو جدید ڈیجیٹل دنیا میں زندہ کرتی ہے۔

یہ مکمل ایپ بنا انٹرنیٹ کے (آف لائن) کام کرتی ہے، اور موبائل، ٹیبلیٹ اور کمپیوٹر پر کسی بھی قسم کی رکاوٹ یا فالتو اسکرولنگ کے بغیر فل اسکرین چلتی ہے۔

---

## 2. بنوں رائل لڈو کے تمام 26 روایتی قوانین کی مکمل وضاحت

1. **دو دانوں والی روایتی لڈو بمقابلہ 1 دانہ (`2 Dice / 1 Die`):**
   بنوں لڈو میں ہر باری پر 2 ڈائس پھینکے جاتے ہیں۔ آپ دونوں نمبر دو الگ گوٹیوں پر چل سکتے ہیں یا ایک ہی گوٹی پر دونوں کا مجموعہ اکٹھا چل سکتے ہیں۔
2. **صرف آخری ایک گوٹی رہنے پر 1 ڈائس کا اصول (`One Die on Last Bead`):**
   جب کھلاڑی کی 3 گوٹیاں پکی ہو جائیں اور پورے بورڈ پر صرف آخری 1 گوٹی باقی رہے، تو کھیل خودکار طور پر 2 کی بجائے 1 ڈائس پر آ جاتا ہے۔ گھر کے اندر یا آخری پوائنٹ پر بھی خودکار 1 ڈائس چلتا ہے تاکہ گوٹی کبھی نہ پھنسے۔
3. **کلوز گیم بمقابلہ اوپن گیم (`Close Game Lock`):**
   کلوز گیم میں جب کوئی گوٹی پہلے ڈائس سے دشمن کا شکار کرتی ہے، تو وہ گوٹی اس باری کے باقی حصے کے لیے اسی خانے پر لاک (🔒) ہو جاتی ہے تاکہ دوسرا نمبر دوسری گوٹی کو ملے۔ اوپن گیم میں گوٹی لاک نہیں ہوتی۔
4. **شکار کرنے پر دوبارہ باری ملنا (`Bonus Roll on Kill`):**
   مخالف کی گوٹی مارنے پر کھلاڑی کو انعام کے طور پر دوبارہ ڈائس رول کرنے کی باری ملتی ہے۔
5. **چھکا آنے پر پہلے ہاتھ والی گوٹی نکالنا لازمی (`Mandatory Yard Spawn`):**
   اگر ہاتھ میں بند گوٹیاں موجود ہوں اور 6 آ جائے تو پہلے نئی گوٹی باہر نکالنا لازمی ہے، پہلے سے باہر چلتی گوٹی پر وہ 6 نہیں چل سکتا۔
6. **بغیر شکار گھر جانا منع — بلڈ گیٹ (`Blood Gate Loop`):**
   کم از کم 1 شکار کیے بغیر گھر کا دروازہ بند رہتا ہے۔ اگر بغیر شکار کے گوٹی دروازے پر پہنچ جائے تو وہ اندر جانے کے بجائے پورے بورڈ کا 52 خانوں کا چکر دوبارہ لگاتی ہے!
7. **گھر جانے کے لیے 2 شکار لازمی (`Two Kills for Home`):**
   دروازہ کھولنے کے لیے 1 کی بجائے 2 شکار کی کڑی شرط۔
8. **گھر کے قریب بقایا نمبر کا اصول (`Strict Home Remainder`):**
   اگر 2 ڈائس کا نمبر آیا اور ایک نمبر سے گوٹی پکی ہوتی ہے لیکن دوسرا نمبر چلنے کے لیے کوئی دوسری گوٹی موجود نہیں، تو فالتو نمبر ضائع کرنے کی اجازت نہیں ہوتی اور چال منسوخ ہو جاتی ہے۔
9. **لگاتار 3 چھکے یا 3 ڈبل سکس پر باری ضائع ہونا (`3 Consecutive Sixes Penalty`):**
   ایک ہی باری میں لگاتار 3 بار 6 یا 6+6 آنے پر پوری باری منسوخ ہو جاتی ہے۔
10. **دو ڈائس میں ایک چھکے پر بھی دوبارہ باری (`Single Six Re-Roll`):**
    عام طور پر 6+6 پر دوبارہ باری ملتی ہے، مگر اس آپشن سے 6+2 یا 6+4 پر بھی دوبارہ باری مل سکتی ہے۔
11. **اسٹیک رول — پہلے تمام باریاں اکٹھی پھینکنا (`Stack Roll Before Moving`):**
    چھکے یا شکار پر ملنے والی اضافی باریاں پہلے اکٹھی رول ہو کر ڈائس بار میں جمع ہوتی ہیں، پھر تمام نمبر اکٹھے چلے جاتے ہیں۔
12. **1 یا 6 دونوں پر گوٹی کھلنا (`Spawn on 1 and 6`):**
    ہاتھ سے گوٹی 6 کے علاوہ 1 پر بھی باہر آ سکتی ہے۔
13. **ڈبل سکس پر دو گوٹیاں باہر آنا (`Double Six Spawns Two`):**
    6+6 آنے پر خودکار طور پر ہاتھ سے 2 الگ گوٹیاں باہر نکلتی ہیں۔
14. **پہلی گوٹی پہلے سے باہر ہونا (`First Bead on Board`):**
    میچ کے آغاز پر ہی ہر کھلاڑی کی 1 تا 4 گوٹیاں پہلے سے باہر سٹاپ پر کھڑی ہوتی ہیں۔
15. **جوڑا راستہ بند کرنا — دیوار بننا (`Pair Blockade / Jora Wall`):**
    ایک ہی کھلاڑی یا ٹیم کی 2 گوٹیاں ایک خانے پر بیٹھ کر جوڑا (🧱 دیوار) بنا لیتی ہیں؛ مخالف گوٹی اس کے اوپر سے نہیں گزر سکتی۔
16. **ایک خانے کی تمام مخالف گوٹیاں مارنا (`Kill All Stacked Enemies`):**
    ایک ہی حملے میں اس خانے پر بیٹھی تمام دشمن گوٹیاں اکٹھی مر جاتی ہیں۔
17. **شکار ممکن ہو تو مارنا لازمی (`Mandatory Capture / Phoonk`):**
    اگر کسی نمبر سے دشمن کی گوٹی مر رہی ہو تو شکار والی چال ہی چلنا لازمی ہو گا۔
18. **شکار کے بعد باہر گھومنے کی مرضی (`Optional Outer Loop`):**
    شکار کے بعد گوٹی گھر جائے یا مزید شکار کے لیے باہر چکر کاٹے، اس کا انتخاب ملتا ہے۔
19. **بغیر شکار تمام میدانی گوٹیاں دروازے پر جمع ہونا (`Wait at Gate`):**
    بغیر شکار والی گوٹی دروازے پر رک کر باقی میدانی گوٹیوں کے جمع ہونے کا انتظار کرتی ہے۔
20. **2v2 آمنے سامنے کی ٹیمیں (`2v2 Team Mode`):**
    لال + پیلا بمقابلہ ہرا + نیلا۔ پارٹنر ایک دوسرے کو نہیں مارتے بلکہ ایک دوسرے پر بیٹھ کر محفوظ رہتے ہیں۔
21. **پارٹنر کی مدد کے لیے 1 ڈائس پر 6 لانا (`Partner Assist Requires Six`):**
    اپنی تمام گوٹیاں پکی کرنے کے بعد 1 ڈائس سے 6 لانے پر پارٹنر کی گوٹیوں کا 2 ڈائس کنٹرول ملتا ہے۔
22. **گوٹی پکی ہونے پر دوبارہ باری (`Bonus Roll on Home`):**
    کوئی بھی گوٹی گھر پہنچنے پر انعام میں دوبارہ باری ملتی ہے۔
23. **چھکے یا ڈبل سکس پر دوبارہ باری (`Double Six Bonus`):**
    چھکا یا 6+6 آنے پر اضافی باری۔
24. **سٹار / سٹاپ خانوں پر گوٹی کا محفوظ رہنا (`Safe Stop Immunity`):**
    تمام 8 سٹاپ خانوں پر گوٹی مکمل محفوظ رہتی ہے۔
25. **3 بار وقت ختم ہونے پر خودکار بوٹ اور سیٹ واپس لینا (`3-Timeouts Bot Takeover`):**
    3 بار ٹائمر ختم ہونے پر ذہین کمپیوٹر بوٹ باری سنبھال لیتا ہے؛ "👤 Reclaim Seat" بٹن سے ایک سیکنڈ میں کنٹرول واپس مل جاتا ہے۔
26. **ملٹی ماؤس ہارڈویئر لاک (`Multi-Mouse Lock for 2-4 Mice`):**
    ایک لیپ ٹاپ پر 2 سے 4 ماؤس لگائیں؛ ہر کھلاڑی کا ماؤس صرف اسی کی باری پر کام کرے گا!

---

## 3. ملٹی ماؤس ہارڈویئر لاک (ایک لیپ ٹاپ پر 2 سے 4 ماؤس)
یہ اس ایپ کی تاریخی ایجاد ہے! آپ ایک ہی لیپ ٹاپ یا کمپیوٹر کے ساتھ 2، 3 یا 4 ماؤس (USB یا وائرلیس) لگا سکتے ہیں۔
- **ونڈوز (Windows):** ماؤس لگائیں اور TeamPlayer4 یا MouseMux سافٹ ویئر چلا کر ملٹی پوائنٹر آن کریں۔
- **لینکس (Linux):** بغیر کسی اضافی سافٹ ویئر کے xinput کمانڈ سے 4 الگ کرسر بنائیں۔
- **سیٹ لاکنگ:** ایپ کے اندر "Setup Mice" پر جا کر ہر کھلاڑی اپنے ماؤس سے اپنے رنگ والے خانے پر کلک کرے گا۔ اس کے بعد لال کی باری پر صرف لال کا ماؤس چلے گا، اگر ہرا یا نیلا ماؤس ہلائے گا تو کمپیوٹر اسے فوراً مسترد کر دے گا!

---

## 4. خیبر سانپ سیڑھی پرو کے روایتی قوانین و فیچرز
- **چھکا داخلہ (Chakka Dakhila):** کیمپ (خانہ 0) سے نکلنے کے لیے 6 درکار ہے۔
- **تین چھکے برسی (3x6 Burn):** لگاتار تین 6 آنے پر باری جل جاتی ہے اور گوٹی واپس شروع میں چلی جاتی ہے۔
- **خیبر ٹکر (Takkar Cut):** مخالف کے خانے پر اترنے سے اس کی گوٹی کٹ کر واپس خانہ نمبر 1 پر چلی جاتی ہے، اور کاٹنے والے کو اضافی باری ملتی ہے!
- **حجرہ محفوظ خانے (Safe Zones):** خانہ نمبر 1، 14، 27، 50، 75 اور 92 محفوظ قلعے ہیں جہاں ٹکر نہیں لگتی۔
- **99 کالا مار کوبرا (Square 99 Kalamar):** خانہ 99 پر خوفناک کالا سانپ بیٹھا ہے جو سیدھا خانہ نمبر 4 پر گراتا ہے۔
- **پورا 100 جیت:** جیتنے کے لیے بالکل پورا 100 نمبر آنا ضروری ہے۔
- **1 سے 4 گوٹیاں فی کھلاڑی:** 1 گوٹی (کلاسک)، 2 گوٹیاں (جوڑا)، 3 گوٹیاں (ٹولی)، 4 گوٹیاں (مکمل حجرہ پارٹی)۔
- **آن بورڈ سانپ میکر (Snake Editor):** بورڈ پر انگلی یا ماؤس سے کلک کر کے اپنی مرضی کا سانپ یا سیڑھی بنائیں، سانپ کا سائز باریک یا موٹا کریں!
- **خودکار باری اور ایمرجنسی بوٹ:** سست کھلاڑیوں کے لیے 10 سیکنڈ ٹائمر کے بعد خودکار رول، اور 3 بار غیر حاضر رہنے پر بوٹ کنٹرول۔
- **فل اسکرین ایمرسیو موڈ:** اسکرین پر تمام بٹن چھپ جاتے ہیں اور صرف بورڈ پر کہیں بھی ٹیپ کر کے ڈائس رول ہوتا ہے۔

---

## 5. کھلاڑیوں کا ریکارڈ، ہال آف فیم اور پرنٹ ایبل اسناد
- **انڈیکسڈ ڈی بی (IndexedDB) ڈیٹا بیس:** تمام کھلاڑیوں کا نام، ضلع (بنوں، پشاور، مردان، سوات، کوہاٹ، چارسدہ، ایبٹ آباد، ڈی آئی خان)، حجرہ رینک، فتوحات اور شکار ریکارڈ ہوتے ہیں۔
- **تصویر اپلوڈ:** کھلاڑی کی تصویر 100 کے بی سے کم سائز میں خودکار کمپریس ہو کر محفوظ ہوتی ہے۔
- **سرٹیفکیٹ پرنٹنگ:** ہر مکمل ہونے والے میچ کا باقاعدہ فتوحات کا سرٹیفکیٹ کمپیوٹر سے پرنٹ کیا جا سکتا ہے۔
- **256-بٹ پاس ورڈ انکرپٹڈ بیک اپ:** پورے ریکارڈ کا پاس ورڈ لگا کر محفوظ بیک اپ بنائیں جو کوئی دوسرا چوری یا خراب نہیں کر سکتا۔

---

## 6. بغیر انٹرنیٹ اور وائی فائی ملٹی پلیئر کھیلنے کا طریقہ
- **1 موبائل پر پاس اینڈ پلے:** ایک ہی موبائل پر 2 سے 4 دوست باری باری کھیل سکتے ہیں۔
- **ایک وائی فائی پر ریڈار روم:** ایک ہی وائی فائی یا موبائل ہاٹ اسپاٹ پر ریڈار پر قریبی دوست کا نام ظاہر ہوتا ہے، کلک کر کے چیلنج بھیجیں!
- **بغیر انٹرنیٹ کیو آر کوڈ (Offline QR P2P):** ایک موبائل پر کیو آر کوڈ بنائیں، دوسرا موبائل کیمرے سے اسکین کرے—بغیر کسی انٹرنیٹ کے دونوں موبائل آپس میں جڑ جائیں گے!

---

### 👨💻 تیار کردہ (Created By)

&lt;div align=&quot;center&quot;&gt;

**یاسین اللہ (Yasin Ullah)** – بنوں سافٹ ویئر سلوشنز (Bannu Software Solutions)  
📱 واٹس ایپ (WhatsApp): **0336-1593533**  
🔗 لنکڈ ان: [LinkedIn Profile](https://www.linkedin.com/in/yasin-ullah-029229232/)  

*پاکستان اور بین الاقوامی دنیا کے لیے جدید ترین روایتی و سائنسی سافٹ ویئر سلوشنز*

&lt;/div&gt;
