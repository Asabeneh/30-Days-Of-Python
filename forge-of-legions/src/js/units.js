/**
 * Forge of Legions - Unit Definitions
 * Defines all unit types, their stats, abilities, and visual data
 */

const UnitTypes = {
    // ===================
    // EMPIRE FACTION
    // ===================
    warrior: {
        id: 'warrior',
        name: 'Legionnaire',
        faction: 'empire',
        type: 'infantry',
        description: 'Reliable frontline infantry with balanced stats.',
        lore: 'The backbone of any Imperial army, Legionnaires are trained from youth in the arts of sword and shield.',

        // Combat stats
        stats: {
            health: 10,
            attack: 4,
            defense: 3,
            movement: 3,
            attackRange: 1,
            initiative: 5
        },

        // Point cost for army building
        pointCost: 50,

        // Special abilities
        abilities: [
            {
                id: 'shield_wall',
                name: 'Shield Wall',
                description: '+2 Defense when adjacent to allied Legionnaire',
                type: 'passive',
                effect: (unit, gameState) => {
                    const adjacent = gameState.getAdjacentUnits(unit);
                    const hasAlly = adjacent.some(u => u.unitType === 'warrior' && u.owner === unit.owner);
                    return hasAlly ? { defense: 2 } : null;
                }
            }
        ],

        // Visual representation for painting
        paintParts: {
            armor: { name: 'Armor', default: '#4A4A4A' },
            cloth: { name: 'Cloth', default: '#8B0000' },
            skin: { name: 'Skin', default: '#DEB887' },
            shield: { name: 'Shield', default: '#C0C0C0' },
            weapon: { name: 'Weapon', default: '#808080' },
            trim: { name: 'Trim', default: '#FFD700' }
        },

        // ASCII/Emoji representation for grid
        symbol: '⚔️',
        symbolAlt: 'W'
    },

    archer: {
        id: 'archer',
        name: 'Longbowman',
        faction: 'empire',
        type: 'ranged',
        description: 'Skilled ranged unit. Weak in melee combat.',
        lore: 'Masters of the yew longbow, these sharpshooters can strike from afar with deadly accuracy.',

        stats: {
            health: 6,
            attack: 5,
            defense: 1,
            movement: 3,
            attackRange: 4,
            initiative: 6
        },

        pointCost: 60,

        abilities: [
            {
                id: 'volley',
                name: 'Volley',
                description: 'Attack all enemies in a 2-tile radius. 3 turn cooldown.',
                type: 'active',
                cooldown: 3,
                range: 4,
                areaOfEffect: 2,
                damage: 0.5, // 50% of normal attack
                effect: async (unit, target, gameState) => {
                    const enemies = gameState.getUnitsInRadius(target, 2)
                        .filter(u => u.owner !== unit.owner);
                    const damage = Math.floor(unit.stats.attack * 0.5);
                    for (const enemy of enemies) {
                        await gameState.dealDamage(unit, enemy, damage);
                    }
                }
            }
        ],

        paintParts: {
            armor: { name: 'Leather', default: '#8B4513' },
            cloth: { name: 'Tunic', default: '#228B22' },
            skin: { name: 'Skin', default: '#DEB887' },
            bow: { name: 'Bow', default: '#654321' },
            quiver: { name: 'Quiver', default: '#8B4513' }
        },

        symbol: '🏹',
        symbolAlt: 'A'
    },

    knight: {
        id: 'knight',
        name: 'Imperial Knight',
        faction: 'empire',
        type: 'cavalry',
        description: 'Heavy cavalry with high mobility and devastating charge.',
        lore: 'Noble warriors clad in blessed steel, Knights are the hammer of the Empire.',

        stats: {
            health: 14,
            attack: 6,
            defense: 4,
            movement: 5,
            attackRange: 1,
            initiative: 7
        },

        pointCost: 120,

        abilities: [
            {
                id: 'charge',
                name: 'Cavalry Charge',
                description: '+3 damage if moved 3+ tiles before attacking.',
                type: 'passive',
                effect: (unit, target, gameState) => {
                    const moveDistance = unit.movedThisTurn || 0;
                    return moveDistance >= 3 ? { attackBonus: 3 } : null;
                }
            },
            {
                id: 'trample',
                name: 'Trample',
                description: 'Deal 2 damage to enemy when moving through adjacent tile.',
                type: 'passive'
            }
        ],

        paintParts: {
            armor: { name: 'Plate Armor', default: '#C0C0C0' },
            tabard: { name: 'Tabard', default: '#000080' },
            plume: { name: 'Plume', default: '#FFFFFF' },
            horse: { name: 'Horse', default: '#8B4513' },
            barding: { name: 'Barding', default: '#4A4A4A' },
            weapon: { name: 'Lance', default: '#808080' }
        },

        symbol: '🐴',
        symbolAlt: 'K'
    },

    mage: {
        id: 'mage',
        name: 'Battle Mage',
        faction: 'empire',
        type: 'spellcaster',
        description: 'Powerful magic user with devastating spells.',
        lore: 'Trained in the Colleges of Magic, these wizards channel arcane energies.',

        stats: {
            health: 5,
            attack: 7,
            defense: 1,
            movement: 3,
            attackRange: 3,
            initiative: 4
        },

        pointCost: 100,
        unlockCost: 300,

        abilities: [
            {
                id: 'fireball',
                name: 'Fireball',
                description: 'Deal 8 damage to target and 4 to adjacent enemies. 2 turn cooldown.',
                type: 'active',
                cooldown: 2,
                range: 3,
                damage: 8,
                splashDamage: 4
            },
            {
                id: 'arcane_shield',
                name: 'Arcane Shield',
                description: 'Block the next attack. 4 turn cooldown.',
                type: 'active',
                cooldown: 4
            }
        ],

        paintParts: {
            robe: { name: 'Robe', default: '#4B0082' },
            cloak: { name: 'Cloak', default: '#2F4F4F' },
            skin: { name: 'Skin', default: '#DEB887' },
            staff: { name: 'Staff', default: '#654321' },
            magic: { name: 'Magic Glow', default: '#00BFFF' }
        },

        symbol: '🔮',
        symbolAlt: 'M'
    },

    captain: {
        id: 'captain',
        name: 'Legion Captain',
        faction: 'empire',
        type: 'hero',
        description: 'Inspiring leader who boosts nearby allies.',
        lore: 'Veterans of countless battles, Captains lead from the front.',

        stats: {
            health: 12,
            attack: 5,
            defense: 4,
            movement: 4,
            attackRange: 1,
            initiative: 8
        },

        pointCost: 150,
        unlockCost: 500,
        isHero: true,

        abilities: [
            {
                id: 'inspire',
                name: 'Inspire',
                description: 'All allies within 3 tiles gain +1 Attack and +1 Defense.',
                type: 'aura',
                range: 3,
                effect: { attack: 1, defense: 1 }
            },
            {
                id: 'rally',
                name: 'Rally!',
                description: 'Remove negative effects from all allies within 2 tiles. 3 turn cooldown.',
                type: 'active',
                cooldown: 3,
                range: 2
            }
        ],

        paintParts: {
            armor: { name: 'Ornate Armor', default: '#DAA520' },
            cape: { name: 'Cape', default: '#8B0000' },
            skin: { name: 'Skin', default: '#DEB887' },
            helmet: { name: 'Helmet', default: '#C0C0C0' },
            weapon: { name: 'Sword', default: '#E8E8E8' },
            banner: { name: 'Banner', default: '#FFD700' }
        },

        symbol: '👑',
        symbolAlt: 'C'
    },

    // ===================
    // HORDE FACTION
    // ===================
    orc_warrior: {
        id: 'orc_warrior',
        name: 'Orc Brute',
        faction: 'horde',
        type: 'infantry',
        description: 'Savage melee fighter with high damage.',
        lore: 'Born for battle, Orc Brutes live only to fight and conquer.',

        stats: {
            health: 12,
            attack: 5,
            defense: 2,
            movement: 3,
            attackRange: 1,
            initiative: 4
        },

        pointCost: 55,
        unlockCost: 200,

        abilities: [
            {
                id: 'berserk',
                name: 'Berserk',
                description: '+2 Attack when below 50% health.',
                type: 'passive',
                effect: (unit) => {
                    return unit.currentHealth < unit.stats.health / 2
                        ? { attack: 2 }
                        : null;
                }
            }
        ],

        paintParts: {
            skin: { name: 'Skin', default: '#228B22' },
            armor: { name: 'Scrap Armor', default: '#8B4513' },
            cloth: { name: 'Loincloth', default: '#2F4F4F' },
            weapon: { name: 'Choppa', default: '#4A4A4A' },
            warpaint: { name: 'Warpaint', default: '#8B0000' }
        },

        symbol: '👹',
        symbolAlt: 'O'
    },

    goblin: {
        id: 'goblin',
        name: 'Goblin Sneaker',
        faction: 'horde',
        type: 'infantry',
        description: 'Cheap, fast unit that excels at flanking.',
        lore: 'What Goblins lack in strength, they make up in cunning and numbers.',

        stats: {
            health: 4,
            attack: 3,
            defense: 1,
            movement: 5,
            attackRange: 1,
            initiative: 9
        },

        pointCost: 25,
        unlockCost: 150,

        abilities: [
            {
                id: 'backstab',
                name: 'Backstab',
                description: '+3 damage when attacking from behind or side.',
                type: 'passive'
            },
            {
                id: 'hide',
                name: 'Hide',
                description: 'Become untargetable until next action. 3 turn cooldown.',
                type: 'active',
                cooldown: 3
            }
        ],

        paintParts: {
            skin: { name: 'Skin', default: '#9ACD32' },
            cloth: { name: 'Rags', default: '#8B4513' },
            weapon: { name: 'Dagger', default: '#808080' },
            eyes: { name: 'Eyes', default: '#FFD700' }
        },

        symbol: '🗡️',
        symbolAlt: 'G'
    },

    troll: {
        id: 'troll',
        name: 'Cave Troll',
        faction: 'horde',
        type: 'monster',
        description: 'Massive brute with regeneration ability.',
        lore: 'These dim-witted giants can shrug off wounds that would kill lesser creatures.',

        stats: {
            health: 20,
            attack: 7,
            defense: 3,
            movement: 2,
            attackRange: 1,
            initiative: 2
        },

        pointCost: 180,
        unlockCost: 600,

        abilities: [
            {
                id: 'regeneration',
                name: 'Regeneration',
                description: 'Heal 2 HP at the start of each turn.',
                type: 'passive'
            },
            {
                id: 'smash',
                name: 'Ground Smash',
                description: 'Stun all adjacent enemies for 1 turn. 4 turn cooldown.',
                type: 'active',
                cooldown: 4
            }
        ],

        paintParts: {
            skin: { name: 'Skin', default: '#708090' },
            belly: { name: 'Belly', default: '#A9A9A9' },
            eyes: { name: 'Eyes', default: '#FF4500' },
            claws: { name: 'Claws', default: '#2F4F4F' }
        },

        symbol: '👊',
        symbolAlt: 'T'
    },

    shaman: {
        id: 'shaman',
        name: 'Orc Shaman',
        faction: 'horde',
        type: 'spellcaster',
        description: 'Tribal magic user who can heal and buff allies.',
        lore: 'Shamans commune with the spirits to bring fortune to their warband.',

        stats: {
            health: 6,
            attack: 4,
            defense: 2,
            movement: 3,
            attackRange: 3,
            initiative: 5
        },

        pointCost: 90,
        unlockCost: 400,

        abilities: [
            {
                id: 'waaagh',
                name: "WAAAGH!",
                description: 'All allies gain +2 Attack for 2 turns. 4 turn cooldown.',
                type: 'active',
                cooldown: 4
            },
            {
                id: 'heal',
                name: 'Spirit Heal',
                description: 'Heal target ally for 5 HP. 2 turn cooldown.',
                type: 'active',
                cooldown: 2,
                range: 3,
                healAmount: 5
            }
        ],

        paintParts: {
            skin: { name: 'Skin', default: '#228B22' },
            robes: { name: 'Robes', default: '#8B4513' },
            staff: { name: 'Bone Staff', default: '#FFFFF0' },
            feathers: { name: 'Feathers', default: '#FF4500' },
            magic: { name: 'Spirit Glow', default: '#00FF00' }
        },

        symbol: '🌿',
        symbolAlt: 'S'
    },

    // ===================
    // UNDEAD FACTION
    // ===================
    skeleton: {
        id: 'skeleton',
        name: 'Skeleton Warrior',
        faction: 'undead',
        type: 'infantry',
        description: 'Fragile but numerous undead infantry.',
        lore: 'Risen from ancient battlefields, these warriors know no fear or pain.',

        stats: {
            health: 5,
            attack: 3,
            defense: 2,
            movement: 3,
            attackRange: 1,
            initiative: 3
        },

        pointCost: 30,
        unlockCost: 250,

        abilities: [
            {
                id: 'undying',
                name: 'Undying',
                description: '25% chance to resurrect with 1 HP when killed.',
                type: 'passive'
            }
        ],

        paintParts: {
            bones: { name: 'Bones', default: '#FFFFF0' },
            armor: { name: 'Rusted Armor', default: '#8B4513' },
            weapon: { name: 'Ancient Blade', default: '#4A4A4A' },
            glow: { name: 'Soul Fire', default: '#00BFFF' }
        },

        symbol: '💀',
        symbolAlt: 'U'
    },

    vampire: {
        id: 'vampire',
        name: 'Vampire Lord',
        faction: 'undead',
        type: 'hero',
        description: 'Powerful undead noble with life-stealing attacks.',
        lore: 'Ancient and cunning, Vampire Lords have unlived for millennia.',

        stats: {
            health: 10,
            attack: 6,
            defense: 3,
            movement: 4,
            attackRange: 1,
            initiative: 8
        },

        pointCost: 160,
        unlockCost: 800,
        isHero: true,

        abilities: [
            {
                id: 'life_drain',
                name: 'Life Drain',
                description: 'Heal for 50% of damage dealt.',
                type: 'passive'
            },
            {
                id: 'summon_bats',
                name: 'Summon Bats',
                description: 'Summon 2 Bat Swarms. 5 turn cooldown.',
                type: 'active',
                cooldown: 5
            }
        ],

        paintParts: {
            skin: { name: 'Pale Skin', default: '#F5F5DC' },
            armor: { name: 'Dark Armor', default: '#1C1C1C' },
            cape: { name: 'Cape', default: '#8B0000' },
            hair: { name: 'Hair', default: '#000000' },
            eyes: { name: 'Eyes', default: '#FF0000' }
        },

        symbol: '🧛',
        symbolAlt: 'V'
    },

    ghost: {
        id: 'ghost',
        name: 'Wraith',
        faction: 'undead',
        type: 'ethereal',
        description: 'Ghostly unit that can move through terrain and units.',
        lore: 'Spirits bound to the mortal realm by hatred and regret.',

        stats: {
            health: 6,
            attack: 4,
            defense: 0,
            movement: 4,
            attackRange: 1,
            initiative: 7
        },

        pointCost: 80,
        unlockCost: 350,

        abilities: [
            {
                id: 'ethereal',
                name: 'Ethereal',
                description: 'Can move through units and terrain. 50% damage from physical attacks.',
                type: 'passive'
            },
            {
                id: 'terrify',
                name: 'Terrifying Wail',
                description: 'Enemies within 2 tiles have -1 Attack. 3 turn cooldown.',
                type: 'active',
                cooldown: 3,
                range: 2
            }
        ],

        paintParts: {
            essence: { name: 'Ghostly Essence', default: '#ADD8E6' },
            shroud: { name: 'Shroud', default: '#2F4F4F' },
            eyes: { name: 'Eyes', default: '#00FFFF' }
        },

        symbol: '👻',
        symbolAlt: 'W'
    }
};

