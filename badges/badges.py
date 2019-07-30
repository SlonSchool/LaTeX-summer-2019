import random

data = open('/dev/stdin','r').read()

print(r'''
\documentclass[a4page, landscape]{article}
\usepackage[utf8]{inputenc}
\usepackage[english,russian]{babel}
\usepackage[a4paper, landscape, margin=5pt] {geometry}
\usepackage{graphicx}
\usepackage{multicol}
\usepackage{rotating}
\usepackage{anyfontsize}
\setlength\parindent{0}
\begin{document}
''')

r'''\framebox{
	\hbox to 85.6mm{
		\vbox to 53.98mm{
			\hspace{5mm}
			
			\vspace{5mm}
			@0#
		}
	}
}
'''

template = r'''\framebox{
	\begin{minipage}[r][53.98mm][t]{85.6mm}
		\begin{flushright}
			\raisebox{-\totalheight}[0pt][9em]
			{
				\begin{turn}{@2#}
					\includegraphics
						[width=9em]
						{slon.png}
				\end{turn}
			}
		\end{flushright}

		\vspace*{-1.9em}

		\textbf
		{
			{ \fontsize{35}{9}\selectfont
				@1#
			}
		}

		\textbf
		{
			{ \fontsize{50}{0}\selectfont
				@0#
			}
		}
	\end{minipage}
}
'''.replace('{',' $_$ ').replace('}',' _$_ ').replace('@','{').replace('#','}')

for i, name in enumerate(data.split('\n')):
	name = list(name.split(' '))
	while len(name) < 2:
		name += ['']
	while len(name) > 2:
		del name[-1]

	name += [random.randint(-10,30)]

	print(template.format(*name).replace(' $_$ ','{').replace(' _$_ ','}'), end='')
	
	if (i+1) % 3 == 0:
		print()
		print()


print(r'''
\end{document}
''')
