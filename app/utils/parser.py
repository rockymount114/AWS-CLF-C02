import re

def parse_markdown_qa(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    # Split by ### 
    blocks = re.split(r'###\s+\d+\.\s*', content)
    questions = []
    for block in blocks[1:]:
        # Extract question
        q_match = re.search(r'\*\*Question:\*\*\s*(.*?)(?:\n- |\n\*\*Correct)', block, re.S)
        if not q_match:
            continue
        q_text = q_match.group(1).strip()
        # Options: lines starting with - 
        raw_opts = re.findall(r'^-\s*(.+)', block, re.M)
        opts = [o.strip() for o in raw_opts if o.strip() and o.strip() not in ['--', '-', '---'] and not set(o.strip()) <= {'-', ' '}]

        # Correct answer
        correct_match = re.search(r'\*\*Correct Answer:\*\*\s*(.*?)(?:\n\*\*Why|\n---|\Z)', block, re.S)
        correct_text = correct_match.group(1).strip() if correct_match else ''
        why_correct = re.search(r'\*\*Why Correct:\*\*\s*(.*?)(?:\n\*\*Why Wrong|\n---|\Z)', block, re.S)
        why_wrong = re.search(r'\*\*Why Wrong:\*\*\s*(.*?)(?:\n---|\n###|\Z)', block, re.S)
        questions.append({
            'question_text': q_text,
            'options_raw': opts,
            'correct_text': correct_text,
            'explanation_correct': why_correct.group(1).strip() if why_correct else '',
            'explanation_wrong': why_wrong.group(1).strip() if why_wrong else '',
        })
    return questions
