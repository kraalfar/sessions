import pandas as pd
from datetime import datetime
from datetime import timedelta
import numpy as np
from collections import namedtuple

action = namedtuple('action', ['treshold_time', 'ses_id'])

threshold = {'Backspace': timedelta(minutes=10),
             'Copy': timedelta(minutes=10),
             'Run': timedelta(minutes=30),
             'Paste': timedelta(minutes=10)}


def set_sessions(log, out_log=None):
    data = pd.read_csv(log, names=['action_id', 'timestamp', 'user_id'])
    data.timestamp = data.timestamp.apply(lambda x: datetime.strptime(x.strip(), "%y.%m.%d %H:%M:%S"))
    data.user_id = data.user_id.apply(lambda x: x.strip())
    sessions = np.zeros(len(data)).astype(int)
    last_actions = {}
    cur_session = 0
    for i, row in data.iterrows():
        if row.user_id not in last_actions:
            cur_session += 1
            last_actions[row.user_id] = action(threshold[row.action_id] + row.timestamp, cur_session)
            sessions[i] = cur_session
        else:
            prev_action = last_actions[row.user_id]
            if prev_action.treshold_time > row.timestamp:
                sessions[i] = prev_action.ses_id
                last_actions[row.user_id] = action(threshold[row.action_id] + row.timestamp, prev_action.ses_id)
            else:
                cur_session += 1
                last_actions[row.user_id] = action(threshold[row.action_id] + row.timestamp, cur_session)
                sessions[i] = cur_session

    if out_log is None:
        out_log = 'session_log'

    with open(out_log, 'w') as f:
        for i, row in data.iterrows():
            f.write(f"{row.action_id}, {row.timestamp.strftime('%y.%m.%d %H:%M:%S')}, {row.user_id}, {sessions[i]}\n")


if __name__ == "__main__":
    set_sessions('log')
