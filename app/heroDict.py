

# key: nameSafe of hero
# value: List where
# 0 is list of pvp runes,
# 1 is Primary stat,
# 2 is Secondary stat,
# 3 is Notes
# 4 is PVP Tier
# 5 is info
# 6 is list pve runes,
# 7 is Primary stat (pve)
# 8 is Secondary stat (pve)
# 9 is Notes (pve)


heroDict = {
        "akwa": [["vitality", "runeSwift", "damage", "precise", "rage"], "APS, ATK, Crit DMG", "Attack Range", "Base of 200, whatever is required to stay behind your front line tanks", "A", "Akwa is kind of a niche hero. Her buff is water attack speed, so she’s usually paired up with either Atlantus or a freeze group with heroes such as Frost Queen, Namida, Snowman, and Pirato. She has decent enough HP and Def to survive in the front line, as long as she is not the very front. She also does decent damage. Her sp2 has pushback, which can slow down the dps of backline heroes. "],
        "alda": [["damage", "runeSwift", "precise", "rage"], "ATK, APS, Crit DMG", "Attack Range", "Needs 35.2% attack range to get to 750 range", "S", "Alda is one of the Crit Sisters. She and Valkyrie are able to give Crit buffs to everyone and are fondly known as the Crit Sisters. This makes her very good in both the Slay Event and PVP. Alda is not in any Crusher Chests, which makes her difficult to obtain."],
        "angelica": [[], "Nothing specific", "Nothing specific", "-", "-", "The lackluster Legendary. At 3 star Angelica is useful in the Guild Slay Event because her Ultimate doubles the attack of your team. It also applies a shield, which may help too. She has the lowest dps in the game, which basically makes her useless in PVP. She can resurrect fallen heroes, but it’s not enough to add her to your Arena team. Since her only real use is her ultimate in the Slay Event, give her weapon level 3 with Intelligent, and be done with her.", ["intelligent"], "Nothing specific", "Nothing specific", "-"],
        "arcana": [["stunning"], "Nothing specific", "Nothing specific", "-", "C", "Arcana is a mediocre rare hero. Crit buffers are nice for the Guild Slay Event and blitz, but since she only buffs Light heroes, it doesn’t translate over to Arena unless you are starting with Spike. Light doesn’t have enough dps heroes to justify using a Light only Crit buffer for Arena."],
        "atlantus": [["vitality", "damage", "runeSwift", "precise"], "AoE, ATK, APS, Crit DMG", "Attack Range", "70-150% AoE. Base Range of 220, get whatever is required to stay behind your front line tanks", "A", "Atlantus is a front line AoE smasher with great damage potential. He is immune to stun, which is very useful with all the Monki King’s flying around in Diamond and Legendary. He has his own Crusher Chest, which means you can increase his stars fairly easily.", ["runeSwift", "precise", "frenzy"], "Crit DMG, APS", "Nothing specific", "Slay Boss event"],
        "bat": [["damage", "runeSwift", "precise", "rage"], "ATK, Crit DMG, APS", "Nothing specific", "-", "C", "Bat was the best common that is not a tank until Dragon Bot was released. Bat is a very good choice for your 4th common to get to 7. Bat has very good dps for a common, but as a 4th hero, he may not make it to your arena team. He will still be very useful in GW and Blitz."],
        "blackBeard": [["vitality"], "HP", "Nothing specific", "-", "C", "Below average HP for a Knight. He’s mostly used as a Tank for Blitz."],
        "bunGun": [["runeSwift", "stunning", "dazed"], "APS, AoE, Stun duration", "Attack Range", "Needs 78.5% attack range to get to 750 range", "A", "Bungun has a lot of potential. Her problem is that she is an event hero, and therefore very difficult to get to high stars. You can use her at low as a crowd control hero. She does AoE, so she can crowd control the front line. Her other downfall is that she doesn’t have a whole lot of base attack range, so she can be difficult to keep alive."],
        "chaos": [["vitality", "damage", "runeSwift", "precise", "rage"], "APS, ATK, Crit DMG, AoE", "Attack Range", "Base range of 220, whatever is required to stay behind your front line tanks", "B", "Chaos is the front line killer. His sp2 is a small aoe that can be devastating to a front line group. Once people start using fewer front line heroes, his usefulness decreases, as his 1v1 damage isn’t as good. The all dark teams love this guy, as there are not a lot of choices for dark tanks outside of Ornok. Most people use him as the front line DPS. You’ll need the vitality set for survival on the front line. Then your choice of Damage, Precise, Swift, and Rage."],
        "circe": [["vitality"], "Nothing specific", "Nothing specific", "Doesn’t need any runes to be effective. Vitality can be used for survivability", "C", "Circe is a Halloween event hero, who can be very annoying to fight. She possesses opponent heroes to fight for her. These heroes cannot use their sp2 for her, just their sp1, but once she starts possessing your main hero, it can be devastating. There is a lot of RNG on how well she will help a team in any given battle. Early on she’s great to add to any team, but later on she becomes less useful. "],
        "clawdette": [["vitality", "damage", "runeSwift"], "APS, Crit DMG, ATK", "Attack Range", "Base range of 160, whatever is required to stay behind your front line tanks", "B", "Clawdette is mostly used for her 20% trophy bonus in blitz. As a brawler, her damage increases with her combo. This increases both her raw damage and her poison damage. Her poison damage is nice because it bypasses Def, and most End Game tanks have a lot of Def. Her team buff also buffs poison which further helps her poison, but is also great when paired with Thorn, for his poison damage."],
        "darkHunter": [["damage", "runeSwift", "precise", "rage"], "APS, ATK, Crit DMG", "Attack Range", "Needs 27,1% to get 750 range", "S", "Dark Hunter is one of the best PVP heroes in the game and is extremely easy to add to any team. His team buff decreases the opponent’s attack, which is pretty much required to keep your tanks alive. He has the best atk and raw dps of any ranger, and of any back line dps. He has the second highest base Attack Range, which means he is very easy to keep alive. He also has 25% base crit rate, which is one of the highest in the game."],
        "darkKnight": [["vitality"], "HP", "Movement speed", "-", "-", "Dark Knight is mostly used as a blitz tank. In blitz, all you really need is the vitality set. All dark teams can pull him off as a tank with Vitality, Phalanx, and Nimble, with HP primaries."],
        "darkWolf": [["runeSwift", "stunning", "dazed"], "Nothing specific", "Nothing specific", "No runes are required, you just use him for his team buff.", "C", "Dark Wolf is a niche PVP hero. He is usually paired with Hikari or another movement speed buffer. Dark Wolf decreases opponent movement speed, and Hikari increases your team’s movement speed. These two heroes combined can keep the opponent’s team near their crystal. This nerfs any attack range buffs. It also allows your aoe to hit their crystal, and possibly defeat them without killing all their heroes. It’s somewhat of a trick tactic that you need to watch out for."],
        "dragonBot": [["damage", "runeSwift", "precise", "rage"], "APS, ATK, Crit DMG", "Nothing specific", "-", "B", "Dragon Bot is the best common that is not a tank. He is a very good choice for your 2nd or 3rd common to get to 7 stars. While Bat has more base dps, DB will usually out damage Bat since he is a gunner and therefore ignores 70% of def. DB also lowers the opponent’s front line hero atk, which is very important early game to keep your main tank alive."],
        "frostQueen": [["chilling", "splash"], "AoE, APS", "Attack Range", "Needs 44.2% to get to 750 range", "A", "Freeze Explode! Frost Queen has Freeze Explode, and this has huge potential. Once she reaches 4, all freezes, whether caused by her or another hero, will explode. Before 4, only freezes initiated by Frost Queen will explode. If you give her chilling, all initial freeze explosions can freeze and explode again. They cannot chain further than that. There are some really strong builds that freeze most of the opponents for most of the time. The problem is a team built around freeze explode requires a lot of good runes."],
        "furiosa": [["vitality", "phalanx", "nimble"], "HP", "Movement speed", "Avoid attack range", "B", "Furiosa is the best hero for slay event. She’s immune to freeze which is handy against Frost Queen teams, so she has a place in PvP. If you want to be a strong Slay Event hitter, use Swift, Precise, and Frenzy with attack speed primaries. For PVP, she’s mostly used as a tank, so use Vitality, Phalanx, and Nimble, with HP primaries.", ["runeSwift", "precise", "frenzy"], "Crit DMG, APS", "Nothing specific", "Slay Boss event"],
        "gladiator": [["vitality", "guard", "nimble"], "HP", "Movement speed, Def", "Avoid attack range", "A", "The main f2p tank of the current meta, Gladiator has a ton of HP. He also has a significant amount of def. Leaf Blade, Ornok, and Paladin are the only tanks ranked higher. Once you get 1 or 2 commons to 7, it is time to start using Magic Medals on Gladiator. While you can technically use Gladiator as a front line AOE smasher, almost everyone uses him as a Pure Tank."],
        "goddess": [[], "Nothing specific", "Nothing specific", "-", "-", "Goddess is nice because her sp2 has push back, which helps early game and in blitz. She doesn’t need runes, but chilling can give her tidal wave a chance to freeze each hero it hits. She is also useful in the Guild Slay Event, as her Ultimate is a shield that is very helpful to keep heroes alive. Don't spend materials on this hero.", ["helpfull", "intelligent"], "Nothing specific", "Nothing specific", "Slay Boss event"],
        "goldKnight": [["vitality"], "HP", "Movement speed", "-", "-", "Gold Knight can be a decent tank in Blitz. His team buff is movement speed, which is helpful for a mostly Light team in blitz. This can push back the opponent closer to their crystal, and allow aoe heroes like Spike and Siegfried to hit the crystal, if they have enough AOE. Other than blitz, there’s not much use for Gold Knight."],
        "greenFaery": [[], "Nothing specific", "Nothing specific", "-", "-", "Green Faery adds a protective shield to a random hero for her sp2. This guarantees at least one extra hit, and for the slay event, this can be useful for survivor builds, especially for the Nimble Knights build. It’s not that helpful in PVP. She’s not that good, one of the worst epics in the game.", ["helpfull", "intelligent"], "Nothing specific", "Nothing specific", "Slay Boss event"],
        "groovine": [["runeSwift", "precise", "damage"], "Nothing specific", "Nothing specific", "-", "C", "Groovine is a crusher with a relatively poor quality crusher chest. Her ultimate turns other elemental damage (other than fire) into earth damage. This is very useful against water bosses in the Guild Slay Event.", ["runeSwift", "precise", "frenzy"], "Crit DMG, APS", "Nothing specific", "Slay Boss event"],
        "hikari": [["frenzy"], "Nothing specific", "Nothing specific", "Frenzy for staging", "-", "Hikari is a niche PVP hero. He is usually paired with Dark Wolf. Dark Wolf decreases opponent movement speed, and Hikari increases your team’s movement speed. These two heroes combined can keep the opponent’s team near their crystal. This nerfs any attack range buffs. It also allows your aoe to hit their crystal, and possibly defeat them without killing all their heroes. It’s somewhat of a trick tactic that you need to watch out for. No runes are required, you just use him for his team buff."],
        "hooky": [[], "Nothing specific", "Nothing specific", "-", "C", "Don't spend materials on this hero. Hooky is a relatively new Blitz Hero. His damage isn’t that great. His team buff increase earth attack range, and not many people use a lot of earth heroes. In addition, you can get all your required attack range from runes. His sp2 pulls opponent heroes nearer, which can help, but doesn’t seem to be enough to use him."],
        "iceCube": [["vitality", "chilling", "runeSwift", "damage"], "HP", "Nothing specific", "-", "B", "Ice Cube has some potential, but is extremely difficult to get medals for. His team buff isn’t great, and having a good team buff is very important for high Tier PVP heroes."],
        "iceKnight": [["chilling", "frozen", "vitality", "phalanx"], "Nothing specific", "Nothing specific", "-", "C", "As an event hero, Ice Knight is somewhat difficult to unlock, and very difficult to get medals for. His team buff is increased freeze duration, and many freeze builds do not want that because they rely on freeze explode."],
        "jasmine": [[], "Nothing specific", "Nothing specific", "-", "C", "Jasmine has some use for buffing fire heroes Crit Damage. This is very important for the Guild Slay Event, as critical hits are where most of the damage comes from. It also helps with a fire team in Blitz. She’s also very fast, and can be used in staging.", ["precise", "runeSwift", "frenzy"], "Crit DMG, APS", "Nothing specific", "Slay Boss event"],
        "kage": [["vitality", "runeSwift"], "HP", "Nothing specific", "-", "A", "Kage is generally used for his HP debuff, which is useful in all aspects of the game. If you’re close to beating a new daily dungeon level, you can throw Kage in for some extra % done to the boss. He is essential for any hitter in Slay Boss event.", ["precise", "runeSwift", "frenzy"], "Crit DMG, APS", "Nothing specific", "Slay Boss event"],
        "kasai": [["vitality", "nimble", "precise"], "Nothing specific", "Nothing specific", "-", "C", "Kasai has the 4th highest base DPS, but one of the lowest base HP. His buff is Fire Atk, and most PVP teams prefer universal Atk Buffs."],
        "kasumi": [["vitality", "nimble", "runeSwift"], "HP", "Nothing specific", "-", "A", "Kasumi has an sp2 with teleport, which makes her very fast for staging, and the best Dark staging hero. She also debuffs opponent attack speed, which is useful in PVP. During the Female Rogue Arena week, she can be quite strong. Teleporting into the backline can be disrupting."],
        "krouki": [["damage", "runeSwift", "precise"], "APS, ATK, Crit DMG", "Attack Range", "-", "C", "Krouki has some use for buffing earth heroes Crit Damage. This is very important for the Guild Slay Event, as critical hits are where most of the damage comes from."],
        "krunk": [["damage", "runeSwift", "precise"], "APS, ATK, Crit DMG", "Attack Range", "-", "C", "Krunk is tied for the third most HP in the game. This makes him a backline tank, which isn’t very useful. He does buff Light Atk, which is useful in Blitz. If you’re using Spike, it’s also useful in Arena and GW. He doesn’t need any runes for this buff though."],
        "leafBlade": [["vitality", "phalanx", "nimble"], "HP", "Movement speed, Def", "-", "S", "Leaf Blade is arguably the second best tank in the game. As a knight, he has a shield. But more importantly, he has an Auto-Shield ability, which makes him immune to damage after he falls below a certain %. It is possible to bypass this Auto-Shield if enough damage is applied to kill him, when he is above that %. When combined with Vlad, the Auto-Shield is long enough to mostly refill his health, which means you basically have to kill him twice."],
        "lightKnight": [["vitality", "nimble", "damage"], "Nothing specific", "Nothing specific", "-", "-", "Light Knight is a fast common, so he can be used for staging, but don't spend materials on this hero."],
        "luka": [[], "Nothing specific", "Nothing specific", "-", "-", "Luka is your first hero! He’s the best water hero for staging. Other than that he can sit comfortably on the bench and jump in as a filler in Blitz. Don't spend materials on this hero.", ["frenzy", "intelligent", "spoiling"], "Nothing specific", "Movement speed", "For staging"],
        "magmus": [["vitality", "damage", "runeSwift"], "HP", "Movement speed, Def", "-", "B", "Magmus is the best Fire Tank."],
        "mechaValken": [["vitality", "runeSwift", "precise", "rage"], "HP", "Movement speed, Def", "-", "C", "Mecha Valken is really good early on but he doesn’t scale as well as others. His team buff is Fire Def, which isn't very useful."],
        "merlinus": [["runeSwift", "vitality", "frenzy"], "HP, APS", "Nothing specific", "-", "C", "Merlinus starts strong, but finishes weak in PVP. He might fully heal an opponent tank in Gold or Platinum, and look amazing. But even early game there's almost always a better option in Arena, namely crowd control."],
        "misty": [["precise", "runeSwift", "rage"], "AoE, ATK, APS, Crit DMG", "Attack Range", "30-50% AoE. Needs 89.9% attack range to get to 750 range", "A", "Misty is a really good hero. She has the lowest base damage of any gunner, but she’s an AoE gunner, so she’ll hit multiple heroes, with a 30% chance to do poison. For her poison, her attack is applied once per second for 5 seconds. Her team buff is Earth Attack, which is great for an Earth team."],
        "mizu": [[], "Nothing specific", "Nothing specific", "-", "C", "Mizu is one of those heroes with an elemental attack buff and decent attack, but not enough survivability to be useful. Don't spend materials on this hero."],
        "monkiKing": [["runeSwift", "splash", "dazed"], "AoE, APS, Stun duration", "Attack Range", "50+% AoE and at least 20% higher than attack range. 30+% attack range.", "A", "Monki King is the best Fire stager as he has one of the fastest movement speeds of any Fire hero. He’s also the best Early to Late game Crowd Control hero, so he’s very useful in PVP. His sp2 is an aoe that has a high chance to stun."],
        "monkiMortar": [["damage", "runeSwift", "precise"], "AoE 30-50%, ATK, APS, Crit DMG", "Attack Range", "Needs 85.2% attack range to get to 750 range", "A", "Monki Mortar buffs Dark Attack making him a great hero due to the amount of viable Dark heroes."],
        "monkiRoboti": [["vitality", "runeSwift", "damage", "nimble"], "HP", "Nothing specific", "-", "A", "Monki Robot is a unique hero as you can only get medals for him from the Lucky Spin Chests. He has a universal attack buff, which is very good. He doesn’t have the base dps of some of the other brawlers, but has more HP than those, so he has decent survivability."],
        "namida": [["runeSwift", "chilling", "stunning"], "APS, AoE", "Attack Range", "-", "S", "Namida has great crowd control. Her sp2 attacks 3 back line heroes and slows them. She is also an AoE gunner, so she attacks the whole front line. Chilling can be added to her to crowd control both the front line and back line. She also debuffs opponents Water damage, which is quite useful against some freeze builds and teams with Water heroes. She also flies, making it quite difficult to kill her without going through the tanks first."],
        "necromancer": [["stunning", "runeSwift", "damage"], "Nothing specific", "Nothing specific", "-", "-", "Necromancer is a really cool hero that just doesn’t perform. He spawns Skeleton heroes. He has been tweaked since he came out, and he's yet to buffed enough to be good. Don’t spend materials on this hero."],
        "neko": [[], "Nothing specific", "Nothing specific", "-", "C", "Neko has the highest base dps of any hero, and highest damage potential with her brawler combo. She buffs Dark movement speed, which is useful in some primarily Dark builds. Don’t spend materials on this hero."],
        "oneEye": [["nimble", "precise", "runeSwift"], "APS, ATK, Crit DMG", "Attack Range", "Base of 120, whatever is required to stay behind your front line tanks", "B", "One Eye is a niche hero. He buffs Light attack speed, so he’s used in primarily Light teams. As a crusher, he does great damage to Gun Lord. He has decent HP for a non-tank class, so if he can get behind a tank, he will have decent survivability.", ["runeSwift", "precise", "frenzy"], "Crit DMG, APS", "Nothing specific", "Slay Boss event"],
        "onyx": [["vitality", "splash", "precise", "runeSwift"], "AoE, HP, ATK, APS, Crit DMG", "Attack Range", "Enough range to stay behind your front line tanks", "A", "Onyx is a great hero and a lot of teams use her in the end game as she has a great buff, and forces opponents to have attack range on all their backline heroes. Onyx doesn’t need runes early on, as she will die quickly no matter what runes you give her. Once she has caught up in stars you can give her runes so she can contribute. It’s probably best to give her HP primaries early on, again for survivability. Later on AoE, Atk, Atk Speed, and Crit Damage can all be used to prove her with more dps, but you may still want some HP primaries too."],
        "ornok": [["vitality", "guard", "nimble"], "HP", "Movement speed, Def", "Avoid attack range", "S", "Ornok is arguably the best tank in the game. He’s about 6th in baseline health if you combine health and his knight shield, and second in defense. Paladin is the only hero that beats Ornok in both stats. Where Ornok trumps Paladin is the elemental weakness. The downside with Ornok is that he is extremely difficult to obtain at high stars."],
        "paladin": [["vitality", "guard", "nimble"], "HP", "Movement speed, Def", "Avoid attack range", "S", "Paladin is one of the best tanks out there. He has great survivability between his HP, knight shield, Def, and healing sp2. His weakness is the elemental weakness to Dark."],
        "petunia": [["runeSwift", "stunning", "dazed"], "Nothing specific", "Nothing specific", "-", "B", "Petunia has a fun sp2 called Frogify, that turns opponents into Frogs. She can be added early on to help slow down the opponent’s attack but later on her crowd control doesn’t hold up to buffers and better crowd control heroes."],
        "pinky": [[], "Nothing specific", "Nothing specific", "-", "-", "Pinky is a fast Earth hero with a movement speed buff, so he is primarily used for staging. He’s the best Earth hero for staging. Other than that he only has use as a Blitz filler.", ["frenzy", "intelligent", "spoiling"], "Nothing specific", "Movement speed", "For staging"],
        "pirato": [["chilling", "stunning", "damage", "precise"], "AoE, APS, ATK, Crit DMG", "Attack Range", "30-50% AoE. Needs 83.8% attack range to get to 750 range", "B", "Pirato is a great hero that is out of the current meta. There are many Gladiator and Leaf Blade tanks out there resistant to Water. He can be found in some Freeze Explode builds, but generally isn’t used as much as he would be without the Earth tanks dominating the meta. He buffs Water Attack, so he can be paired with Atlantus."],
        "pumpKing": [["damage", "vitality", "poisonous", "nimble"], "AoE, ATK, APS, Crit DMG", "Attack Range", "Base of 220, whatever is required to stay behind your front line tanks", "B", "PumpKing is a Halloween event hero that has the largest AOE in the game with his sp2 at 440. He also buffs poison damage."],
        "ra": [["vitality", "nimble", "guard"], "HP", "Movement speed, Def", "Avoid attack range", "C", "Râ's first form has a sand pushback, which is useful for early game Arena. Once his first form is defeated he becomes a mummy that has a lot of HP. It’s a fun mechanic, but not a very useful one."],
        "robinHood": [["damage", "runeSwift", "precise"], "APS, ATK, Crit DMG", "Attack Range", "-", "C", "Robin Hood has some use for buffing earth heroes Crit Damage. This is very important for the Guild Slay Event, as critical hits are where most of the damage comes from. It also helps with an earth team in PVP."],
        "rufus": [["damage", "runeSwift"], "APS, ATK, Crit DMG", "Attack Range", "-", "C", "Rufus, the only hero that is in two Crusher Chests. If you buy Crusher Chests, he will be one of your first rare 7 heroes. He buffs Water Def, which is nearly worthless. He has decent attack for a 1v1 gunner, but he has low attack range, so it’s difficult to keep him alive."],
        "scud": [["damage", "runeSwift", "precise"], "AoE, APS, ATK, Crit DMG", "Attack Range", "30-50% AoE. Needs 87.5% attack range to get to 750", "S", "Scud is one of the best hero you can get from request from Epic Sunday. Scud buffs the entire teams Atk, which is extremely useful. As a gunner, Scud will bypass some of the opponent’s Def, which allows him to do great damage. In addition his attacks do AoE damage, so he can hit the entire front line, and with some AoE runes, some of the medium ranged heroes, like Monki King. In the Legendary Arena Leagues he can be found on almost every team."],
        "serShu": [["vitality", "runeSwift", "dazed", "precise"], "AoE, APS, Stun duration", "Attack Range", "50+% AoE, must be at least as high as attack range. 25+% attack range", "A", "Ser Shȗ is basically Monki King, but on the ground. Flying is one of the best aspects to Monki King, as it helps with survivability. Ser Shû does have more base HP, which helps, but it means she will need higher stars for survival. She buffs Lancer Attack range, which can help Monki King, Onyx, and Atlantus."],
        "siegfried": [["vitality", "damage", "nimble", "splash"], "AoE, HP, ATK, APS", "Attack Range", "AoE 90-150%. Base of 200 range, get whatever is required to stay behind your front line tanks", "A", "While Siegfried is out of the current meta, he can still do significant AoE damage with his sp2. There are so many good Dark dps heroes, and this makes it risky to run Siegfried. If he’s in the front, he will melt against many Late game teams. Siegfried is also a decent early game tank built for survival."],
        "skeletonGiant": [["vitality", "damage", "nimble", "splash"], "AoE, HP, ATK, APS", "Nothing specific", "70-150% AoE.", "B", "Arguably one of the best starting heroes in the game. SG is very useful in all PvP aspects until late game. As a common, it is easy to get SG to 7 and because of the exponential aspect of evolving and awakening, by focusing on SG, he can be your best hero very quickly, and hold this rank for months. He will be useful past the one year mark for most people. SG has enough HP to survive being on the front line, but he really shines with his damage. He has the highest damage and damage per second of any common tank. His sp2 is an AoE that can decimate entire teams."],
        "snowMan": [["chilling", "runeSwift", "vitality"], "APS", "Attack Range", "Needs 70.5% attack range to get to 750 range", "B", "Snowman is a fun hero that was introduced over Christmas of 2019. His sp2 rolls out a giant snowball that lowers opponent Def by 50%. This can be really good later on against heroes like Ornok, Paladin, and even Gladiator. If you attach chilling to him, he will then have a chance to freeze each of the heroes his snowball hits. He buffs Water attack, which is nice in the freeze build, and can help heroes like Atlantus. A fun quirk to snowman is the hero that kills him gets turned into a stationary snowman for a time. This can be useful early on when people are building teams around one front line AoE smasher."],
        "sorrow": [["damage", "runeSwift", "precise", "rage"], "APS, ATK, Crit DMG", "Attack Range", "Needs 21,0% to get 750 range", "A", "Sorrow buffs all gunner atk, which then buffs her own damage. Once she gets to 6 star, she will start doing great damage for your team. As a gunner, she ignores 70% of the opponent’s Def, which can be important. Her sp2 has a stun, while useful, it’s not nearly as important as the damage she does. Since her Crusher Chests are very good, it’s generally best if you buy more of these than other Crusher Chests.", ["runeSwift", "precise", "frenzy"], "Crit DMG, APS", "Nothing specific", "Slay Boss event"],
        "spark": [["damage", "runeSwift", "burning"], "APS, ATK, Burn Time", "Attack Range", "Needs 27.1% attack range to get to 750 range", "B", "Spark has a really fun sp2 that shoots across the screen. It only has a certain width, so it may not hit all the ground units, depending on how high Spark is standing relative to the opponent ground heroes. This gives him some RNG on how useful he is. Since he can hit a lot of heroes, it means Vlad will then be forced to heal multiple heroes, instead of focusing on healing the tank, which is nice. Spark’s team buff is a Fire damage debuff. This is extremely useful keeping Gladiator and Leaf Blade alive."],
        "spike": [["vitality", "damage", "splash", "runeSwift"], "AoE, HP, ATK, APS", "Movement speed, Def", "70-150% AoE. Can also be built as a tank with Vitality, Guard and Nimble", "B", "Spike is tied with Skeleton Giant as the best common hero in the game. SG wins out the best starter common because of his ties to other dark heroes, but Spike has great base stats and sp2 for a common. You can easily use Spike as your main starter common. If you do not choose Spike as your starter common, he is a very good 2nd or 3rd common to get to 7."],
        "sprout": [[], "Nothing specific", "Nothing specific", "-", "-", "Sprout can be useful as damage dealer against Frostwing. Generally not recommended to spend materials on this hero.", ["runeSwift", "precise", "frenzy"], "Crit DMG, APS", "Nothing specific", "Slay Boss event"],
        "spyro": [["vitality", "nimble"], "HP, APS", "Nothing specific", "-", "C", "Spyro is a lancer with low base HP, which makes it difficult for him to survive and be useful. He buffs Fire damage, so he can be useful for buffing Fire in Blitz and Guild War."],
        "swift": [["damage", "runeSwift", "precise"], "APS, ATK, Crit DMG", "Attack Range", "-", "-", "Blitz filler. Don’t spend materials on this hero."],
        "tellus": [["vitality", "nimble", "damage"], "HP", "Movement speed, Def", "-", "C", "Tellus is the tankiest of the brawlers. He has this Block Damage ability, that no one seems to understand the mechanics of. Not many people have spent enough materials on him to really test him out, so there’s a possibility of him being stronger than we think."],
        "tesla": [["runeSwift", "precise", "rage"], "APS, ATK, Crit DMG", "Attack Range", "Needs 92.3% attack range to get to 750 range", "S", "Tesla is the end game counter to Ornok. Her “Team” buff is a self buff that gives her massive amounts of attack. This allows her to focus on other sources of damage. Her normal attack has a chance to stun, and her sp2 is a small aoe stun. Most end game teams use few front line heroes, so this isn’t that important, but it can help take out late game teams. It does give a full dps team some crowd control."],
        "thor": [["vitality", "nimble", "damage"], "HP, ATK, APS", "Nothing specific", "-", "B", "Thor is an interesting hero that can be used with mostly Light teams as he buffs Light attack. His sp2 is Rush, that looks like a whirlwind that can send him behind the opponent’s front line. He has a decent amount of HP, so he can disrupt an opponent’s hero position."],
        "thorn": [["precise", "poisonous", "blight"], "APS, AoE", "Attack Range", " 90-150% AoE, about 100% from than attack range. Needs 50.0% attack range to get to 750 range", "S", "Thorn has the best AoE attack in the game. It has a range of 600, it attacks both ground and flying heroes, and it does a total of 6x damage. The downside is that it’s poison, and you can’t crit on poison damage. It’s not amazing damage, but it forces Vlad to heal other heroes other than the tank, and that is extremely valuable. As an Earth hero, he has a damage advantage over Water heroes, which is valuable taking out freeze teams and Namida in general."],
        "torch": [["damage", "runeSwift", "precise"], "APS, ATK, Crit DMG", "Attack Range", "-", "B", "Torch is a weird hero. He’s a back line class, but has the lowest attack range. If you want him to survive, you’d have to give him a whole lot of attack range."],
        "trickster": [["vitality", "runeSwift", "dazed", "precise"], "APS, Stun duration, HP", "Attack Range", "Needs 47.0% attack range to get to 750 range", "S", "Trickster has decent base dps, decent attack range, and some really interesting crowd control. Both his normal attack and sp2 tried to apply attack down, slow down, def down, and stun, the durations of which increase with stars. His team buff increases negative effects, increasing these durations even more."],
        "valkyrie": [["chilling", "runeSwift", "frenzy"], "APS, ATK, Crit DMG", "Attack Range", "Needs 36.4% attack range to get to 750 range", "S", "Valkyrie is one of the Crit Sisters. She and Alda are able to give Crit buffs to everyone and are fondly known as the Crit Sisters. This makes her very good in both the Slay Event and PVP. Valkyrie is not in any Crusher Chests, which makes her difficult to obtain and difficult to get high stars. Once she does get to 6, she can do decent damage, but she can help freeze at any stars. Water is weak to Earth, so she doesn’t do much damage against two commonly used earth tanks: Gladiator and Leaf Blade."],
        "vlad": [["damage", "runeSwift", "precise"], "APS, ATK, Crit DMG", "Nothing specific", "-", "S", "Vlad is one of the best PVP heroes in the game and is extremely easy to add to any team. His team buff decreases opponent attack speed, which helps keep your team alive and with fewer crowd controls. He also heals based on damage, which helps keep your heroes alive even more."],
        "wolfie": [["vitality", "damage", "resist", "nimble"], "HP", "Movement speed, Def", "-", "B", "Wolfie is a decent tank in an element full of great tanks. He buffs Earth attack which is useful in Blitz."],
        "xak": [["runeSwift", "damage", "dazed"], "AoE, APS, Stun duration", "Attack Range", "75+% AoE. Needs 78.6% attack range to get to 750", "A", "Xak is a really good Stun hero. His sp2 is a massive stunning AOE. He generally works well with Monki King, who will increase Xak’s attack speed, and therefore how often he uses his sp2. If you increase Xak’s attack range, he can stun the back line, which is important starting around Mid game, but can be useful early on to stun other crowd control. Xak also has a shield for an Ultimate, which is useful for survival in Guild Slay Event."],
        "manta": [["runeSwift", "chilling", "stunning"], "AoE, APS", "Attack Range", "Needs 82.9% to get to 750", "A", "Manta was just released in July 2020 as a Blitz hero. She decreases opponent AOE damage. I’m not 100% sure what this means, it either means anything with an AOE radius, or anything that can be buffed by AOE runes. These two definitions mostly overlap, but Frost Queen’s Freeze Explode is where they do not overlap, so I do not know if that is impacted or not. Heroes like Goddess, Ra, Akwa, and Spark are not affected by this debuff. This can be very useful against AOE smashers like Siegfried and Atlantus, and Late/End Game heroes with aoe, like Thorn, Tesla, and Scud. So Mantas primary use seem to be a late game debuffer. She's still a young hero and it seems the 50k flooz to make her 7-star is more than she's worth."],
        "tnt": [["damage", "precise", "rage", "runeSwift"], "AoE, APS, ATK, Crit DMG", "Attack Range", "Needs 56.3% to get to 750 range. Stack as much movement speed as possible.", "A", "TNT was released in July 2020 as a Blitz hero. He has a new team buff that increases the duration of burn. The most exciting aspect to TNT is his SP2. He summons a bomb that runs toward the opponent and explodes after 4s. Attack range makes this worse, as it starts the summon farther away from the opponent. In addition Kamikaze spawns a bit behind TNT, maybe 20 units. Movement speed, either from team buffs or runes is a must for this. Kamikaze has a base movement speed of 140, and 4 seconds only gets him 560 towards the opponent. At 750 range, this would barely hit the front hero. With just runes, you can get to 230 movement speed, which would allow the summon to move 922 in 4s. Even with AOE buffs, this might not be enough for Late Game. If you add Xak to the team, the summon could move 1480, and explode in the middle of the opponent’s team, hitting everyone. Xak alone will allow Kamikaze to move 1120. I see this as the most likely use of TNT, being paired up with Xak. He's still a young hero and it seems the 50k flooz to make him 7-star is more than he's worth."],
        "seraph": [["damage", "precise", "rage", "runeSwift"], "APS, ATK, Crit DMG", "Attack Range", "Needs 44.2% to get to 750 range.", "A", "Seraph was just introduced in October of 2020 as the newest Crusher. She buffs all ranger atk, which then buffs her own damage. Once she gets to 6, she will start doing great damage for your team. Her unique ability is to change her attack between Light and Dark depending on her target. Since her Crusher Chests are very good, it’s generally best if you buy more of these than other Crusher Chests"],
        "lycan": [["vitality", "nimble", "precise", "runeSwift"], "APS", "Attack Range", "Attack Range is required and HP is nice.", "A", "Lycan is being introduced for the Halloween 2020 event. As an epic, he’s going to be somewhat difficult to obtain, with a low chance of getting him from the chests. He’s going to be extremely good though, possibly the best hero in the game for PVP. While he has stats to do damage, the best use of him will be to apply wounded to the opponent tank."],
    }


