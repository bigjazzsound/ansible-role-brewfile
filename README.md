brewfile
=========

Manages a Brewfile used by Homebrew's `brew bundle` command

Role Variables
--------------

```yaml
# An object representing a Brewfile

# Default
brew_packages: []

brew_packages:
  taps:
    - "homebrew/cask"
  brews:
    - "bash"
    - name: "neovim"
      opts:
        link: "false"
        args:
          - "HEAD"
          - "only-dependencies"
    - name: "tmux"
      conditional: if OS.mac?
  casks:
    - "alfred"
  apps:
    - name: "Xcode"
      id: 497799835
  whalebrew:
    - "whalebrew/wget"
```

```yaml
# The location to put the Brewfile
brew_brewfile: ~/.Brewfile
```

Example Playbook
----------------

```yaml
- hosts: all
  ansible.builtin.include_role:
     - name: brewfile
```

License
-------

BSD