// Faction data
const Factions = {
    empire: {
        id: 'empire',
        name: 'The Golden Empire',
        description: 'Disciplined human armies with balanced units and strong formations.',
        color: '#DAA520',
        units: ['warrior', 'archer', 'knight', 'mage', 'captain']
    },
    horde: {
        id: 'horde',
        name: 'The Savage Horde',
        description: 'Brutal orc and goblin forces that overwhelm with raw power.',
        color: '#228B22',
        units: ['orc_warrior', 'goblin', 'troll', 'shaman']
    },
    undead: {
        id: 'undead',
        name: 'The Risen Dead',
        description: 'Undying legions that grow stronger as battle progresses.',
        color: '#4B0082',
        units: ['skeleton', 'vampire', 'ghost']
    }
};

// Unit class for game instances
class Unit {
    constructor(unitType, owner, position = { x: 0, y: 0 }) {
        const template = UnitTypes[unitType];
        if (!template) {
            throw new Error(`Unknown unit type: ${unitType}`);
        }

        this.id = Utils.generateId();
        this.unitType = unitType;
        this.name = template.name;
        this.owner = owner; // 'player1' or 'player2'
        this.faction = template.faction;
        this.type = template.type;

        // Copy stats
        this.stats = { ...template.stats };
        this.maxHealth = template.stats.health;
        this.currentHealth = this.maxHealth;

        // Position
        this.position = { ...position };

        // State
        this.hasMoved = false;
        this.hasActed = false;
        this.movedThisTurn = 0;
        this.isExhausted = false;

        // Ability cooldowns
        this.cooldowns = {};
        template.abilities?.forEach(ability => {
            if (ability.cooldown) {
                this.cooldowns[ability.id] = 0;
            }
        });

        // Status effects
        this.statusEffects = [];

        // Custom paint scheme
        this.paintScheme = Storage.getPaintSchemes()[unitType] || null;

        // Visual properties
        this.symbol = template.symbol;
        this.symbolAlt = template.symbolAlt;
    }

