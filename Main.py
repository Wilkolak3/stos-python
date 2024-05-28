from Stos import Stos

if __name__ == '__main__':
    stos = Stos()
    stos.push(1)
    stos.push(2)
    stos.push(3)
    stos.push(4)

    print(stos.top())
    print(stos.pop())
    print(stos.is_empty())