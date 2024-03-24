# файл к уроку 3.5.2
# создание пуль врагов

import random
from classes.Bullet import Bullet


def create_enemy_bullet(enemy, player, boss_level, shots, shot_true, bullets_enemy, all_sprites, boss):
    if (enemy.rect.x <= player.rect.x <= enemy.rect.topright[
                            0] or enemy.rect.x <= player.rect.topright[
                            0] <= enemy.rect.topright[0] or enemy.rect.x <= player.rect.centerx <= enemy.rect.topright[0]) and enemy.rect.centery < player.rect.centery:

        if not boss_level:
            if random.randint(1, shots.enemy_shot) == shot_true:
                enemy_bullet = Bullet(x = enemy.rect.centerx,
                                    y = enemy.rect.centery,
                                    width = 2,
                                    height = 10,
                                    color = (255, 255, 0),
                                    speed_y = 5)
            
                bullets_enemy.add(enemy_bullet)
                all_sprites.add(enemy_bullet)

        elif boss_level:
            if random.randint(1, shots.boss_shot) == shot_true:
                for key, value in boss.__dict__.items():
                    if 'weapon' in key:
                        enemy_bullet = Bullet(x = value[0],
                                            y = value[1],
                                            width = 2,
                                            height = 10,
                                            color = (255, 255, 0),
                                            speed_y = 10)

                        bullets_enemy.add(enemy_bullet)
                        all_sprites.add(enemy_bullet)

