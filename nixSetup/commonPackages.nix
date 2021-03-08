{pkgs,...}:
{
  packages = with pkgs; [
    htop direnv fortune nodePackages.pyright nodePackages.typescript nodePackages.typescript-language-server fzf tmux
    vim git zsh curl wget mosh rsync nodejs autojump silver-searcher icdiff fzf
  ];
}