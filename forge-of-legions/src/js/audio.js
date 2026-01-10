/**
 * Forge of Legions - Audio System
 * Handles sound effects and music
 */

const AudioManager = {
    sounds: {},
    music: null,
    musicVolume: 0.6,
    sfxVolume: 0.8,
    enabled: true,

    // Sound definitions (using Web Audio API generated sounds)
    soundDefs: {
        move: { type: 'step', duration: 0.15 },
        attack: { type: 'hit', duration: 0.2 },
        ability: { type: 'magic', duration: 0.4 },
        death: { type: 'death', duration: 0.3 },
        turnStart: { type: 'bell', duration: 0.3 },
        victory: { type: 'fanfare', duration: 1.0 },
        defeat: { type: 'defeat', duration: 0.8 },
        buttonClick: { type: 'click', duration: 0.1 },
        select: { type: 'select', duration: 0.1 },
        error: { type: 'error', duration: 0.2 }
    },

    // Audio context
    audioContext: null,

    // Initialize audio system
    init: () => {
        try {
            AudioManager.audioContext = new (window.AudioContext || window.webkitAudioContext)();
            AudioManager.loadSettings();
        } catch (e) {
            console.warn('Web Audio API not supported');
            AudioManager.enabled = false;
        }
    },

    // Load settings from storage
    loadSettings: () => {
        const settings = Storage.getSettings();
        AudioManager.sfxVolume = settings.sfxVolume / 100;
        AudioManager.musicVolume = settings.musicVolume / 100;
    },

    // Play a sound
    play: (soundName) => {
        if (!AudioManager.enabled || !AudioManager.audioContext) return;

        const soundDef = AudioManager.soundDefs[soundName];
        if (!soundDef) return;

        // Resume audio context if suspended
        if (AudioManager.audioContext.state === 'suspended') {
            AudioManager.audioContext.resume();
        }

        AudioManager.generateSound(soundDef);
    },

    // Generate procedural sound
    generateSound: (soundDef) => {
        const ctx = AudioManager.audioContext;
        const now = ctx.currentTime;

        const oscillator = ctx.createOscillator();
        const gainNode = ctx.createGain();

        oscillator.connect(gainNode);
        gainNode.connect(ctx.destination);

        // Set volume
        const volume = AudioManager.sfxVolume * 0.3;

        switch (soundDef.type) {
            case 'step':
                oscillator.type = 'sine';
                oscillator.frequency.setValueAtTime(150, now);
                oscillator.frequency.exponentialRampToValueAtTime(100, now + soundDef.duration);
                gainNode.gain.setValueAtTime(volume, now);
                gainNode.gain.exponentialRampToValueAtTime(0.01, now + soundDef.duration);
                break;

            case 'hit':
                oscillator.type = 'sawtooth';
                oscillator.frequency.setValueAtTime(200, now);
                oscillator.frequency.exponentialRampToValueAtTime(50, now + soundDef.duration);
                gainNode.gain.setValueAtTime(volume * 1.5, now);
                gainNode.gain.exponentialRampToValueAtTime(0.01, now + soundDef.duration);
                break;

            case 'magic':
                oscillator.type = 'sine';
                oscillator.frequency.setValueAtTime(400, now);
                oscillator.frequency.exponentialRampToValueAtTime(800, now + soundDef.duration * 0.5);
                oscillator.frequency.exponentialRampToValueAtTime(300, now + soundDef.duration);
                gainNode.gain.setValueAtTime(volume, now);
                gainNode.gain.exponentialRampToValueAtTime(0.01, now + soundDef.duration);
                break;

            case 'death':
                oscillator.type = 'square';
                oscillator.frequency.setValueAtTime(300, now);
                oscillator.frequency.exponentialRampToValueAtTime(50, now + soundDef.duration);
                gainNode.gain.setValueAtTime(volume, now);
                gainNode.gain.exponentialRampToValueAtTime(0.01, now + soundDef.duration);
                break;

            case 'bell':
                oscillator.type = 'sine';
                oscillator.frequency.setValueAtTime(800, now);
                gainNode.gain.setValueAtTime(volume, now);
                gainNode.gain.exponentialRampToValueAtTime(0.01, now + soundDef.duration);
                break;

            case 'fanfare':
                // Play multiple notes for victory
                const notes = [523, 659, 784, 1047];
                notes.forEach((freq, i) => {
                    const osc = ctx.createOscillator();
                    const gain = ctx.createGain();
                    osc.connect(gain);
                    gain.connect(ctx.destination);
                    osc.type = 'triangle';
                    osc.frequency.setValueAtTime(freq, now + i * 0.15);
                    gain.gain.setValueAtTime(volume, now + i * 0.15);
                    gain.gain.exponentialRampToValueAtTime(0.01, now + i * 0.15 + 0.4);
                    osc.start(now + i * 0.15);
                    osc.stop(now + i * 0.15 + 0.4);
                });
                return; // Don't start main oscillator

            case 'defeat':
                oscillator.type = 'sawtooth';
                oscillator.frequency.setValueAtTime(200, now);
                oscillator.frequency.exponentialRampToValueAtTime(80, now + soundDef.duration);
                gainNode.gain.setValueAtTime(volume, now);
                gainNode.gain.exponentialRampToValueAtTime(0.01, now + soundDef.duration);
                break;

            case 'click':
                oscillator.type = 'square';
                oscillator.frequency.setValueAtTime(1000, now);
                gainNode.gain.setValueAtTime(volume * 0.5, now);
                gainNode.gain.exponentialRampToValueAtTime(0.01, now + soundDef.duration);
                break;

            case 'select':
                oscillator.type = 'sine';
                oscillator.frequency.setValueAtTime(600, now);
                oscillator.frequency.exponentialRampToValueAtTime(800, now + soundDef.duration);
                gainNode.gain.setValueAtTime(volume * 0.5, now);
                gainNode.gain.exponentialRampToValueAtTime(0.01, now + soundDef.duration);
                break;

            case 'error':
                oscillator.type = 'square';
                oscillator.frequency.setValueAtTime(200, now);
                oscillator.frequency.setValueAtTime(150, now + 0.1);
                gainNode.gain.setValueAtTime(volume, now);
                gainNode.gain.exponentialRampToValueAtTime(0.01, now + soundDef.duration);
                break;
        }

        oscillator.start(now);
        oscillator.stop(now + soundDef.duration);
    },

    // Start background music
    startMusic: () => {
        if (!AudioManager.enabled || !AudioManager.audioContext || AudioManager.music) return;

        // Create ambient drone music
        AudioManager.music = AudioManager.createAmbientMusic();
    },

    // Create procedural ambient music
    createAmbientMusic: () => {
        const ctx = AudioManager.audioContext;

        // Create multiple oscillators for ambient pad
        const masterGain = ctx.createGain();
        masterGain.gain.setValueAtTime(AudioManager.musicVolume * 0.1, ctx.currentTime);
        masterGain.connect(ctx.destination);

        const oscillators = [];
        const baseFreqs = [130.81, 164.81, 196.00, 261.63]; // C major chord

        baseFreqs.forEach((freq, i) => {
            const osc = ctx.createOscillator();
            const gain = ctx.createGain();

            osc.type = 'sine';
            osc.frequency.setValueAtTime(freq, ctx.currentTime);

            // Slow LFO for movement
            const lfo = ctx.createOscillator();
            const lfoGain = ctx.createGain();
            lfo.frequency.setValueAtTime(0.1 + i * 0.05, ctx.currentTime);
            lfoGain.gain.setValueAtTime(5, ctx.currentTime);
            lfo.connect(lfoGain);
            lfoGain.connect(osc.frequency);
            lfo.start();

            gain.gain.setValueAtTime(0.25 - i * 0.05, ctx.currentTime);

            osc.connect(gain);
            gain.connect(masterGain);
            osc.start();

            oscillators.push({ osc, lfo, gain });
        });

        return {
            masterGain,
            oscillators,
            stop: () => {
                oscillators.forEach(({ osc, lfo }) => {
                    osc.stop();
                    lfo.stop();
                });
            }
        };
    },

    // Stop music
    stopMusic: () => {
        if (AudioManager.music) {
            AudioManager.music.stop();
            AudioManager.music = null;
        }
    },

    // Set SFX volume
    setSfxVolume: (volume) => {
        AudioManager.sfxVolume = volume / 100;
    },

    // Set music volume
    setMusicVolume: (volume) => {
        AudioManager.musicVolume = volume / 100;
        if (AudioManager.music) {
            AudioManager.music.masterGain.gain.setValueAtTime(
                AudioManager.musicVolume * 0.1,
                AudioManager.audioContext.currentTime
            );
        }
    },

    // Toggle audio
    toggle: () => {
        AudioManager.enabled = !AudioManager.enabled;
        if (!AudioManager.enabled) {
            AudioManager.stopMusic();
        }
        return AudioManager.enabled;
    }
};

// Make available globally
window.AudioManager = AudioManager;
