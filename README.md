# Translation Script

This script reads a `.txt` file containing words, removes punctuation, identifies new words not seen before, translates them into a target language, and generates a CSV file for tools like **Anki**.

## Installation

1. **Clone or download** the script:
   ```bash
   git clone https://github.com/marvinobig/translation-script.git
   cd ./translation-script
   ```

2. **Install Python dependencies** using `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

3. **(Optional) Make the script executable** (Linux/MacOS):
   ```bash
   chmod +x ./translation-script.py
   ```

## Usage

Run the script from the terminal:

```bash
python translation-script.py <input-file> <target-language-code>
```
Or if you made it executable:

```bash
./translation-script.py <input-file> <target-language-code>
```

### Arguments:
- `<input-file>`: Path to your input `.txt` file containing words.
- `<target-language-code>`: Language code for translation (e.g., `de` for German, `fr` for French, etc.).

## Output

- A CSV file named `anki_<uuid>.csv` is generated in the **/translations** folder (which is created in the same location as the script) where the script is run.
- **Format**: `[original_word, translated_word]`
- A text file called `SAVE.txt` is generated and updated to **track already translated words**.
- If a word is already present in `SAVE.txt`, it will not be translated again.

## Script Behavior

- Only `.txt` files are accepted as input.
- Prints number of translated words e.g. `"Translated 68 words"`
- If no new words are found, it prints `"No new words to translate"`.
- All punctuation is automatically removed from the input before splitting words.
- Words are stored and compared in **lowercase** to ensure consistency.

