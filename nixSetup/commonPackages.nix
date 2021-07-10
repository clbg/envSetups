{pkgs,...}:
{
  packages = with pkgs; [
    htop direnv fortune nodePackages.pyright nodePackages.typescript nodePackages.typescript-language-server
    fzf tmux vim git curl wget rsync nodejs autojump silver-searcher icdiff fzf yarn
  ];
}
