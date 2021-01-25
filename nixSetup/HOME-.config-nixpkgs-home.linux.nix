{ config, pkgs, ... }:

{
  home.packages = [
    pkgs.htop
    pkgs.direnv
    pkgs.fortune
  ];


  # Let Home Manager install and manage itself.
  programs.home-manager.enable = true;
  home.username = "$USER";
  home.homeDirectory = "$HOME"

  # This value determines the Home Manager release that your
  # configuration is compatible with. This helps avoid breakage
  # when a new Home Manager release introduces backwards
  # incompatible changes.
  #
  # You can update Home Manager without changing this value. See
  # the Home Manager release notes for a list of state version
  # changes in each release.
  home.stateVersion = "21.03";

  #lorri
  services.lorri.enable = true;
}
