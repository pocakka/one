\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{magazine}[2025/11/04 AI Security Magazine Class]

% Base class
\LoadClass[a4paper,11pt]{article}

% Packages
\RequirePackage[utf8]{inputenc}
\RequirePackage[magyar]{babel}
\RequirePackage[T1]{fontenc}
\RequirePackage{geometry}
\RequirePackage{graphicx}
\RequirePackage{xcolor}
\RequirePackage{fancyhdr}
\RequirePackage{titlesec}
\RequirePackage{tcolorbox}
\RequirePackage{multicol}
\RequirePackage{enumitem}
\RequirePackage{fontawesome5}
\RequirePackage{lmodern}
\RequirePackage{charter}
\RequirePackage{microtype}
\RequirePackage{hyperref}
\RequirePackage{tocloft}
\RequirePackage{lettrine}
\RequirePackage{lipsum}

% Geometry
\geometry{
    a4paper,
    top=2cm,
    bottom=2cm,
    left=2cm,
    right=2cm,
    headsep=0.8cm,
    footskip=1cm
}

% Colors
\definecolor{primary}{RGB}{0,102,204}      % Deep Blue
\definecolor{secondary}{RGB}{220,50,47}     % Red
\definecolor{accent}{RGB}{38,139,210}       % Light Blue
\definecolor{darkgray}{RGB}{51,51,51}
\definecolor{lightgray}{RGB}{242,242,242}
\definecolor{success}{RGB}{133,153,0}       % Green

% Hyperref setup
\hypersetup{
    colorlinks=true,
    linkcolor=primary,
    urlcolor=accent,
    citecolor=secondary
}

% Header and Footer
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\color{primary}\textbf{AI Security Magazine}}
\fancyhead[R]{\color{darkgray}\textit{\@issue}}
\fancyfoot[C]{\color{darkgray}\thepage}
\renewcommand{\headrulewidth}{2pt}
\renewcommand{\headrule}{\hbox to\headwidth{\color{primary}\leaders\hrule height \headrulewidth\hfill}}

% Title formatting
\titleformat{\section}
  {\color{primary}\Large\bfseries\sffamily}
  {}
  {0em}
  {\colorbox{lightgray}{\parbox{\dimexpr\textwidth-2\fboxsep\relax}{\thesection\quad#1}}}

\titleformat{\subsection}
  {\color{accent}\large\bfseries\sffamily}
  {}
  {0em}
  {#1}

\titleformat{\subsubsection}
  {\color{darkgray}\normalsize\bfseries\sffamily}
  {}
  {0em}
  {#1}

% Custom commands
\newcommand{\@issue}{1. szám}
\newcommand{\issue}[1]{\renewcommand{\@issue}{#1}}

\newcommand{\@subtitle}{}
\newcommand{\subtitle}[1]{\renewcommand{\@subtitle}{#1}}

% Cover page
\renewcommand{\maketitle}{
    \begin{titlepage}
        \begin{center}
            \vspace*{2cm}

            {\Huge\bfseries\color{primary}\@title}

            \vspace{0.5cm}

            {\Large\color{accent}\@subtitle}

            \vspace{2cm}

            {\color{darkgray}\rule{\textwidth}{2pt}}

            \vspace{1cm}

            {\LARGE\color{secondary}\textbf{\@issue}}

            \vspace{0.5cm}

            {\Large\color{darkgray}\@date}

            \vfill

            {\large\color{darkgray}\textit{A mesterséges intelligencia biztonságának szakmai magazinja}}

            \vspace{1cm}

        \end{center}
    \end{titlepage}
    \newpage
}

% Box styles
\newtcolorbox{infobox}[1][]{
    colback=lightgray,
    colframe=primary,
    fonttitle=\bfseries,
    title=#1,
    boxrule=1.5pt,
    arc=3pt
}

\newtcolorbox{warningbox}[1][]{
    colback=red!5,
    colframe=secondary,
    fonttitle=\bfseries,
    title=#1,
    boxrule=1.5pt,
    arc=3pt
}

\newtcolorbox{tipbox}[1][]{
    colback=green!5,
    colframe=success,
    fonttitle=\bfseries,
    title=#1,
    boxrule=1.5pt,
    arc=3pt
}

% Quote style
\renewenvironment{quote}
  {\list{}{\leftmargin=1cm\rightmargin=1cm}\item\relax\color{darkgray}\itshape}
  {\endlist}

% TOC styling
\renewcommand{\cftsecfont}{\bfseries\color{primary}}
\renewcommand{\cftsecpagefont}{\bfseries\color{primary}}
\renewcommand{\cftsubsecfont}{\color{accent}}
\renewcommand{\cftsubsecpagefont}{\color{accent}}

\endinput
