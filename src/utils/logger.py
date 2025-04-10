import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s  - %(message)s",
    # asctime = ASCII Time.
    handlers=[logging.FileHandler("logging/todos.log"), logging.StreamHandler()],
)

logger = logging.getLogger(__name__)