"""
        "Hero nameSafe": [["pvp runes"], "Primary", "Secondary", "RUNE NOTES", "PVP TIER", "HERO INFO", ["pve runes"],"Primary", "Secondary", "RUNE NOTES"]
"""

kraken = {
        "Barbarian": 2,
        "Brawler": 2,
        "Gunner": 1,
        "Knight": 3,
        "Lancer": 1,
        "Magician": 1,
        "Ranger": 1,
        "Rogue": 1,
        "Samurai": 2,
        "Support": 1,
        "Fly": 0,
        "Water": 1,
        "Fire": 0.5,
        "Earth": 4,
        "Light": 1,
        "Dark": 1
}

deepseaking = {
        "Barbarian": 1,
        "Brawler": 2,
        "Gunner": 1,
        "Knight": 1,
        "Lancer": 5,
        "Magician": 1,
        "Ranger": 3,
        "Rogue": 1,
        "Samurai": 1,
        "Support": 1,
        "Fly": 0,
        "Water": 1,
        "Fire": 0.5,
        "Earth": 4,
        "Light": 1,
        "Dark": 1
}

frostwing = {
        "Barbarian": 1,
        "Brawler": 1,
        "Gunner": 2,
        "Knight": 1,
        "Lancer": 1,
        "Magician": 5,
        "Ranger": 2,
        "Rogue": 1,
        "Samurai": 1,
        "Support": 1,
        "Fly": 1,
        "Water": 1,
        "Fire": 0.5,
        "Earth": 4,
        "Light": 1,
        "Dark": 1
}

