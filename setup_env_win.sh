scriptDir=$(dirname -- "$(readlink -f -- "$BASH_SOURCE")")

python -m venv "$scriptDir/env"

.\env\Scripts\Activate.ps1

python -m pip install -r "$scriptDir/requirements.txt"

python -m ipykernel install --user --name=env

echo "Done!"