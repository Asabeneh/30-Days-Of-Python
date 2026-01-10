/**
 * Forge of Legions - Tutorial System
 * Interactive tutorial for new players
 */

const Tutorial = {
    currentStep: 0,
    isActive: false,
    highlightElement: null,

    // Tutorial steps
    steps: [
        {
            id: 'welcome',
            title: 'Welcome to Forge of Legions!',
            content: `
                <p>Forge of Legions is a tactical strategy game inspired by tabletop miniature wargames.</p>
                <p>In this tutorial, you'll learn the basics of:</p>
                <ul>
                    <li>Commanding your army</li>
                    <li>Moving and attacking with units</li>
                    <li>Using special abilities</li>
                    <li>Winning battles</li>
                </ul>
            `,
            image: null
        },
        {
            id: 'units_intro',
            title: 'Your Army',
            content: `
                <p>Your army consists of different <strong>unit types</strong>, each with unique strengths:</p>
                <div class="tutorial-units">
                    <div class="tutorial-unit">
                        <span class="symbol">⚔️</span>
                        <span class="name">Infantry</span>
                        <span class="desc">Balanced frontline fighters</span>
                    </div>
                    <div class="tutorial-unit">
                        <span class="symbol">🏹</span>
                        <span class="name">Ranged</span>
                        <span class="desc">Attack from distance</span>
                    </div>
                    <div class="tutorial-unit">
                        <span class="symbol">🐴</span>
                        <span class="name">Cavalry</span>
                        <span class="desc">Fast and powerful charges</span>
                    </div>
                    <div class="tutorial-unit">
                        <span class="symbol">🔮</span>
                        <span class="name">Mages</span>
                        <span class="desc">Devastating spells</span>
                    </div>
                </div>
            `
        },
        {
            id: 'stats',
            title: 'Unit Statistics',
            content: `
                <p>Each unit has important stats that determine their combat effectiveness:</p>
                <div class="tutorial-stats">
                    <div class="stat-item">
                        <span class="label">❤️ Health (HP)</span>
                        <span class="desc">How much damage they can take</span>
                    </div>
                    <div class="stat-item">
                        <span class="label">⚔️ Attack (ATK)</span>
                        <span class="desc">Damage dealt to enemies</span>
                    </div>
                    <div class="stat-item">
                        <span class="label">🛡️ Defense (DEF)</span>
                        <span class="desc">Reduces incoming damage</span>
                    </div>
                    <div class="stat-item">
                        <span class="label">🦶 Movement (MOV)</span>
                        <span class="desc">Tiles they can move per turn</span>
                    </div>
                </div>
                <p>Higher stats generally mean more powerful units!</p>
            `
        },
        {
            id: 'turns',
            title: 'Turn-Based Combat',
            content: `
                <p>Battles are fought in <strong>turns</strong>. On your turn, you can:</p>
                <ol>
                    <li><strong>Select</strong> a unit by clicking on it</li>
                    <li><strong>Move</strong> the unit to a new position</li>
                    <li><strong>Attack</strong> an enemy within range</li>
                    <li><strong>Use abilities</strong> (if available)</li>
                </ol>
                <p>Each unit can move AND attack once per turn.</p>
                <p>When you're done, click <strong>End Turn</strong> to let the enemy act.</p>
            `
        },
        {
            id: 'movement',
            title: 'Moving Units',
            content: `
                <p>To move a unit:</p>
                <ol>
                    <li>Click on one of your units to select it</li>
                    <li>Click the <strong>Move</strong> button</li>
                    <li>Valid movement tiles will be highlighted in <span class="highlight-blue">blue</span></li>
                    <li>Click a highlighted tile to move there</li>
                </ol>
                <p>Units cannot move through enemies or impassable terrain.</p>
                <p><em>Tip: Position your ranged units behind infantry for protection!</em></p>
            `
        },
        {
            id: 'combat',
            title: 'Attacking Enemies',
            content: `
                <p>To attack an enemy:</p>
                <ol>
                    <li>Select a unit that hasn't acted this turn</li>
                    <li>Click the <strong>Attack</strong> button</li>
                    <li>Valid targets will be highlighted in <span class="highlight-red">red</span></li>
                    <li>Click an enemy to attack them</li>
                </ol>
                <p><strong>Damage Calculation:</strong></p>
                <code>Damage = Attacker's ATK - (Defender's DEF / 2)</code>
                <p>There's also a 10% chance for a <strong>Critical Hit</strong> dealing 50% bonus damage!</p>
            `
        },
        {
            id: 'abilities',
            title: 'Special Abilities',
            content: `
                <p>Many units have <strong>special abilities</strong> that can turn the tide of battle!</p>
                <div class="tutorial-abilities">
                    <div class="ability-item">
                        <span class="name">Shield Wall (Legionnaire)</span>
                        <span class="desc">+2 DEF when next to ally</span>
                    </div>
                    <div class="ability-item">
                        <span class="name">Cavalry Charge (Knight)</span>
                        <span class="desc">+3 damage after moving 3+ tiles</span>
                    </div>
                    <div class="ability-item">
                        <span class="name">Fireball (Mage)</span>
                        <span class="desc">Area damage spell</span>
                    </div>
                </div>
                <p>Abilities with cooldowns need time to recharge after use.</p>
            `
        },
        {
            id: 'victory',
            title: 'Winning the Battle',
            content: `
                <p>You win by completing the battle <strong>objective</strong>!</p>
                <p>Common objectives include:</p>
                <ul>
                    <li><strong>Elimination:</strong> Defeat all enemy units</li>
                    <li><strong>Assassination:</strong> Kill the enemy hero</li>
                    <li><strong>Survival:</strong> Keep your units alive for X turns</li>
                    <li><strong>Capture:</strong> Hold a position for X turns</li>
                </ul>
                <p>Winning battles earns <strong>Gold</strong>, <strong>Experience</strong>, and unlocks new units!</p>
            `
        },
        {
            id: 'painting',
            title: 'Paint Your Army',
            content: `
                <p>Just like real miniature wargaming, you can <strong>customize</strong> your units!</p>
                <p>Visit the <strong>Paint Studio</strong> to:</p>
                <ul>
                    <li>Choose colors for each unit part</li>
                    <li>Create unique color schemes</li>
                    <li>Unlock new colors through gameplay</li>
                </ul>
                <p>Your custom paint schemes will be displayed in battle!</p>
                <p><em>This is a tribute to the hobby of painting miniatures that Warhammer fans love.</em></p>
            `
        },
        {
            id: 'armory',
            title: 'Build Your Army',
            content: `
                <p>In the <strong>Armory</strong>, you can build custom armies:</p>
                <ol>
                    <li>Each unit has a <strong>point cost</strong></li>
                    <li>Armies have a <strong>point limit</strong></li>
                    <li>Balance your army composition</li>
                    <li>Save different armies for different strategies</li>
                </ol>
                <p><em>Tip: A balanced army with infantry, ranged, and support units often works best!</em></p>
            `
        },
        {
            id: 'multiplayer',
            title: 'Challenge Other Players',
            content: `
                <p>Ready to test your skills against humans?</p>
                <p>In <strong>Multiplayer</strong> mode, you can:</p>
                <ul>
                    <li><strong>Create a game</strong> and share the code with a friend</li>
                    <li><strong>Join a game</strong> using a friend's code</li>
                    <li><strong>Quick Match</strong> to find a random opponent</li>
                </ul>
                <p>Climb the leaderboards and become the ultimate commander!</p>
            `
        },
        {
            id: 'ready',
            title: "You're Ready!",
            content: `
                <p>You now know the basics of Forge of Legions!</p>
                <p><strong>Quick Tips:</strong></p>
                <ul>
                    <li>Protect your ranged units and mages</li>
                    <li>Use terrain to your advantage</li>
                    <li>Save abilities for crucial moments</li>
                    <li>Learn enemy unit weaknesses</li>
                </ul>
                <p>Start with the <strong>Campaign</strong> to unlock more units and learn advanced tactics!</p>
                <p><strong>Good luck, Commander!</strong></p>
            `,
            showPlayButton: true
        }
    ],

    // Start tutorial
    start: () => {
        Tutorial.currentStep = 0;
        Tutorial.isActive = true;

        UI.showScreen('tutorial-screen');
        Tutorial.renderStep();

        // Update total steps
        document.getElementById('tutorial-total').textContent = Tutorial.steps.length;
    },

    // Render current step
    renderStep: () => {
        const step = Tutorial.steps[Tutorial.currentStep];
        const body = document.getElementById('tutorial-body');
        const stepDisplay = document.getElementById('tutorial-step');
        const prevBtn = document.getElementById('btn-tutorial-prev');
        const nextBtn = document.getElementById('btn-tutorial-next');

        if (!body) return;

        body.innerHTML = `
            <h2>${step.title}</h2>
            <div class="tutorial-content">
                ${step.content}
            </div>
            ${step.showPlayButton ? '<button class="btn-start-playing" id="btn-start-playing">Start Playing!</button>' : ''}
        `;

        stepDisplay.textContent = Tutorial.currentStep + 1;

        // Update button states
        prevBtn.disabled = Tutorial.currentStep === 0;

        if (Tutorial.currentStep === Tutorial.steps.length - 1) {
            nextBtn.textContent = 'Finish';
        } else {
            nextBtn.textContent = 'Next';
        }

        // Attach start playing button
        const startBtn = document.getElementById('btn-start-playing');
        if (startBtn) {
            startBtn.addEventListener('click', () => Tutorial.finish());
        }
    },

    // Go to next step
    next: () => {
        if (Tutorial.currentStep < Tutorial.steps.length - 1) {
            Tutorial.currentStep++;
            Tutorial.renderStep();

            if (window.AudioManager) {
                AudioManager.play('buttonClick');
            }
        } else {
            Tutorial.finish();
        }
    },

    // Go to previous step
    prev: () => {
        if (Tutorial.currentStep > 0) {
            Tutorial.currentStep--;
            Tutorial.renderStep();

            if (window.AudioManager) {
                AudioManager.play('buttonClick');
            }
        }
    },

    // Finish tutorial
    finish: () => {
        Tutorial.isActive = false;

        // Mark tutorial as completed
        Storage.updatePlayer({ tutorialCompleted: true });

        // Award completion bonus
        Storage.addGold(200);
        Storage.addExperience(100);

        UI.showToast('Tutorial completed! +200 Gold, +100 XP', 'success');

        // Return to main menu
        UI.showScreen('main-menu');

        if (window.AudioManager) {
            AudioManager.play('victory');
        }
    },

    // Skip tutorial
    skip: () => {
        Tutorial.isActive = false;
        UI.showScreen('main-menu');
    },

    // Highlight element (for interactive tutorials)
    highlight: (selector) => {
        Tutorial.clearHighlight();

        const element = document.querySelector(selector);
        if (!element) return;

        // Create overlay
        const overlay = document.createElement('div');
        overlay.className = 'tutorial-overlay';
        overlay.id = 'tutorial-highlight';

        // Create highlight box
        const rect = element.getBoundingClientRect();
        const highlight = document.createElement('div');
        highlight.className = 'tutorial-highlight-box';
        highlight.style.top = `${rect.top - 5}px`;
        highlight.style.left = `${rect.left - 5}px`;
        highlight.style.width = `${rect.width + 10}px`;
        highlight.style.height = `${rect.height + 10}px`;

        document.body.appendChild(overlay);
        document.body.appendChild(highlight);

        Tutorial.highlightElement = { overlay, highlight };
    },

    // Clear highlight
    clearHighlight: () => {
        if (Tutorial.highlightElement) {
            Tutorial.highlightElement.overlay.remove();
            Tutorial.highlightElement.highlight.remove();
            Tutorial.highlightElement = null;
        }
    },

    // Check if should show tutorial
    shouldShowTutorial: () => {
        const player = Storage.getPlayer();
        return !player.tutorialCompleted;
    },

    // Interactive battle tutorial
    startBattleTutorial: (battlefield) => {
        Tutorial.battleTutorial = {
            step: 0,
            battlefield: battlefield,
            steps: [
                {
                    text: 'Welcome to your first battle! Click on one of your units to select it.',
                    trigger: 'select_unit',
                    highlight: '.unit-token.player1'
                },
                {
                    text: 'Great! Now click the Move button to see where this unit can go.',
                    trigger: 'click_move',
                    highlight: '#btn-move'
                },
                {
                    text: 'Blue tiles show where you can move. Click one to move your unit.',
                    trigger: 'move_unit',
                    highlight: '.grid-cell.highlight-move'
                },
                {
                    text: 'Well done! Now click Attack to see which enemies you can hit.',
                    trigger: 'click_attack',
                    highlight: '#btn-attack'
                },
                {
                    text: 'Red tiles show enemies in range. Click an enemy to attack!',
                    trigger: 'attack_unit',
                    highlight: '.grid-cell.highlight-attack'
                },
                {
                    text: 'Excellent! You dealt damage to the enemy. Each unit can move and attack once per turn.',
                    trigger: 'continue'
                },
                {
                    text: 'When you\'re done with all your units, click End Turn.',
                    trigger: 'end_turn',
                    highlight: '#btn-end-turn'
                },
                {
                    text: 'Now it\'s the enemy\'s turn. Watch their moves, then plan your counter!',
                    trigger: 'continue'
                }
            ]
        };

        Tutorial.showBattleTip(Tutorial.battleTutorial.steps[0]);
    },

    // Show battle tip
    showBattleTip: (step) => {
        let tip = document.getElementById('battle-tutorial-tip');

        if (!tip) {
            tip = document.createElement('div');
            tip.id = 'battle-tutorial-tip';
            tip.className = 'battle-tutorial-tip';
            document.body.appendChild(tip);
        }

        tip.innerHTML = `
            <div class="tip-content">
                <p>${step.text}</p>
                ${step.trigger === 'continue' ? '<button class="tip-continue">Continue</button>' : ''}
            </div>
        `;

        tip.style.display = 'block';

        if (step.highlight) {
            Tutorial.highlight(step.highlight);
        }

        if (step.trigger === 'continue') {
            tip.querySelector('.tip-continue').addEventListener('click', () => {
                Tutorial.advanceBattleTutorial();
            });
        }
    },

    // Advance battle tutorial
    advanceBattleTutorial: () => {
        Tutorial.clearHighlight();

        if (!Tutorial.battleTutorial) return;

        Tutorial.battleTutorial.step++;

        if (Tutorial.battleTutorial.step >= Tutorial.battleTutorial.steps.length) {
            // Tutorial complete
            const tip = document.getElementById('battle-tutorial-tip');
            if (tip) tip.style.display = 'none';
            Tutorial.battleTutorial = null;
            return;
        }

        Tutorial.showBattleTip(Tutorial.battleTutorial.steps[Tutorial.battleTutorial.step]);
    },

    // Trigger battle tutorial event
    triggerEvent: (eventType) => {
        if (!Tutorial.battleTutorial) return;

        const currentStep = Tutorial.battleTutorial.steps[Tutorial.battleTutorial.step];
        if (currentStep.trigger === eventType) {
            setTimeout(() => Tutorial.advanceBattleTutorial(), 500);
        }
    }
};

// Make available globally
window.Tutorial = Tutorial;
