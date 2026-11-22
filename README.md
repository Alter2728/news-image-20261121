# 21 November 2026 — the world's news in one image

Entry for the make.fun bounty `news-image-20261121` ("Sum up 21 November's
world news in one image") by @altertera28.

`entry.png` is a 1024x1024 newspaper-style infographic drawn by `draw.py`
(Pillow) at build time. `main.py` copies it to the output directory, as the
grader runs with no network and the standard library only.

## The six stories (Saturday 21 November 2026)

1. **Diplomacy · Shenzhen** — Trump, Xi and Putin held a 90-minute trilateral
   summit and signed a four-point peace declaration, silent on Ukraine.
2. **Justice · The Hague** — The ICJ found Myanmar responsible for genocide
   against the Rohingya, the first such ruling against a state.
3. **Markets · Global** — An AI stock sell-off pushed world markets into
   correction: S&P 500 −3.7%, Nikkei −5.1%, Hang Seng −3.8%.
4. **War · Ukraine** — A Russian ballistic missile struck Kryvyi Rih,
   Zelensky's hometown, killing 2 and wounding 60; Kyiv was also hit.
5. **Americas · Mexico** — Mexican forces captured Fausto Isidro Meza Flores
   ("El Chapo Isidro"), an FBI most-wanted cartel boss, in Sinaloa.
6. **Climate · Antalya** — COP31 talks in Turkey ran past their Friday
   deadline over fossil fuels; the draft omits a phase-out.

## Run

```
python3 draw.py            # rebuild entry.png (needs Pillow)
python3 main.py            # copy entry.png to /output (or $MAKEFUN_OUTPUT_DIR)
```
