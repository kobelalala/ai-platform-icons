#!/usr/bin/env python3
"""Fetch App Store icons via iTunes Search API.
Domestic apps searched in CN store, international in US store.
Saves 512x512 artwork as PNG.
"""
import json, os, sys, urllib.request, urllib.parse

OUT = os.path.expanduser("~/workspace/ai-platform-icons")
os.makedirs(f"{OUT}/domestic", exist_ok=True)
os.makedirs(f"{OUT}/international", exist_ok=True)

DOMESTIC = [
    ("doubao", "豆包"),
    ("deepseek", "DeepSeek"),
    ("tongyi-qianwen", "通义千问"),
    ("yuanbao", "腾讯元宝"),
    ("kimi", "Kimi"),
    ("wenxin-yiyan", "文心一言"),
    ("zhipu-qingyan", "智谱清言"),
    ("xunfei-xinghuo", "讯飞星火"),
]
INTERNATIONAL = [
    ("chatgpt", "ChatGPT"),
    ("claude", "Claude"),
    ("gemini", "Gemini"),
    ("grok", "Grok"),
    ("perplexity", "Perplexity"),
    ("copilot", "Microsoft Copilot"),
    ("meta-ai", "Meta AI"),
    ("le-chat", "Le Chat"),
]

FALLBACK = {
    "yuanbao": "元宝",
    "zhipu-qingyan": "智谱清言",
    "xunfei-xinghuo": "讯飞星火",
    "le-chat": "Mistral",
}

def search(term, country):
    url = ("https://itunes.apple.com/search?" + urllib.parse.urlencode(
        {"term": term, "country": country, "entity": "software", "limit": 5}))
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)

def pick(results, want):
    """Pick best match: prefer exact/starts-with trackName match (case-insensitive)."""
    if not results:
        return None
    w = want.lower()
    for r in results:
        if r.get("trackName", "").lower() == w:
            return r
    for r in results:
        if r.get("trackName", "").lower().startswith(w):
            return r
    for r in results:
        if w in r.get("trackName", "").lower():
            return r
    return results[0]

def fetch_one(fname, term, country, folder):
    data = search(term, country)
    results = data.get("results", [])
    print(f"[{fname}] term={term!r} country={country} -> {len(results)} results")
    for r in results[:5]:
        print(f"    - {r.get('trackName')!r} by {r.get('sellerName')!r} bundle={r.get('bundleId')!r}")
    best = pick(results, term)
    if best is None:
        print(f"    !! NO RESULTS for {fname} ({term})")
        return None
    art = best.get("artworkUrl512") or best.get("artworkUrl100")
    if not art:
        print(f"    !! no artwork for {fname}")
        return None
    # artworkUrl512 is 512x512 jpg; keep as-is but save with .png name per spec.
    # Actually download bytes and save; extension .png per task spec.
    dest = f"{OUT}/{folder}/{fname}.png"
    req = urllib.request.Request(art, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        blob = r.read()
    with open(dest, "wb") as f:
        f.write(blob)
    print(f"    => {best.get('trackName')!r} ({best.get('bundleId')}) -> {dest} ({len(blob)} bytes, content-type image)")
    return dest

def main():
    missing = []
    for fname, term in DOMESTIC:
        try:
            d = fetch_one(fname, term, "CN", "domestic")
        except Exception as e:
            print(f"    !! error {fname}: {e}")
            d = None
        if d is None and fname in FALLBACK:
            print(f"    retry with fallback term {FALLBACK[fname]!r}")
            try:
                d = fetch_one(fname, FALLBACK[fname], "CN", "domestic")
            except Exception as e:
                print(f"    !! error {fname}: {e}")
                d = None
        if d is None:
            missing.append(fname)
    for fname, term in INTERNATIONAL:
        try:
            d = fetch_one(fname, term, "US", "international")
        except Exception as e:
            print(f"    !! error {fname}: {e}")
            d = None
        if d is None and fname in FALLBACK:
            print(f"    retry with fallback term {FALLBACK[fname]!r}")
            try:
                d = fetch_one(fname, FALLBACK[fname], "US", "international")
            except Exception as e:
                print(f"    !! error {fname}: {e}")
                d = None
        if d is None:
            missing.append(fname)
    print("\nMISSING:", missing if missing else "none")

if __name__ == "__main__":
    main()
