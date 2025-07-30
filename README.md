GangWarsRPG - The Complete Core Mechanics
This document is the final, unabridged compilation of the foundational backend logic for player progression, economy, social structures, item improvement, inventory, the in-game shop, itemization, accessories, the credit shop, and banking in GangWarsRPG.

Table of Contents
Experience (XP) System

Economy (Money) System

Gang System

Item Upgrades & Refining

4.1 Weapon Upgrades

4.2 Armor Upgrades

4.3 Refining Process

Inventory System

The Shop System

Itemization

Credit Shop

Accessories System

Banking System

1. Experience (XP) System
Experience Points (XP) are required to reach the next level in GangWars. Gaining XP is the primary measure of a player's progression and seniority, unlocking new abilities, items, or access levels.

1.1. XP Requirements by Level
The table below shows the total experience points required to advance to the next level.

|

| To Reach Level | Required XP |
| 2 | 550 |
| 3 | 1,050 |
| 4 | 1,750 |
| 5 | 2,650 |
| 6 | 3,750 |
| 7 | 5,050 |
| 8 | 6,550 |
| 9 | 8,250 |
| 10 | 10,150 |
| 11 | 12,150 |
| 12 | 14,550 |
| 13 | 17,050 |
| 14 | 19,750 |
| 15 | 22,650 |
| 16 | 25,750 |
| 17 | 29,050 |
| 18 | 32,550 |
| 19 | 36,250 |
| 20 | 40,150 |
| 21 | 44,250 |
| 22 | 48,550 |
| 23 | 53,050 |
| 24 | 57,750 |
| 25 | 62,650 |
| 26 | 67,750 |
| 27 | 73,050 |
| 28 | 78,550 |
| 29 | 84,250 |
| 30 | 90,150 |
| 31 | 96,250 |
| 32 | 102,550 |
| 33 | 109,050 |
| 34 | 115,750 |
| 35 | 122,650 |
| 36 | 129,750 |
| 37 | 137,050 |
| 38 | 144,550 |
| 39 | 152,250 |
| 40 | 160,150 |
| 41 | 168,250 |
| 42 | 176,550 |
| 43 | 185,050 |
| 44 | 193,750 |
| 45 | 202,650 |
| 46 | 211,750 |
| 47 | 221,050 |
| 48 | 230,550 |
| 49 | 240,250 |
| 50 | 250,150 |
| 51 | 260,250 |
| 52 | 270,550 |
| 53 | 281,050 |
| 54 | 291,750 |
| 55 | 302,650 |
| 56 | 313,750 |
| 57 | 325,050 |
| 58 | 336,550 |
| 59 | 348,250 |
| 60 | 360,150 |
| 61 | 372,250 |
| 62 | 384,550 |
| 63 | 397,050 |
| 64 | 409,750 |
| 65 | 422,650 |
| 66 | 435,750 |
| 67 | 449,050 |
| 68 | 462,550 |
| 69 | 476,250 |
| 70 | 490,150 |
| 71 | 504,250 |
| 72 | 518,550 |
| 73 | 533,050 |
| 74 | 547,750 |
| 75 | 562,650 |
| 76 | 577,750 |
| 77 | 593,050 |
| 78 | 608,550 |
| 79 | 624,150 |
| 80 | 640,150 |
| 81 | 656,250 |
| 82 | 672,550 |
| 83 | 689,050 |
| 84 | 705,750 |
| 85 | 722,650 |
| 86 | 739,750 |
| 87 | 757,050 |
| 88 | 774,550 |
| 89 | 792,250 |
| 90 | 810,550 |
| 91 | 810,150 |
| 92 | 846,550 |
| 93 | 865,050 |
| 94 | 883,750 |
| 95 | 902,650 |
| 96 | 921,750 |
| 97 | 941,050 |
| 98 | 960,550 |
| 99 | 980,250 |
| 100 | "Be Cool!" |

1.2. XP Acquisition Methods
| Method | Notes |
| Collecting Printer Money | See Section 2.1 for specific values. |
| Completing Hacking Missions | Higher difficulty missions yield more XP. |
| Arresting Players (Police) | XP scales with the target's wanted level. |
| Killing Other Players | Base value modified by level difference. |
| Killing Rival Gang Members | Bonus XP on top of a standard kill. |
| Depositing Money in Bank | Small XP reward to encourage banking. |
| Collecting Deposits (Banker) | XP scales with the number of deposits handled. |
| Drug Farming | XP gained upon successful sale of drugs. |

2. Economy (Money) System
Money is the central resource for acquiring goods, services, and power.

