#!/usr/bin/env python3
# Created by Yevgeniy Goncharov, https://lab.sys-adm.in
# Send HUP signal to a specified process

import argparse
import os
import signal
import subprocess


def find_pid(process_name):
    try:
        pid = subprocess.check_output(['pgrep', process_name])
        return int(pid.strip())
    except subprocess.CalledProcessError:
        print(f"Процесс {process_name} не найден.")
        return None


def send_hup_signal(pid):
    try:
        os.kill(pid, signal.SIGHUP)
        print(f"Сигнал HUP отправлен процессу с PID {pid}.")
    except ProcessLookupError:
        print(f"Процесс с PID {pid} не найден.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Отправка сигнала HUP процессу по имени.")
    parser.add_argument("process_name", help="Имя процесса.")
    args = parser.parse_args()

    process_pid = find_pid(args.process_name)
    if process_pid:
        send_hup_signal(process_pid)
