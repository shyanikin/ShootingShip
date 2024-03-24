# файл у уроку 3.5.2.
# проверка столкновения, пули врага с игроком, игрока с врагом и пули игрока с врагом

from initialization import levelsGame, screenGame

def check_collide(hit_player_bullet = None, hit_player = None, hit_enemies = None, screen_height = None, score = None, player = None, boss_level = None, boss = None):
    if hit_player_bullet:

        for hit in hit_player_bullet:
            if hit or hit.rect.y > screen_height:
                hit.kill()
        levelsGame.live_player -= 1
        screenGame.change_caption(score, levelsGame.live_player)

    if hit_player:
        levelsGame.live_player -= 1
        screenGame.change_caption(score,
                                    levelsGame.live_player,
                                    levelsGame.level_game)
        for hit in hit_player:
            hit.change_x *= -1
            hit.change_y *= -1
            player.change_x *= -1
            player.change_y *= -1


               