2.1. Money Printers
Money printers are a primary source of passive income. Each printer has a level requirement and produces a set amount of cash and XP every 90 seconds. VIP printers offer better returns.

| Level | Name | Cost | Output / 90s | XP / Print |
| 1 | Silver Money Printer | $1,000 | $200 | 18.5 XP |
| 3 | Tuned Gold Money Printer (VIP) | $2,000 | $400 | 44.4 XP |
| 5 | Gold Money Printer | $2,000 | $400 | 37 XP |
| 15 | Platinum Money Printer | $3,800 | $760 | 70.3 XP |
| 22 | Tuned Diamond Money Printer (VIP) | $6,400 | $1,280 | 142.1 XP |
| 25 | Diamond Money Printer | $6,400 | $1,280 | 118.4 XP |
| 35 | Emerald Money Printer | $9,800 | $1,960 | 181.3 XP |
| 42 | Tuned Money Factory (VIP) | $14,000 | $2,800 | 310.8 XP |
| 45 | Money Factory | $14,000 | $2,800 | 259 XP |
| 55 | Silver Silo | $19,400 | $3,880 | 358.1 XP |
| 62 | Tuned Gold Money Silo (VIP) | $24,800 | $4,960 | 549.8 XP |
| 65 | Gold Money Silo | $24,800 | $4,960 | 458.2 XP |
| 75 | Ruby Money Silo | $31,400 | $6,280 | 580.9 XP |
| 82 | Quantum Money Factory (VIP) | $38,800 | $7,760 | 860.2 XP |
| 85 | Nuclear Money Factory | $38,800 | $7,760 | 716.8 XP |

2.2. Other Money Acquisition Methods
| Method | Notes |
| Money Launderers | Higher yield than printers, but with associated risks. |
| Evidence Collection (Police) | Flat rate per evidence piece. |
| Arresting Wanted Player (Police) | Income is tied to the target's bounty. |
| Stock Market Investing | A complex system based on market fluctuations. |
| Selling Items/Shipments | Player-to-player transaction. |
| Bank Interest | Primary earning method from deposits. See Section 10. |
| Banker Fees | Bankers earn fees from handling deposits. See Section 10. |
| Selling Drugs | Prices can fluctuate based on server-wide sales. |
| Lottery Winnings (Mayor) | Winner receives the total pot minus a house cut. |
| Selling Security Turrets | Player-to-player transaction. |
| Stealing Goods | Transfers ownership of an item. No new money is generated. |
| Bank Robbery | Robber steals 50% of the bank's total funds. See Section 10. |
| Terrorist Map Destruction | Large, fixed payout for completing major objectives. |
| Hitman Contracts | Player-set contracts. |
| Paychecks | Fixed amount paid at regular intervals based on job. |
| Player Contracts | System to formalize player-to-player employment. |
| Pickpocketing | Steal a percentage of a target's on-hand cash. |
| Selling Found Items | Player-to-player transaction for world-spawned loot. |

3. Gang System
Gangs are a core gameplay mechanic. Being in a gang provides advantages but also creates rivalries.

3.1. Gang Experience & Leveling
Gangs gain their own experience (Gang XP) to level up. Below is the total experience required to reach each level.

| Target Level | Required XP |
| 2 | 165,000 |
| 3 | 660,000 |
| 4 | 1,485,000 |
| 5 | 2,640,000 |
| 6 | 4,125,000 |
| 7 | 5,940,000 |
| 8 | 8,085,000 |
| 9 | 10,560,000 |
| 10 | 13,365,000 |
| 11 | 16,500,000 |
| 12 | 19,965,000 |
| 13 | 23,760,000 |
| 14 | 27,885,000 |
| 15 | 32,340,000 |
| 16 | 37,125,000 |
| 17 | 42,240,000 |
| 18 | 47,685,000 |
| 19 | 53,460,000 |
| 20 | 59,565,000 |

3.2. Gang Upgrades
Gang Leaders can purchase upgrades that provide passive bonuses to all members. Each upgrade has 10 levels.

