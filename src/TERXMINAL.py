import shutil
import subprocess
import sys

MODEL = "mistral"


def run_ollama(prompt: str) -> str:
    process = subprocess.Popen(
        ["ollama", "run", MODEL],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    output, error = process.communicate(prompt)
    if process.returncode != 0:
        return "error: %s" % (error.strip() or "ollama keluar dengan kode %d" % process.returncode)
    return output.strip()


def main() -> int:
    if shutil.which("ollama") is None:
        print("Ollama tidak ditemukan. Install dari https://ollama.com lalu jalankan `ollama pull %s`." % MODEL)
        return 1

    print("TERXMINAL 🦖")
    print("ketik 'exit' untuk keluar\n")

    while True:
        try:
            user_input = input("you > ")
        except (EOFError, KeyboardInterrupt):
            print("\nTERXMINAL tidur... 🦖")
            return 0

        if user_input.lower() == "exit":
            print("TERXMINAL tidur... 🦖")
            return 0

        response = run_ollama(user_input)
        print("\nterx >", response, "\n")


if __name__ == "__main__":
    sys.exit(main())
