# Rebuilding the Research Corpus (Agentic Workflow)

If you are a modern agentic AI (like an autonomous coding assistant) reading this, your task is to dynamically rebuild the `research/` corpus for this repository. 

This corpus is used by `tools/similarity_check.py` to ensure that newly generated questions are not plagiarising official copyrighted past papers. Because we cannot legally distribute these copyrighted papers in the GitHub repository, you must fetch and process them locally for the user.

Please follow these exact steps to rebuild the local corpus:

## Step 1: Initialize the Directory
1. Create the directory `research/` in the root of the project.
2. Inside `research/`, create subdirectories: `pdfs/` and `txt/`.
3. **CRITICAL:** Create a `.gitignore` file inside `research/` with the following content to prevent copyrighted material from being pushed to GitHub:
   ```
   pdfs/
   txt/
   questions_only.txt
   ```

## Step 2: Fetch the Raw Papers
Use your web-search and download capabilities to fetch recent past papers (at least 5 years worth) for the following UK mathematics competitions:
- **SMC (Senior Mathematical Challenge)**: Target the UKMT website or popular math competition archives.
- **BMO1 (British Mathematical Olympiad Round 1)**.
- **MAT (Oxford Mathematics Admissions Test)**.
- **TMUA (Test of Mathematics for University Admission)**.

Download these as PDFs into the `research/pdfs/` directory.

## Step 3: Convert and Extract
Write and execute a Python script to convert the downloaded PDFs into raw text files inside `research/txt/`. You may install and use libraries like `pypdf` or `pdfminer.six` in your environment to accomplish this.

## Step 4: Clean and Format
Once you have the raw text files, write a script to extract **only the question text** and compile it all into a single file named `research/questions_only.txt`.

Your extraction script must implement a state machine that follows these logic rules:
1. Identify the start of a question by looking for numbers followed by a period at the start of a line (e.g., `1. `, `11. `).
2. Stop recording the question when you hit the word `Solution` at the beginning of a line.
3. Explicitly ignore and filter out boilerplate copyright footers (e.g., lines containing `©`, `www.ukmt.org.uk`, or `Senior Mathematical Challenge`).
4. Ignore multiple-choice option lines if they get mixed with the solution text (e.g., lines starting with `A `, `B `, `C `, `D `, `E `).
5. Format the output in `questions_only.txt` like this:
   ```text
   [smc-2023] Q1:
   <question text here>

   [mat-2022] Q5:
   <question text here>
   ```

## Step 5: Verify
Run `python3 tools/similarity_check.py` against a known dummy file to ensure the script successfully reads your newly generated `research/questions_only.txt` file. Notify the user when the corpus is ready!