valkenbot = {
        "Barbarian": 1,
        "Brawler": 1,
        "Gunner": 5,
        "Knight": 1,
        "Lancer": 1,
        "Magician": 3,
        "Ranger": 1,
        "Rogue": 1,
        "Samurai": 1,
        "Support": 1,
        "Fly": 2,
        "Water": 4,
        "Fire": 1,
        "Earth": 0.5,
        "Light": 1,
        "Dark": 1
}

firegorge = {
        "Barbarian": 1,
        "Brawler": 1,
        "Gunner": 1,
        "Knight": 1,
        "Lancer": 1,
        "Magician": 1,
        "Ranger": 1,
        "Rogue": 3,
        "Samurai": 5,
        "Support": 1,
        "Fly": 1,
        "Water": 4,
        "Fire": 1,
        "Earth": 0.5,
        "Light": 1,
        "Dark": 1
}

madking = {
        "Barbarian": 1,
        "Brawler": 1,
        "Gunner": 2,
        "Knight": 1,
        "Lancer": 5,
        "Magician": 1,
        "Ranger": 2,
        "Rogue": 1,
        "Samurai": 1,
        "Support": 1,
        "Fly": 0,
        "Water": 4,
        "Fire": 1,
        "Earth": 0.5,
        "Light": 1,
        "Dark": 1
}

