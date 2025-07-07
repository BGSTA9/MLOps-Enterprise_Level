# MLOps-Enterprise_Level

The following you will download, install, and initiate all through your terminal window, for [MAC OS]:

#!/usr/bin/env bash
set -euo pipefail

echo "🚀 Starting Enterprise-Level MLOps Setup on macOS…"

# 1. Install Anaconda
ANACONDA_URL="https://repo.anaconda.com/archive/Anaconda3-2025.06-0-MacOSX-x86_64.sh"
ANACONDA_SCRIPT="${ANACONDA_URL##*/}"
wget --quiet "$ANACONDA_URL" -O "$ANACONDA_SCRIPT"
chmod +x "$ANACONDA_SCRIPT"
./"$ANACONDA_SCRIPT" -b
~/anaconda3/bin/conda init zsh

# 2. Install Homebrew (if missing)
if ! command -v brew &>/dev/null; then
  echo "🔄 Installing Homebrew…"
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi

# 3. Install Git
if ! command -v git &>/dev/null; then
  echo "🔄 Installing Git…"
  brew install git
fi

# 4. Install and switch to latest Bash
BREW_BASH="$(brew --prefix)/bin/bash"
if ! grep -qxF "$BREW_BASH" /etc/shells; then
  echo "🔄 Installing Bash via Homebrew…"
  brew install bash
  sudo sh -c "echo '$BREW_BASH' >> /etc/shells"
fi
if [ "$SHELL" != "$BREW_BASH" ]; then
  chsh -s "$BREW_BASH"
fi

echo "🎉 Setup complete. Restart your Terminal to apply changes."