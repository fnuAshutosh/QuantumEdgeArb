# Setup & Development Workflow
This document expands on the README and gives concrete steps for getting
started with the QuantumEdgeArb project.

## Prerequisites
* **OS:** Tested on Linux/WSL2, macOS, Windows (with mingw/MSVC).
* **C++ toolchain:** CMake 3.20+, clang 14+/gcc 11+ or MSVC 2019+.
* **Python:** 3.11+ with `venv`.
* **Gemini CLI** (or another LLM CLI) installed and on `PATH`.
* **gsd** helper: install one of the wrappers below depending on your ecosystem:
  * Python package – `pip install gsd` (current examples in this repo use that).
  * Node.js shim – `npx get-shit-done-cc@latest` (works identically from a fresh checkout).
  * Alternatively clone `gsd-build/get-shit-done` and run `python -m gsd`.
* **VS Code** (optional) with recommended extensions (see `.vscode`).

## First-time build
```bash
git clone https://your.repo.url/QuantumEdgeArb.git
cd QuantumEdgeArb
gsd deps          # installs Python packages and compiles C++
```

## Working with the code
* `gsd build` – compile C++ in `build/` directory.
* `gsd lint` – auto‑format C++ and check Python syntax.
* `gsd test` – run unit tests under `build/`.
* `gsd context` – refresh Gemini/LLM context with current tree.

### Gemini integration
The repository ships `PROMPT.md` and a minimal `.gemini` file with
ignore rules. Running `gsd context` uploads both to Gemini, so chat
sessions automatically include repo-specific text.

VS Code users benefit from preconfigured tasks: open **Terminal → Run
Task…** or use the keybindings **Ctrl+Alt+B/T/C** (build/test/context).
The `gsd context` task runs automatically whenever the workspace
opens, keeping the LLM prompt fresh. Copilot inline and chat suggestions
are enabled in this workspace by default.

### Terraform and infrastructure
Objects like the MSK topic, SageMaker model and Step Function are defined
in `infra/terraform`. To provision them (requires AWS credentials):

```bash
cd infra/terraform
tfenv install # or terraform init
terraform apply -auto-approve
```

Destroy the resources after your demo to avoid charges:

```bash
terraform destroy -auto-approve
```

### Data sources
You can fetch sample historical data or stream live quotes using the
data fetcher:

```bash
# download a small CSV
gsd data:fetch

# or start a live stream
python data_ingestion/fetch_data.py --pair NVDA-TSM --source yfinance
```

### Adding new tools
If you prefer `make`, `just`, or `taskfile`, feel free to replicate the
commands from `gsd.yml`. The important part is that all contributors
document the same entry points.
