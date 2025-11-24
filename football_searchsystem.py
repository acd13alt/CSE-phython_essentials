

# ---------------------------------------------
# FOOTBALL TOURNAMENT SEARCH SYSTEM
# FIFA WORLD CUP & UEFA CHAMPIONS LEAGUE WINNERS
# ---------------------------------------------

# FIFA World Cup Winners (1930–2022)
fifa_world_cup_winners = {1930: "Uruguay", 1934: "Italy", 1938: "Italy",
    1950: "Uruguay", 1954: "West Germany", 1958: "Brazil",
    1962: "Brazil", 1966: "England", 1970: "Brazil",
    1974: "West Germany", 1978: "Argentina", 1982: "Italy",
    1986: "Argentina", 1990: "West Germany", 1994: "Brazil",
    1998: "France", 2002: "Brazil", 2006: "Italy",
    2010: "Spain", 2014: "Germany", 2018: "France",
    2022: "Argentina"}

# UEFA Champions League Winners (2000–2024)
ucl_winners = {2000: "Real Madrid", 2001: "Bayern Munich", 2002: "Real Madrid",
    2003: "AC Milan", 2004: "Porto", 2005: "Liverpool",
    2006: "Barcelona", 2007: "AC Milan", 2008: "Manchester United",
    2009: "Barcelona", 2010: "Inter Milan", 2011: "Barcelona",
    2012: "Chelsea", 2013: "Bayern Munich", 2014: "Real Madrid",
    2015: "Barcelona", 2016: "Real Madrid", 2017: "Real Madrid",
    2018: "Real Madrid", 2019: "Liverpool", 2020: "Bayern Munich",
    2021: "Chelsea", 2022: "Real Madrid", 2023: "Manchester City",
    2024: "Real Madrid",2025:"Paris st. German"}

def search_fifa():
    year = int(input("\\nEnter a FIFA World Cup year (1930–2022): "))

    if year in fifa_world_cup_winners:
        print(f" FIFA World Cup {year} Winner: {fifa_world_cup_winners[year]}")
    else:
        print(" No World Cup held this year OR invalid input.")

def search_ucl():
    year = int(input("\\nEnter a UEFA Champions League year (2000–2024): "))

    if year in ucl_winners:
        print(f" UEFA Champions League {year} Winner: {ucl_winners[year]}")
    else:
        print("Invalid year — No UCL data available for this year.")

def main_menu():
    while True:
        print("\\n===============================")
        print("  FOOTBALL WINNERS SEARCH")
        print("===============================")
        print("1. Search FIFA World Cup Winner")
        print("2. Search UEFA Champions League Winner")
        print("3. View All FIFA Winners")
        print("4. View All UCL Winners")
        print("5. Exit")
        print("===============================")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            search_fifa()

        elif choice == "2":
            search_ucl()

        elif choice == "3":
            print("\\n ALL FIFA WORLD CUP WINNERS:")
            for year, team in fifa_world_cup_winners.items():
                print(f"{year}: {team}")

        elif choice == "4":
            print("\\n ALL UEFA CHAMPIONS LEAGUE WINNERS:")
            for year, team in ucl_winners.items():
                print(f"{year}: {team}")

        elif choice == "5":
            print("\\nThank you for using the Football Search System! ")
            break

        else:
            print(" Invalid option, try again!")

main_menu()

