/**
 * Forge of Legions - Combat System
 * Handles all combat calculations, damage resolution, and special abilities
 */

const Combat = {
    // Calculate attack damage
    calculateDamage: (attacker, defender, gameState = null) => {
        const attackerStats = attacker.getEffectiveStats();
        const defenderStats = defender.getEffectiveStats();

        // Base damage calculation
        let baseDamage = attackerStats.attack;

        // Defense reduction
        const defenseReduction = Math.floor(defenderStats.defense * 0.5);
        let finalDamage = Math.max(1, baseDamage - defenseReduction);

        // Check for passive abilities that modify damage
        const attackerAbilities = attacker.getAbilities();

        // Charge bonus (cavalry)
        const chargeAbility = attackerAbilities.find(a => a.id === 'charge');
        if (chargeAbility && attacker.movedThisTurn >= 3) {
            finalDamage += 3;
        }

        // Berserk bonus
        const berserkAbility = attackerAbilities.find(a => a.id === 'berserk');
        if (berserkAbility && attacker.currentHealth < attacker.maxHealth / 2) {
            finalDamage += 2;
        }

        // Backstab bonus (check position)
        const backstabAbility = attackerAbilities.find(a => a.id === 'backstab');
        if (backstabAbility && gameState) {
            const flanking = Combat.checkFlanking(attacker, defender, gameState);
            if (flanking) {
                finalDamage += 3;
            }
        }

        // Critical hit (10% chance, +50% damage)
        const critRoll = Math.random();
        const isCritical = critRoll < 0.1;
        if (isCritical) {
            finalDamage = Math.floor(finalDamage * 1.5);
        }

        // Ethereal damage reduction
        const etherealAbility = defender.getAbilities().find(a => a.id === 'ethereal');
        if (etherealAbility && attacker.type !== 'spellcaster') {
            finalDamage = Math.floor(finalDamage * 0.5);
        }

        return {
            damage: finalDamage,
            isCritical,
            attackerStats,
            defenderStats
        };
    },

    // Check if attacker is flanking defender
    checkFlanking: (attacker, defender, gameState) => {
        // Simple flanking: not attacking from the front
        const dx = attacker.position.x - defender.position.x;
        const dy = attacker.position.y - defender.position.y;

        // Assume defender faces toward player 1's side (top of map)
        // Flanking if attacking from sides or behind
        if (defender.owner === 'player1') {
            return dy >= 0; // Attack from below or sides
        } else {
            return dy <= 0; // Attack from above or sides
        }
    },

    // Execute attack
    executeAttack: async (attacker, defender, gameState) => {
        const damageResult = Combat.calculateDamage(attacker, defender, gameState);

        // Apply damage
        const defenseResult = defender.takeDamage(damageResult.damage);

        // Life drain (vampire)
        const lifeDrainAbility = attacker.getAbilities().find(a => a.id === 'life_drain');
        let healedAmount = 0;
        if (lifeDrainAbility) {
            healedAmount = attacker.heal(Math.floor(damageResult.damage * 0.5));
        }

        // Mark attacker as having acted
        attacker.hasActed = true;

        // Build result
        const result = {
            attacker: attacker.id,
            defender: defender.id,
            damage: damageResult.damage,
            isCritical: damageResult.isCritical,
            defenderKilled: defenseResult.killed,
            defenderHealth: defender.currentHealth,
            attackerHealed: healedAmount
        };

        // Check for undying (skeleton resurrection)
        if (defenseResult.killed) {
            const undyingAbility = defender.getAbilities().find(a => a.id === 'undying');
            if (undyingAbility && Math.random() < 0.25) {
                defender.currentHealth = 1;
                result.defenderKilled = false;
                result.resurrected = true;
            }
        }

        // Trigger callbacks
        if (gameState && gameState.onCombatResult) {
            await gameState.onCombatResult(result);
        }

        return result;
    },

    // Execute ability
    executeAbility: async (unit, ability, target, gameState) => {
        const result = {
            unit: unit.id,
            ability: ability.id,
            targets: [],
            effects: []
        };

        switch (ability.id) {
            case 'fireball':
                // Damage main target
                const mainDamage = ability.damage;
                const mainTarget = gameState.getUnitAt(target);
                if (mainTarget && mainTarget.owner !== unit.owner) {
                    const dmgResult = mainTarget.takeDamage(mainDamage);
                    result.targets.push({
                        unitId: mainTarget.id,
                        damage: mainDamage,
                        killed: dmgResult.killed
                    });
                }

                // Splash damage to adjacent
                const splashTargets = gameState.getUnitsInRadius(target, 1);
                for (const splashTarget of splashTargets) {
                    if (splashTarget.owner !== unit.owner && splashTarget.id !== mainTarget?.id) {
                        const splashResult = splashTarget.takeDamage(ability.splashDamage);
                        result.targets.push({
                            unitId: splashTarget.id,
                            damage: ability.splashDamage,
                            killed: splashResult.killed,
                            splash: true
                        });
                    }
                }
                break;

            case 'volley':
                const volleyTargets = gameState.getUnitsInRadius(target, 2);
                const volleyDamage = Math.floor(unit.getEffectiveStats().attack * 0.5);
                for (const volleyTarget of volleyTargets) {
                    if (volleyTarget.owner !== unit.owner) {
                        const dmgResult = volleyTarget.takeDamage(volleyDamage);
                        result.targets.push({
                            unitId: volleyTarget.id,
                            damage: volleyDamage,
                            killed: dmgResult.killed
                        });
                    }
                }
                break;

            case 'heal':
            case 'spirit_heal':
                const healTarget = gameState.getUnitAt(target);
                if (healTarget && healTarget.owner === unit.owner) {
                    const healed = healTarget.heal(ability.healAmount || 5);
                    result.targets.push({
                        unitId: healTarget.id,
                        healed
                    });
                }
                break;

            case 'waaagh':
                const alliedUnits = gameState.getUnitsForPlayer(unit.owner);
                for (const ally of alliedUnits) {
                    ally.statusEffects.push({
                        id: 'waaagh_buff',
                        name: 'WAAAGH!',
                        duration: 2,
                        statModifiers: { attack: 2 }
                    });
                    result.targets.push({ unitId: ally.id, effect: 'attack_buff' });
                }
                break;

            case 'arcane_shield':
                unit.statusEffects.push({
                    id: 'arcane_shield',
                    name: 'Arcane Shield',
                    duration: 99,
                    blockNextAttack: true,
                    onDamage: (dmg) => {
                        unit.statusEffects = unit.statusEffects.filter(e => e.id !== 'arcane_shield');
                        return 0; // Block all damage
                    }
                });
                result.effects.push({ effect: 'shield_applied' });
                break;

            case 'rally':
                const nearbyAllies = gameState.getUnitsInRadius(unit.position, 2)
                    .filter(u => u.owner === unit.owner);
                for (const ally of nearbyAllies) {
                    ally.statusEffects = ally.statusEffects.filter(e =>
                        !e.isNegative
                    );
                    result.targets.push({ unitId: ally.id, effect: 'cleansed' });
                }
                break;

            case 'smash':
                const smashTargets = gameState.getUnitsInRadius(unit.position, 1)
                    .filter(u => u.owner !== unit.owner);
                for (const smashTarget of smashTargets) {
                    smashTarget.statusEffects.push({
                        id: 'stunned',
                        name: 'Stunned',
                        duration: 1,
                        isNegative: true,
                        statModifiers: { movement: -99 }
                    });
                    smashTarget.isExhausted = true;
                    result.targets.push({ unitId: smashTarget.id, effect: 'stunned' });
                }
                break;

            case 'terrify':
                const terrifyTargets = gameState.getUnitsInRadius(unit.position, 2)
                    .filter(u => u.owner !== unit.owner);
                for (const terrifyTarget of terrifyTargets) {
                    terrifyTarget.statusEffects.push({
                        id: 'terrified',
                        name: 'Terrified',
                        duration: 2,
                        isNegative: true,
                        statModifiers: { attack: -1 }
                    });
                    result.targets.push({ unitId: terrifyTarget.id, effect: 'terrified' });
                }
                break;

            case 'hide':
                unit.statusEffects.push({
                    id: 'hidden',
                    name: 'Hidden',
                    duration: 99,
                    untargetable: true,
                    onAction: () => {
                        unit.statusEffects = unit.statusEffects.filter(e => e.id !== 'hidden');
                    }
                });
                result.effects.push({ effect: 'hidden' });
                break;

            case 'summon_bats':
                // Summon bat swarms at adjacent positions
                const emptyAdjacent = Utils.getAdjacentCells(
                    unit.position.x, unit.position.y,
                    gameState.gridWidth, gameState.gridHeight
                ).filter(pos => !gameState.getUnitAt(pos));

                for (let i = 0; i < Math.min(2, emptyAdjacent.length); i++) {
                    const batSwarm = new Unit('skeleton', unit.owner, emptyAdjacent[i]);
                    batSwarm.name = 'Bat Swarm';
                    batSwarm.maxHealth = 3;
                    batSwarm.currentHealth = 3;
                    batSwarm.stats.attack = 2;
                    batSwarm.stats.movement = 4;
                    batSwarm.symbol = '🦇';
                    gameState.addUnit(batSwarm);
                    result.targets.push({ unitId: batSwarm.id, effect: 'summoned' });
                }
                break;
        }

        // Set cooldown and mark as acted
        unit.useAbility(ability.id);

        return result;
    },

    // Get valid attack targets for unit
    getValidTargets: (unit, gameState) => {
        if (unit.hasActed || unit.isExhausted) return [];

        const range = unit.getEffectiveStats().attackRange;
        const targets = [];

        for (const otherUnit of gameState.units) {
            if (otherUnit.owner === unit.owner) continue;
            if (otherUnit.currentHealth <= 0) continue;

            // Check for hidden/untargetable
            const isHidden = otherUnit.statusEffects.some(e => e.untargetable);
            if (isHidden) continue;

            const distance = Utils.gridDistance(unit.position, otherUnit.position);
            if (distance <= range) {
                targets.push(otherUnit);
            }
        }

        return targets;
    },

    // Get valid ability targets
    getValidAbilityTargets: (unit, ability, gameState) => {
        if (!unit.isAbilityReady(ability.id)) return [];

        const range = ability.range || unit.getEffectiveStats().attackRange;
        const targets = [];

        if (ability.type === 'active' && ability.range) {
            // Target-based ability
            const cells = Utils.getCellsInRange(
                unit.position.x, unit.position.y,
                range, gameState.gridWidth, gameState.gridHeight
            );

            for (const cell of cells) {
                // For healing, target allies
                if (ability.healAmount) {
                    const ally = gameState.getUnitAt(cell);
                    if (ally && ally.owner === unit.owner && ally.currentHealth < ally.maxHealth) {
                        targets.push(cell);
                    }
                }
                // For damage, target enemies or empty cells (AOE)
                else if (ability.damage || ability.areaOfEffect) {
                    targets.push(cell);
                }
            }
        }

        return targets;
    },

    // Check victory conditions
    checkVictory: (gameState) => {
        const player1Units = gameState.units.filter(
            u => u.owner === 'player1' && u.currentHealth > 0
        );
        const player2Units = gameState.units.filter(
            u => u.owner === 'player2' && u.currentHealth > 0
        );

        if (player1Units.length === 0) {
            return { winner: 'player2', reason: 'elimination' };
        }
        if (player2Units.length === 0) {
            return { winner: 'player1', reason: 'elimination' };
        }

        // Check objective-based victory
        if (gameState.objectives) {
            for (const objective of gameState.objectives) {
                const result = Combat.checkObjective(objective, gameState);
                if (result) return result;
            }
        }

        return null;
    },

    // Check specific objective
    checkObjective: (objective, gameState) => {
        switch (objective.type) {
            case 'capture':
                const unitOnObjective = gameState.getUnitAt(objective.position);
                if (unitOnObjective && unitOnObjective.owner === objective.captureBy) {
                    objective.turnsHeld = (objective.turnsHeld || 0) + 1;
                    if (objective.turnsHeld >= (objective.turnsRequired || 2)) {
                        return { winner: objective.captureBy, reason: 'objective_capture' };
                    }
                } else {
                    objective.turnsHeld = 0;
                }
                break;

            case 'survive':
                if (gameState.currentTurn >= objective.turns) {
                    return { winner: objective.survivor, reason: 'survival' };
                }
                break;

            case 'kill_hero':
                const targetHero = gameState.units.find(
                    u => u.id === objective.targetId || u.unitType === objective.targetType
                );
                if (!targetHero || targetHero.currentHealth <= 0) {
                    return { winner: objective.killer, reason: 'assassination' };
                }
                break;
        }
        return null;
    },

    // Calculate combat preview
    getCombatPreview: (attacker, defender, gameState) => {
        const damageResult = Combat.calculateDamage(attacker, defender, gameState);

        // Counter-attack calculation (if defender survives and in range)
        let counterDamage = 0;
        let canCounter = false;

        if (defender.currentHealth > damageResult.damage) {
            const counterRange = defender.getEffectiveStats().attackRange;
            const distance = Utils.gridDistance(attacker.position, defender.position);
            if (distance <= counterRange) {
                canCounter = true;
                counterDamage = Combat.calculateDamage(defender, attacker, gameState).damage;
            }
        }

        return {
            damage: damageResult.damage,
            isCriticalPossible: true,
            defenderWillDie: defender.currentHealth <= damageResult.damage,
            canCounter,
            counterDamage,
            attackerWillDie: canCounter && attacker.currentHealth <= counterDamage
        };
    }
};

// Make available globally
window.Combat = Combat;
