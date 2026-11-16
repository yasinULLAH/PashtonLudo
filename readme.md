# 🎲 Bannu Royale Ludo & Khyber Saanp Seedhi Pro
### Authentic Pashtun Cultural Rules, 2-Dice Mechanics, Multi-Mouse Hardware Lock & KPK Hujra Board Gaming Suite
**Developer:** Yasin Ullah — Bannu Software Solutions  
**Contact:** WhatsApp: `0336-1593533` | [LinkedIn Profile](https://www.linkedin.com/in/yasin-ullah-029229232/)  
**Dedication:** 💛 Dedicated to my little brother **Muhib Ullah**  
**Edition:** v5.5 Master Production Suite (PWA Offline Enabled, Standalone Android APKs & Windows Portable EXEs Included)

> ### © 2026 Yasin Ullah — Bannu Software Solutions. **All Rights Reserved.**
>
> **Proprietary & confidential.** This software, its source code, game rules engine, UI/UX,
> artwork and all assets are the exclusive property of **Yasin Ullah**.
>
> **Copying, modification, reuse, redistribution, republishing, re-skinning, reverse
> engineering and creation of derivative works are strictly prohibited** without the
> author's prior **written** permission.
>
> Any use permitted in writing must carry the attribution:
> *“Bannu Royale Ludo / Khyber Saanp Seedhi Pro — © 2026 Yasin Ullah, All Rights Reserved.”*
>
> Full legal terms: **[LICENSE](./LICENSE)** · Permission requests: WhatsApp `0336-1593533`

---

## 📌 Table of Contents / فہرست مضامین
1. [English Documentation](#-english-documentation)
   - [Project Overview](#1-project-overview)
   - [Core Architecture & Technology Stack](#2-core-architecture--technology-stack)
   - [Bannu Royale Ludo (`index.html`) — Deep Dive](#3-bannu-royale-ludo-indexhtml--deep-dive)
     - [All 45 Cultural, Tournament & Advanced House Rules Detailed](#all-45-cultural-tournament--advanced-house-rules-detailed)
     - [True 3D Isometric Rolling Canvas Dice Engine](#true-3d-isometric-rolling-canvas-dice-engine)
     - [Multi-Mouse Hardware Lock (2 to 4 Mice)](#multi-mouse-hardware-lock-2-to-4-mice)
     - [7 Match Formats & 7 Cultural Drills](#7-match-formats--7-cultural-drills)
     - [Single-Click Preview vs Second-Click Execution](#single-click-preview-vs-second-click-execution)
     - [Crash Recovery & Unfinished Match Engine](#crash-recovery--unfinished-match-engine)
     - [Replay Studio, Timeline Scrubbing & WebM Video Export](#replay-studio-timeline-scrubbing--webm-video-export)
     - [Generational Machine Learning AI & Turn Speed Controller](#generational-machine-learning-ai--turn-speed-controller)
     - [Match Organizer, Tagging System & Favorite Pinning](#match-organizer-tagging-system--favorite-pinning)
     - [Contextual Victory Roast & Cultural Banter Engine](#contextual-victory-roast--cultural-banter-engine)
     - [Comprehensive Victory Full Stats & Match Drilldown Analytics](#comprehensive-victory-full-stats--match-drilldown-analytics)
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
   - [Installation, Deployment, Browser Support & Native Builds](#8-installation-deployment-browser-support--native-builds)
     - [Native Standalone Builds: Android APKs & Windows Portable EXEs (GitHub Actions CI/CD)](#native-standalone-builds-android-apks--windows-portable-exes-github-actions-cicd)
2. [اردو زبان میں مکمل دستاویزات (Urdu Documentation)](#-اردو-زبان-میں-مکمل-دستاویزات-urdu-documentation)
   - [ایپ کا تعارف اور پس منظر](#1-ایپ-کا-تعارف-اور-پس-منظر)
   - [بنوں رائل لڈو کے تمام 45 روایتی، ٹورنامنٹ اور ہاؤس رولز کی مکمل وضاحت](#2-بنوں-رائل-لڈو-کے-تمام-45-روایتی-ٹورنامنٹ-اور-ہاؤس-رولز-کی-مکمل-وضاحت)
   - [تھری ڈی گھومنے والے دانے (True 3D Isometric Rolling Canvas Dice)](#3-تھری-ڈی-گھومنے-والے-دانے-true-3d-isometric-rolling-canvas-dice)
   - [ملٹی ماؤس ہارڈویئر لاک (ایک لیپ ٹاپ پر 2 سے 4 ماؤس)](#4-ملٹی-ماؤس-ہارڈویئر-لاک-ایک-لیپ-ٹاپ-پر-2-سے-4-ماؤس)
   - [میچ ری پلے اسٹوڈیو، فریم اسکربر اور ویڈیو ڈاؤنلوڈ (Replay Studio & WebM Video Export)](#5-میچ-ری-پلے-اسٹوڈیو-فریم-اسکربر-اور-ویڈیو-ڈاؤنلوڈ-replay-studio--webm-video-export)
   - [خود سیکھنے والی جدید مصنوعی ذہانت اور اسپیڈ کنٹرول (Generational Machine Learning AI)](#6-خود-سیکھنے-والی-جدید-مصنوعی-ذہانت-اور-اسپیڈ-کنٹرول-generational-machine-learning-ai)
   - [میچ آرگنائزر، ٹیگز اور اسٹار پننگ (Match Organizer, Tagging & Pinning)](#7-میچ-آرگنائزر-ٹیگز-اور-اسٹار-پننگ-match-organizer-tagging--pinning)
   - [جیت پر روایتی طنز و مزاح اور چھیڑ چھاڑ (Victory Roast & Banter Engine)](#8-جیت-پر-روایتی-طنز-و-مزاح-اور-چھیڑ-چھاڑ-victory-roast--banter-engine)
   - [خیبر سانپ سیڑھی پرو کے روایتی قوانین و فیچرز](#9-خیبر-سانپ-سیڑھی-پرو-کے-روایتی-قوانین-و-فیچرز)
   - [کھلاڑیوں کا ریکارڈ، ہال آف فیم اور پرنٹ ایبل اسناد](#10-کھلاڑیوں-کا-ریکارڈ-ہال-آف-فیم-اور-پرنٹ-ایبل-اسناد)
   - [بغیر انٹرنیٹ اور وائی فائی ملٹی پلیئر کھیلنے کا طریقہ](#11-بغیر-انٹرنیٹ-اور-وائی-فائی-ملٹی-پلیئر-کھیلنے-کا-طریقہ)
   - [اینڈرائیڈ اے پی کے اور ونڈوز پورٹیبل فائلیں (Android APKs & Windows Portable EXEs)](#12-اینڈرائیڈ-اے-پی-کے-اور-ونڈوز-پورٹیبل-فائلیں-android-apks--windows-portable-exes)

---

# 🇬🇧 English Documentation

## 1. Project Overview
**Bannu Royale Ludo & Khyber Saanp Seedhi Pro** is a world-class cultural board gaming suite developed by **Yasin Ullah (Bannu Software Solutions)**. The suite preserves and digitalizes the centuries-old traditional Hujra board gaming rules of Khyber Pakhtunkhwa (KPK), Pakistan—specifically the historic 2-Dice tactical Ludo played in Bannu, Lakki Marwat, Peshawar, Mardan, and Swat, along with Pashtun Snake and Ladder (Khyber Saanp Seedhi).

The project is structured as a dual-game Progressive Web Application (PWA) with native multi-platform compilation pipelines. It runs 100% client-side in any modern web browser or as standalone native Android APKs (with sticky immersive fullscreen) and portable Windows 64-bit EXEs with zero server latency, complete offline readiness, multi-pointer hardware support, WebRTC peer-to-peer networking, generational machine learning AI, match replay video generation, and bank-grade cryptographic data vaults.

---

## 2. Core Architecture & Technology Stack

| Layer | Technologies & Libraries | Architectural Purpose |
|---|---|---|
| **Render Engine** | HTML5 Canvas 2D API (`index.html`) & Dynamic CSS Grid 10x10 (`snakes.html`) | 60 FPS distraction-free hardware-accelerated board rendering, custom token geometry, true 3D isometric rolling canvas dice with depth shading, breadcrumb hop trails, and realistic snake anatomy. |
| **Styling & Theme** | Tailwind CSS 3.4.17, Animate.css, CSS Custom Properties (`--main-bg`, `--accent-primary`) | Responsive layouts, mobile React Native Android app styling, tactile active-press feedback, and user-customizable UI theme engine. |
| **State & Database** | IndexedDB (`KhyberSaanpSeedhiDB_v1`), HTML5 LocalStorage | Persistent multi-store database for users, players, matches, custom presets, settings, and instant crash recovery snapshots. |
| **Cryptographic Security** | Web Crypto API (`SubtleCrypto`), PBKDF2 (SHA-256, 100k rounds), AES-GCM 256-bit | Authenticated client-side encryption of career vaults and exported JSON backups with random 16-byte salt and 12-byte IV. |
| **Machine Learning AI** | Heuristic Neural-Weight Engine (`aiKnowledgeBase`), Hotspot Coordinate Danger Mapping (`trackDangerStats`) | Generational self-learning AI adapting weights (danger avoidance, kill aggression, home rush, jora blockade) from human moves and match outcomes with multi-tier speed pacing. |
| **Media & Video Synthesis** | HTML5 Canvas `captureStream()`, `MediaRecorder` API | In-memory match frame timeline (`gameState.replayFrames`), frame-by-frame scrubbing, JSON replay export/import, and native WebM video recording in 480p, 720p, or 1080p. |
| **Multi-Touch & Hardware** | Pointer Events API (`pointerdown`, `pointermove`, `pointerup`), `event.pointerId` | Multi-touch drag-and-drop, gesture support, and Multi-Mouse hardware pointer lock (2 to 4 separate USB/wireless mice). |
| **Peer-to-Peer Networking** | PeerJS 1.5.2/1.5.4, Native `RTCPeerConnection`, `RTCDataChannel`, BroadcastChannel | Zero-server device-to-device multiplayer: Wi-Fi LAN Radar, PeerJS room codes, and serverless WebRTC SDP QR code handshakes. |
| **Vision & QR Scanning** | `QRCode.js`, `Html5Qrcode` (2.3.8), `jsQR` (1.4.0) | High-speed QR code generation and real-time camera/image scanner for zero-typing WebRTC room pairing. |
| **Audio Synthesis** | Web Audio API (`AudioContext`, `OscillatorNode`, `GainNode`) | Zero-asset procedural sound effects (hops, dice rattles, kills, victory fanfare) and a live traditional Pashtun Rabab background synth loop. |
| **Data Tables & Export** | jQuery 3.7.1, DataTables 1.13.8, PDFMake, JSZip, Buttons HTML5 | Searchable, paginated, responsive player directories and match archives with 1-click export to PDF, Excel, CSV, and Print. |
| **Offline PWA Engine** | Workbox 7.0.0, Service Worker (`sw.js`), Web App Manifest (`manifest.json`) | Complete offline caching of all assets, standalone home-screen installation on Android/iOS/Windows, and offline fallback page. |
| **Native Packaging & CI/CD** | GitHub Actions (`build.yml`), Capacitor 6, Android SDK, Gradle, Electron 33, Electron-Builder | Automated builds producing standalone offline Android APKs (with `SYSTEM_UI_FLAG_IMMERSIVE_STICKY`) and portable Windows 64-bit `.exe` binaries with custom 512x512 icons. |

---

## 3. Bannu Royale Ludo (`index.html`) — Deep Dive

Bannu Royale Ludo is a full simulation of the authentic Pashtun 2-Dice Ludo ruleset alongside international 1-Die Yalla rules. It operates on an adaptive full-bleed 15x15 board canvas that fills 100% of the screen without empty borders or page scrolling.

### All 45 Cultural, Tournament & Advanced House Rules Detailed

The engine features a comprehensive Rulebook Studio with 45 toggleable cultural, tournament, and tactical house rules:

1. **Two-Dice Tactical Play vs 1-Die Classic (`diceCount: 2 | 1`)**
   - **Mechanism:** Players roll two 6-sided dice simultaneously.
   - **Effect:** Numbers can be split across two different beads or combined into a single sum hop on one bead. In 1-Die mode, classic single-die rolling applies.
2. **Must Use 1 Die When Only 1 Bead Remains on Board (`oneDieWhenOneBeadLeft: true`)**
   - **Mechanism:** As soon as 3 beads reach Home and only 1 bead remains on the board, rolling automatically switches from 2 Dice to 1 Die.
   - **Guardrail:** Even if disabled, the engine automatically switches to 1 Die once the bead enters the Home column or reaches the final square needing 1 step, ensuring no bead ever gets mathematically trapped.
3. **Close Game vs Open Game Capture Lock (`closeGameMode: true`)**
   - **Mechanism:** Capturing an enemy bead on Die 1 locks (🔒) that capturing bead on the kill square for the remainder of that turn if any other bead can legally move.
   - **Effect:** Prevents "hit-and-run" tactics. In Open Game, capturing beads can immediately run away on Die 2.
4. **Keep Capturing Bead Locked Across Bonus Re-Rolls (`keepCaptureLockOnBonus: true`)**
   - **Mechanism:** In Close Game mode, a bead that captures an opponent remains locked on that square during all subsequent bonus re-rolls of that same Bari until your next Bari comes.
5. **Bonus Re-Roll on Kill / Capture (`bonusRollOnKill: true`)**
   - **Mechanism:** Capturing any opponent bead awards a bonus dice re-roll once the current dice are spent.
   - **Effect:** Rewards offensive strategies and momentum shifts.
6. **Mandatory Hand / Yard Spawn on 6 (`mandatoryYardSpawn: true`)**
   - **Mechanism:** If a player rolls a 6 while unplaced beads remain in the hand/yard, the engine forces spawning a bead onto the starting square before moving ground beads.
   - **Auto-Placement:** Includes single-click automatic placement of the pocket bead on 6.
7. **Blood Gate: 1 Kill Required for Home Entry + Outer Loop (`killRequiredForHome: true`)**
   - **Mechanism:** A player's Home column gate stays locked (🔒) until that player captures at least 1 enemy bead.
   - **Effect:** Reaching the Home gate with 0 kills forces the bead to bypass the gate and complete another full 52-square outer lap!
8. **Ground Wipeout Resets Home Eligibility (`wipeoutResetsHomeEligibility: true`)**
   - **Mechanism:** If all beads of a player on the ground are killed/eaten before any bead enters Home, their Home eligibility is lost and clean sweep is restored until a new kill is made.
9. **Single Ground Loop Only Without Kill & Free Choice After Kill (`singleGroundLoopOnlyWithoutKill: true`)**
   - **Mechanism:** If a player has not eaten someone, they cannot come around their Home unless that bead is their ONLY bead on the ground. Once they eat an opponent, they are free to either come around Home or enter inside it.
10. **Optional Outer Loop After Kill (`optionalLoopAfterKill: true`)**
    - **Mechanism:** Once a player has eaten an opponent, they are free to choose between going inside Home to complete or coming around their Home (looping the outer board again to hunt).
11. **No-Kill Gate Wait Until All Ground Beads Gather (`waitAllGroundAtGate: true`)**
    - **Mechanism:** A player with 0 kills cannot go around Home (loop past the gate) until all of their on-ground beads have reached the last home point (step 50) and no movement is possible.
12. **Two Kills Required for Home Entry (`twoKillsForHome: false`)**
    - **Mechanism:** Upgrades the blood-gate threshold from 1 kill to 2 kills before Home unlocks.
13. **Strict Near-Home Remainder Rule (`strictHomeRemainder: true`)**
    - **Mechanism:** Near Home, a player cannot play one die into Home if the second die (the remainder) cannot be legally consumed by any bead on the board without overshooting.
14. **Three Consecutive Sixes Penalty (`threeConsecutiveSixesPenalty: false`)**
    - **Mechanism:** Rolling three consecutive 6s (in 1-Die) or three consecutive 6+6s (in 2-Dice) cancels the turn and passes the dice to the next player.
15. **Single Six Re-Roll in 2-Dice Mode (`singleSixBonusInTwoDice: false`)**
    - **Mechanism:** In traditional 2-Dice Ludo, only Double Six (6+6) grants a bonus roll. Enabling this grants a re-roll even if only one die is a 6 (e.g., 6+2, 6+4).
16. **Stack Roll / Accumulate Sixes Before Moving (`stackRollBeforeMoving: true`)**
    - **Mechanism:** When you roll 2 dice and kill or complete on one die (e.g. rolled 5 & 4 and killed on 4), you can store the remaining 5, roll your bonus dice, and use all remaining dice counts at once!
17. **Spawn on 1 as well as 6 (`spawnOnOneAndSix: false`)**
    - **Mechanism:** Allows bringing beads out of hand on either a 1 or a 6 (popular in fast matches).
18. **Double-Six Spawns Two Beads (`doubleSixSpawnsTwoBeads: false`)**
    - **Mechanism:** Rolling 6+6 with 2+ beads in hand forces bringing two separate beads out onto the starting square simultaneously.
19. **First Bead Starts Already on Board (`firstBeadStartsOnBoard: false`)**
    - **Mechanism:** Players begin the match with 1, 2, 3, or 4 beads already deployed on their starting square, starting immediate action without waiting for a 6.
20. **Pair Blockade / Jora Wall Rule (`pairBlockadeRule: false`)**
    - **Mechanism:** Two beads of the same player (or 2v2 team) on the same square form a "🧱 JORA" wall. Rival beads cannot jump over this square until the blockade breaks.
21. **Kill All Stacked Enemies of Same Player (`killAllStackedEnemies: true`)**
    - **Mechanism:** Landing on stacked opponent beads of the same player outside safe stops captures every enemy bead on that square simultaneously (+N kills).
22. **Mandatory Capture / Must Kill if Possible (`mandatoryCapture: false`)**
    - **Mechanism:** If any legal move captures an enemy bead, peaceful moves are disallowed and the player must execute the capture ("Phoonk" rule).
23. **2v2 Opposite-Corner Teams & Safe Partner Stacking (`teamMode: true`)**
    - **Mechanism:** Red + Yellow (♦Team 1) compete against Green + Blue (★Team 2). Teammates never capture each other, can stack safely, and win when all 8 team beads reach Home.
24. **Teammate Assist Requires Rolling a 1-Die Six First (`teamAssistRequiresSix: true`)**
    - **Mechanism:** After completing all your beads in 2v2, you must roll 1 Die on your turn until you roll a 6. Once rolled, Partner Assist unlocks and you gain 2-Dice control of your partner's beads!
25. **Bonus Re-Roll on Bead Home Completion (`bonusRollOnHome: true`)**
    - **Mechanism:** Moving any bead into the final center Home triangle awards a bonus dice re-roll.
26. **Bonus Re-Roll on 6 / Double 6 (`doubleSixBonusRoll: true`)**
    - **Mechanism:** Master switch for whether 6 (1-Die) or 6+6 (2-Dice) grants another turn.
27. **Star / Stop Square Safe Immunity (`safeStopImmunity: true`)**
    - **Mechanism:** All 8 Stop squares (4 colored start squares + 4 yellow Star stops at 8, 21, 34, 47) provide 100% immunity from enemy capture.
28. **3-Timeouts Auto-Bot Takeover & One-Tap Reclaim (`threeTimeoutsBotTakeover: true`)**
    - **Mechanism:** If a human player misses their turn timer 3 consecutive times, the smart AI Bot automatically takes over their seat. A pulsing "👤 Reclaim Seat" button allows reclaiming control instantly with a single tap.
29. **Reverse Kill / Backstab Rule (`chkReverseKill: false`)**
    - **Mechanism:** Rolling a 1 or 2 allows moving a bead backwards (-1 or -2) to capture an opponent bead sitting right behind you!
30. **Friendly Fire in 2v2 Mode (`chkFriendlyFire: false`)**
    - **Mechanism:** In 2v2 Team Mode, landing on your teammate's bead on an unprotected square captures it and sends it back to the yard instead of stacking safely.
31. **Kamikaze / Mutual Destruction on Jora (`chkKamikazeJora: false`)**
    - **Mechanism:** Landing on an opponent's Jora (2+ enemy beads on an unprotected square) destroys both your attacking bead and all defending enemy beads in that Jora!
32. **Snake Eyes Penalty / Double 1s Trap (`chkSnakeEyesPenalty: false`)**
    - **Mechanism:** Rolling 1+1 in 2-dice mode automatically kills your most advanced on-ground bead and sends it back to the yard.
33. **Max Stack Limit of 2 Beads per Square (`chkMaxStackLimit: false`)**
    - **Mechanism:** At most 2 beads can occupy any single square (including safe stops). Any move that would place a 3rd bead on the same square is invalid.
34. **Heavy Jail / Hardcore Respawn (`chkHeavyJail: false`)**
    - **Mechanism:** A bead captured by an opponent is locked in Heavy Jail (⛓️) and requires a Double-6 (6+6 in 2-dice mode) or two consecutive 6s (in 1-die mode) to respawn.
35. **Position Hijack / 6+1 Swap Rule (`chkPositionHijack: false`)**
    - **Mechanism:** Rolling 6+1 (or 1+6) in 2-dice mode and landing on an opponent bead swaps board positions with the opponent instead of sending them to the yard!
36. **Spawn Invincibility / First Turn Shield (`chkSpawnInvincibility: false`)**
    - **Mechanism:** A bead that just spawned onto the board receives a temporary shield (🛡️) and cannot be killed by an opponent until it has moved on a subsequent turn.
37. **Phook / Blown Bead Penalty (`chkPhookPenalty: false`)**
    - **Mechanism:** Allows ignoring a capture, but if your bead could have killed an opponent and you missed/ignored the kill, that bead is "blown" (sent to yard) at the end of your turn!
38. **Bouncing Home / Overshoot Penalty (`chkBouncingHome: false`)**
    - **Mechanism:** If a bead overshoots the center Home goal (e.g. needs 2 but rolls 5), it steps to the center and bounces backwards down the Home stretch by the excess spaces.
39. **Anti-Camping Limit / Safe Square Eviction (`chkAntiCampingLimit: false`)**
    - **Mechanism:** A bead may only sit on a Safe/Star square for 3 consecutive turns. On the 4th turn without moving, its safe immunity drops (⛺) and enemies can capture it right on the safe stop!
40. **Jora Breaker / Double-6 Wall Crushing (`chkJoraBreaker: false`)**
    - **Mechanism:** Enhances Pair Blockade (Jora): an opponent can jump over or crush an impassable Jora blockade if they roll a strict Double-6 (6+6)!
41. **The Toll Gate / Chungi at Step 50 (`chkTollGate: false`)**
    - **Mechanism:** A bead must stop on the Home Gate square (step 50) first and roll an exact 1 to unlock the gate and step inside the Home stretch.
42. **Qisas / Blood Vengeance +10 Jump (`chkQisasVengeance: false`)**
    - **Mechanism:** Tracks which enemy bead killed yours (marked ⚖️). Capturing that exact "Wanted" killer bead rewards you with an instant +10-step bonus jump for any of your beads!
43. **Strict Spawn-Only Sixes (`chkStrictSpawnOnlySixes: false`)**
    - **Mechanism:** A rolled 6 can ONLY be used to spawn a bead from the yard. If your yard is empty, any rolled 6 is nullified/wasted and cannot move a board bead forward.
44. **Dice Splitting on Even Roll in 1-Die Mode (`chkDiceSplitting: false`)**
    - **Mechanism:** When rolling 1 Die (in 1-Die mode or 1-Die endgame), rolling an even 4 or 6 lets you split the die evenly across two different on-ground beads (2+2 or 3+3)!
45. **Multi-Mouse Per-Player Hardware Lock for 2 to 4 Mice (`chkMultiMouseLock: false`)**
    - **Mechanism:** Tracks physical hardware mouse pointers via `event.pointerId`. Locks each seat to a specific physical mouse so only that mouse can roll or move on that player's turn!

---

### True 3D Isometric Rolling Canvas Dice Engine
Rather than relying on flat sprites or DOM elements, Bannu Royale Ludo features a custom **True 3D Isometric Rolling Dice Engine** rendered directly onto the Canvas 2D corner yards (`drawIsometric3dDieOnCanvas`):
- **Dynamic Physics & Shading:** Procedural tumble rotations, bounce elevation (`liftY`), ground drop shadows that expand/contract with altitude (`ctx.ellipse`), and multi-face isometric lighting (top, front, and side faces).
- **Recessed Pips:** Accurate mathematical pip placement with subtle inner bevels and depth shadows.
- **Interactive Die Selection Halo:** When splitting dice across two beads, active selectable dice pulse with an electric cyan aura (`#38bdf8`), making dice selection intuitive on touchscreens and mice.

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

### Replay Studio, Timeline Scrubbing & WebM Video Export
The comprehensive **Replay Studio** (`replayStudioModal`) records every match turn, hop, kill, and dice roll into an in-memory frame timeline (`gameState.replayFrames`):
- **Timeline Scrubbing:** Scrub through the game frame-by-frame with Step Forward (⏭️), Step Backward (⏮️), and jump to Start/End controls.
- **Event-Based Jump Markers:** Quick-jump buttons allow jumping instantly to key game events:
  - ⚔️ Kills & Captures
  - 🏠 Home Stretch & Goal Arrivals
  - 🎲 Double-Sixes & Turn Burns
  - 💥 Wipeout Resets
- **Variable Playback Speed:** 0.5x Slow-Motion, 1x Normal, 2x Fast, and 4x Blitz playback speeds.
- **Direct WebM Video Recording:** The `exportReplayAsVideoFile` function renders frames to an offscreen canvas and utilizes the browser's `captureStream()` and `MediaRecorder` API to encode high-quality `.webm` video files directly onto your device. Supports 3 output resolutions:
  - 480p Small (540×660 @ 1.5 Mbps) — Optimized for fast WhatsApp sharing
  - 720p Mid (720×880 @ 3.5 Mbps) — Crisp balanced video
  - 1080p High (1080×1320 @ 7.5 Mbps) — Studio-grade archive resolution
- **Portable JSON Replay Archives:** Export and import full matches as lightweight `.json` files (`exportCurrentReplayAsJson`, `importReplayFromJsonFile`) to exchange match records across devices.
- **High-Res Frame Screenshot Downloader:** Capture and download any single frame as a crisp `.PNG` graphic with one tap.

---

### Generational Machine Learning AI & Turn Speed Controller
The game features an autonomous, generational self-learning AI engine (`aiKnowledgeBase`) that progressively evolves its playstyle:
- **Heuristic Neural-Weights:**
  - `dangerAvoidance`: Dynamic weighting on evading enemy kill ranges.
  - `killAggression`: Prioritizes offensive cuts, Jora disruptions, and blood-gate unlocking.
  - `homeRush`: Weighting on advancing beads toward the home column.
  - `joraFocus`: Strategic alignment for pairing beads and forming defensive walls.
- **Dynamic Learning Triggers:**
  - `learnFromHumanMove`: Studies human opening splits and positional risks.
  - `learnFromCaptureEvent`: Updates hot-spot danger coordinates (`trackDangerStats`) across all 52 track squares, avoiding repeatedly punished positions.
  - `learnFromMatchOutcome`: Adjusts overall risk appetite based on victory/defeat margins.
- **Generational Milestones:** The AI tracks its generation milestones and displays its active learning status badge in the in-game pause menu.
- **AI Turn Speed Controller:** Customize AI thinking time via the speed dropdown:
  - `Instant / Blitz` (100ms) — Ultra-fast simulation
  - `Fast` (Default) — Snappy responsive gameplay
  - `Slow` (900ms) — Realistic human deliberative pacing
  - `Dramatic` (1400ms) — Suspenseful high-stakes Hujra timing
  - `Slowest` (2200ms) — Slow-motion beginner friendly
  - `Custom` (0.2s to 10s slider) — Exact millisecond control

---

### Match Organizer, Tagging System & Favorite Pinning
The **Match Organizer** (`matchOrganizerModal`) provides full post-match classification:
- **Custom Title & Referee Notes:** Rename matches and attach custom referee comments.
- **Match Categories:** General, Tournament / Final, Hujra Night, Family Match, Clean Sweep Showcase, Epic Comeback, Funny / Roast, AI Training / Lab, or custom user categories.
- **Quick-Tag Pills:** One-tap tagging with `#Hujra`, `#EpicWin`, `#Tournament`, `#Comeback`, `#CleanSweep`, `#CloseCall`, `#Revenge`, `#DoubleSixMaster`, `#BotTakeover`, and `#BannuDerby`.
- **Favorite Match Pinning (⭐):** Star legendary matches to keep them pinned at the top of the history list.

---

### Contextual Victory Roast & Cultural Banter Engine
The **Victory Roast Engine** (`detectMatchRoastConditions`) evaluates the exact circumstances of a match's conclusion and generates hilarious, culturally grounded Pashto and Urdu roasts:
- **0-Kill Loser Roast:** *"صفر شکار! یار تم لڈو کھیلنے آئے تھے یا صرف چہل قدمی کرنے؟"* (Zero kills! Did you come to play Ludo or just take an evening stroll?)
- **Consecutive Loss Streaks:** Tailored roasts for players on a 2x, 3x, or 4x losing streak (*"مسلسل ہار کا ہیٹ ٹرک! حجرے کی چائے اب تمہارے ذمے ہے!"*).
- **Blown Leads & Heavy Jail Traps:** Roasts players who held massive leads but were wiped out or trapped in Heavy Jail.
- **Interactive Roast Cycler:** Tap **"Next Roast 🔄"** on the victory banner to cycle through hilarious cultural commentary.

---

### Comprehensive Victory Full Stats & Match Drilldown Analytics
The **Victory Full Stats Modal** (`openVictoryFullStatsModal`) provides professional analytics across three dedicated tabs:
- **Summary Tab:** Final placement, total turns, match duration, dice rolled, and team score.
- **Combat & Kills Tab:** Kill/Death ratio per player, most lethal bead, revenge cuts executed, and Jora blockades formed.
- **Dice Analytics Tab:** Total dice rolled, 6s frequency percentage, Double-Six frequency, and Snake-Eyes count.
- **Match Drilldown Modal (`openMatchDrilldownModal`):** Click any past match to view its full metadata badges, referee notes, tags, and a direct **"Watch Replay 🎥"** button to jump straight into Replay Studio!

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

## 8. Installation, Deployment, Browser Support & Native Builds

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

### Native Standalone Builds: Android APKs & Windows Portable EXEs (GitHub Actions CI/CD)

The suite includes an automated multi-platform CI/CD pipeline defined in `.github/workflows/build.yml`. Every push automatically builds 4 standalone offline binary targets:

1. **Bannu Royale Ludo Android APK (`BannuRoyaleLudo.apk`)**:
   - Built with Capacitor 6 and Gradle.
   - Configured with `SYSTEM_UI_FLAG_IMMERSIVE_STICKY` for a true full-bleed, borderless Android gaming experience with hidden navigation and status bars.
   - 100% offline self-contained package.
2. **Khyber Saanp Seedhi Pro Android APK (`KhyberSaanpSeedhi.apk`)**:
   - Standalone Android APK for Snake & Ladder with touch-optimized full-screen gameplay.
3. **Bannu Royale Ludo Windows Portable EXE (`BannuRoyaleLudo.exe`)**:
   - Built with Electron 33 and electron-builder.
   - Zero-installation standalone 64-bit Windows executable (`.exe`).
   - Uses custom high-resolution 512x512 icon (`icon-512.png`).
4. **Khyber Saanp Seedhi Pro Windows Portable EXE (`KhyberSaanpSeedhi.exe`)**:
   - Standalone portable Windows executable for Snakes & Ladders.

All binaries are automatically compiled and published to the GitHub Releases section under the `latest` tag, ready for direct distribution to clients and gamers.

---

# 🇵🇰 اردو زبان میں مکمل دستاویزات (Urdu Documentation)

## 1. ایپ کا تعارف اور پس منظر
**بنوں رائل لڈو اور خیبر سانپ سیڑھی پرو** پختونخوا کے روایتی اور ثقافتی کھیلوں کا ایک بے مثال اور جدید ترین سافٹ ویئر مجموعہ ہے جسے **یاسین اللہ (بنوں سافٹ ویئر سلوشنز)** نے تیار کیا ہے۔ یہ ایپ روایتی پختون حجرہ کلچر، بنوں اور لکی مروت کی 2 ڈائس والی تاریخی لڈو، اور خیبر پختونخوا کے سانپ سیڑھی کے تمام مستند اصولوں کو جدید ڈیجیٹل دنیا میں زندہ کرتی ہے۔

یہ مکمل ایپ بنا انٹرنیٹ کے (آف لائن) کام کرتی ہے، اور براؤزر کے علاوہ باقاعدہ اینڈرائیڈ ایپ (APK) اور ونڈوز کمپیوٹر کی پورٹیبل فائل (EXE) کے طور پر بھی فل اسکرین چلتی ہے۔

---

## 2. بنوں رائل لڈو کے تمام 45 روایتی، ٹورنامنٹ اور ہاؤس رولز کی مکمل وضاحت

1. **دو دانوں والی روایتی لڈو بمقابلہ 1 دانہ (`2 Dice / 1 Die`):**
   بنوں لڈو میں ہر باری پر 2 ڈائس پھینکے جاتے ہیں۔ آپ دونوں نمبر دو الگ گوٹیوں پر چل سکتے ہیں یا ایک ہی گوٹی پر دونوں کا مجموعہ اکٹھا چل سکتے ہیں۔
2. **صرف آخری ایک گوٹی رہنے پر 1 ڈائس کا اصول (`One Die on Last Bead`):**
   جب کھلاڑی کی 3 گوٹیاں پکی ہو جائیں اور پورے بورڈ پر صرف آخری 1 گوٹی باقی رہے، تو کھیل خودکار طور پر 2 کی بجائے 1 ڈائس پر آ جاتا ہے۔ گھر کے اندر یا آخری پوائنٹ پر بھی خودکار 1 ڈائس چلتا ہے تاکہ گوٹی کبھی نہ پھنسے۔
3. **کلوز گیم بمقابلہ اوپن گیم (`Close Game Lock`):**
   کلوز گیم میں جب کوئی گوٹی پہلے ڈائس سے دشمن کا شکار کرتی ہے، تو وہ گوٹی اس باری کے باقی حصے کے لیے اسی خانے پر لاک (🔒) ہو جاتی ہے تاکہ دوسرا نمبر دوسری گوٹی کو ملے۔ اوپن گیم میں گوٹی لاک نہیں ہوتی۔
4. **شکار کے بعد ری رول میں بھی گوٹی لاک رہنا (`Keep Capturing Bead Locked on Bonus`):**
   کلوز گیم میں شکار کرنے والی گوٹی اسی باری کے تمام بونس رولز میں بھی اسی خانے پر لاک رہتی ہے۔
5. **شکار کرنے پر دوبارہ باری ملنا (`Bonus Roll on Kill`):**
   مخالف کی گوٹی مارنے پر کھلاڑی کو انعام کے طور پر دوبارہ ڈائس رول کرنے کی باری ملتی ہے۔
6. **چھکا آنے پر پہلے ہاتھ والی گوٹی نکالنا لازمی (`Mandatory Yard Spawn`):**
   اگر ہاتھ میں بند گوٹیاں موجود ہوں اور 6 آ جائے تو پہلے نئی گوٹی باہر نکالنا لازمی ہے، پہلے سے باہر چلتی گوٹی پر وہ 6 نہیں چل سکتا۔
7. **بغیر شکار گھر جانا منع — بلڈ گیٹ (`Blood Gate Loop`):**
   کم از کم 1 شکار کیے بغیر گھر کا دروازہ بند رہتا ہے۔ اگر بغیر شکار کے گوٹی دروازے پر پہنچ جائے تو وہ اندر جانے کے بجائے پورے بورڈ کا 52 خانوں کا چکر دوبارہ لگاتی ہے!
8. **میدانی صفایا پر شکار کینسل (`Ground Wipeout Resets Home Eligibility`):**
   اگر گھر میں داخل ہونے سے پہلے میدان میں موجود تمام گوٹیاں مر جائیں تو پرانا شکار ختم ہو جاتا ہے اور نیا شکار کرنا پڑتا ہے۔
9. **بغیر شکار صرف اکیلی میدانی گوٹی کا چکر (`Single Ground Loop Only Without Kill`):**
   جب تک شکار نہ ہو، گوٹی صرف اس وقت چکر کاٹ سکتی ہے جب وہ میدان میں اکیلی ہو۔
10. **شکار کے بعد اندر جانے یا باہر گھومنے کی مرضی (`Optional Outer Loop After Kill`):**
    شکار مکمل ہونے کے بعد کھلاڑی کی مرضی ہے کہ وہ گوٹی گھر کے اندر لے جائے یا مزید شکار کے لیے باہر چکر لگائے۔
11. **بغیر شکار تمام میدانی گوٹیاں جمع ہونے تک رکنا (`Wait at Gate Until All Ground Beads Gather`):**
    بغیر شکار والی گوٹی دروازے (خانہ 50) پر رک کر باقی میدانی گوٹیوں کے پہنچنے کا انتظار کرتی ہے۔
12. **گھر جانے کے لیے 2 شکار لازمی (`Two Kills for Home`):**
    دروازہ کھولنے کے لیے 1 کی بجائے 2 شکار کی کڑی شرط۔
13. **گھر کے قریب بقایا نمبر کا اصول (`Strict Home Remainder`):**
    اگر 2 ڈائس کا نمبر آیا اور ایک نمبر سے گوٹی پکی ہوتی ہے لیکن دوسرا نمبر چلنے کے لیے کوئی دوسری گوٹی موجود نہیں، تو فالتو نمبر ضائع کرنے کی اجازت نہیں ہوتی اور چال منسوخ ہو جاتی ہے۔
14. **لگاتار 3 چھکے یا 3 ڈبل سکس پر باری ضائع ہونا (`3 Consecutive Sixes Penalty`):**
    ایک ہی باری میں لگاتار 3 بار 6 یا 6+6 آنے پر پوری باری منسوخ ہو جاتی ہے۔
15. **دو ڈائس میں ایک چھکے پر بھی دوبارہ باری (`Single Six Re-Roll`):**
    عام طور پر 6+6 پر دوبارہ باری ملتی ہے، مگر اس آپشن سے 6+2 یا 6+4 پر بھی دوبارہ باری مل سکتی ہے۔
16. **اسٹیک رول — پہلے تمام باریاں اکٹھی پھینکنا (`Stack Roll Before Moving`):**
    چھکے یا شکار پر ملنے والی اضافی باریاں پہلے اکٹھی رول ہو کر ڈائس بار میں جمع ہوتی ہیں، پھر تمام نمبر اکٹھے چلے جاتے ہیں۔
17. **1 یا 6 دونوں پر گوٹی کھلنا (`Spawn on 1 and 6`):**
    ہاتھ سے گوٹی 6 کے علاوہ 1 پر بھی باہر آ سکتی ہے۔
18. **ڈبل سکس پر دو گوٹیاں باہر آنا (`Double Six Spawns Two`):**
    6+6 آنے پر خودکار طور پر ہاتھ سے 2 الگ گوٹیاں باہر نکلتی ہیں۔
19. **پہلی گوٹی پہلے سے باہر ہونا (`First Bead on Board`):**
    میچ کے آغاز پر ہی ہر کھلاڑی کی 1 تا 4 گوٹیاں پہلے سے باہر سٹاپ پر کھڑی ہوتی ہیں۔
20. **جوڑا راستہ بند کرنا — دیوار بننا (`Pair Blockade / Jora Wall`):**
    ایک ہی کھلاڑی یا ٹیم کی 2 گوٹیاں ایک خانے پر بیٹھ کر جوڑا (🧱 دیوار) بنا لیتی ہیں؛ مخالف گوٹی اس کے اوپر سے نہیں گزر سکتی۔
21. **ایک خانے کی تمام مخالف گوٹیاں مارنا (`Kill All Stacked Enemies`):**
    ایک ہی حملے میں اس خانے پر بیٹھی تمام دشمن گوٹیاں اکٹھی مر جاتی ہیں۔
22. **شکار ممکن ہو تو مارنا لازمی (`Mandatory Capture / Phoonk`):**
    اگر کسی نمبر سے دشمن کی گوٹی مر رہی ہو تو شکار والی چال ہی چلنا لازمی ہو گا۔
23. **2v2 آمنے سامنے کی ٹیمیں (`2v2 Team Mode`):**
    لال + پیلا بمقابلہ ہرا + نیلا۔ پارٹنر ایک دوسرے کو نہیں مارتے بلکہ ایک دوسرے پر بیٹھ کر محفوظ رہتے ہیں۔
24. **پارٹنر کی مدد کے لیے 1 ڈائس پر 6 لانا (`Partner Assist Requires Six`):**
    اپنی تمام گوٹیاں پکی کرنے کے بعد 1 ڈائس سے 6 لانے پر پارٹنر کی گوٹیوں کا 2 ڈائس کنٹرول ملتا ہے۔
25. **گوٹی پکی ہونے پر دوبارہ باری (`Bonus Roll on Home`):**
    کوئی بھی گوٹی گھر پہنچنے پر انعام میں دوبارہ باری ملتی ہے۔
26. **چھکے یا ڈبل سکس پر دوبارہ باری (`Double Six Bonus`):**
    چھکا یا 6+6 آنے پر اضافی باری۔
27. **سٹار / سٹاپ خانوں پر گوٹی کا محفوظ رہنا (`Safe Stop Immunity`):**
    تمام 8 سٹاپ خانوں پر گوٹی مکمل محفوظ رہتی ہے۔
28. **3 بار وقت ختم ہونے پر خودکار بوٹ اور سیٹ واپس لینا (`3-Timeouts Bot Takeover`):**
    3 بار ٹائمر ختم ہونے پر کمپیوٹر بوٹ باری سنبھال لیتا ہے؛ "👤 Reclaim Seat" بٹن سے ایک سیکنڈ میں کنٹرول واپس مل جاتا ہے۔
29. **الٹا شکار — پیچھے وار کرنا (`Reverse Kill / Backstab`):**
    اگر 1 یا 2 کا دانہ آئے تو گوٹی پیچھے (-1 یا -2) چل کر اپنے بالکل پیچھے بیٹھی دشمن گوٹی کو کاٹ سکتی ہے!
30. **دوست کا شکار — 2v2 میں فرینڈلی فائر (`Friendly Fire in 2v2`):**
    اگر چاہیں تو ٹیم میچ میں بھی پارٹنر پر اترنے سے اس کی گوٹی کٹ جائے گی۔
31. **خودکش حملہ — جوڑے پر بمبار (`Kamikaze Jora Destruction`):**
    مخالف کے جوڑے (2 گوٹیوں) پر حملہ کرنے سے حملہ آور گوٹی اور دونوں مدافعتی گوٹیاں سب اکٹھی فنا ہو جائیں گی۔
32. **ڈبل ون کا عذاب — سنیک آئیز پیلنٹی (`Snake Eyes 1+1 Penalty`):**
    دو ڈائس میں 1+1 آنے پر آپ کی سب سے آگے چلنے والی گوٹی خود بخود مر کر واپس یارڈ میں چلی جاتی ہے۔
33. **ہر خانے پر زیادہ سے زیادہ 2 گوٹیوں کی حد (`Max Stack Limit of 2`):**
    کسی بھی خانے (بشمول سٹاپ) پر 2 سے زیادہ گوٹیاں جمع نہیں ہو سکتیں تاکہ اوور کراؤڈنگ نہ ہو۔
34. **سخت قید — ہیوی جیل (`Heavy Jail / Hardcore Respawn`):**
    مرنے والی گوٹی سخت قید (⛓️) میں چلی جاتی ہے جسے دوبارہ میدان میں لانے کے لیے ڈبل سکس (6+6) یا دو مسلسل چھکے لانا لازمی ہوتا ہے۔
35. **تبادلہ — 6+1 پوزیشن ہائی جیک (`Position Hijack / 6+1 Swap`):**
    اگر 6+1 آ جائے اور آپ دشمن کی گوٹی پر اتریں، تو دشمن کی گوٹی مرنے کے بجائے آپ کی پرانی جگہ پر آ جائے گی اور آپ اس کی جگہ پر چلے جائیں گے!
36. **عارضی پناہ — نکلتے ہی امان (`Spawn Invincibility Shield`):**
    ہاتھ سے نئی نکلنے والی گوٹی کو ایک باری کے لیے حفاظتی شیلڈ (🛡️) مل جاتی ہے تاکہ کوئی اسے نکلتے ہی نہ مار سکے۔
37. **پھونک / کچی گوٹی کا جرمانہ (`Phook / Blown Bead Penalty`):**
    اگر آپ سے کوئی شکار ممکن تھا لیکن آپ نے جان بوجھ کر چھوڑ دیا، تو باری کے اختتام پر وہ گوٹی "پھونک" ہو کر مر جائے گی!
38. **باؤنس بیک — باؤنسنگ ہوم (`Bouncing Home Overshoot`):**
    اگر گھر پہنچنے کے لیے 2 چاہیے تھے مگر 5 آ گیا، تو گوٹی مرکز سے ٹکرا کر فالتو 3 خانے پیچھے اچھل جائے گی۔
39. **کیمپنگ پابندی — سٹاپ سے بے دخلی (`Anti-Camping Safe Eviction`):**
    کوئی گوٹی محفوظ سٹاپ پر مسلسل 3 باریاں نہیں بیٹھ سکتی؛ چوتھی باری پر اس کا تحفظ ختم ہو جائے گا اور دشمن اسے وہیں مار سکے گا!
40. **دیوار توڑ — ڈبل سکس سے جوڑا ختم (`Jora Breaker Double-6`):**
    مخالف کا ناقابل عبور جوڑا توڑنے یا اس کے اوپر سے چھلانگ لگانے کے لیے بالکل 6+6 لانا پڑتا ہے۔
41. **چنگی — خانہ نمبر 50 پر ٹول گیٹ (`The Toll Gate at Step 50`):**
    گھر میں داخل ہونے سے پہلے خانہ 50 پر رکنا اور بالکل پورا 1 لا کر دروازہ کھولنا لازمی ہوگا۔
42. **قصاص — قاتل سے بدلہ اور 10 خانوں کی چھلانگ (`Qisas +10 Bonus Jump`):**
    جو دشمن گوٹی آپ کو مارے گی اس پر قصاص کا نشان (⚖️) لگ جائے گا۔ اسے مارنے پر آپ کو فوری +10 خانوں کی مفت چھلانگ ملے گی!
43. **چھکے کا ضیاع — صرف نئی گوٹی نکالنا (`Strict Spawn-Only Sixes`):**
    چھکا صرف نئی گوٹی نکالنے کے لیے استعمال ہو سکے گا؛ اگر اندر کوئی گوٹی نہ ہو تو 6 ضائع ہو جائے گا۔
44. **تقسیم — 1 ڈائس میں جوفت نمبر توڑنا (`Dice Splitting 2+2 or 3+3`):**
    ایک ڈائس موڈ میں 4 آنے پر (2+2) اور 6 آنے پر (3+3) دو الگ گوٹیوں میں تقسیم کیا جا سکتا ہے۔
45. **ملٹی ماؤس ہارڈویئر لاک (`Multi-Mouse Lock for 2-4 Mice`):**
    ایک لیپ ٹاپ پر 2 سے 4 ماؤس لگائیں؛ ہر کھلاڑی کا ماؤس صرف اسی کی باری پر کام کرے گا!

---

### 3. تھری ڈی گھومنے والے دانے (True 3D Isometric Rolling Canvas Dice)
ایپ میں بورڈ کے چاروں کونوں میں کینوس پر براہ راست تھری ڈی ڈائس رینڈر ہوتے ہیں:
- دانے گرتے ہوئے حقیقت کی طرح گھومتے ہیں، بلندی پر جانے پر زمین پر ان کا سایہ ہلکا اور چوڑا ہوتا ہے اور گرنے پر ٹھوس ہو جاتا ہے۔
- دانوں کے اوپر، سامنے اور سائیڈ کے رخ پر شیڈنگ اور گہرائی نظر آتی ہے۔
- نمبر منتخب کرنے پر دانے کے گرد نیلے رنگ کا چمکدار ہالو (`#38bdf8`) ظاہر ہوتا ہے۔

---

### 4. ملٹی ماؤس ہارڈویئر لاک (ایک لیپ ٹاپ پر 2 سے 4 ماؤس)
یہ اس ایپ کی تاریخی ایجاد ہے! آپ ایک ہی لیپ ٹاپ یا کمپیوٹر کے ساتھ 2، 3 یا 4 ماؤس (USB یا وائرلیس) لگا سکتے ہیں۔
- **ونڈوز (Windows):** ماؤس لگائیں اور TeamPlayer4 یا MouseMux سافٹ ویئر چلا کر ملٹی پوائنٹر آن کریں۔
- **لینکس (Linux):** بغیر کسی اضافی سافٹ ویئر کے xinput کمانڈ سے 4 الگ کرسر بنائیں۔
- **سیٹ لاکنگ:** ایپ کے اندر "Setup Mice" پر جا کر ہر کھلاڑی اپنے ماؤس سے اپنے رنگ والے خانے پر کلک کرے گا۔ اس کے بعد لال کی باری پر صرف لال کا ماؤس چلے گا، اگر ہرا یا نیلا ماؤس ہلائے گا تو کمپیوٹر اسے فوراً مسترد کر دے گا!

---

### 5. میچ ری پلے اسٹوڈیو، فریم اسکربر اور ویڈیو ڈاؤنلوڈ (Replay Studio & WebM Video Export)
اب آپ اپنے کھیلے گئے ہر میچ کا مکمل ویڈیو ری پلے دیکھ سکتے ہیں:
- **فریم بائے فریم جانچ:** آگے، پیچھے، یا شروع/آخر میں جانے کی مکمل سہولت۔
- **اہم لمحات پر چھلانگ:** شکار (Kills)، گھر پہنچنا (Home)، اور ڈبل چھکوں کے لمحات پر ایک کلک سے پہنچیں۔
- **ویڈیو بنانا (WebM Video Export):** میچ کا مکمل ویڈیو 480p، 720p یا 1080p کوالٹی میں ڈاؤنلوڈ کر کے واٹس ایپ یا یوٹیوب پر شیئر کریں۔
- **پورٹیبل فائل (JSON Replay):** پورا میچ فائل کی شکل میں ایکسپورٹ اور امپورٹ کریں۔

---

### 6. خود سیکھنے والی جدید مصنوعی ذہانت اور اسپیڈ کنٹرول (Generational Machine Learning AI)
- کمپیوٹر بوٹس انسان کے کھیلنے کے انداز، شکار کی عادتوں اور خطرناک خانوں کو خودکار طور پر سیکھتے ہیں (`aiKnowledgeBase`)۔
- جیسے جیسے آپ کھیلیں گے، بوٹس زیادہ ہوشیار اور کڑے حریف بنتے جائیں گے۔
- **رفتار کنٹرول:** بوٹ کی باری فوری (Instant/Blitz)، تیز (Fast)، حقیقت پسندانہ سوچ بچار (Dramatic)، یا اپنی مرضی کے ملی سیکنڈز میں سیٹ کریں۔

---

### 7. میچ آرگنائزر، ٹیگز اور اسٹار پننگ (Match Organizer, Tagging & Pinning)
- پرانے میچوں کے نام بدلیں، ریفری کے کمنٹس لکھیں، اور کیٹیگری لگائیں (ٹورنامنٹ، فیملی میچ، حجرہ نائٹ وغیرہ)۔
- پسندیدہ میچ کو اسٹار (⭐ Pin as Favorite) کر کے سب سے اوپر نمایاں رکھیں۔

---

### 8. جیت پر روایتی طنز و مزاح اور چھیڑ چھاڑ (Victory Roast & Banter Engine)
میچ جیتنے پر کمپیوٹر میچ کی صورتحال کے عین مطابق پشتو اور اردو میں دلچسپ روایتی طنز و مزاح کرتا ہے:
- صفر شکار والے کے لیے: *"صفر شکار! یار تم لڈو کھیلنے آئے تھے یا صرف چہل قدمی کرنے؟"*
- مسلسل ہارنے والے کے لیے: *"مسلسل ہار کا ہیٹ ٹرک! حجرے کی چائے اب تمہارے ذمے ہے!"*
- "Next Roast 🔄" دبا کر مزید نئے قہقہے اور جگتیں دیکھیں۔

---

### 9. خیبر سانپ سیڑھی پرو کے روایتی قوانین و فیچرز
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

### 10. کھلاڑیوں کا ریکارڈ، ہال آف فیم اور پرنٹ ایبل اسناد
- **انڈیکسڈ ڈی بی (IndexedDB) ڈیٹا بیس:** تمام کھلاڑیوں کا نام، ضلع (بنوں، پشاور، مردان، سوات، کوہاٹ، چارسدہ، ایبٹ آباد، ڈی آئی خان)، حجرہ رینک، فتوحات اور شکار ریکارڈ ہوتے ہیں۔
- **تصویر اپلوڈ:** کھلاڑی کی تصویر 100 کے بی سے کم سائز میں خودکار کمپریس ہو کر محفوظ ہوتی ہے۔
- **سرٹیفکیٹ پرنٹنگ:** ہر مکمل ہونے والے میچ کا باقاعدہ فتوحات کا سرٹیفکیٹ کمپیوٹر سے پرنٹ کیا جا سکتا ہے۔
- **256-بٹ پاس ورڈ انکرپٹڈ بیک اپ:** پورے ریکارڈ کا پاس ورڈ لگا کر محفوظ بیک اپ بنائیں جو کوئی دوسرا چوری یا خراب نہیں کر سکتا۔

---

### 11. بغیر انٹرنیٹ اور وائی فائی ملٹی پلیئر کھیلنے کا طریقہ
- **1 موبائل پر پاس اینڈ پلے:** ایک ہی موبائل پر 2 سے 4 دوست باری باری کھیل سکتے ہیں۔
- **ایک وائی فائی پر ریڈار روم:** ایک ہی وائی فائی یا موبائل ہاٹ اسپاٹ پر ریڈار پر قریبی دوست کا نام ظاہر ہوتا ہے، کلک کر کے چیلنج بھیجیں!
- **بغیر انٹرنیٹ کیو آر کوڈ (Offline QR P2P):** ایک موبائل پر کیو آر کوڈ بنائیں، دوسرا موبائل کیمرے سے اسکین کرے—بغیر کسی انٹرنیٹ کے دونوں موبائل آپس میں جڑ جائیں گے!

---

### 12. اینڈرائیڈ اے پی کے اور ونڈوز پورٹیبل فائلیں (Android APKs & Windows Portable EXEs)
اب یہ پورا پروجیکٹ خودکار طور پر براہ راست انسٹال ہونے والی فائلوں میں تبدیل ہوتا ہے:
- **اینڈرائیڈ اے پی کے (`BannuRoyaleLudo.apk` & `KhyberSaanpSeedhi.apk`):** موبائل میں انسٹال کریں، یہ بغیر کسی براؤزر کے فل اسکرین اصلی موبائل ایپ کی طرح کھلتی ہے۔
- **ونڈوز پورٹیبل فائل (`BannuRoyaleLudo.exe` & `KhyberSaanpSeedhi.exe`):** بغیر انسٹال کیے یو ایس بی یا کمپیوٹر سے ڈبل کلک کر کے چلائیں۔

---

### 👨💻 تیار کردہ (Created By)

<div align="center">

**یاسین اللہ (Yasin Ullah)** – بنوں سافٹ ویئر سلوشنز (Bannu Software Solutions)  
📱 واٹس ایپ (WhatsApp): **0336-1593533**  
🔗 لنکڈ ان: [LinkedIn Profile](https://www.linkedin.com/in/yasin-ullah-029229232/)  

💛 **محبت بھرا نذرانہ:** یہ کھیل اپنے چھوٹے بھائی **محب اللہ (Muhib Ullah)** کے نام وقف ہے۔

*پاکستان اور بین الاقوامی دنیا کے لیے جدید ترین روایتی و سائنسی سافٹ ویئر سلوشنز*

</div>

---

## ⚖️ Copyright & License (جملہ حقوق محفوظ ہیں)

**© 2026 Yasin Ullah — Bannu Software Solutions. All Rights Reserved.**

This software suite — **Bannu Royale Ludo** (`index.html`) and **Khyber Saanp Seedhi Pro**
(`snakes.html`), together with all source code, the rules engines, AI logic, UI/UX, artwork,
icons, text, build scripts and documentation — is the exclusive proprietary property of
**Yasin Ullah**.

**You may not**, without the author's prior written permission:

- copy, clone or mirror any part of the work;
- modify, adapt, re-skin, re-brand or create derivative works from it;
- reuse or extract any code, algorithm, layout, graphic or asset in another project;
- redistribute, publish, upload, bundle, sell, rent, sublicense or host it anywhere;
- reverse engineer, decompile or deobfuscate it;
- remove or alter this copyright notice, the author credits or the `LICENSE` file;
- publish it to any app store, storefront, registry or public repository;
- use it as training data for machine-learning / AI models.

Personal, private, non-commercial use and installation as a PWA on your own devices **is** allowed.

**Attribution (required for any use permitted in writing):**
> “Bannu Royale Ludo / Khyber Saanp Seedhi Pro — © 2026 Yasin Ullah, All Rights Reserved.”

Full legal terms: see **[LICENSE](./LICENSE)**.
Permission requests: WhatsApp `0336-1593533` ·
[LinkedIn](https://www.linkedin.com/in/yasin-ullah-029229232/)

---

## ⚖️ کاپی رائٹ اور قانونی حقوق (اردو خلاصہ)

**© 2026 یاسین اللہ — بنوں سافٹ ویئر سلوشنز۔ جملہ حقوق محفوظ ہیں۔**

یہ سافٹ ویئر، اس کا سارا کوڈ، گرافکس، ڈیزائن اور تحریر مکمل طور پر **یاسین اللہ** کی ذاتی ملکیت ہے۔
مصنف کی **تحریری اجازت کے بغیر** اس کی کاپی کرنا، تبدیل کرنا، دوبارہ استعمال کرنا، کسی اور
پروجیکٹ میں ڈالنا، تقسیم کرنا، شائع کرنا، بیچنا یا اس سے نیا ورژن بنانا **سختی سے ممنوع** ہے۔
اس نوٹس یا مصنف کے نام کو مٹانا بھی منع ہے۔

ذاتی، غیر تجارتی استعمال اور اپنے موبائل/کمپیوٹر پر ایپ کی تنصیب کی اجازت ہے۔
اجازت ملنے کی صورت میں کریڈٹ لکھنا لازمی ہوگا:
*“Bannu Royale Ludo / Khyber Saanp Seedhi Pro — © 2026 Yasin Ullah, All Rights Reserved.”*

مکمل شرائط کے لیے **[LICENSE](./LICENSE)** فائل دیکھیں · رابطہ: `0336-1593533`
