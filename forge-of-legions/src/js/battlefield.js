/**
 * Forge of Legions - Battlefield System
 * Handles the game board, turns, and unit management
 */

class Battlefield {
    constructor(config = {}) {
        this.gridWidth = config.width || 10;
        this.gridHeight = config.height || 8;
        this.cellSize = config.cellSize || 60;

        this.units = [];
        this.terrain = [];
        this.objectives = [];

        this.currentTurn = 1;
        this.currentPlayer = 'player1';
        this.phase = 'movement'; // movement, action, end

        this.selectedUnit = null;
        this.highlightedCells = [];
        this.actionMode = null; // null, 'move', 'attack', 'ability'

        this.player1Name = 'You';
        this.player2Name = 'Enemy';

        this.isMultiplayer = false;
        this.localPlayer = 'player1';

        // Animation state
        this.animating = false;

        // Callbacks
        this.onTurnChange = null;
        this.onCombatResult = null;
        this.onVictory = null;
        this.onUnitSelect = null;

        // Stats tracking
        this.battleStats = {
            player1: { unitsLost: 0, unitsKilled: 0, damageDealt: 0 },
            player2: { unitsLost: 0, unitsKilled: 0, damageDealt: 0 }
        };
    }

    // Initialize battlefield
    init(gridElement, canvasElement) {
        this.gridElement = gridElement;
        this.canvas = canvasElement;
        this.ctx = canvasElement.getContext('2d');

        // Set canvas size
        this.canvas.width = this.gridWidth * this.cellSize;
        this.canvas.height = this.gridHeight * this.cellSize;

        // Create grid cells
        this.createGrid();

        // Initial render
        this.render();
    }

    // Create grid cells
    createGrid() {
        this.gridElement.innerHTML = '';
        this.gridElement.style.gridTemplateColumns = `repeat(${this.gridWidth}, ${this.cellSize}px)`;
        this.gridElement.style.gridTemplateRows = `repeat(${this.gridHeight}, ${this.cellSize}px)`;

        for (let y = 0; y < this.gridHeight; y++) {
            for (let x = 0; x < this.gridWidth; x++) {
                const cell = document.createElement('div');
                cell.className = 'grid-cell';
                cell.dataset.x = x;
                cell.dataset.y = y;

                // Checkerboard pattern
                if ((x + y) % 2 === 0) {
                    cell.classList.add('cell-light');
                } else {
                    cell.classList.add('cell-dark');
                }

                cell.addEventListener('click', () => this.handleCellClick(x, y));
                cell.addEventListener('mouseenter', () => this.handleCellHover(x, y));

                this.gridElement.appendChild(cell);
            }
        }
    }

    // Add terrain
    addTerrain(x, y, type) {
        this.terrain.push({ x, y, type });
        this.updateCell(x, y);
    }

    // Add unit to battlefield
    addUnit(unit) {
        this.units.push(unit);
        this.updateCell(unit.position.x, unit.position.y);
    }

    // Remove unit from battlefield
    removeUnit(unit) {
        const index = this.units.findIndex(u => u.id === unit.id);
        if (index >= 0) {
            this.units.splice(index, 1);
            this.updateCell(unit.position.x, unit.position.y);
        }
    }

    // Get unit at position
    getUnitAt(pos) {
        return this.units.find(u =>
            u.position.x === pos.x &&
            u.position.y === pos.y &&
            u.currentHealth > 0
        );
    }

    // Get units in radius
    getUnitsInRadius(center, radius) {
        return this.units.filter(u => {
            if (u.currentHealth <= 0) return false;
            const distance = Utils.gridDistance(u.position, center);
            return distance <= radius && distance > 0;
        });
    }

    // Get adjacent units
    getAdjacentUnits(unit) {
        return this.units.filter(u => {
            if (u.id === unit.id || u.currentHealth <= 0) return false;
            return Utils.gridDistance(u.position, unit.position) === 1;
        });
    }

    // Get units for player
    getUnitsForPlayer(player) {
        return this.units.filter(u => u.owner === player && u.currentHealth > 0);
    }

