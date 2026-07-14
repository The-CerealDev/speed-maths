import os
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_FILE = os.path.join(ROOT_DIR, 'template.html')
INDEX_FILE = os.path.join(ROOT_DIR, 'index.html')

PILLARS = {
    'algebra': 'PILLAR_ALGEBRA',
    'combinatorics': 'PILLAR_COMBINATORICS',
    'number-theory': 'PILLAR_NUMBER_THEORY',
    'geometry': 'PILLAR_GEOMETRY'
}

def build_site():
    print("Building website...")
    
    with open(TEMPLATE_FILE, 'r') as f:
        html_content = f.read()

    for pillar_folder, placeholder in PILLARS.items():
        pillar_path = os.path.join(ROOT_DIR, pillar_folder)
        sheets_path = os.path.join(pillar_path, 'sheets')
        answers_path = os.path.join(pillar_path, 'answers')

        sheets_found = []
        if os.path.exists(sheets_path):
            for file in sorted(os.listdir(sheets_path)):
                if file.endswith('.pdf'):
                    sheet_num = re.search(r'\d+', file)
                    if sheet_num:
                        sheets_found.append(sheet_num.group(0))

        if not sheets_found:
            # Inject coming soon message
            coming_soon_html = '''
                <div class="coming-soon">
                    Currently under construction. Want to contribute? <a href="https://github.com/The-CerealDev/speed-maths">View GitHub repo</a>
                </div>
            '''
            html_content = html_content.replace(f"<!-- {placeholder} -->", coming_soon_html)
            continue

        # If sheets exist, build the list
        html_list = ['<ul class="sheet-list">']
        
        for sheet_num in sheets_found:
            sheet_pdf = f"sheet{sheet_num}.pdf"
            ans_pdf = f"ans{sheet_num}.pdf"

            has_ans = os.path.exists(os.path.join(answers_path, ans_pdf))

            # Generate HTML pointing directly to the repo files
            list_item = f'''
                    <li>
                        <span class="sheet-name">Sheet {sheet_num}</span>
                        <div class="links">
                            <a href="{pillar_folder}/sheets/{sheet_pdf}" class="pdf-link" target="_blank">Questions</a>'''
            
            if has_ans:
                list_item += f'''
                            <a href="{pillar_folder}/answers/{ans_pdf}" class="pdf-link ans" target="_blank">Answers</a>'''
            
            list_item += '''
                        </div>
                    </li>'''
            html_list.append(list_item)

        html_list.append('</ul>')
        html_content = html_content.replace(f"<!-- {placeholder} -->", "\n".join(html_list))

    with open(INDEX_FILE, 'w') as f:
        f.write(html_content)
    
    print("Website build complete! index.html generated successfully in root.")

if __name__ == "__main__":
    build_site()
