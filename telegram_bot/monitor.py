import subprocess

if __name__ == '__main__':
    while True:
        try:
            subprocess.run(["/home/str/2kaz/.venv/bin/python", "/home/str/2kaz/start_all_bot.py"])
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Ошибка: {e}")
