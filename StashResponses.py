class StashResponses:
    def __init__(self, json):
        self.stashResponses = []
        self.nextChangeId = json['next_change_id']
        for stash in json['stashes']:
            self.stashResponses.append(StashResponse(stash))

class StashResponse:
    def __init__(self, json):
        self.id = json["id"]
        self.lastCharacterName = json["lastCharacterName"]
        self.lastCharacterName = json["lastCharacterName"]
        self.lastCharacterName = json["lastCharacterName"]
        self.lastCharacterName = json["lastCharacterName"]
