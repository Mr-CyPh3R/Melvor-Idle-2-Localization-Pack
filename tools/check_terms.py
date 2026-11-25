import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


WORK = Path(__file__).resolve().parents[1] / "work"
MARKUP = re.compile(r"\{[^{}]*\}|\[[^\]]*\]")
WORD = re.compile(r"\w+")


def load_terms(lang):
    terms = defaultdict(set)
    for line in (WORK / f"glossary_{lang}.tsv").read_text("utf-8-sig").splitlines():
        source, target = line.split("\t", 1)
        terms[source.casefold()].add(target.casefold())
    style_terms = defaultdict(set)
    for line in (WORK / f"STYLE_{lang}.md").read_text("utf-8").splitlines():
        if not re.match(r"^[\w (/)]+=", line):
            continue
        for pair in line.split(" · "):
            source, target = pair.split("=", 1)
            source = source.split(" (")[0]
            target = target.split(" (")[0]
            if source.endswith("(s)"):
                singular = source[:-3]
                style_terms[singular.casefold()].add(target.split("(")[0].casefold())
                plural = "Missões" if target == "Missão(ões)" else target.replace("(s)", "s")
                style_terms[singular.casefold() + "s"].add(plural.casefold())
            else:
                for name, value in zip(source.split("/"), target.split("/"), strict=True):
                    style_terms[name.casefold()].add(value.casefold())
    for source, targets in style_terms.items():
        terms.setdefault(source, targets)
    return terms


def check(lang):
    terms = load_terms(lang)
    by_word = defaultdict(set)
    patterns = {}
    for source in terms:
        words = WORD.findall(source)
        if words:
            by_word[max(words, key=len)].add(source)
        patterns[source] = re.compile(r"(?<!\w)" + re.escape(source) + r"(?!\w)")
    symbols = {source for source in terms if not WORD.search(source)}
    translations = {}
    for path in sorted((WORK / lang).glob("*.json")):
        translations.update(json.loads(path.read_bytes()))
    counts = Counter()
    missing = defaultdict(set)
    for item in json.loads((WORK / "items.json").read_bytes()):
        value = translations.get(item["id"], "")
        forms = value if isinstance(value, list) else [value]
        hits = set()
        for index, target in enumerate(forms):
            source = item["en_plural"] if index and item["en_plural"] else item["en"]
            source = MARKUP.sub(" ", source).casefold()
            target = MARKUP.sub(" ", target).casefold()
            candidates = symbols.union(*(by_word[w] for w in set(WORD.findall(source))))
            for term in candidates:
                if patterns[term].search(source):
                    hits.add(term)
                    if not any(t in target for t in terms[term]):
                        missing[term].add(item["id"])
        counts.update(hits)
    for term in sorted(counts):
        ids = sorted(missing[term])
        print(f"{term}\t{len(ids)}/{counts[term]}\t{', '.join(ids)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="List possible terminology mismatches by source term and text ID.")
    parser.add_argument("--lang", required=True, choices=("pt_BR", "ja", "pl"))
    check(parser.parse_args().lang)
