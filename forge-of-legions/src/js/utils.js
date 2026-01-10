/**
 * Forge of Legions - Utility Functions
 */

const Utils = {
    // Generate unique ID
    generateId: () => {
        return Date.now().toString(36) + Math.random().toString(36).substr(2);
    },

    // Generate game code for multiplayer
    generateGameCode: () => {
        const chars = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789';
        let code = '';
        for (let i = 0; i < 4; i++) {
            code += chars.charAt(Math.floor(Math.random() * chars.length));
        }
        return code;
    },

    // Clamp value between min and max
    clamp: (value, min, max) => {
        return Math.min(Math.max(value, min), max);
    },

    // Calculate distance between two grid positions
    gridDistance: (pos1, pos2) => {
        return Math.abs(pos1.x - pos2.x) + Math.abs(pos1.y - pos2.y);
    },

    // Calculate euclidean distance
    euclideanDistance: (pos1, pos2) => {
        const dx = pos1.x - pos2.x;
        const dy = pos1.y - pos2.y;
        return Math.sqrt(dx * dx + dy * dy);
    },

    // Check if position is within grid bounds
    isInBounds: (x, y, width, height) => {
        return x >= 0 && x < width && y >= 0 && y < height;
    },

    // Get adjacent cells (4-directional)
    getAdjacentCells: (x, y, width, height) => {
        const adjacent = [];
        const directions = [
            { x: 0, y: -1 }, // up
            { x: 1, y: 0 },  // right
            { x: 0, y: 1 },  // down
            { x: -1, y: 0 }  // left
        ];

        for (const dir of directions) {
            const newX = x + dir.x;
            const newY = y + dir.y;
            if (Utils.isInBounds(newX, newY, width, height)) {
                adjacent.push({ x: newX, y: newY });
            }
        }
        return adjacent;
    },

    // Get cells in range (for movement/attack)
    getCellsInRange: (x, y, range, width, height, includeDiagonal = false) => {
        const cells = [];
        for (let dx = -range; dx <= range; dx++) {
            for (let dy = -range; dy <= range; dy++) {
                if (dx === 0 && dy === 0) continue;

                const distance = includeDiagonal
                    ? Math.max(Math.abs(dx), Math.abs(dy))
                    : Math.abs(dx) + Math.abs(dy);

                if (distance <= range) {
                    const newX = x + dx;
                    const newY = y + dy;
                    if (Utils.isInBounds(newX, newY, width, height)) {
                        cells.push({ x: newX, y: newY, distance });
                    }
                }
            }
        }
        return cells;
    },

    // Shuffle array
    shuffle: (array) => {
        const arr = [...array];
        for (let i = arr.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [arr[i], arr[j]] = [arr[j], arr[i]];
        }
        return arr;
    },

    // Roll dice (returns array of results)
    rollDice: (count, sides = 6) => {
        const results = [];
        for (let i = 0; i < count; i++) {
            results.push(Math.floor(Math.random() * sides) + 1);
        }
        return results;
    },

    // Format number with commas
    formatNumber: (num) => {
        return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
    },

    // Debounce function
    debounce: (func, wait) => {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    },

    // Deep clone object
    deepClone: (obj) => {
        return JSON.parse(JSON.stringify(obj));
    },

    // Lerp (linear interpolation)
    lerp: (start, end, t) => {
        return start + (end - start) * t;
    },

    // Ease in out quad
    easeInOutQuad: (t) => {
        return t < 0.5 ? 2 * t * t : 1 - Math.pow(-2 * t + 2, 2) / 2;
    },

    // Convert hex color to RGB
    hexToRgb: (hex) => {
        const result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
        return result ? {
            r: parseInt(result[1], 16),
            g: parseInt(result[2], 16),
            b: parseInt(result[3], 16)
        } : null;
    },

    // Convert RGB to hex
    rgbToHex: (r, g, b) => {
        return '#' + [r, g, b].map(x => {
            const hex = x.toString(16);
            return hex.length === 1 ? '0' + hex : hex;
        }).join('');
    },

    // Lighten/darken color
    adjustColor: (hex, amount) => {
        const rgb = Utils.hexToRgb(hex);
        if (!rgb) return hex;

        return Utils.rgbToHex(
            Utils.clamp(rgb.r + amount, 0, 255),
            Utils.clamp(rgb.g + amount, 0, 255),
            Utils.clamp(rgb.b + amount, 0, 255)
        );
    },

    // Wait for milliseconds
    wait: (ms) => new Promise(resolve => setTimeout(resolve, ms)),

    // Animate value over time
    animate: async (duration, callback, easing = Utils.easeInOutQuad) => {
        const start = performance.now();

        return new Promise(resolve => {
            const update = (currentTime) => {
                const elapsed = currentTime - start;
                const progress = Math.min(elapsed / duration, 1);
                const easedProgress = easing(progress);

                callback(easedProgress);

                if (progress < 1) {
                    requestAnimationFrame(update);
                } else {
                    resolve();
                }
            };
            requestAnimationFrame(update);
        });
    }
};

// Make available globally
window.Utils = Utils;