| Upgrade | Description | Effect per Level | Max Bonus |
| Gang Heart | Increase the max health of all your gang members. | +2% | +20% |
| Gang Shield | Increase the max armor of all your gang members. | +2% | +20% |
| Street Spirit | Gives your gang members regenerating health. | +0.25% / 5 Sec | +2.5% / 5 Sec |
| Made Man | Gives your gang members an EXP boost. | +2% | +20% |
| Streetwise | Gives your gang members a speed boost. | +0.5% | +5% |
| Goldfinger | Gives your gang members more money from printers. | +2.5% | +25% |
| Sticky Fingers | Your gang members grow drugs faster. | +2.5% | +25% |
| Charmed | Gives your gang members more luck in crafting. | +2.0% | +20% |
| Expansion | Allow more members to join the gang. | +2 Members | +20 Members |
| Sworn Enemy | Steal more money from rivals when you kill them. | +2.5% | +25% |
| Five Finger Discount | Get a discount on items in the gang shop. | +2% | +20% |
| Invincible | Reduce the ghost time of your gang members. | +2.5% | +25% |
| Hustler | Increase money collected when pickpocketing. | +5% | +50% |
| Wall Street | Increase money from bank deposits. | +2% | +20% |
| Goodfella | Get more XP when completing missions. | +2% | +20% |
| Wise Guys | Your gang will earn more XP overall. | +2.5% | +25% |
| Gang Land | Capture territory poles faster. | +5% | +50% |

3.3. Gang Management
| Role | Permissions |
| Gang Leader | Invite, Kick, Promote, Demote, Purchase Gang Upgrades. |
| Vice Leader | Invite, Promote, Demote (below Vice Leader). |
| Member | Standard member with access to gang benefits. |

4. Item Upgrades & Refining
Players can enhance their gear by applying upgrades.

4.1. Weapon Upgrades
| Upgrade Type | Level 1 | Level 2 | Level 3 | Level 4 | Level 5 | Level 6 | Description |
| Damage | +5% | +10% | +15% | +20% | +25% | +30% | Increases the percentage of damage that a gun does. |
| Ice Damage | +5% | +10% | +15% | +20% | +25% | +30% | Chance to slow the victim down for a few seconds. |
| Fire Damage | +5% | +10% | +15% | +20% | +25% | +30% | Chance to set the victim on fire, dealing damage over time. |
| Accuracy | +4% | +8% | +12% | +16% | +20% | +24% | Reduces weapon recoil. |

4.2. Armor Upgrades
| Upgrade Type | Level 1 | Level 2 | Level 3 | Level 4 | Level 5 | Level 6 | Description |
| Base Health | +60 | +110 | +180 | +250 | +320 | +400 | Increases the base amount of your armor's health. |
| Health Power | +3% | +6% | +9% | +12% | +15% | +18% | Adds a percentage of your standard health to the armor. |
| Base Armour | +50 | +100 | +150 | +200 | +300 | +400 | Increases the base amount of your armor's armor value. |
| Armour Strength | +3% | +6% | +9% | +12% | +15% | +18% | Adds a percentage of your standard armor to the armor. |
| Speed | +1% | +2% | +3% | +4% | +5% | +6% | Makes you run faster. |
| Fire Resistance | +3% | +6% | +9% | +12% | +15% | +18% | Makes you resistant to fire damage. |
| Ice Resistance | +3% | +6% | +9% | +12% | +15% | +18% | Makes you resistant to ice damage. |
| Absorption | +1% | +2% | +3% | +4% | +5% | +6% | Absorbs a percentage of incoming damage. |

4.3. Refining Process
Formula: 3x Upgrades of the same type and level N → 1x Upgrade of level N+1.

Example: 3x Level 2 Damage Upgrades → 1x Level 3 Damage Upgrade.

5. Inventory System
The inventory is a persistent backpack for items.

5.1. Core Mechanics
| Action | Description |
| Item Pickup | Use the "Inventory" weapon and left-click on an item. |
| Access | Opened via a HUD icon. |
| Persistence | Inventory transfers across all GangWarsRP servers. |

5.2. Inventory Capacity
| Capacity Tier | Total Slots | Method of Unlock |
| Default | [20 SLOTS] | Standard for all new players. |
| Maximum | 80 Slots (4 pages) | Upgraded via the credit shop. |

6. The Shop System
The Shop is the main interface for buying items with in-game money.

6.1. Item Categories
| Category | Examples | Job Requirement |
| Ammunition | Pistol Ammo, Rifle Ammo | N/A |
| Money Printers | Ruby, Emerald, Diamond | N/A |
| Printer Add-ons | Boosters | N/A |
| Blueprints | Car Blueprints, Weapon Blueprints | N/A |
| Consumables | Health Shipment, Armor Shipment | N/A |
| Boosts | Speed Boost, Health Boost | N/A |
| Job-Specific | Hacking Terminal | Hacker |

7. Itemization
This section defines the rarity system that governs item quality.

7.1. Item Rarity
This hierarchy defines the quality of items. Higher rarity items will have better base stats or more upgrade slots.

| Rarity Tier | Color Code |
| Standard | [Grey] |
| Rare | [Blue] |
| Unique | [Purple] |
| Elite | [Orange] |
| Epic | [Gold] |
| Legendary | [Red] |

