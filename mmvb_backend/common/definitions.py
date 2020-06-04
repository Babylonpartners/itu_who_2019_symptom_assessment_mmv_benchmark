import json
import os
from enum import Enum


class HealthCheckStatus(Enum):
    OK = "ok"
    BAD_RESPONSE = "bad response"
    TIMEOUT = "timeout"


BIOLOGICAL_SEXES = ["male", "female"]
PRESENT = "present"
ABSENT = "absent"
UNKNOWN = "unsure"
EVIDENCE_STATES = [PRESENT, ABSENT]
TRIAGE_OPTIONS = ["SC", "PC", "EC", "UNCERTAIN"]

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
FIXTURES_DATA = json.load(open(os.path.join(ROOT_DIR, "fixtures/data.json")))
SYMPTOM_ID_TO_SYMPTOMS = {
    symptom["id"]: symptom for symptom in FIXTURES_DATA["symptoms"]
}

OBSERVATION_PROBABILITY = 0.8
UNSURE_PROBABILITY = 0.1
MIN_AGE, MAX_AGE = 18, 80
