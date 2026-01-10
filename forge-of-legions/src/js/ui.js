/**
 * Forge of Legions - UI System
 * Handles all user interface interactions
 */

const UI = {
    currentScreen: 'loading-screen',

    // Initialize UI
    init: () => {
        UI.setupNavigation();
        UI.setupActionButtons();
        UI.updatePlayerInfo();
    },

    // Show a screen
    showScreen: (screenId) => {
        document.querySelectorAll('.screen').forEach(screen => {
            screen.classList.remove('active');
        });

        const screen = document.getElementById(screenId);
        if (screen) {
            screen.classList.add('active');
            UI.currentScreen = screenId;

            // Screen-specific initialization
            UI.onScreenShow(screenId);
        }

        if (window.AudioManager) {
            AudioManager.play('buttonClick');
        }
    },

    // Screen-specific initialization
    onScreenShow: (screenId) => {
        switch (screenId) {
            case 'main-menu':
                UI.updatePlayerInfo();
                break;
            case 'campaign-screen':
                Campaign.renderMap(document.getElementById('campaign-map'));
                break;
            case 'armory-screen':
                UI.renderArmory();
                break;
            case 'painting-screen':
                PaintStudio.init();
                break;
            case 'multiplayer-screen':
                Multiplayer.init();
                break;
        }
    },

    // Setup navigation
    setupNavigation: () => {
        // Back buttons
        document.querySelectorAll('.back-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                const target = btn.dataset.target || 'main-menu';
                UI.showScreen(target);
            });
        });

        // Main menu buttons
        const menuButtons = {
            'btn-campaign': () => UI.showScreen('campaign-screen'),
            'btn-skirmish': () => Game.startSkirmish(),
            'btn-multiplayer': () => UI.showScreen('multiplayer-screen'),
            'btn-armory': () => UI.showScreen('armory-screen'),
            'btn-painting': () => UI.showScreen('painting-screen'),
            'btn-tutorial': () => Tutorial.start(),
            'btn-settings': () => UI.showScreen('settings-screen')
        };

        Object.entries(menuButtons).forEach(([id, handler]) => {
            const btn = document.getElementById(id);
            if (btn) btn.addEventListener('click', handler);
        });

        // Multiplayer buttons
        document.getElementById('btn-create-game')?.addEventListener('click', async () => {
            const code = await Multiplayer.createGame();
            document.getElementById('game-code-section').style.display = 'block';
            document.getElementById('join-section').style.display = 'none';
        });

        document.getElementById('btn-join-game')?.addEventListener('click', () => {
            document.getElementById('game-code-section').style.display = 'none';
            document.getElementById('join-section').style.display = 'block';
        });

        document.getElementById('btn-submit-code')?.addEventListener('click', () => {
            const code = document.getElementById('join-code-input').value;
            if (code.length === 4) {
                Multiplayer.joinGame(code);
            }
        });

        document.getElementById('btn-quick-match')?.addEventListener('click', () => {
            Multiplayer.quickMatch();
        });

        // Settings
        document.getElementById('btn-save-settings')?.addEventListener('click', () => {
            UI.saveSettings();
        });

        document.getElementById('btn-reset-progress')?.addEventListener('click', () => {
            if (confirm('Are you sure? This will reset all progress!')) {
                Storage.resetProgress();
                UI.showToast('Progress reset', 'info');
                UI.updatePlayerInfo();
            }
        });

        // Tutorial navigation
        document.getElementById('btn-tutorial-next')?.addEventListener('click', () => {
            Tutorial.next();
        });

        document.getElementById('btn-tutorial-prev')?.addEventListener('click', () => {
            Tutorial.prev();
        });
    },

    // Setup action buttons for battlefield
    setupActionButtons: () => {
        document.getElementById('btn-move')?.addEventListener('click', () => {
            if (Game.battlefield && Game.battlefield.selectedUnit) {
                Game.battlefield.showMovementRange(Game.battlefield.selectedUnit);
                Tutorial.triggerEvent('click_move');
            }
        });

        document.getElementById('btn-attack')?.addEventListener('click', () => {
            if (Game.battlefield && Game.battlefield.selectedUnit) {
                Game.battlefield.showAttackRange(Game.battlefield.selectedUnit);
                Tutorial.triggerEvent('click_attack');
            }
        });

        document.getElementById('btn-ability')?.addEventListener('click', () => {
            if (Game.battlefield && Game.battlefield.selectedUnit) {
                const abilities = Game.battlefield.selectedUnit.getAbilities()
                    .filter(a => a.type === 'active' && Game.battlefield.selectedUnit.isAbilityReady(a.id));

                if (abilities.length > 0) {
                    Game.battlefield.showAbilityRange(Game.battlefield.selectedUnit, abilities[0]);
                }
            }
        });

        document.getElementById('btn-end-turn')?.addEventListener('click', () => {
            if (Game.battlefield) {
                Game.battlefield.endTurn();
                Tutorial.triggerEvent('end_turn');
            }
        });

        document.getElementById('btn-battle-menu')?.addEventListener('click', () => {
            UI.showBattleMenu();
        });

        // Battle result continue
        document.getElementById('btn-result-continue')?.addEventListener('click', () => {
            UI.hideBattleResults();
            UI.showScreen('main-menu');
        });
    },

    // Update player info display
    updatePlayerInfo: () => {
        const player = Storage.getPlayer();
        const stats = Storage.getStats();
        const unlocks = Storage.getUnlocks();

        document.getElementById('player-name')?.textContent = player.name;
        document.getElementById('stat-victories')?.textContent = stats.totalVictories;
        document.getElementById('stat-units')?.textContent = unlocks.units.length;
        document.getElementById('stat-gold')?.textContent = Utils.formatNumber(player.gold);
    },

    // Render armory
    renderArmory: () => {
        const roster = document.getElementById('unit-roster');
        const selectedUnits = document.getElementById('selected-units');
        const unlocks = Storage.getUnlocks();

        if (!roster) return;

        roster.innerHTML = '';

        // Show unlocked units
        Object.entries(UnitTypes).forEach(([unitId, unit]) => {
            const isUnlocked = unlocks.units.includes(unitId);

            const card = document.createElement('div');
            card.className = `unit-card ${isUnlocked ? '' : 'locked'}`;

            card.innerHTML = `
                <div class="unit-symbol">${unit.symbol}</div>
                <div class="unit-info">
                    <h4>${unit.name}</h4>
                    <p class="unit-desc">${unit.description}</p>
                    <div class="unit-cost">${unit.pointCost} pts</div>
                </div>
                ${isUnlocked ? '<button class="btn-add-unit">Add</button>' : `<div class="unlock-cost">Unlock: ${unit.unlockCost || 0} Gold</div>`}
            `;

            if (isUnlocked) {
                card.querySelector('.btn-add-unit').addEventListener('click', () => {
                    UI.addToArmy(unitId);
                });
            } else if (unit.unlockCost) {
                card.addEventListener('click', () => {
                    UI.tryUnlockUnit(unitId);
                });
            }

            roster.appendChild(card);
        });

        // Show current army
        UI.renderCurrentArmy();
    },

    // Add unit to current army
    currentArmyUnits: [],
    maxArmyPoints: 1000,

    addToArmy: (unitId) => {
        const unit = UnitTypes[unitId];
        const currentPoints = UI.calculateArmyPoints();

        if (currentPoints + unit.pointCost > UI.maxArmyPoints) {
            UI.showToast('Army point limit reached!', 'error');
            return;
        }

        // Check hero limit
        if (unit.isHero) {
            const hasHero = UI.currentArmyUnits.some(u => UnitTypes[u.unitId].isHero);
            if (hasHero) {
                UI.showToast('Only one hero per army!', 'error');
                return;
            }
        }

        const existing = UI.currentArmyUnits.find(u => u.unitId === unitId);
        if (existing && !unit.isHero) {
            existing.count++;
        } else {
            UI.currentArmyUnits.push({ unitId, count: 1 });
        }

        UI.renderCurrentArmy();

        if (window.AudioManager) {
            AudioManager.play('select');
        }
    },

    removeFromArmy: (unitId) => {
        const index = UI.currentArmyUnits.findIndex(u => u.unitId === unitId);
        if (index >= 0) {
            if (UI.currentArmyUnits[index].count > 1) {
                UI.currentArmyUnits[index].count--;
            } else {
                UI.currentArmyUnits.splice(index, 1);
            }
            UI.renderCurrentArmy();
        }
    },

    calculateArmyPoints: () => {
        return UI.currentArmyUnits.reduce((total, item) => {
            return total + (UnitTypes[item.unitId].pointCost * item.count);
        }, 0);
    },

    renderCurrentArmy: () => {
        const container = document.getElementById('selected-units');
        const pointsDisplay = document.getElementById('army-points');

        if (!container) return;

        const points = UI.calculateArmyPoints();
        if (pointsDisplay) pointsDisplay.textContent = points;

        container.innerHTML = '';

        if (UI.currentArmyUnits.length === 0) {
            container.innerHTML = '<p class="empty-army">No units selected</p>';
            return;
        }

        UI.currentArmyUnits.forEach(item => {
            const unit = UnitTypes[item.unitId];
            const div = document.createElement('div');
            div.className = 'army-unit-item';
            div.innerHTML = `
                <span class="unit-symbol">${unit.symbol}</span>
                <span class="unit-name">${unit.name}</span>
                <span class="unit-count">x${item.count}</span>
                <span class="unit-points">${unit.pointCost * item.count} pts</span>
                <button class="btn-remove">-</button>
            `;

            div.querySelector('.btn-remove').addEventListener('click', () => {
                UI.removeFromArmy(item.unitId);
            });

            container.appendChild(div);
        });
    },

    // Try to unlock a unit
    tryUnlockUnit: (unitId) => {
        const unit = UnitTypes[unitId];
        const player = Storage.getPlayer();

        if (player.gold >= unit.unlockCost) {
            Storage.updatePlayer({ gold: player.gold - unit.unlockCost });
            Storage.unlockUnit(unitId);
            UI.showToast(`Unlocked ${unit.name}!`, 'success');
            UI.renderArmory();
            UI.updatePlayerInfo();
        } else {
            UI.showToast('Not enough gold!', 'error');
        }
    },

    // Save army
    saveArmy: () => {
        if (UI.currentArmyUnits.length === 0) {
            UI.showToast('Army is empty!', 'error');
            return;
        }

        const army = {
            id: Utils.generateId(),
            name: 'Custom Army',
            units: UI.currentArmyUnits,
            totalPoints: UI.calculateArmyPoints()
        };

        Storage.saveArmy(army);
        UI.showToast('Army saved!', 'success');
    },

    // Update selected unit info
    updateUnitInfo: (unit) => {
        const nameEl = document.getElementById('unit-name');
        const hpEl = document.getElementById('unit-hp');
        const hpTextEl = document.getElementById('unit-hp-text');
        const atkEl = document.getElementById('unit-atk');
        const defEl = document.getElementById('unit-def');
        const movEl = document.getElementById('unit-mov');
        const abilitiesEl = document.getElementById('unit-abilities');
        const portraitEl = document.getElementById('unit-portrait');

        if (!unit) {
            if (nameEl) nameEl.textContent = 'Select a Unit';
            if (hpTextEl) hpTextEl.textContent = '-';
            if (atkEl) atkEl.textContent = '-';
            if (defEl) defEl.textContent = '-';
            if (movEl) movEl.textContent = '-';
            if (abilitiesEl) abilitiesEl.innerHTML = '';
            return;
        }

        const stats = unit.getEffectiveStats();
        const hpPercent = (unit.currentHealth / unit.maxHealth) * 100;

        if (nameEl) nameEl.textContent = unit.name;
        if (hpEl) hpEl.style.width = `${hpPercent}%`;
        if (hpTextEl) hpTextEl.textContent = `${unit.currentHealth}/${unit.maxHealth}`;
        if (atkEl) atkEl.textContent = stats.attack;
        if (defEl) defEl.textContent = stats.defense;
        if (movEl) movEl.textContent = stats.movement;
        if (portraitEl) portraitEl.innerHTML = `<span class="portrait-symbol">${unit.symbol}</span>`;

        // Render abilities
        if (abilitiesEl) {
            abilitiesEl.innerHTML = '';
            unit.getAbilities().forEach(ability => {
                const ready = unit.isAbilityReady(ability.id);
                const cooldown = unit.cooldowns[ability.id] || 0;

                const abilityDiv = document.createElement('div');
                abilityDiv.className = `ability-item ${ready ? 'ready' : 'cooldown'}`;
                abilityDiv.innerHTML = `
                    <span class="ability-name">${ability.name}</span>
                    ${cooldown > 0 ? `<span class="cooldown-timer">${cooldown}</span>` : ''}
                `;
                abilityDiv.title = ability.description;
                abilitiesEl.appendChild(abilityDiv);
            });
        }
    },

    // Update turn indicator
    updateTurnIndicator: (turn, player) => {
        const turnEl = document.getElementById('turn-number');
        const phaseEl = document.getElementById('current-phase');
        const p1Name = document.getElementById('p1-name');
        const p2Name = document.getElementById('p2-name');

        if (turnEl) turnEl.textContent = `Turn ${turn}`;
        if (phaseEl) phaseEl.textContent = player === 'player1' ? 'Your Turn' : 'Enemy Turn';

        // Highlight current player
        document.querySelector('.player-panel.player-1')?.classList.toggle('active', player === 'player1');
        document.querySelector('.player-panel.player-2')?.classList.toggle('active', player === 'player2');
    },

    // Show battle results
    showBattleResults: (victory, stats, rewards) => {
        const modal = document.getElementById('battle-results');
        const title = document.getElementById('result-title');
        const losses = document.getElementById('result-losses');
        const kills = document.getElementById('result-kills');
        const turns = document.getElementById('result-turns');
        const rewardsContainer = document.querySelector('#result-rewards .rewards-list');

        if (!modal) return;

        if (title) title.textContent = victory ? 'Victory!' : 'Defeat';
        title?.classList.toggle('victory', victory);
        title?.classList.toggle('defeat', !victory);

        if (losses) losses.textContent = stats.unitsLost || 0;
        if (kills) kills.textContent = stats.unitsKilled || 0;
        if (turns) turns.textContent = stats.turns || 0;

        if (rewardsContainer && rewards) {
            rewardsContainer.innerHTML = '';
            if (rewards.gold) {
                rewardsContainer.innerHTML += `<div class="reward-item">💰 ${rewards.gold} Gold</div>`;
            }
            if (rewards.experience) {
                rewardsContainer.innerHTML += `<div class="reward-item">⭐ ${rewards.experience} XP</div>`;
            }
            if (rewards.gems) {
                rewardsContainer.innerHTML += `<div class="reward-item">💎 ${rewards.gems} Gems</div>`;
            }
        }

        modal.classList.add('active');

        if (window.AudioManager) {
            AudioManager.play(victory ? 'victory' : 'defeat');
        }
    },

    // Hide battle results
    hideBattleResults: () => {
        const modal = document.getElementById('battle-results');
        if (modal) modal.classList.remove('active');
    },

    // Show battle menu
    showBattleMenu: () => {
        const menu = document.createElement('div');
        menu.className = 'battle-menu-overlay';
        menu.innerHTML = `
            <div class="battle-menu">
                <h3>Menu</h3>
                <button class="menu-item" id="battle-resume">Resume</button>
                <button class="menu-item" id="battle-restart">Restart</button>
                <button class="menu-item" id="battle-settings">Settings</button>
                <button class="menu-item danger" id="battle-quit">Quit Battle</button>
            </div>
        `;

        document.body.appendChild(menu);

        menu.querySelector('#battle-resume').addEventListener('click', () => {
            menu.remove();
        });

        menu.querySelector('#battle-quit').addEventListener('click', () => {
            menu.remove();
            if (Game.battlefield?.isMultiplayer) {
                Multiplayer.surrender();
            }
            UI.showScreen('main-menu');
        });

        menu.querySelector('#battle-restart').addEventListener('click', () => {
            menu.remove();
            Game.restartBattle();
        });
    },

    // Show toast notification
    showToast: (message, type = 'info') => {
        const container = document.getElementById('toast-container');
        if (!container) return;

        const toast = document.createElement('div');
        toast.className = `toast toast-${type}`;
        toast.textContent = message;

        container.appendChild(toast);

        // Auto remove
        setTimeout(() => {
            toast.classList.add('fade-out');
            setTimeout(() => toast.remove(), 300);
        }, 3000);
    },

    // Save settings
    saveSettings: () => {
        const settings = {
            sfxVolume: parseInt(document.getElementById('sfx-volume')?.value) || 80,
            musicVolume: parseInt(document.getElementById('music-volume')?.value) || 60,
            battleSpeed: document.getElementById('battle-speed')?.value || 'normal',
            showGrid: document.getElementById('show-grid')?.checked ?? true
        };

        const playerName = document.getElementById('player-name-input')?.value;
        if (playerName) {
            Storage.updatePlayer({ name: playerName });
        }

        Storage.updateSettings(settings);

        if (window.AudioManager) {
            AudioManager.setSfxVolume(settings.sfxVolume);
            AudioManager.setMusicVolume(settings.musicVolume);
        }

        UI.showToast('Settings saved!', 'success');
        UI.showScreen('main-menu');
    },

    // Load settings into form
    loadSettingsForm: () => {
        const settings = Storage.getSettings();
        const player = Storage.getPlayer();

        const sfxVolume = document.getElementById('sfx-volume');
        const musicVolume = document.getElementById('music-volume');
        const battleSpeed = document.getElementById('battle-speed');
        const showGrid = document.getElementById('show-grid');
        const playerName = document.getElementById('player-name-input');

        if (sfxVolume) sfxVolume.value = settings.sfxVolume;
        if (musicVolume) musicVolume.value = settings.musicVolume;
        if (battleSpeed) battleSpeed.value = settings.battleSpeed;
        if (showGrid) showGrid.checked = settings.showGrid;
        if (playerName) playerName.value = player.name;
    }
};

// Make available globally
window.UI = UI;
