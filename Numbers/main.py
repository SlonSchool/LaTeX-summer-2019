import csv

def csv_reader(path):
    global d
    reader = csv.reader(path)
    for row in reader:
        row = row[0]
        row = row.split(";")
        if row[-1] == '':
            row = row[:-1]
        if int(row[-1]) in d.keys():
            d[int(row[-1])] += "\\\\" + " ".join(row[:-1])
        else:
            d[int(row[-1])] = " ".join(row[:-1])


d = {}
path = "table.csv"
with open(path, 'r') as csv_path:
    csv_reader(csv_path)
    csv_path.close()
pathtex = "out.tex"
with open(pathtex, 'wb') as tex_path:
    tex_path.write("""\\documentclass[a4paper, landscape]{article}

\\usepackage[utf8]{inputenc}
\\usepackage[english,russian]{babel}
\\usepackage[a4paper, margin=0px,landscape]{geometry}
\\usepackage{graphicx}
\\geometry{top=0mm,left=0mm, right=0mm, bottom=0mm}

\\newcommand{\\PeopleField}[2]{\\framebox{\\begin{minipage}[c][50mm][c]{96mm}
            \\raisebox{-\\totalheight}[0pt][1em]
			{
				\\includegraphics
					[width=5em]
					{slon2.png}
			}
			\\begin{center}
				{\\large
					\\center
					{#1}\\\\}
				\\vbox to 1em{}
				{\\Large{#2}\\\\}

			\\end{center}
	\\end{minipage}}}

\\setlength\\parindent{0pt}

\\begin{document}\n""".encode())
    for key in d.keys():
        tex_path.write("\\PeopleField{\\textbf{\\LARGE".encode())
        tex_path.write(str(key).encode())
        tex_path.write("}}{".encode())
        tex_path.write(d[key].encode())
        tex_path.write("}\n".encode())

    tex_path.write("\\end{document}".encode())
    tex_path.close()
