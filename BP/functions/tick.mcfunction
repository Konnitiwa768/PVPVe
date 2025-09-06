# プレイヤーが豆腐生成機を所持していたらタイマーセット
execute as @a[hasitem={item=vsconw:tofu_generator, location=inventory},scores={tofu_timer=..0}] run scoreboard players set @s tofu_timer 1200

# タイマー減少
execute as @a[scores={tofu_timer=1..}] run scoreboard players remove @s tofu_timer 1

# タイマーが0のプレイヤーに豆腐を与える
execute as @a[scores={tofu_timer=0}] at @s run give @s vsconw:tofu
execute as @a[scores={tofu_timer=0}] run scoreboard players set @s tofu_timer 1200
