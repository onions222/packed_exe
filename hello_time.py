from datetime import datetime


def main() -> None:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("helloword")
    print(f"当前时间: {now}")


if __name__ == "__main__":
    main()
