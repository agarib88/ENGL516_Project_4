# open a file 
with open('project_3_example_text_new.txt') as project_3_example_doc:
    project_3_example_content = project_3_example_doc.read()
print(project_3_example_content)

# find the annotation 
import re
project_3_annotation = re.findall(r"\[\[.+?\]\]\(\(.+?\)\)", project_3_example_content)
print(project_3_annotation)

# save the output as new lines (optimal version)
with open('trial.txt', "a+") as f:
    for item in project_3_annotation:
        f.write(str(item + '\n'))

# format into different lines (another way for output)
project_3_annotation_lines = '\n'.join(project_3_annotation)
print(project_3_annotation_lines)

# save the output
with open('output.txt', 'w') as output_doc:
    output_doc.write(project_3_annotation_lines)