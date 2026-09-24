import json, sys, urllib.request
def search(q):
    body = json.dumps({"page":"1","pageSize":"100","criteria":"C","basicSearch":q,"fOffices":["DE","EM","WO"]}).encode("utf-8")
    req = urllib.request.Request("https://www.tmdn.org/tmview/api/search/results?translate=false", data=body, headers={
        "Content-Type":"application/json","Accept":"application/json",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/128 Safari/537.36",
        "Origin":"https://www.tmdn.org","Referer":"https://www.tmdn.org/tmview/"})
    return json.load(urllib.request.urlopen(req, timeout=60))
for q in sys.argv[1:]:
    try:
        d = search(q)
    except Exception as e:
        print("==", q, "ERROR", e); continue
    tms = d.get("tradeMarks", [])
    print("==", q, "total", d.get("totalResults"))
    for t in tms[:60]:
        nc = t.get("niceClass") or []
        flag = " <<< class 39/44" if any(c in (39,44) for c in nc) else ""
        print(" -", t.get("tmName"), "|", t.get("tmOffice"), "|", t.get("tradeMarkStatus"), "|", nc, "|", t.get("applicantName"), flag)