    // Get terrain at position
    getTerrainAt(x, y) {
        return this.terrain.find(t => t.x === x && t.y === y);
    }

    // Check if cell is walkable
    isCellWalkable(x, y) {
        if (!Utils.isInBounds(x, y, this.gridWidth, this.gridHeight)) return false;

        const terrain = this.getTerrainAt(x, y);
        if (terrain && terrain.type === 'impassable') return false;

        const unit = this.getUnitAt({ x, y });
        if (unit) return false;

        return true;
    }

    // Handle cell click
    handleCellClick(x, y) {
        if (this.animating) return;

        // In multiplayer, only allow control of local player's units
        if (this.isMultiplayer && this.currentPlayer !== this.localPlayer) return;

        const clickedUnit = this.getUnitAt({ x, y });

        if (this.actionMode === 'move' && this.selectedUnit) {
            // Attempt to move
            const isValidMove = this.highlightedCells.some(c => c.x === x && c.y === y);
            if (isValidMove) {
                this.moveUnit(this.selectedUnit, { x, y });
            }
            this.clearHighlights();
            this.actionMode = null;
        }
        else if (this.actionMode === 'attack' && this.selectedUnit) {
            // Attempt to attack
            if (clickedUnit && clickedUnit.owner !== this.selectedUnit.owner) {
                this.executeAttack(this.selectedUnit, clickedUnit);
            }
            this.clearHighlights();
            this.actionMode = null;
        }
        else if (this.actionMode === 'ability' && this.selectedUnit) {
            // Attempt to use ability
            const isValidTarget = this.highlightedCells.some(c => c.x === x && c.y === y);
            if (isValidTarget) {
                this.executeAbility(this.selectedUnit, this.currentAbility, { x, y });
            }
            this.clearHighlights();
            this.actionMode = null;
            this.currentAbility = null;
        }
        else if (clickedUnit && clickedUnit.owner === this.currentPlayer) {
            // Select unit
            this.selectUnit(clickedUnit);
        }
        else {
            // Deselect
            this.deselectUnit();
        }
    }

    // Handle cell hover
    handleCellHover(x, y) {
        // Update hover preview
        if (this.actionMode === 'attack' && this.selectedUnit) {
            const targetUnit = this.getUnitAt({ x, y });
            if (targetUnit && targetUnit.owner !== this.selectedUnit.owner) {
                const preview = Combat.getCombatPreview(this.selectedUnit, targetUnit, this);
                this.showCombatPreview(preview, targetUnit);
            } else {
                this.hideCombatPreview();
            }
        }
    }

    // Select unit
    selectUnit(unit) {
        this.deselectUnit();
        this.selectedUnit = unit;

        // Update UI
        if (this.onUnitSelect) {
            this.onUnitSelect(unit);
        }

        // Update button states
        this.updateActionButtons();

        // Highlight selected cell
        this.updateCell(unit.position.x, unit.position.y);
    }

    // Deselect unit
    deselectUnit() {
        if (this.selectedUnit) {
            const prevPos = this.selectedUnit.position;
            this.selectedUnit = null;
            this.updateCell(prevPos.x, prevPos.y);
        }
        this.clearHighlights();
        this.actionMode = null;

        if (this.onUnitSelect) {
            this.onUnitSelect(null);
        }
    }

    // Show movement range
    showMovementRange(unit) {
        this.clearHighlights();
        this.actionMode = 'move';

        const range = unit.getEffectiveStats().movement;
        const validCells = this.getValidMovementCells(unit, range);

        validCells.forEach(cell => {
            this.highlightCell(cell.x, cell.y, 'move');
        });
    }

