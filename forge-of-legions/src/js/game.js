/**
 * Forge of Legions - Main Game Controller
 * Ties all systems together and manages game flow
 */

const Game = {
    battlefield: null,
    currentMission: null,
    isInitialized: false,

    // Initialize the game
    init: async () => {
        console.log('Forge of Legions initializing...');

        // Initialize storage
        Storage.init();

        // Initialize audio
        AudioManager.init();

        // Initialize UI
        UI.init();

        // Simulate loading
        await Game.simulateLoading();

        // Check for daily rewards
        Game.checkDailyReward();

        // Check if should show tutorial
        if (Tutorial.shouldShowTutorial()) {
            UI.showScreen('main-menu');
            setTimeout(() => {
                if (confirm('Would you like to play the tutorial?')) {
                    Tutorial.start();
                }
            }, 500);
        } else {
            UI.showScreen('main-menu');
        }

        Game.isInitialized = true;
        console.log('Forge of Legions ready!');
    },

    // Simulate loading for polish
    simulateLoading: async () => {
        const progressBar = document.querySelector('.loading-progress');
        const loadingText = document.querySelector('.loading-text');

        const steps = [
            { progress: 20, text: 'Loading armies...' },
            { progress: 40, text: 'Preparing battlefield...' },
            { progress: 60, text: 'Sharpening swords...' },
            { progress: 80, text: 'Polishing armor...' },
            { progress: 100, text: 'Ready for battle!' }
        ];

        for (const step of steps) {
            if (progressBar) progressBar.style.width = `${step.progress}%`;
            if (loadingText) loadingText.textContent = step.text;
            await Utils.wait(300);
        }

        await Utils.wait(500);
    },

    // Check for daily reward
    checkDailyReward: () => {
        const check = Storage.checkDailyReward();
        if (check.available) {
            setTimeout(() => {
                const claim = confirm(
                    `Daily Reward Available!\n\nDay ${check.day}: ${check.rewards.gold} Gold` +
                    (check.rewards.gems ? ` + ${check.rewards.gems} Gems` : '') +
                    '\n\nClaim your reward?'
                );

                if (claim) {
                    const rewards = Storage.claimDailyReward();
                    UI.showToast(`Claimed: ${rewards.gold} Gold${rewards.gems ? ` + ${rewards.gems} Gems` : ''}!`, 'success');
                    UI.updatePlayerInfo();
                }
            }, 1000);
        }
    },

    // Start a skirmish battle
    startSkirmish: () => {
        // Get player's saved army or use default
        const armies = Storage.getArmies();
        const playerArmy = armies[0]?.units || [
            { unitId: 'warrior', count: 3 },
            { unitId: 'archer', count: 2 }
        ];

        // Generate AI army
        const aiArmy = AI.generateArmy(Storage.getArmies()[0]?.totalPoints || 250);

        Game.startBattle(playerArmy, aiArmy, {
            isSkirmish: true,
            aiControlled: true
        });
    },

    // Start a campaign mission
    startCampaignMission: (missionId) => {
        const mission = Campaign.getMission(missionId);
        if (!mission) return;

        Game.currentMission = mission;

        // Get player's army
        const armies = Storage.getArmies();
        const playerArmy = armies[0]?.units || [
            { unitId: 'warrior', count: 3 },
            { unitId: 'archer', count: 2 }
        ];

        Game.startBattle(playerArmy, mission.enemyArmy, {
            mission: mission,
            aiControlled: true,
            gridWidth: mission.gridSize?.width,
            gridHeight: mission.gridSize?.height,
            terrain: mission.terrain,
            objectives: mission.objectives
        });
    },

    // Start a multiplayer battle
    startMultiplayerBattle: (playerArmy, opponentArmy) => {
        Game.startBattle(playerArmy, opponentArmy, {
            isMultiplayer: true,
            aiControlled: false
        });
    },

    // Start battle
    startBattle: (player1Army, player2Army, options = {}) => {
        // Create battlefield
        Game.battlefield = new Battlefield({
            width: options.gridWidth || 10,
            height: options.gridHeight || 8
        });

        // Setup terrain
        if (options.terrain) {
            options.terrain.forEach(t => {
                Game.battlefield.addTerrain(t.x, t.y, t.type);
            });
        }

        // Setup objectives
        if (options.objectives) {
            Game.battlefield.objectives = options.objectives;
        }

        // Initialize battlefield
        const gridElement = document.getElementById('battlefield-grid');
        const canvasElement = document.getElementById('battlefield-canvas');

        if (gridElement && canvasElement) {
            Game.battlefield.init(gridElement, canvasElement);
        }

        // Setup armies
        Game.battlefield.setupFromArmies(player1Army, player2Army);

        // Configure player names
        Game.battlefield.player1Name = Storage.getPlayer().name;
        Game.battlefield.player2Name = options.mission?.name || 'Enemy';

        // Setup callbacks
        Game.battlefield.onTurnChange = (data) => {
            UI.updateTurnIndicator(data.turn, data.player);

            // AI turn
            if (options.aiControlled && data.player === 'player2') {
                setTimeout(() => {
                    AI.takeTurn(Game.battlefield);
                }, 500);
            }
        };

        Game.battlefield.onUnitSelect = (unit) => {
            UI.updateUnitInfo(unit);
            if (unit) {
                Tutorial.triggerEvent('select_unit');
            }
        };

        Game.battlefield.onVictory = (result) => {
            Game.handleBattleEnd(result, options);
        };

        // Setup multiplayer if needed
        if (options.isMultiplayer) {
            Multiplayer.setupMultiplayerBattle(Game.battlefield);
        }

        // Show battlefield screen
        UI.showScreen('battlefield-screen');

        // Update UI
        UI.updateTurnIndicator(1, 'player1');
        UI.updateUnitInfo(null);

        // Start battle tutorial if first battle
        if (options.mission?.id === 'tutorial_1') {
            Tutorial.startBattleTutorial(Game.battlefield);
        }

        // Audio
        AudioManager.startMusic();
    },

    // Handle battle end
    handleBattleEnd: (result, options) => {
        const victory = result.winner === 'player1';
        const stats = {
            unitsLost: Game.battlefield.battleStats.player1.unitsLost,
            unitsKilled: Game.battlefield.battleStats.player1.unitsKilled,
            damageDealt: Game.battlefield.battleStats.player1.damageDealt,
            turns: Game.battlefield.currentTurn
        };

        // Record battle in statistics
        Storage.recordBattle(
            victory,
            stats.unitsKilled,
            stats.unitsLost,
            stats.damageDealt,
            Game.battlefield.battleStats.player1.damageTaken || 0
        );

        // Handle campaign mission completion
        let rewards = null;
        if (victory && options.mission) {
            const stars = Campaign.calculateStars(options.mission, Game.battlefield.battleStats, stats.turns);
            Campaign.completeMission(options.mission.id, stars, options.mission.rewards);
            rewards = options.mission.rewards;
        } else if (victory) {
            // Skirmish rewards
            rewards = {
                gold: 50 + stats.unitsKilled * 10,
                experience: 25 + stats.unitsKilled * 5
            };
            Storage.addGold(rewards.gold);
            Storage.addExperience(rewards.experience);
        }

        // Update player stats
        if (victory) {
            const player = Storage.getPlayer();
            Storage.updatePlayer({ victories: player.victories + 1 });
        }

        // Stop music
        AudioManager.stopMusic();

        // Show results
        UI.showBattleResults(victory, stats, rewards);
    },

    // Restart current battle
    restartBattle: () => {
        if (Game.currentMission) {
            Game.startCampaignMission(Game.currentMission.id);
        } else {
            Game.startSkirmish();
        }
    },

    // Pause game
    pause: () => {
        if (Game.battlefield) {
            Game.battlefield.paused = true;
        }
    },

    // Resume game
    resume: () => {
        if (Game.battlefield) {
            Game.battlefield.paused = false;
        }
    },

    // Clean up
    cleanup: () => {
        if (Game.battlefield) {
            Game.battlefield = null;
        }
        Game.currentMission = null;
        AudioManager.stopMusic();
    }
};

// Start game when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    Game.init();
});

// Handle visibility change
document.addEventListener('visibilitychange', () => {
    if (document.hidden) {
        Game.pause();
    } else {
        Game.resume();
    }
});

// Make available globally
window.Game = Game;