sandclaw = {
        "Barbarian": 1,
        "Brawler": 1,
        "Gunner": 1,
        "Knight": 2,
        "Lancer": 5,
        "Magician": 1,
        "Ranger": 1,
        "Rogue": 1,
        "Samurai": 3,
        "Support": 1,
        "Fly": 0,
        "Water": 0.5,
        "Fire": 4,
        "Earth": 1,
        "Light": 1,
        "Dark": 1
}

voodootank = {
        "Barbarian": 2,
        "Brawler": 5,
        "Gunner": 1,
        "Knight": 1,
        "Lancer": 1,
        "Magician": 1,
        "Ranger": 1,
        "Rogue": 3,
        "Samurai": 1,
        "Support": 1,
        "Fly": 0,
        "Water": 0.5,
        "Fire": 4,
        "Earth": 1,
        "Light": 1,
        "Dark": 1
}

undeadsamurai = {
        "Barbarian": 3,
        "Brawler": 1,
        "Gunner": 1,
        "Knight": 5,
        "Lancer": 1,
        "Magician": 1,
        "Ranger": 1,
        "Rogue": 1,
        "Samurai": 2,
        "Support": 1,
        "Fly": 0,
        "Water": 0.5,
        "Fire": 4,
        "Earth": 1,
        "Light": 1,
        "Dark": 1
}

