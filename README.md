# The Winds of Kirina: Chronicles of Timbuktu 2142

*The Tiira: a story bible, world book and game design document by **Nci Jean Talsim Konte** (NJ Talsim).*

**Read it online:** https://s7d11.github.io/the-winds-of-kirina/

In the year 2142 Timbuktu stands severed from Mali, divided between corporate oligarchs, zealots and separatists. Two cousins, Khalil and Awa, go looking for a missing father and find a nation instead. This 208-page Tiira covers the world, the factions, the characters, the full branching campaign (*The Sahara Rebellion*), the game systems, the *Harmattan Royale* multiplayer mode, art direction, and in-world tales. It opens with a publisher pitch and the complete storyline told as prose.

All factions, leaders, creeds and events are fictional. The world draws on the real history and culture of Mali.

## Site

| Page | What it is |
|---|---|
| [`/`](https://s7d11.github.io/the-winds-of-kirina/) | Presentation page with the concept reel, characters, world and campaign |
| [`/tiira/`](https://s7d11.github.io/the-winds-of-kirina/tiira/) | The full Tiira: 208 pages, including the pitch and the complete story (built from `book/`) |

## Repository layout

| Path | What it is |
|---|---|
| `index.html` | Hand-written presentation page |
| `assets/` | Shared stylesheet, concept reel (with audio), concept art |
| `tiira/index.html` | The built book (do not edit by hand) |
| `book/canon.md` | Canon bible: binding names, dates and story facts |
| `book/parts/*.html` | Book content, one `<section class="page">` per page |
| `book/shell.html` | Book frame, navigation, styles and interactive widgets |
| `book/build.py` | Assembles the parts into `tiira/index.html` and checks the markup |

## Building

```bash
python3 book/build.py
```

© 2026 NJ Talsim. All rights reserved.