8. Credit Shop
The Credit Shop contains items and boosts purchased with a premium currency, "credits," which are bought with real money.

8.1. Credit Packages
| Credits | Price (£) |
| 2,500 | £2.50 |
| 5,000 | £5.00 |
| 12,000 | £10.00 |
| 25,000 | £20.00 |
| 40,000 | £30.00 |

8.2. Credit Shop Items
| Item | Cost (Credits) | Description |
| V.I.P (1 Day) | 290 | Grants owner access to restricted tools & VIP items for 1 day. |
| V.I.P (2 Week) | 3,650 | Grants owner access to restricted tools & VIP items for 2 weeks. |
| XP Talisman (1 Day) | 290 | Grants the owner 1 day of +50% XP gain upon activation. |
| XP Talisman (2 Week) | 3,650 | Grants the owner 2 weeks of +50% XP gain upon activation. |
| Lucky Charm (2 Week) | 2,100 | Grants the owner 2 weeks of extra luck, increasing crafting chances. |
| Lucky Charm (4 Week) | 3,460 | Grants the owner 4 weeks of extra luck, increasing crafting chances. |
| Golden Discount (1 Week) | 1,800 | Grants the owner 1 week of 25% discount on all items purchased in the gang shop. Includes money printers. |
| Golden Discount (2 Week) | 3,460 | Grants the owner 2 week of 25% discount on all items purchased in the gang shop. Includes money printers. |
| Exclusive Contract (4 Week) | 1,000 | Grants the owner 4 weeks of immunity to demotion. |
| Steel Wallet (2 Week) | 1,000 | Grants the owner 2 weeks of immunity to pickpocketing. |
| Storage Expansion | 2,500 | Expands your storage space by +1 page. Maximum of +3 pages through expansion. |
| Portfolio Expansion | 2,850 | Grants you +50 stocks on the stock market. Maximum of +100 through expansion. |
| Builders Expansion | 1,800 | Increases your prop limit by +15 props. Maximum of +30 through expansion. |
| Spirit Extension | 1,800 | Reduces ghost time by 25%. Maximum of -50% through extension. |
| Crafters Handbook | 3,600 | +5% Chance to craft primary weapons as side weapons. Maximum of +10% through expansion. |
| Collector | 3,940 | +50% Rare craft material drops. Maximum of 100% through expansion. |
| Forge Master | 2,400 | Increases your maximum material forges +1. Maximum +2. |
| Print Master | 2,400 | Increases your maximum spawned money printers +1. Max stolen printers +2. Max of +2/+4. |
| Release Bind | 1,550 | Release the bind on an item so it can be traded. Item is transferred to inventory on purchase. |
| Reset Stone | 1,820 | Take the upgrades out of a weapon. Item is transferred to inventory on purchase. |
| Armor Reset Stone | 1,820 | Take the upgrades out of an armor. Item is transferred to inventory on purchase. |
| Takedown Orb | 1,820 | Reduce the level requirement of a weapon by 1 level. Item is transferred to inventory on purchase. |
| Armor Takedown Orb | 1,820 | Reduce the level requirement of an armor piece by 1 level. Item is transferred to inventory on purchase. |
| Naming Tablet | 1,200 | Give a weapon a custom name. Used in a Gunsmith. Item is transferred to inventory on purchase. |
| Custom Title | 2,900 | Give your character a custom title above their name. |

9. Accessories System
Accessories are upgrades placed into ring slots for passive bonuses. Rings can hold 0-2 slots.

9.1. Accessory Types & Effects
| Accessory Type | Level 1 | Level 2 | Level 3 | Level 4 | Level 5 | Level 6 |
| Experience Boost | +1% | +2% | +3% | +4% | +5% | +6% |
| Luck Boost | +1% | +2% | +3% | +4% | +5% | +6% |
| Print Amount Boost | +2% | +4% | +6% | +8% | +10% | +12% |
| Ghost Reduce | -1% | -2% | -3% | -4% | -5% | -6% |
| Base Damage | +1 | +1 | +2 | +2 | +3 | +4 |

10. Banking System
The banking system is a risk/reward mechanic for depositors and bankers.

10.1. Core Mechanics
| Role / Action | Description |
| Depositor | Gives money to a Banker to earn interest. Goal: Money. |
| Banker | Facilitates deposits for customers. Goal: XP. |
| Bank Robbery | A thief can rob the bank. If successful, deposits are lost and the robber gets 50% of the bank's total funds. |

10.2. Deposit Limits by Level
The maximum amount for a single deposit is based on player level.