odin = {
        "Barbarian": 1,
        "Brawler": 1,
        "Gunner": 3,
        "Knight": 1,
        "Lancer": 1,
        "Magician": 1,
        "Ranger": 5,
        "Rogue": 1,
        "Samurai": 1,
        "Support": 1,
        "Fly": 1,
        "Water": 1,
        "Fire": 1,
        "Earth": 1,
        "Light": 1,
        "Dark": 2
}

lightmech = {
        "Barbarian": 1,
        "Brawler": 3,
        "Gunner": 1,
        "Knight": 1,
        "Lancer": 1,
        "Magician": 5,
        "Ranger": 1,
        "Rogue": 1,
        "Samurai": 1,
        "Support": 1,
        "Fly": 1,
        "Water": 1,
        "Fire": 1,
        "Earth": 1,
        "Light": 1,
        "Dark": 2
}

astrolab = {
        "Barbarian": 1,
        "Brawler": 1,
        "Gunner": 5,
        "Knight": 1,
        "Lancer": 1,
        "Magician": 1,
        "Ranger": 2,
        "Rogue": 1,
        "Samurai": 1,
        "Support": 1,
        "Fly": 1,
        "Water": 1,
        "Fire": 1,
        "Earth": 1,
        "Light": 1,
        "Dark": 2
}

