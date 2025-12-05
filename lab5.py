class Candidate:
    def __init__(self, name, votes, region):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Ім'я кандидата має бути непорожнім рядком")
        if not isinstance(votes, int) or votes < 0:
            raise ValueError("Кількість голосів має бути невід'ємним цілим числом")
        if not isinstance(region, str) or not region.strip():
            raise ValueError("Region має бути непорожнім рядком")

        self.__name = name.strip()
        self.__votes = votes
        self.__region = region.strip()

    def __del__(self):
        if hasattr(self, "_Candidate__name") and hasattr(self, "_Candidate__votes"):
            print(f"Кандидат {self.__name} з {self.__votes} голосами був видалений.")

    def get_name(self):
        return self.__name

    def get_votes(self):
        return self.__votes

    def get_region(self):
        return self.__region

    def set_votes(self, new_votes):
        if isinstance(new_votes, int) and new_votes >= 0:
            self.__votes = new_votes
        else:
            raise ValueError("Кількість голосів має бути невід'ємним цілим числом")

    def display_stats(self, total_votes):
        percent = (self.__votes / total_votes) * 100 if total_votes > 0 else 0
        print(f"{self.__name} ({self.__region}): {self.__votes} голосів ({percent:.2f}%)")


class Election:
    def __init__(self):
        self.candidates = []

    def add_candidate(self, candidate):
        if not isinstance(candidate, Candidate):
            raise TypeError("Потрібен об'єкт типу Candidate")
        if candidate.get_votes() < 0:
            raise ValueError("Кандидат має невід'ємну кількість голосів")
        self.candidates.append(candidate)

    def total_votes(self):
        return sum(c.get_votes() for c in self.candidates)

    def show_all(self):
        total = self.total_votes()
        print("\nРезультати виборів:")
        for c in self.candidates:
            c.display_stats(total)

    def get_winner(self):
        if not self.candidates:
            return None
        winner = max(self.candidates, key=lambda c: c.get_votes())
        return winner.get_name()

    def average_votes_by_region(self, region_name):
        region_key = region_name.strip().lower()
        filtered_candidates = [c for c in self.candidates if c.get_region().lower() == region_key]
        if not filtered_candidates:
            return 0.0
        return sum(c.get_votes() for c in filtered_candidates) / len(filtered_candidates)


def main():
    election = Election()

    for i in range(5):
        print(f"\nКандидат №{i+1}")
        name = input("Введи ім'я кандидата: ").strip()
        while True:
            try:
                votes = int(input("Введи кількість голосів: "))
                if votes < 0:
                    raise ValueError
                break
            except ValueError:
                print("Голос не може бути від'ємним.")
        region = input("Введи регіон кандидата: ").strip()
        candidate = Candidate(name, votes, region)
        election.add_candidate(candidate)

    election.show_all()
    print(f"\nПереможець виборів: {election.get_winner()}")

    region_query = input("\nВведи назву регіону для середнього: ").strip()
    avg = election.average_votes_by_region(region_query)
    if avg == 0.0:
        print("Кандидатів у вказаному регіоні немає.")
    else:
        print(f"Середня кількість голосів у регіоні '{region_query}': {avg:.2f}")


if __name__ == "__main__":
    main()