| Level | Deposit Limit (Customer) | Deposit Limit (Banker) |
| 1 | $2,525 | $5,050 |
| 2 | $5,050 | (not specified) |
| 3 | $7,575 | (not specified) |
| 4 | $10,101 | (not specified) |
| 5 | $12,626 | (not specified) |
| 6 | $15,151 | (not specified) |
| 7 | $17,676 | (not specified) |
| 8 | $20,202 | (not specified) |
| 9 | $22,727 | (not specified) |
| 10 | $25,525 | (not specified) |
| 11 | $27,777 | (not specified) |
| 12 | $30,303 | (not specified) |
| 13 | $32,828 | (not specified) |
| 14 | $35,353 | (not specified) |
| 15 | $37,878 | (not specified) |
| 16 | $40,404 | (not specified) |
| 17 | $42,929 | (not specified) |
| 18 | $45,454 | (not specified) |
| 19 | $47,979 | (not specified) |
| 20 | $50,505 | (not specified) |
| 21 | $53,030 | (not specified) |
| 22 | $55,555 | (not specified) |
| 23 | $58,080 | (not specified) |
| 24 | $60,606 | (not specified) |
| 25 | $63,131 | (not specified) |
| 26 | $65,656 | (not specified) |
| 27 | $68,181 | (not specified) |
| 28 | $70,707 | (not specified) |
| 29 | $73,232 | (not specified) |
| 30 | $75,757 | (not specified) |
| 31 | $78,282 | (not specified) |
| 32 | $80,808 | (not specified) |
| 33 | $83,333 | (not specified) |
| 34 | $85,858 | (not specified) |
| 35 | $88,383 | (not specified) |
| 36 | $90,909 | (not specified) |
| 37 | $93,434 | (not specified) |
| 38 | $95,959 | (not specified) |
| 39 | $98,484 | (not specified) |
| 40 | $101,010 | (not specified) |
| 41 | $103,535 | (not specified) |
| 42 | $106,060 | (not specified) |
| 43 | $108,585 | (not specified) |
| 44 | $111,111 | (not specified) |
| 45 | $113,636 | (not specified) |
| 46 | $116,161 | (not specified) |
| 47 | $118,686 | (not specified) |
| 48 | $121,212 | (not specified) |
| 49 | $123,737 | (not specified) |
| 50 | $126,262 | (not specified) |
| 51 | $128,878 | (not specified) |
| 52 | $131,313 | (not specified) |
| 53 | $133,838 | (not specified) |
| 54 | $136,363 | (not specified) |
| 55 | $138,888 | (not specified) |
| 56 | $141,414 | (not specified) |
| 57 | $143,939 | (not specified) |
| 58 | $146,464 | (not specified) |
| 59 | $148,989 | (not specified) |
| 60 | $151,515 | (not specified) |
| 61 | $154,040 | (not specified) |
| 62 | $156,565 | (not specified) |
| 63 | $159,090 | (not specified) |
| 64 | $161,616 | (not specified) |
| 65 | $164,141 | (not specified) |
| 66 | $166,666 | (not specified) |
| 67 | $169,191 | (not specified) |
| 68 | $171,717 | (not specified) |
| 69 | $174,242 | (not specified) |
| 70 | $176,767 | (not specified) |
| 71 | $179,292 | (not specified) |
| 72 | $181,818 | (not specified) |
| 73 | $184,343 | (not specified) |
| 74 | $186,868 | (not specified) |
| 75 | $189,939 | (not specified) |
| 76 | $191,919 | (not specified) |
| 77 | $194,444 | (not specified) |
| 78 | $196,969 | (not specified) |
| 79 | $199,494 | (not specified) |
| 80 | $202,020 | (not specified) |
| 81 | $204,545 | (not specified) |
| 82 | $207,070 | (not specified) |
| 83 | $209,595 | (not specified) |
| 84 | $212,121 | (not specified) |
| 85 | $214,646 | (not specified) |
| 86 | $217,171 | (not specified) |
| 87 | $219,696 | (not specified) |
| 88 | $224,747 | (not specified) |
| 89 | (not specified) | (not specified) |
| 90 | $227,272 | (not specified) |
| 91 | $229,797 | (not specified) |
| 92 | $232,323 | (not specified) |
| 93 | $234,848 | (not specified) |
| 94 | $237,373 | (not specified) |
| 95 | $239,898 | (not specified) |
| 96 | $242,424 | (not specified) |
| 97 | $244,949 | (not specified) |
| 98 | $247,474 | (not specified) |
| 99 | $250,000 | (not specified) |
