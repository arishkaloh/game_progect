# Создаем пустое поле
board = [[' ' for _ in range(3)] for _ in range(3)]
# Определяем символы для игроков
players = ['X', 'O']
current_player = 0  # Индекс текущего игрока


# Функция для отрисовки поля
def print_board():
    print('---------')
    for row in board:
        print('|', end='')
        for cell in row:
            print(cell + '|', end='')
        print('\n---------')

    # Функция для проверки выигрышной комбинации


def check_win(player):
    # Проверяем строки
    for row in board:
        if row == [player, player, player]:
            return True

            # Проверяем столбцы
    for col in range(3):
        if [board[0][col], board[1][col], board[2][col]] == [player, player, player]:
            return True

            # Проверяем диагонали
    if [board[0][0], board[1][1], board[2][2]] == [player, player, player]:
        return True
    if [board[0][2], board[1][1], board[2][0]] == [player, player, player]:
        return True

    return False


# Основной игровой цикл
def game():
    while True:
        print_board()
        print(f"Ход игрока {players[current_player]})
        row = int(input("Введите номер строки (0, 1, 2): "))
        col = int(input("Введите номер столбца (0, 1, 2): "))

        # Проверяем, что выбранные координаты находятся в пределах поля и ячейка пустая
        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
            # Ставим символ текущего игрока на указанные координаты поля
            board[row][col] = players[current_player]

            # Проверяем, есть ли выигрышная комбинация
            if check_win(players[current_player]):
                print_board()
                print(f"Игрок {players[current_player]} победил!")
                break

                # Проверяем, что остались пустые ячейки
            if all(cell != ' ' for row in board for cell in row):
                print_board()
                print("Ничья!")
                break

                # Переходим к следующему игроку
            current_player = (current_player + 1) % 2
        else:
            print("Некорректный ход. Попробуйте еще раз.")

        # Запуск игры


game()