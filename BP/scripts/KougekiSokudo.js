import { world, system } from "@minecraft/server";

// 武器ごとのクールダウン設定（秒 → tick単位）
const weaponCooldowns = {
  "vsconw:blacksteel_greatblade": 20, // 1秒（20tick）
  // 例: "yourpack:super_fast_dagger": 5, // 0.25秒
};

const cooldownMap = new Map();

world.beforeEvents.entityHit.subscribe(event => {
  const attacker = event.damagingEntity;
  if (!attacker || !attacker.hasComponent("equippable")) return;

  const item = attacker.getComponent("equippable").getEquipment("mainhand");
  if (!item) return;

  const weaponId = item.typeId;
  const cooldownTicks = weaponCooldowns[weaponId];

  if (!cooldownTicks) return; // 管理外の武器なら無視

  const attackerId = attacker.id;
  const lastUsedTick = cooldownMap.get(attackerId + weaponId) ?? -999;
  const currentTick = system.currentTick;

  if (currentTick - lastUsedTick < cooldownTicks) {
    // クールダウン中：ダメージ無効
    event.cancel = true;
    return;
  }

  // 攻撃記録更新
  cooldownMap.set(attackerId + weaponId, currentTick);
});