    // Get effective stats (base + modifiers)
    getEffectiveStats() {
        const effective = { ...this.stats };

        // Apply status effects
        this.statusEffects.forEach(effect => {
            if (effect.statModifiers) {
                Object.keys(effect.statModifiers).forEach(stat => {
                    effective[stat] = (effective[stat] || 0) + effect.statModifiers[stat];
                });
            }
        });

        return effective;
    }

    // Check if can move to position
    canMoveTo(targetPos, gameState) {
        if (this.hasMoved || this.isExhausted) return false;

        const distance = Utils.gridDistance(this.position, targetPos);
        const effectiveStats = this.getEffectiveStats();

        return distance <= effectiveStats.movement;
    }

    // Check if can attack target
    canAttack(target, gameState) {
        if (this.hasActed || this.isExhausted) return false;
        if (target.owner === this.owner) return false;

        const distance = Utils.gridDistance(this.position, target.position);
        const effectiveStats = this.getEffectiveStats();

        return distance <= effectiveStats.attackRange;
    }

    // Take damage
    takeDamage(amount) {
        const actualDamage = Math.max(0, amount);
        this.currentHealth = Math.max(0, this.currentHealth - actualDamage);
        return {
            damage: actualDamage,
            killed: this.currentHealth <= 0
        };
    }

