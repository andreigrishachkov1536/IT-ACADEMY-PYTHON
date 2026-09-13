def error_logs(logs):
    for log in logs:
        if log.startswith("ERROR:"):
            yield log

logs = [
    "INFO: User logged in",
    "ERROR: Database unavailable",
    "INFO: User opened profile",
    "WARNING: Slow response",
    "ERROR: Connection lost",
]

for log in error_logs(logs):
    print(log)