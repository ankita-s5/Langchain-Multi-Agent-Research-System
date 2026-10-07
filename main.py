# from src.tools.tools import web_search , scrape_url

# result = scrape_url.invoke({
#     "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11702416"
# })

# print(result)


from src.pipelines.pipeline import run_research_pipeline


topic = "The impact of AI on the job market in 2026"
run_research_pipeline(topic)