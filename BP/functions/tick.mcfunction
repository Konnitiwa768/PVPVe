# プレイヤーが豆腐生成機を所持していたらタイマーセット
execute as @a[hasitem={item=vsconw:tofu_generator, location=inventory},scores={tofu_timer=..0}] run scoreboard players set @s tofu_timer 1200
execute as @e[hasitem={item=vsconw:poison_sword, location=inventory}] run effect @e [r=5] poison 10 5 true
execute as @e[hasitem={item=vsconw:ice_sword, location=inventory}] run effect @e [r=5] slowness 15 3 true
execute as @a[hasitem={item=vsconw:fire_sword, location=inventory}] at @s run execute as @e[r=3] at @s run setblock ~ ~-1 ~ minecraft:fire
execute as @a[hasitem={item=vsconw:lightning_sword, location=inventory}] at @s run execute as @e[r=5] at @s run summon minecraft:lightning_bolt ~ ~-1 ~
execute as @e[hasitem={item=vsconw:ancient_sword, location=inventory}] run effect [r=5] @e poison infinite 5 true

# タイマー減少
execute as @a[scores={tofu_timer=1..}] run scoreboard players remove @s tofu_timer 1

# タイマーが0のプレイヤーに豆腐を与える
execute as @a[scores={tofu_timer=0}] at @s run give @s vsconw:tofu
execute as @a[scores={tofu_timer=0}] run scoreboard players set @s tofu_timer 1200
