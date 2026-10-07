#!/usr/bin/env bash
# Imprime el binario de Orca a usar en esta sesión. No decide si arranca:
# eso lo comprueba quien lo llama.
#
# Contrato para quien lo invoca: reutilizar el binario devuelto durante toda
# la sesión, nunca mezclar dos. Si no arranca, reportar el error exacto y
# parar — no bajar al siguiente de la lista.
set -euo pipefail

if [[ -n "${ORCA_CLI_COMMAND:-}" ]]; then
  echo "$ORCA_CLI_COMMAND"
elif [[ -n "${ORCA_DEV_REPO_ROOT:-}" ]]; then
  echo "orca-dev"
elif [[ "$(uname -s)" == "Linux" ]]; then
  echo "orca-ide"
else
  echo "orca"
fi
