#!/usr/bin/env bash

COMMAND="${1:-run}"

MIGRATE_PAUSE=5

if [[ "${COMMAND}" == "run" ]]; then
  sleep 60
  python manage.py runserver 0.0.0.0:8000
elif [[ "${COMMAND}" == "run-with-auto-restart" ]]; then
  while true; do
    python manage.py runserver 0.0.0.0:8000
    echo
    echo "One more attempt to start App in ${MIGRATE_PAUSE} seconds."
    sleep 5
  done
elif [[ "${COMMAND}" == "migrate" ]]; then
  for _ in {1..12}; do
    python manage.py migrate
    RET_CODE=${?}
    if [[ "${RET_CODE}" == "0" ]]; then
      break;
    else
      echo
      echo "One more attempt to run migrations in ${MIGRATE_PAUSE} seconds."
      sleep ${MIGRATE_PAUSE}
    fi
  done
else
  echo "ERROR: Unknown command"
  exit 1
fi
