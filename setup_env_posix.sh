scriptDir=$(dirname -- "$(readlink -f -- "$BASH_SOURCE")")

python3 -m venv "$scriptDir/env"

source "$scriptDir/env/bin/activate"

python -m pip install -r "$scriptDir/requirements.txt"

python -m ipykernel install --user --name=env

echo "Done!"
