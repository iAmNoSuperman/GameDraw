from lvl_and_exp import PlayerStats
from lvl_and_exp import ActivitiesAndStore


# player = PlayerStats(1, 0, 0)


# For daily quests: asks if a daily quest has been completed, returns the exp for it
def get_exp_for_completed_daily(random_daily):
    result = input("Выполнили ежедневное задание? (yes / no): ")
    if result != "yes":
        return 0
    return int(random_daily[1])


# For serious works: asks if it was a complete work, not an etude, returns the chosen materials exp
def get_exp_for_completed_challenge(chosen_material):
    additional_question = input("Это полноценная работа? yes/no: ")
    if additional_question == "yes":
        return int(chosen_material[3])
    elif additional_question == "no":
        return int(chosen_material[2])
    else:
        return 0


# Opens the store csv data file,extracting coins from player wallet if anything chosen
def open_store(player_data):
    choice = input("Хотите открыть магазин (yes/no): ")
    if choice != "yes":
        return 0
    store = ActivitiesAndStore()
    store.load_csv("Награда", "store.csv")
    store_list = store.choose("Награда")
    player_data.coins_spent(int(store_list[1]))
    return 0


def main():
    # Load a current saved players data OR reate a new player if there are none to load
    player = PlayerStats.load_data()

    # To reset and manually add exp to player data run these:
    # player.reset_data()
    # player.lvl_up(85)

    # Get a random daily quest, complete it and confirm the result to claim the points!
    daily_quest_data = ActivitiesAndStore()
    daily_quest_data.load_csv("Квест", "daily_quest.csv")
    random_daily = daily_quest_data.get_random_row("Квест")
    print(random_daily[0])
    player.lvl_up(get_exp_for_completed_daily(random_daily))

    # comment to demonstrate git branches

    # Get a list of all major activities, choose one challenge and check if it was completed
    all_activities_data = ActivitiesAndStore()
    all_activities_data.load_csv("Материал", "activities_data.csv")
    chosen_challenge = all_activities_data.choose("Материал")
    if chosen_challenge:
        player.lvl_up(get_exp_for_completed_challenge(chosen_challenge))

    # The store function that provide the function with a player data to extract coins
    open_store(player)

    # TEST playground
    # To lvl up a player manualy run this:
    # player.lvl_up(55)
    # player.coins_added(100)
    # player.coins_spent(60)
    # It is possible to call challenge.choose table with a field index. In this case it will return the indexed field
    # chosen_challenge = all_activities_data.choose("Материал", field_index=3)

    # Printing and saving the result
    print(f"Данные игрока      ->  Уровень: {player.current_lvl},\n "
          f"                       Опыта: {player.exp_gained},\n "
          f"                       Монет: {player.coins},\n "
          f"                       Титул: {player.title}")

    player.save_data()



if __name__ == "__main__":
    main()


# TODO
# 1. Create a player class with lvl, exp and coins                              - DONE
# 2. Create a table of daily and special activities                             - DONE
# 3. Create a system of calculating the exp gained for completed activities     - DONE
# 4. Add additional bonuses - achievements, special bonuses                     - DONE
# 5. Create a store with prizes for coins.                                      - DONE
# 6. Make a clickable store with coins spending system                          - DONE
# 7. Link it to a git repository                                                - DONE
# 8. Add some UI to all these beautiful code!                                   -
# 9. Brush it up to one language                                                -
