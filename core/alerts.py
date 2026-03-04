from core.database import get_last_signal

def should_send_alert(ticker, new_signal):
    last = get_last_signal(ticker)

    if last is None:
        return True

    return last != new_signal