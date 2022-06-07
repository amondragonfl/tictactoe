from game import main
import colorama

if __name__ == "__main__":
    colorama.init(autoreset=True)
    try:
        main()
    except KeyboardInterrupt:
        raise SystemExit
