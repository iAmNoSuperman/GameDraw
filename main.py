from lvl_and_exp import PlayerStats, print_all_rows
from lvl_and_exp import ActivitiesAndStore


# player = PlayerStats(1, 0, 0)


def get_exp_for_completed_daily(random_daily):
    result = input("Have you finished the daily quest yet? (yes / no): ")
    if result != "yes":
        return 0
    return int(random_daily[1])


def main():
    # Load a current saved players data OR reate a new player if there are none to load
    player = PlayerStats.load_data()
    # player.reset_data()

    # Get a random daily quest, complete it and confirm the result to claim the points!
    daily_quest_data = ActivitiesAndStore()
    daily_quest = daily_quest_data.load_csv("Квест", "daily_quest.csv")
    random_daily = daily_quest_data.get_random_row("Квест")
    print(random_daily[0])
    player.lvl_up(get_exp_for_completed_daily(random_daily))

    # Get a list of all major activities and print them all
    all_activities_data = ActivitiesAndStore()
    all_activities_data.load_csv("Материал", "activities_data.csv")
    print_all_rows(all_activities_data.get_all_rows("Материал"))

    # A function that will get the task and calculate the exp gained for completing it
    # choosen_material = input("Выбери материал из списка: ")

    # TEST playground
    # player.lvl_up(25)
    print(f"Final state -> Level: {player.current_lvl}, Exp: {player.exp_gained}, Coins: {player.coins}, Титул: {player.title}")

    # Saving the resul
    player.save_data()


if __name__ == "__main__":
    main()


# TODO
# 1. Create a player class with lvl, exp and coins                              -DONE
# 2. Create a table of daily and special activities                             -DONE
# 3. Create a system of calculating the exp gained for completed activities     - daily - DONE, others are in progress
# 4. Add additional bonuses - achievements, special bonuses                     -DONE
# 5. Create a store with prizes for coins.                                      -DONE
# 6. Make a clickable store with coins spending system                          -
