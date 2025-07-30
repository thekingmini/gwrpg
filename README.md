# Core Mechanics Documentation

This document is the final, unabridged compilation of the foundational backend logic for player progression, the economy, social structures, equipment improvement, inventory, the in-game marketplace, asset classification, accessories, the premium store, and the financial system.

## Table of Contents

1.  [Progression System](#1-progression-system)
    *   [1.1. Experience Requirements by Level](#11-experience-requirements-by-level)
    *   [1.2. Experience Acquisition Methods](#12-experience-acquisition-methods)
2.  [Economic System](#2-economic-system)
    *   [2.1. Currency Generators](#21-currency-generators)
    *   [2.2. Other Currency Acquisition Methods](#22-other-currency-acquisition-methods)
3.  [Faction System](#3-faction-system)
    *   [3.1. Faction Experience & Leveling](#31-faction-experience--leveling)
    *   [3.2. Faction Perks](#32-faction-perks)
    *   [3.3. Faction Management](#33-faction-management)
4.  [Equipment Enhancement & Synthesis](#4-equipment-enhancement--synthesis)
    *   [4.1. Weapon Modifications](#41-weapon-modifications)
    *   [4.2. Armor Modifications](#42-armor-modifications)
    *   [4.3. Synthesis Process](#43-synthesis-process)
5.  [Stash System](#5-stash-system)
    *   [5.1. Core Mechanics](#51-core-mechanics)
    *   [5.2. Stash Capacity](#52-stash-capacity)
6.  [Marketplace System](#6-marketplace-system)
    *   [6.1. Asset Categories](#61-asset-categories)
7.  [Asset Classification](#7-asset-classification)
    *   [7.1. Asset Rarity](#71-asset-rarity)
8.  [Premium Store](#8-premium-store)
    *   [8.1. Premium Credit Packages](#81-premium-credit-packages)
    *   [8.2. Premium Store Offerings](#82-premium-store-offerings)
9.  [Trinket System](#9-trinket-system)
    *   [9.1. Trinket Types & Effects](#91-trinket-types--effects)
10. [Financial System](#10-financial-system)
    *   [10.1. Core Mechanics](#101-core-mechanics)
    *   [10.2. Deposit Limits by Level](#102-deposit-limits-by-level)

---

## 1. Progression System

Experience Points (XP) are required to reach the next level. Gaining XP is the primary measure of a player's progression and seniority, unlocking new abilities, assets, or access levels.

### 1.1. Experience Requirements by Level

The table below shows the total experience points required to advance to the next level.

| To Reach Level | Required XP |
| :------------- | :---------- |
| 2              | 550         |
| 3              | 1,050       |
| 4              | 1,750       |
| 5              | 2,650       |
| 6              | 3,750       |
| 7              | 5,050       |
| 8              | 6,550       |
| 9              | 8,250       |
| 10             | 10,150      |
| 11             | 12,150      |
| 12             | 14,550      |
| 13             | 17,050      |
| 14             | 19,750      |
| 15             | 22,650      |
| 16             | 25,750      |
| 17             | 29,050      |
| 18             | 32,550      |
| 19             | 36,250      |
| 20             | 40,150      |
| 21             | 44,250      |
| 22             | 48,550      |
| 23             | 53,050      |
| 24             | 57,750      |
| 25             | 62,650      |
| 26             | 67,750      |
| 27             | 73,050      |
| 28             | 78,550      |
| 29             | 84,250      |
| 30             | 90,150      |
| 31             | 96,250      |
| 32             | 102,550     |
| 33             | 109,050     |
| 34             | 115,750     |
| 35             | 122,650     |
| 36             | 129,750     |
| 37             | 137,050     |
| 38             | 144,550     |
| 39             | 152,250     |
| 40             | 160,150     |
| 41             | 168,250     |
| 42             | 176,550     |
| 43             | 185,050     |
| 44             | 193,750     |
| 45             | 202,650     |
| 46             | 211,750     |
| 47             | 221,050     |
| 48             | 230,550     |
| 49             | 240,250     |
| 50             | 250,150     |
| 51             | 260,250     |
| 52             | 270,550     |
| 53             | 281,050     |
| 54             | 291,750     |
| 55             | 302,650     |
| 56             | 313,750     |
| 57             | 325,050     |
| 58             | 336,550     |
| 59             | 348,250     |
| 60             | 360,150     |
| 61             | 372,250     |
| 62             | 384,550     |
| 63             | 397,050     |
| 64             | 409,750     |
| 65             | 422,650     |
| 66             | 435,750     |
| 67             | 449,050     |
| 68             | 462,550     |
| 69             | 476,250     |
| 70             | 490,150     |
| 71             | 504,250     |
| 72             | 518,550     |
| 73             | 533,050     |
| 74             | 547,750     |
| 75             | 562,650     |
| 76             | 577,750     |
| 77             | 593,050     |
| 78             | 608,550     |
| 79             | 624,150     |
| 80             | 640,150     |
| 81             | 656,250     |
| 82             | 672,550     |
| 83             | 689,050     |
| 84             | 705,750     |
| 85             | 722,650     |
| 86             | 739,750     |
| 87             | 757,050     |
| 88             | 774,550     |
| 89             | 792,250     |
| 90             | 810,550     |
| 91             | 810,150     |
| 92             | 846,550     |
| 93             | 865,050     |
| 94             | 883,750     |
| 95             | 902,650     |
| 96             | 921,750     |
| 97             | 941,050     |
| 98             | 960,550     |
| 99             | 980,250     |
| 100            | "Be Cool!"  |

### 1.2. Experience Acquisition Methods

| Method                               | Notes                                               |
| :----------------------------------- | :-------------------------------------------------- |
| Collecting from Currency Generators  | See Section 2.1 for specific values.                |
| Completing Cyber Ops                 | Higher difficulty missions yield more XP.           |
| Detaining Opponents (Enforcer)       | XP scales with the target's wanted level.           |
| Defeating Other Players              | Base value modified by level difference.            |
| Defeating Rival Faction Members      | Bonus XP on top of a standard defeat.               |
| Depositing Currency in Bank          | Small XP reward to encourage banking.               |
| Collecting Deposits (Banker)         | XP scales with the number of deposits handled.      |
| Trafficking Contraband               | XP gained upon successful sale of illicit goods.    |

## 2. Economic System

Currency is the central resource for acquiring goods, services, and power.

### 2.1. Currency Generators

Currency generators are a primary source of passive income. Each generator has a level requirement and produces a set amount of currency and XP every 90 seconds. VIP generators offer better returns.

| Level | Name                            | Cost     | Output / 90s | XP / Print |
| :---- | :------------------------------ | :------- | :----------- | :--------- |
| 1     | Silver Currency Generator       | $1,000   | $200         | 18.5 XP    |
| 3     | Tuned Gold Generator (VIP)      | $2,000   | $400         | 44.4 XP    |
| 5     | Gold Currency Generator         | $2,000   | $400         | 37 XP      |
| 15    | Platinum Currency Generator     | $3,800   | $760         | 70.3 XP    |
| 22    | Tuned Diamond Generator (VIP)   | $6,400   | $1,280       | 142.1 XP   |
| 25    | Diamond Currency Generator      | $6,400   | $1,280       | 118.4 XP   |
| 35    | Emerald Currency Generator      | $9,800   | $1,960       | 181.3 XP   |
| 42    | Tuned Currency Factory (VIP)    | $14,000  | $2,800       | 310.8 XP   |
| 45    | Currency Factory                | $14,000  | $2,800       | 259 XP     |
| 55    | Silver Silo                     | $19,400  | $3,880       | 358.1 XP   |
| 62    | Tuned Gold Currency Silo (VIP)  | $24,800  | $4,960       | 549.8 XP   |
| 65    | Gold Currency Silo              | $24,800  | $4,960       | 458.2 XP   |
| 75    | Ruby Currency Silo              | $31,400  | $6,280       | 580.9 XP   |
| 82    | Quantum Currency Factory (VIP)  | $38,800  | $7,760       | 860.2 XP   |
| 85    | Nuclear Currency Factory        | $38,800  | $7,760       | 716.8 XP   |

### 2.2. Other Currency Acquisition Methods

| Method                            | Notes                                                      |
| :-------------------------------- | :--------------------------------------------------------- |
| Currency Launderers               | Higher yield than generators, but with associated risks.   |
| Evidence Collection (Enforcer)    | Flat rate per evidence piece.                              |
| Detaining Wanted Player (Enforcer)| Income is tied to the target's bounty.                     |
| Stock Market Investing            | A complex system based on market fluctuations.             |
| Selling Assets/Shipments          | Player-to-player transaction.                              |
| Bank Interest                     | Primary earning method from deposits. See Section 10.      |
| Banker Fees                       | Bankers earn fees from handling deposits. See Section 10.  |
| Selling Contraband                | Prices can fluctuate based on server-wide sales.           |
| Lottery Winnings (Overseer)       | Winner receives the total pot minus a house cut.           |
| Selling Security Turrets          | Player-to-player transaction.                              |
| Stealing Goods                    | Transfers ownership of an asset. No new currency is generated. |
| Bank Heist                        | Robber steals 50% of the bank's total funds. See Section 10. |
| Insurgent Map Sabotage            | Large, fixed payout for completing major objectives.       |
| Mercenary Contracts               | Player-set contracts.                                      |
| Paychecks                         | Fixed amount paid at regular intervals based on job.       |
| Player Contracts                  | System to formalize player-to-player employment.           |
| Pickpocketing                     | Steal a percentage of a target's on-hand currency.         |
| Selling Found Assets              | Player-to-player transaction for world-spawned loot.       |

## 3. Faction System

Factions are a core gameplay mechanic. Being in a faction provides advantages but also creates rivalries.

### 3.1. Faction Experience & Leveling

Factions gain their own experience (Faction XP) to level up. Below is the total experience required to reach each level.

| Target Level | Required XP  |
| :----------- | :----------- |
| 2            | 165,000      |
| 3            | 660,000      |
| 4            | 1,485,000    |
| 5            | 2,640,000    |
| 6            | 4,125,000    |
| 7            | 5,940,000    |
| 8            | 8,085,000    |
| 9            | 10,560,000   |
| 10           | 13,365,000   |
| 11           | 16,500,000   |
| 12           | 19,965,000   |
| 13           | 23,760,000   |
| 14           | 27,885,000   |
| 15           | 32,340,000   |
| 16           | 37,125,000   |
| 17           | 42,240,000   |
| 18           | 47,685,000   |
| 19           | 53,460,000   |
| 20           | 59,565,000   |

### 3.2. Faction Perks

Faction Leaders can purchase perks that provide passive bonuses to all members. Each perk has 10 levels.

| Perk                | Description                                        | Effect per Level   | Max Bonus        |
| :------------------ | :------------------------------------------------- | :----------------- | :--------------- |
| Faction Heart       | Increase the max health of all your members.       | +2%                | +20%             |
| Faction Shield      | Increase the max armor of all your members.        | +2%                | +20%             |
| Street Spirit       | Gives your members regenerating health.            | +0.25% / 5 Sec     | +2.5% / 5 Sec    |
| Made Man            | Gives your members an EXP boost.                   | +2%                | +20%             |
| Streetwise          | Gives your members a speed boost.                  | +0.5%              | +5%              |
| Goldfinger          | Gives your members more currency from generators.  | +2.5%              | +25%             |
| Sticky Fingers      | Your members cultivate contraband faster.          | +2.5%              | +25%             |
| Charmed             | Gives your members more luck in crafting.          | +2.0%              | +20%             |
| Expansion           | Allow more members to join the faction.            | +2 Members         | +20 Members      |
| Sworn Enemy         | Steal more currency from rivals when you defeat them.| +2.5%              | +25%             |
| Five Finger Discount| Get a discount on assets in the faction store.     | +2%                | +20%             |
| Invincible          | Reduce the respawn time of your members.           | +2.5%              | +25%             |
| Hustler             | Increase currency collected when pickpocketing.    | +5%                | +50%             |
| Wall Street         | Increase currency from bank deposits.              | +2%                | +20%             |
| Goodfella           | Get more XP when completing missions.              | +2%                | +20%             |
| Wise Guys           | Your faction will earn more XP overall.            | +2.5%              | +25%             |
| Faction Land        | Capture territory faster.                          | +5%                | +50%             |

### 3.3. Faction Management

| Role           | Permissions                                         |
| :------------- | :-------------------------------------------------- |
| Faction Leader | Invite, Kick, Promote, Demote, Purchase Faction Perks.|
| Vice Leader    | Invite, Promote, Demote (below Vice Leader).        |
| Member         | Standard member with access to faction benefits.    |

## 4. Equipment Enhancement & Synthesis

Players can enhance their gear by applying modifications.

### 4.1. Weapon Modifications

| Modification Type | Level 1 | Level 2 | Level 3 | Level 4 | Level 5 | Level 6 | Description                                               |
| :---------------- | :------ | :------ | :------ | :------ | :------ | :------ | :-------------------------------------------------------- |
| Damage            | +5%     | +10%    | +15%    | +20%    | +25%    | +30%    | Increases the percentage of damage that a weapon does.    |
| Ice Damage        | +5%     | +10%    | +15%    | +20%    | +25%    | +30%    | Chance to slow the victim down for a few seconds.         |
| Fire Damage       | +5%     | +10%    | +15%    | +20%    | +25%    | +30%    | Chance to set the victim on fire, dealing damage over time. |
| Accuracy          | +4%     | +8%     | +12%    | +16%    | +20%    | +24%    | Reduces weapon recoil.                                    |

### 4.2. Armor Modifications

| Modification Type | Level 1 | Level 2 | Level 3 | Level 4 | Level 5 | Level 6 | Description                                                |
| :---------------- | :------ | :------ | :------ | :------ | :------ | :------ | :--------------------------------------------------------- |
| Base Health       | +60     | +110    | +180    | +250    | +320    | +400    | Increases the base amount of your armor's health.          |
| Health Power      | +3%     | +6%     | +9%     | +12%    | +15%    | +18%    | Adds a percentage of your standard health to the armor.    |
| Base Armour       | +50     | +100    | +150    | +200    | +300    | +400    | Increases the base amount of your armor's armor value.     |
| Armour Strength   | +3%     | +6%     | +9%     | +12%    | +15%    | +18%    | Adds a percentage of your standard armor to the armor.     |
| Speed             | +1%     | +2%     | +3%     | +4%     | +5%     | +6%     | Makes you run faster.                                      |
| Fire Resistance   | +3%     | +6%     | +9%     | +12%    | +15%    | +18%    | Makes you resistant to fire damage.                        |
| Ice Resistance    | +3%     | +6%     | +9%     | +12%    | +15%    | +18%    | Makes you resistant to ice damage.                         |
| Absorption        | +1%     | +2%     | +3%     | +4%     | +5%     | +6%     | Absorbs a percentage of incoming damage.                   |

### 4.3. Synthesis Process

**Formula:** 3x Modifications of the same type and level N → 1x Modification of level N+1.

**Example:** 3x Level 2 Damage Modifications → 1x Level 3 Damage Modification.

## 5. Stash System

The stash is a persistent backpack for assets.

### 5.1. Core Mechanics

| Action         | Description                                        |
| :------------- | :------------------------------------------------- |
| Asset Pickup   | Use the "Stash" tool and left-click on an asset.   |
| Access         | Opened via a HUD icon.                             |
| Persistence    | Stash transfers across all connected servers.      |

### 5.2. Stash Capacity

| Capacity Tier | Total Slots       | Method of Unlock                       |
| :------------ | :---------------- | :------------------------------------- |
| Default       | [20 SLOTS]        | Standard for all new players.          |
| Maximum       | 80 Slots (4 pages)| Upgraded via the premium store.        |

## 6. Marketplace System

The Marketplace is the main interface for buying assets with in-game currency.

### 6.1. Asset Categories

| Category          | Examples                            | Role Requirement |
| :---------------- | :---------------------------------- | :--------------- |
| Ammunition        | Pistol Ammo, Rifle Ammo             | N/A              |
| Currency Generators | Ruby, Emerald, Diamond              | N/A              |
| Generator Add-ons | Boosters                            | N/A              |
| Blueprints        | Vehicle Blueprints, Weapon Blueprints | N/A              |
| Consumables       | Health Shipment, Armor Shipment     | N/A              |
| Boosts            | Speed Boost, Health Boost           | N/A              |
| Role-Specific     | Hacking Terminal                    | Hacker           |

## 7. Asset Classification

This section defines the rarity system that governs asset quality.

### 7.1. Asset Rarity

This hierarchy defines the quality of assets. Higher rarity assets will have better base stats or more modification slots.

| Rarity Tier | Color Code |
| :---------- | :--------- |
| Standard    | [Grey]     |
| Rare        | [Blue]     |
| Unique      | [Purple]   |
| Elite       | [Orange]   |
| Epic        | [Gold]     |
| Legendary   | [Red]      |

## 8. Premium Store

The Premium Store contains assets and boosts purchased with a premium currency, "credits," which are bought with real money.

### 8.1. Premium Credit Packages

| Credits | Price (£) |
| :------ | :-------- |
| 2,500   | £2.50     |
| 5,000   | £5.00     |
| 12,000  | £10.00    |
| 25,000  | £20.00    |
| 40,000  | £30.00    |

### 8.2. Premium Store Offerings

| Offering                | Cost (Credits) | Description                                                                |
| :---------------------- | :------------- | :------------------------------------------------------------------------- |
| V.I.P (1 Day)           | 290            | Grants owner access to restricted tools & VIP assets for 1 day.            |
| V.I.P (2 Weeks)         | 3,650          | Grants owner access to restricted tools & VIP assets for 2 weeks.          |
| XP Talisman (1 Day)     | 290            | Grants the owner 1 day of +50% XP gain upon activation.                    |
| XP Talisman (2 Weeks)   | 3,650          | Grants the owner 2 weeks of +50% XP gain upon activation.                  |
| Lucky Charm (2 Weeks)   | 2,100          | Grants the owner 2 weeks of extra luck, increasing crafting chances.       |
| Lucky Charm (4 Weeks)   | 3,460          | Grants the owner 4 weeks of extra luck, increasing crafting chances.       |
| Golden Discount (1 Week)| 1,800          | Grants the owner 1 week of 25% discount on all assets in the faction store. |
| Golden Discount (2 Weeks)| 3,460          | Grants the owner 2 weeks of 25% discount on all assets in the faction store.|
| Exclusive Contract (4 Weeks) | 1,000          | Grants the owner 4 weeks of immunity to demotion.                        |
| Steel Wallet (2 Weeks)  | 1,000          | Grants the owner 2 weeks of immunity to pickpocketing.                     |
| Storage Expansion       | 2,500          | Expands your storage space by +1 page. Maximum of +3 pages.                |
| Portfolio Expansion     | 2,850          | Grants you +50 stocks on the stock market. Maximum of +100.                |
| Builders Expansion      | 1,800          | Increases your prop limit by +15. Maximum of +30.                          |
| Spirit Extension        | 1,800          | Reduces respawn time by 25%. Maximum of -50%.                              |
| Crafters Handbook       | 3,600          | +5% Chance to craft primary weapons as sidearms. Maximum of +10%.          |
| Collector               | 3,940          | +50% Rare craft material drops. Maximum of 100%.                           |
| Forge Master            | 2,400          | Increases your maximum material forges by +1. Maximum +2.                  |
| Print Master            | 2,400          | Increases your maximum spawned currency generators by +1. Max stolen +2. Max of +2/+4. |
| Release Bind            | 1,550          | Releases the bind on an asset so it can be traded.                         |
| Reset Stone             | 1,820          | Removes the modifications from a weapon.                                   |
| Armor Reset Stone       | 1,820          | Removes the modifications from an armor piece.                             |
| Takedown Orb            | 1,820          | Reduces the level requirement of a weapon by 1.                            |
| Armor Takedown Orb      | 1,820          | Reduces the level requirement of an armor piece by 1.                      |
| Naming Tablet           | 1,200          | Gives a weapon a custom name. Used in a Gunsmith.                          |
| Custom Title            | 2,900          | Gives your character a custom title above their name.                      |

## 9. Trinket System

Trinkets are modifications placed into ring slots for passive bonuses. Rings can hold 0-2 slots.

### 9.1. Trinket Types & Effects

| Trinket Type         | Level 1 | Level 2 | Level 3 | Level 4 | Level 5 | Level 6 |
| :------------------- | :------ | :------ | :------ | :------ | :------ | :------ |
| Experience Boost     | +1%     | +2%     | +3%     | +4%     | +5%     | +6%     |
| Luck Boost           | +1%     | +2%     | +3%     | +4%     | +5%     | +6%     |
| Generator Yield Boost| +2%     | +4%     | +6%     | +8%     | +10%    | +12%    |
| Respawn Time Reduce  | -1%     | -2%     | -3%     | -4%     | -5%     | -6%     |
| Base Damage          | +1      | +1      | +2      | +2      | +3      | +4      |

## 10. Financial System

The financial system is a risk/reward mechanic for depositors and bankers.

### 10.1. Core Mechanics

| Role / Action | Description                                                                                    |
| :------------ | :--------------------------------------------------------------------------------------------- |
| Depositor     | Gives currency to a Banker to earn interest. Goal: Currency.                                   |
| Banker        | Facilitates deposits for customers. Goal: XP.                                                  |
| Bank Heist    | A thief can rob the bank. If successful, deposits are lost and the robber gets 50% of the total funds. |

### 10.2. Deposit Limits by Level

The maximum amount for a single deposit is based on player level.

| Level | Deposit Limit |
| :---- | :------------ |
| 1     | $2,525        |
| 2     | $5,050        |
| 3     | $7,575        |
| 4     | $10,101       |
| 5     | $12,626       |
| 6     | $15,151       |
| 7     | $17,676       |
| 8     | $20,202       |
| 9     | $22,727       |
| 10    | $25,525       |
| 11    | $27,777       |
| 12    | $30,303       |
| 13    | $32,828       |
| 14    | $35,353       |
| 15    | $37,878       |
| 16    | $40,404       |
| 17    | $42,929       |
| 18    | $45,454       |
| 19    | $47,979       |
| 20    | $50,505       |
| 21    | $53,030       |
| 22    | $55,555       |
| 23    | $58,080       |
| 24    | $60,606       |
| 25    | $63,131       |
| 26    | $65,656       |
| 27    | $68,181       |
| 28    | $70,707       |
| 29    | $73,232       |
| 30    | $75,757       |
| 31    | $78,282       |
| 32    | $80,808       |
| 33    | $83,333       |
| 34    | $85,858       |
| 35    | $88,383       |
| 36    | $90,909       |
| 37    | $93,434       |
| 38    | $95,959       |
| 39    | $98,484       |
| 40    | $101,010      |
| 41    | $103,535      |
| 42    | $106,060      |
| 43    | $108,585      |
| 44    | $111,111      |
| 45    | $113,636      |
| 46    | $116,161      |
| 47    | $118,686      |
| 48    | $121,212      |
| 49    | $123,737      |
| 50    | $126,262      |
| 51    | $128,878      |
| 52    | $131,313      |
| 53    | $133,838      |
| 54    | $136,363      |
| 55    | $138,888      |
| 56    | $141,414      |
| 57    | $143,939      |
| 58    | $146,464      |
| 59    | $148,989      |
| 60    | $151,515      |
| 61    | $154,040      |
| 62    | $156,565      |
| 63    | $159,090      |
| 64    | $161,616      |
| 65    | $164,141      |
| 66    | $166,666      |
| 67    | $169,191      |
| 68    | $171,717      |
| 69    | $174,242      |
| 70    | $176,767      |
| 71    | $179,292      |
| 72    | $181,818      |
| 73    | $184,343      |
| 74    | $186,868      |
| 75    | $189,939      |
| 76    | $191,919      |
| 77    | $194,444      |
| 78    | $196,969      |
| 79    | $199,494      |
| 80    | $202,020      |
| 81    | $204,545      |
| 82    | $207,070      |
| 83    | $209,595      |
| 84    | $212,121      |
| 85    | $214,646      |
| 86    | $217,171      |
| 87    | $219,696      |
| 88    | $224,747      |
| 89    | $226,010      |
| 90    | $227,272      |
| 91    | $229,797      |
| 92    | $232,323      |
| 93    | $234,848      |
| 94    | $237,373      |
| 95    | $239,898      |
| 96    | $242,424      |
| 97    | $244,949      |
| 98    | $247,474      |
| 99    | $250,000      |
