import os
import ollama
from graphviz import Digraph

os.environ['PATH'] += os.pathsep + "C:/Program Files/Graphviz/bin"

def analyze_code_for_flow(code_snippet):
    prompt = f"Analyze the following python code and describe its logic flow in a simple way:\n\n{code_snippet}"

    response = ollama.generate(
        model="deepseek-r1:8b",
        prompt=prompt,
        options={"temperature": 0.3}
    )
    return response['response']

def generate_flowchart_from_analysis(flow_analysis):
    dot = Digraph(comment="Python Code Flow")
    dot.node('A','Start')
    dot.node('B','Process')
    dot.node('C','End')

    dot.edges(['AB','BC'])
    return dot

def render_flowchart(flow_analysis):
    flowchart = generate_flowchart_from_analysis(flow_analysis)
    flowchart.render('flowchart_output', view=True)

code_snippet = '''
def add_numbers(a,b,c):
    result = a + b + c
    return result
'''

flow_analysis = analyze_code_for_flow(code_snippet)
print("Code Analysis: ", flow_analysis)
render_flowchart(flow_analysis)