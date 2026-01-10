/**
 * Forge of Legions - AI System
 * Handles computer-controlled opponents
 */

const AI = {
    difficulty: 'normal', // easy, normal, hard

    // Difficulty settings
    settings: {
        easy: {
            thinkTime: 800,
            mistakeChance: 0.3,
            prioritizeWeak: false,
            useAbilities: false
        },
        normal: {
            thinkTime: 500,
            mistakeChance: 0.1,
            prioritizeWeak: true,
            useAbilities: true
        },
        hard: {
            thinkTime: 300,
            mistakeChance: 0,
            prioritizeWeak: true,
            useAbilities: true,
            predictCounters: true
        }
    },

    // Execute AI turn
    takeTurn: async (battlefield) => {
        const settings = AI.settings[AI.difficulty];
        const units = battlefield.getUnitsForPlayer('player2');

        // Sort units by initiative (higher goes first)
        units.sort((a, b) => b.getEffectiveStats().initiative - a.getEffectiveStats().initiative);

        for (const unit of units) {
            if (unit.currentHealth <= 0 || unit.isExhausted) continue;

            await Utils.wait(settings.thinkTime);

            // Decide action
            const action = AI.decideAction(unit, battlefield, settings);

            if (action) {
                await AI.executeAction(unit, action, battlefield);
            }
        }

        // End turn
        await Utils.wait(300);
        battlefield.endTurn();
    },

    // Decide what action to take
    decideAction: (unit, battlefield, settings) => {
        // Mistake chance (for easier difficulties)
        if (Math.random() < settings.mistakeChance) {
            return AI.getRandomAction(unit, battlefield);
        }

        // Priority 1: Use powerful abilities if available
        if (settings.useAbilities) {
            const abilityAction = AI.considerAbilities(unit, battlefield);
            if (abilityAction) return abilityAction;
        }

        // Priority 2: Attack if in range
        const attackAction = AI.considerAttack(unit, battlefield, settings);
        if (attackAction) return attackAction;

        // Priority 3: Move towards best target
        const moveAction = AI.considerMove(unit, battlefield, settings);
        if (moveAction) return moveAction;

        return null;
    },

    // Consider using abilities
    considerAbilities: (unit, battlefield) => {
        const abilities = unit.getAbilities().filter(a =>
            a.type === 'active' && unit.isAbilityReady(a.id)
        );

        for (const ability of abilities) {
            // Healing ability
            if (ability.healAmount) {
                const allies = battlefield.getUnitsForPlayer(unit.owner);
                const woundedAlly = allies.find(a =>
                    a.currentHealth < a.maxHealth * 0.6 &&
                    Utils.gridDistance(unit.position, a.position) <= (ability.range || 3)
                );

                if (woundedAlly) {
                    return {
                        type: 'ability',
                        ability,
                        target: woundedAlly.position
                    };
                }
            }

            // Damage ability
            if (ability.damage) {
                const targets = Combat.getValidAbilityTargets(unit, ability, battlefield);
                if (targets.length > 0) {
                    // Find target with most enemies nearby (for AOE)
                    let bestTarget = targets[0];
                    let bestScore = 0;

                    for (const target of targets) {
                        let score = 0;
                        const nearby = battlefield.getUnitsInRadius(target, ability.areaOfEffect || 1);
                        score = nearby.filter(u => u.owner !== unit.owner).length;

                        const directHit = battlefield.getUnitAt(target);
                        if (directHit && directHit.owner !== unit.owner) {
                            score += 2;
                            if (directHit.currentHealth <= ability.damage) {
                                score += 3; // Can kill
                            }
                        }

                        if (score > bestScore) {
                            bestScore = score;
                            bestTarget = target;
                        }
                    }

                    if (bestScore > 0) {
                        return {
                            type: 'ability',
                            ability,
                            target: bestTarget
                        };
                    }
                }
            }

            // Buff abilities (like WAAAGH)
            if (ability.id === 'waaagh') {
                const allies = battlefield.getUnitsForPlayer(unit.owner);
                if (allies.length >= 3) {
                    return {
                        type: 'ability',
                        ability,
                        target: unit.position
                    };
                }
            }
        }

        return null;
    },

    // Consider attacking
    considerAttack: (unit, battlefield, settings) => {
        if (unit.hasActed) return null;

        const targets = Combat.getValidTargets(unit, battlefield);
        if (targets.length === 0) return null;

        // Score each target
        const scoredTargets = targets.map(target => {
            let score = 0;
            const preview = Combat.getCombatPreview(unit, target, battlefield);

            // Can kill?
            if (preview.defenderWillDie) {
                score += 100;
            }

            // Prioritize weak targets
            if (settings.prioritizeWeak) {
                score += (1 - target.currentHealth / target.maxHealth) * 30;
            }

            // Avoid dangerous counters
            if (settings.predictCounters && preview.attackerWillDie) {
                score -= 150;
            } else if (preview.canCounter) {
                score -= preview.counterDamage * 2;
            }

            // Prioritize high-value targets
            const template = UnitTypes[target.unitType];
            if (template.isHero) score += 20;
            if (template.type === 'spellcaster') score += 15;

            // Consider damage efficiency
            score += preview.damage * 2;

            return { target, score, preview };
        });

        // Sort by score
        scoredTargets.sort((a, b) => b.score - a.score);

        if (scoredTargets.length > 0 && scoredTargets[0].score > 0) {
            return {
                type: 'attack',
                target: scoredTargets[0].target
            };
        }

        return null;
    },

    // Consider moving
    considerMove: (unit, battlefield, settings) => {
        if (unit.hasMoved) return null;

        const enemies = battlefield.getUnitsForPlayer('player1');
        if (enemies.length === 0) return null;

        // Find best position
        const validMoves = battlefield.getValidMovementCells(
            unit,
            unit.getEffectiveStats().movement
        );

        if (validMoves.length === 0) return null;

        // Score each move
        const scoredMoves = validMoves.map(pos => {
            let score = 0;

            // Check if moving here allows attack
            const tempPos = { ...unit.position };
            unit.position = pos;

            const targets = Combat.getValidTargets(unit, battlefield);
            if (targets.length > 0) {
                score += 50;

                // Best target killable?
                for (const target of targets) {
                    const preview = Combat.getCombatPreview(unit, target, battlefield);
                    if (preview.defenderWillDie) {
                        score += 30;
                    }
                }
            }

            unit.position = tempPos;

            // Move closer to nearest enemy
            let minDist = Infinity;
            for (const enemy of enemies) {
                const dist = Utils.gridDistance(pos, enemy.position);
                if (dist < minDist) minDist = dist;
            }
            score -= minDist * 5;

            // Cavalry charge bonus
            const chargeAbility = unit.getAbilities().find(a => a.id === 'charge');
            if (chargeAbility) {
                const moveDistance = Utils.gridDistance(unit.position, pos);
                if (moveDistance >= 3) score += 15;
            }

            // Avoid getting too close if ranged
            if (unit.getEffectiveStats().attackRange > 1) {
                if (minDist <= 1) score -= 20;
            }

            return { pos, score };
        });

        scoredMoves.sort((a, b) => b.score - a.score);

        if (scoredMoves.length > 0) {
            return {
                type: 'move',
                target: scoredMoves[0].pos
            };
        }

        return null;
    },

    // Get random action (for easy AI)
    getRandomAction: (unit, battlefield) => {
        const actions = [];

        // Add possible moves
        if (!unit.hasMoved) {
            const moves = battlefield.getValidMovementCells(unit, unit.getEffectiveStats().movement);
            moves.forEach(pos => {
                actions.push({ type: 'move', target: pos });
            });
        }

        // Add possible attacks
        if (!unit.hasActed) {
            const targets = Combat.getValidTargets(unit, battlefield);
            targets.forEach(target => {
                actions.push({ type: 'attack', target });
            });
        }

        if (actions.length === 0) return null;

        return actions[Math.floor(Math.random() * actions.length)];
    },

    // Execute the decided action
    executeAction: async (unit, action, battlefield) => {
        switch (action.type) {
            case 'move':
                await battlefield.moveUnit(unit, action.target);
                // After moving, check if can attack
                if (!unit.hasActed) {
                    const attackAction = AI.considerAttack(unit, battlefield, AI.settings[AI.difficulty]);
                    if (attackAction) {
                        await Utils.wait(300);
                        await AI.executeAction(unit, attackAction, battlefield);
                    }
                }
                break;

            case 'attack':
                await battlefield.executeAttack(unit, action.target);
                break;

            case 'ability':
                await battlefield.executeAbility(unit, action.ability, action.target);
                break;
        }
    },

    // Generate AI army based on difficulty and points
    generateArmy: (points, faction = null) => {
        const availableFactions = faction ? [faction] : Object.keys(Factions);
        const selectedFaction = availableFactions[Math.floor(Math.random() * availableFactions.length)];

        const factionData = Factions[selectedFaction];
        const army = [];
        let remainingPoints = points;

        // Get available units for faction
        const availableUnits = factionData.units
            .map(unitId => ({ id: unitId, ...UnitTypes[unitId] }))
            .sort((a, b) => b.pointCost - a.pointCost);

        // Fill army
        while (remainingPoints > 0) {
            const affordableUnits = availableUnits.filter(u => u.pointCost <= remainingPoints);
            if (affordableUnits.length === 0) break;

            // Mix of units - prefer variety
            let selectedUnit;

            if (AI.difficulty === 'hard') {
                // Hard AI picks optimal composition
                const hasHero = army.some(u => UnitTypes[u.unitId].isHero);
                const heroUnits = affordableUnits.filter(u => u.isHero);

                if (!hasHero && heroUnits.length > 0 && remainingPoints >= heroUnits[0].pointCost) {
                    selectedUnit = heroUnits[0];
                } else {
                    // Balance between infantry and support
                    const infantry = army.filter(u => UnitTypes[u.unitId].type === 'infantry').length;
                    const ranged = army.filter(u =>
                        UnitTypes[u.unitId].type === 'ranged' ||
                        UnitTypes[u.unitId].type === 'spellcaster'
                    ).length;

                    if (ranged < infantry / 2) {
                        const rangedUnits = affordableUnits.filter(u =>
                            u.type === 'ranged' || u.type === 'spellcaster'
                        );
                        selectedUnit = rangedUnits.length > 0 ? rangedUnits[0] : affordableUnits[0];
                    } else {
                        selectedUnit = affordableUnits[Math.floor(Math.random() * affordableUnits.length)];
                    }
                }
            } else {
                // Random selection for easier difficulties
                selectedUnit = affordableUnits[Math.floor(Math.random() * affordableUnits.length)];
            }

            // Add or increment unit
            const existing = army.find(u => u.unitId === selectedUnit.id);
            if (existing && !selectedUnit.isHero) {
                existing.count++;
            } else {
                army.push({ unitId: selectedUnit.id, count: 1 });
            }

            remainingPoints -= selectedUnit.pointCost;
        }

        return army;
    },

    // Set difficulty
    setDifficulty: (difficulty) => {
        if (AI.settings[difficulty]) {
            AI.difficulty = difficulty;
        }
    }
};

// Make available globally
window.AI = AI;
