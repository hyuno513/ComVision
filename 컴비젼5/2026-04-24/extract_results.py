import json

with open('2.의사결정나무_회귀분석.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

results = []
for cell in nb['cells']:
    if cell['cell_type'] == 'code' and cell.get('outputs'):
        for output in cell['outputs']:
            if output.get('output_type') == 'stream' and output.get('text'):
                text = ''.join(output['text'])
                results.append(text)

full_text = '\n'.join(results)

with open('output/실행결과.txt', 'w', encoding='utf-8') as f:
    f.write(full_text)

print("Results extracted to output/실행결과.txt")
