import re

def parse_markdown_qa(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split by ### <num>. <title>
    blocks = re.split(r'\n###\s+(\d+)\.\s*(.*?)\n', '\n' + content)
    questions = []
    
    # If standard split worked (blocks has num, title, body groups)
    if len(blocks) > 3:
        for i in range(1, len(blocks), 3):
            q_num = blocks[i].strip()
            q_title = blocks[i+1].strip()
            body = blocks[i+2]
            
            # Domain
            d_match = re.search(r'\*\*Domain:\*\*\s*(?:`([^`]+)`|([^\n|\r]+))', body)
            domain = (d_match.group(1) or d_match.group(2)).strip() if d_match else 'Cloud Technology & Service'
            
            # Type
            t_match = re.search(r'\*\*Type:\*\*\s*(?:`([^`]+)`|([^\n|\r]+))', body)
            type_raw = (t_match.group(1) or t_match.group(2)).strip().lower() if t_match else ''
            
            # Difficulty
            diff_match = re.search(r'\*\*Difficulty:\*\*\s*(?:`([^`]+)`|([^\n|\r\*]+))', body)
            difficulty = (diff_match.group(1) or diff_match.group(2)).strip().lower() if diff_match else 'medium'
            
            # Question text
            q_match = re.search(r'\*\*Question:\*\*\s*(?:>\s*)?(.*?)(?=\n\*\*Options:\*\*|\n-\s*\[?[A-E]\]?|\n\*\*Correct Answer:)', body, re.S)
            if not q_match:
                continue
            q_text = q_match.group(1).strip().lstrip('> ').strip()
            
            # Options block
            opts = []
            opts_block_match = re.search(r'(?:\*\*Options:\*\*|\n-\s*\[?[A-E]\]?[.\s])(.*?)(?=\n\*\*Correct Answer:)', body, re.S)
            if opts_block_match:
                raw_text = opts_block_match.group(0)
                for line in raw_text.split('\n'):
                    line_clean = line.strip()
                    if re.match(r'^\*{0,2}Options:?\*{0,2}', line_clean, re.I):
                        continue
                    if line_clean.startswith('-') or line_clean.startswith('*'):
                        opt_str = re.sub(r'^[-\*]\s*', '', line_clean).strip()
                        # Remove bolded brackets like **[A]** or [A] or A.
                        opt_str = re.sub(r'^(?:\*{0,2}\[[A-H]\]\*{0,2}|[A-H][\.\):])\s*-?\s*', '', opt_str).strip()
                        if opt_str and not re.match(r'^\*{0,2}Options:?\*{0,2}', opt_str, re.I) and opt_str not in ['--', '-', '---']:
                            opts.append(opt_str)
            else:
                raw_opts = re.findall(r'^-\s*(.+)', body, re.M)
                for o in raw_opts:
                    clean_o = re.sub(r'^(?:\*{0,2}\[[A-H]\]\*{0,2}|[A-H][\.\):])\s*-?\s*', '', o.strip()).strip()
                    if clean_o and not re.match(r'^\*{0,2}Options:?\*{0,2}', clean_o, re.I) and clean_o not in ['--', '-', '---']:
                        opts.append(clean_o)
                opts = opts[:5]

            # Correct Answer
            corr_match = re.search(r'\*\*Correct Answer:\*\*\s*(.*?)(?=\n\*\*Why|\n---|\Z)', body, re.S)
            corr_text = corr_match.group(1).strip() if corr_match else ''
            
            # Clean corr_text brackets
            cleaned_corr_lines = []
            for cl in corr_text.split('\n'):
                c_clean = cl.strip().lstrip('-* ').strip()
                c_clean = re.sub(r'^\*{0,2}\[[A-H]\]\*{0,2}\s*', '', c_clean).strip('*_ ')
                if c_clean and not re.match(r'^\*{0,2}Correct Answer:?\*{0,2}', c_clean, re.I):
                    cleaned_corr_lines.append(c_clean)
            clean_correct_str = "\n".join(cleaned_corr_lines) if cleaned_corr_lines else corr_text

            # Why Correct
            why_corr_match = re.search(r'\*\*Why Correct:\*\*\s*(.*?)(?=\n\*\*Why (?:Others?|Wrong)|\n---|\Z)', body, re.S)
            why_corr = why_corr_match.group(1).strip() if why_corr_match else ''
            
            # Why Wrong
            why_wrong_match = re.search(r'\*\*Why (?:Others? Are Incorrect|Others? Wrong|Wrong):\*\*\s*(.*?)(?=\n---|\n###|\Z)', body, re.S)
            why_wrong = why_wrong_match.group(1).strip() if why_wrong_match else ''
            
            # Determine q_type
            if 'multi' in type_raw or 'select' in type_raw:
                q_type = 'multi'
            elif 'single' in type_raw:
                q_type = 'single'
            else:
                is_multi = 'select two' in q_text.lower() or 'select 2' in q_text.lower() or 'select three' in q_text.lower() or 'which two' in q_text.lower() or 'two actions' in q_text.lower() or 'two services' in q_text.lower() or len(cleaned_corr_lines) > 1
                q_type = 'multi' if is_multi else 'single'

            questions.append({
                'num': q_num,
                'title': q_title,
                'domain': domain,
                'difficulty': difficulty,
                'q_type': q_type,
                'question_text': q_text,
                'options_raw': opts,
                'correct_text': clean_correct_str,
                'explanation_correct': why_corr,
                'explanation_wrong': why_wrong,
            })
    else:
        # Fallback for simple markdown
        blocks = re.split(r'###\s+\d+\.\s*', content)
        for block in blocks[1:]:
            q_match = re.search(r'\*\*Question:\*\*\s*(.*?)(?:\n- |\n\*\*Correct)', block, re.S)
            if not q_match:
                continue
            q_text = q_match.group(1).strip()
            raw_opts = re.findall(r'^-\s*(.+)', block, re.M)
            opts = [o.strip() for o in raw_opts if o.strip() and o.strip() not in ['--', '-', '---'] and not set(o.strip()) <= {'-', ' '}]
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

