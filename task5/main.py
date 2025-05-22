from builders.hero_builder import HeroBuilder
from builders.enemy_builder import EnemyBuilder
from directors.hero_director import HeroDirector
from directors.enemy_director import EnemyDirector

def main():
    hero_builder = HeroBuilder()
    hero_director = HeroDirector(hero_builder)
    hero = hero_director.construct()

    enemy_builder = EnemyBuilder()
    enemy_director = EnemyDirector(enemy_builder)
    enemy = enemy_director.construct()

    print("=== Герой ===")
    print(hero)
    print("=== Ворог ===")
    print(enemy)

if __name__ == "__main__":
    main()
