"""Lot AJ, étape 1 — diagnostic de la garde, en lecture seule (n'écrit rien, ne publie rien).

    python3 diag_garde.py <entrepôt> M22_05 M22_07      détail des couples
    python3 diag_garde.py <entrepôt> --tous             tous les couples : variations contre la dernière passe

Compare, pour chaque couple :
  - production/publies/<couple>.json (référence actuelle de la garde : dernier envoi publié, celui de la collecte du matin)
  - passes/<chaque passe>/a_blanc/couples/<couple>.json (calcul du samedi)
"""
import json
import sys
from collections import Counter
from pathlib import Path

E = Path(sys.argv[1])
args = sys.argv[2:]
JOUR = "2026-10-24"


def lire(f):
    try:
        return json.loads(Path(f).read_text(encoding="utf-8"))
    except Exception:
        return None


def opps(env):
    return {o["id"]: o for o in env["publier_opportunites"]["opportunites"]} if env else {}


def valable(o, jour):
    if o.get("type") == "ao":
        return bool(o.get("date_limite")) and str(o["date_limite"]) >= jour
    return not o.get("echeance_estimee") or str(o["echeance_estimee"]) >= jour


def cle(o):
    return ((o.get("acheteur_nom") or "").lower().strip(), (o.get("texte_recherche") or o.get("intitule") or "").lower().strip()[:120])


def resume(env):
    if not env:
        return "absent"
    r = env["publier_rapport"]
    O = opps(env)
    z = r.get("zone") or {}
    return (f"zone {z.get('code')} ({z.get('type')}) · {len(O)} opportunités {dict(Counter(o['type'] for o in O.values()))} · "
            f"départements des acheteurs {dict(Counter(o.get('acheteur_dep') for o in O.values()).most_common(8))} · "
            f"chiffres {r.get('chiffres')} · {len(env['publier_opportunites']['attributions'])} attributions · édition {env.get('edition')}")


def ligne(o):
    return (f"    {o['id'][:60]:60} {o.get('type'):6} limite {o.get('date_limite') or '-':10} échéance {o.get('echeance_estimee') or '-':10} "
            f"dép. {o.get('acheteur_dep') or '-':3} {(o.get('acheteur_nom') or '')[:40]} · {(o.get('intitule') or '')[:70]}")


def comparer(nom_a, A_env, nom_b, B_env, couple, jour, detail=True):
    A, B = opps(A_env), opps(B_env)
    dep = couple.split("_")[1]
    disp = [o for i, o in A.items() if i not in B and valable(o, jour)]
    nouv = [o for i, o in B.items() if i not in A]
    cles_b = {cle(o): o for o in B.values()}
    print(f"\n  {nom_a} → {nom_b}")
    print(f"    avant : {resume(A_env)}")
    print(f"    après : {resume(B_env)}")
    valables = sum(1 for o in A.values() if valable(o, jour))
    print(f"    disparues encore valables : {len(disp)} sur {valables} ({round(100 * len(disp) / valables, 1) if valables else 0} %) · nouvelles : {len(nouv)}")
    a = sum(1 for o in disp if cle(o) in cles_b)
    c = sum(1 for o in disp if o.get("type") != "ao" and not o.get("echeance_estimee"))
    d = sum(1 for o in disp if dep != "FR" and o.get("acheteur_dep") and o.get("acheteur_dep") != dep)
    print(f"    parmi les disparues : (a) même acheteur et même objet présents après sous un autre id : {a} · "
          f"(c) sans date limite ni échéance : {c} · (d) acheteur hors du département {dep} : {d}")
    if detail:
        print("    -- disparues")
        for o in sorted(disp, key=lambda o: o["id"]):
            print(ligne(o) + (f"  [retrouvée sous {cles_b[cle(o)]['id']}]" if cle(o) in cles_b else ""))
        print("    -- nouvelles")
        for o in sorted(nouv, key=lambda o: o["id"]):
            print(ligne(o))


def photographie(c):
    """référence de la garde quand le couple n'a jamais été publié par le V2 ni calculé par une passe : le site (V1)"""
    try:
        import os
        sys.path.insert(0, os.environ.get("TH_MOTEUR", "/srv/tenderhit/moteur"))
        from tenderhit_v2.config import Chemins
        from tenderhit_v2 import non_regression
        return non_regression.reference_photographie(Chemins(None, E), c)
    except Exception as e:
        print(f"  (photographie du site indisponible pour {c} : {type(e).__name__} {str(e)[:120]})")
        return None


passes = sorted(p for p in (E / "passes").iterdir() if p.is_dir() and (p / "a_blanc" / "couples").exists()) if (E / "passes").exists() else []
print("passes :", [p.name for p in passes])

if args and args[0] == "--tous":
    der = passes[-1]
    print(f"\nTous les couples : publies (matin) contre la passe {der.name}, et passe précédente contre {der.name}")
    for f in sorted((der / "a_blanc" / "couples").glob("*.json")):
        c = f.stem
        B = lire(f)
        for nom, A in (("publies", lire(E / "production" / "publies" / f"{c}.json")),
                       ("passe précédente", lire(passes[-2] / "a_blanc" / "couples" / f"{c}.json") if len(passes) > 1 else None)):
            if not A:
                continue
            OA, OB = opps(A), opps(B)
            val = [o for o in OA.values() if valable(o, JOUR)]
            disp = [o for o in val if o["id"] not in OB]
            pct = round(100 * len(disp) / len(val), 1) if val else 0
            za, zb = (A["publier_rapport"].get("zone") or {}).get("code"), (B["publier_rapport"].get("zone") or {}).get("code")
            if pct > 0 or za != zb:
                print(f"  {c:9} {nom:16} disparues {len(disp):3}/{len(val):3} = {pct:5} %"
                      + ("  BLOQUÉ (> 30 % et ≥ 5)" if pct > 30 and len(disp) >= 5 else "  sous le plancher de 5" if pct > 30 else "")
                      + (f"  zone {za} → {zb}" if za != zb else ""))
else:
    for c in args:
        print(f"\n===== {c}")
        pub = lire(E / "production" / "publies" / f"{c}.json")
        envs = [(p.name, lire(p / "a_blanc" / "couples" / f"{c}.json")) for p in passes]
        photo = photographie(c)
        if photo:
            envs = [("photographie du site (V1)", photo)] + envs
        for nom, env in envs:
            print(f"  {nom} : {resume(env)}")
        print(f"  publies (dernier envoi du matin) : {resume(pub)}")
        for (na, ea), (nb, eb) in zip(envs, envs[1:]):
            if ea and eb:
                comparer(na, ea, nb, eb, c, JOUR)
        if envs and envs[-1][1] and pub:
            comparer(envs[-1][0], envs[-1][1], "publies (dernier envoi du matin)", pub, c, JOUR)