    // Get valid movement cells using pathfinding
    getValidMovementCells(unit, range) {
        const validCells = [];
        const visited = new Set();
        const queue = [{ x: unit.position.x, y: unit.position.y, distance: 0 }];

        visited.add(`${unit.position.x},${unit.position.y}`);

        while (queue.length > 0) {
            const current = queue.shift();

            if (current.distance > 0 && this.isCellWalkable(current.x, current.y)) {
                validCells.push({ x: current.x, y: current.y });
            }

            if (current.distance < range) {
                const neighbors = Utils.getAdjacentCells(
                    current.x, current.y,
                    this.gridWidth, this.gridHeight
                );

                for (const neighbor of neighbors) {
                    const key = `${neighbor.x},${neighbor.y}`;
                    if (!visited.has(key)) {
                        visited.add(key);

                        // Check if we can pass through
                        const terrain = this.getTerrainAt(neighbor.x, neighbor.y);
                        const occupant = this.getUnitAt(neighbor);

                        const canPass = !terrain || terrain.type !== 'impassable';
                        const noBlocker = !occupant || occupant.owner === unit.owner;

                        // Ethereal units can pass through everything
                        const isEthereal = unit.getAbilities().some(a => a.id === 'ethereal');

                        if (canPass && (noBlocker || isEthereal)) {
                            queue.push({
                                x: neighbor.x,
                                y: neighbor.y,
                                distance: current.distance + 1
                            });
                        }
                    }
                }
            }
        }

        return validCells;
    }

    // Show attack range
    showAttackRange(unit) {
        this.clearHighlights();
        this.actionMode = 'attack';

        const targets = Combat.getValidTargets(unit, this);
        targets.forEach(target => {
            this.highlightCell(target.position.x, target.position.y, 'attack');
        });
    }

    // Show ability range
    showAbilityRange(unit, ability) {
        this.clearHighlights();
        this.actionMode = 'ability';
        this.currentAbility = ability;

        const targets = Combat.getValidAbilityTargets(unit, ability, this);
        targets.forEach(pos => {
            const type = ability.healAmount ? 'heal' : 'attack';
            this.highlightCell(pos.x, pos.y, type);
        });
    }

    // Highlight cell
    highlightCell(x, y, type = 'move') {
        this.highlightedCells.push({ x, y, type });
        const cell = this.getCellElement(x, y);
        if (cell) {
            cell.classList.add(`highlight-${type}`);
        }
    }

    // Clear highlights
    clearHighlights() {
        this.highlightedCells.forEach(({ x, y, type }) => {
            const cell = this.getCellElement(x, y);
            if (cell) {
                cell.classList.remove(`highlight-${type}`);
            }
        });
        this.highlightedCells = [];
        this.hideCombatPreview();
    }

    // Get cell element
    getCellElement(x, y) {
        return this.gridElement.querySelector(`[data-x="${x}"][data-y="${y}"]`);
    }

    // Update cell display
    updateCell(x, y) {
        const cell = this.getCellElement(x, y);
        if (!cell) return;

        // Clear existing content
        const existingUnit = cell.querySelector('.unit-token');
        if (existingUnit) existingUnit.remove();

        // Add terrain indicator
        const terrain = this.getTerrainAt(x, y);
        cell.classList.remove('terrain-forest', 'terrain-water', 'terrain-mountain');
        if (terrain) {
            cell.classList.add(`terrain-${terrain.type}`);
        }

        // Add unit token
        const unit = this.getUnitAt({ x, y });
        if (unit && unit.currentHealth > 0) {
            const token = document.createElement('div');
            token.className = `unit-token ${unit.owner}`;

            if (unit === this.selectedUnit) {
                token.classList.add('selected');
            }

            if (unit.isExhausted) {
                token.classList.add('exhausted');
            }

            // Unit symbol
            token.innerHTML = `
                <span class="unit-symbol">${unit.symbol}</span>
                <div class="unit-health-bar">
                    <div class="health-fill" style="width: ${(unit.currentHealth / unit.maxHealth) * 100}%"></div>
                </div>
            `;

            cell.appendChild(token);
        }
    }

