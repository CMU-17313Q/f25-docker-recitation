from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

MICROSERVICE_LINK = "https://appbox.qatar.cmu.edu/313-teams/team_name/"

TEAM_MENTORS = {"1": "Seckhen", "2": "Aadi",
              "3": "Steve", "4": "Seckhen",
              "5": "Aadi", "6": "Steve"}

@app.get("/team_info/{team_id}")
def get_team_info(team_id: str):

    if team_id is None:
        raise HTTPException(status_code=404, detail="Missing team id")

    team_id = team_id.lower()

    response = requests.get(MICROSERVICE_LINK + team_id)
    # You can check out what the response body looks like in the terminal using the print statement
    data = response.json()
    print(data)

    team_name = data["team_name"]
    
    # TODO Fix this to return correct values for correct team ids.
    if team_id == "1":
        return {
            "team_name": "<name of team 1>",
            "mentor": TEAM_MENTORS[team_id]
        }
    else:
        raise HTTPException(status_code=404, detail="Invalid team id")
