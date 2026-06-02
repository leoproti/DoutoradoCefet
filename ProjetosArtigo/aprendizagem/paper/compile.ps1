$ErrorActionPreference = "Stop"

Push-Location $PSScriptRoot
try {
    if (Get-Command latexmk -ErrorAction SilentlyContinue) {
        latexmk -pdf -output-directory=build main.tex
    }
    elseif (Get-Command pdflatex -ErrorAction SilentlyContinue) {
        pdflatex -interaction=nonstopmode -halt-on-error -output-directory build main.tex
    }
    else {
        throw "Nenhum compilador LaTeX encontrado. Instale MiKTeX ou TeX Live."
    }
}
finally {
    Pop-Location
}