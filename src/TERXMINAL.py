import subprocess

MODEL = "mistral"

def run_ollama(prompt: str) -> str:
    process = subprocess.Popen(
        ["ollama", "run", MODEL],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    output, _ = process.communicate(prompt)
    return output.strip()

def main():
    print("TERXMINAL 🦖")
    print("ketik 'exit' untuk keluar\n")

    while True:
        user_input = input("you > ")

        if user_input.lower() == "exit":
            print("TERXMINAL tidur... 🦖")
            break

        response = run_ollama(user_input)
        print("\nterx >", response, "\n")

if __name__ == "__main__":
    main()
