import re
from utils.helpers import log

RE_CODE_QTY = re.compile(r"([A-Za-z0-9_\-]+)\s*[-:]\s*(\d+)\s*(?:UN|UNIDADES|UN)?", re.IGNORECASE)

def parse_message_items(text):
    items = []
    for m in RE_CODE_QTY.finditer(text):
        code = m.group