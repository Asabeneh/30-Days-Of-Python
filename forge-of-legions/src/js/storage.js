/**
 * Forge of Legions - Storage System
 * Handles saving/loading game data with localStorage
 */

const Storage = {
    KEYS: {
        PLAYER: 'fol_player',
        ARMIES: 'fol_armies',
        CAMPAIGN: 'fol_campaign',
        PAINT_SCHEMES: 'fol_paint_schemes',
        SETTINGS: 'fol_settings',
        UNLOCKS: 'fol_unlocks',
        STATS: 'fol_stats'
    },

    // Default player data
    defaultPlayer: {
        name: 'Commander',
        rank: 1,
        experience: 0,
        gold: 500,
        gems: 10,
        victories: 0,
        defeats: 0,
        tutorialCompleted: false,
        firstPlayDate: null,
        lastPlayDate: null,
        totalPlayTime: 0,
        dailyRewardDay: 0,
        lastDailyReward: null
    },

    // Default settings
    defaultSettings: {
        sfxVolume: 80,
        musicVolume: 60,
        battleSpeed: 'normal',
        showGrid: true,
        showDamageNumbers: true,
        autoEndTurn: false,
        confirmEndTurn: true,
        vibration: true
    },

    // Default unlocks
    defaultUnlocks: {
        units: ['warrior', 'archer', 'knight'],
        factions: ['empire'],
        campaigns: ['shattered_realms'],
        paintColors: [
            '#8B0000', '#006400', '#00008B', '#8B8B00',
            '#4B0082', '#FF4500', '#2F4F4F', '#D2691E',
            '#FFFFFF', '#000000', '#808080', '#C0C0C0',
            '#FFD700', '#B87333', '#CD7F32'
        ],
        achievements: []
    },

    // Default stats
    defaultStats: {
        totalBattles: 0,
        totalVictories: 0,
        totalDefeats: 0,
        unitsKilled: 0,
        unitsLost: 0,
        damageDealt: 0,
        damageTaken: 0,
        criticalHits: 0,
        perfectVictories: 0,
        longestWinStreak: 0,
        currentWinStreak: 0,
        favoriteUnit: null,
        multiplayerWins: 0,
        multiplayerLosses: 0
    },

    // Initialize storage with defaults
    init: () => {
        // Ensure all storage keys have values
        if (!Storage.get(Storage.KEYS.PLAYER)) {
            Storage.set(Storage.KEYS.PLAYER, {
                ...Storage.defaultPlayer,
                firstPlayDate: new Date().toISOString()
            });
        }

        if (!Storage.get(Storage.KEYS.ARMIES)) {
            Storage.set(Storage.KEYS.ARMIES, [Storage.getDefaultArmy()]);
        }

        if (!Storage.get(Storage.KEYS.CAMPAIGN)) {
            Storage.set(Storage.KEYS.CAMPAIGN, {
                currentMission: 0,
                completedMissions: [],
                stars: {}
            });
        }

        if (!Storage.get(Storage.KEYS.PAINT_SCHEMES)) {
            Storage.set(Storage.KEYS.PAINT_SCHEMES, {});
        }

        if (!Storage.get(Storage.KEYS.SETTINGS)) {
            Storage.set(Storage.KEYS.SETTINGS, Storage.defaultSettings);
        }

        if (!Storage.get(Storage.KEYS.UNLOCKS)) {
            Storage.set(Storage.KEYS.UNLOCKS, Storage.defaultUnlocks);
        }

        if (!Storage.get(Storage.KEYS.STATS)) {
            Storage.set(Storage.KEYS.STATS, Storage.defaultStats);
        }

        // Update last play date
        Storage.updatePlayer({ lastPlayDate: new Date().toISOString() });
    },

    // Get default starting army
    getDefaultArmy: () => ({
        id: Utils.generateId(),
        name: 'First Legion',
        faction: 'empire',
        units: [
            { unitId: 'warrior', count: 3 },
            { unitId: 'archer', count: 2 }
        ],
        totalPoints: 250
    }),

    // Generic get/set operations
    get: (key) => {
        try {
            const data = localStorage.getItem(key);
            return data ? JSON.parse(data) : null;
        } catch (e) {
            console.error('Storage get error:', e);
            return null;
        }
    },

    set: (key, value) => {
        try {
            localStorage.setItem(key, JSON.stringify(value));
            return true;
        } catch (e) {
            console.error('Storage set error:', e);
            return false;
        }
    },

    // Player operations
    getPlayer: () => Storage.get(Storage.KEYS.PLAYER),

    updatePlayer: (updates) => {
        const player = Storage.getPlayer();
        Storage.set(Storage.KEYS.PLAYER, { ...player, ...updates });
    },

    addGold: (amount) => {
        const player = Storage.getPlayer();
        Storage.updatePlayer({ gold: player.gold + amount });
    },

    addExperience: (amount) => {
        const player = Storage.getPlayer();
        let newExp = player.experience + amount;
        let newRank = player.rank;

        // Level up check (100 exp per level)
        while (newExp >= newRank * 100) {
            newExp -= newRank * 100;
            newRank++;
        }

        Storage.updatePlayer({
            experience: newExp,
            rank: newRank
        });

        return { leveledUp: newRank > player.rank, newRank };
    },

    // Army operations
    getArmies: () => Storage.get(Storage.KEYS.ARMIES) || [],

    saveArmy: (army) => {
        const armies = Storage.getArmies();
        const existingIndex = armies.findIndex(a => a.id === army.id);

        if (existingIndex >= 0) {
            armies[existingIndex] = army;
        } else {
            armies.push(army);
        }

        Storage.set(Storage.KEYS.ARMIES, armies);
    },

    deleteArmy: (armyId) => {
        const armies = Storage.getArmies().filter(a => a.id !== armyId);
        Storage.set(Storage.KEYS.ARMIES, armies);
    },

    // Campaign operations
    getCampaign: () => Storage.get(Storage.KEYS.CAMPAIGN),

    completeMission: (missionId, stars) => {
        const campaign = Storage.getCampaign();
        if (!campaign.completedMissions.includes(missionId)) {
            campaign.completedMissions.push(missionId);
        }
        campaign.stars[missionId] = Math.max(campaign.stars[missionId] || 0, stars);
        Storage.set(Storage.KEYS.CAMPAIGN, campaign);
    },

    // Paint schemes
    getPaintSchemes: () => Storage.get(Storage.KEYS.PAINT_SCHEMES) || {},

    savePaintScheme: (unitId, scheme) => {
        const schemes = Storage.getPaintSchemes();
        schemes[unitId] = scheme;
        Storage.set(Storage.KEYS.PAINT_SCHEMES, schemes);
    },

    // Settings operations
    getSettings: () => Storage.get(Storage.KEYS.SETTINGS),

    updateSettings: (updates) => {
        const settings = Storage.getSettings();
        Storage.set(Storage.KEYS.SETTINGS, { ...settings, ...updates });
    },

    // Unlocks operations
    getUnlocks: () => Storage.get(Storage.KEYS.UNLOCKS),

    unlockUnit: (unitId) => {
        const unlocks = Storage.getUnlocks();
        if (!unlocks.units.includes(unitId)) {
            unlocks.units.push(unitId);
            Storage.set(Storage.KEYS.UNLOCKS, unlocks);
            return true;
        }
        return false;
    },

    unlockFaction: (factionId) => {
        const unlocks = Storage.getUnlocks();
        if (!unlocks.factions.includes(factionId)) {
            unlocks.factions.push(factionId);
            Storage.set(Storage.KEYS.UNLOCKS, unlocks);
            return true;
        }
        return false;
    },

    unlockColor: (color) => {
        const unlocks = Storage.getUnlocks();
        if (!unlocks.paintColors.includes(color)) {
            unlocks.paintColors.push(color);
            Storage.set(Storage.KEYS.UNLOCKS, unlocks);
            return true;
        }
        return false;
    },

    isUnitUnlocked: (unitId) => {
        return Storage.getUnlocks().units.includes(unitId);
    },

    // Stats operations
    getStats: () => Storage.get(Storage.KEYS.STATS),

    updateStats: (updates) => {
        const stats = Storage.getStats();
        Storage.set(Storage.KEYS.STATS, { ...stats, ...updates });
    },

    recordBattle: (victory, unitsKilled, unitsLost, damageDealt, damageTaken) => {
        const stats = Storage.getStats();
        stats.totalBattles++;

        if (victory) {
            stats.totalVictories++;
            stats.currentWinStreak++;
            stats.longestWinStreak = Math.max(stats.longestWinStreak, stats.currentWinStreak);
            if (unitsLost === 0) stats.perfectVictories++;
        } else {
            stats.totalDefeats++;
            stats.currentWinStreak = 0;
        }

        stats.unitsKilled += unitsKilled;
        stats.unitsLost += unitsLost;
        stats.damageDealt += damageDealt;
        stats.damageTaken += damageTaken;

        Storage.set(Storage.KEYS.STATS, stats);
    },

    // Daily rewards
    checkDailyReward: () => {
        const player = Storage.getPlayer();
        const lastReward = player.lastDailyReward ? new Date(player.lastDailyReward) : null;
        const now = new Date();

        if (!lastReward ||
            now.getDate() !== lastReward.getDate() ||
            now.getMonth() !== lastReward.getMonth() ||
            now.getFullYear() !== lastReward.getFullYear()) {

            // Check if consecutive day
            const isConsecutive = lastReward &&
                (now.getTime() - lastReward.getTime()) < (48 * 60 * 60 * 1000);

            const newDay = isConsecutive ? (player.dailyRewardDay % 7) + 1 : 1;

            return {
                available: true,
                day: newDay,
                rewards: Storage.getDailyRewardForDay(newDay)
            };
        }

        return { available: false };
    },

    getDailyRewardForDay: (day) => {
        const rewards = [
            { gold: 100 },
            { gold: 150 },
            { gold: 200, gems: 5 },
            { gold: 250 },
            { gold: 300, gems: 10 },
            { gold: 400 },
            { gold: 500, gems: 20, specialUnit: 'veteran_warrior' }
        ];
        return rewards[day - 1] || rewards[0];
    },

    claimDailyReward: () => {
        const check = Storage.checkDailyReward();
        if (!check.available) return null;

        const player = Storage.getPlayer();

        Storage.updatePlayer({
            gold: player.gold + (check.rewards.gold || 0),
            gems: player.gems + (check.rewards.gems || 0),
            lastDailyReward: new Date().toISOString(),
            dailyRewardDay: check.day
        });

        if (check.rewards.specialUnit) {
            Storage.unlockUnit(check.rewards.specialUnit);
        }

        return check.rewards;
    },

    // Reset all progress
    resetProgress: () => {
        Object.values(Storage.KEYS).forEach(key => {
            localStorage.removeItem(key);
        });
        Storage.init();
    },

    // Export save data (for cloud saves)
    exportSave: () => {
        const saveData = {};
        Object.values(Storage.KEYS).forEach(key => {
            saveData[key] = Storage.get(key);
        });
        return btoa(JSON.stringify(saveData));
    },

    // Import save data
    importSave: (encodedData) => {
        try {
            const saveData = JSON.parse(atob(encodedData));
            Object.keys(saveData).forEach(key => {
                Storage.set(key, saveData[key]);
            });
            return true;
        } catch (e) {
            console.error('Import error:', e);
            return false;
        }
    }
};

// Make available globally
window.Storage = Storage;