beetle = {
        "Barbarian": 1,
        "Brawler": 1,
        "Gunner": 1,
        "Knight": 1,
        "Lancer": 1,
        "Magician": 5,
        "Ranger": 3,
        "Rogue": 2,
        "Samurai": 1,
        "Support": 1,
        "Fly": 0,
        "Water": 1,
        "Fire": 1,
        "Earth": 1,
        "Light": 2,
        "Dark": 1
}

hauntinghead = {
        "Barbarian": 3,
        "Brawler": 1,
        "Gunner": 2,
        "Knight": 1,
        "Lancer": 1,
        "Magician": 1,
        "Ranger": 5,
        "Rogue": 1,
        "Samurai": 1,
        "Support": 1,
        "Fly": 0,
        "Water": 1,
        "Fire": 1,
        "Earth": 1,
        "Light": 2,
        "Dark": 1
}

gunlord = {
        "Barbarian": 1,
        "Brawler": 1,
        "Gunner": 1,
        "Knight": 1,
        "Lancer": 1,
        "Magician": 2,
        "Ranger": 1,
        "Rogue": 5,
        "Samurai": 3,
        "Support": 1,
        "Fly": 0,
        "Water": 1,
        "Fire": 1,
        "Earth": 1,
        "Light": 2,
        "Dark": 1
}

bosses = {
        "kraken": kraken,
        "deepseaking": deepseaking,
        "frostwing": frostwing,
        "valkenbot": valkenbot,
        "firegorge": firegorge,
        "madking": madking,
        "sandclaw": sandclaw,
        "voodootank": voodootank,
        "undeadsamurai": undeadsamurai,
        "odin": odin,
        "lightmech": lightmech,
        "astrolab": astrolab,
        "beetle": beetle,
        "hauntinghead": hauntinghead,
        "gunlord": gunlord
}
