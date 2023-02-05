#!/usr/bin/env python3
"""Django's command-line utility for administrative tasks."""
import os
import sys
from scheduler import check_scheduler, threading

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'OSINT.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    thread = threading.Thread(target=check_scheduler)
    thread.daemon=True
    thread.start()

    execute_from_command_line(sys.argv)

    import ctypes
    try:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(thread._thread_id,ctypes.py_object(SystemExit))
        thread.killed=True
    except:
        for tid, t in threading._active.items():
            if t is thread:
                ctypes.pythonapi.PyThreadState_SetAsyncExc(tid,ctypes.py_object(SystemExit))


if __name__ == '__main__':
    main()
