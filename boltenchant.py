import requests
import json

# Gets price of item from GE using the item id
def getPrice(id):
	# Get json returned from following url with item id concatenated into the url
	response = requests.get("http://services.runescape.com/m=itemdb_oldschool/api/graph/" + str(id) + ".json");
	# Use json library to load json into a json object (which happens to be a dict)
	# Content needs to be decoded because json returned from url is in byte format
	jsondict = json.loads(response.content.decode('UTF-8'))
	array = []

	# The dict contains 2 keys, daily and average. We want the numbers form daily.
	# Daily contains another dict with all the raw data
	# The data is simply in the form of 'time' : price
	# We want the price from the latest time so we add all the times to an array in order to get the latest time later.
	for key, value in jsondict.items():
		for key2, value2 in value.items():
			array.append(key2)

	# Sort times then get the price from the latest time which is the last (-1th) item in array
	array.sort()
	return jsondict['daily'][str(array[-1])]

sapphireBoltsId = 9337
sapphireBoltsPrice = getPrice(sapphireBoltsId)
sapphireBoltsePrice = getPrice(9240)

emeraldBoltsId = 9338
emeraldBoltsPrice = getPrice(emeraldBoltsId)
emeraldBoltsePrice = getPrice(9241)

topazBoltsId = 9336
topazBoltsPrice = getPrice(topazBoltsId)
topazBoltsePrice = getPrice(9239)

rubyBoltsId = 9339
rubyBoltsPrice = getPrice(rubyBoltsId)
rubyBoltsePrice = getPrice(9242)

diamondBoltsId = 9340
diamondBoltsPrice = getPrice(diamondBoltsId)
diamondBoltsePrice = getPrice(9243)

dragonBoltsId = 9341
dragonBoltsPrice = getPrice(dragonBoltsId)
dragonBoltsePrice = getPrice(9244)

onyxBoltsId = 9342
onyxBoltsPrice = getPrice(onyxBoltsId)
onyxBoltsePrice = getPrice(9245)

mindRunePrice = getPrice(558)

cosmicRuneId = 564
cosmicRunePrice = getPrice(cosmicRuneId)

natureRuneId = 561
natureRunePrice = getPrice(natureRuneId)

bloodRuneId = 565
bloodRunePrice = getPrice(bloodRuneId)

lawRuneId = 563
lawRunePrice = getPrice(lawRuneId)

soulRuneId = 566
soulRunePrice = getPrice(soulRuneId)

deathRuneId = 560
deathRunePrice = getPrice(deathRuneId)

enchantSapphireRunes = mindRunePrice + cosmicRunePrice
enchantEmeraldRunes = natureRunePrice + cosmicRunePrice
enchantTopazRunes = cosmicRunePrice
enchantRubyRunes = bloodRunePrice + cosmicRunePrice
enchantDiamondRunes = lawRunePrice + lawRunePrice + cosmicRunePrice
enchantDragonRunes = soulRunePrice + cosmicRunePrice
enchantOnyxRunes = deathRunePrice + cosmicRunePrice


print("10 Sapphire Bolts price: " + str(10*sapphireBoltsPrice))
print("Cost of runes to enchant: " + str(enchantSapphireRunes))
print("10 Sapphire Bolts (e) price: " + str(10*sapphireBoltsePrice))
print("cost/profit: " + str((10*sapphireBoltsePrice) - (10*sapphireBoltsPrice + enchantSapphireRunes)))
print()

print("10 Emerald Bolts price: " + str(10*emeraldBoltsPrice))
print("Cost of runes to enchant: " + str(enchantEmeraldRunes))
print("10 Emerald Bolts (e) price: " + str(10*emeraldBoltsePrice))
print("cost/profit: " + str((10*emeraldBoltsePrice) - (10*emeraldBoltsPrice + enchantEmeraldRunes)))
print()

print("10 Topaz Bolts price: " + str(10*topazBoltsPrice))
print("Cost of runes to enchant: " + str(enchantTopazRunes))
print("10 Topaz Bolts (e) price: " + str(10*topazBoltsePrice))
print("cost/profit: " + str((10*topazBoltsePrice) - (10*topazBoltsPrice + enchantTopazRunes)))
print()

print("10 Ruby Bolts price: " + str(10*rubyBoltsPrice))
print("Cost of runes to enchant: " + str(enchantRubyRunes))
print("10 Ruby Bolts (e) price: " + str(10*rubyBoltsePrice))
print("cost/profit: " + str((10*rubyBoltsePrice) - (10*rubyBoltsPrice + enchantRubyRunes)))
print()

print("10 Diamond Bolts price: " + str(10*diamondBoltsPrice))
print("Cost of runes to enchant: " + str(enchantDiamondRunes))
print("10 Diamond Bolts (e) price: " + str(10*diamondBoltsePrice))
print("cost/profit: " + str((10*diamondBoltsePrice) - (10*diamondBoltsPrice + enchantDiamondRunes)))
print()

print("10 Dragon Bolts price: " + str(10*dragonBoltsPrice))
print("Cost of runes to enchant: " + str(enchantDragonRunes))
print("10 Dragon Bolts (e) price: " + str(10*dragonBoltsePrice))
print("cost/profit: " + str((10*dragonBoltsePrice) - (10*dragonBoltsPrice + enchantDragonRunes)))
print()

print("10 Onyx Bolts price: " + str(10*onyxBoltsPrice))
print("Cost of runes to enchant: " + str(enchantOnyxRunes))
print("10 Onyx Bolts (e) price: " + str(10*onyxBoltsePrice))
print("cost/profit: " + str((10*onyxBoltsePrice) - (10*onyxBoltsPrice + enchantOnyxRunes)))
print()