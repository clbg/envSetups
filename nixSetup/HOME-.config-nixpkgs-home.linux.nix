{ config, pkgs, ... }:
let
   commonPackages = (import ~/envSetups/nixSetup/commonPackages.nix) { inherit pkgs; };
in
{
  programs.home-manager.enable = true;
  home.username = "$USER";
  home.homeDirectory = "/home/$USER";

  home.packages =   commonPackages.packages ++ [ ];

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
