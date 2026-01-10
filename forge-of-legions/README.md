# Forge of Legions

> A tactical miniature wargame for web and mobile. Build armies, paint units, conquer realms!

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Platform](https://img.shields.io/badge/platform-Web%20%7C%20iOS%20%7C%20Android-green)
![License](https://img.shields.io/badge/license-MIT-yellow)

## Overview

Forge of Legions brings the beloved experience of tabletop miniature wargaming to your browser and mobile device. Inspired by games like Warhammer, this turn-based tactical game features army building, unit customization, and strategic combat.

### Key Features

- **Turn-Based Combat**: Deep tactical gameplay with movement, attacks, and special abilities
- **Three Factions**: Empire, Horde, and Undead - each with unique playstyles
- **Paint Studio**: Customize unit colors just like painting real miniatures
- **Campaign Mode**: Story-driven missions with progressive difficulty
- **Multiplayer**: Challenge friends with shareable game codes
- **No Pay-to-Win**: All gameplay content earnable through play

## Quick Start

### Play in Browser

Simply open `index.html` in a modern web browser:

```bash
cd forge-of-legions
open index.html  # macOS
start index.html # Windows
xdg-open index.html # Linux
```

### Development Server

For development with hot reload:

```bash
# Using Python
python -m http.server 8000

# Using Node.js
npx serve
```

Then open `http://localhost:8000` in your browser.

## Project Structure

```
forge-of-legions/
├── index.html              # Main HTML file
├── manifest.json           # PWA manifest
├── src/
│   ├── js/
│   │   ├── game.js         # Main game controller
│   │   ├── battlefield.js  # Battle system
│   │   ├── combat.js       # Combat calculations
│   │   ├── units.js        # Unit definitions
│   │   ├── ai.js           # AI opponent
│   │   ├── campaign.js     # Campaign system
│   │   ├── painting.js     # Paint studio
│   │   ├── multiplayer.js  # Multiplayer system
│   │   ├── tutorial.js     # Tutorial system
│   │   ├── ui.js           # UI management
│   │   ├── storage.js      # Save/load system
│   │   ├── audio.js        # Sound effects
│   │   └── utils.js        # Utility functions
│   ├── css/
│   │   ├── main.css        # Core styles
│   │   ├── battlefield.css # Battle screen styles
│   │   ├── ui.css          # UI component styles
│   │   └── painting.css    # Paint studio styles
│   └── assets/
│       ├── images/         # Icons and graphics
│       └── sounds/         # Audio files (optional)
├── server/                 # Multiplayer server (optional)
└── docs/
    ├── APP_STORE_LISTING.md
    └── PRICING_STRATEGY.md
```

## Game Mechanics

### Units

Each unit has these core stats:
- **Health (HP)**: Damage capacity
- **Attack (ATK)**: Damage dealt
- **Defense (DEF)**: Damage reduction
- **Movement (MOV)**: Tiles per turn
- **Range**: Attack distance

### Combat

```
Damage = Attacker ATK - (Defender DEF / 2)
Critical Hit: 10% chance for 1.5x damage
```

### Factions

| Faction | Specialty | Units |
|---------|-----------|-------|
| Empire | Formations, versatility | Legionnaire, Archer, Knight, Mage, Captain |
| Horde | Raw power, numbers | Orc Brute, Goblin, Troll, Shaman |
| Undead | Attrition, resurrection | Skeleton, Vampire, Wraith |

## Building for Mobile

### iOS (Capacitor)

```bash
npm install @capacitor/core @capacitor/ios
npx cap init "Forge of Legions" com.forgeoflegions.app
npx cap add ios
npx cap sync
npx cap open ios
```

### Android (Capacitor)

```bash
npm install @capacitor/core @capacitor/android
npx cap add android
npx cap sync
npx cap open android
```

### PWA

The game is PWA-ready with `manifest.json`. Deploy to any static hosting (GitHub Pages, Netlify, Vercel) for installable web app functionality.

## Multiplayer Setup

For local testing, multiplayer uses `BroadcastChannel` API (same-browser tabs).

For production, deploy the WebSocket server:

```bash
cd server
npm install
npm start
```

Update `Multiplayer.serverUrl` in `multiplayer.js`.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## Roadmap

- [ ] Additional campaign chapters
- [ ] More factions (Elves, Dwarves, Demons)
- [ ] Ranked multiplayer with ELO
- [ ] Replay system
- [ ] AI difficulty levels
- [ ] Achievements system
- [ ] Social features

## Credits

Developed as a tribute to the tabletop miniature wargaming hobby. This is an original IP and is not affiliated with Games Workshop or Warhammer.

## License

MIT License - See LICENSE file for details.

---

**Build. Paint. Conquer.**
