# TERXMINAL

BETA — a small terminal chat client for a local [Ollama](https://ollama.com) model.

## Requirements

- Python 3.9 or newer
- Ollama installed and running locally
- The model pulled once: `ollama pull mistral`

## Run

```bash
python3 src/TERXMINAL.py
```

Type a message and press Enter. Type `exit` (or press Ctrl-D) to quit.

## Configuration

The model is set by `MODEL` at the top of `src/TERXMINAL.py` (default:
`mistral`). Change it to any model you have pulled, for example `llama3.2`.

## Notes

- The script talks to Ollama through the `ollama run` command; it does not call
  the HTTP API directly.
- If Ollama is missing, the script prints an install hint instead of a traceback.
- A failed generation prints the error from Ollama and keeps the session open.
