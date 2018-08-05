# Basic Fantasy RPG Dungeoneer Suite
# Copyright 2007-2016 Chris Gonnerman
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# Redistributions of source code must retain the above copyright
# notice, self list of conditions and the following disclaimer.
#
# Redistributions in binary form must reproduce the above copyright
# notice, self list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution.
#
# Neither the name of the author nor the names of any contributors
# may be used to endorse or promote products derived from self software
# without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# AUTHOR OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

monsters = {
    "Ant, Giant": {
        "name": "Giant Ant",
        "ac": 17,
        "daggers": 0,
        "asterisk": 0,
        "stars": 0,
        "hd": (4, 8, 0),
        "noatt": "1",
        "dam": "2d6",
        "mv": "60'",
        "noapp": (2, 6, 0),
        "sv": "F4",
        "ml": 7,
        "tt": "U",
        "dungeonlevel": 3,
        "encounterlevel": 3,
    },
    "Ape, Carnivorous": {
        "name": "Carnivorous Ape",
        "ac": 14,
        "daggers": 0,
        "asterisk": 0,
        "stars": 0,
        "hd": (4, 8, 0),
        "noatt": "2 claws",
        "dam": "1d4/1d4",
        "mv": "40'",
        "noapp": (1, 6, 0),
        "sv": "F4",
        "ml": 7,
        "tt": "None",
        "dungeonlevel": 3,
        "encounterlevel": 3,
    },
    "Basilisk": {
        "name": "Basilisk",
        "ac": 16,
        "daggers": 0,
        "asterisk": 0,
        "stars": 2,
        "hd": (6, 8, 0),
        "noatt": "1 bite/1 gaze",
        "dam": "1d10/petrification",
        "mv": "20' (10')",
        "noapp": (1, 6, 0),
        "sv": "F6",
        "ml": 9,
        "tt": "F",
        "dungeonlevel": (6, 7),
        "encounterlevel": (6, 7),
    },
    "Bear, Cave": {
        "name": "Cave Bear",
        "ac": 15,
        "daggers": 0,
        "asterisk": 0,
        "stars": 0,
        "hd": (7, 8, 0),
        "noatt": "2 claws/1 bite + hug",
        "dam": "1d8/1d8/2d6 + 2d8 hug",
        "mv": "40'",
        "noapp": (1, 2, 0),
        "sv": "F7",
        "ml": 9,
        "tt": "None",
        "dungeonlevel": (4, 5),
        "encounterlevel": (4, 5),
    },
    "Black Pudding": {
        "name": "Black Pudding",
        "asterisk": 1,
        "stars": 1,
        "daggers": 0,
        "ac": 14,
        "asterisk": 0,
        "stars": 0,
        "daggers": 0,
        "hd": (10, 8, 0),
        "noatt": "1 pseudopod",
        "dam": "3d8",
        "mv": "20'",
        "noapp": (0, 0, 1),
        "sv": "F10",
        "ml": 12,
        "tt": "None",
        "dungeonlevel": (6, 8),
        "encounterlevel": (6, 8),
    },
    "Bee, Giant": {
        "name": "Giant Bee",
        "ac": 13,
        "daggers": 0,
        "asterisk": 0,
        "stars": 1,
        "hd": (1, 4, 0),
        "noatt": "1 sting",
        "dam": "1d4 + poison",
        "mv": "10' Fly 50'",
        "noapp": (1, 6, 0),
        "sv": "F1",
        "ml": 9,
        "tt": "Special",
        "dungeonlevel": 1,
        "encounterlevel": 1,
    },
    "Beetle, Giant Bombardier": {
        "name": "Giant Bombardier Beetle",
        "ac": 16,
        "daggers": 0,
        "asterisk": 0,
        "stars": 1,
        "hd": (2, 8, 0),
        "noatt": "1 bite/1 spray",
        "dam": "1d6/2d6 (cone 10' wide by 10' long from rear of monster, save vs. Death Ray for half damage)",
        "mv": "40'",
        "noapp": (1, 8, 0),
        "sv": "F2",
        "ml": 8,
        "tt": "None",
        "dungeonlevel": 2,
        "encounterlevel": 2,
    },
    "Beetle, Giant Tiger": {
        "name": "Giant Tiger Beetle",
        "ac": 17,
        "daggers": 0,
        "asterisk": 0,
        "stars": 0,
        "hd": (3, 8, 1),
        "noatt": "1",
        "dam": "2d6",
        "mv": "50'",
        "noapp": (1, 6, 0),
        "sv": "F3",
        "ml": 9,
        "tt": "U",
        "dungeonlevel": 3,
        "encounterlevel": 3,
    },
    "Bugbear": {
        "name": "Bugbear",
        "ac": 15,
        "daggers": 0,
        "asterisk": 0,
        "stars": 0,
        "hd": (2, 8, 2),
        "noatt": "1 weapon",
        "dam": "1d8 or by weapon",
        "mv": "30'",
        "noapp": (2, 4, 0),
        "sv": "F2",
        "ml": 9,
        "tt": ("B", "L", "M"),
        "dungeonlevel": 3,
        "encounterlevel": 3,
    },
    "Caecilia, Giant": {
        "name": "Giant Caecilia",
        "ac": 14,
        "daggers": 0,
        "asterisk": 0,
        "stars": 1,
        "hd": (6, 8, 0),
        "noatt": "1 bite + swallow on 19/20",
        "dam": "1d8 + 1d8/round if swallowed",
        "mv": "20' (10')",
        "noapp": (1, 3, 0),
        "sv": "F3",
        "ml": 9,
        "tt": "B",
        "dungeonlevel": (4, 5, 6, 7),
        "encounterlevel": (4, 5, 6, 7),
    },
    "Chimera": {
        "name": "Chimera",
        "ac": 16,
        "daggers": 0,
        "asterisk": 0,
        "stars": 2,
        "hd": (9, 8, 0),
        "noatt": "2 claws/3 heads + special",
        "dam": "1d4/1d4/2d4/2d4/3d4 + special",
        "mv": "40' (10') Fly 60' (15')",
        "noapp": (1, 2, 0),
        "sv": "F9",
        "ml": 9,
        "tt": "F",
        "dungeonlevel": 8,
        "encounterlevel": 8,
    },
    "Cockatrice": {
        "name": "Cockatrice",
        "ac": 14,
        "daggers": 0,
        "asterisk": 0,
        "stars": 2,
        "hd": (5, 8, 0),
        "noatt": "1 beak + special",
        "dam": "1d6 + petrification",
        "mv": "30' Fly 60' (10')",
        "noapp": (1, 4, 0),
        "sv": "F5",
        "ml": 7,
        "tt": "D",
        "dungeonlevel": (4, 5),
        "encounterlevel": (4, 5),
    },
    "Displacer": {
        "name": "Displacer",
        "ac": 16,
        "daggers": 0,
        "asterisk": 0,
        "stars": 1,
        "hd": (6, 8, 0),
        "noatt": "2 blades",
        "dam": "1d8/1d8",
        "mv": "50'",
        "noapp": (1, 4, 0),
        "sv": "F6",
        "ml": 8,
        "tt": "D",
        "dungeonlevel": (6, 7),
        "encounterlevel": (6, 7),
    },
    "Doppleganger": {
        "name": "Doppleganger",
        "ac": 15,
        "daggers": 0,
        "asterisk": 0,
        "stars": 1,
        "hd": (4, 8, 0),
        "noatt": "1",
        "dam": "1d12 or by weapon",
        "mv": "30'",
        "noapp": (1, 6, 0),
        "sv": "F4",
        "ml": 10,
        "tt": "E",
        "dungeonlevel": (3, 4),
        "encounterlevel": (3, 4),
    },
    "Fly, Giant": {
        "name": "Giant Fly",
        "ac": 14,
        "daggers": 0,
        "asterisk": 0,
        "stars": 0,
        "hd": (2, 8, 0),
        "noatt": "1 bite",
        "dam": "1d8",
        "mv": "30' Fly 60'",
        "noapp": (1, 6, 0),
        "sv": "F1",
        "ml": 8,
        "tt": "None",
        "dungeonlevel": 2,
        "encounterlevel": 2,
    },
    "Gargoyle": {
        "name": "Gargoyle",
        "ac": 15,
        "daggers": 2,
        "asterisk": 1,
        "stars": 2,
        "hd": (4, 8, 0),
        "noatt": "2 claws/1 bite/1 horn",
        "dam": "1d4/1d4/1d6/1d4",
        "mv": "30' Fly 50' (15')",
        "noapp": (1, 6, 0),
        "sv": "F6",
        "ml": 11,
        "tt": "C",
        "dungeonlevel": 3,
        "encounterlevel": 3,
    },
    "Gelatinous Cube": {
        "name": "Gelatinous Cube",
        "ac": 12,
        "daggers": 0,
        "asterisk": 0,
        "stars": 1,
        "hd": (4, 8, 0),
        "noatt": "1",
        "dam": "2d4 + paralysis",
        "mv": "20'",
        "noapp": (0, 0, 1),
        "sv": "F2",
        "ml": 12,
        "tt": "V",
        "dungeonlevel": 3,
        "encounterlevel": 3,
    },
    "Ghoul": {
        "name": "Ghoul",
        "ac": 14,
        "daggers": 0,
        "asterisk": 0,
        "stars": 1,
        "hd": (2, 8, 0),
        "noatt": "2 claws/1 bite",
        "dam": "1d4/1d4/1d4, all plus paralysis",
        "mv": "30'",
        "noapp": (1, 6, 0),
        "sv": "F2",
        "ml": 9,
        "tt": "B",
        "dungeonlevel": 2,
        "encounterlevel": 2,
    },
    "Giant, Hill": {
        "name": "Hill Giant",
        "ac": 15,
        "daggers": 0,
        "asterisk": 0,
        "stars": 0,
        "hd": (8, 8, 0),
        "noatt": "1",
        "dam": "2d8",
        "mv": "40'",
        "noapp": (1, 4, 0),
        "sv": "F8",
        "ml": 8,
        "tt": ("E", (1, 8, 0, 1000), "GP"),
        "dungeonlevel": 8,
        "encounterlevel": 8,
    },
    "Giant, Stone": {
        "name": "Stone Giant",
        "ac": 17,
        "daggers": 0,
        "asterisk": 0,
        "stars": 0,
        "hd": (9, 8, 0),
        "noatt": "1 stone club or 1 thrown rock",
        "dam": "3d6 or 3d6",
        "mv": "40'",
        "noapp": (1, 2, 0),
        "sv": "F9",
        "ml": 9,
        "tt": ("E", (1, 8, 0, 1000), "GP"),
        "dungeonlevel": 8,
        "encounterlevel": 8,
    },
    "Gnoll": {
        "name": "Gnoll",
        "ac": 15,
        "daggers": 0,
        "asterisk": 0,
        "stars": 0,
        "hd": (2, 8, 0),
        "noatt": "1 weapon",
        "dam": "2d4 or by weapon +1",
        "mv": "30'",
        "noapp": (1, 6, 0),
        "sv": "F1",
        "ml": 8,
        "tt": ("D", "K"),
        "dungeonlevel": 2,
        "encounterlevel": 2,
    },
    "Goblin": {
        "name": "Goblin",
        "ac": 14,
        "daggers": 0,
        "asterisk": 0,
        "stars": 0,
        "hd": (1, 8, -1),
        "noatt": "1 weapon",
        "dam": "1d6 or by weapon",
        "mv": "20'",
        "noapp": (2, 4, 0),
        "sv": "F1",
        "ml": 7,
        "tt": "C",
        "dungeonlevel": 1,
        "encounterlevel": 1,
    },
    "Gray Ooze": {
        "name": "Gray Ooze",
        "ac": 12,
        "daggers": 0,
        "asterisk": 0,
        "stars": 1,
        "hd": (3, 8, 0),
        "noatt": "1",
        "dam": "2d8",
        "mv": "1'",
        "noapp": (0, 0, 1),
        "sv": "F3",
        "ml": 12,
        "tt": "None",
        "dungeonlevel": (2, 3, 4),
        "encounterlevel": (2, 3, 4),
    },
    "Green Slime": {
        "name": "Green Slime",
        "asterisk": 1,
        "stars": 2,
        "daggers": 0,
        "ac": "can always be hit",
        "hd": (2, 8, 0),
        "noatt": "1",
        "dam": "special",
        "mv": "1'",
        "noapp": (0, 0, 1),
        "sv": "F2",
        "ml": 12,
        "tt": "None",
        "dungeonlevel": 1,
        "encounterlevel": 1,
    },
    "Hellhound, 3 HD": {
        "name": "Hellhound",
        "ac": 14,
        "daggers": 0,
        "asterisk": 0,
        "stars": 2,
        "hd": (3, 8, 0),
        "noatt": "1 bite or 1 breath",
        "dam": "1d6 or 1d6 per Hit Die",
        "mv": "40'",
        "noapp": (2, 4, 0),
        "sv": "F3",
        "ml": 9,
        "tt": "C",
        "dungeonlevel": 3,
        "encounterlevel": 3,
    },
    "Hellhound, 4 HD": {
        "name": "Hellhound",
        "ac": 15,
        "daggers": 0,
        "asterisk": 0,
        "stars": 0,
        "hd": (4, 8, 0),
        "noatt": "1 bite or 1 breath",
        "dam": "1d6 or 1d6 per Hit Die",
        "mv": "40'",
        "noapp": (2, 4, 0),
        "sv": "F4",
        "ml": 9,
        "tt": "C",
        "dungeonlevel": 4,
        "encounterlevel": 4,
    },
    "Hellhound, 5 HD": {
        "name": "Hellhound",
        "ac": 16,
        "hd": (5, 8, 0),
        "sv": "F5",
        "daggers": 0,
        "asterisk": 0,
        "stars": 2,
        "noatt": "1 bite or 1 breath",
        "dam": "1d6 or 1d6 per Hit Die",
        "mv": "40'",
        "noapp": (2, 4, 0),
        "ml": 9,
        "tt": "C",
        "dungeonlevel": 5,
        "encounterlevel": 5,
    },
    "Hellhound, 6 HD": {
        "name": "Hellhound",
        "ac": 17,
        "hd": (6, 8, 0),
        "sv": "F6",
        "daggers": 0,
        "asterisk": 0,
        "stars": 2,
        "noatt": "1 bite or 1 breath",
        "dam": "1d6 or 1d6 per Hit Die",
        "mv": "40'",
        "noapp": (2, 4, 0),
        "ml": 9,
        "tt": "C",
        "dungeonlevel": 6,
        "encounterlevel": 6,
    },
    "Hellhound, 7 HD": {
        "name": "Hellhound",
        "ac": 18,
        "hd": (7, 8, 0),
        "sv": "F7",
        "daggers": 0,
        "asterisk": 0,
        "stars": 2,
        "noatt": "1 bite or 1 breath",
        "dam": "1d6 or 1d6 per Hit Die",
        "mv": "40'",
        "noapp": (2, 4, 0),
        "ml": 9,
        "tt": "C",
        "dungeonlevel": 7,
        "encounterlevel": 7,
    },
    "Hobgoblin": {
        "name": "Hobgoblin",
        "ac": 14,
        "daggers": 0,
        "asterisk": 0,
        "stars": 0,
        "hd": (1, 8, 0),
        "noatt": "1 weapon",
        "dam": "1d8 or by weapon",
        "mv": "30'",
        "noapp": (1, 6, 0),
        "sv": "F1",
        "ml": 8,
        "tt": ("D", "K"),
        "dungeonlevel": 2,
        "encounterlevel": 2,
    },
    "Hydra, 5 Headed": {
        "name": "Hydra, 5 Headed",
        "ac": 16,
        "hd": (5, 8, 0),
        "sv": "F5",
        "noatt": "5 bites",
        "daggers": 0,
        "asterisk": 0,
        "stars": 0,
        "dam": "1d10 per bite",
        "mv": "40' (10')",
        "noapp": (0, 0, 1),
        "ml": 9,
        "tt": "B",
        "dungeonlevel": 5,
        "encounterlevel": 0,
    },
    "Hydra, 6 Headed": {
        "name": "Hydra, 6 Headed",
        "ac": 17,
        "daggers": 0,
        "asterisk": 0,
        "stars": 0,
        "hd": (6, 8, 0),
        "noatt": "6 bites",
        "dam": "1d10 per bite",
        "mv": "40' (10')",
        "noapp": (0, 0, 1),
        "sv": "F6",
        "ml": 9,
        "tt": "B",
        "dungeonlevel": 6,
        "encounterlevel": (6, 7),
    },
    "Hydra, 7 Headed": {
        "name": "Hydra, 7 Headed",
        "ac": 18,
        "daggers": 0,
        "asterisk": 0,
        "stars": 0,
        "hd": (7, 8, 0),
        "noatt": "7 bites",
        "dam": "1d10 per bite",
        "mv": "40' (10')",
        "noapp": (0, 0, 1),
        "sv": "F7",
        "ml": 9,
        "tt": "B",
        "dungeonlevel": (7, 8),
        "encounterlevel": 8,
    },
    "Hydra, 8 Headed": {
        "name": "Hydra, 8 Headed",
        "ac": 19,
        "hd": (8, 8, 0),
        "sv": "F8",
        "noatt": "8 bites",
        "daggers": 0,
        "asterisk": 0,
        "stars": 0,
        "dam": "1d10 per bite",
        "mv": "40' (10')",
        "noapp": (0, 0, 1),
        "ml": 9,
        "tt": "B",
        "dungeonlevel": 8,
        "encounterlevel": 0,
    },
    "Hydra, 9 Headed": {
        "name": "Hydra, 9 Headed",
        "ac": 20,
        "hd": (9, 8, 0),
        "sv": "F9",
        "noatt": "9 bites",
        "daggers": 0,
        "asterisk": 0,
        "stars": 0,
        "dam": "1d10 per bite",
        "mv": "40' (10')",
        "noapp": (0, 0, 1),
        "ml": 9,
        "tt": "B",
        "dungeonlevel": 9,
        "encounterlevel": 0,
    },
    "Hydra, 10 Headed": {
        "name": "Hydra, 10 Headed",
        "ac": 21,
        "hd": (10, 8, 0),
        "sv": "F10",
        "noatt": "10 bites",
        "daggers": 0,
        "asterisk": 0,
        "stars": 0,
        "dam": "1d10 per bite",
        "mv": "40' (10')",
        "noapp": (0, 0, 1),
        "ml": 9,
        "tt": "B",
        "dungeonlevel": 10,
        "encounterlevel": 0,
    },
    "Hydra, 11 Headed": {
        "name": "Hydra, 11 Headed",
        "ac": 22,
        "hd": (11, 8, 0),
        "sv": "F11",
        "noatt": "11 bites",
        "daggers": 0,
        "asterisk": 0,
        "stars": 0,
        "dam": "1d10 per bite",
        "mv": "40' (10')",
        "noapp": (0, 0, 1),
        "ml": 9,
        "tt": "B",
        "dungeonlevel": 11,
        "encounterlevel": 0,
    },
    "Hydra, 12 Headed": {
        "name": "Hydra, 12 Headed",
        "ac": 23,
        "hd": (12, 8, 0),
        "sv": "F12",
        "noatt": "12 bites",
        "daggers": 0,
        "asterisk": 0,
        "stars": 0,
        "dam": "1d10 per bite",
        "mv": "40' (10')",
        "noapp": (0, 0, 1),
        "ml": 9,
        "tt": "B",
        "dungeonlevel": 12,
        "encounterlevel": 0,
    },
    "Kobold": {
        "name": "Kobold",
        "ac": 13,
        "daggers": 0,
        "asterisk": 0,
        "stars": 0,
        "hd": (1, 4, 0),
        "noatt": "1 weapon",
        "dam": "1d4 or by weapon",
        "mv": "20'",
        "noapp": (4, 4, 0),
        "sv": "NM",
        "ml": 6,
        "tt": "C",
        "dungeonlevel": 1,
        "encounterlevel": 1,
    },
    "Lizard Man": {
        "name": "Lizard Man",
        "ac": 15,
        "daggers": 0,
        "asterisk": 0,
        "stars": 0,
        "hd": (2, 8, 0),
        "noatt": "1 weapon",
        "dam": "1d6+1 or by weapon +1",
        "mv": "20'",
        "noapp": (2, 4, 0),
        "sv": "F2",
        "ml": 11,
        "tt": "D",
        "dungeonlevel": 2,
        "encounterlevel": 2,
    },
    "Lycanthrope, Wereboar": {
        "name": "Wereboar",
        "ac": 16,
        "daggers": 1,
        "asterisk": 1,
        "stars": 1,
        "hd": (4, 8, 0),
        "noatt": "1 bite",
        "dam": "2d6",
        "mv": "50' Human Form 40'",
        "noapp": (1, 4, 0),
        "sv": "F4",
        "ml": 9,
        "tt": "C",
        "dungeonlevel": 8,
        "encounterlevel": 8,
    },
    "Lycanthrope, Wererat": {
        "name": "Wererat",
        "ac": 13,
        "daggers": 1,
        "asterisk": 1,
        "stars": 1,
        "hd": (3, 8, 0),
        "noatt": "1 bite or 1 weapon",
        "dam": "1d4 or 1d6 or by weapon",
        "mv": "40'",
        "noapp": (1, 8, 0),
        "sv": "F3",
        "ml": 8,
        "tt": "C",
        "dungeonlevel": 3,
        "encounterlevel": 3,
    },
    "Lycanthrope, Weretiger": {
        "name": "Weretiger",
        "ac": 17,
        "daggers": 1,
        "asterisk": 1,
        "stars": 1,
        "hd": (5, 8, 0),
        "noatt": "2 claws/1 bite",
        "dam": "1d6/1d6/2d6",
        "mv": "50' Human Form 40'",
        "noapp": (1, 4, 0),
        "sv": "F5",
        "ml": 9,
        "tt": "C",
        "dungeonlevel": (6, 7),
        "encounterlevel": (6, 7),
    },
    "Lycanthrope, Werewolf": {
        "name": "Werewolf",
        "ac": 15,
        "daggers": 1,
        "asterisk": 1,
        "stars": 1,
        "hd": (4, 8, 0),
        "noatt": "1 bite",
        "dam": "2d4",
        "mv": "60' Human Form 40'",
        "noapp": (1, 6, 0),
        "sv": "F4",
        "ml": 8,
        "tt": "C",
        "dungeonlevel": (4, 5),
        "encounterlevel": (4, 5),
    },
    "Minotaur": {
        "name": "Minotaur",
        "ac": 14,
        "daggers": 0,
        "asterisk": 0,
        "stars": 0,
        "hd": (6, 8, 0),
        "noatt": "1 gore/1 bite or 1 weapon",
        "dam": "1d6/1d6 or by weapon + 2",
        "mv": "40'",
        "noapp": (1, 6, 0),
        "sv": "F6",
        "ml": 11,
        "tt": "C",
        "dungeonlevel": (4, 5),
        "encounterlevel": (4, 5),
    },
    "Mummy": {
        "name": "Mummy",
        "ac": 17,
        "daggers": 2,
        "asterisk": 1,
        "stars": 2,
        "hd": (5, 8, 0),
        "noatt": "1 touch + disease",
        "dam": "1d12 + disease",
        "mv": "20'",
        "noapp": (1, 4, 0),
        "sv": "F5",
        "ml": 12,
        "tt": "D",
        "dungeonlevel": (6, 7),
        "encounterlevel": (6, 7),
    },
    "Ochre Jelly": {
        "name": "Ochre Jelly",
        "ac": 12,
        "daggers": 0,
        "asterisk": 1,
        "stars": 1,
        "hd": (5, 8, 0),
        "noatt": "1",
        "dam": "2d6",
        "mv": "10'",
        "noapp": (0, 0, 1),
        "sv": "F5",
        "ml": 12,
        "tt": "None",
        "dungeonlevel": (4, 5),
        "encounterlevel": (4, 5),
    },
    "Ogre": {
        "name": "Ogre",
        "ac": 15,
        "daggers": 0,
        "asterisk": 0,
        "stars": 0,
        "hd": (4, 8, 1),
        "noatt": "1 weapon",
        "dam": "2d6",
        "mv": "30'",
        "noapp": (1, 6, 0),
        "sv": "F4",
        "ml": 10,
        "tt": ("C", (1, 20, 0, 100), "GP"),
        "dungeonlevel": 3,
        "encounterlevel": 3,
    },
    "Orc": {
        "name": "Orc",
        "ac": 14,
        "daggers": 0,
        "asterisk": 0,
        "stars": 0,
        "hd": (1, 8, 0),
        "noatt": "1 weapon",
        "dam": "1d8 or by weapon",
        "mv": "40'",
        "noapp": (2, 4, 0),
        "sv": "F1",
        "ml": 8,
        "tt": "D",
        "dungeonlevel": 1,
        "encounterlevel": 1,
    },
    "Owlbear": {
        "name": "Owlbear",
        "ac": 15,
        "daggers": 0,
        "asterisk": 0,
        "stars": 0,
        "hd": (5, 8, 0),
        "noatt": "2 claws/1 bite + 1 hug",
        "dam": "1d8/1d8/1d8 + 2d8",
        "mv": "40'",
        "noapp": (1, 4, 0),
        "sv": "F5",
        "ml": 9,
        "tt": "C",
        "dungeonlevel": (4, 5, 6, 7),
        "encounterlevel": (4, 5, 6, 7),
    },
    "Purple Worm, 11 HD": {
        "name": "Purple Worm",
        "ac": 16,
        "daggers": 0,
        "asterisk": 0,
        "stars": 1,
        "hd": (11, 8, 0),
        "noatt": "1 bite/1 sting",
        "dam": "2d8/1d8+poison",
        "mv": "20' (15')",
        "noapp": (1, 2, 0),
        "sv": "F6",
        "ml": 10,
        "tt": "None",
        "dungeonlevel": 8,
        "encounterlevel": 8,
    },
    "Purple Worm, 12 HD": {
        "name": "Purple Worm",
        "ac": 16,
        "daggers": 0,
        "asterisk": 0,
        "stars": 1,
        "hd": (12, 8, 0),
        "noatt": "1 bite/1 sting",
        "dam": "2d8/1d8+poison",
        "mv": "20' (15')",
        "noapp": (1, 2, 0),
        "sv": "F6",
        "ml": 10,
        "tt": "None",
        "dungeonlevel": 12,
        "encounterlevel": 0,
    },
    "Purple Worm, 13 HD": {
        "name": "Purple Worm",
        "ac": 16,
        "daggers": 0,
        "asterisk": 0,
        "stars": 1,
        "hd": (13, 8, 0),
        "noatt": "1 bite/1 sting",
        "dam": "2d8/1d8+poison",
        "mv": "20' (15')",
        "noapp": (1, 2, 0),
        "sv": "F7",
        "ml": 10,
        "tt": "None",
        "dungeonlevel": 13,
        "encounterlevel": 0,
    },
    "Purple Worm, 14 HD": {
        "name": "Purple Worm",
        "ac": 16,
        "daggers": 0,
        "asterisk": 0,
        "stars": 1,
        "hd": (14, 8, 0),
        "noatt": "1 bite/1 sting",
        "dam": "2d8/1d8+poison",
        "mv": "20' (15')",
        "noapp": (1, 2, 0),
        "sv": "F7",
        "ml": 10,
        "tt": "None",
        "dungeonlevel": 14,
        "encounterlevel": 0,
    },
    "Purple Worm, 15 HD": {
        "name": "Purple Worm",
        "ac": 16,
        "daggers": 0,
        "asterisk": 0,
        "stars": 1,
        "hd": (15, 8, 0),
        "noatt": "1 bite/1 sting",
        "dam": "2d8/1d8+poison",
        "mv": "20' (15')",
        "noapp": (1, 2, 0),
        "sv": "F8",
        "ml": 10,
        "tt": "None",
        "dungeonlevel": 15,
        "encounterlevel": 0,
    },
    "Purple Worm, 16 HD": {
        "name": "Purple Worm",
        "ac": 16,
        "daggers": 0,
        "asterisk": 0,
        "stars": 1,
        "hd": (16, 8, 0),
        "noatt": "1 bite/1 sting",
        "dam": "2d8/1d8+poison",
        "mv": "20' (15')",
        "noapp": (1, 2, 0),
        "sv": "F8",
        "ml": 10,
        "tt": "None",
        "dungeonlevel": 16,
        "encounterlevel": 0,
    },
    "Purple Worm, 17 HD": {
        "name": "Purple Worm",
        "ac": 16,
        "daggers": 0,
        "asterisk": 0,
        "stars": 1,
        "hd": (17, 8, 0),
        "noatt": "1 bite/1 sting",
        "dam": "2d8/1d8+poison",
        "mv": "20' (15')",
        "noapp": (1, 2, 0),
        "sv": "F9",
        "ml": 10,
        "tt": "None",
        "dungeonlevel": 17,
        "encounterlevel": 0,
    },
    "Purple Worm, 18 HD": {
        "name": "Purple Worm",
        "ac": 16,
        "daggers": 0,
        "asterisk": 0,
        "stars": 1,
        "hd": (18, 8, 0),
        "noatt": "1 bite/1 sting",
        "dam": "2d8/1d8+poison",
        "mv": "20' (15')",
        "noapp": (1, 2, 0),
        "sv": "F9",
        "ml": 10,
        "tt": "None",
        "dungeonlevel": 18,
        "encounterlevel": 0,
    },
    "Purple Worm, 19 HD": {
        "name": "Purple Worm",
        "ac": 16,
        "daggers": 0,
        "asterisk": 0,
        "stars": 1,
        "hd": (19, 8, 0),
        "noatt": "1 bite/1 sting",
        "dam": "2d8/1d8+poison",
        "mv": "20' (15')",
        "noapp": (1, 2, 0),
        "sv": "F10",
        "ml": 10,
        "tt": "None",
        "dungeonlevel": 19,
        "encounterlevel": 0,
    },
    "Purple Worm, 20 HD": {
        "name": "Purple Worm",
        "ac": 16,
        "daggers": 0,
        "asterisk": 0,
        "stars": 1,
        "hd": (20, 8, 0),
        "noatt": "1 bite/1 sting",
        "dam": "2d8/1d8+poison",
        "mv": "20' (15')",
        "noapp": (1, 2, 0),
        "sv": "F10",
        "ml": 10,
        "tt": "None",
        "dungeonlevel": 20,
        "encounterlevel": 0,
    },
    "Rust Monster": {
        "name": "Rust Monster",
        "ac": 18,
        "daggers": 0,
        "asterisk": 1,
        "stars": 1,
        "hd": (5, 8, 0),
        "noatt": "1",
        "dam": "special",
        "mv": "40'",
        "noapp": (1, 4, 0),
        "sv": "F5",
        "ml": 7,
        "tt": "None",
        "dungeonlevel": (4, 5, 6, 7),
        "encounterlevel": (4, 5, 6, 7),
    },
    "Salamander, Flame": {
        "name": "Flame Salamander",
        "ac": 19,
        "daggers": 2,
        "asterisk": 1,
        "stars": 1,
        "hd": (8, 8, 0),
        "noatt": "2 claws/1 bite+heat",
        "dam": "1d4/1d4/1d8+1d8/round",
        "mv": "40'",
        "noapp": (1, 4, 1),
        "sv": "F8",
        "ml": 8,
        "tt": "F",
        "dungeonlevel": 8,
        "encounterlevel": 8,
    },
    "Salamander, Frost": {
        "name": "Frost Salamander",
        "ac": 21,
        "daggers": 2,
        "asterisk": 1,
        "stars": 1,
        "hd": (12, 8, 0),
        "noatt": "4 claws/1 bite+cold",
        "dam": "1d6/1d6/1d6/1d6/2d6+1d8/round",
        "mv": "40'",
        "noapp": (1, 3, 0),
        "sv": "F12",
        "ml": 9,
        "tt": "E",
        "dungeonlevel": 8,
        "encounterlevel": 8,
    },
    "Scorpion, Giant": {
        "name": "Scorpion, Giant",
        "ac": 15,
        "daggers": 0,
        "asterisk": 0,
        "stars": 1,
        "hd": (4, 8, 0),
        "noatt": "2 claws/1 stinger",
        "dam": "1d10/1d10/1d6 + poison",
        "mv": "50' (10')",
        "noapp": (1, 6, 0),
        "sv": "F2",
        "ml": 11,
        "tt": "None",
        "dungeonlevel": (6, 7),
        "encounterlevel": (6, 7),
    },
    "Shadow": {
        "name": "Shadow",
        "ac": 13,
        "daggers": 2,
        "asterisk": 1,
        "stars": 1,
        "hd": (2, 8, 0),
        "noatt": "1 touch",
        "dam": "1d4 + 1 point Strength loss",
        "mv": "30'",
        "noapp": (1, 10, 0),
        "sv": "F2",
        "ml": 12,
        "tt": "F",
        "dungeonlevel": 3,
        "encounterlevel": 3,
    },
    "Shrieker": {
        "name": "Shrieker",
        "ac": 13,
        "daggers": 0,
        "asterisk": 0,
        "stars": 0,
        "hd": (3, 8, 0),
        "noatt": "Special",
        "dam": "None",
        "mv": "5'",
        "noapp": (1, 8, 0),
        "sv": "F1",
        "ml": 12,
        "tt": "None",
        "dungeonlevel": (1, 2, 3, 4, 5, 6, 7, 8),
        "encounterlevel": 0,
    },
    "Skeleton": {
        "name": "Skeleton",
        "ac": 13,
        "daggers": 0,
        "asterisk": 0,
        "stars": 0,
        "hd": (1, 8, 0),
        "noatt": "1",
        "dam": "1d6 or by weapon",
        "mv": "40'",
        "noapp": (3, 4, 0),
        "sv": "F1",
        "ml": 12,
        "tt": "None",
        "dungeonlevel": 1,
        "encounterlevel": 1,
    },
    "Snake, Pit Viper": {
        "name": "Pit Viper",
        "ac": 14,
        "daggers": 0,
        "asterisk": 0,
        "stars": 1,
        "hd": (2, 8, 0),
        "noatt": "1 bite",
        "dam": "1d4 + poison",
        "mv": "30'",
        "noapp": (1, 8, 0),
        "sv": "F2",
        "ml": 7,
        "tt": "None",
        "dungeonlevel": 2,
        "encounterlevel": 2,
    },
    "Snake, Spitting Cobra": {
        "name": "Spitting Cobra",
        "ac": 13,
        "daggers": 0,
        "asterisk": 0,
        "stars": 1,
        "hd": (1, 8, 0),
        "noatt": "1 bite or 1 spit",
        "dam": "1d4 + poison or blindness",
        "mv": "30'",
        "noapp": (1, 6, 0),
        "sv": "F1",
        "ml": 7,
        "tt": "None",
        "dungeonlevel": 1,
        "encounterlevel": 1,
    },
    "Spectre": {
        "name": "Spectre",
        "ac": 17,
        "daggers": 2,
        "asterisk": 1,
        "stars": 2,
        "hd": (6, 8, 0),
        "noatt": "1 touch",
        "dam": "Energy drain 2 levels/touch",
        "mv": "Fly 100'",
        "noapp": (1, 4, 0),
        "sv": "F6",
        "ml": 11,
        "tt": "E",
        "dungeonlevel": (6, 7),
        "encounterlevel": (6, 7),
    },
    "Spider, Giant Black Widow": {
        "name": "Giant Black Widow Spider",
        "ac": 14,
        "daggers": 0,
        "asterisk": 0,
        "stars": 1,
        "hd": (3, 8, 0),
        "noatt": "1 bite",
        "dam": "2d6 + poison",
        "mv": "20' Web 40'",
        "noapp": (1, 3, 0),
        "sv": "F3",
        "ml": 8,
        "tt": "None",
        "dungeonlevel": 2,
        "encounterlevel": 2,
    },
    "Spider, Giant Crab": {
        "name": "Giant Crab Spider",
        "ac": 13,
        "daggers": 0,
        "asterisk": 0,
        "stars": 1,
        "hd": (2, 8, 0),
        "noatt": "1 bite",
        "dam": "1d8 + poison",
        "mv": "40'",
        "noapp": (1, 4, 0),
        "sv": "F2",
        "ml": 7,
        "tt": "None",
        "dungeonlevel": 1,
        "encounterlevel": 1,
    },
    "Stirge": {
        "name": "Stirge",
        "ac": 13,
        "daggers": 0,
        "asterisk": 0,
        "stars": 1,
        "hd": (1, 8, 0),
        "noatt": "1 bite",
        "dam": "1d4 + 1d4/round blood drain",
        "mv": "10' Fly 60'",
        "noapp": (1, 10, 0),
        "sv": "F1",
        "ml": 9,
        "tt": "D",
        "dungeonlevel": 1,
        "encounterlevel": 1,
    },
    "Tentacle Worm": {
        "name": "Tentacle Worm",
        "ac": 13,
        "daggers": 0,
        "asterisk": 0,
        "stars": 1,
        "hd": (3, 8, 0),
        "noatt": "6 tentacles",
        "dam": "paralysis",
        "mv": "40'",
        "noapp": (1, 3, 0),
        "sv": "F3",
        "ml": 9,
        "tt": "B",
        "dungeonlevel": 3,
        "encounterlevel": 3,
    },
    "Troglodyte": {
        "name": "Troglodyte",
        "ac": 15,
        "daggers": 0,
        "asterisk": 0,
        "stars": 0,
        "hd": (2, 8, 0),
        "noatt": "2 claws/1 bite",
        "dam": "1d4/1d4/1d4",
        "mv": "40'",
        "noapp": (1, 8, 0),
        "sv": "F2",
        "ml": 9,
        "tt": "A",
        "dungeonlevel": 2,
        "encounterlevel": 2,
    },
    "Troll": {
        "name": "Troll",
        "ac": 16,
        "daggers": 0,
        "asterisk": 0,
        "stars": 1,
        "hd": (6, 8, 0),
        "noatt": "3",
        "dam": "1d6/1d6/1d10",
        "mv": "40'",
        "noapp": (1, 8, 0),
        "sv": "F6",
        "ml": 10,
        "tt": "D",
        "dungeonlevel": (6, 7),
        "encounterlevel": (6, 7),
    },
    "Vampire, 7 HD": {
        "name": "Vampire",
        "ac": 18,
        "daggers": 2,
        "asterisk": 1,
        "stars": 2,
        "hd": (7, 8, 0),
        "noatt": "1 weapon or special",
        "dam": "1d8 or by weapon or special",
        "mv": "40' Fly 60'",
        "noapp": (1, 6, 0),
        "sv": "F7",
        "ml": 11,
        "tt": "F",
        "dungeonlevel": 8,
        "encounterlevel": 8,
    },
    "Vampire, 8 HD": {
        "name": "Vampire",
        "ac": 19,
        "daggers": 2,
        "asterisk": 1,
        "stars": 2,
        "hd": (8, 8, 0),
        "noatt": "1 weapon or special",
        "dam": "1d8 or by weapon or special",
        "mv": "40' Fly 60'",
        "noapp": (1, 6, 0),
        "sv": "F8",
        "ml": 11,
        "tt": "F",
        "dungeonlevel": 9,
        "encounterlevel": 0,
    },
    "Vampire, 9 HD": {
        "name": "Vampire",
        "ac": 20,
        "daggers": 2,
        "asterisk": 1,
        "stars": 2,
        "hd": (9, 8, 0),
        "noatt": "1 weapon or special",
        "dam": "1d8 or by weapon or special",
        "mv": "40' Fly 60'",
        "noapp": (1, 6, 0),
        "sv": "F9",
        "ml": 11,
        "tt": "F",
        "dungeonlevel": 10,
        "encounterlevel": 0,
    },
    "Wight": {
        "name": "Wight",
        "ac": 15,
        "daggers": 1,
        "asterisk": 1,
        "stars": 1,
        "hd": (3, 8, 0),
        "noatt": "1 touch",
        "dam": "Energy drain (1 level)",
        "mv": "30'",
        "noapp": (1, 6, 0),
        "sv": "F3",
        "ml": 12,
        "tt": "B",
        "dungeonlevel": 3,
        "encounterlevel": 3,
    },
    "Wolf": {
        "name": "Wolf",
        "ac": 13,
        "daggers": 0,
        "asterisk": 0,
        "stars": 0,
        "hd": (2, 8, 0),
        "noatt": "1 bite",
        "dam": "1d6",
        "mv": "60'",
        "noapp": (2, 6, 0),
        "sv": "F2",
        "ml": 8,
        "tt": "None",
        "dungeonlevel": 1,
        "encounterlevel": 1,
    },
    "Wraith": {
        "name": "Wraith",
        "ac": 15,
        "daggers": 2,
        "asterisk": 1,
        "stars": 2,
        "hd": (4, 8, 0),
        "noatt": "1 touch",
        "dam": "1d6 + energy drain (1 level)",
        "mv": "Fly 80'",
        "noapp": (1, 4, 0),
        "sv": "F4",
        "ml": 12,
        "tt": "E",
        "dungeonlevel": (4, 5),
        "encounterlevel": (4, 5),
    },
    "Zombie": {
        "name": "Zombie",
        "ac": 12,
        "daggers": 0,
        "asterisk": 0,
        "stars": 0,
        "hd": (2, 8, 0),
        "noatt": "1",
        "dam": "1d8 or by weapon",
        "mv": "20'",
        "noapp": (2, 4, 0),
        "sv": "F2",
        "ml": 12,
        "tt": "None",
        "dungeonlevel": 2,
        "encounterlevel": 2,
    },
}

# end of file.
