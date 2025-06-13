from Wappalyzer import Wappalyzer, WebPage

def detect_with_wappalyzer(url):
    try:
        webpage = WebPage.new_from_url(url)
        wappalyzer = Wappalyzer.latest()
        technologies = wappalyzer.analyze(webpage)
        return set(technologies)
    except Exception as e:
        return {"error": f"Technology detection failed: {str(e)}"}
