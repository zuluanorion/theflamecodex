# theflamecodex.com

The Flame Codex / El Códice de la Llama — the sacred language, the Descent of the Flame, Light Code meditation, and the retreats and initiations of the Flame.
English at /, Spanish at /es/. Static files in public/, served by Cloudflare Workers (wrangler.jsonc).

Sister sites: drzuluanorion.org (the author) · www.spiritualbalanceinfo.com (the clinic).

## Source
webgen/ holds the generator (Python 3, no extra packages). Cloudflare serves only public/.
Rebuild: `python3 webgen/build.py` rewrites the HTML in public/; the images and PDFs stay as they are.
