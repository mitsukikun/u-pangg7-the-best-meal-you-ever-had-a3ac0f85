import os

LINE = ("The best meal I ever had was ten sticks of smoky goat satay at a Yogyakarta night market, eaten standing in the rain, peanut sauce dripping down my wrist while the vendor fanned the coals.")

def main():
    try:
        os.makedirs("/output", exist_ok=True)
    except OSError:
        pass
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
