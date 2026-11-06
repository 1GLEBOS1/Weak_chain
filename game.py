from os.path import sep


class Game:

    __players_scores__ = []
    __chain_length__: int
    __round__: int
    __saved_bank__: int

    def __init__(self) -> None:

        self.__chain_length__ = 0
        self.__round__ = 1
        self.__saved_bank__ = 0
        input_ = input()

        while input_ != "" and len(self.__players_scores__) <= 9:

            self.__players_scores__.append([f"{len(self.__players_scores__)+1}. "+input_, 0])
            if len(self.__players_scores__) <= 9:
                input_ = input()


    def game_loop(self):

        while self.__round__ <=8:
            flag = False
            s = f""
            for player in self.__players_scores__:
                s += f"{player[0]}: {player[1]}"
                s += "\n"
                pass
            print(s)
            inp = input()
            while inp != "раунд!":
                try:
                    action = inp.split(sep=" ")
                    if action[0].lower() == 'банк':
                        self.__save_bank__()
                    elif action[1] == '+':
                        self.__get_point__(player_num=int(action[0]))
                    elif action[1] == '-':
                        self.__lose_point__()

                except IndexError as e:
                    print(f"Неверный формат {e}")
                except ValueError as e:
                    print(f"Неверный формат {e}")
                inp = input()

            while not flag:
                flag = self.__kick_player__()
            self.__increase_round__()
        self.__final_duel__()

    def __increase_round__(self, ):
        self.__round__ += 1

    def __get_players_scores__(self):

        return self.__players_scores__

    def __get_chain_length__(self):

        return self.__chain_length__

    def __get_player__index__(self, player_num: int):
        output: int
        for player in self.__players_scores__:
            current_player_num = player[0].split(sep=".")[0]
            if str(player_num) == current_player_num:
                output = self.__players_scores__.index(player)
                return output

        return None

    def __get_point__(self, player_num: int):
        try:
            self.__players_scores__[self.__get_player__index__(player_num)][1] += 1
            self.__chain_length__ += 1

        except IndexError as e:

            print(f"Такого игрока нет, {e}")
        except TypeError as e:
            print()

    def __get_point_final__(self, player_num: int):
        try:
            self.__players_scores__[self.__get_player__index__(player_num)][1] += 1
        except IndexError as e:

            print(f"Такого игрока нет, {e}")
        except TypeError as e:
            print()

    def __lose_point__(self):

        self.__chain_length__ = 0

    def __save_bank__(self):

        self.__saved_bank__ += self.__chain_length__
        self.__chain_length__ = 0

    def __kick_player__(self):

        scores = [player[1] for player in self.__players_scores__]
        min_score = min(scores)
        kicking = []

        for player in self.__players_scores__:
            try:
                if player[1] == min_score:
                    n = player[0].split(sep=".")[0]
                    kicking.append(int(n))
            except IndexError as e:
                print(f"{e}")

        if len(kicking)>1:
            if len(set(kicking)) == 1:
                raise ValueError("Несколько раз один индекс добавился")

            kicking = self.__choice_kick__(kicking)

        value = self.__get_player__index__(kicking)
        if value is not None and kicking is not None:
            kicking = value
        else:
            return False
        print(f"{self.__players_scores__[kicking]} оказался(ь) слабым звеном")

        self.__players_scores__.pop(kicking)
        return True

    @staticmethod
    def __choice_kick__(kicking: list[int]):

        for kick in kicking:

            print(kick)

        kick_num = int(input("Напишите номер выбываемого игрока: "))
        if kick_num in kicking:
            return kick_num
        else:
            print("Этого игрока нет или он не с наименьшей суммой баллов")
            return None

    def __final_duel__(self, count_questions: int):

        count = 0

        while count < count_questions*2:

            inp = input()
            try:

                action = inp.split(sep=" ")

                if action[1] == '+':

                    self.__get_point_final__(player_num=int(action[0]))

            except IndexError as e:

                pass

        while self.__players_scores__[0][1] == self.__players_scores__[-1][1]:

            inp = input()

            try:

                action = inp.split(sep=" ")

                if action[1] == '+':

                    self.__get_point_final__(player_num=int(action[0]))

            except IndexError as e:

                pass

        if self.__players_scores__[0][1] > self.__players_scores__[1][1]:

            print(f"{self.__players_scores__[0][0]}: {self.__players_scores__[0][1]}")

        else:

            print(f"{self.__players_scores__[1][0]}: {self.__players_scores__[1][1]}")