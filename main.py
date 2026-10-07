from src.tools.tools import web_search , scrape_url

result = scrape_url.invoke({
    "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11702416"
})

print(result)