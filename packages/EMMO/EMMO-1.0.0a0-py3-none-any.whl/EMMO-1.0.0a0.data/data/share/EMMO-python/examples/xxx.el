(TeX-add-style-hook
 "xxx"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("report" "a4paper" "")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("fontenc" "T1") ("inputenc" "utf8") ("geometry" "margin=2cm")))
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperref")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperimage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperbaseurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "nolinkurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (TeX-run-style-hooks
    "latex2e"
    "report"
    "rep10"
    "lmodern"
    "amssymb"
    "amsmath"
    "ifxetex"
    "ifluatex"
    "fixltx2e"
    "fontenc"
    "inputenc"
    "textcomp"
    "unicode-math"
    "upquote"
    "microtype"
    "parskip"
    "graphicx"
    "xcolor"
    "hyperref"
    "geometry")
   (TeX-add-symbols
    '("institute" 1)
    "tightlist"
    "oldparagraph"
    "oldsubparagraph")
   (LaTeX-add-labels
    "relations"
    "entity-branch"
    "entities"
    "entity-branch-1"
    "individuals"
    "entity-branch-2"))
 :latex)

