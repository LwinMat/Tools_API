from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origin = [
    "http://localhost:3000",
    ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


tools = {}

class PopularityData(BaseModel):
    google_search: int
    bing_search: int
    google_trends: int
    stack_overflow: int
    reddit: int
    job_offers: int
    linkedin: int
    twitter: int

    def calculate_score(self):
        score = (
            self.google_search +
            self.bing_search +
            self.google_trends +
            self.stack_overflow +
            self.reddit +
            self.job_offers +
            self.linkedin +
            self.twitter
        )

        return score


class KubernetesTool(BaseModel):
    name: str
    github_url: str
    popularity_data: PopularityData

    def get_popularity_score(self):
        return self.popularity_data.calculate_score()




kube_tools = [
    KubernetesTool(
        name="kubetail",
        github_url="https://github.com/johanhaleby/kubetail",
        popularity_data=PopularityData(
            google_search=100,
            bing_search=120,
            google_trends=10,
            stack_overflow=30,
            reddit=20,
            job_offers=50,
            linkedin=40,
            twitter=90
        )
    ),
    KubernetesTool(
        name="Monokle",
        github_url="https://github.com/kubeshop/monokle",
        popularity_data=PopularityData(
            google_search=100,
            bing_search=140,
            google_trends=40,
            stack_overflow=600,
            reddit=200,
            job_offers=150,
            linkedin=180,
            twitter=190
        )
    ),
    KubernetesTool(
        name="Kudo",
        github_url="https://github.com/kudobuilder/kudo",
        popularity_data=PopularityData(
            google_search=100,
            bing_search=100,
            google_trends=100,
            stack_overflow=100,
            reddit=100,
            job_offers=100,
            linkedin=100,
            twitter=100
        )
    ),
    KubernetesTool(
        name="Bootkube",
        github_url="https://github.com/kubernetes-retired/bootkube",
        popularity_data=PopularityData(
            google_search=100,
            bing_search=100,
            google_trends=100,
            stack_overflow=100,
            reddit=180,
            job_offers=100,
            linkedin=100,
            twitter=100
        )
    ),
    KubernetesTool(
        name="Guard",
        github_url="https://github.com/kubeguard/guard",
        popularity_data=PopularityData(
            google_search=100,
            bing_search=100,
            google_trends=100,
            stack_overflow=100,
            reddit=340,
            job_offers=100,
            linkedin=100,
            twitter=100
        )
    ),
    KubernetesTool(
        name="Kubetail",
        github_url="https://github.com/johanhaleby/kubetail",
        popularity_data=PopularityData(
            google_search=100,
            bing_search=100,
            google_trends=300,
            stack_overflow=180,
            reddit=100,
            job_offers=100,
            linkedin=100,
            twitter=100
        )
    ),
]


@app.get("/")
def index():
    return { "message": "Hello World" }

@app.get("/tools")
def get_tools():
    tools_with_scores = [
        {
            "name": tool.name,
            "github_url": tool.github_url,
            "popularity_data": tool.popularity_data,
            "popularity_score": tool.get_popularity_score()
        }
        for tool in kube_tools
    ]
    return {"tools": tools_with_scores}

# add a post method to add a new tool
@app.post("/add-tool")
def add_tool(tool: KubernetesTool):
    kube_tools.append(tool)
    return { "message": "Tool added successfully" }

# add a get method to get a tool by name
@app.get("/tools/{name}")
def get_tool(name: str):
    for tool in kube_tools:
        if tool.name == name:
            return { "tool": tool }
    return { "message": "Tool not found" }

# add another post method to update a tool
@app.post("/update-tool")
def update_tool(tool: KubernetesTool):
    for i, t in enumerate(kube_tools):
        if t.name == tool.name:
            kube_tools[i] = tool
            return { "message": "Tool updated successfully" }
    return { "message": "Tool not found" }