    // Move unit
    async moveUnit(unit, newPos) {
        this.animating = true;

        const oldPos = { ...unit.position };
        const distance = Utils.gridDistance(oldPos, newPos);

        // Animate movement
        await this.animateMovement(unit, oldPos, newPos);

        // Update unit state
        unit.position = newPos;
        unit.hasMoved = true;
        unit.movedThisTurn = distance;

        // Update cells
        this.updateCell(oldPos.x, oldPos.y);
        this.updateCell(newPos.x, newPos.y);

        // Trample damage (knight ability)
        const trampeAbility = unit.getAbilities().find(a => a.id === 'trample');
        if (trampeAbility) {
            // Check if passed through adjacent enemy cells
            // Simplified: just check current adjacent enemies
            const adjacent = this.getAdjacentUnits(unit);
            for (const adj of adjacent) {
                if (adj.owner !== unit.owner) {
                    adj.takeDamage(2);
                    this.showDamageNumber(adj.position, 2);
                }
            }
        }

        this.updateActionButtons();
        this.animating = false;

        // Audio feedback
        if (window.AudioManager) {
            AudioManager.play('move');
        }

        // Multiplayer sync
        if (this.isMultiplayer && this.onAction) {
            this.onAction({
                type: 'move',
                unitId: unit.id,
                from: oldPos,
                to: newPos
            });
        }
    }

    // Animate movement
    async animateMovement(unit, from, to) {
        const duration = 300;
        const cell = this.getCellElement(from.x, from.y);
        const token = cell?.querySelector('.unit-token');

        if (!token) return;

        const dx = (to.x - from.x) * this.cellSize;
        const dy = (to.y - from.y) * this.cellSize;

        await Utils.animate(duration, progress => {
            token.style.transform = `translate(${dx * progress}px, ${dy * progress}px)`;
        });

        token.style.transform = '';
    }

    // Execute attack
    async executeAttack(attacker, defender) {
        this.animating = true;

        // Combat result
        const result = await Combat.executeAttack(attacker, defender, this);

        // Show damage
        this.showDamageNumber(defender.position, result.damage, result.isCritical);

        // Animate attack
        await this.animateAttack(attacker, defender);

        // Handle death
        if (result.defenderKilled && !result.resurrected) {
            await this.animateDeath(defender);
            this.removeUnit(defender);

            // Track stats
            this.battleStats[attacker.owner].unitsKilled++;
            this.battleStats[defender.owner].unitsLost++;
        }

        // Track damage
        this.battleStats[attacker.owner].damageDealt += result.damage;

        // Life drain animation
        if (result.attackerHealed > 0) {
            this.showHealNumber(attacker.position, result.attackerHealed);
        }

        // Update displays
        this.updateCell(attacker.position.x, attacker.position.y);
        this.updateCell(defender.position.x, defender.position.y);
        this.updateActionButtons();

        // Audio
        if (window.AudioManager) {
            AudioManager.play('attack');
            if (result.defenderKilled) {
                AudioManager.play('death');
            }
        }

        // Check victory
        const victoryResult = Combat.checkVictory(this);
        if (victoryResult) {
            await Utils.wait(500);
            if (this.onVictory) {
                this.onVictory(victoryResult);
            }
        }

        this.animating = false;

        // Multiplayer sync
        if (this.isMultiplayer && this.onAction) {
            this.onAction({
                type: 'attack',
                attackerId: attacker.id,
                defenderId: defender.id,
                result
            });
        }
    }

    // Animate attack
    async animateAttack(attacker, defender) {
        const attackerCell = this.getCellElement(attacker.position.x, attacker.position.y);
        const token = attackerCell?.querySelector('.unit-token');

        if (token) {
            const dx = (defender.position.x - attacker.position.x) * 10;
            const dy = (defender.position.y - attacker.position.y) * 10;

            token.style.transition = 'transform 0.1s ease-out';
            token.style.transform = `translate(${dx}px, ${dy}px)`;

            await Utils.wait(100);

            token.style.transform = '';
            await Utils.wait(100);
            token.style.transition = '';
        }
    }

    // Animate death
    async animateDeath(unit) {
        const cell = this.getCellElement(unit.position.x, unit.position.y);
        const token = cell?.querySelector('.unit-token');

        if (token) {
            token.classList.add('dying');
            await Utils.wait(500);
        }
    }

