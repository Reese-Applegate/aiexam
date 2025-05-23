# gugudan.py
def gugudan():
    for i in range(1, 10):
        for j in range(1, 10):
            print(f"{i} x {j} = {i * j}")
        print()  # Add a blank line between each table


def test():
    print("테스트입니다.")


if __name__ == "__main__":
    gugudan()
