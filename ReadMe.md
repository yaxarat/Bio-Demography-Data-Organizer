# Data Organizer Read Me
This project is separated in 4 main modules working in 2 different steps. Original data must be UTF8 and program specifics compliant.

### Step 1 Modules
- Replacer.py
- Parser.py
- Namer.py
### Step 2 Module
- FreqFraq.py

Or you can run all at once by running the Main.py

### File Structure
Original files where nothing has been processed yet is to be placed in a folder named *original_record*. Once step 1 modules finishes running, it well create files where each strand within the record.txt is separated into different .txt files. This result file structure will be outputted to a folder called *separated_records*. Once the separated records are ready, FreqFraq.py can be run. FreqFraq.py will produce survival and mortality frequency/fraction data for each strands. These files will be located within the freqfraq folder.
## Module details
### Replacer.py
Replaces specific non-utf8 compliant characters to compliant string.
```kotlin
// Specific replacement
for line in fileinput.input([file], inplace=True):
    print(line.replace('°C', 'dgr'), end='')
    print(line.replace('∞C', 'dgr'), end='')
```

### Parser.py
Separates one file contains multiple different strands into separate strand file under a correct folder structure.
### Namer.py
Names each produced files with its appropriate strand name.
### FreFrq.py
Creates survival and mortality frequency/fraction data for each strands.
### Main.py
Runs all modules in sequence.
