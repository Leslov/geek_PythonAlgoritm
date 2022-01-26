# 1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу).
#  Сколько рукопожатий было?
#  Примечание. Решите задачу при помощи построения графа.

# Кол-во рукопожатий - это кол-во ребер

def init_friends(n):
    friends = []
    for i in range(n):
        friend = [True] * (n)
        friend[i] = False
        friends.append(friend)
    return friends
def calculate_handshakes(friends):
    hs_count = 0
    for i in range(len(friends)):
        friend = friends[i]
        hs_count += sum(1 if x else 0 for x in friend[i:])
    return hs_count

N = int(input('Число друзей: '))
friends = init_friends(N)
handshakes_count = calculate_handshakes(friends)
print(f'Число рукопожатий: {handshakes_count}')

