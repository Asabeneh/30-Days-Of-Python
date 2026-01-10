/**
 * Forge of Legions - Paint Studio
 * Handles unit customization and color schemes
 */

const PaintStudio = {
    canvas: null,
    ctx: null,
    selectedUnit: null,
    selectedPart: null,
    currentScheme: {},

    // Initialize paint studio
    init: () => {
        PaintStudio.canvas = document.getElementById('paint-canvas');
        if (PaintStudio.canvas) {
            PaintStudio.ctx = PaintStudio.canvas.getContext('2d');
        }

        PaintStudio.renderUnitList();
        PaintStudio.renderColorPalette();
        PaintStudio.setupEventListeners();
    },

    // Render unit list
    renderUnitList: () => {
        const container = document.getElementById('paint-unit-list');
        if (!container) return;

        const unlocks = Storage.getUnlocks();
        container.innerHTML = '';

        unlocks.units.forEach(unitId => {
            const unit = UnitTypes[unitId];
            if (!unit) return;

            const btn = document.createElement('button');
            btn.className = 'paint-unit-btn';
            btn.dataset.unitId = unitId;
            btn.innerHTML = `
                <span class="unit-symbol">${unit.symbol}</span>
                <span class="unit-name">${unit.name}</span>
            `;

            btn.addEventListener('click', () => PaintStudio.selectUnit(unitId));
            container.appendChild(btn);
        });
    },

    // Render color palette
    renderColorPalette: () => {
        const container = document.getElementById('color-swatches');
        if (!container) return;

        const unlocks = Storage.getUnlocks();
        container.innerHTML = '';

        unlocks.paintColors.forEach(color => {
            const swatch = document.createElement('div');
            swatch.className = 'color-swatch';
            swatch.style.backgroundColor = color;
            swatch.dataset.color = color;

            swatch.addEventListener('click', () => PaintStudio.selectColor(color));
            container.appendChild(swatch);
        });
    },

    // Setup event listeners
    setupEventListeners: () => {
        const customColor = document.getElementById('custom-color');
        if (customColor) {
            customColor.addEventListener('change', (e) => {
                PaintStudio.selectColor(e.target.value);
            });
        }

        const saveBtn = document.getElementById('btn-save-scheme');
        if (saveBtn) {
            saveBtn.addEventListener('click', () => PaintStudio.saveScheme());
        }
    },

    // Select unit to paint
    selectUnit: (unitId) => {
        PaintStudio.selectedUnit = unitId;
        const unit = UnitTypes[unitId];

        // Load existing scheme or use defaults
        const savedScheme = Storage.getPaintSchemes()[unitId];
        PaintStudio.currentScheme = savedScheme || {};

        // Ensure all parts have colors
        Object.keys(unit.paintParts).forEach(partId => {
            if (!PaintStudio.currentScheme[partId]) {
                PaintStudio.currentScheme[partId] = unit.paintParts[partId].default;
            }
        });

        // Update unit buttons
        document.querySelectorAll('.paint-unit-btn').forEach(btn => {
            btn.classList.toggle('selected', btn.dataset.unitId === unitId);
        });

        // Render part selector
        PaintStudio.renderPartSelector();

        // Draw unit preview
        PaintStudio.drawUnitPreview();
    },

    // Render part selector
    renderPartSelector: () => {
        const container = document.getElementById('part-selector');
        if (!container || !PaintStudio.selectedUnit) return;

        const unit = UnitTypes[PaintStudio.selectedUnit];
        container.innerHTML = '';

        Object.entries(unit.paintParts).forEach(([partId, part]) => {
            const btn = document.createElement('button');
            btn.className = 'paint-part-btn';
            btn.dataset.partId = partId;

            const currentColor = PaintStudio.currentScheme[partId] || part.default;

            btn.innerHTML = `
                <span class="part-color" style="background-color: ${currentColor}"></span>
                <span class="part-name">${part.name}</span>
            `;

            btn.addEventListener('click', () => PaintStudio.selectPart(partId));
            container.appendChild(btn);
        });
    },

    // Select part to paint
    selectPart: (partId) => {
        PaintStudio.selectedPart = partId;

        document.querySelectorAll('.paint-part-btn').forEach(btn => {
            btn.classList.toggle('selected', btn.dataset.partId === partId);
        });
    },

    // Select color
    selectColor: (color) => {
        if (!PaintStudio.selectedPart || !PaintStudio.selectedUnit) return;

        PaintStudio.currentScheme[PaintStudio.selectedPart] = color;

        // Update part button
        const partBtn = document.querySelector(`[data-part-id="${PaintStudio.selectedPart}"]`);
        if (partBtn) {
            partBtn.querySelector('.part-color').style.backgroundColor = color;
        }

        // Update color swatches
        document.querySelectorAll('.color-swatch').forEach(swatch => {
            swatch.classList.toggle('selected', swatch.dataset.color === color);
        });

        // Redraw preview
        PaintStudio.drawUnitPreview();

        // Audio feedback
        if (window.AudioManager) {
            AudioManager.play('select');
        }
    },

    // Draw unit preview
    drawUnitPreview: () => {
        if (!PaintStudio.ctx || !PaintStudio.selectedUnit) return;

        const ctx = PaintStudio.ctx;
        const canvas = PaintStudio.canvas;
        const unit = UnitTypes[PaintStudio.selectedUnit];
        const scheme = PaintStudio.currentScheme;

        // Clear canvas
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // Draw based on unit type
        const cx = canvas.width / 2;
        const cy = canvas.height / 2;
        const scale = 3;

        ctx.save();
        ctx.translate(cx, cy);
        ctx.scale(scale, scale);

        switch (unit.type) {
            case 'infantry':
                PaintStudio.drawInfantry(ctx, scheme, unit);
                break;
            case 'ranged':
                PaintStudio.drawRanged(ctx, scheme, unit);
                break;
            case 'cavalry':
                PaintStudio.drawCavalry(ctx, scheme, unit);
                break;
            case 'spellcaster':
                PaintStudio.drawSpellcaster(ctx, scheme, unit);
                break;
            case 'hero':
                PaintStudio.drawHero(ctx, scheme, unit);
                break;
            case 'monster':
                PaintStudio.drawMonster(ctx, scheme, unit);
                break;
            case 'ethereal':
                PaintStudio.drawEthereal(ctx, scheme, unit);
                break;
            default:
                PaintStudio.drawDefaultUnit(ctx, scheme, unit);
        }

        ctx.restore();

        // Draw unit name
        ctx.fillStyle = '#fff';
        ctx.font = 'bold 16px Arial';
        ctx.textAlign = 'center';
        ctx.fillText(unit.name, cx, 30);
    },

    // Draw infantry unit
    drawInfantry: (ctx, scheme, unit) => {
        // Body/Armor
        ctx.fillStyle = scheme.armor || '#4A4A4A';
        ctx.beginPath();
        ctx.roundRect(-15, -20, 30, 40, 5);
        ctx.fill();

        // Cloth/Tabard
        ctx.fillStyle = scheme.cloth || '#8B0000';
        ctx.beginPath();
        ctx.roundRect(-10, 0, 20, 25, 3);
        ctx.fill();

        // Head
        ctx.fillStyle = scheme.skin || '#DEB887';
        ctx.beginPath();
        ctx.arc(0, -30, 12, 0, Math.PI * 2);
        ctx.fill();

        // Helmet
        ctx.fillStyle = scheme.armor || '#4A4A4A';
        ctx.beginPath();
        ctx.arc(0, -35, 10, Math.PI, 0);
        ctx.fill();

        // Shield
        if (scheme.shield) {
            ctx.fillStyle = scheme.shield;
            ctx.beginPath();
            ctx.ellipse(-25, 0, 12, 18, 0, 0, Math.PI * 2);
            ctx.fill();

            // Shield trim
            ctx.strokeStyle = scheme.trim || '#FFD700';
            ctx.lineWidth = 2;
            ctx.stroke();
        }

        // Weapon
        ctx.fillStyle = scheme.weapon || '#808080';
        ctx.fillRect(20, -25, 4, 50);
    },

    // Draw ranged unit
    drawRanged: (ctx, scheme, unit) => {
        // Leather armor
        ctx.fillStyle = scheme.armor || '#8B4513';
        ctx.beginPath();
        ctx.roundRect(-12, -15, 24, 35, 4);
        ctx.fill();

        // Tunic
        ctx.fillStyle = scheme.cloth || '#228B22';
        ctx.fillRect(-8, 5, 16, 15);

        // Head
        ctx.fillStyle = scheme.skin || '#DEB887';
        ctx.beginPath();
        ctx.arc(0, -25, 10, 0, Math.PI * 2);
        ctx.fill();

        // Hood
        ctx.fillStyle = scheme.cloth || '#228B22';
        ctx.beginPath();
        ctx.arc(0, -28, 8, Math.PI * 1.2, Math.PI * 1.8);
        ctx.lineTo(-5, -20);
        ctx.lineTo(5, -20);
        ctx.fill();

        // Bow
        ctx.strokeStyle = scheme.bow || '#654321';
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.arc(25, 0, 25, -Math.PI * 0.6, Math.PI * 0.6);
        ctx.stroke();

        // Bowstring
        ctx.strokeStyle = '#fff';
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(25, -20);
        ctx.lineTo(25, 20);
        ctx.stroke();

        // Quiver
        ctx.fillStyle = scheme.quiver || '#8B4513';
        ctx.fillRect(-20, -10, 8, 25);
    },

    // Draw cavalry unit
    drawCavalry: (ctx, scheme, unit) => {
        // Horse body
        ctx.fillStyle = scheme.horse || '#8B4513';
        ctx.beginPath();
        ctx.ellipse(0, 15, 30, 15, 0, 0, Math.PI * 2);
        ctx.fill();

        // Horse legs
        ctx.fillRect(-20, 25, 6, 20);
        ctx.fillRect(-5, 25, 6, 20);
        ctx.fillRect(5, 25, 6, 20);
        ctx.fillRect(15, 25, 6, 20);

        // Barding
        ctx.fillStyle = scheme.barding || '#4A4A4A';
        ctx.beginPath();
        ctx.moveTo(-25, 5);
        ctx.lineTo(25, 5);
        ctx.lineTo(20, 20);
        ctx.lineTo(-20, 20);
        ctx.fill();

        // Horse head
        ctx.fillStyle = scheme.horse || '#8B4513';
        ctx.beginPath();
        ctx.ellipse(30, 0, 10, 8, -0.3, 0, Math.PI * 2);
        ctx.fill();

        // Rider armor
        ctx.fillStyle = scheme.armor || '#C0C0C0';
        ctx.beginPath();
        ctx.roundRect(-10, -25, 20, 25, 3);
        ctx.fill();

        // Rider head
        ctx.beginPath();
        ctx.arc(0, -35, 8, 0, Math.PI * 2);
        ctx.fill();

        // Plume
        ctx.fillStyle = scheme.plume || '#FFFFFF';
        ctx.beginPath();
        ctx.ellipse(0, -48, 4, 10, 0, 0, Math.PI * 2);
        ctx.fill();

        // Tabard
        ctx.fillStyle = scheme.tabard || '#000080';
        ctx.fillRect(-6, -15, 12, 15);

        // Lance
        ctx.fillStyle = scheme.weapon || '#808080';
        ctx.fillRect(15, -50, 3, 60);
    },

    // Draw spellcaster
    drawSpellcaster: (ctx, scheme, unit) => {
        // Robe
        ctx.fillStyle = scheme.robe || '#4B0082';
        ctx.beginPath();
        ctx.moveTo(0, -15);
        ctx.lineTo(20, 40);
        ctx.lineTo(-20, 40);
        ctx.closePath();
        ctx.fill();

        // Cloak
        ctx.fillStyle = scheme.cloak || '#2F4F4F';
        ctx.beginPath();
        ctx.moveTo(-5, -10);
        ctx.lineTo(-25, 35);
        ctx.lineTo(-15, 35);
        ctx.lineTo(0, 0);
        ctx.fill();

        // Head
        ctx.fillStyle = scheme.skin || '#DEB887';
        ctx.beginPath();
        ctx.arc(0, -25, 10, 0, Math.PI * 2);
        ctx.fill();

        // Hood
        ctx.fillStyle = scheme.robe || '#4B0082';
        ctx.beginPath();
        ctx.arc(0, -28, 12, Math.PI, 0);
        ctx.lineTo(10, -20);
        ctx.lineTo(-10, -20);
        ctx.fill();

        // Staff
        ctx.fillStyle = scheme.staff || '#654321';
        ctx.fillRect(18, -45, 4, 80);

        // Staff orb
        ctx.fillStyle = scheme.magic || '#00BFFF';
        ctx.beginPath();
        ctx.arc(20, -50, 8, 0, Math.PI * 2);
        ctx.fill();

        // Magic glow
        ctx.fillStyle = `${scheme.magic || '#00BFFF'}44`;
        ctx.beginPath();
        ctx.arc(20, -50, 15, 0, Math.PI * 2);
        ctx.fill();
    },

    // Draw hero unit
    drawHero: (ctx, scheme, unit) => {
        // Ornate armor
        ctx.fillStyle = scheme.armor || '#DAA520';
        ctx.beginPath();
        ctx.roundRect(-18, -20, 36, 45, 5);
        ctx.fill();

        // Armor details
        ctx.strokeStyle = Utils.adjustColor(scheme.armor || '#DAA520', -40);
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(-10, -10);
        ctx.lineTo(-10, 15);
        ctx.moveTo(10, -10);
        ctx.lineTo(10, 15);
        ctx.stroke();

        // Cape
        ctx.fillStyle = scheme.cape || '#8B0000';
        ctx.beginPath();
        ctx.moveTo(-15, -15);
        ctx.lineTo(-25, 30);
        ctx.lineTo(-5, 25);
        ctx.closePath();
        ctx.fill();
        ctx.beginPath();
        ctx.moveTo(15, -15);
        ctx.lineTo(25, 30);
        ctx.lineTo(5, 25);
        ctx.closePath();
        ctx.fill();

        // Head
        ctx.fillStyle = scheme.skin || '#DEB887';
        ctx.beginPath();
        ctx.arc(0, -32, 12, 0, Math.PI * 2);
        ctx.fill();

        // Helmet
        ctx.fillStyle = scheme.helmet || '#C0C0C0';
        ctx.beginPath();
        ctx.arc(0, -38, 10, Math.PI, 0);
        ctx.fill();

        // Crown/crest
        ctx.fillStyle = scheme.banner || '#FFD700';
        ctx.beginPath();
        ctx.moveTo(-8, -48);
        ctx.lineTo(0, -55);
        ctx.lineTo(8, -48);
        ctx.closePath();
        ctx.fill();

        // Sword
        ctx.fillStyle = scheme.weapon || '#E8E8E8';
        ctx.fillRect(22, -30, 5, 55);
        ctx.fillRect(18, -25, 13, 6);
    },

    // Draw monster
    drawMonster: (ctx, scheme, unit) => {
        // Large body
        ctx.fillStyle = scheme.skin || '#708090';
        ctx.beginPath();
        ctx.ellipse(0, 10, 35, 30, 0, 0, Math.PI * 2);
        ctx.fill();

        // Belly
        ctx.fillStyle = scheme.belly || '#A9A9A9';
        ctx.beginPath();
        ctx.ellipse(0, 15, 20, 20, 0, 0, Math.PI * 2);
        ctx.fill();

        // Head
        ctx.fillStyle = scheme.skin || '#708090';
        ctx.beginPath();
        ctx.arc(0, -25, 20, 0, Math.PI * 2);
        ctx.fill();

        // Eyes
        ctx.fillStyle = scheme.eyes || '#FF4500';
        ctx.beginPath();
        ctx.arc(-8, -28, 5, 0, Math.PI * 2);
        ctx.arc(8, -28, 5, 0, Math.PI * 2);
        ctx.fill();

        // Claws
        ctx.fillStyle = scheme.claws || '#2F4F4F';
        for (let i = -1; i <= 1; i++) {
            ctx.beginPath();
            ctx.moveTo(-30 + i * 5, 30);
            ctx.lineTo(-35 + i * 5, 45);
            ctx.lineTo(-28 + i * 5, 35);
            ctx.fill();
            ctx.beginPath();
            ctx.moveTo(30 + i * 5, 30);
            ctx.lineTo(35 + i * 5, 45);
            ctx.lineTo(28 + i * 5, 35);
            ctx.fill();
        }
    },

    // Draw ethereal unit
    drawEthereal: (ctx, scheme, unit) => {
        // Ghostly body
        ctx.fillStyle = `${scheme.essence || '#ADD8E6'}88`;
        ctx.beginPath();
        ctx.moveTo(0, -40);
        ctx.bezierCurveTo(-30, -20, -25, 30, -20, 45);
        ctx.bezierCurveTo(-10, 50, 10, 50, 20, 45);
        ctx.bezierCurveTo(25, 30, 30, -20, 0, -40);
        ctx.fill();

        // Inner glow
        ctx.fillStyle = `${scheme.essence || '#ADD8E6'}44`;
        ctx.beginPath();
        ctx.ellipse(0, 0, 15, 25, 0, 0, Math.PI * 2);
        ctx.fill();

        // Shroud
        ctx.fillStyle = `${scheme.shroud || '#2F4F4F'}88`;
        ctx.beginPath();
        ctx.moveTo(-15, -30);
        ctx.lineTo(-25, 20);
        ctx.lineTo(25, 20);
        ctx.lineTo(15, -30);
        ctx.closePath();
        ctx.fill();

        // Eyes
        ctx.fillStyle = scheme.eyes || '#00FFFF';
        ctx.beginPath();
        ctx.arc(-8, -25, 4, 0, Math.PI * 2);
        ctx.arc(8, -25, 4, 0, Math.PI * 2);
        ctx.fill();

        // Eye glow
        ctx.fillStyle = `${scheme.eyes || '#00FFFF'}66`;
        ctx.beginPath();
        ctx.arc(-8, -25, 8, 0, Math.PI * 2);
        ctx.arc(8, -25, 8, 0, Math.PI * 2);
        ctx.fill();
    },

    // Default unit drawing
    drawDefaultUnit: (ctx, scheme, unit) => {
        // Simple circle with symbol
        const primaryColor = Object.values(scheme)[0] || '#666';

        ctx.fillStyle = primaryColor;
        ctx.beginPath();
        ctx.arc(0, 0, 30, 0, Math.PI * 2);
        ctx.fill();

        ctx.fillStyle = '#fff';
        ctx.font = 'bold 30px Arial';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText(unit.symbol, 0, 0);
    },

    // Save current scheme
    saveScheme: () => {
        if (!PaintStudio.selectedUnit) return;

        Storage.savePaintScheme(PaintStudio.selectedUnit, PaintStudio.currentScheme);

        if (window.UI) {
            UI.showToast('Paint scheme saved!', 'success');
        }

        if (window.AudioManager) {
            AudioManager.play('select');
        }
    },

    // Reset to defaults
    resetScheme: () => {
        if (!PaintStudio.selectedUnit) return;

        const unit = UnitTypes[PaintStudio.selectedUnit];
        PaintStudio.currentScheme = {};

        Object.keys(unit.paintParts).forEach(partId => {
            PaintStudio.currentScheme[partId] = unit.paintParts[partId].default;
        });

        PaintStudio.renderPartSelector();
        PaintStudio.drawUnitPreview();
    }
};

// Make available globally
window.PaintStudio = PaintStudio;