    // Execute ability
    async executeAbility(unit, ability, target) {
        this.animating = true;

        const result = await Combat.executeAbility(unit, ability, target, this);

        // Show effects
        for (const targetResult of result.targets) {
            const targetUnit = this.units.find(u => u.id === targetResult.unitId);
            if (targetUnit) {
                if (targetResult.damage) {
                    this.showDamageNumber(targetUnit.position, targetResult.damage);
                    if (targetResult.killed) {
                        await this.animateDeath(targetUnit);
                        this.removeUnit(targetUnit);
                    }
                }
                if (targetResult.healed) {
                    this.showHealNumber(targetUnit.position, targetResult.healed);
                }
                this.updateCell(targetUnit.position.x, targetUnit.position.y);
            }
        }

        // Update UI
        this.updateCell(unit.position.x, unit.position.y);
        this.updateActionButtons();

        // Audio
        if (window.AudioManager) {
            AudioManager.play('ability');
        }

        // Check victory
        const victoryResult = Combat.checkVictory(this);
        if (victoryResult && this.onVictory) {
            this.onVictory(victoryResult);
        }

        this.animating = false;

        // Multiplayer sync
        if (this.isMultiplayer && this.onAction) {
            this.onAction({
                type: 'ability',
                unitId: unit.id,
                abilityId: ability.id,
                target,
                result
            });
        }
    }

    // Show damage number
    showDamageNumber(pos, damage, isCritical = false) {
        const cell = this.getCellElement(pos.x, pos.y);
        if (!cell) return;

        const dmgElement = document.createElement('div');
        dmgElement.className = `damage-number ${isCritical ? 'critical' : ''}`;
        dmgElement.textContent = `-${damage}`;

        cell.appendChild(dmgElement);

        setTimeout(() => dmgElement.remove(), 1000);
    }

    // Show heal number
    showHealNumber(pos, amount) {
        const cell = this.getCellElement(pos.x, pos.y);
        if (!cell) return;

        const healElement = document.createElement('div');
        healElement.className = 'heal-number';
        healElement.textContent = `+${amount}`;

        cell.appendChild(healElement);

        setTimeout(() => healElement.remove(), 1000);
    }

    // Show combat preview
    showCombatPreview(preview, targetUnit) {
        // Update combat preview UI
        const previewEl = document.getElementById('combat-preview');
        if (previewEl) {
            previewEl.innerHTML = `
                <div class="preview-damage">${preview.damage} damage</div>
                ${preview.isCriticalPossible ? '<div class="preview-crit">10% crit chance</div>' : ''}
                ${preview.defenderWillDie ? '<div class="preview-kill">LETHAL</div>' : ''}
                ${preview.canCounter ? `<div class="preview-counter">Counter: ${preview.counterDamage}</div>` : ''}
            `;
            previewEl.style.display = 'block';
        }
    }

    // Hide combat preview
    hideCombatPreview() {
        const previewEl = document.getElementById('combat-preview');
        if (previewEl) {
            previewEl.style.display = 'none';
        }
    }

    // Update action buttons
    updateActionButtons() {
        const moveBtn = document.getElementById('btn-move');
        const attackBtn = document.getElementById('btn-attack');
        const abilityBtn = document.getElementById('btn-ability');

        if (this.selectedUnit) {
            const unit = this.selectedUnit;
            const canMove = !unit.hasMoved && !unit.isExhausted;
            const targets = Combat.getValidTargets(unit, this);
            const canAttack = !unit.hasActed && !unit.isExhausted && targets.length > 0;

            // Check abilities
            const abilities = unit.getAbilities().filter(a =>
                a.type === 'active' && unit.isAbilityReady(a.id)
            );
            const hasAbility = abilities.length > 0 && !unit.hasActed;

            if (moveBtn) moveBtn.disabled = !canMove;
            if (attackBtn) attackBtn.disabled = !canAttack;
            if (abilityBtn) {
                abilityBtn.disabled = !hasAbility;
                if (hasAbility) {
                    abilityBtn.dataset.abilityName = abilities[0].name;
                }
            }
        } else {
            if (moveBtn) moveBtn.disabled = true;
            if (attackBtn) attackBtn.disabled = true;
            if (abilityBtn) abilityBtn.disabled = true;
        }
    }

