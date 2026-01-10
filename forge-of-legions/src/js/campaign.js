/**
 * Forge of Legions - Campaign System
 * Handles story missions and progression
 */

const Campaign = {
    // Campaign chapters
    chapters: {
        shattered_realms: {
            id: 'shattered_realms',
            name: 'The Shattered Realms',
            description: 'The Empire faces threats from all sides. Rally your forces and defend the realm!',
            missions: [
                {
                    id: 'tutorial_1',
                    name: 'First Command',
                    description: 'Learn the basics of commanding your forces in battle.',
                    difficulty: 'tutorial',
                    armyPoints: 100,
                    enemyArmy: [
                        { unitId: 'skeleton', count: 2 }
                    ],
                    rewards: { gold: 100, experience: 50 },
                    unlocks: [],
                    objectives: [
                        { type: 'elimination', description: 'Defeat all enemy units' }
                    ],
                    briefing: 'Commander, a small band of undead threatens our border village. Take your soldiers and eliminate this threat. This will be a good opportunity to learn the basics of combat.',
                    gridSize: { width: 8, height: 6 },
                    position: { x: 10, y: 80 }
                },
                {
                    id: 'mission_1',
                    name: 'Border Skirmish',
                    description: 'Orc raiders have crossed the border. Push them back!',
                    difficulty: 'easy',
                    armyPoints: 200,
                    enemyArmy: [
                        { unitId: 'orc_warrior', count: 2 },
                        { unitId: 'goblin', count: 3 }
                    ],
                    rewards: { gold: 150, experience: 75 },
                    unlocks: ['orc_warrior'],
                    starRequirements: {
                        1: { complete: true },
                        2: { maxTurns: 8 },
                        3: { noLosses: true }
                    },
                    briefing: 'A raiding party from the Savage Horde has been spotted near the eastern border. We must intercept them before they reach the farmlands.',
                    position: { x: 25, y: 65 }
                },
                {
                    id: 'mission_2',
                    name: 'The Haunted Keep',
                    description: 'Clear the undead from the abandoned fortress.',
                    difficulty: 'easy',
                    armyPoints: 250,
                    enemyArmy: [
                        { unitId: 'skeleton', count: 4 },
                        { unitId: 'ghost', count: 1 }
                    ],
                    rewards: { gold: 200, experience: 100, gems: 5 },
                    unlocks: ['ghost'],
                    terrain: [
                        { x: 3, y: 2, type: 'ruins' },
                        { x: 4, y: 2, type: 'ruins' },
                        { x: 3, y: 3, type: 'ruins' }
                    ],
                    position: { x: 40, y: 50 }
                },
                {
                    id: 'mission_3',
                    name: 'Ambush at Dawn',
                    description: 'Survive the goblin ambush until reinforcements arrive.',
                    difficulty: 'medium',
                    armyPoints: 200,
                    enemyArmy: [
                        { unitId: 'goblin', count: 6 },
                        { unitId: 'orc_warrior', count: 2 }
                    ],
                    rewards: { gold: 250, experience: 125 },
                    unlocks: ['goblin'],
                    objectives: [
                        { type: 'survive', turns: 5, description: 'Survive for 5 turns' }
                    ],
                    briefing: 'We\'ve walked into a trap! Hold your ground until reinforcements arrive.',
                    position: { x: 55, y: 60 }
                },
                {
                    id: 'mission_4',
                    name: 'The Troll Bridge',
                    description: 'A cave troll blocks the vital bridge. Defeat it!',
                    difficulty: 'medium',
                    armyPoints: 300,
                    enemyArmy: [
                        { unitId: 'troll', count: 1 },
                        { unitId: 'goblin', count: 4 }
                    ],
                    rewards: { gold: 300, experience: 150, gems: 10 },
                    unlocks: ['troll'],
                    terrain: [
                        { x: 4, y: 3, type: 'water' },
                        { x: 5, y: 3, type: 'water' },
                        { x: 4, y: 4, type: 'bridge' },
                        { x: 5, y: 4, type: 'bridge' }
                    ],
                    position: { x: 60, y: 45 }
                },
                {
                    id: 'mission_5',
                    name: 'Night of the Dead',
                    description: 'The vampire lord awakens. Stop the undead rising!',
                    difficulty: 'hard',
                    armyPoints: 400,
                    enemyArmy: [
                        { unitId: 'vampire', count: 1 },
                        { unitId: 'skeleton', count: 5 },
                        { unitId: 'ghost', count: 2 }
                    ],
                    rewards: { gold: 500, experience: 250, gems: 20 },
                    unlocks: ['vampire', 'undead'],
                    objectives: [
                        { type: 'kill_hero', targetType: 'vampire', description: 'Defeat the Vampire Lord' }
                    ],
                    briefing: 'A powerful vampire has risen and is raising an army of the dead. We must strike at its heart before the undead legion grows too powerful.',
                    position: { x: 75, y: 35 }
                },
                {
                    id: 'mission_6',
                    name: 'The Final Stand',
                    description: 'Defend the capital against the combined enemy assault!',
                    difficulty: 'hard',
                    armyPoints: 500,
                    enemyArmy: [
                        { unitId: 'orc_warrior', count: 3 },
                        { unitId: 'shaman', count: 1 },
                        { unitId: 'troll', count: 1 },
                        { unitId: 'skeleton', count: 4 }
                    ],
                    rewards: { gold: 1000, experience: 500, gems: 50 },
                    unlocks: ['shaman', 'captain'],
                    objectives: [
                        { type: 'capture', position: { x: 5, y: 7 }, captureBy: 'player2', turnsRequired: 3, description: 'Prevent enemies from holding the throne' }
                    ],
                    gridSize: { width: 12, height: 10 },
                    briefing: 'The enemy has united! The Horde and the Undead march on our capital together. This is our final stand. Victory or death!',
                    position: { x: 90, y: 20 }
                }
            ]
        }
    },

    currentChapter: 'shattered_realms',
    currentMissionIndex: 0,

    // Get current chapter
    getCurrentChapter: () => {
        return Campaign.chapters[Campaign.currentChapter];
    },

    // Get all missions for current chapter
    getMissions: () => {
        return Campaign.getCurrentChapter().missions;
    },

    // Get specific mission
    getMission: (missionId) => {
        for (const chapter of Object.values(Campaign.chapters)) {
            const mission = chapter.missions.find(m => m.id === missionId);
            if (mission) return mission;
        }
        return null;
    },

    // Check if mission is unlocked
    isMissionUnlocked: (missionIndex) => {
        if (missionIndex === 0) return true;

        const campaign = Storage.getCampaign();
        const missions = Campaign.getMissions();

        // Previous mission must be completed
        const prevMission = missions[missionIndex - 1];
        return campaign.completedMissions.includes(prevMission.id);
    },

    // Get mission stars
    getMissionStars: (missionId) => {
        const campaign = Storage.getCampaign();
        return campaign.stars[missionId] || 0;
    },

    // Calculate stars earned
    calculateStars: (mission, battleStats, turns) => {
        let stars = 0;

        if (!mission.starRequirements) {
            // Default: just completion
            return 1;
        }

        const reqs = mission.starRequirements;

        // Star 1: Complete mission
        if (reqs[1]?.complete) stars++;

        // Star 2: Turn limit
        if (reqs[2]?.maxTurns && turns <= reqs[2].maxTurns) stars++;

        // Star 3: No losses
        if (reqs[3]?.noLosses && battleStats.player1.unitsLost === 0) stars++;

        return Math.max(1, stars); // At least 1 star for completion
    },

    // Start a mission
    startMission: (missionId) => {
        const mission = Campaign.getMission(missionId);
        if (!mission) return null;

        // Create battlefield configuration
        const config = {
            width: mission.gridSize?.width || 10,
            height: mission.gridSize?.height || 8,
            mission: mission,
            terrain: mission.terrain || [],
            objectives: mission.objectives || [{ type: 'elimination' }]
        };

        return config;
    },

    // Complete mission
    completeMission: (missionId, stars, rewards) => {
        const mission = Campaign.getMission(missionId);
        if (!mission) return;

        // Save completion
        Storage.completeMission(missionId, stars);

        // Grant rewards
        if (rewards || mission.rewards) {
            const r = rewards || mission.rewards;
            if (r.gold) Storage.addGold(r.gold);
            if (r.experience) {
                const levelResult = Storage.addExperience(r.experience);
                if (levelResult.leveledUp) {
                    // Show level up notification
                    UI.showToast(`Level Up! You are now Rank ${levelResult.newRank}`, 'success');
                }
            }
            if (r.gems) {
                const player = Storage.getPlayer();
                Storage.updatePlayer({ gems: player.gems + r.gems });
            }
        }

        // Process unlocks
        if (mission.unlocks) {
            mission.unlocks.forEach(unlock => {
                if (UnitTypes[unlock]) {
                    Storage.unlockUnit(unlock);
                    UI.showToast(`New Unit Unlocked: ${UnitTypes[unlock].name}`, 'success');
                } else if (Factions[unlock]) {
                    Storage.unlockFaction(unlock);
                    UI.showToast(`New Faction Unlocked: ${Factions[unlock].name}`, 'success');
                }
            });
        }
    },

    // Get total stars for chapter
    getTotalStars: (chapterId) => {
        const chapter = Campaign.chapters[chapterId];
        if (!chapter) return { earned: 0, total: 0 };

        const campaign = Storage.getCampaign();
        let earned = 0;
        let total = chapter.missions.length * 3;

        chapter.missions.forEach(mission => {
            earned += campaign.stars[mission.id] || 0;
        });

        return { earned, total };
    },

    // Render campaign map
    renderMap: (container) => {
        container.innerHTML = '';
        const missions = Campaign.getMissions();
        const campaign = Storage.getCampaign();

        // Create path connections
        const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
        svg.setAttribute('class', 'campaign-paths');
        svg.setAttribute('width', '100%');
        svg.setAttribute('height', '100%');

        // Draw paths between missions
        for (let i = 0; i < missions.length - 1; i++) {
            const from = missions[i];
            const to = missions[i + 1];

            const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
            line.setAttribute('x1', `${from.position.x}%`);
            line.setAttribute('y1', `${from.position.y}%`);
            line.setAttribute('x2', `${to.position.x}%`);
            line.setAttribute('y2', `${to.position.y}%`);
            line.setAttribute('class', campaign.completedMissions.includes(from.id) ? 'path-complete' : 'path-locked');

            svg.appendChild(line);
        }

        container.appendChild(svg);

        // Create mission nodes
        missions.forEach((mission, index) => {
            const isUnlocked = Campaign.isMissionUnlocked(index);
            const isCompleted = campaign.completedMissions.includes(mission.id);
            const stars = Campaign.getMissionStars(mission.id);

            const node = document.createElement('div');
            node.className = `mission-node ${isCompleted ? 'completed' : ''} ${isUnlocked ? 'unlocked' : 'locked'}`;
            node.style.left = `${mission.position.x}%`;
            node.style.top = `${mission.position.y}%`;

            node.innerHTML = `
                <div class="node-icon">${isCompleted ? '✓' : (isUnlocked ? '⚔️' : '🔒')}</div>
                <div class="node-name">${mission.name}</div>
                <div class="node-stars">
                    ${'★'.repeat(stars)}${'☆'.repeat(3 - stars)}
                </div>
            `;

            if (isUnlocked) {
                node.addEventListener('click', () => Campaign.showMissionDetails(mission));
            }

            container.appendChild(node);
        });
    },

    // Show mission details
    showMissionDetails: (mission) => {
        const detailsPanel = document.getElementById('mission-details');
        if (!detailsPanel) return;

        const stars = Campaign.getMissionStars(mission.id);
        const isCompleted = Storage.getCampaign().completedMissions.includes(mission.id);

        detailsPanel.innerHTML = `
            <h3>${mission.name}</h3>
            <p class="mission-desc">${mission.description}</p>
            <div class="mission-difficulty">Difficulty: <span class="diff-${mission.difficulty}">${mission.difficulty}</span></div>
            <div class="mission-stars">
                ${'★'.repeat(stars)}${'☆'.repeat(3 - stars)}
            </div>
            ${mission.briefing ? `<div class="mission-briefing">"${mission.briefing}"</div>` : ''}
            <div class="mission-rewards">
                <h4>Rewards:</h4>
                <ul>
                    ${mission.rewards.gold ? `<li>💰 ${mission.rewards.gold} Gold</li>` : ''}
                    ${mission.rewards.experience ? `<li>⭐ ${mission.rewards.experience} XP</li>` : ''}
                    ${mission.rewards.gems ? `<li>💎 ${mission.rewards.gems} Gems</li>` : ''}
                </ul>
            </div>
            <button class="btn-start-mission" id="btn-start-mission" data-mission="${mission.id}">
                ${isCompleted ? 'Replay Mission' : 'Start Mission'}
            </button>
        `;

        // Attach event listener
        document.getElementById('btn-start-mission').addEventListener('click', () => {
            Game.startCampaignMission(mission.id);
        });
    }
};

// Make available globally
window.Campaign = Campaign;
