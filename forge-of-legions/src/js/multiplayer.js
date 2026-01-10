/**
 * Forge of Legions - Multiplayer System
 * Handles online PvP matches using WebSocket or WebRTC
 */

const Multiplayer = {
    // Connection state
    isHost: false,
    isConnected: false,
    gameCode: null,
    localPlayer: 'player1',
    remotePlayer: 'player2',

    // WebSocket connection (for production, would connect to a server)
    ws: null,
    serverUrl: 'wss://forge-of-legions-server.example.com',

    // For local/demo mode, use BroadcastChannel
    channel: null,

    // Callbacks
    onConnect: null,
    onDisconnect: null,
    onGameStart: null,
    onAction: null,
    onChat: null,

    // Pending actions queue
    pendingActions: [],

    // Initialize multiplayer
    init: () => {
        // Try to use BroadcastChannel for local testing
        if (typeof BroadcastChannel !== 'undefined') {
            Multiplayer.useLocalMode = true;
        }
    },

    // Create a new game
    createGame: async () => {
        const code = Utils.generateGameCode();
        Multiplayer.gameCode = code;
        Multiplayer.isHost = true;
        Multiplayer.localPlayer = 'player1';
        Multiplayer.remotePlayer = 'player2';

        if (Multiplayer.useLocalMode) {
            // Local mode using BroadcastChannel
            Multiplayer.channel = new BroadcastChannel(`fol-game-${code}`);
            Multiplayer.setupChannelListeners();
        } else {
            // WebSocket mode
            await Multiplayer.connectToServer();
            Multiplayer.send({
                type: 'create_game',
                code: code,
                player: Storage.getPlayer().name
            });
        }

        // Update UI
        Multiplayer.showGameCode(code);

        return code;
    },

    // Join an existing game
    joinGame: async (code) => {
        Multiplayer.gameCode = code.toUpperCase();
        Multiplayer.isHost = false;
        Multiplayer.localPlayer = 'player2';
        Multiplayer.remotePlayer = 'player1';

        if (Multiplayer.useLocalMode) {
            Multiplayer.channel = new BroadcastChannel(`fol-game-${code.toUpperCase()}`);
            Multiplayer.setupChannelListeners();

            // Announce join
            Multiplayer.send({
                type: 'player_joined',
                player: Storage.getPlayer().name
            });
        } else {
            await Multiplayer.connectToServer();
            Multiplayer.send({
                type: 'join_game',
                code: code.toUpperCase(),
                player: Storage.getPlayer().name
            });
        }

        Multiplayer.isConnected = true;
        return true;
    },

    // Connect to WebSocket server
    connectToServer: () => {
        return new Promise((resolve, reject) => {
            try {
                Multiplayer.ws = new WebSocket(Multiplayer.serverUrl);

                Multiplayer.ws.onopen = () => {
                    Multiplayer.isConnected = true;
                    resolve();
                };

                Multiplayer.ws.onclose = () => {
                    Multiplayer.isConnected = false;
                    if (Multiplayer.onDisconnect) {
                        Multiplayer.onDisconnect();
                    }
                };

                Multiplayer.ws.onerror = (error) => {
                    console.error('WebSocket error:', error);
                    reject(error);
                };

                Multiplayer.ws.onmessage = (event) => {
                    const data = JSON.parse(event.data);
                    Multiplayer.handleMessage(data);
                };

                // Timeout
                setTimeout(() => {
                    if (!Multiplayer.isConnected) {
                        reject(new Error('Connection timeout'));
                    }
                }, 10000);
            } catch (e) {
                // Fall back to local mode if WebSocket fails
                console.warn('WebSocket not available, using local mode');
                Multiplayer.useLocalMode = true;
                resolve();
            }
        });
    },

    // Setup BroadcastChannel listeners
    setupChannelListeners: () => {
        if (!Multiplayer.channel) return;

        Multiplayer.channel.onmessage = (event) => {
            Multiplayer.handleMessage(event.data);
        };
    },

    // Send message
    send: (data) => {
        const message = {
            ...data,
            timestamp: Date.now(),
            from: Multiplayer.localPlayer
        };

        if (Multiplayer.useLocalMode && Multiplayer.channel) {
            Multiplayer.channel.postMessage(message);
        } else if (Multiplayer.ws && Multiplayer.ws.readyState === WebSocket.OPEN) {
            Multiplayer.ws.send(JSON.stringify(message));
        }
    },

    // Handle incoming message
    handleMessage: (data) => {
        // Ignore own messages
        if (data.from === Multiplayer.localPlayer) return;

        switch (data.type) {
            case 'player_joined':
                Multiplayer.isConnected = true;
                UI.showToast(`${data.player} joined the game!`, 'success');

                if (Multiplayer.isHost) {
                    // Send acknowledgment and start game
                    Multiplayer.send({
                        type: 'game_start',
                        hostName: Storage.getPlayer().name
                    });

                    if (Multiplayer.onGameStart) {
                        Multiplayer.onGameStart();
                    }
                }
                break;

            case 'game_start':
                UI.showToast(`Game starting against ${data.hostName}!`, 'success');
                if (Multiplayer.onGameStart) {
                    Multiplayer.onGameStart();
                }
                break;

            case 'action':
                // Handle game action from opponent
                if (Multiplayer.onAction) {
                    Multiplayer.onAction(data.action);
                }
                break;

            case 'army_select':
                // Opponent selected their army
                Multiplayer.opponentArmy = data.army;
                if (Multiplayer.onArmySelect) {
                    Multiplayer.onArmySelect(data.army);
                }
                break;

            case 'chat':
                if (Multiplayer.onChat) {
                    Multiplayer.onChat(data.player, data.message);
                }
                break;

            case 'disconnect':
                Multiplayer.isConnected = false;
                UI.showToast(`${data.player} disconnected`, 'error');
                if (Multiplayer.onDisconnect) {
                    Multiplayer.onDisconnect();
                }
                break;

            case 'surrender':
                UI.showToast(`${data.player} surrendered!`, 'success');
                if (Multiplayer.onSurrender) {
                    Multiplayer.onSurrender();
                }
                break;
        }
    },

    // Send game action
    sendAction: (action) => {
        Multiplayer.send({
            type: 'action',
            action: action
        });
    },

    // Send army selection
    sendArmySelect: (army) => {
        Multiplayer.send({
            type: 'army_select',
            army: army
        });
    },

    // Send chat message
    sendChat: (message) => {
        Multiplayer.send({
            type: 'chat',
            player: Storage.getPlayer().name,
            message: message
        });
    },

    // Surrender
    surrender: () => {
        Multiplayer.send({
            type: 'surrender',
            player: Storage.getPlayer().name
        });

        Multiplayer.disconnect();
    },

    // Disconnect
    disconnect: () => {
        Multiplayer.send({
            type: 'disconnect',
            player: Storage.getPlayer().name
        });

        if (Multiplayer.channel) {
            Multiplayer.channel.close();
            Multiplayer.channel = null;
        }

        if (Multiplayer.ws) {
            Multiplayer.ws.close();
            Multiplayer.ws = null;
        }

        Multiplayer.isConnected = false;
        Multiplayer.gameCode = null;
    },

    // Show game code UI
    showGameCode: (code) => {
        const codeSection = document.getElementById('game-code-section');
        const codeDisplay = document.getElementById('game-code');

        if (codeSection && codeDisplay) {
            codeDisplay.textContent = code;
            codeSection.style.display = 'block';
        }
    },

    // Quick match (for future matchmaking)
    quickMatch: async () => {
        UI.showToast('Looking for opponent...', 'info');

        // For demo, just create a game
        const code = await Multiplayer.createGame();

        // In production, would send to matchmaking server
        UI.showToast(`Waiting for match... Code: ${code}`, 'info');
    },

    // Check if it's local player's turn
    isLocalPlayerTurn: (currentPlayer) => {
        return currentPlayer === Multiplayer.localPlayer;
    },

    // Setup battlefield for multiplayer
    setupMultiplayerBattle: (battlefield) => {
        battlefield.isMultiplayer = true;
        battlefield.localPlayer = Multiplayer.localPlayer;

        battlefield.onAction = (action) => {
            Multiplayer.sendAction(action);
        };

        // Handle incoming actions
        Multiplayer.onAction = async (action) => {
            switch (action.type) {
                case 'move':
                    const unit = battlefield.units.find(u => u.id === action.unitId);
                    if (unit) {
                        await battlefield.moveUnit(unit, action.to);
                    }
                    break;

                case 'attack':
                    const attacker = battlefield.units.find(u => u.id === action.attackerId);
                    const defender = battlefield.units.find(u => u.id === action.defenderId);
                    if (attacker && defender) {
                        await battlefield.executeAttack(attacker, defender);
                    }
                    break;

                case 'ability':
                    const caster = battlefield.units.find(u => u.id === action.unitId);
                    if (caster) {
                        const ability = caster.getAbilities().find(a => a.id === action.abilityId);
                        if (ability) {
                            await battlefield.executeAbility(caster, ability, action.target);
                        }
                    }
                    break;

                case 'endTurn':
                    battlefield.endTurn();
                    break;
            }
        };
    },

    // Get player color based on local/remote
    getPlayerColor: (player) => {
        if (player === Multiplayer.localPlayer) {
            return '#4CAF50'; // Green for local
        } else {
            return '#f44336'; // Red for remote
        }
    },

    // Leaderboard (would connect to server in production)
    leaderboard: {
        getTop: async () => {
            // Mock leaderboard data
            return [
                { name: 'LegionMaster', rank: 1, wins: 256, losses: 12 },
                { name: 'WarChief', rank: 2, wins: 189, losses: 23 },
                { name: 'DeathBringer', rank: 3, wins: 167, losses: 31 },
                { name: 'IronForge', rank: 4, wins: 145, losses: 28 },
                { name: 'ShadowLord', rank: 5, wins: 134, losses: 42 }
            ];
        },

        submitScore: async (wins, losses) => {
            // Would submit to server
            console.log('Score submitted:', wins, losses);
        }
    }
};

// Make available globally
window.Multiplayer = Multiplayer;