    // End current player's turn
    endTurn() {
        // Exhaust all units
        this.getUnitsForPlayer(this.currentPlayer).forEach(unit => {
            unit.endTurn();
            this.updateCell(unit.position.x, unit.position.y);
        });

        // Switch player
        this.currentPlayer = this.currentPlayer === 'player1' ? 'player2' : 'player1';

        // Increment turn counter when back to player 1
        if (this.currentPlayer === 'player1') {
            this.currentTurn++;
        }

        // Start new turn for current player's units
        this.getUnitsForPlayer(this.currentPlayer).forEach(unit => {
            unit.startTurn();
            this.updateCell(unit.position.x, unit.position.y);
        });

        // Deselect
        this.deselectUnit();

        // Callback
        if (this.onTurnChange) {
            this.onTurnChange({
                turn: this.currentTurn,
                player: this.currentPlayer
            });
        }

        // Check objectives
        const victoryResult = Combat.checkVictory(this);
        if (victoryResult && this.onVictory) {
            this.onVictory(victoryResult);
        }

        // Audio
        if (window.AudioManager) {
            AudioManager.play('turnStart');
        }

        // Multiplayer sync
        if (this.isMultiplayer && this.onAction) {
            this.onAction({ type: 'endTurn' });
        }
    }

    // Full render
    render() {
        // Clear canvas
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);

        // Draw grid background
        this.drawGrid();

        // Update all cells
        for (let y = 0; y < this.gridHeight; y++) {
            for (let x = 0; x < this.gridWidth; x++) {
                this.updateCell(x, y);
            }
        }
    }

    // Draw grid on canvas
    drawGrid() {
        this.ctx.strokeStyle = 'rgba(255, 255, 255, 0.1)';
        this.ctx.lineWidth = 1;

        for (let x = 0; x <= this.gridWidth; x++) {
            this.ctx.beginPath();
            this.ctx.moveTo(x * this.cellSize, 0);
            this.ctx.lineTo(x * this.cellSize, this.gridHeight * this.cellSize);
            this.ctx.stroke();
        }

        for (let y = 0; y <= this.gridHeight; y++) {
            this.ctx.beginPath();
            this.ctx.moveTo(0, y * this.cellSize);
            this.ctx.lineTo(this.gridWidth * this.cellSize, y * this.cellSize);
            this.ctx.stroke();
        }
    }

    // Setup from army data
    setupFromArmies(player1Army, player2Army) {
        this.units = [];

        // Spawn player 1 units (bottom)
        let x = 1;
        player1Army.forEach(unitConfig => {
            for (let i = 0; i < (unitConfig.count || 1); i++) {
                const unit = new Unit(unitConfig.unitId, 'player1', {
                    x: x % (this.gridWidth - 2) + 1,
                    y: this.gridHeight - 1 - Math.floor(x / (this.gridWidth - 2))
                });
                this.addUnit(unit);
                x++;
            }
        });

        // Spawn player 2 units (top)
        x = 1;
        player2Army.forEach(unitConfig => {
            for (let i = 0; i < (unitConfig.count || 1); i++) {
                const unit = new Unit(unitConfig.unitId, 'player2', {
                    x: x % (this.gridWidth - 2) + 1,
                    y: Math.floor(x / (this.gridWidth - 2))
                });
                this.addUnit(unit);
                x++;
            }
        });

        this.render();
    }

    // Serialize game state
    serialize() {
        return {
            gridWidth: this.gridWidth,
            gridHeight: this.gridHeight,
            currentTurn: this.currentTurn,
            currentPlayer: this.currentPlayer,
            units: this.units.map(u => u.serialize()),
            terrain: this.terrain,
            objectives: this.objectives,
            battleStats: this.battleStats
        };
    }

    // Deserialize game state
    static deserialize(data) {
        const battlefield = new Battlefield({
            width: data.gridWidth,
            height: data.gridHeight
        });

        battlefield.currentTurn = data.currentTurn;
        battlefield.currentPlayer = data.currentPlayer;
        battlefield.terrain = data.terrain;
        battlefield.objectives = data.objectives;
        battlefield.battleStats = data.battleStats;

        data.units.forEach(unitData => {
            const unit = Unit.deserialize(unitData);
            battlefield.units.push(unit);
        });

        return battlefield;
    }
}

// Make available globally
window.Battlefield = Battlefield;
