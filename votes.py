# Нужно вывести число, которое встречается чаще всего в списке

def vote(votes):
    return (max(votes, key=lambda el: votes.count(el)))


if __name__ == '__main__':
    print(vote([1, 1, 1, 2, 3]))
    print(vote([1, 2, 3, 2, 2]))