    // Heal
    heal(amount) {
        const healedAmount = Math.min(amount, this.maxHealth - this.currentHealth);
        this.currentHealth += healedAmount;
        return healedAmount;
    }

    // Start turn
    startTurn() {
        this.hasMoved = false;
        this.hasActed = false;
        this.movedThisTurn = 0;
        this.isExhausted = false;

        // Reduce cooldowns
        Object.keys(this.cooldowns).forEach(abilityId => {
            if (this.cooldowns[abilityId] > 0) {
                this.cooldowns[abilityId]--;
            }
        });

        // Process status effects
        this.statusEffects = this.statusEffects.filter(effect => {
            if (effect.onTurnStart) {
                effect.onTurnStart(this);
            }
            if (effect.duration !== undefined) {
                effect.duration--;
                return effect.duration > 0;
            }
            return true;
        });

        // Regeneration check
        const template = UnitTypes[this.unitType];
        const regenAbility = template.abilities?.find(a => a.id === 'regeneration');
        if (regenAbility) {
            this.heal(2);
        }
    }

    // End turn
    endTurn() {
        this.isExhausted = true;
    }

    // Get abilities
    getAbilities() {
        return UnitTypes[this.unitType].abilities || [];
    }

    // Check if ability is ready
    isAbilityReady(abilityId) {
        return (this.cooldowns[abilityId] || 0) === 0;
    }

    // Use ability
    useAbility(abilityId) {
        const ability = this.getAbilities().find(a => a.id === abilityId);
        if (ability && ability.cooldown) {
            this.cooldowns[abilityId] = ability.cooldown;
        }
        this.hasActed = true;
    }

    // Serialize for network/save
    serialize() {
        return {
            id: this.id,
            unitType: this.unitType,
            owner: this.owner,
            position: this.position,
            currentHealth: this.currentHealth,
            hasMoved: this.hasMoved,
            hasActed: this.hasActed,
            cooldowns: this.cooldowns,
            statusEffects: this.statusEffects
        };
    }

    // Deserialize
    static deserialize(data) {
        const unit = new Unit(data.unitType, data.owner, data.position);
        unit.id = data.id;
        unit.currentHealth = data.currentHealth;
        unit.hasMoved = data.hasMoved;
        unit.hasActed = data.hasActed;
        unit.cooldowns = data.cooldowns;
        unit.statusEffects = data.statusEffects;
        return unit;
    }
}

// Make available globally
window.UnitTypes = UnitTypes;
window.Factions = Factions;
window.Unit = Unit;
