NAVY="#121A26"; CORAL_L="#D4664A"; CORAL_D="#F2A38A"; CREAM="#EAF0F7"
UP="M187 88 A59 59 0 1 0 117.75 146.1 L123.66 112.62 A25 25 0 1 1 153 88 Z"
LO="M69 168 A59 59 0 1 0 138.25 109.9 L132.34 143.38 A25 25 0 1 1 103 168 Z"
def sym(top,bot): return f'<path fill="{top}" d="{UP}"/><path fill="{bot}" d="{LO}"/>'
def word(c):
    return (f'<path fill="{c}" d="M85 101 A29 29 0 1 0 56 130 A9 9 0 1 1 47 139 L27 139 A29 29 0 1 0 56 110 A9 9 0 1 1 65 101 Z"/>'
      f'<g fill="none" stroke="{c}" stroke-width="20" stroke-linecap="butt" stroke-linejoin="round">'
      ''
      '<path d="M113 74 L136.58 162 L153.73 98 L170.88 162 L194.46 74"/>'
      '<circle cx="265" cy="120" r="38"/><path d="M303 72 L303 168"/>'
      '<path d="M339 72 L339 216"/><circle cx="377" cy="120" r="38"/>'
      '<path d="M449 72 L449 216"/><circle cx="487" cy="120" r="38"/></g>')
def svg(vb,body,title="Swapp"):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}"><title>{title}</title>{body}</svg>\n'
W=lambda n,s: open(n,"w").write(s)
# symbols
W("swapp-symbol.svg", svg("0 0 256 256", sym(CORAL_L,NAVY)))
W("swapp-symbol-dark.svg", svg("0 0 256 256", sym(CORAL_D,CREAM)))
W("swapp-symbol-black.svg", svg("0 0 256 256", sym("#000","#000")))
# wordmark
W("swapp-wordmark.svg", svg("17 52 528 184", word(NAVY)))
# horizontal lockup: symbol scaled k so its height (198) ≈ 1.5 x-height (144)
k=0.73; sx=0; sy=120-128*k  # centre on x-height middle
def horiz(top,bot,wc):
    return (f'<g transform="translate({sx-69*k+8:.2f} {sy:.2f}) scale({k})">{sym(top,bot)}</g>'
            f'<g transform="translate({118*k+36:.2f} 0)">{word(wc)}</g>')
off=118*k+36
vb=f"0 40 {off+545:.0f} 196"
W("swapp-horizontal.svg", svg(vb, horiz(CORAL_L,NAVY,NAVY)))
W("swapp-horizontal-dark.svg", svg(vb, f'<rect x="-50" y="0" width="2000" height="400" fill="{NAVY}"/>'+horiz(CORAL_D,CREAM,CREAM)))
W("swapp-horizontal-reversed.svg", svg(vb, horiz(CORAL_D,CREAM,CREAM)))
# stacked: symbol on top, wordmark below
def stack(top,bot,wc):
    return (f'<g transform="translate({281-128} 0)">{sym(top,bot)}</g>'
            f'<g transform="translate(0 196) ">{word(wc)}</g>')
W("swapp-stacked.svg", svg("10 20 542 404", stack(CORAL_L,NAVY,NAVY)))
W("swapp-stacked-reversed.svg", svg("10 20 542 404", stack(CORAL_D,CREAM,CREAM)))
# app icon 1024 with 70s bands signature
bands=["#2B4A6E","#4D6F95","#E08A6E","#F2C2A8"]
b="".join(f'<rect x="0" y="{820+i*34}" width="1024" height="34" fill="{c}"/>' for i,c in enumerate(bands))
W("swapp-app-icon.svg", svg("0 0 1024 1024", f'<rect width="1024" height="1024" fill="{NAVY}"/>{b}<g transform="translate(512 410) scale(2.55) translate(-128 -128)">{sym(CORAL_D,CREAM)}</g>'))
W("swapp-app-icon-plain.svg", svg("0 0 1024 1024", f'<rect width="1024" height="1024" fill="{NAVY}"/><g transform="translate(512 500) scale(2.9) translate(-128 -128)">{sym(CORAL_D,CREAM)}</g>'))
